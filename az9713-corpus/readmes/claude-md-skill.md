# claude-md-creator

A Claude Code skill that generates production-quality `CLAUDE.md` files for any project — automatically exploring the codebase, inferring the stack, and applying proven best practices.

## Background

This skill is based on the best practices from the video **"Knowing This Gives You An Unfair Advantage With Claude Code"** by AI Labs:

**[Watch on YouTube →](https://www.youtube.com/watch?v=fMY5Sdj2DMk&t=182s)**

The video makes the case that `CLAUDE.md` is not a passive README — it's an **operating policy file** that shapes Claude Code's default behavior, task framing, safety posture, verification discipline, and context economy. This skill encodes all 19 best practices from the video into a repeatable workflow.

## What it does

When you invoke this skill, Claude will:

1. **Explore the project** — reads `package.json`, `pyproject.toml`, `Cargo.toml`, lockfiles, config files, and directory structure to infer the full stack without asking
2. **Ask targeted questions** — only for things it can't infer (max 5 questions)
3. **Generate a tailored `CLAUDE.md`** — structured as a behavioral contract, not a README
4. **Handle monorepos** — root file with global invariants + proposed per-app scoped files
5. **Offer scoped rule files** — `rules/api.md`, `rules/frontend.md`, etc. for complex projects

## What the generated CLAUDE.md includes

Every output follows this structure (in priority order):

| Section | Purpose |
|---|---|
| Project Context | Stack, key directories, entry points |
| Non-Negotiable Rules | Behavioral contract: think before coding, surgical changes, verify before done |
| Task Execution Protocol | 6-step process for each task |
| Coding Standards | Project-specific patterns |
| Verification Protocol | Ordered: tests → typecheck → lint → build → runtime |
| Tools and Commands | Stack-specific commands only (pnpm vs pip vs cargo, etc.) |
| Git Safety | Destructive commands requiring confirmation |
| Completion Report | What changed, what was verified, what was observed but not changed |

## How to use

Install the skill by copying this directory into `~/.claude/skills/claude-md-creator/`.

Then in any Claude Code session, say any of:

- `Create a CLAUDE.md for this project`
- `Initialize CLAUDE.md`
- `Help Claude understand my codebase`
- `Set up Claude for this repo`

Claude will detect the skill and run the full workflow.

## Benchmark results

Tested across three project types (Next.js/pnpm, Python/FastAPI, pnpm monorepo):

| | With skill | Without skill |
|---|---|---|
| Behavioral contract sections present | **100%** | 0% |
| Git Safety section | **100%** | 33% |
| Completion Report | **100%** | 0% |
| Stack-correct commands | 100% | 100% |
| Overall pass rate | **100%** | 58.5% |

The main gap: Claude without guidance correctly identifies the stack and commands but produces a README-style file. The skill produces a behavioral contract.

## Key best practices encoded

From the video's 19-point framework:

- **Project description first** — context before rules, always
- **Non-negotiable rules at the top** — safety and verification before everything else
- **Local truth only** — no boilerplate Claude already knows
- **Surgical changes rule** — only touch files required for the task
- **Verify behavior, not just code presence** — ordered verification protocol
- **Under 200 lines** — root file stays concise; detail goes in scoped files
- **Git safety** — explicit confirmation required for destructive commands
- **Completion report** — every task ends with a structured status report

## Files

```
claude-md-creator/
├── SKILL.md                    # Main skill — workflow and generation rules
├── README.md                   # This file
├── references/
│   └── best-practices.md       # Full best-practices reference and skeleton
└── evals/
    └── evals.json              # Test cases for skill evaluation
```
