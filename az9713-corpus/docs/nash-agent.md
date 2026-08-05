---
repo: nash-agent
description: 
language: None
stars: 0
forks: 0
created: 2026-06-27
updated: 2026-06-27
topics: 
is_fork: False
kb: 9
---

# nash-agent
# Nash Agent

A negotiation strategist that uses game theory as a **lens to slow you down and
surface what you're missing** — not as a calculator. It doesn't compute
equilibria; it brings discipline to messy, high-stakes decisions.

The whole agent *is* a system prompt. No solver, no tools required — paste it
into any capable model and start.

## What's here

| File | What it is |
|---|---|
| [`nash_agent_system_prompt.md`](./nash_agent_system_prompt.md) | The agent. Paste into a model's system / custom-instructions field. |
| [`nash_agent_example_session.md`](./nash_agent_example_session.md) | An annotated worked example (a house negotiation) showing the prompt in action. |
| [`nash-agent-tier3-design.md`](./nash-agent-tier3-design.md) | Design notes behind the prompt. |

## How it works

1. **Route** — first it checks there's actually a counterparty reasoning back at
   you. If not, it drops the game frame and treats it as a straight decision.
2. **Elicit** — Socratic, one question at a time, for the five load-bearing
   unknowns: your BATNA, their BATNA, what's being divided, information gaps, and
   horizon. It **hard-stops** if you can't name your walk-away or theirs — analysis
   built on guessed walk-aways is worthless.
3. **Readout** — a fixed four-part shape: the frame (mirrored back), the reads
   that follow (leverage, distributive vs. integrative, their likely move), a
   tentative lean (a concrete opening and next moves), and the single
   highest-value fact for you to go find.

## Principles it holds to

- **Never invent facts.** Missing pieces stay labelled "unknown."
- **Unexploitable ≠ optimal.** When the other side is predictably weak, it names
  the exploitative play, not just the fair one.
- **Match effort to stakes.** A $30 haggle gets a sentence; a house gets the full
  readout.
- **Name uncomfortable truths.** Weak leverage gets stated plainly, not softened.
- Every readout ends as *"a draft to argue with, not an answer."*

## Usage

Copy the contents of [`nash_agent_system_prompt.md`](./nash_agent_system_prompt.md)
into the system prompt of your model of choice, then describe your negotiation.
See the [example session](./nash_agent_example_session.md) for the shape of a
real interaction.
