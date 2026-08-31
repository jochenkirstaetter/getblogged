#!/usr/bin/env python3
"""
Generates posts/index.md containing the latest published articles
sorted in reverse chronological order up to _indexCount from posts/docfx.json.
"""

import json
import re
from pathlib import Path
from datetime import datetime

def unquote(val: str) -> str:
    val = val.strip()
    if len(val) >= 2:
        if (val.startswith('"') and val.endswith('"')) or (val.startswith("'") and val.endswith("'")):
            val = val[1:-1]
    return val.replace(r'\"', '"').replace(r"\'", "'")

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
    if fm.get("isErrorPage") is True or str(fm.get("isErrorPage", "")).lower() == "true" or fm.get("isPost") is False or str(fm.get("isPost", "")).lower() == "false" or file_path.name in ("404.md", "error404.md"):
        return None

    title = fm.get("title") or file_path.stem.replace("-", " ").title()
    uid = fm.get("uid") or fm.get("slug") or file_path.stem
    date_val = fm.get("publishedAt") or fm.get("date") or fm.get("updatedAt") or "1970-01-01"
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
    primary_tag = tags[0] if tags and len(tags) > 0 else "General"
    tag_slug = primary_tag.lower().replace(" ", "-")
    tag_slug = re.sub(r"[^a-z0-9_-]+", "", tag_slug)
    mtime = file_path.stat().st_mtime

    return {
        "title": title,
        "uid": uid,
        "slug": uid,
        "date": dt.strftime("%Y-%m-%d"),
        "formattedDate": dt.strftime("%b %-d, %Y") if dt.year > 1970 else "",
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
    posts_dir = repo_root / "posts"
    published_dir = posts_dir / "published"
    output_file = posts_dir / "index.md"
    docfx_cfg_file = posts_dir / "docfx.json"

    index_count = 12
    if docfx_cfg_file.exists():
        try:
            docfx_cfg = json.loads(docfx_cfg_file.read_text(encoding="utf-8"))
            index_count = int(docfx_cfg.get("build", {}).get("globalMetadata", {}).get("_indexCount", 12))
        except Exception as ex:
            print(f"Warning: Could not read _indexCount from {docfx_cfg_file}: {ex}")

    if not published_dir.exists():
        print(f"Error: {published_dir} does not exist.")
        return

    posts = []
    for f in published_dir.glob("*.md"):
        post = parse_post(f)
        if post:
            posts.append(post)

    # Sort descending by date (publishedAt/date), then by title
    posts.sort(key=lambda x: (x["dt"], x["title"]), reverse=True)

    top_posts = posts[:index_count]

    yaml_lines = [
        "---",
        "uid: home",
        'title: "Get Blogged by JoKi"',
        'description: "The only frontiers are in your mind"',
        "canonicalUrl: https://jochen.kirstaetter.name/",
        "isHome: true",
        "bodyClass: home-template",
        "posts:"
    ]

    for p in top_posts:
        t = p["title"].replace('"', '\\"')
        e = p["excerpt"].replace('"', '\\"')
        uid = p["uid"]
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
        yaml_lines.append(f"  uid: {uid}")
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
    yaml_lines.append("# Welcome to Get Blogged by JoKi")
    yaml_lines.append("")
    yaml_lines.append("Get Blogged by JoKi is the personal technology blog and knowledge base of **Jochen Kirstätter** (also known as JoKi). Based in Mauritius, Jochen is a senior software crafter, Microsoft MVP for Developer Technologies, Google Developer Expert (GDE) for Google Cloud & AI, international speaker, and founder of the Mauritius Software Craftsmanship Community (MSCC).")
    yaml_lines.append("")
    yaml_lines.append("## Core Focus & Technology Deep-Dives")
    yaml_lines.append("")
    yaml_lines.append("- **.NET & Modern C#**: Practical architectural patterns, cross-platform app development, minimal APIs, NuGet package authoring, and performance optimisation.")
    yaml_lines.append("- **Google Cloud & Gemini AI**: Integrating Google Gemini API and Vertex AI in .NET using `Mscc.GenerativeAI`, structured outputs (`ResponseSchema`), and autonomous multi-agent systems.")
    yaml_lines.append("- **Developer Tooling & Cloud Workflows**: Practical experiences with Google Antigravity Remote Control, Docker containers, Google Cloud Build, Portless local reverse proxying, and CI/CD pipelines.")
    yaml_lines.append("- **Software Craftsmanship & Community**: Insights from running monthly MSCC meetups and the annual Developers Conference Mauritius.")
    yaml_lines.append("")
    yaml_lines.append("## Agent & Machine-Readable Access")
    yaml_lines.append("")
    yaml_lines.append("This website is built for both human software crafters and autonomous AI agents:")
    yaml_lines.append("- **Agent Guidance & When to Use**: See [`/llms.txt`](https://jochen.kirstaetter.name/llms.txt) and [`/llms-full.txt`](https://jochen.kirstaetter.name/llms-full.txt) for machine-readable manifests and best-fit use case definitions.")
    yaml_lines.append("- **Markdown Content Negotiation**: All articles provide raw, token-efficient Markdown sources via `Accept: text/markdown` or directly under `/raw/<slug>.md`.")
    yaml_lines.append("- **Site Navigation & Trust**: Explore our [About](xref:about), [Contact](xref:contact), [Privacy Policy](xref:privacy), [Blog Archive](xref:blog), and [Topic Tags](xref:tags-index).")
    yaml_lines.append("")

    content_str = "\n".join(yaml_lines)
    output_file.write_text(content_str, encoding="utf-8")
    print(f"Successfully generated {output_file} with {len(top_posts)} published posts (limited to _indexCount={index_count}).")

if __name__ == "__main__":
    main()
