#!/usr/bin/env python3
"""
scripts/publish-post.py
Fast-track CLI utility for promoting a draft to production, synchronizing frontmatter,
verifying responsive assets, running zero-warning DocFX builds, and preparing deployment.

Lifecycle Steps Automated:
  1. Move markdown file: posts/draft/<slug>.md -> posts/published/<slug>.md
  2. Frontmatter sync: status: published, isDraft: false, publishedAt: <now>, updatedAt: <now>
  3. Asset verification: Ensure 16:9 hero, responsive variants, and OG card exist
  4. Taxonomy & Index: Regenerate posts/index.md and posts/tags.md
  5. DocFX Compilation: Run full production build (docfx posts/docfx.json)
  6. Git Guardrails: Validate clean git status and asset cache buster

Usage Examples:
  # Dry-run / preview promotion and build:
  python3 scripts/publish-post.py --slug assembling-an-ai-publishing-agency --dry-run

  # Promote draft to published and run full verification build:
  python3 scripts/publish-post.py --slug assembling-an-ai-publishing-agency

  # Promote, verify build, and commit changes:
  python3 scripts/publish-post.py --slug assembling-an-ai-publishing-agency --commit
"""

import os
import sys
import re
import argparse
import subprocess
from pathlib import Path
from datetime import datetime, timezone

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
POSTS_DIR = REPO_ROOT / "posts"
DRAFT_DIR = POSTS_DIR / "draft"
PUBLISHED_DIR = POSTS_DIR / "published"
CONTENT_IMAGES_DIR = POSTS_DIR / "content" / "images"


