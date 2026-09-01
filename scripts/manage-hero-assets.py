#!/usr/bin/env python3
"""
scripts/manage-hero-assets.py
Dedicated CLI utility for AI image generation, hero image processing,
responsive WebP variant generation, and intelligent 1200x630 OpenGraph preview cards.

Capabilities:
  1. AI Hero Generation: Generate high-resolution 16:9 hero imagery directly via
     Gemini Imagen 3 REST API using `--ai-prompt "<prompt>" --slug <uid>`.
  2. Process Hero Asset: Auto-crop 16:9, convert to WebP, generate Ghost size variants (w300..w2000),
     generate OG card, and update markdown frontmatter.
  3. Batch OG Generation: Regenerate OpenGraph cards en bloc across drafts, published posts,
     or specific articles in seconds (purely local, zero network calls).
  4. Batch Variants: Generate missing responsive WebP variants across content/images/.
  5. Alternative Description/Title Switch: Override display title/description during generation.

Usage Examples:
  # Generate a brand new hero image with AI prompt, process variants, OG card, and update frontmatter:
  python3 scripts/manage-hero-assets.py --ai-prompt "Futuristic multi-agent control desk in comic style" --slug my-post

  # Process an existing master photo into master WebP + variants + OG card + frontmatter update:
  python3 scripts/manage-hero-assets.py --process-hero posts/draft/assets/my-slug/photo.jpg --slug my-slug --crop top

  # Regenerate OpenGraph cards en bloc for all drafts in seconds:
  python3 scripts/manage-hero-assets.py --og-cards --drafts-only [--force]

  # Regenerate OpenGraph cards for all published posts:
  python3 scripts/manage-hero-assets.py --og-cards --published-only

  # Regenerate OpenGraph card for a specific post with an alternative title/description:
  python3 scripts/manage-hero-assets.py --og-cards --slug gdg-cloud-munich --alt-title "Custom Title" --force

  # Ensure all responsive size variants exist across content/images/:
  python3 scripts/manage-hero-assets.py --generate-variants
"""

import os
import sys
import re
import json
import base64
import argparse
from pathlib import Path
from datetime import datetime
import requests
from PIL import Image, ImageOps, ImageDraw, ImageFont, ImageFilter

# Add scripts directory to sys.path to load pure Python qr_generator
SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
POSTS_DIR = REPO_ROOT / "posts"
CONTENT_IMAGES_DIR = POSTS_DIR / "content" / "images"
GHOST_SIZES = [300, 600, 1000, 1600, 2000]
USER_AGENT = "OpenAI File Downloader, XaiImageApiFetch/1.0"

sys.path.insert(0, str(SCRIPT_DIR))
try:
    from qr_generator import generate_qr_image
except ImportError:
    generate_qr_image = None


def load_api_key(cli_key: str = None) -> str:
    """Load Gemini API Key from CLI argument, environment, or .env file."""
    if cli_key:
        return cli_key
    
    for var in ["GEMINI_API_KEY", "GOOGLE_API_KEY", "IMAGEN_API_KEY"]:
        val = os.environ.get(var)
        if val:
            return val
            
    # Check .env file in REPO_ROOT or home dir
    env_paths = [REPO_ROOT / ".env", Path.home() / ".env"]
    for env_path in env_paths:
        if env_path.exists():
            for line in env_path.read_text(encoding="utf-8").splitlines():
                line = line.strip()
                if line.startswith("#") or not line:
                    continue
                match = re.match(r"^(GEMINI_API_KEY|GOOGLE_API_KEY|IMAGEN_API_KEY)\s*=\s*(.*)$", line)
                if match:
                    return match.group(2).strip("\"'")
    return None


def get_font(font_name: str, size: int):
    """Retrieve system TrueType or OpenType font with graceful fallback."""
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
        ]
    }
    for p in font_paths.get(font_name, font_paths['bold']):
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size=size)
            except Exception:
                pass
    return ImageFont.load_default()


def balance_wrap_text(text: str, font, max_width: int, draw: ImageDraw.Draw):
    """Balanced multi-line text wrapping preventing dangling single words."""
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


def crop_to_16_9(img: Image.Image, crop_mode: str = 'center', custom_offset: int = None) -> Image.Image:
    """Crop any image into a strict 16:9 master ratio with flexible framing."""
    w, h = img.size
    target_ratio = 16 / 9
    current_ratio = w / h

    if abs(current_ratio - target_ratio) < 0.01:
        return img

    if current_ratio > target_ratio:
        # Image is wider than 16:9 -> crop width
        new_w = int(h * target_ratio)
        offset_x = (w - new_w) // 2
        return img.crop((offset_x, 0, offset_x + new_w, h))
    else:
        # Image is taller than 16:9 -> crop height
        new_h = int(w / target_ratio)
        if custom_offset is not None:
            offset_y = max(0, min(custom_offset, h - new_h))
        elif crop_mode == 'top':
            offset_y = 0
        elif crop_mode == 'bottom':
            offset_y = h - new_h
        else: # center
            offset_y = (h - new_h) // 2
        return img.crop((0, offset_y, w, offset_y + new_h))


