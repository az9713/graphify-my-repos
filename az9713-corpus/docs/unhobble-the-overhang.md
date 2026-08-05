---
repo: unhobble-the-overhang
description: Unhobbling the product overhang: what today's models can already do that no product lets them express. Based on Boris Cherny's 'Building Claude Code' talk (Y Combinator).
language: HTML
stars: 0
forks: 0
created: 2026-07-28
updated: 2026-07-29
topics: 
is_fork: False
kb: 2001
---

# unhobble-the-overhang
# Unhobble the Overhang

**Product overhang** is the gap between what today's model can already do and what any product lets it express. **Hobbling** is when the product itself gets in the model's way — a chat box that can only read code, an autocomplete that can only finish a line, while the model underneath could write the whole feature.

**Unhobbling the overhang** means building the minimal harness that lets the latent capability out. Claude Code itself was born this way (~Sonnet 3.5 era): the market offered autocomplete and read-only chat, the model could already write whole files, so a terminal plus write access was enough to elicit it. The founder message from the talk: *the next Claude Code is whoever unhobbles the next overhang.*

How to hunt overhangs in practice:

1. Give tasks slightly harder than you think the model can do.
2. Prefer a high-level goal + guardrails + exit criteria over step-by-step micromanagement.
3. Keep re-throwing "impossible" problems at each new model generation.
4. Verification (tests, screenshots, oracles) beats prompt polish.

Source: [Boris Cherny: Building Claude Code](https://www.youtube.com/watch?v=qyPCVqFUyDo) (Y Combinator).

## Live page

**[Product Overhangs: The Next Claude Code](https://az9713.github.io/unhobble-the-overhang/claude_product_overhang_matrix.html)** — click the screenshot to open it:

[![Product Overhangs matrix — screenshot](screenshot.png)](https://az9713.github.io/unhobble-the-overhang/claude_product_overhang_matrix.html)

## Worked example: unhobbling one of them

[`research/`](research/) takes the overhang the matrix ranks second — *Claude Code for
scientific research* — and actually builds it: a minimal harness that commits to a
falsifiable test **before** downloading any data, runs it, and reports what it could and
could not have detected.

The hypothesis was killed. The more useful output is the bound: over 2010–2026 the data rule
out a turn-of-month effect above ~9.6 basis points a day, while the effect the literature
claims sits *below* what the design could reliably detect — a distinction no p-value reveals
on its own.

Two adversarial review passes found nine real problems, all recorded rather than smoothed
over. One of them reversed a claim this author had already published. Start at
[`research/README.md`](research/README.md).

## Second worked example: repair, not just detection

[`visual/`](visual/) takes a different overhang — the one where a tool **detects** a problem and
then stops. Percy, Chromatic and BackstopJS all catch visual regressions and hand a human a red
diff. Detection is solved; repair is not.

Ten pages get one seeded CSS regression each (overflow, z-index, flex collapse, contrast failure,
box-sizing, and five more), two more are handed over already correct as controls, and a repair
agent gets only the broken page, a reference screenshot committed before the agent existed, and a
pixel-diff score. All ten were repaired and both controls left untouched.

The interesting part is what adversarial review then did to that number. Eleven findings, and two
of them matter: every agent had been told its fault's mechanism by its own working directory, and
the pre-registration contradicted itself — granting the agent readable source while claiming to
test repair from "only a rendered screenshot". The repairs are real; the blind test was not blind.
The harness also learned that a suspiciously clean calibration is indistinguishable from a blind
scorer, and that its own anti-cheat check could not, in principle, detect a cheat.

Start at [`visual/README.md`](visual/README.md).
