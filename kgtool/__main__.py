# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from kgtool import version
from kgtool.interface import connect, fullGraph


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="kgtool",
    help="awesome kgtool",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]kgtool[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(name="info")
def _info():
    """Prints Info about the API ?"""
    return 0


@app.command(name="fullGraph")
def _fullGraph():
    fullGraph()


@app.command()
def main(
    options: Optional[str] = typer.Option(
        None,
        "-o",
        "--options",
        help="Options to connect to the database",
    ),
    print_version: bool = typer.Option(
        None,
        "-v",
        "--version",
        callback=version_callback,
        is_eager=True,
        help="Prints the version of the kgtool package.",
    ),
) -> None:
    """Connect to the Databases"""

    connect(options)


if __name__ == "__main__":
    app()
