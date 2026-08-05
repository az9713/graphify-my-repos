---
repo: vercel-eve-tutorial
description: Clone of vercel/eve with a 10-part tutorial by Fable-5: agent-harness deep dive, critique, roadmap, and competitive analysis vs Claude Code, Codex, and Grok Build
language: TypeScript
stars: 0
forks: 0
created: 2026-07-16
updated: 2026-07-16
topics: 
is_fork: False
kb: 4415
---

# vercel-eve-tutorial
# vercel-eve-tutorial

A clone of [vercel/eve](https://github.com/vercel/eve) — Vercel's filesystem-first framework for durable AI agents — enhanced with a tutorial documentation set created by **Fable-5** (Anthropic's Claude Fable 5, via Claude Code).

## What's here

| Path | Contents |
|---|---|
| [`eve/`](eve/) | The upstream repo, cloned at commit [`5f8818b`](https://github.com/vercel/eve/commit/5f8818b42aa7b094ea8f341df5a8e57d43d01272) (2026-07-16). All credit and license (Apache-2.0) belong to Vercel — see [`eve/LICENSE`](eve/LICENSE). Its own published docs live in [`eve/docs/`](eve/docs/). |
| [`docs/`](docs/) | **The tutorial set** — 10 analysis documents written by Fable-5 from a multi-agent deep-dive of the source, with `file:line` references throughout. |

## The tutorial docs

Start at [`docs/index.md`](docs/index.md). The set:

1. [What is an agent harness?](docs/01-what-is-an-agent-harness.md) — educational primer: the nine components every harness shares
2. [eve overview & key concepts](docs/02-eve-overview-and-key-concepts.md)
3. [Harness deep dive](docs/03-eve-harness-deep-dive.md) — the tool loop, compaction, prompt cache, HITL parking, durability seam
4. [Subsystems](docs/04-eve-subsystems.md) — authoring pipeline, tools, skills, channels, connections, sandbox, evals, CLI/TUI
5. [Critique](docs/05-critique.md) — strengths and weaknesses with code references
6. [Roadmap](docs/06-roadmap.md) — improvements, new features, and features worth adopting from competing harnesses
7. [Claude Code profile](docs/07-claude-code.md)
8. [OpenAI Codex profile](docs/08-openai-codex.md)
9. [Grok Build profile](docs/09-grok-build.md)
10. [Competitive analysis](docs/10-competitive-analysis.md) — eve vs Claude Code vs Codex vs Grok Build, feature by feature

**Suggested reading path:** 01 → 02 → 03 (with `eve/packages/eve/src/harness/tool-loop.ts` open beside it) → 05 → 10 → 06.

## Provenance & disclaimers

- Not affiliated with or endorsed by Vercel. The `eve/` tree is unmodified upstream source at the pinned commit; to get the latest, clone [vercel/eve](https://github.com/vercel/eve) directly.
- The tutorial docs were generated 2026-07-16 by Claude Fable 5 orchestrating parallel code-analysis and web-research agents. Competitor facts are sourced in the profile docs; anything unverified is labeled.
- The docs describe eve **0.24.x** (public beta) — expect drift as upstream evolves.
