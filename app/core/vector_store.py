import chromadb
from chromadb.config import Settings
from chromadb.utils import embedding_functions

client = chromadb.Client(Settings(chroma_db_impl="duckdb+parquet", persist_directory="./chroma_store"))
collection = client.get_or_create_collection(name="pdf_chunks")

def add_documents_to_vector_db(chunks, embeddings):
    for i, chunk in enumerate(chunks):
        collection.add(
            ids=[f"chunk_{i}"],
            embeddings=[embeddings[i]],
            documents=[chunk["text"]],
            metadatas=[{"page": chunk["page"]}]
        )

def retrieve_similar_chunks(query_embedding, k=3):
    results = collection.query(query_embeddings=[query_embedding], n_results=k)
    return results