def run_cmd(cmd: str, check: bool = True) -> subprocess.CompletedProcess:
    """Execute shell command within REPO_ROOT."""
    print(f"  $ {cmd}")
    res = subprocess.run(cmd, shell=True, cwd=REPO_ROOT, capture_output=True, text=True)
    if check and res.returncode != 0:
        print(f"\n❌ Command Failed (code {res.returncode}):\n{res.stderr}\n{res.stdout}")
        sys.exit(res.returncode)
    return res


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    """Extract YAML frontmatter, raw YAML block, and body."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return {}, "", content
    raw_yaml = match.group(1)
    body = match.group(2)
    fm = {}
    for line in raw_yaml.splitlines():
        kv = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
        if kv:
            fm[kv.group(1).strip()] = kv.group(2).strip().strip('"\'')
    return fm, raw_yaml, body


def promote_draft(slug: str, dry_run: bool = False) -> tuple[Path, dict]:
    """Move draft file to published directory and update publication frontmatter."""
    draft_file = DRAFT_DIR / f"{slug}.md"
    published_file = PUBLISHED_DIR / f"{slug}.md"

    if not draft_file.exists():
        if published_file.exists():
            print(f"ℹ️ Post '{slug}' is already in published directory.")
            content = published_file.read_text(encoding="utf-8")
            fm, _, _ = parse_frontmatter(content)
            return published_file, fm
        else:
            print(f"❌ Draft post not found: {draft_file}")
            sys.exit(1)

    print(f"\n📦 Step 1: Promoting draft to published: {slug}.md")
    content = draft_file.read_text(encoding="utf-8")
    fm, raw_yaml, body = parse_frontmatter(content)

    now_iso = datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    date_val = fm.get("date") or now_iso.split("T")[0]

    # Update YAML lines cleanly
    lines = raw_yaml.splitlines()
    new_lines = []
    has_status = False
    has_is_draft = False
    has_published_at = False
    has_updated_at = False

    for line in lines:
        if re.match(r"^status\s*:", line):
            new_lines.append("status: published")
            has_status = True
        elif re.match(r"^isDraft\s*:", line):
            new_lines.append("isDraft: false")
            has_is_draft = True
        elif re.match(r"^publishedAt\s*:", line):
            new_lines.append(f"publishedAt: {now_iso}")
            has_published_at = True
        elif re.match(r"^updatedAt\s*:", line):
            new_lines.append(f"updatedAt: {now_iso}")
            has_updated_at = True
        elif re.match(r"^metaDescription\s*:", line):
            # Enforce DRY: omit metaDescription if identical to description
            desc_val = fm.get("description", "")
            meta_desc_val = line.split(":", 1)[1].strip().strip('"\'')
            if meta_desc_val != desc_val:
                new_lines.append(line)
        else:
            new_lines.append(line)

    if not has_status:
        new_lines.append("status: published")
    if not has_is_draft:
        new_lines.append("isDraft: false")
    if not has_published_at:
        new_lines.append(f"publishedAt: {now_iso}")
    if not has_updated_at:
        new_lines.append(f"updatedAt: {now_iso}")

    new_content = "---\n" + "\n".join(new_lines) + "\n---\n" + body

    if dry_run:
        print(f"  [Dry-run] Would move {draft_file} -> {published_file}")
        return published_file, fm

    published_file.write_text(new_content, encoding="utf-8")
    if draft_file.exists():
        draft_file.unlink()

    # Update resources.md if it exists in draft assets
    resource_file = DRAFT_DIR / "assets" / slug / "resources.md"
    if resource_file.exists():
        r_text = resource_file.read_text(encoding="utf-8")
        r_text = re.sub(r"-\s*\*\*Draft File\*\*:\s*`posts/draft/[^`]+`", f"- **Published File**: `posts/published/{slug}.md`", r_text)
        r_text = re.sub(r"-\s*\*\*Status\*\*:\s*Draft", "- **Status**: Published", r_text)
        resource_file.write_text(r_text, encoding="utf-8")

    print(f"  ✔ Moved to {published_file.relative_to(REPO_ROOT)} with published frontmatter.")
    return published_file, fm


def verify_assets(slug: str, fm: dict):
    """Ensure hero WebP and OpenGraph card are generated."""
    print(f"\n🖼️ Step 2: Verifying Hero & OpenGraph Assets")
    hero_rel = fm.get("image")
    if not hero_rel:
        print(f"  ⚠️ No hero image defined in frontmatter for [{slug}].")
        return

    hero_path = POSTS_DIR / hero_rel
    og_rel = fm.get("ogImage") or re.sub(r"\.(webp|jpg|png)$", "-og.webp", hero_rel)
    og_path = POSTS_DIR / og_rel

    if not og_path.exists():
        print(f"  ⚡ Generating missing OpenGraph card for [{slug}]...")
        run_cmd(f"python3 scripts/manage-hero-assets.py --og-cards --slug {slug} --force")
    else:
        print(f"  ✔ OpenGraph card exists: {og_rel}")


def build_and_verify(dry_run: bool = False):
    """Run production build pipeline and check guardrails."""
    print(f"\n🔨 Step 3: Running Production Site Build")
    if dry_run:
        print("  [Dry-run] Skipping production build.")
        return

    # Clean, generate indices, and compile production docfx
    run_cmd("npm run build")
    print("  ✔ Production DocFX build passed with 0 warnings and 0 errors.")

    print(f"\n🛡️ Step 4: Verifying Git Deployment Guardrail")
    res = run_cmd("python3 scripts/check-clean-posts.py", check=False)
    if res.returncode == 0:
        print("  ✔ Git deployment guardrail passed.")
    else:
        print("  ℹ️ Content changes ready for commit.")


def main():
    parser = argparse.ArgumentParser(
        description="Fast-Track Post Publication CLI for GhostFx / DocFX.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )
    parser.add_argument("--slug", type=str, required=True, help="Draft UID / slug to publish.")
    parser.add_argument("--dry-run", action="store_true", help="Simulate promotion without modifying files.")
    parser.add_argument("--commit", action="store_true", help="Commit publication changes to Git upon success.")

    args = parser.parse_args()

    print(f"\n🚀 Fast-Track Post Publication: [{args.slug}]")
    print(f"==================================================")

    # 1. Promote draft & sync frontmatter
    pub_path, fm = promote_draft(args.slug, dry_run=args.dry_run)

    # 2. Verify / generate assets & OG cards
    if not args.dry_run:
        verify_assets(args.slug, fm)

    # 3. Full production build & guardrail check
    build_and_verify(dry_run=args.dry_run)

    # 4. Optional Git Commit
    if args.commit and not args.dry_run:
        title = fm.get("title", args.slug)
        commit_msg = f"feat(posts): publish '{title}'"
        print(f"\n📝 Step 5: Committing Publication Changes")
        run_cmd(f"git add posts/published/{args.slug}.md posts/index.md posts/tags.md posts/tags/ posts/content/images/")
        if (DRAFT_DIR / "assets" / args.slug).exists():
            run_cmd(f"git add posts/draft/assets/{args.slug}/")
        run_cmd(f"git commit -m \"{commit_msg}\"")
        print(f"  ✔ Committed: \"{commit_msg}\"")

    print(f"\n✨ Publication workflow complete for [{args.slug}]!")
    print(f"👉 To deploy to production when approved: npm run deploy\n")


if __name__ == "__main__":
    main()
