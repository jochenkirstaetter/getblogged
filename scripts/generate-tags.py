#!/usr/bin/env python3
"""
Generates posts/tags.md, individual tag pages in posts/tags/<slug>.md,
and posts/tags/toc.yml from frontmatter tags of published posts.
"""

import re
from pathlib import Path
from datetime import datetime
from collections import defaultdict

def unquote(val: str) -> str:
    val = val.strip()
    if len(val) >= 2:
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
    return val.replace(r'\"', '"').replace(r"\'", "'")

def parse_post(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return {}
    
    raw_yaml = match.group(1)
    fm = {}
    current_list = None
    
    for line in raw_yaml.splitlines():
        list_match = re.match(r"^\s*-\s+(.*)$", line)
        if list_match and current_list is not None:
            fm[current_list].append(unquote(list_match.group(1)))
            continue
        
        kv_match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
        if kv_match:
            k = kv_match.group(1).strip()
            v = kv_match.group(2).strip()
            if v == "" or v == "[]":
                fm[k] = []
                current_list = k
            elif v.startswith("[") and v.endswith("]"):
                fm[k] = [unquote(item) for item in v[1:-1].split(",") if item.strip()]
                current_list = None
            else:
                fm[k] = unquote(v)
                current_list = None

    uid = fm.get("uid") or file_path.stem
    title = fm.get("title") or file_path.stem.replace("-", " ").title()
    date_val = fm.get("date") or fm.get("publishedAt") or fm.get("updatedAt") or "1970-01-01"
    date_str = str(date_val).split("T")[0]
    
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        dt = datetime(1970, 1, 1)

    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]

    return {
        "uid": uid,
        "title": title,
        "date": date_str,
        "dt": dt,
        "tags": tags,
        "file_path": file_path
    }

def read_existing_tag_metadata(tags_dir: Path) -> dict:
    """Reads existing tag files to preserve custom images, descriptions, and file naming."""
    metadata = {}
    if not tags_dir.exists():
        return metadata

    for f in tags_dir.glob("*.md"):
        if f.name.startswith("."):
            continue
        try:
            content = f.read_text(encoding="utf-8")
            match = re.match(r"^---\s*\n(.*?)\n---", content, re.DOTALL)
            if match:
                raw_yaml = match.group(1)
                tag_name = None
                image = None
                description = None
                for line in raw_yaml.splitlines():
                    if line.startswith("tagName:"):
                        tag_name = unquote(line.split("tagName:", 1)[1])
                    elif line.startswith("title:") and not tag_name:
                        tag_name = unquote(line.split("title:", 1)[1])
                    elif line.startswith("image:"):
                        image = unquote(line.split("image:", 1)[1])
                    elif line.startswith("description:"):
                        description = unquote(line.split("description:", 1)[1])
                
                if tag_name:
                    metadata[tag_name] = {
                        "filename": f.name,
                        "slug": f.stem,
                        "image": image,
                        "description": description
                    }
        except Exception as e:
            print(f"Warning reading {f}: {e}")

    return metadata

def get_tag_slug(tag_name: str, existing_metadata: dict) -> str:
    # Specific known canonical mappings
    slug_overrides = {
        "Projects": "project"
    }
    if tag_name in slug_overrides:
        return slug_overrides[tag_name]

    if tag_name in existing_metadata and "slug" in existing_metadata[tag_name]:
        return existing_metadata[tag_name]["slug"]

    slug = tag_name.lower().replace(" ", "-")
    slug = re.sub(r"[^a-z0-9_-]+", "", slug)
    return slug

