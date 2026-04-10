import subprocess

import typer

app = typer.Typer()


@app.command(help='disable crosshair')
def disable() -> None:
    subprocess.run(
        ['pkill', '-f', 'wayland-pixel-crosshair'],
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )
