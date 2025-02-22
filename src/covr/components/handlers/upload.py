from covr.components.document_parser import parse, split_into_chunks

def upload_handler(file):
    documents = parse(file)
    chunks = split_into_chunks(documents)

    print(chunks[0])
