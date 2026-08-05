# Claude Code 7-Level Operational Playbook

A practical, opinionated operating manual for moving Claude Code from raw prompting to a closed-loop, semi-autonomous artifact system.

> Based on the YouTube video **[The 7 Levels of Claude Code & Content (From Slop to Agentic)](https://www.youtube.com/watch?v=S6YwrVql83U&t=43s)**. This playbook takes the video's framework and upgrades it with concrete repo architecture, hooks, evals, provenance tracking, and human-controlled autonomy.

---

## Core Thesis

> Taste first. Workflow systems second. Automation last.

The winning pattern is not using Claude Code as a content spinner. It is moving from raw prompting into voice-controlled, systematized, scalable workflows — while keeping human review and brand judgment in the loop.

The correct path:

```
Context → Command → Artifact → Eval → Human Review → Controlled Reuse
```

---

## The 7 Levels

| Level | Name | What changes |
|---|---|---|
| 1 | Prompting Assistant | Stop vague prompting. Every request has task, audience, constraints, and failure modes. |
| 2 | Context-Governed Assistant | Durable voice, taste, and quality standards live in `CLAUDE.md` and `specs/`. |
| 3 | Skill-Based Workflow Executor | Repeated workflows become callable slash commands (`/brief`, `/critique`, `/research`). |
| 4 | Multimodal / Multi-Tool Orchestrator | Add images, diagrams, slides, UI mockups, web data — with a structured visual brand system. |
| 5 | Artifact Factory | One source → many outputs: summary, playbook, memo, thread, README, visual brief. |
| 6 | Scheduled Semi-Autonomous System | Automated draft generation with hooks as guardrails and mandatory human review gates. |
| 7 | Closed-Loop Agent System | Research → Draft → Critique → Eval → Human Approval → Performance learning loop. |

---

## Highlights

### Structured Prompt Template (Level 1)
Every task gets explicit fields: `Task`, `Input`, `Desired output`, `Audience`, `Constraints`, `Quality bar`, `Failure modes to avoid`. Eliminates generic AI output from the start.

### Voice + Context System (Level 2)
A `master_voice.md` defines identity ("technical, rigorous, high-signal, skeptical, operator-oriented"). A `banned_phrases.md` kills AI-isms like "game changer," "unlock," and "dive into." Good/bad example pairs drive behavior, not tone instructions.

### Five Core Slash Commands (Level 3)
- `/brief` — high-signal briefing with executive summary, mechanisms, implications, and next actions
- `/critique` — internal coherence, factual risk, incentive conflicts, and failure modes
- `/research` — claim table with evidence, source, and confidence rating
- `/cascade` — one source → full artifact bundle
- `/publish-check` — factuality, voice fidelity, reputational risk, and publish verdict

### Cascade Workflow (Level 5)
Feed one transcript, paper, or earnings call and receive: technical summary, critique, operational playbook, checklist, short post, long memo, and visual brief — all with source provenance tracked.

### Safety Hooks (Level 6)
Deterministic Python hooks block writes to sensitive paths, reject unsourced factual claims, and log every session. No automation publishes without a human approval gate. Every artifact carries explicit `status: draft` / `review_required: true` metadata.

### Closed-Loop Agent Architecture (Level 7)
Six specialized agents — `researcher`, `synthesizer`, `critic`, `editor`, `compliance`, `publisher-assistant` — each with a distinct role. An evaluation rubric scores every artifact on factuality, signal density, voice fidelity, structural clarity, operational usefulness, and risk control (1–5 scale). Performance data generates *proposed* spec updates — never silent self-modification.

---

## Repo Structure

```
claude-os/
  CLAUDE.md                        # Global operating instructions
  specs/voice/                     # Voice, banned phrases, examples
  specs/research/                  # Citation and claim policies
  specs/visual/                    # Brand system, image prompt schema
  .claude/commands/                # Slash command workflows
  .claude/hooks/                   # Deterministic safety gates
  workflows/                       # Human-readable workflow descriptions
  artifacts/drafts|briefs|memos/   # Generated outputs
  scripts/                         # Deterministic utilities
```

---

## Minimum Viable Starting Point

Build only these first — they deliver most of the leverage:

```
CLAUDE.md
specs/voice/master_voice.md
specs/research/citation_policy.md
.claude/commands/brief.md
.claude/commands/critique.md
.claude/commands/cascade.md
.claude/commands/publish-check.md
```

---

## Implementation Sequence

| Week | Focus |
|---|---|
| Week 1 | Levels 1–2: CLAUDE.md, voice spec, banned phrases, citation policy |
| Week 2 | Level 3: Five slash commands, tested on real transcripts and repos |
| Week 3 | Levels 4–5: Visual brand system, image prompt schema, cascade workflow |
| Week 4 | Level 6: Scheduled ingestion, hooks, human review gate |
| Month 2 | Level 7: Subagents, eval rubrics, scorecards, controlled memory update process |

---

## Key Guardrails

- No automation publishes without human review
- No silent self-modification of core specs — performance data generates proposals, humans approve
- Hooks block sensitive paths and reject unsourced current-event claims
- Every artifact is versioned and carries explicit review status
- Level 7 agents are separated by role — research, drafting, critique, and eval never collapse into one step
