from langchain.schema import Document
from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from typing import List

from covr.components.database import get_from_database
from covr.components.environment import OPENAI_API_KEY, CHAT_MODEL

PROMPT_TEMPLATE = """
You are a helpful job hunting assistant, who excels at extracting information from candidate documents.
Here is some context regarding the candidate:
{context}
---
Based on the context, answer the following question:
{question}
"""

def get_context(results: List[Document]) -> str:
    """Get the context from the results"""
    
    return "\n\n --- \n\n".join([result[0].page_content for result in results])

def get_prompt(query: str, context: str) -> str:
    """Get the prompt for the query"""

    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    return prompt_template.format(context=context, question=query)

def query(query: str) -> str:
    """Execute the query and return the result"""

    print(f"Executing query: {query}")

    results = get_from_database(query)
    context = get_context(results)
    prompt = get_prompt(query, context)

    print(f"Generated prompt: {prompt}")

    model = ChatOpenAI(
        api_key=OPENAI_API_KEY,
        model=CHAT_MODEL
    )

    response = model.predict(prompt)

    print("Generated response.")
    return response