def render_intelligent_og_image(
    hero_img_path: Path,
    title: str,
    slug: str,
    app_url: str = 'https://jochen.kirstaetter.name',
    author: str = 'Jochen Kirstätter',
    output_path: Path = None,
    overwrite: bool = False
) -> Image.Image:
    """Render a 1200x630 frosted-glass OpenGraph preview card with QR code."""
    if output_path and output_path.exists() and not overwrite:
        return None

    width, height = 1200, 630

    # 1. Base hero image backdrop with blur
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

    # 2. Dynamic Balanced Title Sizing
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
    line_widths = [
        temp_draw.textbbox((0, 0), line, font=font_title)[2] - temp_draw.textbbox((0, 0), line, font=font_title)[0]
        for line in title_lines
    ]
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

    # 4. Bottom-Left Author & URL Attribution Plate
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

    # Soft Drop Shadow
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

    # 7. Frosted-Glass Extension-less QR Code
    if generate_qr_image:
        clean_app_url = app_url.rstrip('/')
        post_url = f'{clean_app_url}/{slug}'  # Extension-less canonical URL
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
        output_path.parent.mkdir(parents=True, exist_ok=True)
        final_output.save(output_path, 'WEBP', quality=90, method=4)

    return final_output


def generate_size_variants(master_path: Path, force: bool = False) -> list:
    """Generate all 5 Ghost responsive size buckets (w300..w2000) for a master WebP."""
    if not master_path.exists():
        return []

    try:
        img = Image.open(master_path)
    except Exception as e:
        print(f"  ❌ Error opening {master_path}: {e}")
        return []

    rel_path = master_path.relative_to(CONTENT_IMAGES_DIR)
    generated = []

    orig_w, orig_h = img.size
    for size_w in GHOST_SIZES:
        target_size_path = CONTENT_IMAGES_DIR / "size" / f"w{size_w}" / rel_path
        target_size_path.parent.mkdir(parents=True, exist_ok=True)

        if target_size_path.exists() and not force:
            continue

        if orig_w > size_w:
            new_h = int(orig_h * (size_w / orig_w))
            resized = img.resize((size_w, new_h), Image.Resampling.LANCZOS)
        else:
            resized = img.copy()

        if resized.mode in ("RGBA", "LA") or (resized.mode == "P" and "transparency" in resized.info):
            resized.save(target_size_path, "WEBP", quality=82, method=4)
        else:
            rgb_resized = resized.convert("RGB")
            rgb_resized.save(target_size_path, "WEBP", quality=82, method=4)

        generated.append(target_size_path)

    return generated


MODEL_ALIASES = {
    "nano-banana-2": "gemini-3.1-flash-image",
    "nano-banana": "gemini-2.5-flash-image",
    "imagen-3": "imagen-3.0-generate-002",
    "imagen-4": "imagen-4.0-generate-001"
}


def generate_ai_image(prompt: str, api_key: str, aspect_ratio: str = "16:9", model: str = "gemini-3.1-flash-image") -> bytes:
    """Generate image bytes using Gemini 3.1 Flash Image (Nano Banana 2) or Imagen models."""
    model_name = MODEL_ALIASES.get(model.lower(), model)
    headers = {
        "User-Agent": USER_AGENT,
        "Content-Type": "application/json"
    }

    if "gemini" in model_name:
        # Gemini Flash Image (Nano Banana 2) generateContent endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:generateContent?key={api_key}"
        payload = {
            "contents": [{"parts": [{"text": prompt}]}],
            "generationConfig": {
                "responseModalities": ["IMAGE"],
                "imageConfig": {"aspectRatio": aspect_ratio}
            }
        }
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        if response.status_code != 200:
            raise RuntimeError(f"Gemini Image API error ({model_name}, status {response.status_code}): {response.text}")
        data = response.json()
        try:
            candidates = data.get("candidates", [])
            parts = candidates[0]["content"]["parts"]
            for part in parts:
                if "inlineData" in part:
                    return base64.b64decode(part["inlineData"]["data"])
            raise KeyError("No inlineData in parts")
        except Exception as e:
            raise RuntimeError(f"Could not parse image bytes from Gemini response: {data}") from e
    else:
        # Imagen predict endpoint
        url = f"https://generativelanguage.googleapis.com/v1beta/models/{model_name}:predict?key={api_key}"
        payload = {
            "instances": [{"prompt": prompt}],
            "parameters": {
                "sampleCount": 1,
                "aspectRatio": aspect_ratio,
                "outputOptions": {"mimeType": "image/jpeg"}
            }
        }
        response = requests.post(url, headers=headers, json=payload, timeout=90)
        if response.status_code != 200:
            raise RuntimeError(f"Imagen API error ({model_name}, status {response.status_code}): {response.text}")
        data = response.json()
        predictions = data.get("predictions", [])
        if not predictions or not predictions[0].get("bytesBase64Encoded"):
            raise RuntimeError(f"No image predictions returned by Imagen API: {data}")
        return base64.b64decode(predictions[0]["bytesBase64Encoded"])


