#!/usr/bin/env python3
"""
scripts/generate-audio.py
Automates audio script extraction, TTS voice generation (Piper local or ElevenLabs API),
and frontmatter synchronization for blog articles on getblogged.

Supports automatic language detection (English vs German) and selects the appropriate voice:
  - English (en_GB): 'en_GB-aru-medium' (default) or 'en_GB-alan-medium'
  - German  (de_DE): 'de_DE-thorsten-medium'

Usage Examples:
  # 1. Generate audio locally for a single post using Piper (auto-detects language, defaults to Aru):
  python3 scripts/generate-audio.py --uid assembling-an-ai-publishing-agency --provider piper

  # 2. Test English voice "alan":
  python3 scripts/generate-audio.py --uid assembling-an-ai-publishing-agency --provider piper --voice alan

  # 3. Test a pre-2007 German article (auto-detects German -> Thorsten voice):
  python3 scripts/generate-audio.py --uid javascript-macht-spass --provider piper

  # 4. Extract clean narration script only:
  python3 scripts/generate-audio.py --uid assembling-an-ai-publishing-agency --extract-only

  # 5. Batch generate audio for all published articles:
  python3 scripts/generate-audio.py --all-published --provider piper
"""

import os
import sys
import re
import json
import argparse
import subprocess
import urllib.request
import urllib.error
from pathlib import Path
from datetime import datetime

SCRIPT_DIR = Path(__file__).resolve().parent
REPO_ROOT = SCRIPT_DIR.parent
POSTS_DIR = REPO_ROOT / "posts"
DRAFT_DIR = POSTS_DIR / "draft"
PUBLISHED_DIR = POSTS_DIR / "published"
CONTENT_AUDIO_DIR = POSTS_DIR / "content" / "audio"

PIPER_CACHE_DIR = Path.home() / ".cache" / "piper" / "models"
USER_AGENT = "OpenAI File Downloader, XaiImageApiFetch/1.0"

# Common German stopwords for lightweight, 100% offline language detection
GERMAN_STOPWORDS = {
    "der", "die", "das", "und", "ist", "in", "den", "von", "zu", "mit", "sich",
    "des", "auf", "für", "eine", "ein", "nicht", "dem", "auch", "es", "an",
    "werden", "aus", "er", "hat", "dass", "sie", "nach", "wird", "bei", "einer",
    "um", "am", "sind", "noch", "wie", "einem", "über", "einen", "so", "haben",
    "oder", "aber", "vor", "zur", "bis", "wurde", "wenn", "kann", "sehr"
}

# Pronunciation normalization maps
PRONUNCIATION_MAP_EN = [
    (r"\bDocFX\b", "Doc F X"),
    (r"\bDocFx\b", "Doc F X"),
    (r"\bGhostFx\b", "Ghost F X"),
    (r"\bghostfx\b", "ghost F X"),
    (r"\b\.NET\b", "Dot Net"),
    (r"\bCLI\b", "C L I"),
    (r"\bCLIs\b", "C L I's"),
    (r"\bAPI\b", "A P I"),
    (r"\bAPIs\b", "A P I's"),
    (r"\bYAML\b", "Yammel"),
    (r"\bJSON\b", "Jason"),
    (r"\bHTML\b", "H T M L"),
    (r"\bCSS\b", "C S S"),
    (r"\bSVG\b", "S V G"),
    (r"\bSDK\b", "S D K"),
    (r"\bSDKs\b", "S D K's"),
    (r"\bVFP\b", "Visual FoxPro"),
    (r"\bNginx\b", "Engine X"),
    (r"\bSQLite\b", "Sequel Lite"),
    (r"\bSQL\b", "Sequel"),
    (r"\bREST\b", "Rest"),
    (r"\bMSCC\b", "M S C C"),
    (r"\bGDG\b", "G D G"),
    (r"\bCI/CD\b", "C I C D"),
    (r"\bPR\b", "Pull Request"),
    (r"\bPRs\b", "Pull Requests"),
    (r"\bSEO\b", "S E O"),
    (r"\bDevOps\b", "Dev Ops"),
    (r"\bOG\b", "Open Graph"),
    (r"\bi\.e\.", "that is"),
    (r"\be\.g\.", "for example"),
    (r"\betc\.", "etcetera"),
]

