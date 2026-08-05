---
repo: fable-ray-tracing
description: MirrorForge — a WebGPU compute-shader ray-traced mirror-puzzle game, built end-to-end with Claude Fable 5 (xhigh). Includes a transparent token-economics writeup.
language: TypeScript
stars: 1
forks: 0
created: 2026-06-11
updated: 2026-06-14
topics: 
is_fork: False
kb: 7773
---

# fable-ray-tracing
# MirrorForge

> **▶ [Play it live](https://az9713.github.io/fable-ray-tracing/)** &nbsp;·&nbsp; WebGPU required (Chrome / Edge 113+)
> &nbsp;·&nbsp; Inspired by van Zyl's video **["Anthropic's New Claude Fable 5 is Insanely Good at Coding"](https://www.youtube.com/watch?v=I3PYGi_tGy0&t=6s)**

https://github.com/user-attachments/assets/7143092a-a074-4fae-a5b6-9d8bd1c9ebee

A browser mini game engine and playable reflection-puzzle demo: **WebGPU
compute-shader ray tracing** drives the visuals, a deterministic CPU beam
simulator drives the puzzle. You are locked in a dark mirrored vault — rotate
the mirrors in 15° detents and feed the ember beam to the receiver core to
open the door.

Zero runtime dependencies. Everything that ships to the browser is in this
repo: custom math library, analytic ray tracer in WGSL (planes, quads,
spheres, oriented boxes, capsules), Whitted bounce loop with Schlick Fresnel,
progressive accumulation, quarter-res bloom, and three procedural WebAudio
cues.

## Run

```
npm install      # dev deps only: vite, typescript, vitest, @webgpu/types
npm run dev      # http://localhost:5173 — requires WebGPU (Chrome/Edge 113+)
npm test         # full unit suite (math, intersections, beam, level, FSM)
npm run build && npm run preview   # production bundle smoke test
```

Dev/verification flags: `?selftest` (boot smoke test incl. GPU readback),
`?parity` (runs the production WGSL intersection code against the shared
test vectors), `?nogpu` (forces the detection screen).

## Controls

| Input | Action |
|---|---|
| Drag / wheel | Orbit / zoom |
| Click a mirror | Select it |
| `Q` / `E` (or ←/→) | Rotate selected mirror ±15° |
| `R` | Reset the level |
| `M` | Mute audio |
| `` ` `` | Debug overlay (adapter, FPS, samples, beam state) |
| `P` | Performance mode (½ resolution, 2 bounces, 1 shadow ray) |
| `B` | Bloom toggle |

## How this was built

MirrorForge was built end-to-end with **Claude Fable 5** in **`xhigh`** effort
mode inside Claude Code, one milestone per commit. The
**[development journey](docs/journey/)** documents the whole experience with full
cost transparency — including a [token-economics reveal](docs/journey/03-token-economics.md)
of what the "powerful but expensive" mode actually costs. Inspired by
["Anthropic's New Claude Fable 5 is Insanely Good at Coding"](https://www.youtube.com/watch?v=I3PYGi_tGy0&t=6s).

## What it cost — token economics

MirrorForge was built at Claude Fable 5's **`xhigh`** effort — the most capable,
most expensive way to run it. Here is the honest bill. Full accounting and
caveats in **[docs/journey/03-token-economics.md](docs/journey/03-token-economics.md)**.

| Headline | Value |
|---|---|
| **The real bottleneck** | **Throughput, not dollars** — a rolling 5-hour usage cap, not an invoice |
| Planning cost | An **entire 5-hour window driven to 100%** — before one line of code |
| Heaviest phases | M1–M4, each **~20–42%** of a 5-hour window |
| Cheapest phase | M7, **~7%** of a window |
| Largest single turn | **42 min / 74k output tokens** (during M5) |
| Whole-project estimate | **~5M – 14M tokens**, order of magnitude (derived — see below) |
| Calendar span vs. work | **~26 hours elapsed** for **~2 hours of active agent work** — the rest was waiting for the cap to reset |

Per-milestone usage, as the **observed 5-hour-window delta** (commit + the
developer's live annotation):

| Phase | Commit | 5h-window Δ | Annotation |
|---|---|---|---|
| Planning | *(pre-code)* | 69% → **100% cap** | hit the cap before code |
| M1 | `bb5ae1f` | ~24 pts | *"42% in <30 min !! stop it"* |
| M2 | `b4e7482` | ~27 pts | *"28% used for milestone 2"* |
| M3 | `74bfbb1` | ~20 pts | *"58% for both milestone 2,3"* |
| M4 | `1abd51e` | ~30–42 pts | *"61%→90%", "nothing like van zyls"* |
| M5 | `9c4d359` | ~54 pts | the 42-min / 74k-token turn |
| M6 | `cfc358f` | *(not cleanly read)* | largest commit (914 insertions) |
| M7 | `043a4fa` | ~7 pts | *"18%"* |
| M8 | `a42cf11` | ~25 pts | — |

### How these numbers are arrived at

Be skeptical of any token figure — including these. The Claude Code CLI does
**not** expose a per-session or per-milestone token total. It only shows:

1. **Rolling-window gauges** — `5h NN%` and `7d NN%`, the fraction of the Max
   plan's rolling 5-hour / 7-day allowance consumed. This is the *lived* metric
   the developer actually watched, and the table above reports it directly. **But
   the 5-hour window resets** (it reset 4+ times across this 26-hour build), so
   per-milestone deltas are meaningful only *within one window* and **cannot be
   summed** into a project total.
2. **Sporadic per-turn counters** — e.g. `(5m 33s · ↓ 14.0k tokens)`. That number
   is **output tokens for one turn only**; it omits input, *thinking*, and
   cache-read tokens, which dominate true cost at `xhigh`. So it's a **floor**,
   not a total, and it only appeared on a dozen of the project's hundreds of turns.

The whole-project **~5M–14M token** range is therefore an **estimate**, reached by
making two independent methods agree:

- **Bottom-up** — ~25 turns/milestone × ~4k output tokens × a **5–15× multiplier**
  for the unshown thinking + input + cache ≈ **0.5M–1.5M tokens/milestone**, ×9
  phases ≈ **5M–14M**.
- **Top-down** — each milestone burned ~20–40% of a 5-hour window; back-solving
  against the bottom-up figure implies **~2–5M tokens per full 5-hour window**.

Both land in the same range — and that convergence is the only validation
honestly available, because **the ~2–5M-tokens-per-window anchor is an assumption,
not a published Anthropic number.** Change the anchor and every absolute figure
rescales. The dollar cost was ~zero *only* because Fable 5 was promo-included in
the Max plan during this window; after the promo, the same work bills against
usage credits and the money story changes entirely.

## Architecture in one paragraph

`Scene` is the single source of truth for geometry. The GPU tracer
(`shaders/`) makes it pretty; the pure-function `BeamSimulator` (CPU) decides
the puzzle — both use the same intersection math, mirrored function-for-
function between `math/intersect.ts` and `intersect.wgsl` and held together
by shared test vectors plus a GPU parity harness (`?parity`). Beam visuals
are generated *from* simulator output, so the drawn beam is definitionally
the logical beam. `PLAN.md` is the full architecture document;
`docs/worklog.md` records every milestone with verification evidence.

## Future work (deliberately cut — see PLAN.md §16 R12)

- Additional levels / level select (the format is data-driven and ready)
- Refraction / glass primitives
- Triangle meshes + BVH
- Fuller soundscape (ambient room tone, hover ticks)
- Half-res reflections and other unspent performance headroom
- GPU timestamp queries for the overlay (CPU frame-ms suffices for the knobs)
