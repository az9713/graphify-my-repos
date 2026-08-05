---
repo: html-effectiveness-demo
description: Self-contained HTML artifacts for learning HTML effectiveness
language: HTML
stars: 0
forks: 0
created: 2026-05-11
updated: 2026-05-11
topics: 
is_fork: False
kb: 627
---

# html-effectiveness-demo
# HTML Effectiveness Demo

This repository uses Thariq's principle of the "Unreasonable Effectiveness of HTML" to explain the broader "effectiveness of HTML": use self-contained HTML artifacts when a human needs to understand, compare, decide, tune, present, or export something back into an AI agent.

The main entry point is:

- [`html_effectiveness_onboarding/00-index.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/00-index.html)

Each artifact is a plain `.html` file with inline CSS and JavaScript. There is no build step. Open the files directly in a browser.

## What Was Created

- [`00-index.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/00-index.html) - curriculum map and operating rule.
- [`01-effective-html-principles.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/01-effective-html-principles.html) - when HTML beats Markdown and when it does not.
- [`02-decision-comparison.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/02-decision-comparison.html) - side-by-side decision artifact with filters and copyable decision text.
- [`03-code-review-map.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/03-code-review-map.html) - annotated diff, reviewer focus list, and SVG module map.
- [`04-prototype-playground.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/04-prototype-playground.html) - interactive checkout-button playground with sliders and copyable CSS.
- [`05-report-timeline.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/05-report-timeline.html) - incident/status report with root-cause callout, metrics, timeline, chart, and checklist.
- [`06-export-editor.html`](https://az9713.github.io/html-effectiveness-demo/html_effectiveness_onboarding/06-export-editor.html) - custom editor that turns choices into a clean agent prompt.
- `verify_html_pack.mjs` - Playwright smoke test for rendering, links, and basic interactions.

## Source Links

These are the sources from `sources.txt`:

- Thariq X post: https://x.com/trq212/status/2052809885763747935
- Thariq playground X post: https://x.com/trq212/status/2017024445244924382
- Thariq HTML effectiveness gallery: https://thariqs.github.io/html-effectiveness/
- AI Coding Daily YouTube video: https://www.youtube.com/watch?v=jiEdmQDE8h4
- Jay E YouTube video: https://www.youtube.com/watch?v=BZzmBRYC_4s
- Visual Explainer GitHub repo: https://github.com/nicobailon/visual-explainer

Local transcript files used:

- `transcript_ai_coding_daily.txt`
- `transcript_jay_E.txt`

## How The Artifacts Were Created

1. Read the local transcripts and `sources.txt`.
2. Opened the public HTML effectiveness gallery to understand the artifact categories:
   - exploration and planning
   - code review and understanding
   - design
   - prototyping
   - diagrams
   - decks
   - research and learning
   - reports
   - custom editors
3. Extracted the practical thesis from the sources:
   - Markdown is still good for short, durable, version-controlled prose.
   - HTML is more effective when the output needs layout, visual emphasis, diagrams, controls, side-by-side comparison, or export buttons.
   - The relevant efficiency is not just token efficiency. It is decision efficiency: a higher chance that the human reads carefully and chooses well.
4. Designed a six-page onboarding sequence that teaches the concept by using the concept.
5. Built each page as a standalone HTML file with inline CSS and JavaScript so the artifacts can be opened directly from disk or GitHub Pages.
6. Added a Playwright smoke test to verify that every page renders and that the interactive examples still work.

## Verification

The local smoke test checks:

- every HTML file loads
- every page has the expected title and `h1`
- local HTML links resolve
- no browser page errors or console errors are thrown
- the decision-filter interaction works
- the prototype playground slider updates generated CSS
- the export editor updates the generated prompt

Run it with Playwright available:

```bash
node html_effectiveness_onboarding/verify_html_pack.mjs
```

In the original Codex desktop environment, the test was run with the bundled Playwright runtime and passed.

## Core Pattern

Ask an agent for a self-contained HTML artifact when you want it to make information easier to act on:

```text
Create a self-contained HTML artifact for this decision.
Include side-by-side options, realistic examples, diagrams or tables where useful,
interactive controls if they help, and a copyable export block I can paste back
into the agent.
```

The artifact should not merely look nicer. It should reduce the chance of skimming, missed tradeoffs, and weak decisions.
