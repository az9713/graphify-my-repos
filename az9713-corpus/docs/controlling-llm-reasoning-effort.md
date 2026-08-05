---
repo: controlling-llm-reasoning-effort
description: Technical atlas of how LLMs learn and expose reasoning-effort controls, based on Sebastian Raschka's article.
language: HTML
stars: 0
forks: 0
created: 2026-07-18
updated: 2026-07-18
topics: 
is_fork: False
kb: 16
---

# controlling-llm-reasoning-effort
# Controlling LLM Reasoning Effort

An offline, source-grounded technical atlas explaining how modern large language models learn and expose low-, medium-, and high-effort reasoning modes.

## Live site

[Open the GitHub Pages atlas](https://az9713.github.io/controlling-llm-reasoning-effort/)

## Original article

This project is an independent technical synthesis of Sebastian Raschka's article:

[Controlling Reasoning Effort in LLMs](https://magazine.sebastianraschka.com/p/controlling-reasoning-effort-in-llms)

The article is the primary source and should be read for the author's complete argument, figures, context, and current wording.

## What the atlas covers

- The distinction between learned reasoning-effort policies and hard inference-time token budgets
- Training scaling versus inference scaling
- Effort-conditioned supervised fine-tuning and reinforcement learning
- Reasoning controls in DeepSeek V4, Nemotron 3 Ultra, Kimi K2.5, GLM-5, Qwen3, and Inkling
- Quantitative details, literal control signals, disclosure gaps, and epistemic labels
- Engineering decision rules and falsifiable research questions

## Evidence boundary

The atlas was derived from a locally saved copy of the original article. It separates mechanisms documented in the source from the author's inferences and from additional synthesis. Linked technical reports, APIs, and benchmarks were not independently verified for this version.

The local saved webpage contained unrelated account and session metadata in embedded scripts. Those scripts and metadata are not included in this repository.

## Repository contents

- [`index.html`](./index.html) — the complete single-file technical atlas
- `README.md` — project context, attribution, and evidence limitations

The site has no build step, JavaScript, remote fonts, trackers, or external runtime dependencies. Open `index.html` directly or serve the repository as a static site.

## Attribution

The original article and its figures are the work of Sebastian Raschka and their respective publisher or rights holders. This repository contains a transformed analytical summary and does not reproduce the original article or its image collection.
