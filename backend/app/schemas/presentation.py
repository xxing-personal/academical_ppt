from pydantic import BaseModel
from typing import List

class Slide(BaseModel):
    title: str
    points: List[str]

class PresentationContent(BaseModel):
    title: str
    slides: List[Slide]

class PresentationResponse(BaseModel):
    content: PresentationContent
    message: str = "Presentation content generated successfully" 