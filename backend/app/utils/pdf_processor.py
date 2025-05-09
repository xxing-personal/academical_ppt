import fitz  # PyMuPDF
import os
from typing import Tuple, List, Dict
from fastapi import UploadFile, HTTPException
import base64
from io import BytesIO

async def save_upload_file(upload_file: UploadFile, upload_dir: str) -> str:
    """Save the uploaded file to the specified directory."""
    try:
        # Create the upload directory if it doesn't exist
        os.makedirs(upload_dir, exist_ok=True)
        
        # Create the file path
        file_path = os.path.join(upload_dir, upload_file.filename)
        
        # Save the file
        with open(file_path, "wb") as f:
            content = await upload_file.read()
            f.write(content)
            
        return file_path
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