PRONUNCIATION_MAP_DE = [
    (r"\bz\.B\.", "zum Beispiel"),
    (r"\bd\.h\.", "das heißt"),
    (r"\bbzw\.", "beziehungsweise"),
    (r"\busw\.", "und so weiter"),
    (r"\bca\.", "zirka"),
    (r"\bggf\.", "gegebenenfalls"),
    (r"\bevtl\.", "eventuell"),
    (r"\binkl\.", "inklusive"),
    (r"\b\.NET\b", "Dot Net"),
    (r"\bVFP\b", "Visual FoxPro"),
    (r"\bSQL\b", "Sequel"),
    (r"\bHTML\b", "H T M L"),
    (r"\bCSS\b", "C S S"),
    (r"\bAPI\b", "A P I"),
    (r"\bMS\b", "Microsoft"),
]

PIPER_MODEL_URLS = {
    "en_GB-alan-medium": (
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx",
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx.json"
    ),
    "en_GB-aru-medium": (
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/aru/medium/en_GB-aru-medium.onnx",
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/aru/medium/en_GB-aru-medium.onnx.json"
    ),
    "de_DE-thorsten-medium": (
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx",
        "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx.json"
    )
}


def detect_language(body: str, fm: dict) -> str:
    """Detect if content is in German ('de') or English ('en')."""
    # 1. Check explicit frontmatter
    if fm.get("lang") == "de" or fm.get("language") == "de":
        return "de"
    if fm.get("lang") == "en" or fm.get("language") == "en":
        return "en"

    # 2. Heuristic word analysis
    words = set(re.findall(r"\b[a-zäöüß]+\b", body.lower()[:3000]))
    german_matches = len(words.intersection(GERMAN_STOPWORDS))
    if german_matches >= 6:
        return "de"

    return "en"


def find_post(uid: str) -> tuple[Path, bool]:
    """Find post markdown file by UID in draft or published directories."""
    p = PUBLISHED_DIR / f"{uid}.md"
    if p.is_file():
        return p, False
    d = DRAFT_DIR / f"{uid}.md"
    if d.is_file():
        return d, True
    for f in PUBLISHED_DIR.rglob(f"*{uid}*.md"):
        if f.is_file():
            return f, False
    for f in DRAFT_DIR.rglob(f"*{uid}*.md"):
        if f.is_file():
            return f, True
    raise FileNotFoundError(f"Could not find markdown post with UID '{uid}' in draft or published directories.")


def parse_frontmatter(content: str) -> tuple[dict, str, str]:
    """Extract YAML frontmatter dictionary, raw frontmatter text, and body."""
    match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
    if not match:
        return {}, "", content
    raw_yaml = match.group(1)
    body = match.group(2)
    fm = {}
    for line in raw_yaml.splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key, val = m.group(1), m.group(2).strip()
            if val.startswith(('"', "'")) and val.endswith(('"', "'")) and len(val) >= 2:
                val = val[1:-1]
            fm[key] = val
    return fm, raw_yaml, body


def sanitize_markdown_for_speech(body: str, title: str = "", lang: str = "en") -> str:
    """Transform markdown content into smooth, spoken narrative text."""
    text = body

    # 1. Strip HTML tags (including comments)
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)

    # 2. Handle fenced code blocks
    def replace_code_fence(m):
        lang_tag = m.group(1).strip() if m.group(1) else ""
        if lang == "de":
            if lang_tag:
                return f"\n\n[Im Artikel folgt ein {lang_tag}-Codeausschnitt.]\n\n"
            return "\n\n[Codeausschnitt für Audio-Wiedergabe übersprungen.]\n\n"
        else:
            if lang_tag:
                return f"\n\n[The article contains a {lang_tag} code snippet.]\n\n"
            return "\n\n[Code block omitted for audio narration.]\n\n"

    text = re.sub(r"```([a-zA-Z0-9_-]*)\n.*?\n```", replace_code_fence, text, flags=re.DOTALL)

    # 3. Strip custom container markers (::: grid, ::: strip, ::: gallery, :::)
    text = re.sub(r":::\s*[a-zA-Z0-9_-]*", "", text)

    # 4. Strip alert headers (> [!NOTE], > [!TIP], etc.) while keeping block content
    text = re.sub(r">\s*\[![A-Z]+\]", "", text)
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)

    # 5. Remove images ![alt](url)
    text = re.sub(r"!\[(.*?)\]\(.*?\)", r"\1", text)

    # 6. Simplify markdown links [text](url) -> text
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)

    # 7. Headings #, ##, etc.
    text = re.sub(r"^#{1,6}\s+(.+)$", r"\1.\n", text, flags=re.MULTILINE)

    # 8. Strip inline backticks `code` -> code
    text = re.sub(r"`([^`]+)`", r"\1", text)

    # 9. Strip bold and italic
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"__([^_]+)__", r"\1", text)
    text = re.sub(r"_([^_]+)_", r"\1", text)

    # 10. Strip horizontal rules
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)

    # 11. Normalize bullet points
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)

    # 12. Apply pronunciation normalization
    pmap = PRONUNCIATION_MAP_DE if lang == "de" else PRONUNCIATION_MAP_EN
    for pattern, replacement in pmap:
        text = re.sub(pattern, replacement, text)

    # 13. Clean up whitespace
    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    speech_text = "\n\n".join(paragraphs)

    if title:
        intro = f"{title}.\n\n"
        if not speech_text.startswith(title):
            speech_text = intro + speech_text

    return speech_text


