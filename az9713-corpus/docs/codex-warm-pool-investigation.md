---
repo: codex-warm-pool-investigation
description: A performance-debugging detective story that reverse-engineers OpenAI Codex's hidden warm worker-pool. Observed-vs-inferred labeled, with a reproducible PowerShell appendix.
language: HTML
stars: 0
forks: 0
created: 2026-06-09
updated: 2026-06-09
topics: 
is_fork: False
kb: 17
---

# codex-warm-pool-investigation
# The Case of the Vanishing Milliseconds

**A performance-debugging detective story that reverse-engineers OpenAI Codex's hidden warm worker-pool — from process trees, timings, and connection ownership alone.**

📖 **Read it as a web page:** https://az9713.github.io/codex-warm-pool-investigation/

---

## TL;DR

A Windows laptop felt "sluggish." A deliberately dumb probe — timing `whoami`, a no-op native process — showed that *creating any process at all* was taking **6–14 seconds** while CPU, RAM, and disk all sat idle.

The recurring diagnosis had always blamed the real-time antivirus. This time the usual fix failed, so we ran one controlled experiment instead: **leave the antivirus fully on, kill the AI coding agent that happened to be running.** Spawn time collapsed from ~10 seconds to **40 milliseconds**.

The real root cause was an *interaction*, not a fault in either component:

> The antivirus does a **synchronous security check on every process creation**. The agent **spawns processes relentlessly**. Every unrelated process launch on the machine ends up **queuing behind the agent's spawns** in the security filter — so a queue of agent spawns taxes the whole system.

The fix is a one-line exclusion (allow-list the agent's folders), validated to cut the tax ~15×.

Then the better question: *why does the agent spawn so much?* Following that thread into the process tree uncovered an undocumented piece of Codex's architecture — a **warm worker-pool**:

> Codex runs a **central orchestrator** that owns all the API connections and conversation state, plus a **pre-warmed pool of idle execution workers** (`node_repl → codex app-server --listen stdio://`). Workers are kept warm so tasks dispatch without cold-start latency. The pool scales up for parallel work, trims itself lazily, and holds a small floor of idle workers — which on a normal machine is a smart, invisible optimization, and here was the very thing flooding the antivirus.

## What's in this repo

| File | What it is |
|---|---|
| [`index.html`](index.html) / [`codex-warm-pool-investigation.html`](codex-warm-pool-investigation.html) | The full article, styled for the web (self-contained, no dependencies) |
| [`codex-warm-pool-investigation.md`](codex-warm-pool-investigation.md) | The same article in Markdown source |

## How to read it critically

Because the warm-pool conclusion is **reverse-engineered from runtime behavior, not from source code**, every claim in the article is tagged:

- 🟢 **`OBSERVED`** — a fact taken directly from tool output (a timing, a process tree, a connection count), reproducible with the commands in the appendix.
- 🟡 **`INFERRED`** — an interpretation reasoned *from* those facts.

A capstone **evidence ledger** maps each measurement to the conclusion it supports, and the one thing the evidence can't yet settle is called out explicitly. The article also ships a **7-command PowerShell appendix** so you can rerun the entire investigation yourself.

## Method, in six lines

1. Measure adjectives into numbers (a dumb `whoami` probe was the whole key).
2. Magnitude discriminates mechanism — a multi-second stall on a no-op process is a *blocking wait*, not CPU contention.
3. Variance is a fingerprint — a fixed delay is a timeout; a wildly variable one is a queue. Queues have producers.
4. When a reliable fix suddenly fails, distrust the diagnosis, not your luck.
5. Isolate one variable before you escalate.
6. "Confounded" is not a footnote — ask what was *also* true during every measurement.

---

*Written up from a real diagnostic session on a Windows 11 machine. All host-specific identifiers have been removed; process IDs are illustrative. The antivirus behavior described is generic to real-time endpoint protection and is not a defect in any specific product. The Codex architecture described is inferred from runtime observation, not source.*
