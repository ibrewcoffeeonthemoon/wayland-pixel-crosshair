import typer

from .terminate import terminate_existing

app = typer.Typer()


@app.command(help='disable crosshair')
def disable() -> None:
    terminate_existing()
