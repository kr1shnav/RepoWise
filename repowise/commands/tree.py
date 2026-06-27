from pathlib import Path

from git import Repo
from rich.console import Console
from rich.tree import Tree

console = Console()

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode"
}


def add_tree(directory: Path, tree: Tree):

    for path in sorted(directory.iterdir()):

        if path.name in IGNORE_DIRS:
            continue

        if path.is_dir():

            branch = tree.add(f"📁 {path.name}")

            add_tree(path, branch)

        else:
            tree.add(f"📄 {path.name}")


def tree():
    # Get the Git repository root
    repo = Repo(".", search_parent_directories=True)

    root = Path(repo.working_dir)
    repo_tree = Tree(f"📦 {root.name}")

    add_tree(root, repo_tree)

    console.print(repo_tree)