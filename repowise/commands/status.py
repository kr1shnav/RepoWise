from git import Repo
from rich.console import Console
from rich.table import Table

console = Console()

def status():
    repo = Repo(".", search_parent_directories=True)

    table = Table(title="Repository Status")

    table.add_column("Type",style="cyan")
    table.add_column("File", style="green")

    # Untracked files
    for file in repo.untracked_files:
        table.add_row("Untracked", file)

    # Modified files
    for item in repo.index.diff(None):
        table.add_row("Modified", item.a_path)

    # Staged files
    for item in repo.index.diff("HEAD"):
        table.add_row("Staged", item.a_path)

    console.print(table)

    if not repo.untracked_files and not repo.index.diff(None):
        console.print("[green]Repository is clean![/green]")