# 📄 OceanAI – Multimodal PDF Question Answering using RAG

## 🧩 Overview
> OceanAI is a comprehensive, modular system built to perform question answering on PDF documents by combining text and visual content understanding. It uses a Retrieval-Augmented Generation (RAG) architecture with LangChain and Ollama, integrates sentence-level semantic chunking, and supports basic Visual Question Answering (VQA) via image captioning. The frontend is built with Streamlit for user interaction, and the backend is implemented in FastAPI for API orchestration.

This solution reflects a practical approach suitable for junior engineers and data science interns, focused on clean design, modular logic, and lightweight open-source tools.

## 🎯 Objective
> To develop a robust RAG pipeline using LangChain and Ollama, capable of extracting structured data from PDFs and answering both text and image-based user queries, with a clean interface and scalable backend design.

## ⚙️ Tech Stack
- **Frontend**: Streamlit
- **Backend**: FastAPI
- **PDF Parsing**: PyMuPDF, unstructured
- **Chunking**: NLTK sentence tokenizer + token limit logic
- **Embeddings**: Sentence Transformers (MiniLM)
- **Vector DB**: ChromaDB with metadata
- **LLM Engine**: Ollama (LLaMA3 or similar)
- **VQA**: BLIP captioning (Hugging Face)
- **Testing**: Pytest

## 🔧 Features
- Upload structured PDF files with paragraphs, tables, and images.
- Automatically parse PDF and chunk text semantically.
- Generate embeddings from each chunk for semantic similarity search.
- Store text chunks with metadata in ChromaDB for efficient retrieval.
- Retrieve relevant context using LangChain RetrievalQA.
- Answer user queries using local LLM (via Ollama).
- Extract images and caption them using BLIP for basic VQA.
- Display answers and relevant PDF context in Streamlit interface.

## 🏗️ Architecture

```
User → Streamlit UI → FastAPI API
          ↓
     PDF Upload
          ↓
  PDF Parser (Text + Images)
          ↓
    Text Chunker (Semantic Units)
          ↓
Embedding → ChromaDB (w/ Metadata)
          ↓
       LangChain RAG
      ↙             ↘
 VQA Caption       Query
    ↘                ↓
     Merged Prompt → LLM → Answer
```

## 🚀 Running the Project

### 1. Install Dependencies
```bash
pip install -r requirements.txt
```

### 2. Start Backend
```bash
uvicorn app.main:app --reload
```

### 3. Start Frontend
```bash
streamlit run streamlit_app/ui.py
```

> Ensure Ollama is installed and the local LLM model is running (e.g., `ollama run llama3`).

## 📦 Folder Structure

```
OceanAI_Project/
├── app/
│   ├── core/
│   ├── api/
│   └── main.py
├── streamlit_app/
├── tests/
├── requirements.txt
└── README.md
```

## ✅ Testing

Run unit tests:
```bash
pytest tests/
```

Test coverage includes:
- Chunking logic
- Embedding generation
- Vector retrieval
- VQA caption output

## 📌 Known Limitations

- VQA only supports static image captioning
- No visual highlighting on PDF or image
- Backend and frontend are not containerized
- No user authentication or session management

## 🌱 Future Improvements

- Advanced VQA integration with region detection
- PDF page number + section highlighting in answers
- Dockerized backend + frontend for production
- Cloud vector store support (Qdrant, Pinecone)

## 👨‍💻 Author
Built by a junior software engineer with a background in microservices and a data science traineeship, this project emphasizes practical, modular, and testable design suitable for entry-level deployment and learning showcase.
