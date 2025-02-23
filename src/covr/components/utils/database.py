from typing import List
from langchain.schema import Document

from covr.components.environment import DEFAULT_RELEVANCE_SCORE_THRESHOLD

def no_result(results: List[Document], similarity_threshold: float = DEFAULT_RELEVANCE_SCORE_THRESHOLD) -> bool:
    """Check if there are no results based on length and relevance score"""

    len(results) == 0 or results[0][1] < similarity_threshold
