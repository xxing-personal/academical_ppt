from pydantic import BaseModel
from typing import List, Dict

class ImageData(BaseModel):
    page: int
    index: int
    format: str
    data: str

class PDFUploadResponse(BaseModel):
    filename: str
    text: str
    num_pages: int
    images: List[ImageData]
    message: str 