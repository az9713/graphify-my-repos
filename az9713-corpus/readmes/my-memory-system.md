# My Memory System (MMS)

> A portable behavioral memory layer that runs alongside Claude Code — so the AI model of how you work lives on your machine, not inside a provider's infrastructure.

---

## Why this exists

In April 2026, a packaging error exposed half a million lines of Anthropic's internal source code. Hidden inside was a project called **Conway** — an always-on agent environment that learns how you work over time: which emails you prioritize, how you structure decisions, which patterns you repeat. The agent compounds its usefulness with every passing day.

The problem: that compounding lives in Anthropic's infrastructure, not yours.

This is a new category of vendor lock-in. Previous lock-in was about *data* — your files, your messages, your records. Data portability laws and export tools exist for that. Conway-style lock-in is about *intelligence* — the behavioral model of how you work, built up over months of always-on observation. There is no export format for "how this person thinks." Switch providers and you leave the brain behind.

Every major AI lab (Anthropic, Google, OpenAI) is converging on this model. The race is not to build the best model — it's to build the persistent agent layer that accumulates the most behavioral context about its users. Whoever owns that layer owns the customer.

**MMS exists to break that lock-in before it sets.**

> This project was motivated by the analysis: [*"I Analyzed 512,000 Lines of Leaked Code. It Shows What's Coming for Your AI Tools."*](https://www.youtube.com/watch?v=ro5jpbi5uYc)

---

## What MMS is

MMS is a set of PowerShell scripts hooked into Claude Code's lifecycle. It captures what happens in every session, distills that into structured memory files you own, and feeds those memories back into future sessions.

**The memory belongs to you.** The files are plain markdown. Copy them into a ChatGPT or Gemini system prompt and they work there too. Switch providers and take your memory with you.

### Storage

MMS uses two stores:

| Store | Location | Contents |
|-------|----------|----------|
| Global | `C:\Users\<you>\mms\memory\` | Who you are, how you like to work — applies everywhere |
| Per-project | `<project>\.mms\memory\` | Project goals, decisions, deadlines — scoped to one repo |

Both stores are plain markdown files indexed by a `MEMORY.md` file. No database. No proprietary format.

### Memory types

| Type | Examples |
|------|---------|
| `user` | Role, expertise, background |
| `feedback` | "Always write tests first", "Prefer terse responses" |
| `project` | Deadline, architecture decision, stakeholder context |
| `reference` | "Bugs tracked in Linear project INGEST" |

---

## How it works

MMS has three layers:

```
┌─────────────────────────────────────────────┐
│  LAYER 1: CAPTURE                           │
│  Claude Code hooks → raw/events.jsonl       │
│  Every prompt + significant tool call       │
└──────────────────┬──────────────────────────┘
                   │ on SessionEnd
┌──────────────────▼──────────────────────────┐
│  LAYER 2: DISTILLATION                      │
│  distill.ps1 calls Claude → memory/*.md    │
│  Raw events → structured behavioral facts  │
└──────────────────┬──────────────────────────┘
                   │ on SessionStart
┌──────────────────▼──────────────────────────┐
│  LAYER 3: SURFACING                         │
│  load-memory.ps1 injects MEMORY.md          │
│  Claude starts each session knowing you     │
└─────────────────────────────────────────────┘
```

### Layer 1 — Capture

Four Claude Code hooks run automatically:

| Hook event | Script | Async? |
|-----------|--------|--------|
| `UserPromptSubmit` | `capture-prompt.ps1` | Yes — zero latency impact |
| `PostToolUse` | `capture-tool.ps1` | Yes — zero latency impact |
| `SessionEnd` | `capture-session-end.ps1` | No — must complete before exit |
| `SessionStart` | `load-memory.ps1` | No — output feeds session context |

Everything appends to `raw/events.jsonl`. A full Claude Code JSONL transcript is also mirrored to `raw/transcripts/` as a lossless backup.

### Layer 2 — Distillation

At session end, `distill.ps1` runs in the background:

1. Reads new events since the last watermark (`distiller/watermark.json`)
2. Sends them to Claude via `claude -p` (non-interactive)
3. Claude returns a JSON array of memory objects
4. MMS writes each as a `.md` file in the appropriate store
5. Updates the `MEMORY.md` index and advances the watermark

The distillation prompt (`distiller/prompt.md`) controls what Claude extracts. Edit it to change what gets remembered.

### Layer 3 — Surfacing

At session start, `load-memory.ps1` reads both `MEMORY.md` files (global + per-project) and injects them into the new session as `additionalContext`. Claude starts with your behavioral history already loaded — no re-explaining yourself.

---

## Repository structure

```
mms/
├── scripts/
│   ├── capture-prompt.ps1        # UserPromptSubmit hook
│   ├── capture-tool.ps1          # PostToolUse hook
│   ├── capture-session-end.ps1   # SessionEnd hook (triggers distiller)
│   ├── mirror-transcripts.ps1    # Passive transcript backup
│   ├── distill.ps1               # Extracts memories via Claude
│   └── load-memory.ps1           # Injects memories on SessionStart
├── distiller/
│   └── prompt.md                 # Distillation prompt template
├── memory/
│   └── MEMORY.md                 # Global memory index (auto-maintained)
└── docs/                         # Full documentation
    ├── index.md
    ├── getting-started/
    │   ├── onboarding.md         # Start here — the full why/what/how
    │   └── quickstart.md         # Setup from scratch
    ├── concepts/                 # Deep dives: capture, distillation, surfacing
    ├── guides/                   # How-tos: run manually, customize, reset
    ├── reference/                # Scripts and configuration reference
    ├── architecture/
    │   ├── system-design.md
    │   └── adr/                  # Why each design decision was made
    └── troubleshooting/
```

---

## Getting started

See [docs/getting-started/quickstart.md](docs/getting-started/quickstart.md) for full setup instructions.

**Prerequisites:** Windows 10/11, Claude Code, Git Bash, `ANTHROPIC_API_KEY`

The short version:

1. Copy `scripts/` and `distiller/` to `C:\Users\<you>\mms\`
2. Seed `memory/MEMORY.md` and `distiller/watermark.json`
3. Register the four hooks in `~\.claude\settings.json`
4. Start a Claude Code session — capture begins immediately

---

## The portability test

After a few sessions, copy `memory/MEMORY.md` into a ChatGPT or Gemini system prompt. Ask it what it knows about how you work. If it answers correctly — without being told anything — behavioral lock-in is broken. Your memory travels with you.

---

## Full documentation

**[docs/getting-started/onboarding.md](docs/getting-started/onboarding.md)** — the complete why/what/how narrative, including the Conway context, design rationale, and a realistic end-to-end walkthrough.

**[docs/index.md](docs/index.md)** — full documentation index.

---

## License

MIT
