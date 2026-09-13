# Build Piper TTS + Gemini Translation Microservice for Cloud Run
FROM python:3.11-slim

# Prevent python from buffering stdout/stderr
ENV PYTHONUNBUFFERED=1 \
    PORT=8080 \
    PIPER_MODELS_DIR=/app/models

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    curl \
    ca-certificates \
    && rm -rf /var/lib/apt/lists/*

# Install Piper standalone binary
RUN mkdir -p /usr/local/piper \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" \
       "https://github.com/rhasspy/piper/releases/download/2023.11.14-2/piper_linux_x86_64.tar.gz" \
       | tar -xz -C /usr/local/ \
    && ln -sf /usr/local/piper/piper /usr/local/bin/piper

# Create models directory and pre-download curated voice models
RUN mkdir -p /app/models \
    # English UK (Alan & Aru)
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/en_GB-alan-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/en_GB-alan-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/alan/medium/en_GB-alan-medium.onnx.json" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/en_GB-aru-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/aru/medium/en_GB-aru-medium.onnx" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/en_GB-aru-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/en/en_GB/aru/medium/en_GB-aru-medium.onnx.json" \
    # German (Thorsten)
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/de_DE-thorsten-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/de_DE-thorsten-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/de/de_DE/thorsten/medium/de_DE-thorsten-medium.onnx.json" \
    # Portuguese Brazil (Faber)
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/pt_BR-faber-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/pt_BR-faber-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/pt/pt_BR/faber/medium/pt_BR-faber-medium.onnx.json" \
    # Spanish (DaveFX)
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/es_ES-davefx-medium.onnx "https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx" \
    && curl -sL -A "OpenAI File Downloader, XaiImageApiFetch/1.0" -o /app/models/es_ES-davefx-medium.onnx.json "https://huggingface.co/rhasspy/piper-voices/resolve/main/es/es_ES/davefx/medium/es_ES-davefx-medium.onnx.json"

# Install Python packages
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application source code
COPY main.py .

EXPOSE 8080

CMD ["python", "-m", "uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8080"]
