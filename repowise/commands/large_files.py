from pathlib import Path

from git import Repo
from rich.console import Console
from rich.table import Table

from services.large_file_detector import (
    LargeFileDetector
)

console = Console()


def large_files():

    repo = Repo(
        ".",
        search_parent_directories=True
    )

    root = Path(repo.working_dir)

    detector = LargeFileDetector()

    results = detector.find(root)

    if not results:
        console.print(
            "[green]No large files found![/green]"
        )
        return

    table = Table(title="Large Files")

    table.add_column("File", style="cyan")
    table.add_column("Lines", style="red")

    for item in results:

        table.add_row(
            str(item["file"].relative_to(root)),
            str(item["lines"])
        )

    console.print(table)
