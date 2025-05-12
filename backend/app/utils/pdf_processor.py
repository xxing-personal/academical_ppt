import fitz  # PyMuPDF
import os
from typing import Tuple, List, Dict
from fastapi import UploadFile, HTTPException
import base64
from io import BytesIO
from app.core.config import get_settings

settings = get_settings()

async def validate_file(file: UploadFile) -> None:
    """Validate the uploaded file."""
    # Check file type
    if file.content_type not in settings.ALLOWED_FILE_TYPES:
        raise HTTPException(
            status_code=400,
            detail=f"Invalid file type. Allowed types: {', '.join(settings.ALLOWED_FILE_TYPES)}"
        )
    
    # Check file size
    file_size = 0
    chunk_size = 1024 * 1024  # 1MB chunks
    
    while chunk := await file.read(chunk_size):
        file_size += len(chunk)
        if file_size > settings.MAX_UPLOAD_SIZE:
            raise HTTPException(
                status_code=400,
                detail=f"File size exceeds maximum limit of {settings.MAX_UPLOAD_SIZE / (1024 * 1024)}MB"
            )
    
    # Reset file pointer
    await file.seek(0)

async def save_upload_file(upload_file: UploadFile, upload_dir: str) -> str:
    """Save the uploaded file to the specified directory."""
    try:
        # Validate file before saving
        await validate_file(upload_file)
        
        # Create the upload directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)
        
        # Create the file path
        file_path = os.path.join(upload_dir, upload_file.filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            content = await upload_file.read()
            f.write(content)
            
        return file_path
    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error saving file: {str(e)}")

def extract_images_from_pdf(doc: fitz.Document) -> List[Dict[str, str]]:
    """Extract images from a PDF document and return them as base64 encoded strings."""
    images = []
    
    for page_num in range(len(doc)):
        page = doc[page_num]
        image_list = page.get_images(full=True)
        
        for img_index, img in enumerate(image_list):
            try:
                xref = img[0]
                base_image = doc.extract_image(xref)
                image_bytes = base_image["image"]
                
                # Convert to base64
                image_base64 = base64.b64encode(image_bytes).decode()
                
                # Get image format
                image_format = base_image["ext"]
                
                images.append({
                    "page": page_num + 1,
                    "index": img_index + 1,
                    "format": image_format,
                    "data": f"data:image/{image_format};base64,{image_base64}"
                })
            except Exception as e:
                print(f"Error extracting image {img_index} from page {page_num + 1}: {str(e)}")
                continue
    
    return images

def extract_text_from_pdf(file_path: str) -> Tuple[str, int, List[Dict[str, str]]]:
    """Extract text and images from a PDF file and return the text, number of pages, and images."""
    try:
        # Open the PDF file
        doc = fitz.open(file_path)
        
        # Extract text from all pages
        text = ""
        for page in doc:
            text += page.get_text()
            
        # Get the number of pages
        num_pages = len(doc)
        
        # Extract images
        images = extract_images_from_pdf(doc)
        
        # Close the document
        doc.close()
        
        return text, num_pages, images
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error processing PDF: {str(e)}")
    finally:
        # Clean up the temporary file
        try:
            os.remove(file_path)
        except:
            pass 