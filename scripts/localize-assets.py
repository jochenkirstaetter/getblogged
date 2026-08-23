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
from PIL import Image, ImageDraw, ImageFont, ImageFilter, ImageOps

# Ensure scripts directory is in path for qr_generator import
sys.path.insert(0, str(Path(__file__).resolve().parent))
from qr_generator import generate_qr_image

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

def get_font(font_name='bold', size=32):
    font_paths = {
        'bold': [
            '/usr/share/fonts/truetype/noto/NotoSans-Bold.ttf',
            '/usr/share/fonts/opentype/urw-base35/NimbusSans-Bold.otf',
            '/usr/share/fonts/opentype/cantarell/Cantarell-VF.otf',
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf',
        ],
        'regular': [
            '/usr/share/fonts/truetype/noto/NotoSans-Regular.ttf',
            '/usr/share/fonts/opentype/urw-base35/NimbusSans-Regular.otf',
            '/usr/share/fonts/opentype/cantarell/Cantarell-VF.otf',
            '/usr/share/fonts/truetype/droid/DroidSansFallbackFull.ttf',
            '/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf',
        ],
        'mono': [
            '/usr/share/fonts/truetype/noto/NotoSansMono-Bold.ttf',
            '/usr/share/fonts/opentype/urw-base35/NimbusMonoPS-Bold.otf',
        ]
    }
    for p in font_paths.get(font_name, font_paths['bold']):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                pass
    return ImageFont.load_default()

def balance_wrap_text(text, font, max_width, draw):
    words = text.split()
    if not words:
        return []
    single = ' '.join(words)
    b = draw.textbbox((0, 0), single, font=font)
    if b[2] - b[0] <= max_width:
        return [single]
        
    total_w = b[2] - b[0]
    num_lines = max(2, int(total_w / max_width) + 1)
    target_line_w = total_w / num_lines
    
    lines = []
    curr = []
    for w in words:
        test_line = ' '.join(curr + [w])
        bbox = draw.textbbox((0, 0), test_line, font=font)
        line_w = bbox[2] - bbox[0]
        if line_w > max_width and curr:
            lines.append(' '.join(curr))
            curr = [w]
        elif line_w >= target_line_w and len(lines) < num_lines - 1 and len(curr) >= 2:
            lines.append(' '.join(curr + [w]))
            curr = []
        else:
            curr.append(w)
    if curr:
        lines.append(' '.join(curr))
    return lines

