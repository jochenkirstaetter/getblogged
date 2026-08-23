#!/usr/bin/env python3
"""
Generates posts/index-draft.md containing all draft articles sorted in reverse chronological order.
"""

import re
from pathlib import Path
from datetime import datetime

def parse_post(file_path: Path) -> dict:
    content = file_path.read_text(encoding="utf-8")
    fm = {}
    body = ""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if match:
        raw_yaml = match.group(1)
        body = match.group(2)
        current_list = None
        for line in raw_yaml.splitlines():
            list_match = re.match(r"^\s*-\s+(.*)$", line)
            if list_match and current_list is not None:
                fm[current_list].append(list_match.group(1).strip("\"'"))
                continue
            
            kv_match = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
            if kv_match:
                k = kv_match.group(1).strip()
                v = kv_match.group(2).strip().strip("\"'")
                if v == "" or v == "[]":
                    fm[k] = []
                    current_list = k
                else:
                    fm[k] = v
                    current_list = None
    else:
        body = content

    title = fm.get("title") or file_path.stem.replace("-", " ").title()
    slug = fm.get("slug") or file_path.stem
    date_val = fm.get("date") or fm.get("updatedAt") or fm.get("publishedAt") or "1970-01-01"
    date_str = str(date_val).split("T")[0]
    
    try:
        dt = datetime.strptime(date_str, "%Y-%m-%d")
    except Exception:
        dt = datetime(1970, 1, 1)

    image = fm.get("image") or fm.get("featureImage") or fm.get("imageUrl") or ""
    
    excerpt = fm.get("excerpt") or fm.get("description") or fm.get("metaDescription") or ""
    if (not excerpt or excerpt.strip() == "") and body:
        for p in body.split("\n\n"):
            p_strip = p.strip()
            if p_strip and not p_strip.startswith("#") and not p_strip.startswith("!") and not p_strip.startswith("```"):
                clean_p = re.sub(r"\[([^\]]+)\]\([^\)]+\)", r"\1", p_strip)
                clean_p = re.sub(r"[*_`]", "", clean_p)
                clean_p = " ".join(clean_p.split())
                excerpt = clean_p[:220] + ("..." if len(clean_p) > 220 else "")
                break

    tags = fm.get("tags") or []
    if isinstance(tags, str):
        tags = [t.strip() for t in tags.split(",") if t.strip()]
    primary_tag = tags[0] if tags and len(tags) > 0 else "Development"
    tag_slug = primary_tag.lower().replace(" ", "-")
    mtime = file_path.stat().st_mtime

    return {
        "title": title,
        "slug": slug,
        "date": dt.strftime("%Y-%m-%d"),
        "formattedDate": dt.strftime("%b %-d, %Y") if dt.year > 1970 else "Draft",
        "dt": dt,
        "mtime": mtime,
        "image": image,
        "excerpt": excerpt,
        "authorName": fm.get("author") or "Jochen Kirstätter",
        "authorSlug": fm.get("authorSlug") or "joki",
        "authorImage": fm.get("authorImage") or "content/images/2018/10/JoKi_StAubin_100px.webp",
        "primaryTag": primary_tag,
        "tagSlug": tag_slug,
        "tagClass": f"tag-{tag_slug}",
        "imageClass": "with-image" if image else "no-image"
    }

def main():
    repo_root = Path(__file__).resolve().parent.parent
    draft_dir = repo_root / "posts" / "draft"
    output_file = draft_dir / "index.md"
    legacy_output_file = repo_root / "posts" / "index-draft.md"

    # Clean up legacy index-draft.md if it exists
    if legacy_output_file.exists():
        legacy_output_file.unlink()

    posts = [
        parse_post(p)
        for p in draft_dir.glob("*.md")
        if not p.name.startswith(".") and p.name not in ("toc.yml", "index.md", "index-draft.md") and "assets" not in p.parts
    ]
    posts.sort(key=lambda x: (x["dt"], x["mtime"], x["title"]), reverse=True)

    yaml_lines = [
        "---",
        "uid: home",
        "title: Get Blogged by JoKi (Drafts)",
        "description: Draft articles and works in progress",
        "coverImage: content/images/2023/07/GDG_Google_Banner.webp",
        "isHome: true",
        "bodyClass: home-template",
        "posts:"
    ]

    for p in posts:
        t = p["title"].replace('"', '\\"')
        e = p["excerpt"].replace('"', '\\"')
        slug = p["slug"]
        date = p["date"]
        formatted_date = p["formattedDate"]
        image = p["image"]
        author_name = p["authorName"]
        author_slug = p["authorSlug"]
        author_image = p["authorImage"]
        primary_tag = p["primaryTag"]
        tag_slug = p["tagSlug"]
        tag_class = p["tagClass"]
        image_class = p["imageClass"]

        yaml_lines.append(f'- title: "{t}"')
        yaml_lines.append(f"  slug: {slug}")
        yaml_lines.append(f"  date: {date}")
        yaml_lines.append(f"  formattedDate: {formatted_date}")
        if image:
            yaml_lines.append(f"  image: {image}")
        else:
            yaml_lines.append("  image: ''")
        yaml_lines.append(f'  excerpt: "{e}"')
        yaml_lines.append(f"  authorName: {author_name}")
        yaml_lines.append(f"  authorSlug: {author_slug}")
        yaml_lines.append(f"  authorImage: {author_image}")
        yaml_lines.append(f"  primaryTag: {primary_tag}")
        yaml_lines.append(f"  tagSlug: {tag_slug}")
        yaml_lines.append(f"  tagClass: {tag_class}")
        yaml_lines.append(f"  imageClass: {image_class}")

    yaml_lines.append("---")
    yaml_lines.append("")

    content_str = "\n".join(yaml_lines)
    output_file.write_text(content_str, encoding="utf-8")
    print(f"Successfully generated {output_file} with {len(posts)} draft posts.")

if __name__ == "__main__":
    main()


