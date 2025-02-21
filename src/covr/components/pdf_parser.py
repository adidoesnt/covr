import fitz

from covr.components.utils.file_utils import is_pdf

def extract_text(pdf_path):
    if not is_pdf(pdf_path):
        raise ValueError("Invalid PDF file")
    
    with fitz.open(pdf_path) as doc:
        text = []

        for page in doc:
            text.append(page.get_text())

        full_text = "\n".join(text)
        return full_text
