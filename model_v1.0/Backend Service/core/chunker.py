from typing import List

def chunk_text(text: str, max_tokens: int) -> List[str]:
    import nltk
    from nltk.tokenize import sent_tokenize
    nltk.download('punkt', quiet=True)

    sentences = sent_tokenize(text)
    chunks, buffer, token_count = [], [], 0

    for sentence in sentences:
        tokens = sentence.split()
        if token_count + len(tokens) > max_tokens:
            chunks.append(" ".join(buffer))
            buffer = [sentence]
            token_count = len(tokens)
        else:
            buffer.append(sentence)
            token_count += len(tokens)

    if buffer:
        chunks.append(" ".join(buffer))

    return chunks
