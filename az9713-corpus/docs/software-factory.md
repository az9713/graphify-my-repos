---
repo: software-factory
description: Claude Code software factory — 9 agents, 2 skills, 3 hooks. Based on Ullah's FreeCodeCamp article.
language: Shell
stars: 1
forks: 1
created: 2026-05-25
updated: 2026-07-20
topics: 
is_fork: False
kb: 58
---

# software-factory
# Software Factory for Claude Code

A ready-to-drop-in software factory for Claude Code, reverse-engineered and implemented from Qudrat Ullah's article ["How to Build a Software Factory with Claude Code: From Vibe Coding to Agentic Development"](https://www.freecodecamp.org/news/how-to-build-software-factory-with-claude-code/) (FreeCodeCamp, May 2026).

This factory was used to build **[saas-billing](https://github.com/az9713/saas-billing)** — a multi-tenant SaaS billing application — by running seven specialized agents in sequence: `@codebase-researcher` mapped the codebase before every feature, `@story-writer` and `@spec-writer` produced the story and technical brief, `@backend-builder` and `@frontend-builder` implemented each slice, `@test-verifier` wrote acceptance tests against the story criteria, and `@implementation-validator` caught gaps before any PR was opened.

---

## What This Is

This is a **pre-defined agent pipeline** — a structured set of Claude Code files that gives one developer and one AI the coordination patterns of a small engineering team. It is not a fully autonomous, non-interactive coding agent. You remain in the loop at three explicit approval gates. Think of it as a disciplined workflow scaffold, not a black box.

> If you are looking for an end-to-end autonomous coding agent that takes a spec and produces a codebase without human intervention, see [Attractor](https://factory.strongdm.ai/products/attractor). This factory is a different category of tool: structured, human-gated, and transparent about every decision it makes.

---

## Origin

Ullah's article argues that "vibe coding" — prompting Claude ad-hoc and accepting whatever it produces — breaks down on real projects. Features contradict each other. Conventions drift. The AI forgets what it decided three sessions ago.

His solution is a small software factory: a structured approach to using AI for **planning, building, testing, and reviewing** features while maintaining control of your codebase. The key insight is that you are not replacing the engineering team — you are giving a single developer the coordination patterns of a team by routing work through specialized agents with defined responsibilities.

---

## The Five Layers

The factory is organized into five layers, each building on the one below.

```
┌─────────────────────────────────────────────────────────┐
│  Layer 5 — Delivery                                     │
│  Hooks enforce quality gates before every commit        │
│  pre-commit.sh · PostToolUse lint · Stop typecheck+test │
├─────────────────────────────────────────────────────────┤
│  Layer 4 — Workflow                                     │
│  Skills define the orchestration procedure              │
│  feature-factory/SKILL.md · build-with-tests/SKILL.md  │
├─────────────────────────────────────────────────────────┤
│  Layer 3 — Agents                                       │
│  Subagents with isolated context windows and tool locks │
│  9 agents: researcher · story · spec · backend ·        │
│  frontend · test-verifier · validator · orchestrator ·  │
│  pr-reviewer                                            │
├─────────────────────────────────────────────────────────┤
│  Layer 2 — Knowledge                                    │
│  Domain documentation agents read before writing        │
│  docs/architecture · billing · email · jobs · db        │
├─────────────────────────────────────────────────────────┤
│  Layer 1 — Context                                      │
│  CLAUDE.md — auto-loaded every session                  │
│  Stack · commands · architecture rules · don't-dos      │
└─────────────────────────────────────────────────────────┘
```

**Layer 1 — Context:** `CLAUDE.md` is automatically loaded at the start of every Claude Code session. It contains the project stack, CLI commands, architectural rules, and hard prohibitions (no raw payment logging, no database errors in client responses, no editing merged migrations). Every agent inherits this context without being told to read it.

**Layer 2 — Knowledge:** The `docs/` directory gives agents deeper domain context on demand. Before writing billing code, an agent reads `docs/billing.md`. Before touching background jobs, it reads `docs/jobs.md`. This keeps `CLAUDE.md` short (100–300 lines) while still giving agents the detail they need.

**Layer 3 — Agents:** Each agent is a subagent definition in `.claude/agents/`. Agents run in isolated context windows, have a restricted tool list (read-only agents cannot write files; write agents cannot call arbitrary shell commands), and are assigned a model appropriate to their task (Haiku for cheap searches, Sonnet for reasoning and building).

**Layer 4 — Workflow:** Skills in `.claude/skills/` define the orchestration procedure. A skill is a `SKILL.md` file that Claude Code loads on demand when you invoke `/feature-factory` or `/build-with-tests`. The skill file tells Claude exactly which agents to run, in which order, and where to pause for human input.

**Layer 5 — Delivery:** Hooks in `.claude/hooks/` and wired in `.claude/settings.json` run deterministic shell scripts at lifecycle events. They are not AI suggestions — they are mandatory gates that fire regardless of what the agent decided.

---

## The Orchestrator Chain

Running `/feature-factory` triggers the 11-step pipeline:

```
┌─────────────────────────────────────────────────────────────────┐
│  /feature-factory  "I want to <describe feature>"               │
└───────────────┬─────────────────────────────────────────────────┘
                │
                ▼
        ┌───────────────┐
        │ @codebase-    │  Maps every file that will be touched.
        │ researcher    │  Read/Grep/Glob only. Can run in parallel.
        └───────┬───────┘
                │
                ▼
        ┌───────────────┐
        │ @story-writer │  Turns the feature idea into a user story
        │               │  with acceptance criteria.
        └───────┬───────┘
                │
                ▼
        ╔═══════════════╗
        ║  HUMAN GATE 1 ║  "Is this the right problem?"
        ║  Story review ║  Cheapest point to fix a misunderstood goal.
        ╚═══════╤═══════╝
                │ approved
                ▼
        ┌───────────────┐
        │ @spec-writer  │  Turns the story into a technical brief:
        │               │  schema changes, service contracts, test plan.
        └───────┬───────┘
                │
                ▼
        ╔═══════════════╗
        ║  HUMAN GATE 2 ║  "Any design red flags?"
        ║  Brief review ║  Cheapest point to catch architectural mistakes.
        ╚═══════╤═══════╝
                │ approved
                ▼
        ┌───────────────┐   ┌───────────────┐
        │ @backend-     │   │ @frontend-    │  Sequential (frontend reads
        │ builder       │──▶│ builder       │  what backend just wrote).
        │               │   │               │  PostToolUse lint hook fires
        └───────┬───────┘   └───────┬───────┘  after every Edit.
                │                   │           Stop hook runs typecheck+test
                └─────────┬─────────┘           after each agent finishes.
                          │
                          ▼
                ┌───────────────────┐
                │  @test-verifier   │  Writes acceptance tests proving
                │                   │  each story criterion is met.
                └─────────┬─────────┘
                          │
                          ▼
                ┌───────────────────┐
                │ @implementation-  │  Gap report by severity:
                │ validator         │  CRITICAL / WARNING / PASS.
                └─────────┬─────────┘
                          │
              ┌───────────┴────────────┐
              │ critical findings?     │
              │ Yes → loop back to     │
              │ builder(s), re-verify, │
              │ re-validate            │
              │ No → continue          │
              └───────────┬────────────┘
                          │ no criticals
                          ▼
                ╔═════════════════╗
                ║  HUMAN GATE 3   ║  "Ready to ship?"
                ║  PR approval    ║  Final accountability stays with a person.
                ╚═════════════════╝
```

The three human gates are non-negotiable. Business intent (Gate 1), architectural safety (Gate 2), and final accountability (Gate 3) cannot be delegated to an AI.

---

## Repository Contents

```
.
├── README.md                          ← This file
├── factory/                           ← Drop into any Next.js + Node.js project
│   ├── CLAUDE.md                      ← Auto-loaded project context
│   ├── docs/
│   │   ├── architecture.md            ← Service boundaries, tenant isolation
│   │   ├── billing.md                 ← Stripe webhooks, invoice lifecycle
│   │   ├── email.md                   ← Resend setup, available templates
│   │   ├── jobs.md                    ← BullMQ queues, retry policy
│   │   └── db.md                      ← Schema conventions, soft-delete rules
│   └── .claude/
│       ├── settings.json              ← Hook wiring
│       ├── agents/                    ← 9 subagent definitions
│       │   ├── codebase-researcher.md
│       │   ├── story-writer.md
│       │   ├── spec-writer.md
│       │   ├── backend-builder.md
│       │   ├── frontend-builder.md
│       │   ├── test-verifier.md
│       │   ├── implementation-validator.md
│       │   ├── feature-orchestrator.md
│       │   └── pr-reviewer.md
│       ├── skills/
│       │   ├── feature-factory/SKILL.md     ← Full 11-step pipeline
│       │   └── build-with-tests/SKILL.md   ← Targeted single-feature build
│       └── hooks/
│           └── pre-commit.sh               ← Blocks secret file commits
└── docs/                              ← Meta-documentation for this repo
    ├── software_factory_explained.md  ← Architecture deep-dive with diagrams
    ├── factory_inventory.md           ← Fidelity audit: every file mapped to spec
    └── factory_workflows.md           ← 7 worked examples exercising every feature
```

---

## Using the Factory

### Prerequisites

Copy `factory/` into your project root. The factory is designed for a Next.js 14 + Node.js + Prisma stack. Before running features, scaffold your external services:

- **[Neon](https://neon.tech)** — Serverless Postgres. Create a project and set `DATABASE_URL` in `.env`.
- **[Redis](https://redis.io)** (or [Upstash](https://upstash.com)) — Required for BullMQ background jobs. Set `REDIS_URL` in `.env`.
- **[Resend](https://resend.com)** — Transactional email. Create an API key and set `RESEND_API_KEY` in `.env`.

### Run the full factory chain

```
/feature-factory

I want to <describe your feature in one sentence>.
```

### Run a targeted backend fix

```
/build-with-tests

<describe the bug or change>
```

### Invoke individual agents

```
@codebase-researcher how does invoice creation work today?
@pr-reviewer review this PR against the project checklist
```

### Advanced: run the orchestrator in its own context window

```
@feature-orchestrator I want to add <feature>.
```

Keeps your main session clean for large, multi-service features.

---

## What the Factory Does Not Do

- It does not scaffold the Next.js project itself. Run `npx create-next-app` first.
- It does not create your Neon database, Redis instance, or Resend account. You do that.
- It does not bypass the three human approval gates. That is intentional.
- It is not a fire-and-forget autonomous agent. You review and approve at each gate.

---

## Related

- Article: [How to Build a Software Factory with Claude Code](https://www.freecodecamp.org/news/how-to-build-software-factory-with-claude-code/) — Qudrat Ullah, FreeCodeCamp, May 2026
- Sample app built with this factory: [saas-billing](https://github.com/az9713/saas-billing) — multi-tenant SaaS billing app (Next.js 14, Prisma, BullMQ, Resend)
- Autonomous end-to-end coding agent (different category): [Attractor by StrongDM](https://factory.strongdm.ai/products/attractor)
