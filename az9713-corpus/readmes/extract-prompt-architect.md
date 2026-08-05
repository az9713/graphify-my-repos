# Minimal Prompts, Maximal Extraction

*A development journey: how do you build the **smallest set of prompts** that pulls the **most strategic signal** out of a dense source? It ended in a reusable Claude Code skill — `extraction-prompt-architect` — which we then ran on the article that started it all.*

> ### 📄 Source article
> **SemiAnalysis — [*US Grid Constraints: Towards 40GW+ of Behind-The-Meter Datacenter by 2028?*](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw)**
> Every worked example in this repo extracts from this note. The article itself is paywalled/copyrighted and is **not** redistributed here — only the prompts and the derived analysis.

---

## The question

Given a meaty document — a research note, a paper, a filing — most "analyze this" prompts return generic sludge. The interesting problem isn't writing *more* questions; it's finding the **minimal set that captures ~80% of the value**, and being able to **justify every prompt that made the cut and every one that didn't**.

This folder is the worked record of solving that, end to end.

## The journey (in brief)

1. **A source + a prompt pack.** We started with a paywalled SemiAnalysis article — [*US Grid Constraints: Towards 40GW+ of Behind-The-Meter Datacenter by 2028?*](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw) — plus a prior ChatGPT session that had generated **15 extraction prompts** across many "dimensions."
2. **Assess, don't admire.** We graded the 15 prompts on yield, orthogonality, source-fit, and falsifiability — and found two genuine blind spots no dimension had covered: **provenance** (facts vs. the vendor's own model outputs) and **author-incentive / reflexivity**.
3. **Distill.** Using an explicit, auditable 80/20 criterion, we cut 15 → a **7-prompt minimal set**, with a written ledger of what each omission costs. *(See `prompt-distillation-report.md`.)*
4. **Generalize into a skill.** The repeatable method became a 6-step workflow — the key insight being a dedicated **blind-spot pass** that *generates* the prompts dimensions miss. *(See `.claude/skills/extraction-prompt-architect/`.)*
5. **Test it.** We sanity-tested the skill on two unlike sources (an advice essay, an AGI forecast); it adapted in opposite directions and beat a no-skill baseline.
6. **Dogfood it.** Finally we pointed the finished skill back at the original article. *(See `extraction-prompts_us-grid-btm.md`.)*

## The skill: `extraction-prompt-architect`

Given a source, it designs the **instrument** (a distilled prompt set) — it doesn't run it. Six steps:

**0. Profile** the source type and bind the reader's decision → **1. Derive** orthogonal dimensions → **2. Generate** the maximal prompt set → **3. Blind-spot pass** (provenance, incentive, ontology, recall, base-rate) → **4. Distill** to a minimal set against a 3-test criterion (yield × orthogonality × load-bearing) → **5. Explain** every include/exclude in a ledger.

Two ideas do most of the work: the **minimal set is relative to what you'll do with it** (a trader's set ≠ an operator's), and *"maximal" isn't maximal until you check what no dimension named.*

## Applied to the SemiAnalysis article

Running the skill on the source produced an 8-prompt set tuned to an *evaluate-to-position* decision. Notably, Step 0 caught that the article is **split-paywalled** — the named investment calls are cut (so that prompt *starves*), but the **ERCOT co-location deal table is fully available** (so that prompt is the richest in the set). The result grades SemiAnalysis's *own prior calls* against later reality rather than taking the thesis on faith.

## What's in this repo

| Path | What it is |
|------|-----------|
| `README.md` | This overview. |
| `DEVELOPMENT-JOURNEY.md` | The full audit trail — every decision fork, mistake, and correction. |
| `prompt-distillation-report.md` | The 15 → 7 distillation of the prior prompt pack (criterion, two new blind-spot prompts, exclusion ledger). |
| `extraction-prompts_us-grid-btm.md` | The skill **applied to the article** → a fresh 8-prompt set (the design). |
| `extraction-output/` | The 8-prompt set **run** against the article — 8 matched prompt+output files plus an index. |
| `.claude/skills/extraction-prompt-architect/SKILL.md` | The reusable skill (the generalized 6-step method). |

**Source inputs — described here but not redistributed** (the article is paywalled/copyrighted; the raw transcripts contain contact info): the SemiAnalysis article [*US Grid Constraints: Towards 40GW+ of Behind-The-Meter Datacenter by 2028?*](https://newsletter.semianalysis.com/p/us-grid-constraints-towards-40gw), and the prior ChatGPT session that produced the original 15 prompts.

## Using the skill

It's installed in this project (`.claude/skills/`) and globally. Trigger it by handing Claude a dense source and asking for an extraction plan — e.g. *"give me the smallest set of prompts to pull the most out of this report,"* or invoke `/extraction-prompt-architect`. It returns a distillation report; ask it to **run** the set as a separate step.

## License

MIT — see [`LICENSE`](LICENSE). Covers the original work here (the skill, the write-ups, and the prompt sets). The analyzed SemiAnalysis article is third-party, copyrighted, and **not** redistributed in this repo.
