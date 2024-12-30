from chromadb import HttpClient, config
from langchain.embeddings import HuggingFaceEmbeddings

from covr.components.chromadb.constants import CHROMADB_HOST, CHROMADB_PORT, CHROMA_CLIENT_AUTH_PROVIDER, CHROMA_CLIENT_AUTH_CREDENTIALS, CHROMA_AUTH_TOKEN_TRANSPORT_HEADER
from covr.components.langchain.constants import EMBEDDINGS_MODEL_NAME

embeddings_model = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)

client = HttpClient(
    host=CHROMADB_HOST,
    port=int(CHROMADB_PORT),
    settings=config.Settings(
        chroma_client_auth_provider=CHROMA_CLIENT_AUTH_PROVIDER,
        chroma_client_auth_credentials=CHROMA_CLIENT_AUTH_CREDENTIALS,
        chroma_auth_token_transport_header=CHROMA_AUTH_TOKEN_TRANSPORT_HEADER
    )
)

def connect_chromadb():
    try:
        client.heartbeat()
        
        print("Connected to ChromaDB.")
    except Exception as e:
        print("Error connecting to ChromaDB:", e)
        exit(1)
        
def upload_resume(user_id, file_content):
    try:
        print(f"Uploading resume for user {user_id}...")
        
        collection = client.get_or_create_collection(f"user_{user_id}")
        embeddings = embeddings_model.embed_query(file_content)
        
        collection.add(
            ids=[f"resume_{user_id}"],
            metadatas=[{"user_id": user_id}],
            embeddings=embeddings,
            documents=[file_content]
        )
        
        print(f"Resume uploaded successfully for user {user_id}.")
    except Exception as e:
        print("Error uploading resume:", e)
        raise e
    
def check_if_resume_exists(user_id):
    try:
        collection = client.get_collection(f"user_{user_id}")
        
        if collection.count() == 0:
            return False
        else:
            return True
    except Exception as e:
        print("Error checking if resume exists:", e)
        raise e