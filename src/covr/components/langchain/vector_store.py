from langchain_chroma import Chroma
from langchain.prompts import PromptTemplate

from covr.components.chromadb.db import client
from covr.components.langchain.embeddings import embeddings_model
from covr.components.langchain.generator import llm

def get_user_collection(user_id):
    collection = Chroma(
        client=client,
        collection_name=f"user_{user_id}",
        embedding_function=embeddings_model
    )
    
    return collection

def query_user_collection(user_id, query):
    print(f"Querying user {user_id} for: {query}")
    collection = get_user_collection(user_id=user_id)
    
    results = collection.similarity_search(query=query, k=1)
    
    if not results:
        raise Exception("No results found.")
    
    context = results[0].page_content
    
    print("Received context, generating summary...")
    summary_prompt = PromptTemplate(
        input_variables=["context"],
        template="""
        You are a skilled writer, and you have been tasked with summarizing the following content:

        {context}
        """
    )
    
    formatted_summary_prompt = summary_prompt.format(context=context)
    print("Formatted summary prompt, generating response from LLM...")
    
    llm_result = llm.generate([formatted_summary_prompt])
    response = llm_result.generations[0][0].text
    print("Generated response, returning to caller.")
    
    return response
