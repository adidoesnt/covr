import click

@click.group()
def cli():
    """Command-line interface for Covr"""
    pass

@click.command(name="upload-files")
@click.option("--file", multiple=True, prompt="File(s) to upload", help="Enter path(s) to file(s) to upload")
def upload_files(file):
    """Upload files to be stored in the knowledge base"""
    
    for f in file:
        print(f"Uploading file: {f}")

cli.add_command(upload_files)
