import os
from fastapi import APIRouter, UploadFile, File, HTTPException
from app.schemas.pdf import PDFUploadResponse
from app.utils.pdf_processor import save_upload_file, extract_text_from_pdf

router = APIRouter()

@router.post("/upload_pdf", response_model=PDFUploadResponse)
async def upload_pdf(file: UploadFile = File(...)):
    # Validate file type
    if not file.filename.lower().endswith('.pdf'):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed"
        )
    
    # Get the upload directory path
    upload_dir = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), "uploads")
    
    try:
        # Save the uploaded file
        file_path = await save_upload_file(file, upload_dir)
        
        # Extract text and images from the PDF
        text, num_pages, images = extract_text_from_pdf(file_path)
        
        return PDFUploadResponse(
            filename=file.filename,
            text=text,
            num_pages=num_pages,
            images=images,
            message="PDF processed successfully"
        )
    except HTTPException as e:
        raise e
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"An error occurred while processing the PDF: {str(e)}"
        ) 