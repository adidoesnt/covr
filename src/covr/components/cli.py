import click

from covr.components.handlers.upload import upload_handler 

@click.group()
def cli():
    """Command-line interface for Covr"""
    pass

@click.command(name="upload")
@click.option("--dir", prompt="Directory from which to upload files", help="Enter path to directory from which to upload files")
def upload_files(dir):
    """Upload files to be stored in the knowledge base"""

    upload_handler(dir)

cli.add_command(upload_files)
