import fitz
from io import BytesIO

def parse_pdf(file_content):
    stream = BytesIO(file_content)
    doc = fitz.open(stream=stream, filetype="pdf")
    
    parsed_text = ""
    
    for page_number, page in enumerate(doc, start=1):
        parsed_text += f"--- Page {page_number} ---\n"
        parsed_text += page.get_text()
    
    return parsed_text