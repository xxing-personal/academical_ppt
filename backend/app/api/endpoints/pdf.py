import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.pdf import PDFResponse
from app.schemas.presentation import PresentationResponse
from app.utils.pdf_processor import save_upload_file, extract_text_from_pdf
from app.services.openai_service import generate_presentation_content
from app.core.config import get_settings

router = APIRouter()
settings = get_settings()

@router.post("/upload", response_model=PDFResponse)
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF file and extract its text and images.
    """
    try:
        # Save the uploaded file
        upload_dir = os.path.join(settings.UPLOAD_DIR, "pdfs")
        file_path = await save_upload_file(file, upload_dir)
        
        # Process the PDF
        text, num_pages, images = extract_text_from_pdf(file_path)
        
        return PDFResponse(
            filename=file.filename,
            text=text,
            num_pages=num_pages,
            images=images
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@router.post("/generate_presentation", response_model=PresentationResponse)
async def generate_presentation(file: UploadFile = File(...)):
    """
    Upload a PDF file, extract its text, and generate a presentation outline using GPT-4.
    """
    try:
        # Save and process the PDF
        upload_dir = os.path.join(settings.UPLOAD_DIR, "pdfs")
        file_path = await save_upload_file(file, upload_dir)
        text, _, _ = extract_text_from_pdf(file_path)
        
        # Generate presentation content using GPT
        presentation_content = generate_presentation_content(text)
        
        return PresentationResponse(
            content=presentation_content,
            message="Presentation content generated successfully"
        )
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 