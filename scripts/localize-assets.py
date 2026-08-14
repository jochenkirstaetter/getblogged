#!/usr/bin/env python3
"""
Asset Localization, WebP Migration & Attribution Tool for GhostFx / DocFX.
"""

import os
import sys
import re
import json
import glob
import urllib.request
import urllib.parse
from pathlib import Path
from PIL import Image

REPO_ROOT = Path(__file__).resolve().parent.parent
DOCFX_JSON = REPO_ROOT / "posts" / "docfx.json"
POSTS_DIR = REPO_ROOT / "posts"
CONTENT_IMAGES_DIR = POSTS_DIR / "content" / "images"
SIZE_DIR = CONTENT_IMAGES_DIR / "size"
GHOST_SIZES = [300, 600, 1000, 1600, 2000]

IGNORED_DOMAINS = [
    "assoc-amazon.com",
    "amazon-adsystem.com",
    "amazon.com",
    "feedburner.com",
    "statcounter.com",
    "doubleclick.net",
    "google-analytics.com",
    "googlesyndication.com",
    "wikipedia.org",
    "teepublic.com",
    "brring.com",
    "microsoft.com"
]

DOWNLOADED_CACHE = {}

def load_app_url():
    try:
        with open(DOCFX_JSON, "r", encoding="utf-8") as f:
            data = json.load(f)
            return data.get("build", {}).get("globalMetadata", {}).get("_appUrl", "https://jochen.kirstaetter.name")
    except Exception as e:
        print(f"Warning: Could not read _appUrl from docfx.json: {e}")
        return "https://jochen.kirstaetter.name"

def extract_attribution(url):
    domain = urllib.parse.urlparse(url).netloc.lower()
    if "unsplash.com" in domain:
        return "Photo on Unsplash"
    elif "flickr.com" in domain:
        return "Photo on Flickr"
    elif "wikimedia.org" in domain:
        return "Photo via Wikimedia"
    elif domain:
        clean_domain = domain.replace("www.", "")
        return f"Image via {clean_domain}"
    return "External Source"

def extract_remote_filename(url, fallback_slug):
    parsed = urllib.parse.urlparse(url)
    path = parsed.path
    basename = os.path.basename(path)
    if "?" in basename:
        basename = basename.split("?")[0]
    name_no_ext, _ = os.path.splitext(basename)
    if name_no_ext and len(name_no_ext) > 3:
        return f"{name_no_ext}.webp"
    return f"{fallback_slug}.webp"

def save_and_generate_variants(img, base_target_path):
    base_target_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Save base full-res WebP if not already present
    if not base_target_path.exists():
        if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
            img.save(base_target_path, "WEBP", quality=85, method=4)
        else:
            rgb_img = img.convert("RGB")
            rgb_img.save(base_target_path, "WEBP", quality=85, method=4)
    
    rel_from_images = base_target_path.relative_to(CONTENT_IMAGES_DIR)
    
    orig_w, orig_h = img.size
    for size_w in GHOST_SIZES:
        size_dir = SIZE_DIR / f"w{size_w}" / rel_from_images.parent
        size_dir.mkdir(parents=True, exist_ok=True)
        size_target_path = size_dir / base_target_path.name
        if size_target_path.exists():
            continue
            
        if orig_w > size_w:
            ratio = size_w / float(orig_w)
            size_h = max(1, int(float(orig_h) * ratio))
            resized = img.resize((size_w, size_h), Image.Resampling.LANCZOS)
            if resized.mode in ("RGBA", "LA") or (resized.mode == "P" and "transparency" in resized.info):
                resized.save(size_target_path, "WEBP", quality=82, method=4)
            else:
                resized.convert("RGB").save(size_target_path, "WEBP", quality=82, method=4)
        else:
            if img.mode in ("RGBA", "LA") or (img.mode == "P" and "transparency" in img.info):
                img.save(size_target_path, "WEBP", quality=85, method=4)
            else:
                img.convert("RGB").save(size_target_path, "WEBP", quality=85, method=4)

