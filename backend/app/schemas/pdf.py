from pydantic import BaseModel, ConfigDict
from typing import List, Dict

class ImageData(BaseModel):
    page: int
    index: int
    format: str
    data: str

class PDFResponse(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    filename: str
    text: str
    num_pages: int
    images: List[Dict[str, str]]

class PDFUploadResponse(BaseModel):
    filename: str
    text: str
    num_pages: int
    images: List[ImageData]
    message: str 