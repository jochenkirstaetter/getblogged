#!/usr/bin/env python3
"""
service/main.py
FastAPI microservice for dynamic, on-the-fly text-to-speech (Piper)
and translation (Gemini Flash) deployed to Google Cloud Run and rewritten
via Firebase Hosting at /api/tts.

Google-style language parameter 'hl':
  - hl=en-GB (or en)    -> English (Piper: en_GB-alan-medium or en_GB-aru-medium)
  - hl=de-DE (or de)    -> German  (Piper: de_DE-thorsten-medium)
  - hl=pt-BR (or pt)    -> Brazilian Portuguese (Piper: pt_BR-faber-medium)
  - hl=es-ES (or es)    -> Spanish (Piper: es_ES-davefx-medium)
"""

import os
import re
import sys
import tempfile
import subprocess
from pathlib import Path
from typing import Optional

import httpx
from fastapi import FastAPI, HTTPException, Query, Response
from fastapi.middleware.cors import CORSMiddleware

# Initialize FastAPI
app = FastAPI(
    title="GetBlogged Piper TTS & Translation Service",
    description="On-the-fly multilingual speech synthesis with Piper ONNX and Gemini translation.",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET", "OPTIONS"],
    allow_headers=["*"],
)

# Configuration & Paths
BLOG_BASE_URL = os.getenv("BLOG_BASE_URL", "https://jochen.kirstaetter.name")
PIPER_CACHE_DIR = Path(os.getenv("PIPER_MODELS_DIR", Path.home() / ".cache" / "piper" / "models"))
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

USER_AGENT = "OpenAI File Downloader, XaiImageApiFetch/1.0"

# Supported Language Mappings (Google 'hl' query parameter convention)
HL_LANGUAGE_CONFIG = {
    "en": {
        "name": "English",
        "default_voice": "en_GB-aru-medium",
        "voices": ["en_GB-aru-medium", "en_GB-alan-medium"],
        "prompt_name": "English"
    },
    "en-gb": {
        "name": "English (UK)",
        "default_voice": "en_GB-aru-medium",
        "voices": ["en_GB-aru-medium", "en_GB-alan-medium"],
        "prompt_name": "British English"
    },
    "en-us": {
        "name": "English (US)",
        "default_voice": "en_GB-aru-medium",
        "voices": ["en_GB-aru-medium"],
        "prompt_name": "English"
    },
    "de": {
        "name": "German",
        "default_voice": "de_DE-thorsten-medium",
        "voices": ["de_DE-thorsten-medium"],
        "prompt_name": "German"
    },
    "de-de": {
        "name": "German (Germany)",
        "default_voice": "de_DE-thorsten-medium",
        "voices": ["de_DE-thorsten-medium"],
        "prompt_name": "German"
    },
    "pt": {
        "name": "Portuguese",
        "default_voice": "pt_BR-faber-medium",
        "voices": ["pt_BR-faber-medium"],
        "prompt_name": "Brazilian Portuguese"
    },
    "pt-br": {
        "name": "Portuguese (Brazil)",
        "default_voice": "pt_BR-faber-medium",
        "voices": ["pt_BR-faber-medium"],
        "prompt_name": "Brazilian Portuguese"
    },
    "es": {
        "name": "Spanish",
        "default_voice": "es_ES-davefx-medium",
        "voices": ["es_ES-davefx-medium"],
        "prompt_name": "Spanish"
    },
    "es-es": {
        "name": "Spanish (Spain)",
        "default_voice": "es_ES-davefx-medium",
        "voices": ["es_ES-davefx-medium"],
        "prompt_name": "European Spanish"
    }
}

GERMAN_STOPWORDS = {
    "der", "die", "das", "und", "ist", "in", "den", "von", "zu", "mit", "sich",
    "des", "auf", "für", "eine", "ein", "nicht", "dem", "auch", "es", "an",
    "werden", "aus", "er", "hat", "dass", "sie", "nach", "wird", "bei", "einer"
}

PRONUNCIATION_EN = [
    (r"\bDocFX\b", "Doc F X"),
    (r"\bDocFx\b", "Doc F X"),
    (r"\bGhostFx\b", "Ghost F X"),
    (r"\bghostfx\b", "ghost F X"),
    (r"\b\.NET\b", "Dot Net"),
    (r"\bCLI\b", "C L I"),
    (r"\bAPI\b", "A P I"),
    (r"\bYAML\b", "Yammel"),
    (r"\bJSON\b", "Jason"),
    (r"\bVFP\b", "Visual FoxPro"),
    (r"\bNginx\b", "Engine X"),
    (r"\bSQLite\b", "Sequel Lite"),
    (r"\bSQL\b", "Sequel"),
    (r"\bMSCC\b", "M S C C"),
    (r"\bGDG\b", "G D G"),
    (r"\bi\.e\.", "that is"),
    (r"\be\.g\.", "for example"),
    (r"\betc\.", "etcetera"),
]

