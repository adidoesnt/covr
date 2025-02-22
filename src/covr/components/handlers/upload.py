from covr.components.document_parser import parse, split_into_chunks
from covr.components.database import save_to_database

def upload_handler(file):
    documents = parse(file)
    chunks = split_into_chunks(documents)

    save_to_database(chunks)
