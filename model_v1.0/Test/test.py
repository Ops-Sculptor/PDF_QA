import os
import tempfile
import pytest
from fastapi.testclient import TestClient
from Backend_Service.main import app
from Backend_Service.core.pipeline import run_pipeline
from Backend_Service.core.vqa import caption_image

client = TestClient(app)

@pytest.fixture
def sample_pdf():
    path = os.path.join(os.path.dirname(__file__), "sample_data", "test_doc.pdf")
    assert os.path.exists(path), "Test PDF not found."
    return path

@pytest.fixture
def sample_image():
    path = os.path.join(os.path.dirname(__file__), "sample_data", "test_image.jpg")
    assert os.path.exists(path), "Test image not found."
    with open(path, "rb") as img:
        yield img.read()

@pytest.fixture
def valid_query():
    return "What does the image show?"

def test_caption_image(sample_image):
    caption = caption_image(sample_image)
    assert isinstance(caption, str), "Caption output is not a string."
    assert len(caption.strip()) > 0, "Empty caption returned."
    assert any(word in caption.lower() for word in ["diagram", "chart", "figure", "image", "photo"]), "Caption seems unrelated to visual content."

def test_run_pipeline(sample_pdf, valid_query):
    result = run_pipeline(sample_pdf, valid_query)
    assert isinstance(result, str), "Pipeline output is not a string."
    assert len(result.strip()) > 0, "Pipeline returned empty response."

def test_api_process_endpoint(sample_pdf, valid_query):
    with open(sample_pdf, "rb") as file:
        response = client.post(
            "/process/",
            files={"file": (os.path.basename(sample_pdf), file, "application/pdf")},
            data={"query": valid_query}
        )
        assert response.status_code == 200, f"Unexpected status code: {response.status_code}"
        data = response.json()
        assert "answer" in data, "Missing 'answer' in API response."
        assert isinstance(data["answer"], str), "Answer is not a string."
        assert len(data["answer"]) > 0, "Empty answer returned."

def test_api_error_handling():
    response = client.post("/process/", data={"query": "Incomplete input"})
    assert response.status_code == 422, "API did not validate missing file input."