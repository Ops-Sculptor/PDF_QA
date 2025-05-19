from app.core.chunker import chunk_text_by_sentences

def test_chunking():
    text = "This is sentence one. This is sentence two. This is sentence three."
    chunks = chunk_text_by_sentences(text, max_tokens=10)
    assert isinstance(chunks, list)
    assert len(chunks) > 0
