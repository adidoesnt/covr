from chromadb.errors import InvalidCollectionException

from covr.components.chromadb.db import client
from covr.components.langchain.text_splitter import split_text
from covr.components.langchain.vector_store import get_user_collection

def upload_resume(user_id, file_content):
    chunks = split_text(text=file_content)
    
    collection = get_user_collection(user_id=user_id)
    collection.add_texts(texts=chunks) 
    
def delete_resume(user_id):
    client.delete_collection(f"user_{user_id}")

def check_if_resume_exists(user_id):
    try:
        client.get_collection(f"user_{user_id}")
        return True
    
    except Exception as e:
        if isinstance(e, InvalidCollectionException):
            return False
        else:
            raise e