def get_audio_duration(audio_path: Path) -> str:
    """Calculate duration of audio file formatted as MM:SS."""
    try:
        cmd = [
            "ffprobe", "-v", "error", "-show_entries", "format=duration",
            "-of", "default=noprint_wrappers=1:nokey=1", str(audio_path)
        ]
        res = subprocess.run(cmd, capture_output=True, text=True, check=True)
        sec = float(res.stdout.strip())
        m = int(sec // 60)
        s = int(sec % 60)
        return f"{m}:{s:02d}"
    except Exception:
        pass

    try:
        import mutagen.mp3
        audio = mutagen.mp3.MP3(str(audio_path))
        sec = int(audio.info.length)
        m = sec // 60
        s = sec % 60
        return f"{m}:{s:02d}"
    except Exception:
        pass

    return "05:00"


def ensure_piper_model(model_name: str) -> Path:
    """Ensure piper model and its json config are downloaded in PIPER_CACHE_DIR."""
    PIPER_CACHE_DIR.mkdir(parents=True, exist_ok=True)
    onnx_file = PIPER_CACHE_DIR / f"{model_name}.onnx"
    json_file = PIPER_CACHE_DIR / f"{model_name}.onnx.json"

    if onnx_file.is_file() and json_file.is_file():
        return onnx_file

    if model_name not in PIPER_MODEL_URLS:
        raise ValueError(f"Unknown Piper model '{model_name}'. Available: {list(PIPER_MODEL_URLS.keys())}")

    onnx_url, json_url = PIPER_MODEL_URLS[model_name]
    print(f"📥 Downloading Piper voice model '{model_name}'...")

    def download_url(url: str, dest: Path):
        req = urllib.request.Request(url, headers={"User-Agent": USER_AGENT})
        with urllib.request.urlopen(req) as resp, open(dest, "wb") as f:
            f.write(resp.read())

    download_url(onnx_url, onnx_file)
    download_url(json_url, json_file)
    print(f"✔ Downloaded {model_name} ({round(onnx_file.stat().st_size / (1024*1024), 1)} MB)")
    return onnx_file


def run_piper_tts(text: str, model_path: Path, output_mp3: Path):
    """Synthesize text to MP3 using local piper binary and ffmpeg."""
    piper_bin = subprocess.run(["which", "piper"], capture_output=True, text=True).stdout.strip()
    if not piper_bin:
        # Check ~/.local/piper/piper
        local_bin = Path.home() / ".local" / "piper" / "piper"
        if local_bin.is_file():
            piper_bin = str(local_bin)
        else:
            raise RuntimeError("Piper binary not found. Please ensure piper is installed.")

    temp_wav = output_mp3.with_suffix(".temp.wav")
    output_mp3.parent.mkdir(parents=True, exist_ok=True)

    # 1. Synthesize with Piper
    proc = subprocess.Popen(
        [piper_bin, "--model", str(model_path), "--output_file", str(temp_wav)],
        stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
    )
    stdout, stderr = proc.communicate(input=text)
    if proc.returncode != 0:
        raise RuntimeError(f"Piper error: {stderr}")

    # 2. Compress to 64kbps MP3 via ffmpeg
    cmd_ffmpeg = [
        "ffmpeg", "-y", "-i", str(temp_wav),
        "-c:a", "libmp3lame", "-b:a", "64k",
        str(output_mp3)
    ]
    subprocess.run(cmd_ffmpeg, capture_output=True, check=True)
    temp_wav.unlink(missing_ok=True)


def call_elevenlabs_tts(text: str, voice_id: str, api_key: str, output_path: Path):
    """Generate speech audio via ElevenLabs REST API."""
    url = f"https://api.elevenlabs.io/v1/text-to-speech/{voice_id}"
    headers = {
        "xi-api-key": api_key,
        "Content-Type": "application/json",
        "Accept": "audio/mpeg",
        "User-Agent": USER_AGENT
    }

    max_chunk = 4500
    paragraphs = text.split("\n\n")
    chunks = []
    current_chunk = []
    current_len = 0

    for p in paragraphs:
        if current_len + len(p) + 2 > max_chunk and current_chunk:
            chunks.append("\n\n".join(current_chunk))
            current_chunk = [p]
            current_len = len(p)
        else:
            current_chunk.append(p)
            current_len += len(p) + 2
    if current_chunk:
        chunks.append("\n\n".join(current_chunk))

    temp_parts = []
    output_path.parent.mkdir(parents=True, exist_ok=True)

    try:
        for idx, chunk in enumerate(chunks):
            payload = {
                "text": chunk,
                "model_id": "eleven_multilingual_v2",
                "voice_settings": {
                    "stability": 0.5,
                    "similarity_boost": 0.75,
                    "style": 0.0,
                    "use_speaker_boost": True
                }
            }
            req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers, method="POST")
            part_path = output_path.with_name(f"{output_path.stem}_part{idx}.mp3")
            print(f"  🔊 Generating audio chunk {idx+1}/{len(chunks)} ({len(chunk)} characters)...")
            with urllib.request.urlopen(req) as resp:
                with open(part_path, "wb") as f:
                    f.write(resp.read())
            temp_parts.append(part_path)

        if len(temp_parts) == 1:
            if output_path.exists():
                output_path.unlink()
            temp_parts[0].rename(output_path)
        else:
            concat_list = output_path.with_name("concat_list.txt")
            with open(concat_list, "w", encoding="utf-8") as f:
                for p in temp_parts:
                    f.write(f"file '{p.resolve()}'\n")
            cmd = ["ffmpeg", "-y", "-f", "concat", "-safe", "0", "-i", str(concat_list), "-c", "copy", str(output_path)]
            subprocess.run(cmd, capture_output=True, check=True)
            concat_list.unlink(missing_ok=True)
            for p in temp_parts:
                p.unlink(missing_ok=True)

    except urllib.error.HTTPError as e:
        error_body = e.read().decode("utf-8", errors="replace")
        print(f"\n❌ ElevenLabs API Error ({e.code}):\n{error_body}", file=sys.stderr)
        raise


