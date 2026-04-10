from typing import Annotated

import typer
from typer import Option

app = typer.Typer()


@app.command(help='enable crosshair')
def enable(
    color: Annotated[str, Option('--color', '-c', help='crosshair color')] = '#00ff00',
) -> None:
    print(f'gonna enable crosshair with {color=}')
