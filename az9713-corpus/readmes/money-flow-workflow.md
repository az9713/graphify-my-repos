# Money-Flow Workflow

A reproducible research workflow that turns one a16z essay into a ranked, falsified
shortlist of **compute + energy** investment opportunities — built as a *pipeline of
prompts*, not a pile of essays.

> **This is investment _research_, not advice.** Every figure is sourced or flagged
> (⚠). Numbers are point-in-time (gathered June 2026). Do your own verification.

---

## 1. Where it started

The seed is a single article: **["The money flow is the moat"](https://a16zcrypto.substack.com/p/the-money-flow-is-the-moat)**
by Jason Rosenthal (a16z crypto).

Its thesis in one line: **the most durable businesses sit *inside* a flow of value and
take a small clip that grows as the flow grows** — railroads, Standard Oil, AT&T, then
Google/Meta (attention→commerce), AWS (compute), Visa ($15.7T volume → $35.9B revenue),
Jane Street and PFOF market makers. Money flow + network effects = the most defensible
structure. The corollary ("your margin is my opportunity") points at traditional
finance — interchange, remittances, custody, FX, settlement — as the fattest margin
pools to attack, now newly attackable via stablecoins and programmable settlement. The
article flags **compute, GPU marketplaces, energy, robotics, space, and rare earths** as
the open frontier.

## 2. The method: thesis → prompt bank

The article's lens was converted into **20 reusable research prompts**
([`prompts.md`](prompts.md)) — money-flow x-ray, margin-pool attack, public-equity
screen, AI-agent money flow, compute/energy deep-dives, flow-multiple valuation,
falsification, asymmetric-opportunity, and more. These are the raw instruments.

## 3. The planning session: which prompts, in what order, why

Running 20 prompts cold is wasteful — many overlap ~70%. The
[`prompt_run_plan.md`](prompt_run_plan.md) collapses them into an **8-step pipeline**
where each step consumes the previous one's output:

```
orient → map → express → score → kill → synthesize
  #1      #2     #3/#18/#8   #15     #17      #20
```

Key planning decisions:
- **#2 gates everything** — rank the fattest, least-defended margin pools first, then
  run later prompts *only* against the top 3–4 (don't spread expensive prompts thin).
- **#3 then #18** — #3 gives the full instrument universe (incl. the obvious); #18
  filters for the *mispriced* subset. That ordering is where the alpha is.
- **#17 (falsification) runs last and cheapest** — only against survivors, to flag
  subsidized-flow traps before acting.
- **Minimum-viable path** if you want 3 not 8: **#2 → #18 → #17**.

## 4. The scoping: compute + energy as one coupled flow

The entity was deliberately scoped to **compute + energy analyzed *together*, not
separately**, because *power is the binding constraint on the AI buildout* and is a
*regulated* chokepoint (harder to commoditize than GPU-hours).
[`compute_run_brief.md`](compute_run_brief.md) bakes this in as two ready-to-run
versions:

- **Version A (full):** the complete 8-step chain, three flow layers labeled throughout.
- **Version B (lean):** `#2 → #9+#10 → #18 → #17` — ~80% of the signal for ~40% of the output.

Three flow layers, kept labeled end-to-end:
1. **Upstream supply chokepoints** (chips, HBM, interconnect, power/grid) — actionable today.
2. **Transaction/routing layer** (GPU-hour marketplaces, forward markets) — frontier, speculative.
3. **Demand layer** (AI agents paying for compute/inference) — new flow, early.

## 5. The execution: Version A, fully autonomous, web-grounded

**Version A was run fully autonomously**, web-enabled, each step saved to
[`outputs/`](outputs/) and feeding the next. See [`outputs/00_README.md`](outputs/00_README.md)
for a reader's guide to the output files.

---

## The Version A prompt chain (what actually ran)

| Step | Prompt | Role | Output file |
|------|--------|------|-------------|
| 1 | **#2 Margin-pool attack** (compute+energy reframe) | Rank where the take-rate is fattest *and* least defended | `02_margin_pool_attack.md` |
| 2 | **#9 Compute-marketplace + #10 Energy-flow** (run together) | The coupled deep-dive — power as the binding constraint | `09_10_compute_energy_deepdive.md` |
| 3 | **#8 AI-agent money flow** | Demand-side / machine-to-machine settlement picture | `08_ai_agent_money_flow.md` |
| 4 | **#3 Public-equity implication** | Full listed-instrument universe (incl. the obvious) | `03_public_equity_universe.md` |
| 5 | **#18 Asymmetric opportunity** | The mispriced subset — *the alpha step* | `18_asymmetric_opportunity.md` |
| 6 | **#15 Flow-multiple valuation** | Score every candidate 0–21 on a flow rubric | `15_flow_multiple_valuation.md` |
| 7 | **#17 Falsification** | Attack the survivors; confirm the traps | `17_falsification.md` |

*(#20 capstone was skipped — the watchlist was already assembled from #15/#17.)*

---

## The outcomes (concrete compute + energy opportunities)

**The reframe that drove everything:** the binding constraint has moved *off silicon
onto electrical delivery.* Only ~5 of 12 GW of 2026 US data-center capacity is actually
under construction; high-voltage transformer lead times are **36–48 months**; PJM warns
of a **49 GW generation shortfall by 2028**. So the defended money-flow moat is upstream
at **power + the gear that delivers it**, not at the GPU-hour layer.

### Survivors — passed #18 (mispriced) → #15 (scored 15–17/21) → #17 (survived the kill)

| Name | Thesis | Survived #17? |
|------|--------|---------------|
| **PWR** — Quanta Services | Builds the grid interconnection itself; labor + execution moat | ✓ best cyclical |
| **FIX** — Comfort Systems | Scarce DC build/electrification labor, priced as an HVAC contractor | ✓ |
| **TLN** — Talen Energy | Behind-the-meter merchant nuclear (AWS ~$18B / 1,920 MW deal) | ✓ *with FERC risk* ⚠ |
| **POWL** — Powell Industries | Switchgear chokepoint priced as an oil-&-gas cyclical | ✓ as a cyclical |
| **MOD** — Modine | Liquid cooling priced as a legacy auto-parts company | ✓ as a cyclical |

The common asymmetry: **every survivor is paid by the *physical* buildout regardless of
which neocloud, model, or payment rail wins.** They own watts, gear, fuel, or the labor
to install them — flows the AI boom cannot route around.

### Confirmed traps (what the pipeline killed)

- **Neoclouds (CoreWeave / Nebius)** — scored **7–8/21**. Sell a *depreciating good*,
  GAAP-lossy, pricing compressing to ~$2.80–3.20/GPU-hr. Owning GPU-hour flow is *not*
  a moat — the literal "owns commoditizing compute flow" trap.
- **Agent-payment tokens (x402 / Circle / Coinbase)** — ~**$28k/day** of real onchain
  volume against a ~**$7B** ecosystem valuation. Reflexive activity dressed as flow.

### The number that would break the bull case

**"Phantom gigawatts"** — if the queued/announced data-center demand is speculative
double-counting, the scarcity premium unwinds fast and the upstream basket de-rates like
every prior industrial supercycle. Verify before sizing. ⚠

---

## Repository layout

```
README.md                     ← you are here (the journey)
CLAUDE.md                     ← orients an AI agent to re-run the workflow
prompts.md                    ← the 20-prompt bank (the raw instruments)
prompt_run_plan.md            ← the 8-step pipeline logic + justification
compute_run_brief.md          ← compute+energy scoping (Version A full / B lean)
outputs/
  00_README.md                ← reader's guide to the outputs
  02_margin_pool_attack.md    ← #2  (the map)
  09_10_compute_energy_deepdive.md  ← #9+#10 (the deep-dive)
  08_ai_agent_money_flow.md   ← #8  (demand layer)
  03_public_equity_universe.md← #3  (full universe)
  18_asymmetric_opportunity.md← #18 (the alpha)
  15_flow_multiple_valuation.md← #15 (the scorecard)
  17_falsification.md         ← #17 (the kill step)
```

## Reproduce it

1. Read [`prompt_run_plan.md`](prompt_run_plan.md) for the pipeline.
2. Pick an entity and a version in [`compute_run_brief.md`](compute_run_brief.md)
   (or scope your own).
3. Run the prompts from [`prompts.md`](prompts.md) **in plan order, as a pipeline** —
   each step's output feeds the next — web-enabled, saving to `outputs/NN_name.md`.

---

## Sources for the load-bearing figures

- [a16z — "The money flow is the moat"](https://a16zcrypto.substack.com/p/the-money-flow-is-the-moat)
- [Belfer Center — AI, data centers & the US grid](https://www.belfercenter.org/research-analysis/ai-data-centers-us-electric-grid)
- [Build.inc — data-center transformer procurement (lead times)](https://build.inc/insights/data-center-transformer-procurement-2026)
- [Power Engineering — GE Vernova turbine backlog](https://www.power-eng.com/gas/turbines/data-centers-drive-record-surge-in-ge-vernova-power-equipment-orders-as-turbine-slots-tighten-through-2030/)
- [Utility Dive — nuclear / data-center PPAs](https://www.utilitydive.com/news/constellation-vistra-pseg-nuclear-data-center/719206/)
- [CoinDesk — x402 agent-payment volume reality](https://www.coindesk.com/markets/2026/03/11/coinbase-backed-ai-payments-protocol-wants-to-fix-micropayment-but-demand-is-just-not-there-yet)
