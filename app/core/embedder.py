from sentence_transformers import SentenceTransformer

model = SentenceTransformer('all-MiniLM-L6-v2')  # Lightweight + semantic similarity

def embed_text_chunks(chunks):
    embeddings = model.encode([chunk['text'] for chunk in chunks], show_progress_bar=True)
    return embeddings
