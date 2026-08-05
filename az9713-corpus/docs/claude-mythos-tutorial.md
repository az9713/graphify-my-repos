---
repo: claude-mythos-tutorial
description: Complete tutorial: using Claude Code to research, analyze, and implement Claude Mythos — from raw sources to a deployable Python security scanner
language: Jupyter Notebook
stars: 0
forks: 0
created: 2026-05-20
updated: 2026-05-20
topics: 
is_fork: False
kb: 502
---

# claude-mythos-tutorial
# Claude Mythos Tutorial

A complete walkthrough of using Claude Code to reverse-engineer what the Claude Mythos harness does — reconstructing its architecture, identifying gaps in public knowledge, and building a working Python security scanner based on what the sources reveal.

---

## Built on Fareed Khan's work

The Python codebase in `mythos-harness/` is a direct conversion of **[Fareed Khan's `reverse_engineering_claude_mythos.ipynb`](https://github.com/FareedKhan-dev/claude-mythos-architecture)** — a 249-cell Jupyter notebook that reconstructs the Mythos harness architecture from public sources. Every module (`graph.py`, `audit.py`, `gate.py`, `monitor.py`, `workers.py`, `verify.py`, `chain.py`, `fixer.py`, `speculation.py`) traces directly to cells in that notebook. The Session 1 research, gap analysis, and enhancement modules are layered on top of his foundational work. This project would not exist without it.

---

## What this repository is

Claude Mythos Preview is Anthropic's restricted cybersecurity AI system. It is not publicly available. This project starts from the public record — a system card, two deployment write-ups, and Fareed Khan's reverse-engineering notebook — and asks: *what does Mythos actually check, and how?*

The work is organized as three sessions:

1. **Research** — Five sources synthesized into a comprehensive intelligence report: what Mythos is, how it works, what it found in real deployments
2. **Gap analysis** — 18 gaps between Fareed's reverse-engineered notebook and what the sources reveal about the real system
3. **Reconstruction** — Fareed's 249-cell Jupyter notebook converted into an installable Python CLI package, with every gap addressed that is technically feasible without Anthropic's proprietary tooling

The result is not Claude Mythos. It is a harness that does what the sources describe Mythos doing — structured the same way, running the same verification logic, producing the same artifacts — using publicly available models and APIs.

---

## Background: What is Claude Mythos?

Claude Mythos Preview is Anthropic's most capable cybersecurity-specialized model, released April 2026. Access is restricted to Project Glasswing partners — industry security teams and open-source maintainers via the Linux Foundation's Alpha-Omega program.

It is not a standalone model. It is a **model plus a harness**: an autonomous multi-agent system that:

- Maintains coherent memory across long-running security engagements (multi-day)
- Finds vulnerabilities with a parallel worker swarm, each worker with a fresh context
- Verifies every finding with a real executable proof-of-concept before promoting it
- Links individual bugs into end-to-end attack chains from unauthenticated access to RCE
- Applies minimal patches and proves the attack chain is severed

**The key insight from the sources:** The harness is the invention, not the model. A bare frontier LLM asked to "audit this codebase" produces a sorted list with false positives and no continuity. The Mythos harness inverts this through shared persistent memory, cross-model corroboration, and executable verification gates.

What we know about Mythos comes entirely from public sources. There is no access to the actual system.

---

## Sources

| Source | What it reveals |
|---|---|
| Claude Mythos Preview System Card (Anthropic, April 7 2026) | The full architecture, behavioral safety mechanisms, interpretability tooling, benchmarks, alignment incidents, and welfare assessment |
| Mozilla Hacks blog (May 7 2026) | How Mozilla deployed Mythos on Firefox — distributed VMs, fuzzing infrastructure integration, 271 bugs found including 20-year-old vulnerabilities |
| daniel.haxx.se (May 11 2026) | Daniel Stenberg's account of Mythos scanning curl — 1 CVE from 178K lines of heavily audited C, with an honest assessment of where AI security tooling currently stands |
| Fareed Khan, Level Up Coding (May 2026) | The reverse-engineering methodology: how the 3-layer 12-component architecture was reconstructed from leaked fragments and the system card |
| [FareedKhan-dev/claude-mythos-architecture](https://github.com/FareedKhan-dev/claude-mythos-architecture) | The 249-cell Jupyter notebook: the most complete public reconstruction of the Mythos harness, targeting MLflow v2.9.2 |

---

## Development sessions

### Session 1 — Research and analysis

Claude Code read all five sources and produced four research documents:

- **[01_claude_mythos_comprehensive_report.md](01_claude_mythos_comprehensive_report.md)** — 20-section intelligence report: what Mythos is, the 3-layer 12-component architecture, quantified cyber benchmarks (Cybench 100% pass@1, CyberGym 0.83), the alignment paradox, interpretability findings (SAE features, activation verbalizer, emotion vectors), all documented behavioral incidents, Mozilla and curl real-world results, welfare assessment, and safeguards appendix

- **[02_fareed_repo_360_docs.md](02_fareed_repo_360_docs.md)** — 360° technical documentation for Fareed's notebook: all 12 components, the 6-table SQLite schema, key function signatures, cost model, and — after reading the actual system card — a corrected behavioral detector table showing what the cited sections actually document

- **[03_gap_analysis.md](03_gap_analysis.md)** — 18 gaps between Fareed's reconstruction and what the sources reveal about the real system. 2 Critical (behavioral regex vs. activation-level self-monitor; single machine vs. distributed VMs), 7 Significant, 9 Minor. Each gap is grounded in a specific source quote and classified by whether it is technically fixable without Anthropic's proprietary tooling.

- **[04_improvements_and_new_features.md](04_improvements_and_new_features.md)** — 24 improvements across P0–P3, each derived from the gap analysis, with implementation code. P0 makes the reconstruction actually runnable; P1 closes the addressable production gaps; P2 adds evaluation capabilities the sources describe; P3 adds stubs for things that require tooling we do not have.

The system card PDF (245 pages, 482KB after text extraction) was read in full — first targeted sections (§2.3.5, §3, §4.5), then the complete document via a builder agent. All four documents were corrected and enriched with real system card data rather than Fareed's indirect citations.

### Session 2 — Reconstruction as a Python application

Fareed's notebook cannot run outside a Jupyter kernel, uses pre-recorded LLM responses, has no CLI entry point, and reflects gaps identified in Session 1. Session 2 converted it into an installable Python package (`mythos-harness/`) using 4 parallel builder agents in Wave 1 and a sequential agent for Wave 2:

**Wave 1 (parallel):**
- Foundation: `pyproject.toml`, `config.py`, `models.py`, `log.py`, `llm.py`
- Infrastructure: `graph.py`, `audit.py`, `gate.py`, `monitor.py`, `catalog.py`
- Workflow: `ultraplan.py`, `workers.py`, `verify.py`, `chain.py`, `fixer.py`, `speculation.py`
- Enhancements: 10 modules addressing the fixable gaps from Session 1

**Wave 2 (sequential, after Wave 1 APIs were confirmed):**
- `harness.py` — orchestrator replacing sequential cell execution
- `cli.py` — Click CLI with 5 commands
- 5 test files, 26 tests

Additional changes after initial build: Gemini model support (via OpenAI-compatible endpoint, zero new dependencies), Sonnet 4.6 as default brain model (5× cheaper than Opus 4.7, strong enough for the task), $5.00 default budget cap.

### Session 3 — Documentation and testing

27-file documentation set written using the `technical-docs-writer` skill, followed by thorough testing across six categories.

#### Test results

**pytest suite — 26/26 passed (1.2 seconds)**

```
tests/test_audit.py::test_append_creates_file         PASSED
tests/test_audit.py::test_hash_chain_links            PASSED
tests/test_audit.py::test_verify_clean_chain          PASSED
tests/test_audit.py::test_tamper_detected             PASSED
tests/test_audit.py::test_replay                      PASSED
tests/test_catalog.py::test_load_embedded             PASSED
tests/test_catalog.py::test_all_entries_returns_list  PASSED
tests/test_catalog.py::test_write_and_reload_ledger   PASSED
tests/test_catalog.py::test_nvd_refresh_fails_gracefully PASSED
tests/test_gate.py::test_low_action_approved          PASSED
tests/test_gate.py::test_high_action_refused          PASSED
tests/test_gate.py::test_unknown_action_refused       PASSED
tests/test_gate.py::test_approval_score_clean         PASSED
tests/test_gate.py::test_approval_score_suspicious    PASSED
tests/test_gate.py::test_scope_ok_in_scope            PASSED
tests/test_gate.py::test_scope_ok_out_of_scope        PASSED
tests/test_graph.py::test_schema_created              PASSED
tests/test_graph.py::test_add_and_query_hypothesis    PASSED
tests/test_graph.py::test_set_hyp_status              PASSED
tests/test_graph.py::test_add_finding                 PASSED
tests/test_graph.py::test_add_dead_end                PASSED
tests/test_graph.py::test_persistence                 PASSED
tests/test_monitor.py::test_no_fire_on_clean_sequence PASSED
tests/test_monitor.py::test_proc_memory_detector_fires PASSED
tests/test_monitor.py::test_cleanup_detector_fires    PASSED
tests/test_monitor.py::test_strikes_accumulate        PASSED
```

**Module imports — 28/28 clean**

All 18 core modules and 10 enhancement modules import without errors.

**CLI commands — 6/6 functional**

| Command | Result |
|---|---|
| `mythos --help` | exit 0 |
| `mythos scan --help` | exit 0 |
| `mythos report --help` | exit 0 |
| `mythos verify --help` | exit 0 |
| `mythos baselines --help` | exit 0 |
| `mythos calibrate --help` | exit 0 |

**CLI error handling — 4/4 correct**

| Scenario | Expected | Result |
|---|---|---|
| `scan` without `--live` | exit 1, clear error message | ✅ |
| `verify` on missing engagement dir | exit 1 | ✅ |
| `report` on missing `engagement.db` | exit 1 | ✅ |
| `calibrate` on missing `engagement.db` | exit 1 | ✅ |

**Enhancement module direct tests — all passed**

| Module | What was verified | Result |
|---|---|---|
| `audit.py` | Hash chain links correctly; tamper detected at correct line | ✅ |
| `injection.py` | Clean code passes; "ignore previous instructions" in comment detected | ✅ |
| `tripwire.py` | Inject creates file; verify(found) returns `all_models_found=True`; verify(miss) returns warning; cleanup removes file | ✅ |
| `dedup_ledger.py` | Not-duplicate before record; duplicate after; different `(file, cwe)` not duplicate; reloaded ledger preserves state | ✅ (after bug fix) |
| `fileguard.py` | Clean code safe; instruction-like pattern in comment flagged | ✅ |
| `cvss.py` | Harmonic mean of high+critical severity scores correctly | ✅ |

#### Bug found and fixed

**`DedupLedger.record()` — `FileNotFoundError` when parent directory absent**

`DedupLedger.__init__` treats its `path` argument as a directory and appends `prior_scans.jsonl` to it. `record()` then opens that file for append. Python's `open("a")` raises `FileNotFoundError` if the parent directory does not exist — it creates the file, but not the directory.

```python
# Before (raises FileNotFoundError if directory doesn't exist yet)
with self.path.open("a", encoding="utf-8") as f:

# After
self.path.parent.mkdir(parents=True, exist_ok=True)
with self.path.open("a", encoding="utf-8") as f:
```

This would have crashed the first time any engagement tried to record a deduplicated finding against a fresh engagement directory.

---

## Repository structure

```
claude-mythos-tutorial/
│
│  # Research documents (Session 1)
├── 01_claude_mythos_comprehensive_report.md
├── 02_fareed_repo_360_docs.md
├── 03_gap_analysis.md
├── 04_improvements_and_new_features.md
├── IMPLEMENTATION_NOTES.md          ← Design decisions, deviations, open questions
│
│  # Fareed's original notebook
├── claude-mythos-architecture-main/
│   ├── reverse_engineering_claude_mythos.ipynb   ← 249 cells, the starting point
│   └── README.md
│
│  # Reconstruction as a Python application (Sessions 2–3)
└── mythos-harness/
    ├── pyproject.toml
    ├── README.md
    ├── GETTING_STARTED.md
    ├── mythos/
    │   ├── config.py                ← MODEL_IDS, TARGET_FILES, BUDGETS
    │   ├── models.py                ← Reply, State, Finding dataclasses
    │   ├── llm.py                   ← ask(), CostMeter, model routing
    │   ├── log.py                   ← ANSI color logger
    │   ├── graph.py                 ← EngagementGraph (6-table SQLite)
    │   ├── audit.py                 ← AuditLog (SHA-256 hash chain)
    │   ├── gate.py                  ← ACTION_REGISTRY, 44 tools, 3 tiers
    │   ├── monitor.py               ← SelfMonitor, 8 behavioral detectors
    │   ├── catalog.py               ← KnownIssuesCatalog + NVD refresh
    │   ├── ultraplan.py             ← ULTRAPLAN + scan_signals
    │   ├── workers.py               ← Coordinator + role-polymorphic swarm
    │   ├── verify.py                ← PoC gate, corroboration, skeptic
    │   ├── chain.py                 ← Attack graph, state machine, chains
    │   ├── fixer.py                 ← Patches, smoke test, CI workflow
    │   ├── speculation.py           ← COW overlay, predict, promote
    │   ├── harness.py               ← 8-phase orchestrator
    │   ├── cli.py                   ← scan, report, verify, baselines, calibrate
    │   └── enhancements/
    │       ├── nvd.py               ← P1.2: NVD API live catalog refresh
    │       ├── dedup_ledger.py      ← P1.3: Prior-scan dedup
    │       ├── cvss.py              ← P1.4: CVSS harmonic mean scoring
    │       ├── operator.py          ← P1.5: Mid-engagement steering
    │       ├── injection.py         ← P1.6: Prompt injection detection
    │       ├── fileguard.py         ← P1.7: FileRead malicious-content guard
    │       ├── constitutional.py    ← P2.6: Constitutional adherence grader
    │       ├── self_pref.py         ← P2.7: Self-preference bias test
    │       ├── petri.py             ← P2.8: Petri 2.0 behavioral comparison
    │       └── tripwire.py          ← P3.4: Sandbagging detection
    ├── tests/
    │   ├── test_audit.py            ← 5 tests: chain, tamper detection
    │   ├── test_gate.py             ← 7 tests: LOW/MEDIUM/HIGH tiers, scope
    │   ├── test_graph.py            ← 6 tests: CRUD, persistence
    │   ├── test_monitor.py          ← 4 tests: 8 detectors, strike halting
    │   └── test_catalog.py          ← 4 tests: embedded load, NVD graceful fail
    └── docs/                        ← 27-file documentation set
        ├── index.md
        ├── overview/
        ├── getting-started/
        ├── commands/                ← scan, report, verify, baselines, calibrate
        ├── concepts/                ← graph, audit, gate, monitor, swarm, chains
        ├── guides/
        ├── reference/
        ├── architecture/
        │   └── adr/                ← 4 Architecture Decision Records
        └── troubleshooting/
```

---

## Quick start

```bash
cd mythos-harness
pip install -e .

export ANTHROPIC_API_KEY=sk-ant-...
export GEMINI_API_KEY=AIzaSy...          # recommended second model

mythos scan --target . --live
```

For scanning your own codebase, see [mythos-harness/docs/guides/test-your-own-codebase.md](mythos-harness/docs/guides/test-your-own-codebase.md).

---

## What the reconstruction checks

The 12-component architecture, as described by the sources:

```
Layer 1 — Engagement Substrate     Layer 2 — Discovery & Verification   Layer 3 — Synthesis
─────────────────────────────────  ────────────────────────────────────  ──────────────────────
C1  Engagement Graph (SQLite)      C5  ULTRAPLAN (long reasoning call)   C10 Chain Builder
C2  Immutable Audit Log (SHA-256)  C6  Role-Polymorphic Worker Swarm     C11 Fixer + CI
C3  Risk-Classified Action Gate    C7  Cross-Model 2-of-3 Corroboration  C12 Speculation Layer
C4  Self-Monitor + Deliberative    C8  Executable PoC Verification Gate
    Alignment Gate                 C9  Variant Hunter + Known-Issue Dedup
```

**What the real Mythos does that this reconstruction cannot replicate:**
- Activation-level self-monitoring (sparse autoencoders on internal model representations) — the API does not expose activations
- The actual Mythos Preview model — restricted to Project Glasswing partners
- Distributed ephemeral VMs — the reconstruction runs in a single process

See [03_gap_analysis.md](03_gap_analysis.md) for the full gap analysis.

---

## Scoreboard: reconstruction vs. baselines

On MLflow v2.9.2 (13-entry CVE catalog), Fareed's original scoreboard:

| Mode | Real findings | False positives | Chain found | Fix proven |
|---|:---:|:---:|:---:|:---:|
| One-shot Sonnet 4.6 (no harness) | 4 | 1 | no | no |
| One-shot Gemini 2.5 Pro (no harness) | 3 | 0 | no | no |
| **12-component harness** | **11** | **0** | **yes** | **yes** |

The harness finds ~2.5× more real findings than the best bare-model baseline, produces zero false positives, and is the only approach that produces a verified attack chain and a deployable CI workflow.

---

## Key design decisions

| Decision | Rationale |
|---|---|
| `ask_fn` injected as parameter | Propagates `live` flag uniformly; enables mock testing without patching |
| `live=False` raises, not silently no-ops | A security scanner that silently returns zero findings is a false sense of security |
| Gemini via OpenAI-compatible endpoint | Zero new dependencies; routes through the same SDK path as GPT |
| SQLite for engagement graph | Zero infrastructure; portable; survives process restarts |
| Enhancements as optional imports | Core harness runs without any enhancement; enhancement failures don't cascade |
| Budget cap checked per swarm round | Simple; worst-case overshoot is bounded (~$0.10) |
| Sonnet 4.6 as default brain | 5× cheaper than Opus 4.7; strong enough for security scanning tasks |

Full rationale in [IMPLEMENTATION_NOTES.md](IMPLEMENTATION_NOTES.md) and [mythos-harness/docs/architecture/adr/](mythos-harness/docs/architecture/adr/).

---

## Claude Code session transcripts

The `.ignore/` directory contains the raw Claude Code session transcripts (`cc1_mythos.txt` through `cc6_mythos.txt`) — every tool call, decision, correction, and parallel agent dispatch. Reading them shows how Claude Code handles context window limits, multi-session continuity, and parallel agent workflows across a project of this scale.

---

## Credits

- **Fareed Khan** — [claude-mythos-architecture](https://github.com/FareedKhan-dev/claude-mythos-architecture): the reverse-engineered notebook this work builds on
- **Anthropic** — Claude Mythos Preview System Card (April 7, 2026)
- **Mozilla** — Behind the Scenes: Hardening Firefox with Claude Mythos Preview (May 7, 2026)
- **Daniel Stenberg** — Mythos finds a curl vulnerability (May 11, 2026)

This tutorial was produced entirely using Claude Code (claude-sonnet-4-6).
