# Simple Agent Harness

A three-role coding agent harness: **Planner -> Generator <-> Evaluator**.

Open-source, self-hostable Python implementation that synthesizes the best-validated lessons from mini-coding-agent, pi, Claude Code, Anthropic's three-agent pattern, and Vercel's tool-reduction research into a single general-purpose coding agent.

---

## What makes it different

Every major coding agent harness as of 2026 has at least one of these failure modes:

| Harness | Core limitation |
|---------|----------------|
| mini-coding-agent | 6-step cap, single agent, context clipping, no evaluation |
| pi | Single agent, no eval feedback, context control is developer burden |
| Claude Code | Closed source, opaque compaction, monolithic |
| Anthropic 3-agent | No open implementation, web-app-only |
| Managed Agents | Cloud-only, no self-hosted option |

This harness unifies three advances no single prior implementation combined:

1. **Role separation** — Planner, Generator, and Evaluator each run in isolated contexts with purpose-specific tool sets
2. **Context resets, not compaction** — each sprint starts fresh from structured handoff artifacts (`spec.md`, `eval.md`, `memory.md`), eliminating context drift
3. **Minimal tool set** — 4 tools (bash, read_file, write_file, search), validated by Vercel's finding that stripping from 16 to 3 tools improved success rate from 80% to 100%

---

## How it works

```
User task
    |
[PLANNER] --> spec.md (feature list with acceptance criteria)
                  |
         .--------+--------.
         |                  |
    [GENERATOR] <-- spec.md + eval.md + memory.md
         |                  |
         |            [EVALUATOR] --> score >= 0.7? mark done : retry
         |                  |
         `------------------'
                  |
         all features [x]
                  |
                done
```

The harness is stateless — all state lives in a session directory (`~/.harness/sessions/<id>/`) as plain files and a SQLite event log. Sessions can be resumed after any interruption.

---

## Quickstart

```bash
# Install
git clone https://github.com/az9713/simple-agent-harness
cd simple-agent-harness
python -m venv .venv
source .venv/Scripts/activate   # Windows Git Bash
# source .venv/bin/activate     # macOS/Linux
pip install -e .
pip install pytest

# Set API key
export ANTHROPIC_API_KEY=sk-ant-...

# Run
mkdir my-task
python -m harness run "write a fizzbuzz function in fizzbuzz.py and test it with pytest" --dir my-task

# Inspect
python -m harness list
python -m harness inspect <session-id>
```

---

## CLI

```
python -m harness run "<task>" [--dir PATH] [--max-sprints N] [--quiet]
python -m harness resume <session-id> [--dir PATH]
python -m harness inspect <session-id>
python -m harness list
```

Override the model:

```bash
export HARNESS_MODEL=claude-haiku-4-5-20251001   # cheaper, for testing
export HARNESS_MODEL=claude-opus-4-6             # more capable
```

Default model: `claude-sonnet-4-6`.

---

## File structure

```
harness/
  artifacts.py   # SpecArtifact and EvalArtifact Pydantic models
  cli.py         # argparse entry point
  harness.py     # stateless run_turn() loop
  roles.py       # PLANNER, GENERATOR, EVALUATOR configs
  session.py     # SQLite event log + artifact store
  tools.py       # bash, read_file, write_file, search
docs/            # full documentation
```

---

## Test run results

First successful end-to-end run (session `c91098bf`, 2026-04-10):

- Task: `write a fizzbuzz function in fizzbuzz.py and test it with pytest`
- Result: 23/23 tests passing
- 2 sprints, 9 API calls, 12 tool calls, ~63 seconds
- Both features scored 100% by the Evaluator

Full report: [`docs/background/test-run-report.md`](docs/background/test-run-report.md)

---

## Documentation

| Doc | Purpose |
|-----|---------|
| [docs/index.md](docs/index.md) | Navigation hub |
| [docs/getting-started/quickstart.md](docs/getting-started/quickstart.md) | Working in under 10 minutes |
| [docs/overview/what-is-this.md](docs/overview/what-is-this.md) | Mental model and architecture |
| [docs/architecture/comparative-analysis.md](docs/architecture/comparative-analysis.md) | vs mini-coding-agent, pi, Claude Code, Anthropic 3-agent |
| [docs/background/research-findings.md](docs/background/research-findings.md) | OpenAI, LangChain, Vercel, Anthropic synthesis |
| [docs/background/design-session.md](docs/background/design-session.md) | Full design history and decisions |

---

## Requirements

- Python 3.10+
- `anthropic>=0.40.0`
- `pydantic>=2.0`
- Anthropic API key

---

## License

MIT
