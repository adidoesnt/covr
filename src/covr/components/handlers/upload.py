from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader

from covr.components.utils.file_utils import is_directory, is_pdf

def upload_handler(file):
    if is_directory(file):
        print(f"Processing directory: {file}")

        loader = PyPDFDirectoryLoader(file)
    elif not is_pdf(file):
        raise ValueError("File must be a PDF")
    else:
        print(f"Processing file: {file}")

        loader = PyPDFLoader(file)
    
    documents = loader.load()
    print(documents[0])
