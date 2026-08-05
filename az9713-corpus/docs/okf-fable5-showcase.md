---
repo: okf-fable5-showcase
description: Daily AI-news captures → Open Knowledge Format → a 383-node knowledge graph. The Claude Fable 5 storyline, assembled by community detection.
language: HTML
stars: 0
forks: 0
created: 2026-07-03
updated: 2026-07-03
topics: 
is_fork: False
kb: 678
---

# okf-fable5-showcase
# OKF + Fable 5

**Claude Fable 5** turned a folder of raw daily AI-news captures into a portable **[Open Knowledge Format (OKF)](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf)** bundle — then that bundle became a navigable knowledge graph in which the **Fable 5** storyline assembles itself across seven days of otherwise-unrelated sources.

![Knowledge graph of the OKF bundle](graph/graph.svg)

> **[▶ Interactive graph](https://az9713.github.io/okf-fable5-showcase/graph/graph.html)** · **[▶ OKF viz](https://az9713.github.io/okf-fable5-showcase/okf_bundle/viz.html)** (live on GitHub Pages)

## What it is

```
raw captures            →   OKF bundle            →   knowledge graph
(transcripts, caption        (markdown + YAML          (383 nodes, 434 edges,
 files, notes — ~1.5M         frontmatter, one          38 communities via
 words across 7 days)         file per source)          community detection)
        └──────────── created by Claude Fable 5 ─────────────┘
```

**Fable 5 produced the OKF artifacts** in this repo: it drove the conversion that collapses each source's several raw forms (captions, transcript, metadata, summary) into one clean, self-describing, cross-linked concept file — portable, git-diffable, and tool-agnostic. See [`examples/`](examples/) for one source shown before → after.

## Layout

| Path | What |
|------|------|
| `okf_bundle/` | 70 OKF concept files across 7 day-directories + `viz.html` |
| `graph/` | interactive `graph.html`, `graph.json`, `graph.svg`, `GRAPH_REPORT.md` |
| `examples/` | one source, raw capture → OKF concept |
| `scripts/` | `build_okf.py` (raw → OKF) · `gen_viz.py` (OKF → viz) |

## Reproduce

```bash
python scripts/build_okf.py /path/to/root     # root/brain_dump/ → root/okf_bundle/
# graph built with graphify (https://pypi.org/project/graphifyy/): graphify export html
```

The captures are notes on public AI-industry videos and articles; every concept cites its source URL. The raw dump itself is not included — only the OKF bundle and the graph derived from it.

Built with [OKF](https://github.com/GoogleCloudPlatform/knowledge-catalog/tree/main/okf) · [graphify](https://pypi.org/project/graphifyy/) · created by **Claude Fable 5**.
