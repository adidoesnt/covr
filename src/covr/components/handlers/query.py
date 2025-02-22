from covr.components.query_executor import query

def query_handler(query_text):
    result = query(query_text)

    print(result)