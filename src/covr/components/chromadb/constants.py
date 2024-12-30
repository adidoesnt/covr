from dotenv import load_dotenv
import os

load_dotenv()

CHROMADB_HOST = os.getenv('CHROMADB_HOST', 'localhost')
CHROMADB_PORT = os.getenv('CHROMADB_PORT', '8000')
CHROMA_CLIENT_AUTH_PROVIDER = os.getenv('CHROMA_CLIENT_AUTH_PROVIDER', 'chromadb.auth.token_authn.TokenAuthClientProvider')
CHROMA_CLIENT_AUTH_CREDENTIALS = os.getenv('CHROMA_CLIENT_AUTH_CREDENTIALS', 'DUMMY-SECRET')
CHROMA_AUTH_TOKEN_TRANSPORT_HEADER=os.getenv('CHROMA_AUTH_TOKEN_TRANSPORT_HEADER', 'X-Chroma-Token')
PERSIST_DIRECTORY=os.getenv('PERSIST_DIRECTORY', '/storage/chroma-storage')
