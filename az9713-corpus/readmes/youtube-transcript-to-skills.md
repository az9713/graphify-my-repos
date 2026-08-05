# Claude Code 50 Tips -> Skills

A curated set of **11 Claude Code skills** distilled from [John Kim's "50 Claude Code Tips from 6 Months of Daily Use"](https://www.linkedin.com/pulse/50-claude-code-tips-from-6-months-daily-use-john-kim-cfa-cqf-frm-klknc/) (Staff SWE at Meta) — plus a meta-skill that automates the entire extraction process for any AI workflow transcript.

Not every tip should be a skill. Of the 50 tips, 19 were converted into 10 domain skills. The rest were categorized as keyboard shortcuts, built-in commands, one-time setup, philosophy, CLAUDE.md rules, or hooks. See [docs/tip-to-skill-mapping.md](docs/tip-to-skill-mapping.md) for the full breakdown.

## Skills

### Domain Skills (from Kim's 50 tips)

| Skill | Command | What it does |
|-------|---------|-------------|
| **claude-md-doctor** | `/claude-md-doctor` | Audit & improve CLAUDE.md files |
| **setup-validation** | `/setup-validation` | Configure build/test/lint loop |
| **plan-feature** | `/plan-feature <desc>` | Plan before coding |
| **session-save** | `/session-save` | Save session progress |
| **session-load** | `/session-load` | Restore session context |
| **create-skill-from-workflow** | `/create-skill-from-workflow <name>` | Turn workflows into skills |
| **spawn-investigator** | `/spawn-investigator <question>` | Isolated codebase investigation |
| **setup-hooks** | `/setup-hooks` | Configure Claude Code hooks |
| **setup-mcp** | `/setup-mcp <service>` | Find & install MCP servers |
| **explore-plugins** | `/explore-plugins` | Discover & install plugins |

### Meta-Skill: AI Workflow Transcript -> Skills

| Skill | Command | What it does |
|-------|---------|-------------|
| **youtube-transcript-to-skill** | `/youtube-transcript-to-skill <path>` | Extract skills from AI workflow transcripts |

> **AI workflows only.** This meta-skill is purpose-built for transcripts and articles about **AI-assisted development**: Claude Code, Cursor, Copilot, Windsurf, agentic coding patterns, and similar tools. It is **not** a general-purpose transcript processor — content about cooking, woodworking, fitness, etc. will produce zero skills (and the skill will explain why). The selection criteria (G1-G4 gates, V1-V4 values, E1-E6 exclusions) are calibrated specifically for evaluating whether a developer workflow tip should become a Claude Code skill.

The meta-skill encodes the full process used to create the 10 domain skills above. Give it a `.txt`, `.md`, or `.pdf` transcript from a YouTube video (or article) about AI coding workflows, and it extracts tips, evaluates each against the selection framework, groups qualifying tips into skills, and generates SKILL.md files — with full transparency at every step. See [The Meta-Skill Story](#the-meta-skill-story) below.

## Installation

Copy the `.claude/skills/` directory into your project:

```bash
cp -r .claude/skills/ /path/to/your/project/.claude/skills/
```

Or install individual skills by copying specific skill directories.

## How Skills Were Selected

Each of John Kim's 50 tips was evaluated against a decision framework:

**Gate criteria** (all must pass): Is it automatable? Recurring? Not built-in? Best as a skill (vs CLAUDE.md/Hook/MCP)?

**Value criteria** (at least one): Multi-step workflow? Domain knowledge? Error reduction? Time savings?

**Exclusions**: Keyboard shortcuts, one-time setup, pure philosophy, always-on rules (CLAUDE.md), deterministic automation (Hooks).

The full framework is documented in `.claude/skills/youtube-transcript-to-skill/selection-criteria.md` and used automatically by the meta-skill.

## The Meta-Skill Story

Creating the 10 domain skills from Kim's 50-tip video was a multi-hour manual process: read the transcript, extract tips, evaluate each against the selection criteria, categorize non-skill tips by reason, group related tips into skills, write SKILL.md files, and document every decision.

The `youtube-transcript-to-skill` meta-skill automates all of it. It was built to answer a simple question: **can we do this again for any AI workflow video without the manual effort?**

### Eating our own dog food

To validate the meta-skill, we ran it back against the original Kim transcript — the same input that produced this project. Results:

- **50 tips extracted** (exact match with manual analysis)
- **10 skills generated** from 19 skill-worthy tips (exact match)
- **Same skill names, same groupings, same classifications**
- **Found 2 tips (#45, #46) that the manual analysis had missed entirely** — they weren't classified in any category

The complete test run with per-tip evaluations is captured in [docs/meta-skill-dogfood-test.md](docs/meta-skill-dogfood-test.md). The generated analysis report is at [docs/kim-50-claude-code-tips-analysis.md](docs/kim-50-claude-code-tips-analysis.md).

## Project Structure

```
.claude/
  skills/           <- 11 skills (10 domain + 1 meta-skill)
    youtube-transcript-to-skill/
      SKILL.md              <- The meta-skill
      selection-criteria.md <- G/V/E evaluation framework
  sessions/         <- Session save/load storage
  plans/            <- Feature plan storage
docs/
  tip-to-skill-mapping.md              <- Full 50-tip classification
  skill-selection-and-usage-guide.md   <- Selection criteria + real-world examples
  kim-50-claude-code-tips-analysis.md  <- Meta-skill's analysis of Kim transcript
  meta-skill-dogfood-test.md           <- Full dogfood test run with findings
CLAUDE.md           <- Project conventions
```

## Adding Community Skills

If you want community skills alongside these custom ones, install them separately:

```bash
npx skills add anthropics/skills    # skill-creator, frontend-design, etc.
npx skills add vercel-labs/skills   # find-skills
```

This creates `.agents/skills/` (canonical files) and symlinks into `.claude/skills/` and other tool directories. Those are not included in this repo — install them yourself if you want them.

## Acknowledgements

1. This project was inspired by the YouTube video ["The #1 Agent Skill Nobody Is Talking About (Yet)"](https://www.youtube.com/watch?v=ap8635U6jbI).
2. All code and documentation were generated by [Claude Code](https://claude.ai/claude-code) powered by Opus 4.6.
