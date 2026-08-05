# jacobian-lens-lab

**Experiments on Anthropic's Jacobian lens: emergence with scale, pretraining
ontogeny, and J-space geometry — all run on one consumer laptop.**

### 📖 [Read the full illustrated report (live page)](https://az9713.github.io/jacobian-lens-lab/)

The report is written for readers new to the topic — it builds the background
from zero (residual streams, the global-workspace claim, what a Jacobian lens
is, and a geometric mental model for rank / effective rank / rotation) before
presenting results.

---

## What this is

Anthropic's paper [*Verbalizable Representations Form a Global Workspace in
Language Models*](https://transformer-circuits.pub/2026/workspace/index.html)
introduces the **Jacobian lens**: read a transformer's middle layer by
transporting its residual vector into the final layer's basis with the
model's own averaged Jacobian, then decoding with the model's own unembedding
— `lens_l(h) = unembed(J_l · h)`. The paper demonstrates a mid-network
"workspace" of word-readable concepts on Claude-class and large open models.

This repo points the same instrument at territory the paper doesn't visit:
**small models, pretraining checkpoints, and the geometry of the lens
matrices themselves.** It contains a small library (`jlab/`) extending the
[reference implementation](https://github.com/anthropics/jacobian-lens) —
an eval harness, steering/swap interventions, J-space geometry tools, and a
"three clocks" visualization suite (generation time · depth · training
time) — plus one runnable script per experiment.

## Findings (novel to our knowledge — hedges and caveats in the report)

1. **The J-lens advantage is emergent with scale.** Absent at 124–160M
   (the logit lens is near-optimal there, and averaged transport *actively
   harms* readout on tied-embedding models like GPT-2), partial at
   Pythia-410M, dominant by Qwen3.5-0.8B (4.4× on multihop eval).
2. **Stated content before implied content.** Transport of directly-stated
   content arrives between 160M→410M; the advantage on implied content
   arrives only by 0.8B.
3. **A pretraining ontogeny result (Clock 3).** Fitting a lens at 8
   Pythia-160M training checkpoints: **no J-lens workspace forms at any
   point in training** at this scale — while the same pipeline cleanly shows
   *direct* late-layer readability growing (a null with a built-in positive
   control). The paper's dynamics work covers base-vs-post-trained only.

   ![Clock 3](docs/figs/clock3_lograank_logit.png)

4. **A geometric boundary marker (Clock 2).** Healthy lenses show a
   low-rotation plateau through the middle layers and one sharp hand-off
   spike — at *exactly 2/3 depth in both Qwen3.5 sizes* — coinciding with
   where probe content snaps to rank 1. Weak lenses have no plateau at all,
   suggesting **median adjacent-layer rotation as a workspace-presence score
   computable from a lens file alone** (no model, no forward passes).

   ![Rotation profiles](docs/figs/rotation_profiles.png)

5. **The estimator matters on weak models.** A same-cost last-position
   estimator variant improves the GPT-2 J-lens up to 7× at early layers —
   the reference implementation's "both estimators work" understates this
   below the workspace threshold.

## Repo tour

| path | what |
|---|---|
| `jlab/` | library: `evals` (pass@k), `interventions` (steer/swap), `geometry` (SVD, rotation, band detection), `clocks` (3-clock viz), `ontogeny` (checkpoint loop), `estimators` (last-self variant) |
| `phase_b.py` … `phase_f.py` | one runnable script per experiment |
| `REPORT.md` | full experimental log: hypotheses H1–H8, every result, synthesis |
| `AUTONOMOUS-RUN.md` | process chronicle, warts and all — wrong hypotheses, flawed controls, crashes, recoveries |
| `PLAN.md` | the phase plan as it evolved |
| `docs/` | the illustrated report (`index.html`, served via Pages) + learning-path docs |
| `tests/` | CPU test suite vs. the upstream TinyDecoder (seconds to run) |

## Validate our claims — pick your tier

We actively invite replication (and contradiction — that's the valuable
kind). Environment used: Python 3.13, torch 2.11 (CUDA 12.8), transformers
5.14; exact tested versions are pinned in `pyproject.toml`'s comments.
Setup for all tiers:

```bash
git clone https://github.com/anthropics/jacobian-lens
git clone https://github.com/az9713/jacobian-lens-lab
cd jacobian-lens-lab
pip install -e ../jacobian-lens -e .[dev]
pytest        # ~5 s on CPU — 7 tests must pass before anything else matters
```

| tier | command | cost | validates | expect |
|---|---|---|---|---|
| 1 | `python phase_f.py` | ~5 min, CPU only, downloads lens *files* not models (~1 GB) | finding 4 (rotation spike) | qwen3.5-0.8b & 2b spike at L14→15, ~45°, ratio ≥3.5; gpt2/pythia-70m medians >25° |
| 2 | `python phase_b.py` | ~30–60 min, any 8 GB machine | finding 1 (0.8B endpoint) | J-lens beats logit lens at every probed layer; multihop pass@50 ≥3× logit lens |
| 2 | `python phase_c.py` | ~20 min (fits a small lens) | finding 5 (estimator) | last-self estimator ≥3× better than standard at L2/L4 on GPT-2 |
| 3 | `python -m jlab.ontogeny` | GPU ~30–45 min / CPU overnight; resumable | finding 3 (ontogeny null) | binary hit@10 ≈ 0 at all checkpoints; logit-lens log-rank heatmap shows late-layer gradient, J-lens shows none |
| 3 | `python phase_d.py` | GPU ~25 min / CPU hours | findings 1–2 (410M midpoint) | J-lens wins probe at all layers; logit lens still wins multihop |

Tolerances: exact ranks vary with dtype/hardware (we ran bf16 on GPU, fp32
on CPU); the *orderings and ratios* above are the claims. If your run
contradicts one, please open a GitHub issue with your environment and
numbers — contradictions are more valuable to us than confirmations.

Everything ran on an i5-12450H laptop, 32 GB RAM, RTX 3050 (4 GB). Fitted
lenses land in `out/` (git-ignored); pre-fitted lenses for 38 models are
published by [Neuronpedia](https://huggingface.co/neuronpedia/jacobian-lens).

## Provenance

Developed in an AI-pair-programmed session (Claude Code); the later
experimental phases ran fully autonomously overnight under pre-agreed
decision rules — `AUTONOMOUS-RUN.md` documents the process honestly,
including the mistakes. Code is Apache-2.0 (see `LICENSE`/`NOTICE`);
`tests/tiny.py` is from Anthropic's jlens (Apache-2.0). Not affiliated with
Anthropic or Neuronpedia.
