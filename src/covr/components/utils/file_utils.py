import os

def is_directory(path: str) -> bool:
    """Check if a path is a directory"""

    return os.path.isdir(path)

def is_pdf(path: str) -> bool:
    """Check if a path is a PDF file"""

    return path.endswith(".pdf")
