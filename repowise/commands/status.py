from git import Repo
from rich.console import Console
from rich.table import Table

console = Console()

def status():
    repo = Repo(".", search_parent_directories=True)

    untracked = repo.untracked_files
    modified = list(repo.index.diff(None))
    staged = list(repo.index.diff("HEAD"))

    if not untracked and not modified and not staged:
        console.print("[bold green]✓ Repository is clean![/bold green]")
        return

    table = Table(title="Repository Status")

    table.add_column("Type", style="cyan")
    table.add_column("File", style="green")

    # Untracked files
    for file in untracked:
        table.add_row("Untracked", file)

    # Modified files
    for item in modified:
        table.add_row("Modified", item.a_path)

    # Staged files
    for item in staged:
        table.add_row("Staged", item.a_path)

    console.print(table)