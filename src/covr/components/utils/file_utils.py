import os

def is_directory(path: str) -> bool:
    """Check if a path is a directory"""

    return os.path.isdir(path)

def is_pdf(path: str) -> bool:
    """Check if a path is a PDF file"""

    return path.endswith(".pdf")

def write_to_file(path: str, content):
    """Create a file and create the directory if it doesn't exist"""

    dir_name = os.path.dirname(path)

    if not os.path.exists(dir_name):
        os.makedirs(dir_name, exist_ok=True)

    with open(path, "w") as file:
        file.write(content)
