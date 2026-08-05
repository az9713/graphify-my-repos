---
repo: karpathy-skill-creator
description: A Claude Code skill for creating skills governed by Karpathy's four principles: think before drafting, simplicity first, surgical changes, goal-driven execution.
language: None
stars: 0
forks: 0
created: 2026-04-29
updated: 2026-04-29
topics: 
is_fork: False
kb: 5
---

# karpathy-skill-creator
# karpathy-skill-creator

A Claude Code skill for creating skills the right way — governed by Andrej Karpathy's four principles of disciplined AI execution.

Inspired by Jack Roberts' video **"Claude Code + Karpathy's System = $10,000 Skills"**:
[https://www.youtube.com/watch?v=pCqpuHA8kHM&t=221s](https://www.youtube.com/watch?v=pCqpuHA8kHM&t=221s)

---

## The Problem

Most Claude Code skills are static markdown files. They're:

- **Generic** — they don't know your business, audience, or standards
- **Amnesic** — they forget feedback and prior conversations
- **Static** — they behave identically on day 1 and day 1000
- **Tool-blind** — they can't fetch live data or interact with external systems
- **Non-improving** — they never update themselves after feedback

The result is a graveyard of skills that sound good on paper but don't drive real value.

---

## The Solution: Karpathy's Principles Applied to Skill Creation

Andrej Karpathy — co-founder of OpenAI, former Tesla AI director — articulated four principles that expose the big limitations when working with AI models. Jack Roberts' video shows how these principles, originally framed around coding, can be applied to building **super skills**: skills that listen, remember, and improve over time.

### The Four Principles

| Principle | Original meaning | In skill creation |
|---|---|---|
| **Think before coding** | Surface assumptions and trade-offs before writing code | Define outcome, failure modes, and verifiable success criterion *before* drafting SKILL.md |
| **Simplicity first** | No overengineering, no bloated abstractions | 200-line target, no bundled resources unless tests prove they're needed, explain the *why* not the *what* |
| **Surgical changes** | Touch only what you must; don't refactor adjacent code | During improvement, change only what feedback named — maintain a CHANGELOG |
| **Goal-driven execution** | Define verifiable success and work toward it | Write assertions before spawning test runs, not after seeing the output |

---

## The Super Skill Framework (From the Video)

The video introduces a 4-level framework for skills that do real work:

| Level | Name | What it means |
|---|---|---|
| 1 | **Creation** | Architect the skill around a concrete verifiable outcome — not a generic description |
| 2 | **Data** | Give the skill eyes: tools, connectors, live data sources |
| 3 | **Memory** | Persist strategic context, feedback history, and user preferences across sessions |
| 4 | **Self-improvement** | Build in a feedback → changelog → skill-update loop |

A skill missing any level is, per the video's framing, "a Ferrari running on hopes and dreams."

This skill enforces all four levels via a shipping checklist.

---

## What `karpathy-skill-creator` Does

`karpathy-skill-creator` is a Claude Code skill that guides you through creating other skills — using Karpathy's principles as a governing discipline layered over [Anthropic's official `skill-creator` workflow](https://github.com/anthropics/claude-code).

### Phase 1 — Think Before Drafting

Before any writing, you must explicitly answer:

1. **Outcome** — What does this skill produce, given what input?
2. **Failure modes** — What are the 3 most likely ways this goes wrong?
3. **Success criterion** — One verifiable sentence: what does a passing test look like?
4. **Scope boundary** — What is this skill explicitly NOT doing?

If you can't answer #3, you stop. No drafting until success is defined.

### Phase 2 — Simplicity First

Write the minimum viable SKILL.md. Enforce leanness at draft time:

- Under 200 lines for most skills
- No bundled resources until 2+ test cases independently create the same helper
- Instructions explain the *why*, not just the what
- No all-caps rules — reframe as explanation of consequences

### Phase 3 — Goal-Driven Testing

Write assertions for each test case **before** spawning runs — not while they execute. Assertions come from the success criterion defined in Phase 1, not from observing the skill's output.

### Phase 4 — Surgical Improvement

Before editing, write out:
```
Failures this iteration:
1. [exact failure from feedback]

Changes I'm making:
1. [change] → fixes failure #1
```

If a change isn't tied to a listed failure, it doesn't ship. Every iteration adds one line to `CHANGELOG.md`.

---

## Installation

Copy the skill folder into your Claude Code skills directory:

```bash
# macOS / Linux
cp -r .claude/skills/karpathy-skill-creator ~/.claude/skills/

# Windows
xcopy /E /I .claude\skills\karpathy-skill-creator %USERPROFILE%\.claude\skills\karpathy-skill-creator
```

Then in Claude Code, invoke it:

```
/karpathy-skill-creator
```

Or reference it by name when asking Claude to create a skill — it will appear in the available skills list and trigger automatically when you ask to create or improve a Claude Code skill.

---

## Repo Structure

```
.claude/
  skills/
    karpathy-skill-creator/
      SKILL.md          ← the skill itself
```

---

## Credit

- **Andrej Karpathy** — four principles of disciplined AI execution
- **Jack Roberts** — ["Claude Code + Karpathy's System = $10,000 Skills"](https://www.youtube.com/watch?v=pCqpuHA8kHM&t=221s)
- **Anthropic** — Claude Code skills system and `skill-creator` workflow
