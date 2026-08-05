---
repo: autonomous-video-creation
description: An AI agent autonomously remade a 250th-anniversary film on ElevenLabs: 8 human messages, ~200 autonomous actions. Film + pipeline + full docs + development chronicle.
language: Shell
stars: 0
forks: 0
created: 2026-07-21
updated: 2026-07-21
topics: 
is_fork: False
kb: 221539
---

# autonomous-video-creation
# Autonomous Video Creation

A complete remake of [*A Shining City: 1776–2026*](https://github.com/az9713/a-shining-city-1776-2026), produced end-to-end on ElevenLabs' Image & Video platform by an autonomous AI agent (Claude Fable 5) — 8 human messages, ~200 autonomous actions, one overnight session.

**▶ The film:** [`usa250_elevenlabs_1080p.mp4`](usa250_elevenlabs_1080p.mp4) (1080p master) · [`usa250_elevenlabs_preview720.mp4`](usa250_elevenlabs_preview720.mp4) (14 MB share copy)

## Start here

| | |
|---|---|
| [The development journey](DEVELOPMENT.md) | The full chronicle: every decision fork, tool, failure, and cost — the showcase of long-running autonomous task completion |
| [Documentation](docs/index.md) | Complete docs for developers (rebuild, regenerate, verify) and viewers (watching guide, FAQ) |
| [Quickstart](docs/getting-started/quickstart.md) | Rebuild the film from the clips in this repo in ~10 minutes |

## The one-paragraph version

Ten AI-generated shots (Nano Banana 2 stills → Veo 3.1 Fast clips at 1080p, one Runway Gen-4.5 fallback after a content-filter rejection), captioned and crossfaded by an ffmpeg pipeline ([`build.sh`](build.sh)), closed by the real America250 banner and The Star-Spangled Banner (US Air Force Band, public domain) — both inherited from the 2025 original. Total cost: ~41,000 ElevenLabs credits. Generation ran through browser automation because the platform has no public video API; the whole story is in [DEVELOPMENT.md](DEVELOPMENT.md).

## Repo contents

| Path | What |
|---|---|
| `usa250_elevenlabs_1080p.mp4` | The film (71.7 s master) |
| `DEVELOPMENT.md` | The build chronicle |
| `docs/` | Full documentation set (developer + user) |
| `build.sh` | The assembly pipeline: captions, end card, xfade chain, anthem |
| `clips/` | The 10 generated source clips, named by shot |
| `caps/` | Caption text per shot |
| `flag-still.png` | The machine-verified 13-star Betsy Ross still |

Requires the [original repo](https://github.com/az9713/a-shining-city-1776-2026) as a sibling checkout to rebuild (anthem + end card source) — see [prerequisites](docs/getting-started/prerequisites.md).
