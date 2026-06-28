from pathlib import Path

from git import Repo
from rich.console import Console
from rich.table import Table

from services.todo_finder import TodoFinder

console = Console()


def todos():

    repo = Repo(
        ".",
        search_parent_directories=True
    )

    root = Path(repo.working_dir)

    finder = TodoFinder()

    results = finder.find(root)

    if not results:
        console.print(
            "[green]No TODOs found![/green]"
        )
        return

    table = Table(title="TODOs")

    table.add_column("File")
    table.add_column("Line")
    table.add_column("Text")

    for item in results:

        table.add_row(
            str(item["file"].relative_to(root)),
            str(item["line"]),
            item["text"]
        )

    console.print(table)
