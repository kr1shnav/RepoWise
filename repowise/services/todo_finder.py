import re
from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode"
}

SUPPORTED_EXTENSIONS = {
    ".py",
    ".js",
    ".ts",
    ".java",
    ".cpp",
    ".c",
    ".md",
    ".jsx",
    ".tsx",
    ".go",
    ".rs",
    ".php",
    ".rb"
}

PATTERN = re.compile(
    r"(#|//|/\*)\s*(TODO|FIXME|HACK|BUG)\s*:",
    re.IGNORECASE
)


class TodoFinder:

    def find(self, root: Path):

        todos = []

        for file in root.rglob("*"):

            # Ignore unwanted directories
            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            # Skip directories
            if not file.is_file():
                continue

            # Skip unsupported files
            if file.suffix not in SUPPORTED_EXTENSIONS:
                continue

            try:
                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    for line_number, line in enumerate(f, start=1):

                        if PATTERN.search(line):

                            todos.append(
                                {
                                    "file": file,
                                    "line": line_number,
                                    "text": line.strip()
                                }
                            )

            except Exception:
                continue

        return todos
