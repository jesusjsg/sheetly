import click
from src.core.config import settings


@click.command()
@click.version_option(settings.VERSION)
def version():
    click.echo(f"Sheetly version: {settings.VERSION}")
