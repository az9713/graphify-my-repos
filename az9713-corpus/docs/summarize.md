---
repo: summarize
description: Clone of github.com/steipete/summarize — Link summarization tool (CLI + Chrome Extension + Daemon) with PDF URL support
language: TypeScript
stars: 0
forks: 0
created: 2026-02-16
updated: 2026-07-10
topics: 
is_fork: False
kb: 8462
---

# summarize
# Summarize 📝 — Chrome Side Panel + CLI

> **This repository is a clone of [https://github.com/steipete/summarize](https://github.com/steipete/summarize).**
> The original project is created and maintained by [Peter Steinberger (@steipete)](https://github.com/steipete).
> This clone is for study, documentation, and local development purposes.
> For the latest updates, issues, and contributions, please refer to the [original repository](https://github.com/steipete/summarize).

**NEW: PDF summarization in the Chrome extension** — navigate to any PDF URL and click Summarize. The daemon downloads and converts it server-side via `markitdown`, then streams a full Markdown summary.

![Summarize PDF in Chrome extension](docs/summarize_pdf.jpg)

---

![GitHub Repo Banner](https://ghrb.waren.build/banner?header=Summarize%F0%9F%93%9D&subheader=Chrome+Side+Panel+%2B+CLI&bg=f3f4f6&color=1f2937&support=true)

<!-- Created with GitHub Repo Banner by Waren Gonzaga: https://ghrb.waren.build -->

Fast summaries from URLs, files, and media — including PDFs, YouTube, podcasts, and images. Works in the terminal, a Chrome Side Panel and Firefox Sidebar.

**0.11.0 preview (unreleased):** this README reflects the upcoming release.

## 0.11.0 preview highlights (most interesting first)

- **PDF support in extension**: navigate to any PDF URL (arxiv, papers, docs) and click Summarize — the daemon downloads and converts the PDF server-side via `markitdown`, then streams a full summary.
- Chrome Side Panel **chat** (streaming agent + history) inside the sidebar.
- **YouTube slides**: screenshots + OCR + transcript cards, timestamped seek, OCR/Transcript toggle.
- Media-aware summaries: auto‑detect video/audio vs page content.
- Streaming Markdown + metrics + cache‑aware status.
- CLI supports URLs, files, podcasts, YouTube, audio/video, PDFs.

## Feature overview

- URLs, files, and media: web pages, PDFs, images, audio/video, YouTube, podcasts, RSS.
- Slide extraction for video sources (YouTube/direct media) with OCR + timestamped cards.
- Transcript-first media flow: published transcripts when available, Whisper fallback when not. Audio/video pipeline: `yt-dlp` (download) → `ffmpeg` (transcode/split) → `whisper.cpp` or cloud Whisper (speech→text) → LLM summary. All optional — only needed for audio/video content.
- Streaming output with Markdown rendering, metrics, and cache-aware status.
- Local, paid, and free models: OpenAI‑compatible local endpoints, paid providers, plus an OpenRouter free preset.
- Output modes: Markdown/text, JSON diagnostics, extract-only, metrics, timing, and cost estimates.
- Smart default: if content is shorter than the requested length, we return it as-is (use `--force-summary` to override).

### Why Summarize instead of asking an AI chatbot?

For simple web pages, pasting a URL into Claude or ChatGPT works fine. Summarize is built for what chatbots can't do: YouTube/podcast transcription (yt-dlp + Whisper), PDF parsing, video slide extraction (ffmpeg + OCR), SQLite caching (same URL twice is instant and free), cost tracking, batch processing, multi-provider switching, and one-click browser extension summaries.

## Get the extension (recommended)

![Summarize extension screenshot](docs/assets/summarize-extension.png)

One‑click summarizer for the current tab. Chrome Side Panel + Firefox Sidebar + local daemon for streaming Markdown.

**Chrome Web Store:** [Summarize Side Panel](https://chromewebstore.google.com/detail/summarize/cejgnmmhbbpdmjnfppjdfkocebngehfg)

YouTube slide screenshots (from the browser):

![Summarize YouTube slide screenshots](docs/assets/youtube-slides.png)

### Beginner quickstart (extension)

1. Install the CLI (choose one):
   - **npm** (cross‑platform): `npm i -g @steipete/summarize`
   - **Homebrew** (macOS arm64): `brew install steipete/tap/summarize`
2. Install the extension (Chrome Web Store link above) and open the Side Panel.
3. The panel shows a token + install command. Run it in Terminal:
   - `summarize daemon install --token <TOKEN>`

### The Daemon — What, Why, and How

#### What is it?

The daemon is a lightweight local HTTP server that runs in the background on your machine. It listens on `127.0.0.1:8787` (localhost only — never exposed to the network) and acts as the bridge between the browser extension and all the heavy processing that browsers can't do themselves.

The implementation lives in [`src/daemon/server.ts`](src/daemon/server.ts). The entry point is `runDaemonServer()` which creates a Node.js `http.Server`:

```typescript
// src/daemon/server.ts:452-468
export async function runDaemonServer({
  env, fetchImpl, config,
  port = config.port ?? DAEMON_PORT_DEFAULT,  // default: 8787
  signal, onListening, onSessionEvent,
}: { ... }): Promise<void> {
```

#### Why is it needed?

Chrome extensions run in a strict sandbox. They **cannot**:

1. **Run local binaries** — `yt-dlp` (YouTube audio download), `ffmpeg` (video processing, slide extraction), `tesseract` (OCR), `whisper.cpp` (audio transcription) are all command-line tools that only run natively on your OS
2. **Access the filesystem** — SQLite caching, saving slide images, reading local files
3. **Make unrestricted API calls** — CORS policies block direct browser-to-LLM-provider calls
4. **Run long computations** — Chrome kills idle service workers after ~30 seconds

The daemon solves all of these by running as a normal Node.js process on your machine:

```
Without daemon:  Extension --X--> LLM APIs        (blocked by CORS)
                 Extension --X--> yt-dlp, ffmpeg   (can't run binaries)
                 Extension --X--> filesystem        (sandboxed)

With daemon:     Extension --HTTP--> Daemon ---> LLM APIs      (no CORS issue)
                                     Daemon ---> yt-dlp, ffmpeg (native access)
                                     Daemon ---> SQLite cache   (filesystem)
                                     Daemon ---> slide images   (filesystem)
```

#### How does it work?

**Authentication:** Every `/v1/*` request requires a Bearer token. The token is generated when you install the daemon and shared with the extension. See [`src/daemon/server.ts:512-517`](src/daemon/server.ts):

```typescript
const token = readBearerToken(req);
const authed = token && token === config.token;
if (pathname.startsWith("/v1/") && !authed) {
  json(res, 401, { ok: false, error: "unauthorized" }, cors);
  return;
}
```

**HTTP API routes** (defined in [`src/daemon/server.ts`](src/daemon/server.ts)):

| Route                           | Method | Purpose                                                                                                       |
| ------------------------------- | ------ | ------------------------------------------------------------------------------------------------------------- |
| `/health`                       | GET    | Health check — no auth required. Returns `{ok, pid, version}`                                                 |
| `/v1/ping`                      | GET    | Auth verification — confirms Bearer token is valid                                                            |
| `/v1/summarize`                 | POST   | Start a summarization. Accepts `{url, text, title, model, length, ...}`. Returns `{ok, id}` with a session ID |
| `/v1/summarize/{id}/events`     | GET    | **SSE stream** — subscribe to real-time summary events for a session                                          |
| `/v1/agent`                     | POST   | Chat/agent requests from the extension (SSE or JSON response)                                                 |
| `/v1/tools`                     | GET    | Reports which local tools are available (`yt-dlp`, `ffmpeg`, `tesseract`)                                     |
| `/v1/models`                    | GET    | Lists available LLM models based on configured API keys                                                       |
| `/v1/logs`                      | GET    | Tail daemon logs (for troubleshooting)                                                                        |
| `/v1/processes`                 | GET    | List active/completed processing tasks                                                                        |
| `/v1/summarize/{id}/slides`     | GET    | Fetch extracted slide images for a session                                                                    |
| `/v1/slides/{sourceId}/{index}` | GET    | Stable URL for individual slide images (survives session cleanup)                                             |

**Streaming via SSE (Server-Sent Events):** When the extension requests a summary, the daemon creates a session and streams results back in real-time using SSE. Events are defined in [`src/shared/sse-events.ts`](src/shared/sse-events.ts):

```typescript
// src/shared/sse-events.ts:32-40
export type SseEvent =
  | { event: "meta";    data: { model, modelLabel, inputSummary, summaryFromCache } }
  | { event: "status";  data: { text: string } }           // "Extracting content..."
  | { event: "chunk";   data: { text: string } }           // streaming summary text
  | { event: "slides";  data: { sourceUrl, slides[] } }    // extracted slide images
  | { event: "metrics"; data: { elapsedMs, summary } }     // timing/cost info
  | { event: "done";    data: {} }                          // session complete
  | { event: "error";   data: { message: string } };       // something went wrong
```

Sessions are buffered in memory (max 2000 events or 512KB per session, 30-minute lifetime) so clients can reconnect without losing data. See [`src/daemon/server.ts:234-238`](src/daemon/server.ts):

```typescript
const MAX_SESSION_BUFFER_EVENTS = 2000;
const MAX_SESSION_BUFFER_BYTES = 512 * 1024;
const MAX_SESSION_LIFETIME_MS = 30 * 60_000;
```

**Typical request flow:**

1. Extension sends `POST /v1/summarize` with `{url: "https://example.com", model: "auto", length: "medium"}`
2. Daemon creates a session (UUID), responds `{ok: true, id: "abc-123"}`
3. Extension subscribes to `GET /v1/summarize/abc-123/events` (SSE)
4. Daemon extracts content (using core library's `createLinkPreviewClient`)
5. Daemon calls LLM via `generateTextWithModelId` / `streamTextWithModelId`
6. Daemon pushes events to all subscribed clients: `meta` → `status` → `chunk` (repeated) → `metrics` → `done`

**Platform service management:** The daemon registers as an auto-starting system service so it's always ready when you open the extension. The implementation is in [`src/daemon/cli.ts`](src/daemon/cli.ts) with platform-specific backends:

- **macOS:** `launchd` — see [`src/daemon/launchd.ts`](src/daemon/launchd.ts) (label: `com.steipete.summarize.daemon`)
- **Linux:** `systemd` user service — see [`src/daemon/systemd.ts`](src/daemon/systemd.ts)
- **Windows:** Scheduled Task — see [`src/daemon/schtasks.ts`](src/daemon/schtasks.ts) (task: `Summarize Daemon`)

**Daemon commands:**

```bash
summarize daemon install --token <TOKEN>   # Register + start as system service
summarize daemon install --token <TOKEN> --dev  # Use local source (for developers)
summarize daemon status                    # Check if running
summarize daemon restart                   # Restart after code changes
summarize daemon stop                      # Stop the service
summarize daemon uninstall                 # Remove autostart (keeps config)
```

**Configuration:** Stored in `~/.summarize/daemon.json` with the token, port, and a snapshot of environment variables (so the daemon has access to API keys even when started by the system service manager).

If you only want the **CLI**, you can skip the daemon install entirely — the CLI runs everything directly in-process.

Notes:

- Summarization only runs when the Side Panel is open.
- Auto mode summarizes on navigation (incl. SPAs); otherwise use the button.
- Tip: configure `free` via `summarize refresh-free` (needs `OPENROUTER_API_KEY`). Add `--set-default` to set model=`free`.

More:

- Step-by-step install: [apps/chrome-extension/README.md](apps/chrome-extension/README.md)
- Architecture + troubleshooting: [docs/chrome-extension.md](docs/chrome-extension.md)
- Firefox compatibility notes: [apps/chrome-extension/docs/firefox.md](apps/chrome-extension/docs/firefox.md)

### Slides (extension)

- Select **Video + Slides** in the Summarize picker.
- Slides render at the top; expand to full‑width cards with timestamps.
- Click a slide to seek the video; toggle **Transcript/OCR** when OCR is significant.
- Requirements: `yt-dlp` + `ffmpeg` for extraction; `tesseract` for OCR. Missing tools show an in‑panel notice.

### Advanced (unpacked / dev)

1. Build + load the extension (unpacked):
   - Chrome: `pnpm -C apps/chrome-extension build`
     - `chrome://extensions` → Developer mode → Load unpacked
     - Pick: `apps/chrome-extension/.output/chrome-mv3`
   - Firefox: `pnpm -C apps/chrome-extension build:firefox`
     - `about:debugging#/runtime/this-firefox` → Load Temporary Add-on
     - Pick: `apps/chrome-extension/.output/firefox-mv3/manifest.json`
2. Open Side Panel/Sidebar → copy token.
3. Install daemon in dev mode:
   - `pnpm summarize daemon install --token <TOKEN> --dev`

## CLI

![Summarize CLI screenshot](docs/assets/summarize-cli.png)

### Install

Requires Node 22+.

- npx (no install):

```bash
npx -y @steipete/summarize "https://example.com"
```

- npm (global):

```bash
npm i -g @steipete/summarize
```

- npm (library / minimal deps):

```bash
npm i @steipete/summarize-core
```

```ts
import { createLinkPreviewClient } from "@steipete/summarize-core/content";
```

- Homebrew (custom tap):

```bash
brew install steipete/tap/summarize
```

Apple Silicon only (arm64).

### CLI vs extension

- **CLI only:** just install via npm/Homebrew and run `summarize ...` (no daemon needed).
- **Chrome/Firefox extension:** install the CLI **and** run `summarize daemon install --token <TOKEN>` so the Side Panel can stream results and use local tools.

> **Extension + YouTube:** The extension fully supports YouTube video summarization. Navigate to any YouTube video and click Summarize — the daemon extracts the transcript server-side (via YouTube web API, yt-dlp, or Whisper) and summarizes it.
>
> **Extension + PDFs:** PDF URLs are detected automatically and routed to the daemon, which downloads and converts them via `markitdown`. Requires `uvx` installed or `UVX_PATH` set in `~/.summarize/daemon.json`. See the screenshot at the top of this README.

### Quickstart

```bash
summarize "https://example.com"
```

### Inputs

URLs or local paths:

```bash
summarize "/path/to/file.pdf" --model google/gemini-3-flash-preview
summarize "https://example.com/report.pdf" --model google/gemini-3-flash-preview
summarize "/path/to/audio.mp3"
summarize "/path/to/video.mp4"
```

Stdin (pipe content using `-`):

```bash
echo "content" | summarize -
pbpaste | summarize -
# binary stdin also works (PDF/image/audio/video bytes)
cat /path/to/file.pdf | summarize -
```

**Notes:**

- Stdin has a 50MB size limit
- The `-` argument tells summarize to read from standard input
- Text stdin is treated as UTF-8 text (whitespace-only input is rejected as empty)
- Binary stdin is preserved as raw bytes and file type is auto-detected when possible
- Useful for piping clipboard content or command output

YouTube (supports `youtube.com` and `youtu.be`):

```bash
summarize "https://youtu.be/dQw4w9WgXcQ" --youtube auto
```

Podcast RSS (transcribes latest enclosure):

```bash
summarize "https://feeds.npr.org/500005/podcast.xml"
```

Apple Podcasts episode page:

```bash
summarize "https://podcasts.apple.com/us/podcast/2424-jelly-roll/id360084272?i=1000740717432"
```

Spotify episode page (best-effort; may fail for exclusives):

```bash
summarize "https://open.spotify.com/episode/5auotqWAXhhKyb9ymCuBJY"
```

### Output length

`--length` controls how much output we ask for (guideline), not a hard cap.

```bash
summarize "https://example.com" --length long
summarize "https://example.com" --length 20k
```

- Presets: `short|medium|long|xl|xxl`
- Character targets: `1500`, `20k`, `20000`
- Optional hard cap: `--max-output-tokens <count>` (e.g. `2000`, `2k`)
  - Provider/model APIs still enforce their own maximum output limits.
  - If omitted, no max token parameter is sent (provider default).
  - Prefer `--length` unless you need a hard cap.
- Short content: when extracted content is shorter than the requested length, the CLI returns the content as-is.
  - Override with `--force-summary` to always run the LLM.
- Minimums: `--length` numeric values must be >= 50 chars; `--max-output-tokens` must be >= 16.
- Preset targets (source of truth: `packages/core/src/prompts/summary-lengths.ts`):
  - short: target ~900 chars (range 600-1,200)
  - medium: target ~1,800 chars (range 1,200-2,500)
  - long: target ~4,200 chars (range 2,500-6,000)
  - xl: target ~9,000 chars (range 6,000-14,000)
  - xxl: target ~17,000 chars (range 14,000-22,000)

### What file types work?

Best effort and provider-dependent. These usually work well:

- `text/*` and common structured text (`.txt`, `.md`, `.json`, `.yaml`, `.xml`, ...)
  - Text-like files are inlined into the prompt for better provider compatibility.
- PDFs: `application/pdf` (provider support varies; Google is the most reliable here)
- Images: `image/jpeg`, `image/png`, `image/webp`, `image/gif`
- Audio/Video: `audio/*`, `video/*` (local audio/video files MP3/WAV/M4A/OGG/FLAC/MP4/MOV/WEBM automatically transcribed, when supported by the model)

Notes:

- If a provider rejects a media type, the CLI fails fast with a friendly message.
- xAI models do not support attaching generic files (like PDFs) via the AI SDK; use Google/OpenAI/Anthropic for those.

### Model ids

Use gateway-style ids: `<provider>/<model>`.

Examples:

- `openai/gpt-5-mini`
- `anthropic/claude-sonnet-4-5`
- `xai/grok-4-fast-non-reasoning`
- `google/gemini-3-flash-preview`
- `zai/glm-4.7`
- `openrouter/openai/gpt-5-mini` (force OpenRouter)

Note: some models/providers do not support streaming or certain file media types. When that happens, the CLI prints a friendly error (or auto-disables streaming for that model when supported by the provider).

### Limits

- Text inputs over 10 MB are rejected before tokenization.
- Text prompts are preflighted against the model input limit (LiteLLM catalog), using a GPT tokenizer.

### Common flags

```bash
summarize <input> [flags]
```

Use `summarize --help` or `summarize help` for the full help text.

- `--model <provider/model>`: which model to use (defaults to `auto`)
- `--model auto`: automatic model selection + fallback (default)
- `--model <name>`: use a config-defined model (see Configuration)
- `--timeout <duration>`: `30s`, `2m`, `5000ms` (default `2m`)
- `--retries <count>`: LLM retry attempts on timeout (default `1`)
- `--length short|medium|long|xl|xxl|s|m|l|<chars>`
- `--language, --lang <language>`: output language (`auto` = match source)
- `--max-output-tokens <count>`: hard cap for LLM output tokens
- `--cli [provider]`: use a CLI provider (`--model cli/<provider>`). Supports `claude`, `gemini`, `codex`, `agent`. If omitted, uses auto selection with CLI enabled.
- `--stream auto|on|off`: stream LLM output (`auto` = TTY only; disabled in `--json` mode)
- `--plain`: keep raw output (no ANSI/OSC Markdown rendering)
- `--no-color`: disable ANSI colors
- `--theme <name>`: CLI theme (`aurora`, `ember`, `moss`, `mono`)
- `--format md|text`: website/file content format (default `text`)
- `--markdown-mode off|auto|llm|readability`: HTML -> Markdown mode (default `readability`)
- `--preprocess off|auto|always`: controls `uvx markitdown` usage (default `auto`)
  - Install `uvx`: `brew install uv` (or https://astral.sh/uv/)
- `--extract`: print extracted content and exit (URLs only; stdin `-` is not supported)
  - Deprecated alias: `--extract-only`
- `--slides`: extrac