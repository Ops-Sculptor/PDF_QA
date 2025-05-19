from fastapi import APIRouter, UploadFile, File
from app.core.pdf_parser import extract_text_and_images

router = APIRouter()

@router.post("/upload-pdf/")
async def upload_pdf(file: UploadFile = File()):
    contents = await file.read()
    result = extract_text_and_images(contents)
    return {"status": "parsed", "pages": len(result['text_chunks']), "images_found": len(result['images'])}
