from langchain.chains import RetrievalQA
from langchain.llms import Ollama
from langchain.vectorstores import Chroma
from langchain.embeddings import HuggingFaceEmbeddings
from app.core.retriever import retrieve_context

def get_answer(query: str):
    # Get top-k chunks
    context = retrieve_context(query)
    top_chunks = [doc for doc in context["documents"][0]]

    prompt = "Context:\n" + "\n".join(top_chunks) + f"\n\nQuestion: {query}\nAnswer:"
    llm = Ollama(model="llama3")
    answer = llm(prompt)
    return answer
