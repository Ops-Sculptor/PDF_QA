# README.md

## 📘 Multimodal RAG Pipeline for PDF & Visual Question Answering

This system enables question answering from PDF documents using both textual and visual (image-based) content. It leverages open-source LLMs, LangChain, Sentence Transformers, BLIP, and FAISS for fast retrieval and multimodal response generation.

---

## 📐 System Architecture

```mermaid
graph TD
    A[User Uploads PDF / Image + Question] -->|UI| B(Streamlit)
    B -->|Sends to| C(FastAPI Backend)
    C --> D(PDF Parser: text + images)
    D --> E(Text Chunker)
    E --> F(Embedding Generator)
    F --> G(FAISS Vector Store)
    D --> H(Image Captioning: BLIP)
    G --> I(LangChain RetrievalQA)
    H --> I
    I --> J(Final Answer)
    J -->|Displays in UI| B
```

---

## ⚙️ Set-Up and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/Ops-Sculptor/PDF_QA.git
cd multimodal-rag-pipeline
```

### 2. Install Dependencies
Make sure you have Python 3.10 or higher.
```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### 3. Install NLTK Tokenizer (first run only)
```python
import nltk
nltk.download('punkt')
```

### 4. Start the Backend (FastAPI)
```bash
uvicorn main:app --reload
```

### 5. Start the Frontend (Streamlit)
```bash
streamlit run ui.py
```

### Directory Structure:
```
project/
├── main.py                # FastAPI backend
├── ui.py                  # Streamlit frontend
├── pipeline.py            # End-to-end orchestrator
├── pdf_parser.py          # PDF text and image extraction
├── chunker.py             # Sentence-based text chunking
├── embedder.py            # Sentence Transformer embedding
├── vector_store.py        # FAISS storage and retrieval
├── qa_engine.py           # LangChain QA generation
├── vqa.py                 # Visual Question Answering (BLIP)
├── config.py              # Configuration constants
├── test_pipeline.py       # Unit and integration tests
├── requirements.txt       # Python dependencies
└── sample_data/           # Sample PDF and images for testing
```

---

## 🔌 API Usage

### 📤 POST `/process/`
Submit a PDF + text query and receive an answer.

#### Request:
- **Content-Type:** `multipart/form-data`
- **Parameters:**
  - `file`: PDF file
  - `query`: Textual question

#### Sample Code:
```python
import requests

files = {"file": open("sample.pdf", "rb")}
data = {"query": "What is the conclusion?"}
response = requests.post("http://localhost:8000/process/", files=files, data=data)
print(response.json())
```

#### Response:
```json
{
  "answer": "The document concludes with..."
}
```

---

## ✅ Features
- PDF text extraction and chunking
- Embedding with SentenceTransformers
- Visual image captioning with BLIP
- LangChain + Ollama RetrievalQA
- Fast and scalable with FAISS
- UI via Streamlit
- API via FastAPI

---

## 🧪 Testing
Run all unit and integration tests:
```bash
pytest test_pipeline.py --disable-warnings
```

Ensure `test_doc.pdf` and `test_image.jpg` are present in `sample_data/`.

---

## 🚀 To-Do / Roadmap
- [ ] Add support for image-based question routing
- [ ] Enhance OCR for scanned PDFs
- [ ] Deploy with Docker
- [ ] Add feedback ranking and retraining loop

---

## 👨‍💻 Author
Developed with precision for OceanAI Assignment. For Evaluation Assignment.
---
