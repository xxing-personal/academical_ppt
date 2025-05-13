import os
import pytest
from fastapi.testclient import TestClient
from app.main import app
from app.core.config import get_settings

settings = get_settings()
client = TestClient(app)

def test_generate_presentation_success():
    # Test with a sample PDF file
    test_file_path = os.path.join(os.path.dirname(__file__), "test_paper.pdf")
    
    with open(test_file_path, "rb") as f:
        response = client.post(
            "/api/v1/pdf/generate_presentation",
            files={"file": ("test_paper.pdf", f, "application/pdf")}
        )
    
    assert response.status_code == 200
    data = response.json()
    
    # Check response structure
    assert "content" in data
    assert "message" in data
    assert data["message"] == "Presentation content generated successfully"
    
    # Check presentation content structure
    content = data["content"]
    assert "title" in content
    assert "slides" in content
    assert isinstance(content["slides"], list)
    
    # Check slides structure
    for slide in content["slides"]:
        assert "title" in slide
        assert "points" in slide
        assert isinstance(slide["points"], list)
        assert len(slide["points"]) > 0

def test_generate_presentation_invalid_file():
    # Test with a non-PDF file
    test_file_path = os.path.join(os.path.dirname(__file__), "test.txt")
    
    with open(test_file_path, "w") as f:
        f.write("This is a test file")
    
    with open(test_file_path, "rb") as f:
        response = client.post(
            "/api/v1/pdf/generate_presentation",
            files={"file": ("test.txt", f, "text/plain")}
        )
    
    assert response.status_code == 400
    assert "Only PDF files are allowed" in response.json()["detail"]

def test_generate_presentation_no_file():
    # Test without file
    response = client.post("/api/v1/pdf/generate_presentation")
    assert response.status_code == 422  # Validation error

def test_generate_presentation_empty_file():
    # Test with empty PDF
    test_file_path = os.path.join(os.path.dirname(__file__), "empty.pdf")
    
    with open(test_file_path, "wb") as f:
        f.write(b"")
    
    with open(test_file_path, "rb") as f:
        response = client.post(
            "/api/v1/pdf/generate_presentation",
            files={"file": ("empty.pdf", f, "application/pdf")}
        )
    
    assert response.status_code == 500
    assert "Error processing PDF" in response.json()["detail"] 