def process_image(url_or_path, post_date_str, post_slug, app_url, dry_run=False):
    clean_url = url_or_path.strip()
    is_external = False
    
    for ign in IGNORED_DOMAINS:
        if ign in clean_url:
            return None, None

    if clean_url in DOWNLOADED_CACHE:
        return DOWNLOADED_CACHE[clean_url]
    
    if clean_url.startswith("http://") or clean_url.startswith("https://") or clean_url.startswith("//"):
        if clean_url.startswith(app_url):
            path_part = clean_url[len(app_url):].lstrip("/")
            local_src = POSTS_DIR / path_part
            is_external = False
        else:
            is_external = True
    else:
        path_part = clean_url.lstrip("/")
        local_src = POSTS_DIR / path_part
        is_external = False
    
    if is_external:
        try:
            year = post_date_str.split("-")[0] if post_date_str else "2026"
            month = post_date_str.split("-")[1] if post_date_str and len(post_date_str.split("-")) > 1 else "01"
        except Exception:
            year, month = "2026", "01"
        target_filename = extract_remote_filename(clean_url, post_slug)
        target_rel_path = f"content/images/{year}/{month}/{target_filename}"
        attribution = extract_attribution(clean_url)
    else:
        if path_part.startswith("content/images/"):
            rel_under_images = path_part[len("content/images/"):].lstrip("/")
        else:
            rel_under_images = path_part
        
        name_no_ext, _ = os.path.splitext(rel_under_images)
        target_rel_path = f"content/images/{name_no_ext}.webp"
        attribution = None

    target_full_path = POSTS_DIR / target_rel_path
    
    if dry_run:
        DOWNLOADED_CACHE[clean_url] = (target_rel_path, attribution)
        return target_rel_path, attribution
    
    # Check if target webp already exists
    if target_full_path.exists() and (SIZE_DIR / "w600" / target_full_path.relative_to(CONTENT_IMAGES_DIR)).exists():
        DOWNLOADED_CACHE[clean_url] = (target_rel_path, attribution)
        return target_rel_path, attribution

    img = None
    if is_external:
        print(f"  [Download] {clean_url} -> {target_rel_path}")
        req = urllib.request.Request(clean_url, headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})
        try:
            with urllib.request.urlopen(req, timeout=2.5) as resp:
                import io
                img_data = resp.read()
                img = Image.open(io.BytesIO(img_data))
        except Exception as e:
            print(f"  [Skip/Error] Failed to download {clean_url}: {e}")
            DOWNLOADED_CACHE[clean_url] = (None, None)
            return None, None
    else:
        if not local_src.exists():
            if target_full_path.exists():
                try:
                    img = Image.open(target_full_path)
                except Exception:
                    pass
            if not img:
                DOWNLOADED_CACHE[clean_url] = (None, None)
                return None, None
        else:
            try:
                img = Image.open(local_src)
            except Exception as e:
                print(f"  [ERROR] Failed to open local image {local_src}: {e}")
                DOWNLOADED_CACHE[clean_url] = (None, None)
                return None, None
    
    if img:
        save_and_generate_variants(img, target_full_path)
        DOWNLOADED_CACHE[clean_url] = (target_rel_path, attribution)
        return target_rel_path, attribution
    
    DOWNLOADED_CACHE[clean_url] = (None, None)
    return None, None

