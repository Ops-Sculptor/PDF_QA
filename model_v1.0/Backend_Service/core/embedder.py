import numpy as np
from typing import List
from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')

def embed_chunks(chunks: List[str]) -> np.ndarray:
    return model.encode(chunks, show_progress_bar=True)
