---
repo: harness-engineering-blueprint
description: Comprehensive guide to harness engineering for long-running, multi-agent AI systems
language: TypeScript
stars: 11
forks: 2
created: 2026-02-23
updated: 2026-05-08
topics: 
is_fork: False
kb: 64
---

# harness-engineering-blueprint
# Harness Engineering Blueprint

A comprehensive, actionable guide to building infrastructure for long-running, multi-agent AI systems — synthesized from the latest research by Anthropic, OpenAI, Vercel, and LangChain.

## What is Harness Engineering?

The harness is the infrastructure layer that wraps around an AI model — managing what it can see, what tools it can use, how it recovers from mistakes, and how it persists state across sessions. As models become commoditized, the harness is what determines whether an agent actually works in production.

This repository contains:
- A **masterplan** distilling key principles from the leading teams
- A **CLI tool** (`harness`) that implements ~80% of the masterplan's patterns
- **Claude Code skills and hooks** for automatic enforcement in agent sessions

## Quick Start

```bash
# Install
npm install -g harness-cli

# Initialize in your project
cd your-project
harness init

# Add features to track
harness feature add

# Start a session
harness session start

# ... do work ...

# Verify before claiming done
harness verify

# End the session
harness session end
```

## CLI Commands

| Command | Description |
|---------|-------------|
| `harness init` | Initialize harness infrastructure in your project |
| `harness status` | Show project dashboard (progress, features, warnings) |
| `harness feature add` | Add a new feature to track |
| `harness feature list` | List all features with pass/fail status |
| `harness feature pass <id>` | Mark a feature as passing |
| `harness feature fail <id>` | Mark a feature as failing |
| `harness feature next` | Show the next feature to work on |
| `harness session start` | Start a new agent session |
| `harness session end` | End the current session and log progress |
| `harness verify` | Run the full verification loop |
| `harness monitor` | Check doom loop and budget status |
| `harness audit` | Audit MCP tools and skills for redundancy |
| `harness install skills` | Install Claude Code skills |
| `harness install hooks` | Install Claude Code hooks |

## What Gets Created

After `harness init`, your project will contain:

| File | Purpose |
|------|---------|
| `harness.json` | Project configuration and command definitions |
| `features.json` | Feature tracking with pass/fail status |
| `progress.md` | Session-by-session progress log |
| `init.sh` | Environment initialization script |
| `AGENTS.md` | Agent instructions and project context |
| `.harness/` | Runtime state (edit counts, budget tracking) |

## Claude Code Integration

### Skills

Install skills to get guided workflows:

```bash
harness install skills
```

- **harness-session** - Session start/end workflow with context loading
- **harness-verify** - Verification loop ("Ralph Wiggum" rule)
- **harness-init** - Interactive project setup

### Hooks

Install hooks for automatic enforcement:

```bash
harness install hooks
```

- **doom-loop-detector** - Warns when a file is edited too many times
- **commit-validator** - Checks commit message quality
- **budget-warning** - Alerts at 50%, 75%, 90% of session budget

## Key Patterns Implemented

From the [masterplan](harness_engineering_masterplan.md):

- **Incremental feature delivery** - One feature per session, tracked with pass/fail
- **Doom loop detection** - Catches repetitive edits before they waste time
- **Session budgets** - Time-based warnings to prevent runaway sessions
- **Verification loops** - Mandatory checks before claiming completion
- **Progress persistence** - Session logs carry context between agent runs
- **Git discipline** - Atomic commits, clean working tree checks

## Development

```bash
npm install
npm run typecheck    # Type check
npm test             # Run tests
npm run build        # Build with tsup
```

## Sources

This work synthesizes insights from the following publications:

1. **Anthropic** — [Effective harnesses for long-running agents](https://www.anthropic.com/engineering/effective-harnesses-for-long-running-agents)
2. **LangChain** — [Improving Deep Agents with harness engineering](https://blog.langchain.com/improving-deep-agents-with-harness-engineering/)
3. **OpenAI** — [Harness engineering: leveraging Codex in an agent-first world](https://openai.com/index/harness-engineering/)
4. **Vercel** — [We removed 80% of our agent's tools](https://vercel.com/blog/we-removed-80-percent-of-our-agents-tools)
5. **Prompt Engineering (YouTube)** — [The AI Model Doesn't Matter Anymore](https://www.youtube.com/watch?v=1Ohf2aeSPFA)

## License

This repository is for educational and reference purposes. All original research belongs to its respective authors and organizations linked above.