def process_markdown_file(file_path, app_url, dry_run=False):
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    fm_match = re.match(r"^---\s*\n(.*?)\n---\s*\n(.*)$", content, re.DOTALL)
    if not fm_match:
        return False
    
    frontmatter = fm_match.group(1)
    body = fm_match.group(2)
    
    date_match = re.search(r"^date:\s*['\"]?([0-9]{4}-[0-9]{2}-[0-9]{2})", frontmatter, re.MULTILINE)
    post_date = date_match.group(1) if date_match else "2026-01-01"
    
    slug_match = re.search(r"^slug:\s*['\"]?([^\s'\"]+)", frontmatter, re.MULTILINE)
    post_slug = slug_match.group(1) if slug_match else Path(file_path).stem
    
    modified = False
    added_attribution = None
    
    fm_fields = ["image", "featureImage", "imageUrl", "coverImage", "authorImage", "authorImageUrl"]
    
    for field in fm_fields:
        field_match = re.search(rf"^{field}:\s*['\"]?([^\s'\"]+)['\"]?", frontmatter, re.MULTILINE)
        if field_match:
            original_val = field_match.group(1).strip('\"\'')
            # Normalize any ../content/images/ in frontmatter to content/images/
            clean_fm_val = original_val
            if clean_fm_val.startswith("../content/images/"):
                clean_fm_val = clean_fm_val.replace("../content/images/", "content/images/")
                
            is_http = clean_fm_val.startswith("http://") or clean_fm_val.startswith("https://") or clean_fm_val.startswith("//")
            is_unoptimized = clean_fm_val.endswith(".jpg") or clean_fm_val.endswith(".png") or clean_fm_val.endswith(".jpeg")
            
            if is_http or is_unoptimized:
                new_rel, attr = process_image(clean_fm_val, post_date, post_slug, app_url, dry_run)
                if new_rel:
                    clean_fm_val = new_rel
                    if attr and field in ("image", "featureImage", "imageUrl", "coverImage") and not added_attribution:
                        added_attribution = attr
                        
            if clean_fm_val != original_val:
                frontmatter = re.sub(
                    rf"^{field}:\s*['\"]?.*$",
                    f"{field}: {clean_fm_val}",
                    frontmatter,
                    flags=re.MULTILINE
                )
                modified = True

    if added_attribution:
        if not re.search(r"^imageAttribution:", frontmatter, re.MULTILINE):
            frontmatter += f"\nimageAttribution: \"{added_attribution}\""
            modified = True
            
    # Handle remote/full URL inline images
    inline_images = re.findall(r"!\[(.*?)\]\((https?://[^\s\)]+)\)", body)
    for alt_text, img_url in inline_images:
        new_rel, _ = process_image(img_url, post_date, post_slug, app_url, dry_run)
        if new_rel:
            body_rel = f"../{new_rel}" if not new_rel.startswith("../") else new_rel
            body = body.replace(f"![{alt_text}]({img_url})", f"![{alt_text}]({body_rel})")
            modified = True
            
    # Also fix any inline images with content/images/ lacking ../ or with unoptimized extensions
    inline_local = re.findall(r"!\[(.*?)\]\(((?:\.\./)?content/images/[^\s\)]+)\)", body)
    for alt_text, img_url in inline_local:
        clean_url = img_url.lstrip(".")
        if not clean_url.startswith("/"):
            clean_url = "/" + clean_url
        new_rel, _ = process_image(clean_url, post_date, post_slug, app_url, dry_run)
        target_body_rel = f"../{new_rel}" if new_rel else (f"../{img_url}" if not img_url.startswith("../") else img_url)
        if target_body_rel != img_url:
            body = body.replace(f"![{alt_text}]({img_url})", f"![{alt_text}]({target_body_rel})")
            modified = True

    if modified and not dry_run:
        new_content = f"---\n{frontmatter}\n---\n{body}"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(new_content)
        return True
    
    return modified

def main():
    dry_run = "--dry-run" in sys.argv
    app_url = load_app_url()
    
    print(f"=== GhostFx Asset Localization & WebP Migration ===")
    print(f"App URL: {app_url}")
    print(f"Mode: {'DRY RUN' if dry_run else 'LIVE MIGRATION'}")
    
    all_md_patterns = [
        str(REPO_ROOT / "posts" / "published" / "*.md"),
        str(REPO_ROOT / "posts" / "pages" / "*.md"),
        str(REPO_ROOT / "posts" / "draft" / "*.md"),
        str(REPO_ROOT / "posts" / "author" / "*.md"),
        str(REPO_ROOT / "posts" / "tags" / "*.md"),
        str(REPO_ROOT / "posts" / "*.md")
    ]
    
    post_files = []
    for pat in all_md_patterns:
        post_files.extend(glob.glob(pat))
    post_files = sorted(set(post_files))
    
    print(f"Found {len(post_files)} markdown documents across published, pages, draft, author, tags, and root.\n")
    
    processed_count = 0
    for idx, post_file in enumerate(post_files, 1):
        rel_post = os.path.relpath(post_file, REPO_ROOT)
        was_mod = process_markdown_file(post_file, app_url, dry_run=dry_run)
        if was_mod:
            processed_count += 1
            print(f"[{idx}/{len(post_files)}] Processed: {rel_post}")
            
    print(f"\nMigration completed. {processed_count} files processed/updated.")

if __name__ == "__main__":
    main()
