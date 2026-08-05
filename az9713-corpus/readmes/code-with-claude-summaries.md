# Claude Workflow Playlist Summaries

Description: Transcript-grounded Claude workflow summaries, playbooks, and meta-patterns from Code with Claude London 2026.

## Source Playlists

- Code with Claude London 2026 Playlist #1: https://www.youtube.com/playlist?list=PLmWCw1CzcFilPJdvw6scjHjbBripZWFps
- Code with Claude London 2026 Playlist #2: https://www.youtube.com/watch?v=qOjleN2-50c&list=PLmWCw1CzcFinm44PAkEoR2glf-iNPhulP
- Extra videos (unlisted or added after playlist snapshot): `docs/sources.md`

It seems that Anthropic either deleted one playlist or merged the two into one. After these summaries were created, it was noticed that only one Code With Claude London 2026 playlist can be found in YouTube with only 24 videos. Five additional videos were later identified in `docs/sources.md` and added as items 32–36.

## What Is In This Repository

- `markdown_summaries/README.md`: master index for all video reports.
- `markdown_summaries/00_cross_playlist_claude_workflow_playbook.md`: cross-playlist Claude workflow synthesis.
- `markdown_summaries/01_*.md` through `36_*.md`: one hand-written, transcript-grounded report per video.
- `CLAUDE_WORKFLOW_META_PATTERNS.md`: cross-profession Claude workflow meta-patterns, reusable templates, prompt patterns, and source back-links synthesized from the summaries. Covers 12 meta-patterns.
- `METHODOLOGY.md`: how the summaries were produced, including the pipeline limitations and the manual rewrite process.
- `video_sources/<video_id>/transcript.clean.txt`: cleaned transcript used as the primary source for each report.
- `transcript_manifest.json`: processing manifest with video metadata, source basis, status, relevance, and detected workflow concepts.
- `source_snapshots/anthropic_docs/README.md`: official Claude documentation references used for best-practice gap filling.
- `build_claude_workflow_summaries.py`: pipeline for playlist expansion, transcript acquisition, cleaning, and manifest generation. Generates template-based initial draft reports; see METHODOLOGY.md for why those drafts were replaced.
- `process_extra_videos.py`: processes individual video URLs not in the original playlists (used for the 5 extra videos in `docs/sources.md`).
- `transcribe_blocked_videos.py`: local Whisper fallback for videos without YouTube captions.

## Source Grounding

Every report is a hand-written, transcript-grounded summary. The pipeline (`build_claude_workflow_summaries.py`) handles transcript acquisition, cleaning, and manifest generation, but its auto-generated reports used identical template paragraphs regardless of what the speaker actually said. All 36 reports were fully rewritten by reading each cleaned transcript directly and extracting the speaker's actual arguments, demos, workflows, and recommendations.

The cleaned transcript is the primary source for each report. Official Claude documentation is used only to clarify terminology. Speaker names, company names, product names, and metrics are taken from the transcript; uncertain proper nouns (common with Whisper transcription) are flagged with `(?)` in the affected reports.

Current verification state:

- 36 videos processed.
- 36 cleaned transcripts generated.
- 36 per-video markdown summaries hand-written from transcripts.
- 0 blockers.
- Source basis: 19 YouTube caption transcripts, 17 local Whisper `base.en` transcripts.

## Git Scope

This repository intentionally excludes bulky raw artifacts such as downloaded audio, raw VTT captions, raw YouTube logs, Python caches, and full saved HTML pages. The GitHub-ready source of truth is the cleaned transcript set, generated markdown reports, manifest, scripts, and documentation reference index.