def sync_frontmatter(post_file: Path, audio_rel: str, duration: str, narrator: str):
    """Add or update audio, audioDuration, and audioNarrator in the markdown frontmatter."""
    content = post_file.read_text(encoding="utf-8")
    fm, raw_yaml, body = parse_frontmatter(content)

    new_lines = []
    keys_handled = set()

    for line in raw_yaml.splitlines():
        m = re.match(r"^([A-Za-z0-9_-]+):\s*(.*)$", line)
        if m:
            key = m.group(1)
            if key == "audio":
                new_lines.append(f"audio: {audio_rel}")
                keys_handled.add("audio")
                continue
            elif key == "audioDuration":
                new_lines.append(f'audioDuration: "{duration}"')
                keys_handled.add("audioDuration")
                continue
            elif key == "audioNarrator":
                new_lines.append(f'audioNarrator: "{narrator}"')
                keys_handled.add("audioNarrator")
                continue
        new_lines.append(line)

    if "audio" not in keys_handled:
        new_lines.append(f"audio: {audio_rel}")
    if "audioDuration" not in keys_handled:
        new_lines.append(f'audioDuration: "{duration}"')
    if "audioNarrator" not in keys_handled:
        new_lines.append(f'audioNarrator: "{narrator}"')

    new_content = f"---\n{chr(10).join(new_lines)}\n---\n{body}"
    post_file.write_text(new_content, encoding="utf-8")
    print(f"✔ Frontmatter synchronized in {post_file.name}:")
    print(f"    audio: {audio_rel}")
    print(f"    audioDuration: {duration}")
    print(f"    audioNarrator: {narrator}")


