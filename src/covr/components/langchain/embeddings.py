from langchain_huggingface import HuggingFaceEmbeddings

from covr.components.langchain.constants import EMBEDDINGS_MODEL_NAME

embeddings_model = HuggingFaceEmbeddings(model_name=EMBEDDINGS_MODEL_NAME)
