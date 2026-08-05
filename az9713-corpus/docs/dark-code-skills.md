---
repo: dark-code-skills
description: Claude Code skills and hooks addressing the dark code problem — AI-generated code that ships without anyone understanding it
language: PowerShell
stars: 0
forks: 0
created: 2026-04-13
updated: 2026-04-14
topics: 
is_fork: False
kb: 228
---

# dark-code-skills
# Dark Code Skills Suite

A suite of fourteen Claude Code skills and seven hooks that address the "dark code" problem: AI-generated code that passed automated checks and shipped without anyone ever understanding it.

Built in response to Nate Jones's work on the organizational risk of shipping code nobody comprehends:

- **Video**: [I Looked At Amazon After They Fired 16,000 Engineers. Their AI Broke Everything.](https://www.youtube.com/watch?v=E1idsrv79tI)
- **Substack**: [Your codebase is full of code nobody understood — not when it shipped, not now, not ever. Here's the fix.](https://natesnewsletter.substack.com/p/your-codebase-is-full-of-code-nobody)

---

## The Problem

AI coding tools generate code faster than teams can understand it. Automated tests pass. PRs merge. But nobody can explain what the module does, why it works that way, or what breaks if you change it. That gap — between code that runs and code that anyone comprehends — is dark code. As teams scale their AI usage, the gap compounds: every new feature is built on a foundation nobody fully understood.

Nate's framework names three layers of prevention: write a spec before generating code (Layer 1), make systems self-describing via context engineering (Layer 2), and require a comprehension gate before merge (Layer 3). This suite implements all three as Claude Code skills and hooks.

---

## Skills

### Core (Phase 1)

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `dark-code-audit` | Codebase comprehension debt audit — hotspot map, scorecard, action plan | `/dark-code-audit` |
| `context-layer-generator` | Generates MODULE_MANIFEST.md, BEHAVIORAL_CONTRACTS.md, DECISION_LOG.md for a module | `/context-layer-generator <path>` |
| `comprehension-gate` | Seven-dimension pre-merge review → CLEAR / REVIEW REQUIRED / HOLD | `/comprehension-gate` |
| `spec-driven-development` | Spec-first workflow with falsifiable eval assertions; gate is the closing step | `/spec-driven-development` |

### Phase 2: Isolation and agent safety

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `generate-isolation-tests` | Tenant isolation test scaffold for net-new shared resource writes | `/generate-isolation-tests <path>` |
| `pre-agent-task` | Pre-flight check before delegating work to an AI agent | `/pre-agent-task` |

### Phase 2: Compliance documentation

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `generate-data-lineage` | Data flow narrative from context layers — HIGH/MEDIUM/LOW confidence | `/generate-data-lineage` |
| `generate-gdpr-ropa` | Draft GDPR Article 30 Record of Processing Activities | `/generate-gdpr-ropa` |
| `generate-eu-ai-act-system-card` | Per-service EU AI Act system card — risk classification + documentation | `/generate-eu-ai-act-system-card <path>` |
| `generate-soc2-evidence` | SOC 2 CC8 Change Management evidence package from comprehension artifacts | `/generate-soc2-evidence` |

### Utilities

| Skill | Purpose | Invoke |
|-------|---------|--------|
| `dark-code-suite-init` | One-command setup — CLAUDE.md template + directory structure | `/dark-code-suite-init` |

---

## Hooks

| Hook | Event | Enforced? | Purpose |
|------|-------|-----------|---------|
| `load-dark-code-context` | SessionStart | No | Injects context layer coverage into every session |
| `check-spec-for-branch` | SessionStart | No | Warns when a feature branch has no spec document |
| `check-module-manifest` | PreToolUse Edit/Write | No | Warns when editing a module with no MODULE_MANIFEST.md |
| `decision-log-guard` | PreToolUse Edit/Write | No | Surfaces relevant Decision Log warnings before edits |
| `pre-commit-comprehension-check` | PreToolUse Bash | **Yes** | Blocks commits ≥50 lines without a recent comprehension artifact |
| `sign-comprehension-artifact` | PostToolUse Write | No | SHA-256 hash (+ GPG if available) after each artifact write |
| `push-artifact-to-protected-branch` | PostToolUse Bash | No | Pushes comprehension artifact to protected `comprehension-artifacts` branch |

The single enforced step is the pre-commit check: commits of ≥50 changed lines are blocked unless a recent `COMPREHENSION_ARTIFACT.md` exists. Everything else is advisory — warnings that surface relevant context before an action without blocking it.

---

## Artifacts

Each skill produces specific files:

- **COMPREHENSION_ARTIFACT.md** — written by `comprehension-gate`; required by the pre-commit hook; contains change summary, findings table, blast radius map, and CLEAR / REVIEW REQUIRED / HOLD verdict
- **MODULE_MANIFEST.md** — written by `context-layer-generator`; maps dependencies, persistent resources, and agent access permissions
- **BEHAVIORAL_CONTRACTS.md** — written by `context-layer-generator`; documents per-interface idempotency, failure modes, and isolation guarantees
- **DECISION_LOG.md** — written by `context-layer-generator`; captures why decisions were made, with Warning fields that surface when editing related files

---

## Documentation

- **[docs/index.md](docs/index.md)** — situation-based navigation: where to start depending on what you need to do
- **[Getting started](docs/getting-started/quickstart.md)** — working setup in under 15 minutes
- **[End-to-end workflow](docs/guides/end-to-end-workflow.md)** — how all the pieces fit together on a real project
- **[New feature workflow](docs/guides/new-feature-workflow.md)** — spec → build → gate loop that prevents dark code from being created
- **[Agent safety workflow](docs/guides/agent-safety-workflow.md)** — pre-flight, gate, and manifest update cycle for AI agent tasks
- **[Compliance workflow](docs/guides/compliance-workflow.md)** — GDPR, EU AI Act, and SOC 2 from context layer files
- **[Pain points coverage](docs/nate-pain-points-coverage.md)** — which of Nate's specific concerns this addresses, to what degree, and what remains out of scope
- **[Key concepts](docs/overview/key-concepts.md)** — definitions for dark code, comprehension debt, the Kiro pattern, context layers, and more
- **[Hooks reference](docs/reference/hooks.md)** — full configuration for each hook
- **[Artifacts reference](docs/reference/artifacts.md)** — what each artifact file contains and how to read it

---

## Audit Results (2026-04-13)

The suite was independently audited against the [OB1](https://github.com/openbrainos/ob1) codebase as a realistic test fixture. 10 of 11 skills were executed end-to-end; all 7 hooks were reviewed statically.

**Summary verdict:** Core skills work well. The enforcement layer has two critical failures that must be fixed before the suite's safety guarantees hold.

| Layer | Status |
|-------|--------|
| Core skills (audit, context-layer-generator, comprehension-gate) | PASS |
| Isolation and agent safety skills | PASS / PARTIAL |
| Compliance generators | PASS / PARTIAL |
| Enforcement hooks | 2 CRITICAL failures, 1 PARTIAL, 4 PASS |

### Critical findings requiring immediate action

1. **`decision-log-guard.ps1` — hook is broken for all auto-generated files** (DC-001, DC-002)  
   The regex `'^##\s+Decision:\s+(.+)'` cannot match headers produced by `/context-layer-generator` (`## Decision 1: Name`). The hook fires but surfaces no warnings. The two halves of the suite — skills that generate `DECISION_LOG.md` and the hook that enforces it — use incompatible formats.  
   **Fix:** Change the regex to `'^##\s+Decision\s*\d*[:\s]+(.+)'` and the Warning line regex to `'^\s*>?\s*[\*_]*\s*[⚠️]?\s*Warning'`.

2. **`push-artifact-to-protected-branch.ps1` — pushes full branch, not just artifacts** (DC-003)  
   The implementation pushes `HEAD` to `comprehension-artifacts`, exposing source code. The documented intent (cherry-pick only) is not implemented.  
   **Recommendation:** Disable this hook until the cherry-pick logic is correctly implemented.

3. **MODULE_MANIFEST.md schema mismatch between `context-layer-generator` and `pre-agent-task`** (DH-002)  
   `pre-agent-task` looks for "Agent Access section" and "Persistent resources table" — sections that `context-layer-generator` does not produce. Every well-documented module generates a permanent INFO alert.

Full findings: **[docs/audit/README.md](docs/audit/README.md)**  
All defects with reproduction steps: **[docs/audit/skill-defects.md](docs/audit/skill-defects.md)**  
Hook static review: **[docs/audit/hook-review.md](docs/audit/hook-review.md)**  
Per-skill test records: **[docs/audit/test-log.md](docs/audit/test-log.md)**

---

## What this cannot address

Three things are permanently outside the scope of Claude Code tooling:

1. **Runtime structural dark code** — an AI agent assembling an execution path at runtime that leaks data between services. Requires production APM and request tracing.
2. **Compliance-grade tamper-proof audit logging** — `COMPREHENSION_ARTIFACT.md` is evidence that a review happened, but it is not a tamper-proof audit log suitable for regulatory submission. Requires external immutable log infrastructure.
3. **Runtime cross-tenant exposure detection** — whether a Redis key that looks properly scoped in code is actually readable by another tenant under specific conditions. Requires security testing against a live system.

These gaps are documented in [Pain points coverage — out of scope](docs/nate-pain-points-coverage.md#what-remains-out-of-scope).

---

## Installation

### Skills

Copy each skill directory from `skills/` into `~/.claude/skills/`:

```bash
cp -r skills/comprehension-gate ~/.claude/skills/
cp -r skills/context-layer-generator ~/.claude/skills/
cp -r skills/dark-code-audit ~/.claude/skills/
cp -r skills/dark-code-suite-init ~/.claude/skills/
cp -r skills/spec-driven-development ~/.claude/skills/
cp -r skills/generate-isolation-tests ~/.claude/skills/
cp -r skills/generate-data-lineage ~/.claude/skills/
cp -r skills/generate-gdpr-ropa ~/.claude/skills/
cp -r skills/generate-eu-ai-act-system-card ~/.claude/skills/
cp -r skills/generate-soc2-evidence ~/.claude/skills/
cp -r skills/pre-agent-task ~/.claude/skills/
```

### Hooks

Copy each hook script from `hooks/` into `~/.claude/hooks/`:

```bash
cp hooks/*.ps1 ~/.claude/hooks/
```

Then register the hooks in `~/.claude/settings.json`. Add to the appropriate event arrays:

```json
{
  "hooks": {
    "SessionStart": [
      { "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/load-dark-code-context.ps1" }] },
      { "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/check-spec-for-branch.ps1" }] }
    ],
    "PreToolUse": [
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/check-module-manifest.ps1" }] },
      { "matcher": "Edit|Write", "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/decision-log-guard.ps1" }] },
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/pre-commit-comprehension-check.ps1" }] }
    ],
    "PostToolUse": [
      { "matcher": "Write", "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/sign-comprehension-artifact.ps1" }] },
      { "matcher": "Bash", "hooks": [{ "type": "command", "command": "powershell -File ~/.claude/hooks/push-artifact-to-protected-branch.ps1" }] }
    ]
  }
}
```

See [Getting started](docs/getting-started/quickstart.md) for the full setup walkthrough.
