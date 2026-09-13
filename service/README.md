# Piper TTS & Multilingual Translation Microservice (Cloud Run)

A serverless Text-to-Speech (TTS) and machine translation microservice built with **FastAPI**, **Piper ONNX**, and **Gemini Flash**.

Deployed to **Google Cloud Run** and rewritten via **Firebase Hosting** at `/api/tts`.

---

## 1. Google Query Parameter Convention

The service adopts Google's standard **`hl`** (**Host Language**) parameter:

```http
GET /api/tts?uid=<post-uid>&hl=<language-code>[&voice=<voice-override>]
```

| Parameter | Type | Required | Description | Example |
| :--- | :--- | :---: | :--- | :--- |
| **`uid`** | `string` | **Yes** | Post unique identifier | `assembling-an-ai-publishing-agency` |
| **`hl`** | `string` | No | Google standard Host Language code (defaults to `en-GB`) | `en-GB`, `de-DE`, `pt-BR`, `es-ES` |
| **`voice`** | `string` | No | Optional Piper voice override | `aru`, `alan`, `thorsten`, `faber`, `davefx` |

### Supported `hl` Language Codes & Default Piper Voices

| `hl` Code | Language | Default Piper Voice | Translation Engine |
| :--- | :--- | :--- | :--- |
| **`en-GB`** (or `en`) | British English | `en_GB-aru-medium` | Source prose |
| **`de-DE`** (or `de`) | German | `de_DE-thorsten-medium` | Gemini Flash (if source != German) |
| **`pt-BR`** (or `pt`) | Brazilian Portuguese | `pt_BR-faber-medium` | Gemini Flash |
| **`es-ES`** (or `es`) | Spanish | `es_ES-davefx-medium` | Gemini Flash |

---

## 2. Architecture & Edge CDN Caching

```
Browser  -->  Firebase Hosting  -->  Cloud Run (FastAPI + Piper)
                  |                          |
             Cloud CDN                Gemini Flash (Translation)
         (Cached for 30 days)                |
                                        Piper ONNX (TTS)
                                             |
                                        ffmpeg (64kbps MP3)
```

- **Firebase Hosting Rewrite**: Any request to `https://jochen.kirstaetter.name/api/tts/**` is proxied directly to Cloud Run.
- **Cloud CDN Edge Caching**: Responses return `Cache-Control: public, max-age=86400, s-maxage=2592000`.
  - The first listener triggers translation and synthesis (~5–10s).
  - Every subsequent listener across the globe receives the cached audio file in **~15ms** with 0 compute cost.

---

## 3. Local Development & Testing

### Running Locally with Python Virtual Environment
```bash
# Set Gemini API key for translation:
export GEMINI_API_KEY="your-gemini-api-key"

# Run locally on port 8080:
.venv/bin/python -m uvicorn service.main:app --port 8080 --reload
```

### Test Endpoints
```bash
# 1. Health check:
curl http://localhost:8080/health

# 2. Synthesise English (UK):
curl -o test_en.mp3 "http://localhost:8080/api/tts?uid=article-templates&hl=en-GB"

# 3. Translate & synthesise Portuguese (Brazil):
curl -o test_pt.mp3 "http://localhost:8080/api/tts?uid=article-templates&hl=pt-BR"

# 4. Translate & synthesise Spanish:
curl -o test_es.mp3 "http://localhost:8080/api/tts?uid=article-templates&hl=es-ES"
```

---

## 4. Deploying to Google Cloud Run

To deploy to project `getblogged-b8929` in region `europe-west1`:

```bash
# 1. Build and deploy container directly to Cloud Run:
gcloud run deploy piper-tts \
  --source ./service \
  --project getblogged-b8929 \
  --region europe-west1 \
  --memory 1Gi \
  --cpu 2 \
  --timeout 300s \
  --concurrency 10 \
  --allow-unauthenticated \
  --set-env-vars "GEMINI_API_KEY=your-gemini-api-key,BLOG_BASE_URL=https://jochen.kirstaetter.name"

# 2. Deploy updated Firebase Hosting rewrite:
firebase deploy --only hosting
```
