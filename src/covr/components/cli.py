import click

from covr.components.handlers.upload import upload_handler
from covr.components.handlers.query import query_handler

@click.group()
def cli():
    """Command-line interface for Covr"""
    pass

@click.command(name="upload")
@click.option("--path", "-p", prompt="Directory or file to upload", help="Enter path to the directory or file to upload.")
def upload_files(path):
    """Upload files to be stored in the knowledge base"""

    upload_handler(path)

@click.command(name="query")
@click.option("--query", "-q", prompt="Query to send to the knowledge base", help="Enter the query.")
@click.option("--output", "-o", prompt="Output file path", help="Enter the output file path.")
def query_knowledge_base(query, output):
    """Query the knowledge base"""

    query_handler(query, output)

cli.add_command(upload_files)
cli.add_command(query_knowledge_base)