PRONUNCIATION_DE = [
    (r"\bz\.B\.", "zum Beispiel"),
    (r"\bd\.h\.", "das heißt"),
    (r"\bbzw\.", "beziehungsweise"),
    (r"\busw\.", "und so weiter"),
    (r"\bca\.", "zirka"),
    (r"\bggf\.", "gegebenenfalls"),
    (r"\b\.NET\b", "Dot Net"),
    (r"\bVFP\b", "Visual FoxPro"),
    (r"\bSQL\b", "Sequel"),
]


def detect_source_language(body: str) -> str:
    words = set(re.findall(r"\b[a-zäöüß]+\b", body.lower()[:2000]))
    if len(words.intersection(GERMAN_STOPWORDS)) >= 6:
        return "de"
    return "en"


def sanitize_markdown(body: str, title: str = "", lang: str = "en") -> str:
    text = body
    text = re.sub(r"<!--.*?-->", "", text, flags=re.DOTALL)
    text = re.sub(r"<[^>]+>", " ", text)
    text = re.sub(r"```[a-zA-Z0-9_-]*\n.*?\n```", "\n\n[Code snippet omitted for audio]\n\n", text, flags=re.DOTALL)
    text = re.sub(r":::\s*[a-zA-Z0-9_-]*", "", text)
    text = re.sub(r">\s*\[![A-Z]+\]", "", text)
    text = re.sub(r"^>\s*", "", text, flags=re.MULTILINE)
    text = re.sub(r"!\[(.*?)\]\(.*?\)", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\([^)]+\)", r"\1", text)
    text = re.sub(r"^#{1,6}\s+(.+)$", r"\1.\n", text, flags=re.MULTILINE)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\*\*([^*]+)\*\*", r"\1", text)
    text = re.sub(r"\*([^*]+)\*", r"\1", text)
    text = re.sub(r"^\s*[-*_]{3,}\s*$", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*[-*+]\s+", "", text, flags=re.MULTILINE)
    text = re.sub(r"^\s*\d+\.\s+", "", text, flags=re.MULTILINE)

    pmap = PRONUNCIATION_DE if lang == "de" else PRONUNCIATION_EN
    for pattern, repl in pmap:
        text = re.sub(pattern, repl, text)

    paragraphs = [p.strip() for p in text.split("\n\n") if p.strip()]
    cleaned = "\n\n".join(paragraphs)
    if title and not cleaned.startswith(title):
        cleaned = f"{title}.\n\n" + cleaned
    return cleaned


async def fetch_article_markdown(uid: str) -> tuple[str, str]:
    """Fetch raw markdown from local workspace or public URL."""
    # 1. Check local file paths first (for local testing / container mount)
    for base in [Path("posts/published"), Path("posts/draft"), Path("posts/_site/raw")]:
        candidate = base / f"{uid}.md"
        if candidate.is_file():
            content = candidate.read_text(encoding="utf-8")
            match = re.match(r"^---\s*\n(.*?)\n---\s*\n?(.*)$", content, re.DOTALL)
            title = ""
            if match:
                for line in match.group(1).splitlines():
                    if line.startswith("title:"):
                        title = line.split(":", 1)[1].strip().strip('"\'')
                return match.group(2), title
            return content, ""

    # 2. Fetch from public blog via raw markdown endpoint
    urls = [
        f"{BLOG_BASE_URL}/raw/{uid}.md",
        f"https://jochen.kirstaetter.name/raw/{uid}.md"
    ]
    async with httpx.AsyncClient(headers={"User-Agent": USER_AGENT}) as client:
        for url in urls:
            try:
                resp = await client.get(url, timeout=5.0)
                if resp.status_code == 200:
                    text = resp.text
                    lines = text.strip().splitlines()
                    title = lines[0].lstrip("# ").strip() if lines else ""
                    return text, title
            except Exception:
                pass

    raise HTTPException(status_code=404, detail=f"Article '{uid}' not found.")


async def translate_text_with_gemini(text: str, target_lang_name: str) -> str:
    """Translate text using Gemini 2.5 Flash via google-genai or REST API."""
    if not GEMINI_API_KEY:
        print("⚠️ GEMINI_API_KEY not configured. Skipping translation.")
        return text

    try:
        from google import genai
        client = genai.Client(api_key=GEMINI_API_KEY)
        prompt = (
            f"You are an expert technical translator. Translate the following technical blog article "
            f"into natural, fluent, spoken {target_lang_name}. "
            f"Keep software brand names, acronyms (.NET, DocFX, CLI, API, GCP), and technical terminology intact. "
            f"Output ONLY the translated text without commentary or quotation marks:\n\n"
            f"{text}"
        )
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt,
        )
        if response and response.text:
            return response.text.strip()
    except Exception as e:
        print(f"⚠️ Gemini translation error: {e}", file=sys.stderr)

    return text


