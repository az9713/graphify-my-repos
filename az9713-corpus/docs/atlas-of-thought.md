---
repo: atlas-of-thought
description: 90-second AI documentary on visualizing the latent spaces of language models and world models — researched, generated (ElevenLabs/Veo 3.1 Fast), edited, and documented autonomously by Claude Fable 5 in one session
language: HTML
stars: 0
forks: 0
created: 2026-07-21
updated: 2026-07-22
topics: 
is_fork: False
kb: 245626
---

# atlas-of-thought
# Atlas of Thought

A 90-second AI-made documentary that helps humans visualize the latent spaces of language models and world models — from embedding-space "concept galaxies" to Anthropic's J-Space and LeCun's JEPA. Researched, storyboarded, generated on ElevenLabs, and edited with ffmpeg autonomously by an AI agent in a single session on July 21, 2026.

[![Watch Atlas of Thought](media/poster.jpg)](https://az9713.github.io/atlas-of-thought/watch.html)

**▶ [Watch the film](https://az9713.github.io/atlas-of-thought/watch.html)** (streams in the browser, 71 MB web encode) · [full-quality master](https://github.com/az9713/atlas-of-thought/raw/main/atlas_of_thought_1080p.mp4) (174 MB download, 1920×1080 CRF 18)

[![Read The Mathematics of Atlas of Thought](media/atlas-math-poster.png)](https://az9713.github.io/atlas-of-thought/atlas-math.html)

**∑ [The Mathematics of Atlas of Thought](https://az9713.github.io/atlas-of-thought/atlas-math.html)** — companion deep-dive with full derivations of the math the film gestures at: latent-space geometry (Johnson–Lindenstrauss, t-SNE/UMAP), LeCun's JEPA (energy-based models, collapse and VICReg), and a formalization of Anthropic's J-Space (Jacobian lens, workspace rank bottleneck). 19 figures, all computed by a reproducible generator in `tools/`. Written autonomously by the same agent on July 22, 2026.

**The credit goal — accomplished.** The brief's second constraint was to consume the account's entire remaining ~47K ElevenLabs credit balance. Result: **47,196 of 47,261 available credits spent (99.86%)**, leaving 65 — less than the price of any purchasable generation — with every credit converted into shippable assets (11 clips, two narration takes, a 2-minute score, four SFX, an outro read) rather than filler. Full accounting: [credit ledger](docs/reference/pipeline-reference.md).

---

## Documentation

| Section | What's inside |
|---------|--------------|
| [Overview](docs/overview/what-is-this.md) | What the film is, the mental model behind it |
| [Watching the film](docs/user-guide/watching-the-film.md) | Viewer guide + [FAQ](docs/user-guide/faq.md) — no technical background needed |
| [Autonomous production system](docs/concepts/autonomous-production-system.md) | How Fable 5 made this: tools, control loop, delegation, limits |
| [Prerequisites](docs/getting-started/prerequisites.md) | Exact dependencies with verify commands |
| [Key concepts](docs/overview/key-concepts.md) | J-Space, JEPA, latent space, and every other term used |
| [Quickstart](docs/getting-started/quickstart.md) | Rebuild the master from assets in one command |
| [Reproducing the pipeline](docs/guides/reproducing-the-pipeline.md) | Redo the whole autonomous run for a new topic |
| [Pipeline reference](docs/reference/pipeline-reference.md) | Every shot, prompt, asset, and the full credit ledger |
| [System design](docs/architecture/system-design.md) | Pipeline architecture and the decisions behind it |
| [Development journey](docs/history/development-journey.md) | The build chronicle: what happened, what broke, what it cost |
| [Troubleshooting](docs/troubleshooting/common-issues.md) | Browser-automation and ffmpeg gotchas, with fixes |

## Repository layout

| Path | Contents |
|------|----------|
| `atlas_of_thought_1080p.mp4` | Final master |
| `clips/shot01–11.mp4` | 11 source clips (Veo 3.1 Fast, 6 s, 1080p) |
| `audio/` | `narration.mp3`, `music.mp3`, `outro_credits.mp3` |
| `caps/` | Caption text files burned into the film |
| `build.sh` | One-command assembly pipeline (ffmpeg) |
| `DEVELOPMENT.md` | Complete build chronicle — every autonomous step, incident, and verification |
| `STORYBOARD.md` | Original 14-shot storyboard (11 made the final cut) |
| `research/` | Three research reports the script was built from |
| [`atlas-math.html`](https://az9713.github.io/atlas-of-thought/atlas-math.html) | Companion math deep-dive (self-contained — [read it rendered](https://az9713.github.io/atlas-of-thought/atlas-math.html), not the source view) |
| `tools/` | Figure generator + splicer that produce every figure/number in `atlas-math.html` |
| `docs/` | Full documentation |

> **Note:** Docs change in the same commit as the behavior they describe. The pipeline reference tracks `build.sh` — update both together.
