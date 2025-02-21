import click

from covr.components.handlers.upload_files import upload_files_handler 

@click.group()
def cli():
    """Command-line interface for Covr"""
    pass

@click.command(name="upload-files")
@click.option("--file", multiple=True, prompt="File(s) to upload", help="Enter path(s) to file(s) to upload")
def upload_files(file):
    """Upload files to be stored in the knowledge base"""
    
    for f in file:
        upload_files_handler(f)

cli.add_command(upload_files)
