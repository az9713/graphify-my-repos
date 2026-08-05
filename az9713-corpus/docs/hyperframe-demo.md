---
repo: hyperframe-demo
description: One-shot HyperFrames video generation from a research paper using Claude Code
language: HTML
stars: 0
forks: 0
created: 2026-05-03
updated: 2026-05-03
topics: 
is_fork: False
kb: 7638
---

# hyperframe-demo
# HyperFrames Demo

Two one-shot demos of [HyperFrames](https://github.com/heygen-com/hyperframes) generating videos from a single prompt using Claude Code as the authoring agent — no manual HTML editing, no keyframing.

---

## Demo 1 — Research Paper Explainer (Verkor)

## The Prompt

> use hyperframes to create a 15 second video for the paper https://arxiv.org/pdf/2603.08716

That's the complete prompt. Claude Code read the PDF, designed the composition, wrote the HTML, fixed lint warnings, and rendered the MP4 — no manual editing.

## The Paper

**"Design Conductor: An agent autonomously builds a 1.5 GHz Linux-capable RISC-V CPU"**  
Ravi Krishna, Suresh Krishna, David Chin — The Verkor Team  
arXiv:2603.08716v1 · March 2026

Design Conductor (DC) is an autonomous AI agent that built a complete RISC-V CPU ("VerCore") in 12 hours from a 219-word requirements document — the first autonomous agent to go from spec to tape-out ready GDSII layout.

## The Output

<video src="https://github.com/user-attachments/assets/ec37a9ec-d6e1-4dd0-b987-9e239ecb09de" controls width="100%"></video>

| Property | Value |
|---|---|
| Duration | 15 seconds |
| Resolution | 1920 × 1080 |
| Frame rate | 30 fps |
| File size | 991 KB |
| Render time | 36s |

### Scene breakdown

| Time | Scene | Content |
|---|---|---|
| 0–4.5s | Hook | "AI Built a CPU." — big title, "In 12 hours. From a 219-word spec." |
| 4.5–9s | What | "Spec → Silicon. End-to-End." — what Design Conductor is |
| 9–13.5s | Stats | 4-card grid: 1.48 GHz · 3261 CoreMark · 7nm · 12h build time |
| 13.5–15s | Outro | "Chip Design. Reinvented." — fade to black |

## How It Was Made

### 1. Install HyperFrames skills

```bash
npx skills add heygen-com/hyperframes
```

This installs 12 skills into `.claude/skills/` (symlinked from `.agents/skills/`) that teach Claude Code how to write correct HyperFrames compositions, GSAP timelines, and transitions.

### 2. One-shot prompt

```
use hyperframes to create a 15 second video for the paper https://arxiv.org/pdf/2603.08716
```

Claude Code:
1. Read the 13-page PDF with PyMuPDF
2. Extracted key facts: 12h build, 1.48 GHz, 3261 CoreMark, 219-word input, first spec→GDSII agent
3. Designed a 4-scene narrative arc with fade-to-black transitions
4. Wrote `verkor/index.html` — a standalone HyperFrames composition using GSAP 3 for animation
5. Fixed all lint warnings (missing `class="clip"`, `data-start="0"` on root, tween boundary overlaps, hard-kill sets)
6. Rendered to MP4

### 3. Render

```bash
cd verkor
npx hyperframes render
# → renders/verkor_2026-05-03_07-17-02.mp4
```

## Design Choices

- **Palette:** Dark premium — `#07070f` background, `#00d4ff` cyan (circuit traces), `#7c3aed` purple (AI), `#ff6b35` orange (numbers)
- **Font:** Space Grotesk (auto-fetched and embedded by the HyperFrames compiler)
- **Transitions:** Fade-to-black overlays on separate tracks between each scene
- **Animation:** GSAP `from()` entrances only; no exit animations except the final scene fade

## Files

```
verkor/
├── index.html                              # HyperFrames composition source
└── renders/
    └── verkor_2026-05-03_07-17-02.mp4     # Rendered output (991 KB)
```

---

## Demo 2 — Bar Chart Race (Programming Language Popularity)

### The Prompt

```
use hyperframes to create a bar chart race video from lang-popularity/data.csv showing programming language popularity 2016–2024
```

### The Output

<video src="https://github.com/user-attachments/assets/4f2e02ea-6e2d-40f7-9a61-82785c93e918" controls width="100%"></video>

| Property | Value |
|---|---|
| Duration | 22.5 seconds |
| Resolution | 1920 × 1080 |
| Frame rate | 30 fps |
| File size | 2.1 MB |
| Render time | 43.8s |

### What it shows

8 languages race from 2016 to 2024, sourced from the Stack Overflow Developer Survey. Key moments:
- **2018** — JavaScript hits its all-time peak (71.5%), Java briefly surges to 45.4%
- **2019–2020** — Python overtakes Java, claims 2nd place
- **2021–2022** — TypeScript overtakes Java (a notable rank swap mid-animation)
- **2023–2024** — Rust rockets from near-zero to within reach of Go; Python approaches 51%

### How it was made

Claude Code generated a [72-row CSV](lang-popularity/data.csv) from Stack Overflow survey research, then wrote a HyperFrames composition that:
- Reads all data embedded in JS (no runtime fetch)
- Animates bar `width` and row `y` (rank) simultaneously via GSAP `power1.inOut`
- Updates value text deterministically using `tl.set(attr)` + CSS `content: attr(data-val)` — no `onUpdate` callbacks
- Flashes the year badge on each year change via `fromTo` with explicit start/end state

```bash
cd lang-popularity
npx hyperframes preview   # live in browser with scrub timeline
npx hyperframes render    # → renders/lang-popularity_2026-05-03_12-10-59.mp4
```

### Files

```
lang-popularity/
├── data.csv                                              # Source data (8 languages × 9 years)
├── index.html                                            # HyperFrames composition source
└── renders/
    └── lang-popularity_2026-05-03_12-10-59.mp4          # Rendered output (2.1 MB)
```

---

## Demo 3 — GitHub Repo State of the Project (hermes-agent)

### The Prompt

```
Using hyperframes, create a 30-second "state of the project" video for
https://github.com/nousresearch/hermes-agent with data pulled from the GitHub API
```

### The Output

<video src="https://github.com/user-attachments/assets/799e809f-6b80-47c9-b805-265ab33e43c7" controls width="100%"></video>

| Property | Value |
|---|---|
| Duration | 30 seconds |
| Resolution | 1920 × 1080 |
| Frame rate | 30 fps |
| File size | 2.7 MB |
| Render time | 56s |

### What it shows

4 scenes built entirely from GitHub API data — no assets, no design files:

1. **Title card** — repo name, tagline, stars (130,984) / forks (19,829) / open issues (8,073)
2. **Commit activity** — 10 monthly bars (Aug 2025–May 2026) growing from a baseline, April peak highlighted
3. **Top contributors** — 7 horizontal bars; teknium1 dominates with 3,804 commits (55% of all commits)
4. **Outro** — 6,984 commits · 130K stars · 9.5 months · "still growing."

### How it was made

Claude Code queried the GitHub API (`/contributors`, `/commits`, `/repos`) then wrote a HyperFrames composition with all data embedded in JS — no runtime fetches. Key techniques:
- Bottom-anchored bars (`bottom: 300px; height: 0`) grow upward via GSAP `height` animation
- Contributor bars use `overflow: hidden` wrapper + animated `width` (same pattern as the bar chart race)
- Orange accent palette derived from Nous Research's brand color

```bash
cd hermes-agent
npx hyperframes preview   # live in browser
npx hyperframes render    # → renders/hermes-agent_2026-05-03_13-36-56.mp4
```

### Files

```
hermes-agent/
├── index.html                                          # HyperFrames composition source
└── renders/
    └── hermes-agent_2026-05-03_13-36-56.mp4           # Rendered output (2.7 MB)
```

---

## Demo 4 — Website → Social Ad (Anthropic)

### The Prompt

```
Use website-to-hyperframes on anthropic.com and turn it into a 15-second social ad
```

### The Output

<video src="https://github.com/user-attachments/assets/65e7454f-ec27-4049-b57a-dd60b7f3646b" controls width="100%"></video>

| Property | Value |
|---|---|
| Duration | 16 seconds |
| Resolution | 1920 × 1080 |
| Frame rate | 30 fps |
| File size | 1.8 MB |
| Render time | 31.7s |

### What it shows

4 scenes built entirely from live content fetched from anthropic.com — no design files, no brand kit, no assets:

1. **Hook** — "Safety at the frontier." + "AI research and products for humanity's long-term well-being."
2. **400m on Mars** — The NASA/Perseverance story from the homepage, recomposed as a giant stat with context
3. **Claude family** — Product lineup (Code · Security · Enterprise · Max) + model row (Opus · Sonnet · Haiku · Mythos)
4. **CTA** — "Build AI that lasts." + anthropic.com

### How it was made

Claude Code fetched anthropic.com, extracted headlines, the NASA quote, product names, and brand tone, then wrote the composition from scratch. Key decisions inferred from the page:
- Palette: warm dark `#0d0c0b` + cream `#f0ebe0` + terracotta `#c8643a` (matching Anthropic's dark aesthetic)
- The 400m Mars fact was the most striking content on the page — made it the centerpiece of Scene 2 at 290px font
- No screenshots, no assets — pure text-to-video from the page's HTML content

```bash
cd anthropic-ad
npx hyperframes preview   # live in browser
npx hyperframes render    # → renders/anthropic-ad_2026-05-03_14-24-46.mp4
```

### Files

```
anthropic-ad/
├── index.html                                        # HyperFrames composition source
└── renders/
    └── anthropic-ad_2026-05-03_14-24-46.mp4         # Rendered output (1.8 MB)
```

---

## Requirements

- Node.js ≥ 22
- FFmpeg on PATH
- Chrome (for headless rendering)
