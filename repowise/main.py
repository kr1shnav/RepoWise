import typer

from commands.summary import summary
from commands.status import status
from commands.info import info
from commands.scan import scan


app = typer.Typer()


@app.command()
def version():
    print("Repowise v0.1")


app.command()(summary)
app.command()(status)
app.command()(info)
app.command()(scan)


if __name__ == "__main__":
    app()
