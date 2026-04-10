import re
from typing import Annotated

import typer
from typer import Option

from pixel_crosshair.disable.terminate import terminate_existing

from .overlay import start_overlay

app = typer.Typer()


def validate_rgba_color(value: str):
    # Regex for #RRGGBBAA
    if not re.fullmatch(r'#[0-9a-fA-F]{6}', value):
        raise typer.BadParameter('Color must be in #RRGGBB format (e.g., #00FF00)')
    return value


def validate_alpha(value: float) -> float:
    if not 0.0 <= value <= 1.0:
        raise ValueError('Alpha must be between 0.0 and 1.0')
    return value


@app.command(help='enable crosshair')
def enable(
    color: Annotated[str, Option(
        '--color', '-c',
        callback=validate_rgba_color,
        help='crosshair color in RGB hex format, i.e.#RRGGBB'
    )] = '#00FF00',
    alpha: Annotated[float, Option(
        '--alpha', '-a',
        callback=validate_alpha,
        help='crosshair color alpha value',
    )] = 1.0,
) -> None:
    # disable existing instance
    terminate_existing()

    # convert color format to floats
    r, g, b = [int(color[i:i+2], 16)/255.0 for i in (1, 3, 5)]
    rgba = (r, g, b, alpha, )

    # start overlay
    start_overlay(rgba)
