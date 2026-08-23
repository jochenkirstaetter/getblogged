#!/usr/bin/env python3
"""
Guardrail script: Ensures there are no uncommitted or untracked post files in the workspace before deploying,
and updates the _assetVersion cache buster across configuration files and Service Worker.
"""

import json
import re
import subprocess
import sys
from pathlib import Path

# Target paths containing post content, assets, and feeds
POST_PATHS = [
    "posts/published",
    "posts/draft",
    "posts/pages",
    "posts/content",
    "posts/index.md",
]

def check_uncommitted_posts(repo_root: Path):
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

def bump_asset_version(repo_root: Path):
    try:
        rev_count = subprocess.run(
            ["git", "rev-list", "--count", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()
        short_hash = subprocess.run(
            ["git", "rev-parse", "--short", "HEAD"],
            cwd=repo_root,
            capture_output=True,
            text=True,
            check=True
        ).stdout.strip()
        version = f"v{rev_count}-{short_hash}"
    except Exception as e:
        print(f"Warning: Could not retrieve git revision metadata: {e}", file=sys.stderr)
        version = "v-latest"

    # Update posts/docfx.json
    docfx_path = repo_root / "posts" / "docfx.json"
    if docfx_path.exists():
        try:
            cfg = json.loads(docfx_path.read_text(encoding="utf-8"))
            if "build" in cfg and "globalMetadata" in cfg["build"]:
                cfg["build"]["globalMetadata"]["_assetVersion"] = version
                docfx_path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        except Exception as e:
            print(f"Error updating {docfx_path}: {e}", file=sys.stderr)

    # Update posts/docfx.draft.json
    docfx_draft_path = repo_root / "posts" / "docfx.draft.json"
    if docfx_draft_path.exists():
        try:
            cfg = json.loads(docfx_draft_path.read_text(encoding="utf-8"))
            if "build" in cfg and "globalMetadata" in cfg["build"]:
                cfg["build"]["globalMetadata"]["_assetVersion"] = version
                docfx_draft_path.write_text(json.dumps(cfg, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        except Exception as e:
            print(f"Error updating {docfx_draft_path}: {e}", file=sys.stderr)

    # Update posts/ghostfx/public/sw-v1.js
    sw_path = repo_root / "posts" / "ghostfx" / "public" / "sw-v1.js"
    if sw_path.exists():
        try:
            sw_content = sw_path.read_text(encoding="utf-8")
            sw_content = re.sub(
                r"const CACHE_NAME_STATIC = ['\"].*?['\"];",
                f"const CACHE_NAME_STATIC = 'ghostfx-static-{version}';",
                sw_content
            )
            sw_content = re.sub(
                r"const CACHE_NAME_CONTENT = ['\"].*?['\"];",
                f"const CACHE_NAME_CONTENT = 'ghostfx-content-{version}';",
                sw_content
            )
            sw_path.write_text(sw_content, encoding="utf-8")
        except Exception as e:
            print(f"Error updating {sw_path}: {e}", file=sys.stderr)

    print(f"✔ Cache buster asset version updated to: {version}")

def main():
    repo_root = Path(__file__).resolve().parent.parent
    check_uncommitted_posts(repo_root)
    bump_asset_version(repo_root)

if __name__ == "__main__":
    main()

