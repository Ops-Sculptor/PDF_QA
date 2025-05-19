import streamlit as st
import requests
from PIL import Image
import io

st.title("📄 OceanAI PDF Question Answering")

uploaded_file = st.file_uploader("Upload PDF", type="pdf")
question = st.text_input("Ask a question")

if uploaded_file:
    st.success("PDF uploaded. Now you can ask a question.")

    if question:
        with st.spinner("Processing..."):
            response = requests.post("http://localhost:8000/upload-pdf/", files={"file": uploaded_file})
            st.write("✅ PDF processed")

            response = requests.post("http://localhost:8000/query", json={"question": question})
            st.subheader("Answer:")
            st.markdown(response.json()["answer"])
