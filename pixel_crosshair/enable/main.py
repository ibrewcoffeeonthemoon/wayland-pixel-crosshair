import re
from typing import Annotated

import typer
from typer import Option

from .overlay import start_overlay

app = typer.Typer()


def validate_rgba_color(value: str):
    # Regex for #RRGGBBAA
    if not re.fullmatch(r'#[0-9a-fA-F]{8}', value):
        raise typer.BadParameter('Color must be in #RRGGBBAA format (e.g., #00FF00FF)')
    return value


@app.command(help='enable crosshair')
def enable(
    color: Annotated[str, Option(
        '--color', '-c',
        callback=validate_rgba_color,
        help='crosshair color in RGBA hex format, i.e.#RRGGBBAA'
    )] = '#00FF00FF',
) -> None:
    start_overlay(color)
