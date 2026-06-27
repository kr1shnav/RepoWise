from collections import Counter
from pathlib import Path

from rich.console import Console
from rich.table import Table

console = Console()

# Directories to ignore
IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".pytest_cache",
    ".idea",
    ".vscode"
}

# File extensions to ignore
IGNORE_EXTENSIONS = {
    ".pyc",
    ".exe",
    ".idx",
    ".pack",
    ".rev",
    ".sample"
}

# Technology detection by filename
TECH_FILES = {
    "requirements.txt": "Python",
    "pyproject.toml": "Python",
    "package.json": "Node.js",
    "manage.py": "Django",
    "Dockerfile": "Docker",
    "docker-compose.yml": "Docker Compose",
    "docker-compose.yaml": "Docker Compose",
}


def scan():
    root = Path(".")

    extensions = Counter()
    technologies = set()
    total_files = 0

    # Scan repository
    for file in root.rglob("*"):

        # Skip ignored directories
        if any(part in IGNORE_DIRS for part in file.parts):
            continue

        # Skip non-files
        if not file.is_file():
            continue

        # Skip ignored extensions
        if file.suffix in IGNORE_EXTENSIONS:
            continue

        total_files += 1

        # Count extensions
        extensions[file.suffix or "No Extension"] += 1

        # Detect technologies by file names
        if file.name in TECH_FILES:
            technologies.add(TECH_FILES[file.name])

    # Detect frameworks from requirements.txt
    requirements = root / "requirements.txt"

    if requirements.exists():
        try:
            content = requirements.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "fastapi" in content:
                technologies.add("FastAPI")

            if "django" in content:
                technologies.add("Django")

            if "flask" in content:
                technologies.add("Flask")

            if "streamlit" in content:
                technologies.add("Streamlit")

        except Exception:
            pass

    # Detect frameworks from package.json
    package_json = root / "package.json"

    if package_json.exists():
        try:
            content = package_json.read_text(
                encoding="utf-8",
                errors="ignore"
            ).lower()

            if "react" in content:
                technologies.add("React")

            if "express" in content:
                technologies.add("Express")

            if "next" in content:
                technologies.add("Next.js")

        except Exception:
            pass

    # Display scan summary
    summary_table = Table(title="Repository Scan")

    summary_table.add_column("Metric", style="cyan")
    summary_table.add_column("Value", style="green")

    summary_table.add_row("Total Files", str(total_files))

    console.print(summary_table)

    # Display extension counts
    extension_table = Table(title="File Extensions")

    extension_table.add_column("Extension", style="cyan")
    extension_table.add_column("Count", style="green")

    for ext, count in sorted(extensions.items()):
        extension_table.add_row(ext, str(count))

    console.print(extension_table)

    # Display detected technologies
    console.print("\n[bold cyan]Detected Technologies[/bold cyan]\n")

    if technologies:
        for tech in sorted(technologies):
            console.print(f"[green]✓[/green] {tech}")
    else:
        console.print("[yellow]No technologies detected[/yellow]")