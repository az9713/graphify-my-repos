# The J-Space

An interactive lesson that teaches Anthropic's **"Verbalizable Representations Form a Global Workspace in Language Models"** — the Jacobian lens (J-lens) and the J-space — in plain language without watering down the math or the evidence.

### ▶ [Open the live lesson](https://az9713.github.io/the-J-space/)

Hosted on GitHub Pages — opens in your browser, no install. (GitHub can't run the interactive HTML inside this README, so it's served live at the link above.)

## What's here

- **[`lessons/0001-the-j-space-guided-tour.html`](lessons/0001-the-j-space-guided-tour.html)** — a self-contained interactive lesson. Open it in a browser. Includes:
  - the J-lens equation built up from scratch (\(J_\ell = \mathbb{E}[\partial h_{\text{final},t'}/\partial h_{\ell,t}]\)), with the logit lens shown as the \(J_\ell = I\) special case;
  - an interactive **swap bench** for the five functional workspace properties (report, modulation, reasoning, flexible generalization, selectivity);
  - a layer-band explorer (sensory → workspace → motor), the ablation and reflection-training result tables, and six quizzes with immediate feedback.
  - Equations render via MathJax (needs a network connection); everything else works offline.

The repo is also a small teaching workspace: `MISSION.md`, `RESOURCES.md`, `NOTES.md`, plus `learning-records/` for tracking progress across sessions.

## Official sources

- Blog post — Anthropic, *A global workspace in language models* (Jul 6, 2026): https://www.anthropic.com/research/global-workspace
- Full paper — *Verbalizable Representations Form a Global Workspace in Language Models*, Transformer Circuits (2026): https://transformer-circuits.pub/2026/workspace/index.html

Experiments default to Claude Sonnet 4.5, corroborated on Haiku 4.5 and Opus 4.5/4.6. All figures and numbers in the lesson are quoted from those two sources.

## License

Teaching material built on Anthropic's published research; see the official sources above for the primary work.
