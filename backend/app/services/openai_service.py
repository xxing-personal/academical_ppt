from openai import OpenAI
from app.core.config import get_settings
from app.schemas.presentation import PresentationContent, Slide
import json

settings = get_settings()
client = OpenAI(api_key=settings.OPENAI_API_KEY)

def generate_presentation_content(text: str) -> PresentationContent:
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
            model="gpt-4",  # or "gpt-3.5-turbo" if preferred
            messages=[
                {"role": "system", "content": "You are an expert presentation creator that creates clear, concise, and engaging academic presentations."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        # Extract the JSON response
        content = response.choices[0].message.content
        presentation_data = json.loads(content)
        
        # Convert to our Pydantic model
        slides = [Slide(**slide) for slide in presentation_data["slides"]]
        return PresentationContent(
            title=presentation_data["title"],
            slides=slides
        )
        
    except Exception as e:
        raise Exception(f"Error generating presentation content: {str(e)}") 