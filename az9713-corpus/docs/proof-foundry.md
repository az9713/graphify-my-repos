---
repo: proof-foundry
description: An adversarially-verified compendium: 8 Putnam proofs + 8 open Erdős surveys, built by a 110-agent fleet (Fable conducted, Opus solved/verified, Sonnet typeset).
language: HTML
stars: 0
forks: 0
created: 2026-07-22
updated: 2026-07-28
topics: claude, erdos, mathematics, multi-agent, putnam
is_fork: False
kb: 601
---

# proof-foundry
# The Proof Foundry

**▶ Live compendium: https://az9713.github.io/proof-foundry/**

A two-wave, 113-agent adversarial mathematics workflow: 8 Putnam problems proved
(panel-verified), 8 open Erdős conjectures surveyed, 3 deep dives. Fable conducted;
Opus solved and verified; Sonnet curated and typeset.

[![The Proof Foundry — click to open the live compendium](docs/preview.jpg)](https://az9713.github.io/proof-foundry/)

*↑ Click the screenshot to open the live compendium.*

## Contents

- **[`index.html`](index.html)** — the compendium (single self-contained HTML, 19 sections). Rendered live at the link above.
- **[`proof-foundry-agent-report.md`](proof-foundry-agent-report.md)** — orchestration postmortem: per-problem agent breakdown, sizing rationale, roles, and 9 lessons learned.

## The build

~8.1M subagent tokens across two waves. Wave 1 solved and verified; wave 2 added
three deep dives (the minimum-overlap deep dive ships **unverified with objections
printed** — by design). See the report for the full account.
