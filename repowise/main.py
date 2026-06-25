import typer

from commands.summary import summary
from commands.status import status

app = typer.Typer()


@app.command()
def version():
    print("Repowise v0.1")


app.command()(summary)
app.command()(status)


if __name__ == "__main__":
    app()
