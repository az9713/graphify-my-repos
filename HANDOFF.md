# HANDOFF — az9713 portfolio atlas

**Read this first each new session.** No `CLAUDE.md` in this folder; standing
conventions come from `~/.claude/CLAUDE.md` (global). **This directory is not a
git repository** — nothing is committed or pushed, and every artifact below is
plain files on disk. Treat them as the durable record.

## Current state

Two deliverables, both finished and verified:

- **`portfolio-suggestions.html`** — 16 ambitious project suggestions across two
  tracks (A: extend 7 existing repos, B: 9 new domains), with per-idea cost
  rating, first move, and "the hard part". Filter chips at top. Self-contained.
  ⚠️ **Contains two claims later disproven** — see Corrections below. Not yet
  updated; `atlas.html` carries the corrections instead.
- **`atlas.html`** (154 KB, data inlined) — A1 executed. All 448 repos clustered
  into 14 discovered subject clusters, with a reach chart, expandable cluster
  cards listing every member repo, the 72-orphan list, and a hub/bridge table.
  Verified section-by-section in Chrome; renders correctly.

### Corrections established this session (supersede the suggestions page)

1. **Stars track subject, not originality.** Derivative repos average 0.68★,
   originals 0.54★ — indistinguishable noise. The real split: 6 agent-tooling
   clusters hold 268 repos / 244 stars; the 6 clusters covering physics, trading,
   film, courses, knowledge graphs and deployed apps hold 113 repos / **11 stars**.
2. **Only 15 of 448 repos have GitHub topics set** (37 have a homepage URL).
   This is the cheapest reach fix available and was missed in the original A7.
3. Derivative repo count is **120, not ~180**. Trading cluster is **17 repos, not
   13** (affects A2 scope). Physics & math is **24 repos** (A5 should widen from
   CFD to physics generally).
4. **147 repos sit in two clusters whose top terms are generic** — roughly a third
   of the portfolio is agent infrastructure too self-similar to separate.

## Graph — DONE (`graph.html`)

`graph.html` (340 KB, data + force-graph lib inlined, double-clickable, no server)
— Obsidian-style force layout of the repo–repo projection, built with the same
recipe as `buzz_me/buzz-tutorial/audit/graph` (vasturiano **force-graph** on
canvas; drag re-heats the sim, so neighbours follow with the springy lag).

- **440 repos, 1,551 edges, 57 orphans.** 5 in-graph nodes have no
  `atlas-data.json` record and are dropped.
- Edges: `build_graph.py` recomputes the Newman projection exactly as
  `recluster.py` (concepts in >120 repos dropped, weight `1/(k-1)`, prune ≤0.02)
  → 7,581 edges, then **keeps each repo's 6 strongest ties only** (`K` in the
  script). The full 7.5k-edge set lays out as one featureless ball.
- Colour = the 14 subject clusters, size = √stars, white ring = has stars.
  Legend filters clusters; search jumps; hover dims non-neighbours; orphans
  toggle. `Fit` frames the connected core only.
- **Finding: the topic clusters do not separate spatially.** Only 15.7% of linked
  repos sit nearest their own cluster centroid (7.1% = chance). Toggle
  **"color by link community"** and it jumps to **35.0%** over 11 Louvain
  communities (~9% = chance) — the concept links carry real structure, it just
  isn't the TF-IDF topic structure. Extends correction 4 above.
- Layout numbers live in `graph-template.html`: charge −120 / distanceMax 400,
  link distance 25, link strength `min(1, w·10)`. A hand-rolled gravity force was
  tried and **collapsed every node to (0,0)** — the built-in centering force is
  enough; orphans drift to a natural outer halo (core r≈670, orphan median r≈808).
- Screenshots of both colour modes: `graph-topics.jpeg`, `graph-linkcommunity.jpeg`.

Not wired into `atlas.html` — it is a standalone page. Link it from the atlas if
you want one entry point.

`DEVELOPMENT_JOURNEY.html` — full project narrative from the opening prompt to the
graph: chapters, problems/fixes, the corrections table, numbers-and-what-they-count,
file inventory. Scrubbed of account handle, paths and any personal identifiers.

## Next task

Open. Candidates: link `graph.html` from `atlas.html`; apply the corrections above
to `portfolio-suggestions.html`; or execute one of the A-track suggestions
(A7 topics-and-homepage fix is still the cheapest reach win).

## Where to read things

- `atlas-data.json` — merged per-repo record: cluster id + name, stars, language,
  kb, created, derivative flag, neighbors, betweenness. Plus cluster summaries,
  hubs, bridges. **This is the file to build the graph view from.**
- `az9713-corpus/docs/` — 448 markdown files, one per repo: YAML front matter
  (repo, description, language, stars, forks, created, updated, topics, is_fork,
  kb) + README truncated to 20k chars. `bollinger_band_monitor` is empty.
- `az9713-corpus/repos.json` — raw GitHub metadata for all 448.
- `graphify-out/GRAPH_REPORT.md` — graphify's own audit (god nodes, 146 fine
  communities, surprising connections).
- `graphify-out/graph.json` — 1,569 nodes / 2,868 edges, node-link format.
- `graphify-out/atlas2.json` — repo→coarse-community, degree, betweenness.

`build_graph.py` + `graph-template.html` + `force-graph.min.js` → `graph.html`.
Re-run `python build_graph.py` after editing the template; never edit `graph.html`
directly (same inject-and-overwrite rule as `atlas.html`).

## Scratch scripts on disk (reproducible; the durable record is the HTML/JSON)

All are re-runnable from this directory. Run order was:

1. `recluster.py` — loads `graph.json`, builds the Newman-weighted repo–repo
   projection, tunes Louvain resolution, writes `graphify-out/atlas2.json`.
   Must be run from inside `graphify-out/`.
2. `topics2.py` — the one that worked. TF-IDF over `az9713-corpus/docs/` with
   front matter, code blocks, HTML markup, md links and file paths stripped,
   plus a boilerplate stopword list; SVD→KMeans k=14; writes `topics.json`.
   (`topics.py` is the earlier broken version — its clusters grouped on README
   furniture. Kept only as a record of the failure; do not use.)
3. `merge.py` — joins `topics.json` + `atlas2.json` + `repos.json` into
   `atlas-data.json`, hand-labels the 14 clusters, computes orphans/hubs/bridges.
4. `atlas-template.html` + inline-injection snippet → `atlas.html`. The template
   has a `/*__DATA__*/{}` placeholder; a short Python step replaces it with the
   trimmed JSON. **To edit the page, edit the template and re-inject** — editing
   `atlas.html` directly gets overwritten on the next rebuild.

## Gotchas that cost time this session

- **Verify rendered HTML in a browser, not by reading the source.** A missing
  `c.members` field threw inside the cluster-card render and silently blanked
  three whole sections; the file looked fine. Chrome's console showed no page
  error (only an unrelated extension exception), so screenshots were what caught it.
- **`file://` URLs are blocked** by the Chrome tool. Serve with
  `python -m http.server 8731 --bind 127.0.0.1` and navigate to
  `http://127.0.0.1:8731/…`. Kill the background task when done.
- Screenshots taken immediately after a scroll sometimes return a blank frame.
  Re-take before concluding a section failed to render.
- `gh api` output must be read with `encoding='utf-8'` in Python — Windows
  defaults to cp1252 and dies on repo descriptions.

## Budget context

The extraction run alone consumed **3,366,498 input tokens** across 18 subagents.
Weigh that before proposing another agent fleet — a local TF-IDF pass answered the
question that actually mattered in seconds, for nothing.
