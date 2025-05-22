from openai import OpenAI
from app.core.config import get_settings
from app.schemas.presentation import PresentationContent, Slide
import json
import os
import shutil
from pathlib import Path
from typing import Dict

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def get_slidev_output_path(presentation_title: str) -> str:
    base_dir = Path("backend/slidev_output/public")
    safe_title = "".join(c if c.isalnum() else "_" for c in presentation_title)
    paper_dir = base_dir / safe_title
    paper_dir.mkdir(parents=True, exist_ok=True)
    slides_md_path = paper_dir / "slides.md"
    return str(slides_md_path)

def generate_slidev_markdown(presentation: PresentationContent) -> str:
    """Generate Slidev markdown content from presentation data."""
    markdown = """---
theme: default
background: https://source.unsplash.com/collection/94734566/1920x1080
class: text-center
highlighter: shiki
lineNumbers: false
info: |
  ## {title}
  Generated presentation from academic paper
drawings:
  persist: false
transition: slide-left
title: {title}
---

# {title}

---
""".format(title=presentation.title)

    for slide in presentation.slides:
        markdown += f"\n# {slide.title}\n\n"
        for point in slide.points:
            markdown += f"- {point}\n"
        markdown += "\n---\n"

    return markdown

def generate_presentation_content(text: str) -> tuple[PresentationContent, bool]:
    prompt = f"""You are an expert presentation creator. Create a structured presentation outline from the following academic paper text.
    The presentation should include:
    1. A clear title
    2. An introduction slide
    3. Key sections with 3-5 bullet points each
    4. A conclusion slide
    
    Format the response as a JSON object with the following structure:
    {{
        "title": "Presentation Title",
        "slides": [
            {{
                "title": "Slide Title",
                "points": ["Point 1", "Point 2", "Point 3"]
            }}
        ]
    }}
    
    Paper text:
    {text}
    """
    
    try:
        response = client.chat.completions.create(
            model="o4-mini",  # or "gpt-3.5-turbo" if preferred
            messages=[
                {"role": "system", "content": "You are an expert presentation creator that creates clear, concise, and engaging academic presentations."},
                {"role": "user", "content": prompt}
            ],
            temperature=1,
        )
        
        # Extract the JSON response
        content = response.choices[0].message.content
        presentation_data = json.loads(content)
        
        # Convert to our Pydantic model
        slides = [Slide(**slide) for slide in presentation_data["slides"]]
        presentation = PresentationContent(
            title=presentation_data["title"],
            slides=slides
        )
        
        # Get Slidev markdown output path
        slides_md_path = get_slidev_output_path(presentation.title)
        
        # Generate and save markdown content
        markdown_content = generate_slidev_markdown(presentation)
        with open(slides_md_path, "w", encoding="utf-8") as f:
            f.write(markdown_content)
        
        return presentation, True
        
    except Exception as e:
        raise Exception(f"Error generating presentation content: {str(e)}") 