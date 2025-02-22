from covr.components.query_executor import query
from covr.components.utils.file_utils import write_to_file

def query_handler(query_text, output_path):
    result = query(query_text)

    print(f"Writing result to {output_path}")
    write_to_file(output_path, result)
