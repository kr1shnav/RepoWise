from pathlib import Path

from git import Repo
from rich.console import Console
from rich.table import Table

console = Console()


def info():
    repo = Repo(".", search_parent_directories=True)

    table = Table(title="Repository Information")

    table.add_column("Property", style="cyan")
    table.add_column("Value", style="green")

    repo_name = Path(repo.working_dir).name

    total_commits = sum(1 for _ in repo.iter_commits())

    table.add_row("Repository Name", repo_name)
    table.add_row("Current Branch", str(repo.active_branch))
    table.add_row("Total Branches", str(len(repo.branches)))
    table.add_row("Total Commits", str(total_commits))
    table.add_row("Working Directory", repo.working_dir)

    console.print(table)