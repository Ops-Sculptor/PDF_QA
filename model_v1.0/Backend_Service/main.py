from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
from core.pipeline import run_pipeline
import os
import shutil
import traceback

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

UPLOAD_DIR = "temp_uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/process/")
def process_pdf(
    file: UploadFile = File(...),
    query: str = Form(...),
    image: UploadFile = File(None)
):
    try:
        pdf_path = os.path.join(UPLOAD_DIR, file.filename)
        with open(pdf_path, "wb") as f:
            shutil.copyfileobj(file.file, f)

        image_bytes = None
        if image:
            image_bytes = image.file.read()

        answer = run_pipeline(pdf_path, query, image_bytes)

        return JSONResponse(content={"answer": answer})
      
    except Exception as e:
     traceback.print_exc()
     return JSONResponse(status_code=500, content={"error": str(e)})
