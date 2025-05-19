import fitz     #PyMuPDF

def extract_text_and_images(file_bytes: bytes):
    doc = fitz.open(stream=file_bytes, filetype="pdf")
    text_chunks = []
    images = []

    for page_num, page in enumerate(doc):
        text = page.get_text()
        text_chunks.append({"page": page_num + 1, "text": text})

        for img_index, img in enumerate(page.get_images(full=True)):
            xref = img[0]
            base_image = doc.extract_image(xref)
            images.append({
                "page": page_num + 1,
                "image_bytes": base_image["image"],
                "ext": base_image["ext"]
            })

    return {"text_chunks": text_chunks, "images": images}