def process_single_post(uid: str, args):
    """Process narration extraction and audio generation for a single post."""
    post_file, is_draft = find_post(uid)
    content = post_file.read_text(encoding="utf-8")
    fm, raw_yaml, body = parse_frontmatter(content)
    title = fm.get("title", "")
    date_str = fm.get("date", fm.get("publishedAt", datetime.now().strftime("%Y-%m-%d")))[:10]
    dt = datetime.strptime(date_str, "%Y-%m-%d") if len(date_str) == 10 else datetime.now()

    lang = detect_language(body, fm)
    year = dt.strftime("%Y")
    month = dt.strftime("%m")
    target_dir = CONTENT_AUDIO_DIR / year / month
    target_dir.mkdir(parents=True, exist_ok=True)

    filename = args.output_name or f"{uid}.mp3"
    target_mp3 = target_dir / filename
    rel_audio_path = f"content/audio/{year}/{month}/{filename}"

    draft_assets_dir = DRAFT_DIR / "assets" / uid
    draft_assets_dir.mkdir(parents=True, exist_ok=True)
    script_file = draft_assets_dir / "narration.txt"

    print(f"\n📖 Processing post: '{title}' ({uid})")
    print(f"    Language detected: {'German (de)' if lang == 'de' else 'English (en)'}")

    # Extract clean text
    narration_text = sanitize_markdown_for_speech(body, title, lang=lang)
    script_file.write_text(narration_text, encoding="utf-8")
    char_count = len(narration_text)
    word_count = len(narration_text.split())
    est_duration_min = round(word_count / (130 if lang == 'de' else 150), 1)

    print(f"✔ Clean narration script saved to: {script_file.name}")
    print(f"    Stats: {word_count} words | {char_count} chars | ~{est_duration_min} min listening time")

    if args.extract_only:
        return

    # Audio synthesis
    narrator_label = args.narrator
    if args.import_audio:
        import_path = Path(args.import_audio).resolve()
        import shutil
        shutil.copy2(import_path, target_mp3)
        print(f"✔ Imported audio from {import_path.name}")
    elif args.provider == "piper":
        # Voice selection logic
        if lang == "de":
            model_name = "de_DE-thorsten-medium"
            if not narrator_label:
                narrator_label = "Gelesen von Piper (Thorsten)"
        else:
            # English: check if user chose 'alan' or default 'aru'
            if args.voice and "alan" in args.voice.lower():
                model_name = "en_GB-alan-medium"
                if not narrator_label:
                    narrator_label = "Narrated by Piper (Alan)"
            else:
                model_name = "en_GB-aru-medium"
                if not narrator_label:
                    narrator_label = "Narrated by Piper (Aru)"

        print(f"🎙️ Synthesizing locally with Piper ({model_name})...")
        model_path = ensure_piper_model(model_name)
        start_t = datetime.now()
        run_piper_tts(narration_text, model_path, target_mp3)
        elapsed = (datetime.now() - start_t).total_seconds()
        print(f"✔ Audio synthesized in {elapsed:.1f}s -> {rel_audio_path}")

    elif args.provider == "elevenlabs":
        api_key = os.getenv("ELEVENLABS_API_KEY", "")
        voice_id = args.voice_id
        if not api_key or not voice_id:
            print("❌ ELEVENLABS_API_KEY and ELEVENLABS_VOICE_ID required.", file=sys.stderr)
            sys.exit(1)
        if not narrator_label:
            narrator_label = "Jochen Kirstätter (AI Voice Clone)"
        print(f"🎙️ Generating voice clone via ElevenLabs...")
        call_elevenlabs_tts(narration_text, voice_id, api_key, target_mp3)

    if not narrator_label:
        narrator_label = "Jochen Kirstätter (Audio)"

    duration = get_audio_duration(target_mp3)
    sync_frontmatter(post_file, rel_audio_path, duration, narrator_label)


def main():
    parser = argparse.ArgumentParser(description="Generate and manage blog audio narration with Piper or ElevenLabs.")
    parser.add_argument("--uid", help="Post UID (e.g. assembling-an-ai-publishing-agency)")
    parser.add_argument("--all-published", action="store_true", help="Batch process all published articles")
    parser.add_argument("--provider", choices=["piper", "elevenlabs"], default="piper", help="TTS Engine (default: piper)")
    parser.add_argument("--voice", type=str, default="", help="Voice selection (e.g. aru, alan, thorsten)")
    parser.add_argument("--extract-only", action="store_true", help="Only extract and save narration script")
    parser.add_argument("--import-audio", type=str, help="Path to existing MP3 file to import")
    parser.add_argument("--voice-id", type=str, default=os.getenv("ELEVENLABS_VOICE_ID", ""), help="ElevenLabs Voice ID")
    parser.add_argument("--narrator", type=str, default="", help="Custom narrator label")
    parser.add_argument("--output-name", type=str, help="Custom filename for output MP3")

    args = parser.parse_args()

    if args.all_published:
        posts = sorted(list(PUBLISHED_DIR.glob("*.md")))
        print(f"🚀 Starting batch audio generation for {len(posts)} published articles using Piper...")
        for p in posts:
            uid = p.stem
            try:
                process_single_post(uid, args)
            except Exception as e:
                print(f"⚠️ Failed to process {uid}: {e}", file=sys.stderr)
    elif args.uid:
        process_single_post(args.uid, args)
    else:
        parser.print_help()


if __name__ == "__main__":
    main()
