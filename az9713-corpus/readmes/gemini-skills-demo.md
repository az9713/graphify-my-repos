# Gemini Skills Demo

Three practical CLI tools, each built to showcase a distinct set of Gemini API capabilities. Every demo was generated from a single natural-language prompt using **Claude Code** with the **[superpowers plugin](https://github.com/obra/superpowers)** and a corresponding Gemini skill installed.

---

## What Are Gemini Skills?

Skills are Markdown documents that inject up-to-date Gemini API knowledge into an AI coding agent before it writes any code. Without them, the agent falls back on training data — which may reference deprecated SDKs, old model names, or outdated patterns.

Skills are distributed via the [`google-gemini/gemini-skills`](https://github.com/google-gemini/gemini-skills) repository and activated by the [superpowers plugin](https://github.com/obra/superpowers) for Claude Code.

Install a skill globally:
```bash
npx skills add google-gemini/gemini-skills@<skill-name> -g
```

---

## Demos

| Demo | Skill | Gemini Features | Language |
|------|-------|----------------|----------|
| [`snap2data/`](#snap2data--visual-data-extractor) | `gemini-api-dev` | Multimodal input, structured output, function calling | Python |
| [`deepdive/`](#deepdive--research--discussion-cli) | `gemini-interactions-api` | Deep Research agent, server-side stateful chat, streaming | TypeScript |
| [`voicenote/`](#voicenote--real-time-voice-notepad) | `gemini-live-api-dev` | Bidirectional audio streaming, transcription, VAD, session resumption | Python |

---

## snap2data — Visual Data Extractor

**Skill:** `gemini-api-dev`

Extracts structured data from images — receipts, business cards, tables, handwritten notes — and outputs JSON, CSV, or an ASCII table. A `--save` flag demonstrates function calling: instead of writing the file directly, the model is asked to invoke a `save_to_file` tool.

**Gemini features used:**
- **Multimodal input** — raw image bytes + text prompt in one call
- **Structured output** — Pydantic model as `response_json_schema`, validated at runtime
- **Function calling** — model invokes `save_to_file`, CLI executes it locally

**Install & run:**
```bash
cd snap2data_demo
pip install -e .
cp .env.example .env        # add your GEMINI_API_KEY
python -m snap2data.cli extract docs/test_receipt.jpg --mode receipt --format table
python -m snap2data.cli extract docs/test_receipt.jpg --mode receipt --save out.json
python -m snap2data.cli extract docs/test_receipt.jpg --mode general --format json
```

**Extraction modes:** `receipt` · `card` · `table` · `general`

See [`snap2data_demo/docs/CASE_STUDY.md`](snap2data_demo/docs/CASE_STUDY.md) for a full walkthrough from prompt to verified output.

---

## deepdive — Research & Discussion CLI

**Skill:** `gemini-interactions-api`

Terminal research assistant. Launch a Deep Research job on any topic in the background, then have a multi-turn stateful conversation about the findings. The server retains full context — you never resend the report.

**Gemini features used:**
- **Deep Research agent** — `interactions.create` with `background: true`, polled via `interactions.get`
- **Server-side stateful chat** — `previous_interaction_id` chains turns without resending history
- **Streaming** — `stream: true`, processes `content.delta` SSE events

**Install & run:**
```bash
cd deepdive
npm install
cp ../.env.example ../.env  # add your GEMINI_API_KEY
npm run build
node dist/index.js
# In the REPL: /research quantum computing
```

**Commands:** `/research <topic>` · `/status` · `/new` · `/quit` · or freeform chat

---

## voicenote — Real-time Voice Notepad

**Skill:** `gemini-live-api-dev`

Voice-powered note-taking over a live WebSocket connection. Speak into your mic; Gemini transcribes and acknowledges. Ask it to organize or summarize your notes by voice. Notes save as timestamped markdown. Includes a reconnect command that proves session context survives disconnection.

**Gemini features used:**
- **Bidirectional audio streaming** — PCM audio in (16 kHz) and out (24 kHz) via `send_realtime_input`
- **Input + output transcription** — `AudioTranscriptionConfig` on both directions
- **VAD** — automatic turn detection, interruption handling
- **Session resumption** — reconnect with a session handle, full context retained

**Install & run:**
```bash
cd voicenote
pip install -r requirements.txt   # includes pyaudio
cp ../.env.example ../.env         # add your GEMINI_API_KEY
python -m voicenote.cli
# Keys: [s] save notes  [r] reconnect (session resumption demo)  [q] quit
```

> **Note:** PyAudio requires `portaudio` on your system. On macOS: `brew install portaudio`. On Ubuntu: `sudo apt install portaudio19-dev`.

---

## Setup

All three demos read `GEMINI_API_KEY` from a `.env` file at the project root:

```bash
cp .env.example .env
# Edit .env and set GEMINI_API_KEY=your_key_here
```

For full setup instructions and a step-by-step guide to running each demo, see [`QUICKSTART.md`](QUICKSTART.md).

---

## How the Code Was Generated

Each demo was created from a single natural-language prompt given to Claude Code with:
1. The [superpowers plugin](https://github.com/obra/superpowers) installed (enables skill injection)
2. The corresponding Gemini skill active (e.g., `gemini-api-dev`)

The skill ensured the generated code used the correct SDK (`from google import genai`), current model names, and up-to-date API patterns. See [`QUICKSTART.md`](QUICKSTART.md) for the exact prompts used to generate each demo.

The `snap2data_demo/` directory is the generated output of a live walkthrough documented in [`snap2data_demo/docs/CASE_STUDY.md`](snap2data_demo/docs/CASE_STUDY.md).
