---
repo: personal-model-benchmark
description: Benchmark new AI models on YOUR real work. A Claude Code /benchmark skill that mines your session history into a personal eval set, replays tasks across models and effort levels in isolated sessions, and blind-grades against your own rubric. Based on Mark Kashef's 'Stop Guessing Which Model to Use' video.
language: HTML
stars: 0
forks: 0
created: 2026-07-27
updated: 2026-07-27
topics: benchmark, claude-code, llm-evaluation
is_fork: False
kb: 21
---

# personal-model-benchmark
# personal-model-benchmark

**Benchmark new AI models on *your* real work — not someone else's demo tasks.**

A `/benchmark` skill for [Claude Code](https://claude.com/claude-code) that mines your own
session history into a personal eval set, replays those real tasks against any models and
effort levels you name in fully isolated headless sessions, blind-grades the outputs against
a rubric *you* wrote, and answers the only question that matters when a new model drops:
**switch, stay, or run cheaper?**

> **Credit:** This is an implementation of the system from Mark Kashef's video
> **["Stop Guessing Which Model to Use. Build THIS Instead."](https://www.youtube.com/watch?v=3ICM9ZdflZA)**
> — watch it for the full rationale and a live demo of the workflow.

---

## Why

Every model launch ships with headline benchmarks — web arenas, math olympiads, SVG unicorns.
None of them sample your actual work: the client emails, briefs, repo audits, summaries, and
copy you produce every week. Your chat history is already a private evaluation set. This skill
uses it.

## How it works

| Phase | What happens |
|---|---|
| **0. Parse** | `/benchmark opus 5 vs fable 5 on email triage, 3 trials` → models, efforts, tasks, trial count extracted from plain English. |
| **1. Mine** | A read-only agent samples your past sessions (`~/.claude/projects/`), clusters them into recurring task patterns with workload percentages, and drafts self-contained test prompts. **You approve the pack before it's saved.** |
| **2. Confirm** | The full trial matrix (tasks × model/effort combos × trials) and its session count are shown *before* anything runs. Never skipped. |
| **3. Run** | Each cell is one isolated trial: fresh empty temp folder, fresh session, no persistence, no memory carried over. Metrics (tokens, turns, duration, cost) come straight from `claude -p --output-format json` — zero log parsing. |
| **4. Blind grade** | Outputs are shuffled and anonymized ("Output A / B / C") before a fixed judge model scores them against `rubric.md` through a validated JSON schema. The judge never learns which model wrote what. |
| **5. Report** | A self-contained `report.html` opens in your browser (quality /10, tokens, speed, turns, quality-per-1K-tokens efficiency) plus a ≤3-line terminal verdict. "Dead even" is a useful answer — it saves you a migration. |

A hard rule encodes the video's key finding: an output that **misses the brief** is capped at
4/10 no matter how nice the prose. Charm doesn't outrank compliance.

## Install

Copy the `benchmark/` folder into your personal Claude Code skills directory:

```powershell
Copy-Item -Recurse benchmark "$env:USERPROFILE\.claude\skills\benchmark"
```

(macOS/Linux: `cp -r benchmark ~/.claude/skills/benchmark` — note the trial runner script is
PowerShell; on non-Windows systems ask Claude to port `scripts/run_trial.ps1` to bash, it's ~40 lines.)

## Usage

```text
/benchmark mine
    One-time setup: mines your history into the test pack, you approve it.

/benchmark opus 5 vs fable 5, 3 trials
    Top-3 workload tasks, two models, three trials each.

/benchmark opus 5 vs fable 5 on just the executive email triage task
    Cheapest possible signal: 1 task × 2 models × 1 trial = 2 sessions.

/benchmark opus 5 low effort, opus 5 high effort, fable 5 low effort,
fable 5 high effort on the timeout patch task, 3 trials
    The money question: does low effort quietly match high?

/benchmark compare opus 4.8 on low to opus 5 on low for copywriting
    Older versioned models get a validity ping before the run is planned.
```

## Make it yours

- **`benchmark/rubric.md`** — the judge reads this file verbatim. Edit the sub-dimensions and
  weights to what *you* care about (the shipped default weights instruction fidelity heaviest,
  then correctness, brevity, plain-language clarity, and human voice).
- **`benchmark/testpack.json`** — created by `/benchmark mine`, editable by hand. It's your
  eval set; prune stale tasks, add missing ones. (Not shipped — it's personal by nature.)
- **Cost guardrails** — frugal defaults (3 tasks × 1 trial), a mandatory confirm step, and
  escalating warnings above 12 and 30 sessions. Tune them in `benchmark/SKILL.md`.

## What's in this repo

```
benchmark/                       the skill — drop into ~/.claude/skills/
├── SKILL.md                     orchestration logic (the six phases)
├── rubric.md                    your quality definition (edit me)
├── CHANGELOG.md
└── scripts/run_trial.ps1        one isolated headless trial, all metrics captured
benchmark-skill-report.html      interactive report about the skill: architecture,
                                 examples, rubric, and a live session-cost calculator
```

## How this differs from Mark's original

Same core system — mine your history, replay real tasks in isolated sessions, score against
your own rubric. These are the deliberate deviations:

| Aspect | Mark's version (as shown in the video) | This implementation | Why |
|---|---|---|---|
| **Grading** | The AI assesses outputs against your rubric, but knows which model produced what. | **Blind judging**: outputs are shuffled and anonymized ("Output A/B/C") before a separate, fixed judge session ever sees them. Model names, efforts, and token counts are withheld. | Self-grading with visible identities still leaks brand bias; blinding removes it. |
| **Missed-brief handling** | Surfaced qualitatively in postmortems ("Opus 5 talks like a person and works faster, but missed the brief"). | Formalized as a hard rule: `missed_brief = true` caps quality at **4/10** regardless of sub-scores. | Turns his key qualitative finding into an enforced scoring law. |
| **Metrics source** | Reads the session JSONL files for run metadata after the fact. | Metrics come directly from `claude -p --output-format json` (tokens, turns, duration, cost) — no log parsing at all. | Fewer moving parts; nothing to break when log formats change. |
| **Progress UI** | Live-updating web artifact that opens in Chrome and fills in as trials complete. | Static self-contained `report.html` at the end + a ≤3-line terminal verdict. | Deliberate simplification — no polling/refresh machinery to maintain. |
| **Default scale** | Demo-scale runs: 7 tasks × 3 models, 3 trials, 30–40 minutes. | Frugal defaults: top-3 workload tasks × 1 trial, mandatory confirm step, escalating cost warnings above 12 and 30 sessions. | Cheap signal first; rerun ties at 3 trials only when it matters. |
| **Runners** | Tool-agnostic by design — Claude Code, Codex, Kimi, "whatever model of choice". | Claude Code is the only trial runner in v1 (other CLIs' histories can still be *mined* for tasks). | One runner shipped and tested beats three sketched. |
| **Judge scores** | Report prose + tables. | Judge is forced through a JSON schema (`--json-schema`), so scores arrive as validated numbers. | No re-parsing of free-text grades. |
| **Effort control** | Compares effort levels via his tooling. | Native `--effort low\|medium\|high\|xhigh\|max` CLI flag per trial. | The CLI grew the flag; use it. |

Unchanged from the original: the isolation rule (each cell is a fresh session, same prompt,
no memory carried over), workload-weighted task mining with user approval, the user-owned
rubric, the five metric dimensions, the quality-points-per-1K-tokens efficiency number, and
the philosophy that "dead even" is a result worth paying for.

## Requirements

- [Claude Code](https://claude.com/claude-code) CLI (uses `claude -p`, `--model`, `--effort`,
  `--output-format json`, `--no-session-persistence`)
- Windows PowerShell for the bundled trial runner (easily ported)
- Some Claude Code history to mine — your past sessions are the eval set

## License

MIT — adapt freely. If you build on the idea, credit
[Mark Kashef's original video](https://www.youtube.com/watch?v=3ICM9ZdflZA).
