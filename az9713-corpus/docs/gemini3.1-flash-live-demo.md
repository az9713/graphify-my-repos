---
repo: gemini3.1-flash-live-demo
description: Real-time audio + video demo using Gemini 3.1 Flash Live model and the Gemini Live API
language: JavaScript
stars: 0
forks: 0
created: 2026-03-28
updated: 2026-03-31
topics: 
is_fork: False
kb: 164
---

# gemini3.1-flash-live-demo
# Gemini Live — Real-Time Audio + Video Demo

A single-page web app showcasing the **Gemini 3.1 Flash Live** model via the **Gemini Live API**. Stream your microphone and webcam (or screen) directly to Gemini and get real-time spoken responses back — all with low latency, barge-in support, and live transcription.

![Demo](docs/demo.jpg)

---

## Inspiration

This project was inspired by the YouTube video by **Nate Herk**:
[**Google Gemini 3.1 Flash Live — Build Voice Agents with Claude Code**](https://www.youtube.com/watch?v=Qt3zMBH-FNg)

Nate walks through the Gemini 3.1 Flash Live model, demos it in Google AI Studio, and builds two working apps using Claude Code. This project is a clean, standalone implementation of the audio + video showcase concept he demonstrated.

---

## What It Does

- **Speech-to-speech** — talk naturally, Gemini responds with voice (no text-to-speech pipeline)
- **Vision** — share your webcam or screen; Gemini sees and reacts to what's in frame
- **Barge-in** — interrupt Gemini mid-sentence and it stops immediately
- **Live transcript** — real-time captions for both your speech and Gemini's responses
- **Secure** — your API key never touches the browser (ephemeral token pattern)

---

## Model & API

| Detail | Value |
|--------|-------|
| Model | `gemini-3.1-flash-live-preview` |
| API | [Gemini Live API](https://ai.google.dev/gemini-api/docs/live-api) |
| Protocol | Stateful WebSocket (WSS) |
| Audio in | 16-bit PCM, 16 kHz mono |
| Audio out | 16-bit PCM, 24 kHz mono |
| Video in | JPEG frames @ 1 FPS |

---

## Architecture

```
Browser                          Python Server              Gemini API
───────                          ─────────────              ──────────
Click Connect  ──POST /api/token──>  mint ephemeral token
               <── { token } ──────
Open WebSocket ──────────────────────────────────────────> generativelanguage.googleapis.com
Stream mic audio (PCM 16kHz) ──────────────────────────────────────────>
Stream camera/screen (JPEG 1fps) ───────────────────────────────────────>
                               <──── audio response (PCM 24kHz) ─────────
                               <──── transcripts ────────────────────────
```

The browser connects **directly** to Gemini's WebSocket endpoint using a short-lived ephemeral token — the Python server only mints tokens and serves static files.

---

## Tech Stack

- **Backend:** Python 3.11+, `aiohttp`, `google-genai`, `python-dotenv`
- **Frontend:** Vanilla JS (ES modules), Web Audio API `AudioWorklet`, WebSocket API, `getUserMedia` / `getDisplayMedia`
- **No build step** — runs straight from source

---

## Project Structure

```
├── server.py                        # aiohttp server — token endpoint + static files
├── requirements.txt
├── .env.example
└── frontend/
    ├── index.html                   # App shell
    ├── style.css                    # Dark theme UI
    ├── app.js                       # UI orchestration
    ├── gemini-live.js               # Gemini Live WebSocket client
    ├── media-utils.js               # AudioStreamer, VideoStreamer, ScreenCapture, AudioPlayer
    └── audio-processors/
        ├── capture.worklet.js       # Mic → PCM16 (AudioWorklet)
        └── playback.worklet.js      # PCM24kHz → speakers (AudioWorklet)
```

---

## Getting Started

### Prerequisites

- Python 3.11+
- A [Gemini API key](https://aistudio.google.com/app/apikey) with access to `gemini-3.1-flash-live-preview`
- Chrome (recommended for WebRTC/AudioWorklet support)

### Setup

```bash
# 1. Clone
git clone https://github.com/az9713/gemini3.1-flash-live-demo.git
cd gemini3.1-flash-live-demo

# 2. Create virtual environment and install deps
python -m venv .venv
source .venv/bin/activate        # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# 3. Add your API key
cp .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here

# 4. Start the server
python server.py
```

Then open **http://localhost:8000** in Chrome.

---

## Usage

| Action | How |
|--------|-----|
| Connect | Click **▶ Connect** — mic auto-starts |
| Talk | Speak naturally, Gemini responds with voice |
| Interrupt | Just talk over Gemini — it stops immediately |
| Camera | Click **📷 Camera** — Gemini sees your webcam |
| Screen share | Click **🖥️ Screen** — Gemini sees your screen |
| Mute | Click **🎤 Mic On** to toggle |
| Disconnect | Click **■ Disconnect** |

---

## References

- [Gemini 3.1 Flash Live Preview — Model Card](https://ai.google.dev/gemini-api/docs/models/gemini-3.1-flash-live-preview)
- [Gemini Live API Docs](https://ai.google.dev/gemini-api/docs/live-api)
- [google-gemini/gemini-live-api-examples](https://github.com/google-gemini/gemini-live-api-examples)
- [Nate Herk's YouTube Channel](https://www.youtube.com/@nateherk)
- [Debugging Notes](docs/DEBUGGING.md) — problems encountered integrating the Gemini Live API and how they were resolved
