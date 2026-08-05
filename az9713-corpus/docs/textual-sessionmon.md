---
repo: textual-sessionmon
description: One terminal pane showing every live Claude Code, Codex, and Grok CLI session — context fill, model cost tier, and current tool. Built with Textual.
language: Python
stars: 0
forks: 0
created: 2026-08-02
updated: 2026-08-02
topics: 
is_fork: False
kb: 4865
---

# textual-sessionmon
# sessionmon

**One terminal pane showing every Claude Code, Codex, and Grok CLI session you have running.**

If you drive more than one coding agent, you lose track of them. Which session is
about to hit its context limit? Which one is still running a shell command? Which
expensive model did you leave open two hours ago? The answers are all sitting on
disk in JSONL logs — `sessionmon` reads them and puts them in one table.

![sessionmon demo](docs/demo.gif)

<sub>Sorting by context fill, switching agent tabs, and opening the command
palette. Plays inline above — for full resolution, grab
[the 1.3 MB MP4](docs/sessionmon.mp4).</sub>

Built with [Textual](https://github.com/Textualize/textual).

---

## What it shows

| Column | Meaning |
|---|---|
| ● | live (writing right now) / ○ idle / ✖ collector error |
| AGENT | claude · codex · grok, each with a fixed hue |
| SESSION | short id, dimmed — there to copy, not to scan |
| PROJECT | working directory name, faded by how long since it moved |
| MODEL | coloured by cost tier, not identity |
| CTX | tokens the model held on its most recent turn |
| CONTEXT FILL | coloured meter — green under 50%, red near the limit |
| TOOLS | tool calls seen in the tail window |
| AGE | time since the log last grew |
| DOING | the current tool, coloured by risk class |

Nothing is decorative. Six independent colour dimensions mean a glance answers six
questions without reading a word:

- **state** — is it alive, idle, or broken?
- **agent** — which tool is this? (scan the All tab by hue)
- **age** — a gradient, not a live/dead binary
- **context fill** — how close to compaction? the one that costs money
- **cost tier** — burn rate per token, premium / mid / cheap
- **doing** — writes (orange) vs reads (blue) vs network (cyan) vs delegation (violet)

Press `l` for a legend so none of it has to be memorised.

## Install and run

```bash
git clone https://github.com/az9713/textual-sessionmon
cd textual-sessionmon
pip install textual
python app.py
```

Python 3.12+. Textual 8.2.8 or newer. No other dependencies.

`sessionmon` is read-only — it opens log files, seeks, and reads. It never writes
to, modifies, or deletes anything an agent owns.

## Controls

| Input | Action |
|---|---|
| **click a column header** | sort by it; click again to reverse (▼/▲ marks the active column) |
| `ctrl+p` | command palette — fuzzy-jump to any session by project, agent, model, or id |
| tabs / arrows | switch between All · claude · codex · grok |
| `a` | cycle the age window (1h → 24h → 7d) |
| `l` | toggle the colour legend |
| `r` | refresh now |
| `q` | quit |

## Where the data comes from

| Agent | Log location | What is available |
|---|---|---|
| Claude Code | `~/.claude/projects/<project>/<uuid>.jsonl` | model, per-turn context, tools, cwd |
| Codex CLI | `~/.codex/sessions/YYYY/MM/DD/rollout-*.jsonl` | context, real context window, lifetime spend |
| Grok CLI | `~/.grok/sessions/<cwd>/<uuid>/events.jsonl` | status, tool lifecycle, turn outcome |

### Honest limits

These are measured against real logs, not assumed:

1. **Grok records no token usage anywhere on disk.** Grok rows show status, tool
   counts, and turn outcome — the context columns stay empty. Not a bug.
2. **Codex rarely records its model name.** In a 24-hour sample, 0 of 40 sessions
   wrote a `turn_context` record. Those rows show the provider (`openai`) instead
   of inventing a model.
3. **Claude context % appears only for models whose window is known.** The logs
   never record it, and a flat 200k guess was disproven by real sessions holding
   239k and 310k. Unknown families render `-` rather than a confidently wrong
   percentage. Override with `SESSIONMON_CLAUDE_WINDOW=1000000`.
4. **Model cost tiers are a hand-maintained prefix map** in `app.py`. No log
   records price. Unlisted models stay grey rather than get a guessed tier.

## How it is built

Two files, and the split is the point.

**`collect.py` — zero Textual imports, deliberately.** It scans the three log
trees and returns plain `Session` dataclasses. It runs standalone:

```bash
python collect.py            # print a table, no TUI
python collect.py --selftest # check the tail parser
```

Because the collector has no framework in it, the same code can feed a cron job,
a web view, or a different UI entirely. The TUI is one consumer, not the owner.

**`app.py` — the Textual layer.** Tabs, colour, sorting, the command palette,
and a 2-second refresh running in a worker so disk reads never block the UI.

### The one decision that mattered

Claude's log tree here is 734 files and about 1 GB, the largest single session
66 MB. Nothing is ever read whole. `tail_records()` seeks to the last 256 KB of a
file, discards the truncated first line, and parses from there — so cost is flat
no matter how large a session grows. A full refresh across all three agents takes
about 0.22 seconds.

That parser is the only non-trivial logic in the project, so it is the only thing
with a test: `python collect.py --selftest` checks that tailing returns records
contiguous to end-of-file, skips corrupt lines, and handles empty files.

For the full account of how this was built — every fork, every wrong turn, and
which Textual capability solved each feature — see
**[DEVELOPMENT-JOURNEY.md](DEVELOPMENT-JOURNEY.md)**.

## Adding another agent

`collect.py` exposes a `COLLECTORS` dict. Write a function that returns
`list[Session]`, register it, and the app grows a tab for it automatically —
`TABS = ["", *COLLECTORS]` in `app.py` does the rest. No UI changes needed.

## License

MIT — see [LICENSE](LICENSE).
