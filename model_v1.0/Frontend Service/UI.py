import streamlit as st
import requests
from PIL import Image
import io

st.set_page_config(page_title="PDF + Image QA", layout="wide")
st.title("Multimodal PDF Question Answering")

st.sidebar.title("Upload Inputs")
uploaded_pdf = st.sidebar.file_uploader("Upload a PDF", type=["pdf"])
uploaded_image = st.sidebar.file_uploader("Upload an Image (optional)", type=["jpg", "jpeg", "png"])
question = st.sidebar.text_input("Enter your question")
submit_btn = st.sidebar.button("Submit")

if submit_btn:
    if not uploaded_pdf:
        st.warning("You need to upload a PDF file.")
    elif not question:
        st.warning("Please type your question.")
    else:
        with st.spinner("Processing your request..."):
            try:
                
                pdf_bytes = uploaded_pdf.read()
                files = {"file": (uploaded_pdf.name, pdf_bytes, uploaded_pdf.type)}
                data = {"query": question}

                
                response = requests.post("http://localhost:8000/process/", files=files, data=data)

                
                if response.status_code == 200:
                    result = response.json()

                    
                    st.success("Answer generated successfully!")
                    st.subheader("Answer:")
                    st.write(result.get("answer", "No answer found."))

                    
                    if uploaded_image:
                        st.subheader("Uploaded Image")
                        image = Image.open(uploaded_image)
                        st.image(image, use_column_width=True)
                else:
                    try:
                        error_detail = response.json().get("error", "Unknown error.")
                    except Exception:
                        error_detail = response.text
                    st.error(f"Server returned an error: {error_detail}")
            except Exception as e:
                st.error(f"An error occurred: {str(e)}")

st.markdown("---")
st.caption("Built using Streamlit and FastAPI. Supports both textual and visual PDF QA.")