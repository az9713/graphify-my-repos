---
repo: general-relativity-dwarkesh
description: Interactive, transcript-grounded General Relativity course based on Adam Brown's Dwarkesh lecture, with reconstructed boards, visual labs, practice, and an Einstein archive.
language: JavaScript
stars: 0
forks: 0
created: 2026-07-12
updated: 2026-07-12
topics: 
is_fork: False
kb: 5833
---

# general-relativity-dwarkesh
# Essence of General Relativity

## Live course

**[Open the interactive General Relativity course →](https://az9713.github.io/general-relativity-dwarkesh/)**

The GitHub Pages edition includes all seven lessons, reconstructed board arguments, interactive visual labs, practice, references, and the Einstein Archive.

**Project credit:** This course is a joint project of **Grok 4.5** and **GPT 5.6 sol**.

> **For agents & developers:** full implementation snapshot, architecture, validation results, and extension rules are in **[`IMPLEMENTATION_STATUS.md`](./IMPLEMENTATION_STATUS.md)**. Read that before major changes.

Interactive, **offline-capable** HTML learning experience grounded in Adam Brown’s lecture (Dwarkesh Patel conversation). The course separates:

- **Transcript-grounded** claims (with timestamps)
- **Board reconstructions** (confidence-labeled, not facsimiles)
- **GR supplements** (established background)
- **Historical archive** material (evidence-status labeled)

Implementation follows `GR_LEARNING_MATERIALS_PLAN.md`.

The current learner-facing edition uses a **1915 Seminar Folio** design: a restrained private-press page, reconstructed chalkboard arguments, generous reading typography, horizontal lesson tabs, and evidence notes in the margin. It includes interactive experiments, retrieval practice, cross-links, and a historically sourced Einstein Archive.

## Quick start

```bash
npm install
npm run dev
```

Open the URL Vite prints (usually `http://localhost:5173/`).

### Production / offline build

```bash
npm run build
npm run preview
```

The `dist/` folder is a static site. After build, no CDN is required; assets are local.

## Project map

| Path | Role |
|------|------|
| `transcript.txt` | Local-only immutable raw transcript; ignored by Git and not published |
| `source/` | Normalized transcript, argument units, claims, boards |
| `src/` | Course app (content, components, apps, styles) |
| `lessons/` | Seven lesson HTML entry points |
| `visual-lab/` | All boards + interactive labs |
| `practice/` | Misconceptions & flashcards |
| `reference/` | Atlas, equation cards, glossary |
| `archive/` | Einstein Archive appendices A–E |
| `review/` | Capstone teach-back |
| `scripts/` | Source prep, validation, flashcard export |
| `tests/unit/` | Formula unit tests |

## Scripts

```bash
npm run validate:source   # transcript registries
npm run validate:content  # HTML course pages
npm run test:unit         # Schwarzschild, redshift, etc.
npm run export:flashcards # public/flashcards.csv
npm run build
```

## Course structure

1. The Coincidence Einstein Took Seriously  
2. Einstein’s Happiest Thought  
3. Gravity Becomes Geometry  
4. The Field Equation Without Tensor Calculus  
5. Why a Black Hole Must Be Black  
6. Clocks, Energy, and Horizon Crossing  
7. How Nature Answers Back  

Plus Visual Lab, Practice, Reference, Capstone, and Einstein Archive (Ten-Year Ascent, Constellation, Quantum Salon, Turing & Shannon, Nobel Dossier).

## Progress & privacy

Lesson completion and predictions use **localStorage** only. No accounts, no backend.

## Scientific guardrails (non-exhaustive)

- Equivalence is **local**; tides matter  
- Horizon ≠ singularity; horizon ≠ material shell  
- Newtonian escape speed is a **clue**, not a GR proof  
- Static redshift formulas are not free-fall horizon formulas  
- EHT does not “photograph a solid horizon”  
- Turing/Shannon are **near-encounters**, not documented friendships with Einstein  
- Nobel counts are not lifetime rankings  

## Source pipeline

```bash
node scripts/prepare_source.js
node scripts/build_source_maps.js
node scripts/validate_source.js
```

Do not edit or commit the local-only `transcript.txt` via these scripts.
