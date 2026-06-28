from pathlib import Path

from git import Repo
from rich.console import Console
from rich.table import Table

from services.dependency_analyzer import (
    DependencyAnalyzer
)

console = Console()


def deps():

    repo = Repo(
        ".",
        search_parent_directories=True
    )

    root = Path(repo.working_dir)

    analyzer = DependencyAnalyzer()

    dependencies = analyzer.analyze(root)

    table = Table(title="Dependencies")

    table.add_column("Ecosystem")
    table.add_column("Package")

    for ecosystem, packages in dependencies.items():

        for package in packages:

            table.add_row(
                ecosystem,
                package
            )

    console.print(table)