import os

from covr.components.pdf_parser import extract_text
from covr.components.utils.file_utils import is_directory

def upload_files_handler(file):
    if is_directory(file):
        print(f"Processing directory: {file}")

        for f in os.listdir(file):
            upload_files_handler(os.path.join(file, f))
    else:
        print(f"Processing file: {file}")
        
        text = extract_text(file)
        print(text)