def render_intelligent_og_image(hero_img_path, title, slug, app_url='https://jochen.kirstaetter.name', author='Jochen Kirstätter', output_path=None, overwrite=False):
    if output_path and Path(output_path).exists() and not overwrite:
        return
    
    width, height = 1200, 630
    
    # 1. Base hero image backdrop
    if hero_img_path and Path(hero_img_path).exists():
        try:
            src_img = Image.open(hero_img_path).convert('RGB')
            base_img = ImageOps.fit(src_img, (width, height), method=Image.Resampling.LANCZOS, centering=(0.5, 0.5))
            backdrop = base_img.filter(ImageFilter.GaussianBlur(radius=5))
        except Exception:
            backdrop = Image.new('RGB', (width, height), (30, 41, 59))
    else:
        backdrop = Image.new('RGB', (width, height), (30, 41, 59))

    canvas = backdrop.convert('RGBA')
    temp_draw = ImageDraw.Draw(canvas)
    
    # 2. Dynamic Balanced Title
    if len(title) < 35:
        title_font_size = 52
        max_title_w = 780
    elif len(title) < 65:
        title_font_size = 46
        max_title_w = 820
    elif len(title) < 95:
        title_font_size = 40
        max_title_w = 850
    else:
        title_font_size = 35
        max_title_w = 880

    font_title = get_font('bold', title_font_size)
    title_lines = balance_wrap_text(title, font_title, max_title_w, temp_draw)
    
    line_spacing = int(title_font_size * 1.28)
    line_widths = [temp_draw.textbbox((0, 0), line, font=font_title)[2] - temp_draw.textbbox((0, 0), line, font=font_title)[0] for line in title_lines]
    max_measured_w = max(line_widths) if line_widths else 400
    title_block_h = len(title_lines) * line_spacing

    pad_left = 60
    pad_right = 44
    pad_v = 30
    
    card_top = 80
    card_bottom = card_top + title_block_h + pad_v * 2
    card_w = pad_left + max_measured_w + pad_right

    # 3. Left-Attached Frosted Glass Plates (42% opacity: alpha = 107)
    frosted_overlay = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    f_draw = ImageDraw.Draw(frosted_overlay)

    glass_fill = (20, 30, 48, 107)
    glass_border = (255, 255, 255, 52)

    f_draw.rounded_rectangle(
        [(-20, card_top), (card_w, card_bottom)],
        radius=20,
        fill=glass_fill,
        outline=glass_border,
        width=1
    )

    # 4. Bottom-Left Author Attribution Plate
    font_author = get_font('bold', 25)
    font_url = get_font('regular', 21)
    clean_domain = app_url.replace('https://', '').replace('http://', '').rstrip('/')
    
    b_author = temp_draw.textbbox((0, 0), author, font=font_author)
    b_url = temp_draw.textbbox((0, 0), clean_domain, font=font_url)
    bottom_text_w = max(b_author[2] - b_author[0], b_url[2] - b_url[0])
    
    bottom_card_top = 490
    bottom_card_bottom = 598
    bottom_card_w = pad_left + bottom_text_w + 40
    
    f_draw.rounded_rectangle(
        [(-20, bottom_card_top), (bottom_card_w, bottom_card_bottom)],
        radius=18,
        fill=glass_fill,
        outline=glass_border,
        width=1
    )

    # Soft Shadow
    shadow_layer = Image.new('RGBA', (width, height), (0, 0, 0, 0))
    s_draw = ImageDraw.Draw(shadow_layer)
    s_draw.rounded_rectangle([(-20, card_top + 4), (card_w + 4, card_bottom + 6)], radius=20, fill=(0, 0, 0, 50))
    s_draw.rounded_rectangle([(-20, bottom_card_top + 4), (bottom_card_w + 4, bottom_card_bottom + 6)], radius=18, fill=(0, 0, 0, 50))
    shadow_layer = shadow_layer.filter(ImageFilter.GaussianBlur(radius=8))

    canvas = Image.alpha_composite(canvas, shadow_layer)
    canvas = Image.alpha_composite(canvas, frosted_overlay)
    draw = ImageDraw.Draw(canvas)

    # 5. Draw Title Text (Off-white with soft shadow)
    title_y_start = card_top + pad_v
    for i, line in enumerate(title_lines):
        draw.text((pad_left + 1, title_y_start + i * line_spacing + 1), line, fill=(0, 0, 0, 210), font=font_title)
        draw.text((pad_left, title_y_start + i * line_spacing), line, fill=(248, 250, 252, 255), font=font_title)

    # 6. Draw Bottom-Left Author & URL
    author_y = bottom_card_top + 20
    url_y = bottom_card_top + 56
    
    draw.text((pad_left + 1, author_y + 1), author, fill=(0, 0, 0, 200), font=font_author)
    draw.text((pad_left, author_y), author, fill=(248, 250, 252, 255), font=font_author)
    
    draw.text((pad_left + 1, url_y + 1), clean_domain, fill=(0, 0, 0, 200), font=font_url)
    draw.text((pad_left, url_y), clean_domain, fill=(186, 200, 218, 255), font=font_url)

    # 7. Frosted-Glass QR Code (Extension-less URL with center favicon logo matching JS QRCode)
    clean_app_url = app_url.rstrip('/')
    post_url = f'{clean_app_url}/{slug}'  # Extension-less URL
    favicon_path = str(POSTS_DIR / "favicon.png")
    
    qr_img = generate_qr_image(
        post_url,
        box_size=4,
        border=1,
        fg_color=(17, 24, 39, 255),
        bg_color=(255, 255, 255, 255),
        logo_path=favicon_path if Path(favicon_path).exists() else None,
        logo_size_ratio=0.24
    )
    
    qr_card_w = 176
    qr_card_h = 196
    qr_card_x = width - qr_card_w - 48
    qr_card_y = height - qr_card_h - 32
    
    glass_card = Image.new('RGBA', (qr_card_w, qr_card_h), (0, 0, 0, 0))
    glass_draw = ImageDraw.Draw(glass_card)
    
    glass_draw.rounded_rectangle(
        [(0, 0), (qr_card_w, qr_card_h)],
        radius=18,
        fill=(255, 255, 255, 235),
        outline=(255, 255, 255, 250),
        width=2
    )
    
    font_qr_label = get_font('bold', 12)
    label_text = 'SCAN TO READ'
    l_bbox = glass_draw.textbbox((0, 0), label_text, font=font_qr_label)
    lw = l_bbox[2] - l_bbox[0]
    glass_draw.text(((qr_card_w - lw) // 2, 12), label_text, fill=(30, 41, 59, 240), font=font_qr_label)
    
    qr_resized = qr_img.resize((136, 136), Image.Resampling.LANCZOS)
    qr_pos_x = (qr_card_w - qr_resized.width) // 2
    qr_pos_y = 36
    glass_card.paste(qr_resized, (qr_pos_x, qr_pos_y), qr_resized if qr_resized.mode == 'RGBA' else None)
    
    shadow = Image.new('RGBA', (qr_card_w + 24, qr_card_h + 24), (0, 0, 0, 0))
    sh_draw = ImageDraw.Draw(shadow)
    sh_draw.rounded_rectangle([(12, 12), (qr_card_w + 12, qr_card_h + 12)], radius=18, fill=(0, 0, 0, 110))
    shadow = shadow.filter(ImageFilter.GaussianBlur(radius=10))
    
    canvas.paste(shadow, (qr_card_x - 12, qr_card_y - 8), shadow)
    canvas.paste(glass_card, (qr_card_x, qr_card_y), glass_card)

    final_output = canvas.convert('RGB')
    if output_path:
        Path(output_path).parent.mkdir(parents=True, exist_ok=True)
        final_output.save(output_path, 'WEBP', quality=90, method=4)
    return final_output

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
    
    title_match = re.search(r"^title:\s*['\"]?(.*?)['\"]?$", frontmatter, re.MULTILINE)
    post_title = title_match.group(1).strip() if title_match else Path(file_path).stem.replace("-", " ").title()
    
    author_match = re.search(r"^author:\s*['\"]?(.*?)['\"]?$", frontmatter, re.MULTILINE)
    author_name = author_match.group(1).strip() if author_match else "Jochen Kirstätter"
    
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

    # Generate designated Open Graph image for the primary hero image
    img_field_match = re.search(r"^image:\s*['\"]?([^\s'\"]+)['\"]?", frontmatter, re.MULTILINE)
    if img_field_match:
        hero_val = img_field_match.group(1).strip('\"\'')
        if hero_val and hero_val.startswith("content/images/"):
            hero_full = POSTS_DIR / hero_val
            og_target_rel = str(Path(hero_val).parent / f"{Path(hero_val).stem}-og.webp")
            og_target_full = POSTS_DIR / og_target_rel
            
            if not dry_run and hero_full.exists():
                render_intelligent_og_image(
                    hero_img_path=str(hero_full),
                    title=post_title,
                    slug=post_slug,
                    app_url=app_url,
                    author=author_name,
                    output_path=str(og_target_full),
                    overwrite=False
                )
                
            # Populate or update ogImage in frontmatter if not already pointing to a custom override
            og_match = re.search(r"^ogImage:\s*['\"]?([^\s'\"]*)['\"]?", frontmatter, re.MULTILINE)
            if og_match:
                curr_og = og_match.group(1).strip('\"\'')
                if not curr_og:
                    frontmatter = re.sub(r"^ogImage:.*$", f"ogImage: {og_target_rel}", frontmatter, flags=re.MULTILINE)
                    modified = True
            else:
                frontmatter = re.sub(r"^(image:\s*.*)$", rf"\1\nogImage: {og_target_rel}", frontmatter, flags=re.MULTILINE)
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
