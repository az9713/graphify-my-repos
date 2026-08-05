---
repo: claude-knowlege-base-prompting
description: A study of the self-improving Claude knowledge base prompt: how it works, how to write constitution-style prompts, Obsidian from several angles, and a Python tool to extract hub/orphan signals without Obsidian.
language: Python
stars: 0
forks: 0
created: 2026-06-25
updated: 2026-06-25
topics: 
is_fork: False
kb: 26
---

# claude-knowlege-base-prompting
# Claude Knowledge Base — Prompting Study

A study of the "self-improving Claude knowledge base" prompt: what it does, how it
is built, and how to write **constitution-style prompts** like it. Plus a small
Python tool that pulls the same **hub** and **orphan** signals out of a markdown
wiki that people usually reach for Obsidian to see.

## Source

This work is based on the YouTube video
[**Build a Self Improving Claude Knowledge Base**](https://www.youtube.com/watch?v=0-QDPnEIkvw)
and its associated
[**Knowledge Base Prompt**](https://docs.google.com/document/d/1OuGOpp8aJkUtGSH55qy-OHmI94HexeXZAGz_XcY8-P0/edit).
The prompt text we analyze is captured in [`Knowledge Base Prompt.md`](./Knowledge%20Base%20Prompt.md)
(three related prompts: a Knowledge Base, a Business Journal, and a Health Dashboard).

## What's here

| File | What it is |
|---|---|
| [`Knowledge Base Prompt.md`](./Knowledge%20Base%20Prompt.md) | The source prompts, verbatim. |
| [`Knowledge Base Prompt — Discussion Notes.md`](./Knowledge%20Base%20Prompt%20%E2%80%94%20Discussion%20Notes.md) | Full walkthrough: the meta-thinking, how the prompts work, the self-improvement question, and the Obsidian thread. |
| [`graph_report.py`](./graph_report.py) | Extracts hubs and orphans from a markdown wiki — no Obsidian. |
| [`graph_report — README.md`](./graph_report%20%E2%80%94%20README.md) | How `graph_report.py` works, how to run it, and the test fixture. |
| [`test_wiki/`](./test_wiki) | A 6-page fixture seeded with a hub, an orphan, a self-link, and a wikilink. |

## What we learned

**Not just what the prompt does — how to write prompts like it.** The prompt isn't
a task ("do X"); it's a **constitution** for an ongoing system. It stands up a
self-maintaining folder, then writes a `CLAUDE.md` that becomes its own permanent
instruction every future session. The reusable moves it teaches:

- safety rails stated *before* any capability ("never delete, never move without
  approval");
- **plan → approve → act**, with a human gate in front of every irreversible step;
- separating raw **sources** from synthesized **wiki**, so output can never
  corrupt ground truth;
- naming the operating loop (**INGEST / ANSWER / TIDY**) as permanent vocabulary;
- defining persona by its **failure mode** ("if it reads like a self-help blog
  post, you failed");
- plain-markdown **portability**, so nothing is locked to one app.

We also weigh the "self-improving" claim honestly: the knowledge *accumulates*
automatically, but the system only gets *better* through you (TIDY reports a punch
list, it doesn't fix anything). It's **self-accumulating + human-maintained**, not
a closed learning loop.

**Obsidian, from several angles.** Is it in the prompt? (No — never mentioned, and
the prompt deliberately uses portable markdown.) What does it buy you? (A visible
graph and free backlinks — for the human, not the system.) What's lost without it?
(Ergonomics, not capability.) And the punchline below: the structural signals
people open Obsidian for are recomputable from plain text.

## Extracting hubs & orphans without Obsidian

`graph_report.py` counts links to surface the two signals that tell you most about
a wiki's shape:

- **Hubs** — the most linked-to pages. A high inbound count means a load-bearing
  page: either a genuine foundation, or an over-broad "junk drawer" worth
  splitting.
- **Orphans** — pages nothing links to. A forgotten link, a true island, or an
  undeveloped seed.

```bash
python graph_report.py test_wiki      # report on the fixture
python graph_report.py --selftest     # built-in checks
```

```
TOP HUBS (most linked-to):
    4  <- markdown.md
    ...
ORPHANS (nothing links here):
       orphan-page.md
```

### Pros

- **No dependency, no lock-in.** Stdlib only; runs on any folder of `.md`. The
  signal lives in the plain text, not in any app's database.
- **Handles both link styles** — `[text](page.md)` and Obsidian `[[wikilinks]]`.
- **Handles the index trap.** A table-of-contents page links to everything; the
  script ignores links *originating from* `index`/`readme`/`log`, so the TOC
  doesn't mask every orphan or masquerade as the top hub. (This bug was real and
  only showed up when run on a wiki *with* an index — see the discussion notes.)

### Cons / limits

- **Regex scrape, not a real markdown parser.** Links inside code fences are
  counted; reference-style links (`[a][1]`) are missed.
- **Matches by filename, not path** — same-named files in different folders
  collide.
- **Inbound only** — it finds orphans (no inbound) but not dead-ends (no
  *outbound*). Easy to add when you need it.

### How accurate / reliable are the hubs and orphans?

**Directionally very reliable; not exact.** The link structure of a wiki is real
data, and ~95% of it is plain `[ ]( )` / `[[ ]]` links that the regex catches
cleanly, so the **ranking** of hubs and the **set** of orphans are trustworthy
enough to act on — which page to verify first, which page to connect or prune.

Where to be careful:

- Counts can be off by a few links (missed reference-style links, code-fence false
  positives), so treat exact in-degree numbers as *approximate*. The *ordering*
  survives small miscounts.
- **Degree is a prompt for inquiry, not a verdict.** A hub might be a foundation or
  a junk drawer — the script can't tell you which; you decide. A fresh page is a
  legitimate orphan, indistinguishable from a neglected one until it's sat
  disconnected for a while.
- The fixture in `test_wiki/` is a regression baseline: if its output changes, the
  script changed behavior.

**Bottom line:** backlinks and the graph aren't *stored* by Obsidian — they're
*derived* from link text every time you open it. Anything derivable is
reproducible, so no tool holds your knowledge graph hostage. The one thing this
script can't give you is the *picture* — seeing a disconnected cluster at a glance.
For find-the-hubs, find-the-orphans, the 40-line script is the whole job.
