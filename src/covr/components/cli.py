import click

from covr.components.handlers.upload import upload_handler 

@click.group()
def cli():
    """Command-line interface for Covr"""
    pass

@click.command(name="upload")
@click.option("--path", "-p", prompt="Directory or file to upload", help="Enter path to the directory or file to upload.")
def upload_files(path):
    """Upload files to be stored in the knowledge base"""

    upload_handler(path)

cli.add_command(upload_files)
