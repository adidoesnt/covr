import os

def is_directory(path: str) -> bool:
    """Check if a path is a directory"""

    return os.path.isdir(path)
