from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode"
}

IMPORTANT_FILES = {
    "README.md",
    "requirements.txt",
    "pyproject.toml",
    "package.json",
    "Dockerfile",
    "docker-compose.yml",
    "main.py",
    "app.py",
    "manage.py"
}


class RepositoryScanner:

    def scan(self):

        important_files = []

        root = Path(".")

        for file in root.rglob("*"):

            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            if not file.is_file():
                continue

            if (
                file.name in IMPORTANT_FILES
                or file.suffix in [".py", ".js", ".ts"]
            ):
                important_files.append(file)

        return important_files