import typer

app = typer.Typer()


@app.command(help='disable crosshair')
def disable() -> None:
    print(f'gonna disable crosshair')
