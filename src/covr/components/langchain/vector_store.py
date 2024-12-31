from langchain_chroma import Chroma

from covr.components.chromadb.db import client
from covr.components.langchain.embeddings import embeddings_model

def get_user_collection(user_id):
    collection = Chroma(
        client=client,
        collection_name=f"user_{user_id}",
        embedding_function=embeddings_model
    )
    
    return collection
