import typer
from commands.summary import summary

app = typer.Typer()


@app.command()
def version():
    print("Repowise v0.1")

app.command()(summary)


if __name__ == "__main__":
    app()