from chromadb import HttpClient, config

from covr.components.chromadb.constants import CHROMADB_HOST, CHROMADB_PORT, CHROMA_CLIENT_AUTH_PROVIDER, CHROMA_CLIENT_AUTH_CREDENTIALS, CHROMA_AUTH_TOKEN_TRANSPORT_HEADER

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
