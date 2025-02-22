from langchain_openai import OpenAIEmbeddings

from covr.components.environment import EMBEDDINGS_MODEL, OPENAI_API_KEY

embedding_function = OpenAIEmbeddings(model=EMBEDDINGS_MODEL, api_key=OPENAI_API_KEY)