def parse_post_frontmatter(md_path: Path) -> dict:
    """Parse YAML frontmatter from a markdown post."""
    content = md_path.read_text(encoding="utf-8")
    fm = {}
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return fm

    for line in match.group(1).splitlines():
        kv = re.match(r"^([a-zA-Z0-9_-]+)\s*:\s*(.*)$", line)
        if kv:
            k = kv.group(1).strip()
            v = kv.group(2).strip().strip('"\'')
            fm[k] = v
    return fm


def update_post_frontmatter(md_path: Path, image_rel: str, og_image_rel: str, alt_desc: str = None) -> bool:
    """Update or insert image and ogImage frontmatter attributes."""
    content = md_path.read_text(encoding="utf-8")
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return False

    raw_yaml = match.group(1)
    body = match.group(2)

    lines = raw_yaml.splitlines()
    new_lines = []
    has_image = False
    has_og_image = False

    for line in lines:
        if re.match(r"^image\s*:", line):
            new_lines.append(f"image: {image_rel}")
            has_image = True
        elif re.match(r"^ogImage\s*:", line):
            new_lines.append(f"ogImage: {og_image_rel}")
            has_og_image = True
        elif alt_desc and re.match(r"^(description|metaDescription)\s*:", line):
            prefix = line.split(":", 1)[0]
            new_lines.append(f'{prefix}: "{alt_desc}"')
        else:
            new_lines.append(line)

    if not has_image:
        new_lines.append(f"image: {image_rel}")
    if not has_og_image:
        new_lines.append(f"ogImage: {og_image_rel}")

    updated = "---\n" + "\n".join(new_lines) + "\n---\n" + body
    md_path.write_text(updated, encoding="utf-8")
    return True


def find_post_md(slug: str) -> Path:
    """Find markdown file for a given slug in draft, published, or pages."""
    for folder in ["draft", "published", "pages"]:
        target = POSTS_DIR / folder / f"{slug}.md"
        if target.exists():
            return target
    return None


def cmd_ai_generate_hero(args):
    """Generate hero image with Gemini 3.1 Flash Image (Nano Banana 2) or Imagen, archive raw asset, and process pipeline."""
    api_key = load_api_key(args.api_key)
    if not api_key:
        print("\n❌ Gemini / Google API Key not found.")
        print("Please set GEMINI_API_KEY or GOOGLE_API_KEY environment variable, or pass --api-key <key>.")
        print("Example: export GEMINI_API_KEY=\"AIzaSy...\"\n")
        sys.exit(1)

    slug = args.slug
    if not slug:
        print("❌ Please specify target post slug via --slug <uid>")
        sys.exit(1)

    prompt = args.ai_prompt
    print(f"\n✨ Generating Hero Image with AI: [{slug}]")
    print(f"  Prompt: \"{prompt}\"")
    print(f"  Aspect Ratio: {args.aspect_ratio}")
    print(f"  Model: {args.ai_model}")

    try:
        raw_bytes = generate_ai_image(
            prompt=prompt,
            api_key=api_key,
            aspect_ratio=args.aspect_ratio,
            model=args.ai_model
        )
    except Exception as e:
        print(f"\n❌ AI Generation Failed: {e}\n")
        sys.exit(1)

    # Archive raw asset into draft assets directory
    draft_asset_dir = POSTS_DIR / "draft" / "assets" / slug
    draft_asset_dir.mkdir(parents=True, exist_ok=True)
    raw_archive_path = draft_asset_dir / f"{slug}-ai-raw.jpg"
    raw_archive_path.write_bytes(raw_bytes)
    print(f"  ✔ Raw master archived to: {raw_archive_path.relative_to(REPO_ROOT)} ({len(raw_bytes) // 1024} KB)")

    # Forward directly into process_hero logic
    args.process_hero = str(raw_archive_path)
    cmd_process_hero(args)


