import importlib.metadata as meta

import typer

from .enable import app as enable

NAME = 'wayland-pixel-crosshair'


app = typer.Typer(
    name=NAME,
    no_args_is_help=True,
    help='a video restoration and processing app',
)


@app.command(help='show version info')
def version() -> None:
    print(f'v{meta.version(NAME)}')


app.add_typer(enable)
