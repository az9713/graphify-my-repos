# LLM Molecule Benchmark

> **No frontier LLM has ever correctly designed a 22-atom ligand. This benchmark proves it — automatically, reproducibly, and for free.**

A rigorous, open-source benchmark that tests whether large language models can perform **constrained molecular design** — generating molecules that satisfy exact chemical constraints. Built around a real challenge used by [Prof. Heather Kulik](https://kulik.mit.edu/) (MIT Chemical Engineering) to probe every new LLM.

[![Tests](https://img.shields.io/badge/tests-62%20passing-brightgreen)](#running-tests)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue)](https://python.org)
[![License](https://img.shields.io/badge/license-MIT-green)](LICENSE)
[![Cost](https://img.shields.io/badge/full%20benchmark-~%240.15-lightgrey)](#cost)

---

## The Problem

Prof. Heather Kulik (MIT) has run the same test on every new LLM since the field took off:

> *"Please design me a ligand that has 22 atoms. I can never get an answer that has 22 atoms."*
> — Prof. Heather Kulik, [Latent Space podcast](https://www.youtube.com/watch?v=KSCCKCz2x04)

This is not a trick question. Designing a 22-atom bidentate ligand for iron coordination is a **routine task** for a second-year chemistry graduate student. It requires no creativity — just structural reasoning. Yet no frontier LLM consistently succeeds.

This project turns that informal test into a systematic, automated benchmark.

---

## Why This Matters

LLMs are rapidly being deployed in scientific workflows. Understanding precisely *where* they fail — not just that they fail — is essential for using them responsibly.

The Kulik test reveals a specific, important gap: **LLMs cannot reliably satisfy exact structural constraints in molecular design**. They possess declarative knowledge (they know what a ligand is, what Fe(II) means, what a donor atom is) but lack the combinatorial reasoning to generate a molecule that simultaneously satisfies multiple explicit constraints.

This is not a knowledge problem. It is a **constraint satisfaction problem** — and it is one of the most practically important failure modes in AI for science.

---

## What This Benchmark Does

It sends the same constrained molecular design prompts to multiple LLMs and grades each response using [RDKit](https://www.rdkit.org/) — the standard open-source chemistry toolkit. No human expert required. No ambiguity in the grade.

### The 5 Challenge Levels

| Level | Challenge | What's tested |
|---|---|---|
| **L1** | Valid Molecule | Can the model output valid SMILES at all? |
| **L2** | Exact Atom Count (10, 15, 22, 30) | Can it count non-hydrogen atoms exactly? |
| **L3** | Count + Composition | 22 atoms AND exactly 2 nitrogen atoms |
| **L4** | **The Kulik Challenge** | 22 atoms, 2 N-donor atoms, bidentate Fe(II) ligand |
| **L5** | Multi-Constraint | Atom count + MW window + aromatic ring + LogP range |

Each challenge has machine-verifiable pass/fail criteria. No interpretation required.

### Why LLMs Fail

LLMs generate **tokens**, not **atoms**. Counting atoms in a SMILES string requires parsing a molecular graph:
- Implicit hydrogens are inferred from valence rules, not written: `CCO` (ethanol) has 3 heavy atoms, not 1
- Ring-closure digits are structural markers, not atoms: `c1ccccc1` (benzene) has 6, not 8
- Brackets mix charges, isotopes, and atom types: `[13C]`, `[NH4+]`, `[Fe]`

A model generating SMILES character-by-character has no natural mechanism for counting graph nodes. It pattern-matches to training data — and for bidentate N-donor ligands, training data is dominated by bipyridine and phenanthroline, both with 12 heavy atoms, not 22.

---

## Leaderboard

Results from the latest benchmark run (3 trials per model, `temperature=0.0`):

<!-- LEADERBOARD_START -->

_Run the benchmark to generate results. See [Quickstart](#quickstart) below._

<!-- LEADERBOARD_END -->

**Score per cell**: `passes/trials (avg score)`.
Score = 0.25 valid SMILES + 0.15 connected molecule + 0.50 constraints satisfied + 0.10 novelty.

---

## Quickstart

**Requirements:** Python 3.10+, ~500 MB disk. No GPU.

```bash
# 1. Install
git clone https://github.com/az9713/llm-molecule-benchmark
cd llm-molecule-benchmark
pip install -r requirements.txt

# 2. Verify (no API keys needed)
python -m pytest tests/ -q
# Expected: 62 passed

# 3. Set API keys
cp .env.example .env
# Edit .env — add keys for the providers you want to test

# 4. See what would run and estimated cost
python run_benchmark.py --dry-run

# 5. Quick test (free with Google's API)
python run_benchmark.py --models gemini-2.5-flash --challenges L1_valid --trials 1

# 6. Full benchmark
python run_benchmark.py

# 7. Generate leaderboard
python generate_leaderboard.py --update-readme
```

---

## Cost

The full benchmark (4 models × 8 challenges × 3 trials = 96 API calls) costs approximately:

| Model | Est. cost |
|---|---|
| `gpt-4.1` | ~$0.05 |
| `claude-sonnet` | ~$0.08 |
| `gemini-2.5-flash` | ~$0.01 |
| `llama-4-maverick` | ~$0.01 |
| **Total** | **~$0.15** |

Use `--dry-run` to verify the estimate before spending anything. Google Gemini has a free tier; Together AI provides $5 free credit on sign-up.

---

## Models Included

| Alias | Model | Provider |
|---|---|---|
| `gpt-4.1` | GPT-4.1 | OpenAI |
| `gpt-4.1-mini` | GPT-4.1 Mini | OpenAI |
| `claude-sonnet` | Claude Sonnet 4 | Anthropic |
| `claude-haiku` | Claude Haiku 4 | Anthropic |
| `gemini-2.5-flash` | Gemini 2.5 Flash | Google |
| `gemini-2.5-pro` | Gemini 2.5 Pro | Google |
| `llama-4-maverick` | Llama 4 Maverick | Together AI |
| `llama-4-scout` | Llama 4 Scout | Together AI |

Adding a new model: one line in `benchmark/config.py`. See [Adding Models](#adding-models-and-challenges).

---

## CLI Reference

```bash
# List all models and challenges
python run_benchmark.py --list

# Run specific models
python run_benchmark.py --models gpt-4.1 claude-sonnet

# Run specific challenges
python run_benchmark.py --challenges L4_kulik_22 L3_n2_count_22

# More trials
python run_benchmark.py --trials 5

# Resume interrupted run (default: on)
python run_benchmark.py

# Re-run from scratch
python run_benchmark.py --no-resume
```

---

## How Scoring Works

Each LLM response is scored 0.0 – 1.0:

| Component | Weight | Criterion |
|---|---|---|
| Valid SMILES | 0.25 | RDKit can parse it |
| Chemical reasonableness | 0.15 | Connected, valid valences |
| Constraints satisfied | 0.50 | Fraction of challenge constraints met |
| Novelty | 0.10 | Not a common textbook molecule |

`overall_pass` is a binary flag — `true` only when every constraint is satisfied.

A model returning bipyridine (the most common LLM response to the Kulik Challenge) scores **~0.60**: valid SMILES ✓, connected ✓, 2 nitrogens ✓, 2 N-donors ✓ — but wrong atom count ✗ (12 atoms, not 22), and not novel ✗.

---

## Adding Models and Challenges

### New model

Add to `benchmark/config.py`:
```python
MODEL_MAP["my-model"] = "provider/litellm-model-string"
```

### New challenge

Add to `benchmark/challenges.py`:
```python
Challenge(
    id="L3_sulfur_15",
    level=3,
    name="15 Atoms, 2 Sulfurs",
    description="15 heavy atoms with exactly 2 sulfur atoms.",
    prompt=(
        "Generate a molecule with exactly 15 heavy atoms and exactly 2 sulfur "
        "atoms. Respond with ONLY the SMILES string, nothing else."
    ),
    constraints={
        "valid_smiles": True,
        "is_connected": True,
        "heavy_atom_count": 15,
        "element_count": {"S": 2},
    },
)
```

Supported constraint keys: `valid_smiles`, `is_connected`, `heavy_atom_count`, `element_count`, `nitrogen_donors`, `has_aromatic_ring`, `mw_range`, `logp_range`.

---

## Documentation

Full documentation lives in [`docs/`](docs/):

| Document | Contents |
|---|---|
| [`docs/1_material_science.md`](docs/1_material_science.md) | Materials science background: atoms, SMILES, ligands, coordination chemistry, the Kulik Challenge |
| [`docs/2_ai_role.md`](docs/2_ai_role.md) | Role of AI in materials science, why LLMs fail at molecular design, what this benchmark measures |
| [`docs/3_user_guide.md`](docs/3_user_guide.md) | Full setup guide, expected results, cost table, troubleshooting |

---

## Attribution

This benchmark is directly motivated by **Prof. Heather Kulik**'s research and her public discussion of LLM limitations in molecular design, as shared in the [Latent Space podcast interview](https://www.youtube.com/watch?v=KSCCKCz2x04).

Prof. Kulik's group develops open-source tools for computational materials chemistry:
- [molSimplify](https://github.com/hjkgrp/molSimplify) — transition metal complex generation and screening
- [MOFSimplify](https://github.com/hjkgrp/MOFSimplify) — metal-organic framework screening

---

## License

MIT — see [LICENSE](LICENSE).
