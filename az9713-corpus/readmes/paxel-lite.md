# paxel-lite

A **100% local** "Spotify Wrapped" for your Claude Code sessions. It reads your
own transcripts from `~/.claude/projects/`, computes a deck of stat cards, and
renders a single self-contained `report.html`. **Nothing is uploaded anywhere** —
no server, no Docker, no account, no telemetry. Stdlib-only Python, zero
dependencies.

Every card is clickable and opens a detail view: hour-of-day histograms, top-5
lists, a streak calendar, and model / tool / project breakdowns.

**▶ [View the live demo](https://az9713.github.io/paxel-lite/)** (synthetic data)

![paxel-lite demo report](docs/demo-screenshot.png)

## Why this exists

It's a clean-room, privacy-first take on **Paxel**, the transcript-analysis tool
YC's design team showed off in this video:

> **YC's Head of Design Shows You How To Design With AI**
> https://www.youtube.com/watch?v=VbqaL_eHhKY&t=400s

Paxel ([paxel.ycombinator.com](https://paxel.ycombinator.com)) does the same
kind of "how do you build with AI" analysis, but its pipeline routes transcript
excerpts through YC's LLM proxy and uploads scores and metadata to YC.
`paxel-lite` reproduces the *experience* — the stamp-card report, the fun facts,
the archetype — while keeping **every byte on your machine**. It shares no code
with Paxel; the metrics and rendering were reimplemented from scratch.

## Demo

[`demo.html`](demo.html) is generated from **synthetic data** — open it to see
the format without looking at anyone's real usage.

## Usage

```bash
python wrapped.py                    # analyze everything -> report.html
python wrapped.py --since 30         # only the last 30 days
python wrapped.py --project my-app   # only projects matching a substring
python wrapped.py --llm              # add LLM-written cards (uses your local `claude` CLI)
python wrapped.py --demo             # synthetic demo.html, reads no transcripts
```

Requires Python 3.9+. Open the resulting `.html` in any modern browser.

## The cards

Archetype · most-used model · most productive hours · longest single session ·
prompts per session · prompt length · parallel sessions · plan-mode usage ·
favorite tools · total volume · busiest project · biggest crash-out · longest
streak · subagent fleet. With `--llm`, three cards (archetype flavor, a crash-out
roast, and a "signature move") are rewritten by your local `claude` CLI.

## Privacy

- `report.html` embeds **your real data** (project names, prompt excerpts, token
  counts). It is **gitignored** so you can't commit it by accident. Only
  `demo.html` — built from fabricated data — is committed.
- The report is fully offline. The only network reference is a Google Fonts
  `<link>` in the HTML; delete it for a truly airtight file.
- `--llm` shells out to your local `claude` CLI under your own account;
  transcript excerpts never leave your machine otherwise.

## How it works

`wrapped.py` streams each `*.jsonl` transcript line by line, identifies genuine
human-typed prompts (filtering out tool results, meta records, and subagent
sidechains), and aggregates metrics into the card deck. Card art is procedurally
generated (a seeded Bayer-dithered PNG, written with the stdlib — no image
library).

## License

MIT. Not affiliated with, endorsed by, or connected to Y Combinator or Paxel.
