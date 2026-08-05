---
repo: ai-video-pipeline
description: Transform natural language questions into VTuber-style video responses. Educational project demonstrating Gemini, Qwen3-TTS, and OmniHuman integration.
language: Python
stars: 0
forks: 0
created: 2026-01-24
updated: 2026-01-25
topics: 
is_fork: False
kb: 5633
---

# ai-video-pipeline
# AI Video Pipeline

Transform natural language questions into VTuber-style video responses.

> **Educational Use Only:** This project is intended for educational and research purposes. It is not intended for commercial use or profit. See [License & Disclaimer](#license--disclaimer) below.

## Quick Start

```bash
python pipeline.py "What is the latest news in AI?"
```

**Output:** `output/oracle_<timestamp>.mp4`

---

## Setup

### 1. Create Virtual Environment

```bash
# Create venv
python -m venv venv

# Activate (Windows Command Prompt)
venv\Scripts\activate

# Activate (Windows Git Bash / MINGW64)
source venv/Scripts/activate

# Activate (Mac/Linux)
source venv/bin/activate
```

**Troubleshooting:** If packages install globally instead of in venv, see [Issue 3 in TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md#issue-3-virtual-environment-not-activating-properly).

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure API Keys

```bash
cp .env.example .env
```

Edit `.env` with your API keys:
- `GEMINI_API_KEY` - Get from [Google AI Studio](https://aistudio.google.com/app/apikey)
- `FAL_KEY` - Get from [fal.ai Dashboard](https://fal.ai/dashboard/keys)

### 4. Install FFmpeg

Download from [ffmpeg.org](https://ffmpeg.org/download.html) and add to PATH.

### 5. Add Required Assets

```
assets/
├── voice/
│   ├── vtube.wav          # Reference voice (included)
│   └── transcript.txt     # Voice transcript (included)
├── image/
│   └── vtube.jpg          # Avatar image (included, or provide your own)
└── music/
    └── *.mp3              # Background tracks (YOU PROVIDE)
```

**Note:** The avatar image can be `.jpg` or `.png`. Update `config/settings.py` if using a different filename.

### 6. Validate Setup

```bash
python validate_env.py
```

---

## Usage

```bash
# Basic usage
python pipeline.py "your question here"

# Custom output path
python pipeline.py "your question" -o output/my_video.mp4

# Verbose logging
python pipeline.py "your question" -v
```

---

## Pipeline Architecture

```
┌─────────────────────────────────────────────────────────────────────────────────────┐
│                            AI VIDEO PIPELINE ARCHITECTURE                            │
└─────────────────────────────────────────────────────────────────────────────────────┘

  "Your Question"
        │
        ▼
┌───────────────┐    Text     ┌───────────────┐    Audio    ┌───────────────┐
│   01 ANSWER   │   (≤50     │   02 VOICE    │    (.wav)   │   03 UPLOAD   │
│     GEN       │   words)    │     GEN       │   (≤20s)    │               │
│───────────────│ ──────────▶ │───────────────│ ──────────▶ │───────────────│
│ Gemini 2.5    │             │  Qwen3-TTS    │             │  fal.ai       │
│ Flash         │             │  1.7B Base    │             │  Storage      │
│ + Google      │             │  Voice Clone  │             │               │
│   Search      │             │               │             │ + Avatar IMG  │
└───────────────┘             └───────────────┘             └───────┬───────┘
                                                                    │
                              URLs (audio_url, image_url)           │
        ┌───────────────────────────────────────────────────────────┘
        │
        ▼
┌───────────────┐   Video     ┌───────────────┐    File     ┌───────────────┐
│   04 VIDEO    │    URL      │ 05 RETRIEVAL  │   (.mp4)    │ 06 POST-PROD  │
│     GEN       │             │               │             │               │
│───────────────│ ──────────▶ │───────────────│ ──────────▶ │───────────────│
│ OmniHuman     │             │  fal.ai CDN   │             │  FFmpeg       │
│ v1.5          │             │  Download     │             │  + Music      │
│ Lip-sync      │             │               │             │  (15% vol)    │
│ 720p          │             │               │             │               │
└───────────────┘             └───────────────┘             └───────┬───────┘
                                                                    │
                                                                    ▼
                                                          output/final.mp4
```

### Pipeline Steps

| Step | Module | API | Input | Output |
|------|--------|-----|-------|--------|
| 1 | `answer_generator.py` | Gemini 2.5 Flash | Question | Text (≤50 words) |
| 2 | `voice_generator.py` | Qwen3-TTS 1.7B | Text | Audio (≤20s) |
| 3 | `storage_manager.py` | fal.ai Storage | Audio + Image | CDN URLs |
| 4 | `video_generator.py` | OmniHuman v1.5 | URLs | Video URL |
| 5 | `video_retriever.py` | fal.ai CDN | Video URL | MP4 File |
| 6 | `post_processor.py` | FFmpeg | Video + Music | Final MP4 |

---

## Constraints

| Setting | Value |
|---------|-------|
| Max answer length | 50 words |
| Max audio duration | 20 seconds |
| Video resolution | 720p |
| Background music volume | 15% |

---

## Project Structure

```
ai-video-pipeline/
├── config/
│   └── settings.py           # Configuration
├── modules/
│   ├── answer_generator.py   # Step 1
│   ├── voice_generator.py    # Step 2
│   ├── storage_manager.py    # Step 3
│   ├── video_generator.py    # Step 4
│   ├── video_retriever.py    # Step 5
│   └── post_processor.py     # Step 6
├── utils/
│   ├── logger.py             # Logging
│   └── retry.py              # Retry decorator
├── assets/                   # Voice, image, music files
├── output/                   # Generated videos
├── temp/                     # Temporary files
├── pipeline.py               # Main orchestrator
├── validate_env.py           # Environment checker
├── requirements.txt
└── .env.example
```

---

## Documentation

| Document | Description |
|----------|-------------|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Pipeline architecture, component roles, and artifact flow |
| [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) | All known issues encountered during development and their solutions |
| [ROBUST_TOKEN_HANDLING.md](docs/ROBUST_TOKEN_HANDLING.md) | Advanced fix for Gemini token truncation (not yet implemented) |
| [api_sources.md](docs/api_sources.md) | API documentation links and references |

---

## Demo Materials

The `output/` and `assets/` folders contain example outputs and sample assets for demonstration purposes.

---

## License & Disclaimer

### Educational Purpose

This project is created for **educational and research purposes only**. It demonstrates how to:
- Integrate multiple AI APIs (Gemini, Qwen3-TTS, OmniHuman)
- Build automated video generation pipelines
- Work with voice cloning and lip-sync technology

**This project is NOT intended for commercial use or profit.**

### Third-Party Assets

Some assets included in this repository (`assets/voice/vtube.wav`, `assets/image/vtube.jpg`) are sourced from third-party websites for demonstration purposes only. The background music (`assets/music/*.mp3`) is an original creation by the developer and is not subject to third-party copyright. The third-party assets:
- Are included solely for educational demonstration
- Should not be used for commercial purposes
- May be subject to their original creators' copyright

If you are the copyright holder of any included asset and wish it removed, please open an issue.

### Code License

The source code in this repository is provided under the MIT License for educational purposes:

```
MIT License

Copyright (c) 2026

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### API Usage

This project uses the following third-party APIs:
- [Google Gemini API](https://ai.google.dev/) - Subject to Google's Terms of Service
- [fal.ai](https://fal.ai/) - Subject to fal.ai's Terms of Service
- [Qwen3-TTS](https://github.com/QwenLM/Qwen3-TTS) - Subject to Qwen's license terms

Users are responsible for complying with all applicable API terms of service.

---

## Acknowledgements

### Inspiration

This project was inspired by the YouTube video ["Claude Code Let's Build: The AI Video Oracle (Qwen3 TTS)"](https://www.youtube.com/watch?v=Vbws3a_OmBM).

### Asset Credits

- **Reference Voice (`vtube.wav`)**: [Kid Saying "Did I Do It Wrong?"](https://samplefocus.com/samples/kid-saying-did-i-do-it-wrong?search_id=186354948) from SampleFocus
- **Avatar Image (`vtube.jpg`)**: [Young Man Anime-Style Character](https://www.freepik.com/premium-vector/vector-young-man-animestyle-character-vector-illustration-design-manga-anime-boy_57672461.htm) from Freepik
- **Background Music (`Echo_of_Changing_Times_*.mp3`)**: Original composition created by the developer using [ElevenLabs](https://elevenlabs.io/)

### Development

All code and documentation in this repository were generated by [Claude Code](https://claude.ai/claude-code) powered by Claude Opus 4.5.

**Autonomous API Research:** Claude Code performed web searches for ALL API documentation autonomously. No API docs were manually curated or stored in local directories by the developer. Claude Code researched and integrated:
- Google Gemini API with Search Grounding
- Qwen3-TTS voice cloning
- fal.ai storage and OmniHuman v1.5
- FFmpeg command-line usage

**Development Timeline:** The application ran successfully on the **2nd attempt**. The only API that required correction was Qwen3-TTS (see [Issue 2 in TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md#issue-2-qwen_tts-api-mismatch-critical)), which Claude Code diagnosed and fixed by inspecting the actual package exports. The `max_output_tokens` issue (Issue 4) was discovered during subsequent testing, not the initial run.

---

*Built with Claude Code*
