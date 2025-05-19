import nltk
from typing import List
from nltk.tokenize import sent_tokenize

nltk.download('punkt')

def chunk_text_by_sentences(text: str, max_tokens: int = 300) -> List[str]:
    sentences = sent_tokenize(text)
    chunks, current_chunk = [], []

    token_count = 0
    for sent in sentences:
        tokens = sent.split()
        if token_count + len(tokens) > max_tokens:
            chunks.append(" ".join(current_chunk))
            current_chunk = [sent]
            token_count = len(tokens)
        else:
            current_chunk.append(sent)
            token_count += len(tokens)

    if current_chunk:
        chunks.append(" ".join(current_chunk))
    return chunks
