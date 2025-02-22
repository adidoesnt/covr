from langchain_community.vectorstores import Chroma
from langchain.schema import Document
from typing import List

from covr.components.environment import CHROMA_PATH, CHROMA_COLLECTION_NAME
from covr.components.embeddings import embedding_function
from covr.components.utils.database import no_result

def save_to_database(chunks: List[Document]):
    """Save chunks to the vector store"""

    Chroma.from_documents(
        chunks,
        collection_name=CHROMA_COLLECTION_NAME,
        persist_directory=CHROMA_PATH,
        embedding=embedding_function
    )

    print(f"Chunks saved to collection {CHROMA_COLLECTION_NAME}, persisted at {CHROMA_PATH}")

def get_from_database(query: str, k: int = 3) -> List[Document]:
    """Get documents from the vector store"""

    database = Chroma(
        persist_directory=CHROMA_PATH,
        collection_name=CHROMA_COLLECTION_NAME,
        embedding_function=embedding_function,
    )

    results = database.similarity_search_with_relevance_scores(query, k=k)

    if no_result(results):
        raise ValueError("No results found")
    
    return results
