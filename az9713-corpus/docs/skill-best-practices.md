---
repo: skill-best-practices
description: Go-to reference for Claude Code Agent Skills: best practices, 27 reference skills, and a skill-creator eval walkthrough. Built from Thariq's 'How We Use Skills'.
language: Python
stars: 0
forks: 0
created: 2026-06-24
updated: 2026-06-24
topics: 
is_fork: False
kb: 229
---

# skill-best-practices
# skill-best-practices

A go-to reference for building **Claude Code Agent Skills**, reverse-engineered from Anthropic's own
playbook.

It bundles three things:

1. **[`SKILLS_BEST_PRACTICES.md`](./SKILLS_BEST_PRACTICES.md)** — the best practices for writing skills,
   distilled from the source post, with a completeness audit.
2. **27 reference skills** in [`.claude/skills/`](./.claude/skills/) — one for every example in the
   post, built as real folders (scripts, references, assets, hooks, config), not just markdown.
3. **An under-the-hood look at `skill-creator`** — a real eval run on `billing-lib` (with-skill vs
   baseline) and a description-optimization pass, written up in
   **[`DEVELOPMENT_JOURNEY.md`](./DEVELOPMENT_JOURNEY.md)**.

## Contents

| Path | What it is |
|---|---|
| [`SKILLS_BEST_PRACTICES.md`](./SKILLS_BEST_PRACTICES.md) | The 17 best practices + completeness audit |
| [`SKILLS_DOCUMENTATION.md`](./SKILLS_DOCUMENTATION.md) | Full catalog of all 27 skills |
| [`DEVELOPMENT_JOURNEY.md`](./DEVELOPMENT_JOURNEY.md) | How the repo was built and why |
| [`.claude/skills/`](./.claude/skills/) | The 27 reference skills |
| `.claude/skills/billing-lib-workspace/` | The eval run: `benchmark.md`, `review.html` |
| `.claude/skills/_desc-opt/` | Trigger eval sets for description optimization |

## The 9 skill categories

Library & API Reference · Product Verification · Data Fetching & Analysis · Business Process &
Team Automation · Code Scaffolding & Templates · Code Quality & Review · CI/CD & Deployment ·
Runbooks · Infrastructure Operations.

## Attribution

Built from Thariq's (@trq212) post **"Lessons from Building Claude Code: How We Use Skills"**:
https://x.com/trq212/status/2033949937936085378

All credit for the original skill taxonomy and best practices belongs to Thariq and the Claude Code
team at Anthropic. This repository is an independent study that applies those ideas to a worked set of
example skills. The example skills target fictional internal systems and are for reference only.
