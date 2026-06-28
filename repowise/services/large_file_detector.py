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


class LargeFileDetector:

    def find(self, root: Path, threshold: int = 200):

        large_files = []

        for file in root.rglob("*"):

            if any(part in IGNORE_DIRS for part in file.parts):
                continue

            if not file.is_file():
                continue

            if file.suffix not in SUPPORTED_EXTENSIONS:
                continue

            try:
                with open(
                    file,
                    "r",
                    encoding="utf-8",
                    errors="ignore"
                ) as f:

                    line_count = sum(1 for _ in f)

                if line_count >= threshold:

                    large_files.append(
                        {
                            "file": file,
                            "lines": line_count
                        }
                    )

            except Exception:
                continue

        return sorted(
            large_files,
            key=lambda x: x["lines"],
            reverse=True
        )