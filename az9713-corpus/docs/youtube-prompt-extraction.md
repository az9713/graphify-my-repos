---
repo: youtube-prompt-extraction
description: Extract image-generation prompts from YouTube videos using yt-dlp, FFmpeg, and EasyOCR. Outputs a timestamped Markdown table of every detected prompt.
language: Python
stars: 0
forks: 0
created: 2026-04-24
updated: 2026-04-24
topics: 
is_fork: False
kb: 31
---

# youtube-prompt-extraction
# youtube-prompt-extraction

A Python script that extracts image-generation prompts from YouTube videos. It downloads the video, pulls one frame per second, reads the bottom portion of each frame with OCR, and outputs a timestamped Markdown table of every distinct prompt it finds.

## How it works

```
YouTube URL → yt-dlp (download) → FFmpeg (1fps frames) → EasyOCR (bottom 25%) → prompts.md
```

## Requirements

- Python 3.10+
- [yt-dlp](https://github.com/yt-dlp/yt-dlp)
- [FFmpeg](https://ffmpeg.org/) (system binary)
- Python packages: `easyocr`, `pillow`, `numpy`

Install Python packages:

```bash
pip install yt-dlp easyocr pillow numpy
```

## Usage

1. Set `VIDEO_URL` in `extract_prompts.py` to your target YouTube video.
2. Run:

```bash
python extract_prompts.py
```

3. Open `prompts.md` — a timestamped table of all detected prompts.

**First run** downloads the EasyOCR English model (~100 MB). Subsequent runs skip the download. The video and frames are cached so re-running only re-runs OCR if you change settings.

## Example run

This script was used to extract prompts from [**GPT Image 2 Is Here — Everything You NEED to Know**](https://www.youtube.com/watch?v=blOlUnC75O4) by [ElevenLabs](https://www.youtube.com/@elevenlabs) — **130 prompts** extracted from a 4-minute video. Results are in [`prompts.md`](prompts.md).

## Output example

| Timestamp | Prompt |
|-----------|--------|
| 0:55 | Underwater shot of a great white shark silhouette against sunlit ocean surface, deep blue, cinematic. |
| 1:35 | A red cube on a blue sphere inside a pyramid with green light from the left casting a cyan shadow. |
| 2:00 | A face fragmented across broken mirror shards mid-fall, each shard reflecting a different angle of expression... |

## Configuration

Edit these constants at the top of `extract_prompts.py`:

| Constant | Default | Description |
|----------|---------|-------------|
| `VIDEO_URL` | ElevenLabs GPT Image 2 video | YouTube URL to process |
| `CROP_BOTTOM_PCT` | `0.25` | Fraction of frame height to analyse (bottom 25%) |
| `CONFIDENCE_THRESHOLD` | `0.4` | Minimum OCR confidence to include a detection |
| `OUTPUT_PATH` | `prompts.md` | Output file path |

See [docs/reference/configuration.md](docs/reference/configuration.md) for full details.

## Docs

| Doc | What's inside |
|-----|--------------|
| [Prerequisites](docs/getting-started/prerequisites.md) | Required tools with verify commands |
| [Quickstart](docs/getting-started/quickstart.md) | Step-by-step first run |
| [Configuration](docs/reference/configuration.md) | All tunable constants |
| [Output format](docs/reference/output-format.md) | What `prompts.md` contains |
| [Adapt for a different video](docs/guides/adapt-for-different-video.md) | Swap URLs and re-run |
| [Improve OCR accuracy](docs/guides/improve-ocr-accuracy.md) | Tune crop and confidence |
| [Troubleshooting](docs/troubleshooting/common-issues.md) | Fixes for common failures |

## Known limitations

- **OCR artefacts** — EasyOCR occasionally misreads characters (e.g., `@` for `a`, `;` for `,`). Output is raw and not post-processed.
- **UI chrome** — If the video's interface overlaps the crop zone, interface text may appear in results.
- **Deduplication** — Uses exact string match. Minor OCR variation across frames can produce near-duplicate entries for long prompts.
- **CPU speed** — ~2–5 seconds per frame on CPU. A 4-minute video takes roughly 10–15 minutes without a GPU.
