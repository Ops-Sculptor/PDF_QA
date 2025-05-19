from fastapi import FastAPI
from app.api import endpoints

app = FastAPI(
    title="OceanAI PDF RAG System",
    description="Rag PDF-based question answering system",
    version="1.0"
)

app.include_router(endpoints.router)
