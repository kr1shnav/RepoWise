from pathlib import Path

IGNORE_DIRS = {
    ".git",
    ".venv",
    "__pycache__",
    "node_modules",
    ".idea",
    ".vscode"
}

KEYWORDS = [
    "TODO",
    "FIXME",
    "HACK",
    "BUG"
]


class TodoFinder:

    def find(self, root: Path):

        todos = []

        for file in root.rglob("*"):

            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            if not file.is_file():
                continue

            # Only scan source files
            if file.suffix not in [
                ".py",
                ".js",
                ".ts",
                ".java",
                ".cpp",
                ".c",
                ".md"
            ]:
                continue

            try:

                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    for line_number, line in enumerate(f, start=1):

                        for keyword in KEYWORDS:

                            if keyword in line:

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
