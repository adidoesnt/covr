from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
from langchain.schema import Document
from typing import List

from covr.components.environment import CHROMA_PATH, CHROMA_COLLECTION_NAME, EMBEDDINGS_MODEL, OPENAI_API_KEY

def save_to_database(chunks: List[Document]):
    """Save chunks to the vector store"""

    embeddings = OpenAIEmbeddings(model=EMBEDDINGS_MODEL, api_key=OPENAI_API_KEY)

    Chroma.from_documents(
        chunks,
        collection_name=CHROMA_COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding=embeddings
    )

    print(f"Chunks saved to collection {CHROMA_COLLECTION_NAME}, persisted at {CHROMA_PATH}")
