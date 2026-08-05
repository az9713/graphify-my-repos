# Personal Knowledge Base (Cerebras-style)

One Postgres table, hybrid retrieval (vector + FTS + RRF), MCP interface, four Claude Code skills. The full development journey — architecture, algorithms, incidents, lessons — is the series in [docs/](docs/00-index.md). (The working SPEC/JOURNAL/EVAL artifacts referenced there live in the author's private repo; they enumerate a personal corpus.)

## Inspiration

- **Video:** [Cerebras Killed Notion, Obsidian, and Your "Second Brain"](https://www.youtube.com/watch?v=eCx3SSCcISo) — the trigger for this project
- **Blog:** [How We Built Our Knowledge Base](https://www.cerebras.ai/blog/how-we-built-our-knowledge-base) (Cerebras, Jul 2026) — the engineering design this system reverse-engineers and adapts for a single user

## How it was built

**Largely autonomously, by an AI coding agent in Claude Code.** The human set direction, made
the gated decisions (budget, credentials, scope, taste), and field-tested; the agent did the rest
end-to-end under a documentation-and-QA contract (SPEC.md §15): spec-first design, its own unit +
integration tests, self-initiated security and code reviews (whose findings it then fixed), an
eval suite it had to keep green, and an append-only journal of every issue and decision fork.
Human touchpoints during the entire phase 1–5 implementation numbered roughly a dozen — approving
spend, supplying an API key, answering "which of these is genuinely absent from your corpus," and
interrupting exactly the right rabbit holes. Everything else — including building, measuring, and
then *deleting* a spec-mandated feature that benchmarked worse — ran without a human in the loop.
The warts (a destroyed $10 of embeddings, silently-wrong denylists, a 15-minute feed the human
called "not a viable product") are documented, not hidden: see [docs/05](docs/05-build-log.md)
and [docs/06](docs/06-field-testing.md).

**Models used** (Claude, via Claude Code — the human switched tiers deliberately during the run):

| Model | Used for |
|---|---|
| **Fable 5** (primary, ~85% of the work) | Reverse-engineering the blog; SPEC v1; the blindspot/hardening pass; the entire autonomous phase-1 build (schema, connectors, embedding + spend meter, retrieval, MCP server, reviews, eval); the local-embedding pivot; all field-test fixes (identifier lane, `ingest_subtree`); the four skills; the docs series (written by parallel Fable fork-agents) |
| **Opus 4.8** (incl. 1M-context) | Spec revision/consistency passes, the PRD/MVP assessment, the gbrain relationship analysis, and long monitoring stretches of the embedding runs where a large context window mattered |
| **Sonnet 5** (one brief stint, medium effort) | The hardware probe (GPU/VRAM check) and recording the embedding-provider decision it informed |

The division of labor emerged naturally: the frontier model for design, autonomous building, and
debugging; Opus for review-and-monitor stretches; Sonnet for a quick mechanical probe. Embeddings
themselves run on **local Ollama (nomic-embed-text)** — no Claude or paid API is involved in
serving queries; the consuming Claude Code session is the synthesizer by design (SPEC §9).

## Components

```
kb-postgres (Docker)     pgvector/pgvector:pg16, 127.0.0.1:5433, volume kb_pgdata
kb/config.py             all knobs: denylists, tiers, priorities, $10 spend cap (G2)
kb/connector_fs.py       walk <projects> -> chunk rows (tier by .kb-tier marker, else 90d mtime)
kb/embed.py              embed pending rows by priority under spend cap; HNSW via halfvec(3072)
kb/retrieval.py          vector + FTS -> RRF(k=60) -> per-file diversity cap -> evidence rows
kb/connector_web.py      curated urls.txt -> fetch/strip/chunk -> rows (append-only, no LLM)
kb/health.py             kb_health (H6): per-source recency, embed backlog vs FTS-only-by-design, warnings
kb/primitives.py         search_code (FTS over code), what_knows (topic -> which projects cover it)
kb/retrieval.py          ...+ context expansion: matched chunk pulls its neighbors (SPEC §8 step 5)
kb/mcp_server.py         MCP tools: search, search_code, what_knows, kb_health (in .mcp.json)
kb/evalrun.py            EVAL.md runner: 31 positives hit-rate@10 + 3 negatives
tests/test_kb.py         unit tests (no DB/API): RRF math, denylists, chunking, priorities, cap
```

## Quickstart — the four-skill interface

The uniform interface is Claude Code skills (in `~/.claude/skills/`), usable from any directory:

| Skill | When | What it does |
|---|---|---|
| `/install-cerebras-brain` | first time / broken | full stack install-or-repair (runs `setup.ps1`) |
| `/start-cerebras-brain` | daily, idempotent | starts Docker + Postgres + Ollama, prints health (runs `brain.ps1 -NoLaunch`) |
| `/ask-cerebras-brain` | anytime | recall with citations via the `kb` MCP tools |
| `/feed-cerebras-brain <folders/URLs>` | after adding/changing material | ingest + embed. Folders MUST be under `<projects>` (refused otherwise) |

Daily flow: `/start-cerebras-brain` once, then ask/feed freely. The scripts (`setup.ps1`,
`brain.ps1`) are the version-controlled machinery the skills call — `brain.ps1` without
`-NoLaunch` also works standalone from a terminal to check deps and open a session.

## Operate

```powershell
# start (Docker Desktop must be running; container auto-restarts with it)
docker start kb-postgres

# ingest (resumable; unchanged files keep their embeddings)
.\.venv\Scripts\python.exe -c "from kb.connector_fs import ingest; from kb import config; print(ingest(config.PROJECTS_ROOT))"

# embed pending rows (local/free by default; halts at KB_SPEND_CAP_USD if provider is openai)
.\.venv\Scripts\python.exe -c "from kb.embed import embed_pending, ensure_hnsw_index; print(embed_pending()); ensure_hnsw_index()"

# run acceptance eval
.\.venv\Scripts\python.exe -m kb.evalrun

# unit tests
.\.venv\Scripts\python.exe -m pytest tests -q
```

MCP: `search` and `kb_health` are available to any Claude Code session in this directory via `.mcp.json`.

## Status (2026-07-20, phase 1 complete)

| | |
|---|---|
| Corpus | 632,743 rows from 4,127 project folders (629k chunks + 3,723 project summaries) |
| Embeddings | **Local & free** — Ollama `nomic-embed-text`, 768d, ~35 rows/s. Run in progress covers all 272,757 docs+summaries (~2.5 h, $0) |
| Code/data rows | ~360k `_MAIN` chunks intentionally unembedded — FTS beats vectors for identifiers, flags, error strings |
| Eval | **29/31** positives hit-rate@10, **3/3** negatives — *identical to the paid OpenAI baseline* |
| Tests | 17/17 (13 unit + 4 DB convergence) |
| Spend | $9.99 historical (OpenAI, vectors since lost — see JOURNAL incident); **$0 ongoing** |

Switch providers any time with `KB_EMBED_PROVIDER=openai|ollama` — model, dimensions, index type, and
metering all follow automatically (H1). Local requires `ollama serve` running.

Retrieval lanes fused by RRF (k=60): vector (HNSW/halfvec) · FTS-AND · FTS-OR (w 0.5) · project-summaries · IDF rare-token (w 1.5).

**To embed more:** raise `KB_SPEND_CAP_USD` and re-run the embed command below — it resumes in priority order.

## Data locations & knobs

- Vectors + rows: Docker volume `kb_pgdata` (recomputable — the raw files are the asset, per SPEC H8)
- Spend ledger: `spend_log` table; cap in `KB_SPEND_CAP_USD` env (default 10.0)
- Pin a folder's tier: drop `.kb-tier` file (`full`/`summary`) in its root — never name-based
- Dormant sources (x, gmail, gdocs, slack): `data_sources.enabled=false`; activate by flipping the flag

## Adding a connector

Emit rows matching the `embeddings` schema (SPEC §7): `fetch(watermark) -> (rows, new_watermark)`, one `data_sources` entry. Everything downstream (retrieval, MCP, eval) works unchanged.
