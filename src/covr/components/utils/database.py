from typing import List
from langchain.schema import Document

def no_result(results: List[Document], similarity_threshold: float = 0.7) -> bool:
    """Check if there are no results based on length and relevance score"""

    len(results) == 0 or results[0][1] < similarity_threshold
