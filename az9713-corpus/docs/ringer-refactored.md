---
repo: ringer-refactored
description: Static one-page refactor of Nate B. Jones's Ringer guide with visible prompt tabs and related video/Substack context.
language: HTML
stars: 1
forks: 0
created: 2026-07-08
updated: 2026-07-26
topics: 
is_fork: False
kb: 505
---

# ringer-refactored
# Ringer Refactored

This repository contains a clean one-page HTML refactor of Nate B. Jones's Ringer guide:

- Original guide: [Ringer - swarm power without the frontier bill](https://unlock-ai.natebjones.com/guides/ringer)
- Live page: [GitHub Pages](https://az9713.github.io/ringer-refactored/)
- Refactored page: [ringer_one_page_tabs.html](./ringer_one_page_tabs.html)

The goal of the refactor was to turn the saved guide into a readable static package with no hidden prompt payloads. The original guide is a Next.js page with rendered content plus hydration data. This version keeps the useful guide content and prompt sequence visible in normal HTML.

## What Changed

- Rebuilt the guide as a static one-page HTML file.
- Added an index tab that explains the whole package before readers enter the step-by-step prompt sequence.
- Turned each major guide section into a tab-style navigation target:
  - Quickstart
  - Manifests
  - Cross-model worker lanes
  - Ringside
  - The eval loop
  - Field notes
  - Get Ringer
- Preserved the seven visible prompt blocks as ordinary code blocks.
- Removed the Next.js hydration payload and duplicated framework script data.
- Kept only the image assets required by the refactored page.

## Why This Exists

Ringer is a practical pattern for running multi-agent swarms without spending frontier-model prices on every worker. The guide's core idea is simple: put the expensive model in the judgment seat, send implementation work to cheaper worker lanes, and verify every result with executable checks.

This refactor makes that prompt package easier to inspect, copy, and share as a single static HTML file.

## Related Video And Essay

Readers should watch the related YouTube video:

[20 AI Agents Rebuilt My Wife's Website For $8. I Never Typed a Word.](https://www.youtube.com/watch?v=suY66oTDn0s)

And read the related Substack essay:

[Your agents will fabricate something this week. A one-penny audit can catch it before the work ever reaches you.](https://natesnewsletter.substack.com/p/trust-ai-agents)

Together, the video, essay, and Ringer guide explain the same operating model: hallucination is not solved by trusting agents harder. It is handled by building institutions around them: org charts, executable audits, constitutions, and appeals.

## Files

- `index.html` - the live GitHub Pages entrypoint for the refactored one-page static guide.
- `ringer_one_page_tabs.html` - the same static guide retained as a named local artifact.
- `assets/` - the PNG images used by the static page.

Local source captures such as transcripts, Substack exports, and the original saved browser snapshot are intentionally not part of the publishable package.


