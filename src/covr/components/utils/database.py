def no_result(results) -> bool:
    """Check if there are no results based on length and relevance score"""

    return len(results) == 0 or results[0][1] < 0.7
