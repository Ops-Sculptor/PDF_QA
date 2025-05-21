from typing import List
from langchain.vectorstores import FAISS
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.docstore.document import Document
from utils.config import EMBEDDING_MODEL, FAISS_INDEX_PATH

embedding_function = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL)

def create_vector_store(chunks: List[str]) -> FAISS:
    docs = [Document(page_content=chunk) for chunk in chunks]
    vector_db = FAISS.from_documents(docs, embedding_function)
    vector_db.save_local(FAISS_INDEX_PATH)
    return vector_db

def load_vector_store() -> FAISS:
    return FAISS.load_local(FAISS_INDEX_PATH, embedding_function)
