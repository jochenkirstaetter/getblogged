#!/usr/bin/env python3
"""
Guardrail script: Ensures there are no uncommitted or untracked post files in the workspace before deploying.
"""

import sys
import subprocess
from pathlib import Path

# Target paths containing post content, assets, and feeds
POST_PATHS = [
    "posts/published",
    "posts/draft",
    "posts/pages",
    "posts/content",
    "posts/index.md",
]

def check_uncommitted_posts():
    repo_root = Path(__file__).resolve().parent.parent
    try:
        result = subprocess.run(
            ["git", "status", "--porcelain"] + POST_PATHS,
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        )
    except Exception as e:
        print(f"Error checking git status: {e}", file=sys.stderr)
        sys.exit(1)

    lines = [line.strip() for line in result.stdout.splitlines() if line.strip()]
    dirty_lines = [
        line for line in lines
        if not line.endswith(".DS_Store")
    ]

    if dirty_lines:
        print("\n❌ Deployment Guardrail Failed: Uncommitted or untracked posts detected in workspace.", file=sys.stderr)
        print("Please commit or stash your changes in content paths before deploying:\n", file=sys.stderr)
        for line in dirty_lines:
            print(f"   {line}", file=sys.stderr)
        print("\nDeployment aborted.", file=sys.stderr)
        sys.exit(1)

    print("✔ Deployment Guardrail Passed: All posts and content files are clean and committed.")

if __name__ == "__main__":
    check_uncommitted_posts()