def cmd_process_hero(args):
    """Process a raw source photo into 16:9 master WebP, responsive sizes, and OG card."""
    source_path = Path(args.process_hero)
    if not source_path.exists():
        print(f"❌ Source image not found: {source_path}")
        sys.exit(1)

    slug = args.slug
    if not slug:
        if "posts/draft/assets/" in str(source_path):
            slug = source_path.parent.name
        else:
            slug = source_path.stem

    # Locate markdown file for date/year extraction
    md_path = find_post_md(slug)
    fm = parse_post_frontmatter(md_path) if md_path else {}

    # Determine Year/Month directory
    date_val = fm.get("date") or fm.get("publishedAt") or datetime.now().strftime("%Y-%m-%d")
    year_str = args.year or date_val.split("-")[0]
    month_str = args.month or (date_val.split("-")[1] if len(date_val.split("-")) > 1 else "01")

    # Output master paths
    master_rel = f"content/images/{year_str}/{month_str}/{slug}.webp"
    master_og_rel = f"content/images/{year_str}/{month_str}/{slug}-og.webp"
    master_path = POSTS_DIR / master_rel
    og_path = POSTS_DIR / master_og_rel
    master_path.parent.mkdir(parents=True, exist_ok=True)

    print(f"\n🖼️  Processing Hero Asset: [{slug}]")
    print(f"  Source: {source_path}")
    print(f"  Target: {master_path}")

    # 1. Open and crop to 16:9
    src_img = Image.open(source_path)
    cropped_16_9 = crop_to_16_9(src_img, crop_mode=args.crop, custom_offset=args.crop_offset)
    
    # Save master WebP
    rgb_cropped = cropped_16_9.convert("RGB") if cropped_16_9.mode not in ("RGBA", "LA") else cropped_16_9
    rgb_cropped.save(master_path, "WEBP", quality=args.quality, method=4)
    print(f"  ✔ Master 16:9 WebP saved: {master_path.stat().st_size // 1024} KB ({cropped_16_9.width}x{cropped_16_9.height})")

    # 2. Generate 5 responsive size variants
    variants = generate_size_variants(master_path, force=args.force)
    print(f"  ✔ Generated {len(variants)} responsive size variants (w300..w2000)")

    # 3. Generate OpenGraph preview card
    title = args.alt_title or fm.get("title") or slug.replace("-", " ").title()
    render_intelligent_og_image(
        hero_img_path=master_path,
        title=title,
        slug=slug,
        output_path=og_path,
        overwrite=True
    )
    print(f"  ✔ OpenGraph preview card generated: {og_path}")

    # 4. Update frontmatter if markdown file exists
    if md_path and (args.update_frontmatter or not args.no_update_frontmatter):
        update_post_frontmatter(md_path, master_rel, master_og_rel, alt_desc=args.alt_desc)
        print(f"  ✔ Frontmatter updated in: {md_path.relative_to(REPO_ROOT)}")

    print(f"✨ Hero asset processing complete for {slug}!\n")


def cmd_og_cards(args):
    """Regenerate OpenGraph cards en bloc across drafts, published posts, or specific slugs."""
    print("\n🎨 OpenGraph Cards Generation (Offline Fast Pipeline)")

    md_files = []
    if args.slug:
        target = find_post_md(args.slug)
        if target:
            md_files.append(target)
        else:
            print(f"❌ Post with slug '{args.slug}' not found.")
            sys.exit(1)
    else:
        if args.drafts_only or not args.published_only:
            md_files.extend(list((POSTS_DIR / "draft").glob("*.md")))
        if args.published_only or args.all:
            md_files.extend(list((POSTS_DIR / "published").glob("*.md")))
            md_files.extend(list((POSTS_DIR / "pages").glob("*.md")))

    count_generated = 0
    count_skipped = 0

    for md_path in md_files:
        if md_path.name in ("index.md", "toc.yml"):
            continue

        fm = parse_post_frontmatter(md_path)
        slug = fm.get("uid") or fm.get("slug") or md_path.stem
        title = args.alt_title or fm.get("title") or slug.replace("-", " ").title()

        # Locate assigned hero image or fallback
        hero_img_rel = fm.get("image") or fm.get("featureImage") or fm.get("imageUrl")
        hero_img_path = POSTS_DIR / hero_img_rel if hero_img_rel else None

        # Determine target OG path
        if hero_img_rel and not hero_img_rel.endswith("-og.webp"):
            og_rel = re.sub(r"\.(webp|jpg|jpeg|png)$", "-og.webp", hero_img_rel)
            og_path = POSTS_DIR / og_rel
        else:
            date_val = fm.get("date") or fm.get("publishedAt") or datetime.now().strftime("%Y-%m-%d")
            year = date_val.split("-")[0]
            month = date_val.split("-")[1] if len(date_val.split("-")) > 1 else "01"
            og_path = CONTENT_IMAGES_DIR / year / month / f"{slug}-og.webp"

        if og_path.exists() and not args.force:
            count_skipped += 1
            continue

        render_intelligent_og_image(
            hero_img_path=hero_img_path,
            title=title,
            slug=slug,
            output_path=og_path,
            overwrite=args.force
        )
        count_generated += 1
        print(f"  ✔ Rendered OG: [{slug}] -> {og_path.relative_to(POSTS_DIR)}")

    print(f"\n📊 Summary: {count_generated} cards generated, {count_skipped} skipped (use --force to overwrite).\n")


