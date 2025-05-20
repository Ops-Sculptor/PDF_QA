from utils.config import CHUNK_SIZE
from pdf_parser import extract_pdf_content
from chunker import chunk_text
from embedder import embed_chunks
from vector_store import create_vector_store
from vqa import caption_image
from qa_engine import answer_query

def run_pipeline(pdf_path: str, user_question: str) -> str:
    print("[INFO] Parsing PDF...")
    data = extract_pdf_content(pdf_path)

    print("[INFO] Chunking text...")
    chunks = chunk_text(data['text'], CHUNK_SIZE)

    print("[INFO] Generating embeddings...")
    embeddings = embed_chunks(chunks)

    print("[INFO] Storing vectors...")
    vector_db = create_vector_store(chunks)

    print("[INFO] Processing images...")
    captions = [caption_image(img) for img in data['images']]

    print("[INFO] Running QA...")
    return answer_query(user_question, vector_db, image_captions=captions)