def synthesize_with_piper(text: str, model_name: str) -> bytes:
    """Run Piper binary on ONNX model and convert output to 64kbps MP3."""
    onnx_file = PIPER_CACHE_DIR / f"{model_name}.onnx"
    if not onnx_file.is_file():
        raise HTTPException(status_code=500, detail=f"Model '{model_name}' is not installed in {PIPER_CACHE_DIR}")

    piper_bin = subprocess.run(["which", "piper"], capture_output=True, text=True).stdout.strip()
    if not piper_bin:
        local_bin = Path.home() / ".local" / "piper" / "piper"
        if local_bin.is_file():
            piper_bin = str(local_bin)
        else:
            piper_bin = "/usr/local/piper/piper"

    with tempfile.TemporaryDirectory() as tmpdir:
        wav_path = Path(tmpdir) / "out.wav"
        mp3_path = Path(tmpdir) / "out.mp3"

        # 1. Synthesize WAV
        proc = subprocess.Popen(
            [piper_bin, "--model", str(onnx_file), "--output_file", str(wav_path)],
            stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True
        )
        stdout, stderr = proc.communicate(input=text)
        if proc.returncode != 0:
            raise HTTPException(status_code=500, detail=f"Piper synthesis error: {stderr}")

        # 2. Compress to MP3
        cmd = ["ffmpeg", "-y", "-i", str(wav_path), "-c:a", "libmp3lame", "-b:a", "64k", str(mp3_path)]
        subprocess.run(cmd, capture_output=True, check=True)

        return mp3_path.read_bytes()


@app.get("/health")
def health_check():
    return {
        "status": "healthy",
        "piper_models_dir": str(PIPER_CACHE_DIR),
        "available_models": [f.stem for f in PIPER_CACHE_DIR.glob("*.onnx")] if PIPER_CACHE_DIR.is_dir() else []
    }


@app.get("/api/tts")
async def get_tts_audio(
    uid: str = Query(..., description="Post UID (e.g. assembling-an-ai-publishing-agency)"),
    hl: str = Query("en-GB", description="Host Language parameter (e.g. en-GB, de-DE, pt-BR, es-ES)"),
    voice: Optional[str] = Query(None, description="Optional Piper voice override (e.g. aru, alan, thorsten, faber, davefx)")
):
    """
    Generate on-the-fly audio narration for a blog article.
    Rewritten via Firebase Hosting from /api/tts.
    """
    # 1. Resolve language and voice configuration
    hl_key = hl.lower().strip()
    lang_info = HL_LANGUAGE_CONFIG.get(hl_key)
    if not lang_info:
        # Fallback to 2-letter prefix
        prefix = hl_key.split("-")[0]
        lang_info = HL_LANGUAGE_CONFIG.get(prefix, HL_LANGUAGE_CONFIG["en"])

    target_lang_code = hl_key.split("-")[0]
    target_voice = voice or lang_info["default_voice"]

    # If voice alias was given (e.g. 'aru')
    if voice:
        for candidate in lang_info["voices"]:
            if voice.lower() in candidate.lower():
                target_voice = candidate
                break

    # 2. Fetch article content
    body, title = await fetch_article_markdown(uid)
    source_lang = detect_source_language(body)

    # 3. Translate if target language differs from source
    speech_text = sanitize_markdown(body, title, lang=source_lang)
    if target_lang_code != source_lang:
        print(f"🌐 Translating article '{uid}' ({source_lang} -> {lang_info['prompt_name']})...")
        speech_text = await translate_text_with_gemini(speech_text, lang_info["prompt_name"])

    # 4. Synthesize with Piper
    print(f"🎙️ Synthesizing '{uid}' with voice '{target_voice}'...")
    mp3_data = synthesize_with_piper(speech_text, target_voice)

    # 5. Return MP3 with long CDN cache headers
    return Response(
        content=mp3_data,
        media_type="audio/mpeg",
        headers={
            "Cache-Control": "public, max-age=86400, s-maxage=2592000",
            "X-TTS-Voice": target_voice,
            "X-TTS-Language": target_lang_code
        }
    )


if __name__ == "__main__":
    import uvicorn
    port = int(os.getenv("PORT", 8080))
    uvicorn.run("main:app", host="0.0.0.0", port=port, reload=True)
