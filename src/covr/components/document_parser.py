from langchain_community.document_loaders import PyPDFLoader, PyPDFDirectoryLoader
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
from typing import List

from covr.components.utils.file_utils import is_directory, is_pdf

def parse(file: str):
    if is_directory(file):
        print(f"Processing directory: {file}")

        loader = PyPDFDirectoryLoader(file)
    elif not is_pdf(file):
        raise ValueError("File must be a PDF")
    else:
        print(f"Processing file: {file}")

        loader = PyPDFLoader(file)
    
    documents = loader.load()
    return documents

def split_into_chunks(documents: List[Document], chunk_size: int = 300, chunk_overlap: int = 100) -> List[Document]:
    """Chunk documents into smaller strings"""
    
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        length_function=len,
        add_start_index=True,
    )

    chunks = text_splitter.split_documents(documents)
    print(f"List of {len(documents)} documents chunked into {len(chunks)} chunks")

    return chunks
