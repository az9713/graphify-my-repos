# AGI → ASI: A Multi-Lens Deep Dive

A structured, multi-perspective analysis of Google DeepMind's position paper ***From AGI to ASI*** — and, just as importantly, a transparent record of the **method** used to design the analysis.

📄 **Paper:** [*From AGI to ASI*](https://www.alphaxiv.org/abs/2606.12683) — Genewein, Franklin, Lerchner, Orseau, Albanie, Bales, Wyeth, Chan, Gabriel, Leibo, Dafoe, Hutter, Graepel & Legg (Google DeepMind), arXiv `2606.12683`, June 2026.

---

## What this is

Most "summarize this paper" efforts produce one lossy pass. This repo instead asks: **what is the smallest set of prompts that extracts the maximum information, insight, and latent signal from a paper?** — and then executes that set as eight deep reports.

The work split into two layers:

1. **A methodology** — how a vague request for "orthogonal prompts" was interrogated, formalized into a 5-dimension model of *ways to read a text*, expanded to an exhaustive 25-prompt grid, collapsed to a 5-prompt spanning core, and finally tuned to an 8-prompt set sitting at the knee of the information-per-prompt curve. The full journey (including the dead ends and the honest admission that the first set was generated bottom-up, not from first principles) is in [`00_METHODOLOGY_prompt-design-journey.md`](00_METHODOLOGY_prompt-design-journey.md).

2. **Eight executed reports** — the chosen prompt set run against the paper, each ~2–3 pages.

## The method in one diagram

```
"orthogonal prompts"  →  13 sampled probes  →  5-dimension model (A·B·C·D·E)
   →  25-cell grid (exhaustive)  →  P1–P5 (minimal spanning)  →  P1–P5 + {E5, Re2, E4}
```

The five dimensions a prompt can vary along:

| Dim | Meaning | Values |
|-----|---------|--------|
| **A** | Epistemic stance | reproduce · decompose · evaluate · relate · generate |
| **B** | Vantage | internal · external |
| **C** | Abstraction layer | object · meta |
| **D** | Representational mode | qualitative · quantitative · formal · relational |
| **E** | Temporal frame | static · dynamic · longitudinal |

The final 8 = a complete **spanning** core (P1–P5, every dimension touched once) **plus** the three highest *latent-signal* cells the spanning logic structurally under-serves (E5, Re2, E4). See the methodology doc for the five explicit selection criteria.

## The reports

| File | Prompt · cell | Headline finding |
|------|---------------|------------------|
| [`01_P1_faithful-reconstruction.md`](01_P1_faithful-reconstruction.md) | **P1** · REPRODUCE | Faithful baseline — the paper on its own terms, uncompressed. |
| [`02_P2_growth-dynamics-decomposition.md`](02_P2_growth-dynamics-decomposition.md) | **P2** · DECOMPOSE | The outcome hinges on two *unmeasured* couplings, not the headline ~10×/yr compute growth. |
| [`03_P3_redteam-and-rhetoric.md`](03_P3_redteam-and-rhetoric.md) | **P3** · EVALUATE·meta | Thesis is near-unfalsifiable by hedge-density; the "assume alignment is solved" bracket does the heaviest lifting. |
| [`04_P4_theoretical-and-discourse-positioning.md`](04_P4_theoretical-and-discourse-positioning.md) | **P4** · RELATE·formal | Distinctive move = grounding forecasts in an *incomputable* ideal (AIXI); sits between Bostrom-caution and Kurzweil-determinism. |
| [`05_P5_research-agenda-and-tripwires.md`](05_P5_research-agenda-and-tripwires.md) | **P5** · GENERATE | 25 named research projects ranked by tractability × leverage + a 1–3 yr monitoring-tripwire dashboard. |
| [`06_E5_taxonomy-completeness.md`](06_E5_taxonomy-completeness.md) | **E5** · EVALUATE·completeness ⭐ | Two highest-impact *missing* frictions: alignment-as-capability-gate and the verification gate. |
| [`07_Re2_forecast-reconciliation.md`](07_Re2_forecast-reconciliation.md) | **Re2** · RELATE·quant ⭐ | An internal **3×-vs-6×/yr algorithmic-efficiency inconsistency** is the key numeric fault line. |
| [`08_E4_aixi-bridge-critique.md`](08_E4_aixi-bridge-critique.md) | **E4** · EVALUATE·formal ⭐ | "log-loss ≈ universal compression" grades *conjectured-leaning-analogical*; the bridge licenses "ASI permitted," not "ASI favored." |

⭐ = high-latent-signal additions beyond the spanning core.

## The cross-cutting finding

Read together, the three ⭐ reports converge on one meta-observation the paper itself never states: **its optimism rests on (i) quantities it admits are unmeasured, (ii) a taxonomy that omits the gating frictions, and (iii) a formal bridge that is analogical, not proven.**

## How to use

- **Just want the paper's content?** Read `01_P1_…` (it follows the paper's own Section 1 summary instructions).
- **Want to know if you can trust it?** Read `03_P3_…`, `07_Re2_…`, `08_E4_…`.
- **Want to act on it?** Read `05_P5_…`.
- **Want to reuse the method on another paper?** Read `00_METHODOLOGY_…` — it ends with a one-line reusable decision rule and eight transferable principles.

## Scope & attribution

- The **analysis and methodology in this repo are original** to this project.
- The **paper itself is © its authors / Google DeepMind**; read it at the [link above](https://www.alphaxiv.org/abs/2606.12683). The source PDF and its extracted full text are **deliberately not redistributed here** — this repo contains commentary, not the work it comments on.
- Reports were drafted with AI assistance and reflect a point-in-time reading; treat quantitative cross-checks (esp. `07_Re2_…`) as analyst estimates, not verified figures.

---

🤖 Analysis generated with [Claude Code](https://claude.com/claude-code).
