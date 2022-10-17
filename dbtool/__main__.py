# type: ignore[attr-defined]
from typing import Optional

from enum import Enum
from random import choice

import typer
from rich.console import Console

from dbtool import version
from dbtool.interface import connect


class Color(str, Enum):
    white = "white"
    red = "red"
    cyan = "cyan"
    magenta = "magenta"
    yellow = "yellow"
    green = "green"


app = typer.Typer(
    name="dbtool",
    help="awesome dbtool",
    add_completion=False,
)
console = Console()


def version_callback(print_version: bool) -> None:
    """Print the version of the package."""
    if print_version:
        console.print(f"[yellow]dbtool[/] version: [bold blue]{version}[/]")
        raise typer.Exit()


@app.command(options="")
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
        help="Prints the version of the dbtool package.",
    ),
) -> None:
    """Connect to the Databases"""

    connect(options)


if __name__ == "__main__":
    app()