def main():
    import sys
    repo_root = Path(__file__).resolve().parent.parent
    posts_dir = repo_root / "posts"
    published_dir = posts_dir / "published"
    draft_dir = posts_dir / "draft"
    tags_dir = posts_dir / "tags"
    tags_index_file = posts_dir / "tags.md"
    toc_file = tags_dir / "toc.yml"

    tags_dir.mkdir(parents=True, exist_ok=True)
    existing_meta = read_existing_tag_metadata(tags_dir)
    for f in tags_dir.glob("*.md"):
        try:
            f.unlink()
        except OSError:
            pass

    posts_by_tag = defaultdict(list)

    post_files = list(published_dir.glob("*.md"))
    if "--draft" in sys.argv and draft_dir.exists():
        post_files.extend([
            p for p in draft_dir.glob("*.md")
            if p.name not in ("toc.yml", "index.md", "index-draft.md") and "assets" not in p.parts
        ])

    for post_file in sorted(post_files):
        if post_file.name.startswith("."):
            continue
        post = parse_post(post_file)
        if not post or not post.get("uid"):
            continue
        for tag in post.get("tags", []):
            clean_tag = tag.strip()
            if clean_tag:
                posts_by_tag[clean_tag].append(post)

    sorted_tag_names = sorted(posts_by_tag.keys(), key=lambda s: s.lower())

    # 1. Generate posts/tags.md
    tags_index_lines = [
        "---",
        "uid: tags-index",
        'title: "Browse by Tag"',
        "layout: tags",
        "isTagsIndexPage: true",
        'bodyClass: "tag-template tag-index-template"',
        "---",
        "",
        "# Browse Content by Tag",
        ""
    ]

    for tag in sorted_tag_names:
        slug = get_tag_slug(tag, existing_meta)
        count = len(posts_by_tag[tag])
        tags_index_lines.append(f"- [{tag} ({count})](tags/{slug}.md)")

    tags_index_lines.append("")
    tags_index_file.write_text("\n".join(tags_index_lines), encoding="utf-8")
    print(f"Generated {tags_index_file} with {len(sorted_tag_names)} tags.")

    # 2. Generate individual tag pages (posts/tags/<slug>.md)
    toc_entries = []
    for tag in sorted_tag_names:
        slug = get_tag_slug(tag, existing_meta)
        tag_file = tags_dir / f"{slug}.md"
        posts = posts_by_tag[tag]
        posts.sort(key=lambda x: (x["dt"], x["title"]), reverse=True)

        meta = existing_meta.get(tag, {})
        tag_lines = [
            "---",
            f"uid: tag-{slug}",
            f'title: "{tag}"',
            "layout: tag",
            "isTagPage: true",
            f'bodyClass: "tag-template tag-{slug}"',
            f'tagName: "{tag}"'
        ]

        if meta.get("image"):
            tag_lines.append(f"image: {meta['image']}")
        if meta.get("description"):
            tag_lines.append(f'description: "{meta["description"]}"')

        tag_lines.extend([
            "---",
            "",
            f"# Tag: {tag}",
            "",
            "## Articles",
            ""
        ])

        for p in posts:
            title = p["title"]
            uid = p["uid"]
            date_str = p["date"]
            tag_lines.append(f"- [{title}](xref:{uid}) - *{date_str}*")

        tag_lines.append("")
        tag_file.write_text("\n".join(tag_lines), encoding="utf-8")
        if slug == "project":
            proj_lines = [line.replace("uid: tag-project", "uid: tag-projects") for line in tag_lines]
            (tags_dir / "projects.md").write_text("\n".join(proj_lines), encoding="utf-8")

        toc_entries.append(f'- name: "{tag}"\n  href: {slug}.md')

    print(f"Generated {len(sorted_tag_names)} tag detail pages in {tags_dir}.")

    # 3. Generate posts/tags/toc.yml
    toc_content = "\n".join(toc_entries) + "\n"
    toc_file.write_text(toc_content, encoding="utf-8")
    print(f"Generated {toc_file}.")

    # 4. Generate posts/ghostfx/partials/meta-tasks.tmpl.partial for dynamic msapplication-task tags
    meta_tasks_file = posts_dir / "ghostfx" / "partials" / "meta-tasks.tmpl.partial"
    meta_task_lines = []
    icon_map = {
        "Linux": "/linux.ico",
        "Android": "/android.ico",
        "iOS": "/apple.ico"
    }
    for tag in sorted_tag_names:
        slug = get_tag_slug(tag, existing_meta)
        ico = icon_map.get(tag, "/favicon.ico")
        meta_task_lines.append(
            f'<meta name="msapplication-task" content="name={tag};action-uri={{{{#_appUrl}}}}{{{{_appUrl}}}}/{{{{/_appUrl}}}}tags/{slug}.html;icon-uri={ico}" />'
        )
    meta_tasks_file.write_text("\n".join(meta_task_lines) + "\n", encoding="utf-8")
    print(f"Generated {meta_tasks_file} with {len(sorted_tag_names)} tasks.")

if __name__ == "__main__":
    main()
