---
repo: forward-deployed-engineer
description: Transcript-grounded field guide to Forward Deployed Engineering, synthesized from eight AI Engineer talks.
language: HTML
stars: 0
forks: 0
created: 2026-07-29
updated: 2026-07-29
topics: 
is_fork: False
kb: 4706
---

# forward-deployed-engineer
# Forward Deployed Engineering, Decoded

A transcript-grounded field guide to Forward Deployed Engineering (FDE), built
from eight talks published by the [AI Engineer](https://www.youtube.com/@aiDotEngineer)
channel on July 28, 2026.

The guide compares how practitioners at Anthropic, Cognition, Kepler, Sierra,
Varick Agents, Factory, Decagon, and Ramp describe the role. It distills their
shared operating model, important disagreements, and a practical 12–24 month
preparation roadmap for an early-career engineer with a statistics background.

[![Open the live interactive field guide](fde-guide-preview.png)](https://az9713.github.io/forward-deployed-engineer/)

*Click the preview to open the live interactive guide.*

## Read the guide

- Open the [live GitHub Pages version](https://az9713.github.io/forward-deployed-engineer/).
- Open [`Forward-Deployed-Engineering-Decoded.html`](Forward-Deployed-Engineering-Decoded.html)
  for the self-contained, offline version.
- Run the source application locally for the development version.

The offline HTML includes its styling, hero artwork, all nine report panels, and
keyboard-accessible tab navigation in one file.

## Primary sources

![AI Engineer source-talk collection](fde_ai_engineer.jpg)

| # | Talk | Speaker / perspective | Length |
|---|---|---|---:|
| 1 | [Forward Deployed Engineering 101](https://www.youtube.com/watch?v=KwhgfwOSToQ) | Kevin Bai — economic rationale, platform leverage, and the boundary between product and service | 17:48 |
| 2 | [How Forward Deployed Engineering is done at Cognition](https://www.youtube.com/watch?v=RVxym6mmIns) | Jia Wu — baseline measurement, customer activation, and outcome evidence | 17:38 |
| 3 | [How Forward Deployed Engineering is done at Kepler](https://www.youtube.com/watch?v=1OMHGsUZiqA) | Vinoo Ganesh — workflow observation, ontology, thin slices, and product strategy | 22:20 |
| 4 | [The Dirty Secret of Forward Deployed Engineering](https://www.youtube.com/watch?v=Byv311hdoHE) | Natalie Meurer — role taxonomy, historical evolution, and outcome accountability | 16:49 |
| 5 | [AI tools for Forward Deployed Engineering](https://www.youtube.com/watch?v=l0FLhNqBOic) | Vasuman Moza — brownfield automation, workflow mapping, and context engineering | 20:22 |
| 6 | [How Forward Deployed Engineering is done at Factory](https://www.youtube.com/watch?v=wpOA-UXynoM) | Eno Reyes — agent readiness, customer-owned harnesses, and constrained autonomy | 21:21 |
| 7 | [How Forward Deployed Engineering is done at Decagon](https://www.youtube.com/watch?v=7wu2hsRfvV0) | Sunny Rekhi — early value, long-horizon trust, and upstreaming integrations | 18:08 |
| 8 | [How Forward Deployed Engineering is done at Ramp](https://www.youtube.com/watch?v=ITMXwI6QL6A) | Leo Mehr — scoping discipline, intake systems, grounding, and evaluation | 14:04 |

All eight talks were treated as separate primary sources. Timestamped links and
other URL variants should be canonicalized by YouTube video ID rather than
counted as additional works.

## Evidence and interpretation policy

The analysis was produced from locally archived English caption transcripts and
publisher metadata retrieved July 28, 2026.

- Speaker claims are attributed and paraphrased.
- Quotations and quantitative claims are not presented as independently
  verified facts unless explicitly stated.
- The guide distinguishes recurring agreement across speakers from
  speaker-specific emphasis.
- The career roadmap is an analyst synthesis, not a claim made by any single
  speaker.
- Raw caption files, transcript text, and metadata are intentionally excluded
  from this repository. They remain local research evidence rather than
  redistributed source material.

The resulting synthesis identifies six recurring threads:

1. The unit of work is a customer outcome.
2. Field work must compound into reusable product capability.
3. Scoping is a first-class technical skill.
4. Enterprise context is harder than model access.
5. Trust is earned through evidence and operational discipline.
6. AI shifts human work toward judgment, discovery, and accountability.

## Run locally

Requirements: Node.js 22.13 or newer.

```bash
npm install
npm run dev
```

Production validation:

```bash
npm test
```

## Project structure

- `app/page.tsx` — source summaries, synthesis, and tabbed report interface
- `app/globals.css` — responsive visual system
- `public/fde-learning-map.png` — hero artwork
- `tests/rendered-html.test.mjs` — rendered-output checks
- `index.html` — GitHub Pages entry point
- `Forward-Deployed-Engineering-Decoded.html` — portable offline artifact

## Limitations

This repository is a source synthesis and learning guide, not a comprehensive
survey of every FDE organization. The talks were published by one channel in one
coordinated series, so the apparent consensus may partly reflect editorial
selection. Company practices, job definitions, and speaker affiliations can
also change after the retrieval date.

## License and source rights

The original talks, captions, thumbnails, and channel branding remain the
property of their respective owners. This repository contains an original
analysis and interface; it does not grant rights to the underlying videos.
