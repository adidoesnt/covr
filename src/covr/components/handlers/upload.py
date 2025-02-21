from langchain.document_loaders.pdf import PyPDFDirectoryLoader

from covr.components.utils.file_utils import is_directory

def upload_handler(dir):
    if is_directory(dir):
        print(f"Processing directory: {dir}")

        loader = PyPDFDirectoryLoader(dir)
        documents = loader.load()

        print(documents[0])
    else:
        raise ValueError("Uploaded file is not a directory")
