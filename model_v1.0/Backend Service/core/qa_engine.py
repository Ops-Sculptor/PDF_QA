from langchain.chains import RetrievalQA
from langchain.llms import Ollama

def answer_query(query: str, vector_db, image_captions=None) -> str:
    if image_captions:
        visual_context = "\n".join(image_captions)
        query = f"Visual Context:\n{visual_context}\n\nQuestion: {query}"

    retriever = vector_db.as_retriever(search_kwargs={"k": 5})
    qa = RetrievalQA.from_chain_type(llm=Ollama(model="llama3"), retriever=retriever)
    return qa.run(query)