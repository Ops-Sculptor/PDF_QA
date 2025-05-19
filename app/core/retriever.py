from app.core.embedder import model
from app.core.vector_store import retrieve_similar_chunks

def retrieve_context(query: str, k: int = 3):
    query_embedding = model.encode([query])[0]
    result = retrieve_similar_chunks(query_embedding, k=k)
    return result