def cmd_generate_variants(args):
    """Scan content/images/ and generate missing responsive variants."""
    print("\n📐 Scanning for missing responsive size variants (w300..w2000)...")
    masters = [p for p in CONTENT_IMAGES_DIR.glob("**/*.webp") if "/size/" not in str(p) and not p.name.endswith("-og.webp")]

    total_created = 0
    for master in masters:
        variants = generate_size_variants(master, force=args.force)
        if variants:
            total_created += len(variants)
            print(f"  ✔ {len(variants)} variants -> {master.name}")

    print(f"\n✨ Generated {total_created} responsive variants.\n")


def main():
    parser = argparse.ArgumentParser(
        description="Dedicated CLI tool for AI image generation, hero image processing, and OpenGraph card generation.",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog=__doc__
    )

    # Mode Switches
    parser.add_argument("--ai-prompt", type=str, metavar="PROMPT", help="Generate hero image directly via Google Imagen 3.")
    parser.add_argument("--process-hero", type=str, metavar="SOURCE_IMG", help="Process an existing raw photo or master image.")
    parser.add_argument("--og-cards", action="store_true", help="Generate / regenerate OpenGraph cards en bloc.")
    parser.add_argument("--generate-variants", action="store_true", help="Generate missing Ghost size variants across images.")

    # Target & Scope Filters
    parser.add_argument("--slug", type=str, help="Target post slug / UID.")
    parser.add_argument("--drafts-only", action="store_true", help="Scope OG generation to draft posts.")
    parser.add_argument("--published-only", action="store_true", help="Scope OG generation to published posts.")
    parser.add_argument("--all", action="store_true", help="Scope OG generation across all posts & pages.")

    # AI Generation & Model Options
    parser.add_argument("--api-key", type=str, help="Gemini / Google API Key (or set GEMINI_API_KEY env).")
    parser.add_argument("--ai-model", type=str, default="gemini-3.1-flash-image", help="Image model name or alias: gemini-3.1-flash-image / nano-banana-2, nano-banana, imagen-3 (default: gemini-3.1-flash-image).")
    parser.add_argument("--aspect-ratio", choices=["16:9", "1:1", "4:3", "3:4", "9:16"], default="16:9", help="Aspect ratio for AI generation (default: 16:9).")

    # Cropping & Conversion Options
    parser.add_argument("--crop", choices=["top", "center", "bottom"], default="center", help="16:9 crop anchor position (default: center).")
    parser.add_argument("--crop-offset", type=int, help="Custom pixel offset for 16:9 crop.")
    parser.add_argument("--quality", type=int, default=85, help="WebP compression quality (default: 85).")
    parser.add_argument("--year", type=str, help="Override year folder (e.g. 2026).")
    parser.add_argument("--month", type=str, help="Override month folder (e.g. 08).")

    # Frontmatter & Text Overrides
    parser.add_argument("--alt-title", type=str, help="Alternative title for OpenGraph preview card.")
    parser.add_argument("--alt-desc", type=str, help="Alternative description to update into frontmatter.")
    parser.add_argument("--force", action="store_true", help="Force overwrite existing output files.")
    parser.add_argument("--no-update-frontmatter", action="store_true", help="Do not update markdown frontmatter.")
    parser.add_argument("--update-frontmatter", action="store_true", help="Explicitly update markdown frontmatter.")

    args = parser.parse_args()

    if args.ai_prompt:
        cmd_ai_generate_hero(args)
    elif args.process_hero:
        cmd_process_hero(args)
    elif args.og_cards:
        cmd_og_cards(args)
    elif args.generate_variants:
        cmd_generate_variants(args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
