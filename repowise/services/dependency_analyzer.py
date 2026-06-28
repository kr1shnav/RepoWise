import json
from pathlib import Path


class DependencyAnalyzer:

    def analyze(self, root: Path):

        dependencies = {
            "Python": [],
            "JavaScript": []
        }

        requirements = root / "requirements.txt"

        if requirements.exists():

            with open(requirements, "r") as f:

                for line in f:

                    line = line.strip()

                    if line and not line.startswith("#"):

                        package = line.split("==")[0]

                        dependencies["Python"].append(package)

        package_json = root / "package.json"

        if package_json.exists():

            with open(package_json, "r") as f:

                data = json.load(f)

            deps = data.get("dependencies", {})

            dependencies["JavaScript"].extend(
                deps.keys()
            )

        return dependencies
