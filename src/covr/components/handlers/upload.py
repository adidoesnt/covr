from covr.components.document_parser import parse

def upload_handler(file):
    documents = parse(file)

    print(documents[0])
