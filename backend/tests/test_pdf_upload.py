import os
import sys

# Ensure backend is in the Python path
backend_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(backend_dir)

from app.utils.pdf_processor import extract_text_from_pdf

def test_pdf_processing():
    # Get the path to the test PDF file
    current_dir = os.path.dirname(os.path.abspath(__file__))
    pdf_path = os.path.join(current_dir, "file.pdf")
    
    # Process the PDF using the actual utility function
    text, num_pages, images = extract_text_from_pdf(pdf_path)
    
    # Print results
    print(f"\nPDF Processing Results:")
    print(f"Number of pages: {num_pages}")
    print(f"Number of images found: {len(images)}")
    print("\nFirst 500 characters of extracted text:")
    print(text[:500])
    if images:
        print("\nFirst image info:")
        print(images[0])
    
    return text, num_pages, images

if __name__ == "__main__":
    test_pdf_processing() 