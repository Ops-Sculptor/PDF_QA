import fitz
from typing import List, Dict

def extract_pdf_content(pdf_path: str) -> Dict[str, List]:
    doc = fitz.open(pdf_path)
    full_text, image_blobs = [], []
    for page in doc:
        full_text.append(page.get_text())
        for img in page.get_images(full=True):
            xref = img[0]
            base_img = doc.extract_image(xref)
            image_blobs.append(base_img["image"])
    return {"text": "\n".join(full_text), "images": image_blobs}
