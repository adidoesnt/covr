import os
from dotenv import load_dotenv

load_dotenv()

CHROMA_PATH = os.getenv("CHROMA_PATH", "infra/local/chroma-data")
CHROMA_COLLECTION_NAME = os.getenv("CHROMA_COLLECTION_NAME", "knowledge_base")

EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", "text-embedding-3-small")
CHAT_MODEL = os.getenv("CHAT_MODEL", "gpt-4o-mini")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

K_VALUE = int(os.getenv("K_VALUE", 3))
RELEVANCE_SCORE_THRESHOLD = float(os.getenv("RELEVANCE_SCORE_THRESHOLD", 0.7))
DEFAULT_RELEVANCE_SCORE_THRESHOLD = float(os.getenv("DEFAULT_RELEVANCE_SCORE_THRESHOLD", 0.3))
