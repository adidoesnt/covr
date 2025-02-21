import os

def is_directory(path):
    return os.path.isdir(path)

def is_file(path):
    return os.path.isfile(path)

def is_pdf(path):
    return path.endswith(".pdf")
