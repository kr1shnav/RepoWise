from git import Repo


def summary():
    repo = Repo(".")

    print("\nRepository Summary")
    print("--------------------")

    print(f"Current Branch: {repo.active_branch}")
    print(f"Repository Name: {repo.working_dir.split('/')[-1]}")

    branches = repo.branches
    print(f"Branches: {len(branches)}")

    commit_count = sum(1 for _ in repo.iter_commits())
    print(f"Total Commits: {commit_count}")

    print("\nRecent Commits:")

    commits = list(repo.iter_commits(max_count=5))

    for commit in commits:
        print(f"-{commit.message.strip()}")
