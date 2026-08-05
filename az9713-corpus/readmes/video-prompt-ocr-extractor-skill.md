# Video Prompt OCR Extractor

This Codex skill extracts on-screen image generation prompts from videos when the important text is burned into the frame instead of present in the transcript.

It was created as the result of extracting all visible prompt text from the YouTube video ["GPT Image 2 vs Nano Banana 2 (Real Results)"](https://www.youtube.com/watch?v=l284Xo8NOgE). In that project, a transcript-first pass using `/yt-transcript-summary` missed many prompts because the prompts appeared as visual overlays, UI text, comparison labels, and fast montage frames rather than spoken narration.

## Why This Exists

Transcript tools are useful for narration, but they are not enough for videos where the actual prompt is displayed on screen. The original extraction showed several failure modes:

- Prompts flashed during the opening montage for less than a second.
- Some prompts existed only as lower-third overlays.
- Some prompts were inside UI screenshots or generation interfaces.
- Short workflow inputs, such as a single-word prompt, were easy to ignore.
- Prompt text could be partially obscured by picture-in-picture video or motion.
- Transcript summaries captured the topic of the segment but not the exact prompt text.

This skill forces a frame-first workflow: sample the video, inspect contact sheets, crop prompt regions, transcribe cautiously, and reconcile the visual evidence against any transcript-derived candidate list.

## Skill Layout

In this repository, the skill files live at the repository root. When installed inside a project, the same files should live under:

```text
.codex/skills/video-prompt-ocr-extractor/
  DEVELOPMENT_SUMMARY.md
  README.md
  SKILL.md
  agents/
    openai.yaml
  references/
    token-saving-mode.md
  scripts/
    video_prompt_scan.py
```

- `SKILL.md` contains the operational workflow Codex should follow.
- `agents/openai.yaml` provides display metadata and the default invocation prompt.
- `references/token-saving-mode.md` defines the coarse-to-fine extraction pattern that keeps runs from wasting tokens on every frame.
- `scripts/video_prompt_scan.py` builds sampled-frame contact sheets and enlarged evidence crops from a video file.
- `DEVELOPMENT_SUMMARY.md` records the source extraction process and lessons learned.

## When To Use It

Use this skill for requests like:

- "Extract every prompt shown in this video."
- "The YouTube transcript missed the prompts on screen."
- "OCR the image generation prompts from this video."
- "Use this screenshot as an example and recover the rest of the prompts."
- "Find all UI prompt text, lower-third prompts, or visual prompt overlays."

Do not use it as a general transcript summarizer. It is designed for visual prompt recovery.

## Requirements

The workflow works best with:

- `ffmpeg` and `ffprobe` available on PATH.
- `yt-dlp` for downloading a local copy of YouTube videos when the user has not provided one.
- Python 3.
- Pillow, used by `video_prompt_scan.py` for contact sheets.

Install Pillow if needed:

```powershell
python -m pip install pillow
```

## Basic Invocation

In Codex:

```text
Use $video-prompt-ocr-extractor to extract every on-screen image generation prompt from this YouTube video: <video URL>
```

The skill should produce a timestamped Markdown prompt inventory, with uncertainty notes and evidence folders kept beside the working files.

## Typical Workflow

Before running the workflow, apply `references/token-saving-mode.md`: start from likely prompt-heavy regions, generate contact sheets, crop only candidate prompt text, and keep evidence on disk rather than embedding large image batches in chat.

### 1. Download or locate the video

Prefer an existing local video file. If needed, download a manageable 720p copy:

```powershell
yt-dlp -f "bv*[height<=720]+ba/b[height<=720]/best[height<=720]" --merge-output-format mp4 --write-info-json --no-playlist -o "source_video.%(ext)s" "<youtube-url>"
```

Verify duration and streams:

```powershell
ffprobe -v error -show_entries format=duration -show_streams -of compact=p=0:nk=1 "source_video.mp4"
```

### 2. Build contact sheets

Sample the likely prompt region across the video:

```powershell
python .\.codex\skills\video-prompt-ocr-extractor\scripts\video_prompt_scan.py --video .\source_video.mp4 --out-dir .\video_prompt_scan --start 00:00:00 --end 00:03:35 --fps 1
```

For longer comparison sections, scan the main body separately:

```powershell
python .\.codex\skills\video-prompt-ocr-extractor\scripts\video_prompt_scan.py --video .\source_video.mp4 --out-dir .\video_prompt_scan_main --start 00:03:35 --end 00:15:20 --fps 1
```

### 3. Crop prompt regions

Use enlarged crops when text is small or fast-moving:

```powershell
python .\.codex\skills\video-prompt-ocr-extractor\scripts\video_prompt_scan.py --video .\source_video.mp4 --out-dir .\prompt_crops --crop-times "00:00:27,00:00:33,00:03:54" --crop-rect "0:490:1280:230" --crop-scale 2 --exact-crop
```

`--crop-rect` uses `x:y:w:h`. Common prompt regions for a 1280x720 video are:

- Lower-third prompt band: `0:490:1280:230`
- Larger comparison panel: `0:420:1280:300`
- Screenshot-like bottom band: `0:500:1280:220`

Adjust the crop after inspecting frames.

### 4. Transcribe and reconcile

For each prompt:

- Record the timestamp.
- Transcribe the visible text as shown.
- Preserve quotes and prompt-specific formatting instructions.
- Mark uncertain words explicitly.
- Keep repeated prompts when they appear in distinct examples.
- Use narration only to locate or disambiguate, not to invent missing words.

Then compare the visual list against existing transcript-derived notes:

```powershell
rg -n "Prompt|Generate|photorealistic|image|@Image" .
```

The final artifact should clearly separate confirmed visible prompts from uncertain or inferred text.

## Expected Output

A strong extraction produces:

- A Markdown inventory of all visible prompts.
- Timestamps for each prompt.
- Evidence folders containing contact sheets and crops.
- A note about what transcript-first extraction missed.
- A count of recovered prompt entries.
- An uncertainty section for ambiguous crops.

## Lesson From The Source Project

The source video project recovered many prompts only after moving beyond transcript analysis. The durable lesson is simple: when a video demonstrates image generation, the prompt is often a visual object, not a spoken sentence. A reliable extractor must inspect frames, not just captions.
