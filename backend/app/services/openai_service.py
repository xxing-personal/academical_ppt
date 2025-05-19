from openai import OpenAI
from app.core.config import get_settings
from app.schemas.presentation import PresentationContent, Slide
import json
import os
import shutil
from pathlib import Path
import subprocess
import socket
import psutil
import atexit
from typing import Dict, Optional

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

# Global dictionary to track running Slidev processes
running_slidev_processes: Dict[str, subprocess.Popen] = {}

def find_available_port(start_port: int = 3030, max_port: int = 3130) -> int:
    """Find an available port in the given range."""
    for port in range(start_port, max_port + 1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            try:
                s.bind(('localhost', port))
                return port
            except OSError:
                continue
    raise RuntimeError("No available ports found in the specified range")

def cleanup_slidev_processes():
    """Cleanup function to terminate all running Slidev processes on application shutdown."""
    for process in running_slidev_processes.values():
        try:
            process.terminate()
            process.wait(timeout=5)
        except (subprocess.TimeoutExpired, psutil.NoSuchProcess):
            try:
                process.kill()
            except psutil.NoSuchProcess:
                pass

# Register cleanup function
atexit.register(cleanup_slidev_processes)

def start_slidev_server(slides_md_path: str) -> tuple[subprocess.Popen, int]:
    """Start a Slidev development server in the directory containing the slides.md file."""
    # Find an available port
    port = find_available_port()
    
    # Start Slidev server in the output directory
    output_dir = os.path.dirname(slides_md_path)
    process = subprocess.Popen(
        ['npx', 'slidev', os.path.basename(slides_md_path), '--port', str(port)],
        cwd=output_dir,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        env={**os.environ, 'NODE_ENV': 'development'}
    )
    
    # Store the process
    running_slidev_processes[slides_md_path] = process
    
    return process, port

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

def generate_presentation_content(text: str) -> tuple[PresentationContent, str]:
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
        
        # Start Slidev server
        process, port = start_slidev_server(slides_md_path)
        
        # Return both the presentation content and the URL
        return presentation, f"http://localhost:{port}"
        
    except Exception as e:
        raise Exception(f"Error generating presentation content: {str(e)}") 