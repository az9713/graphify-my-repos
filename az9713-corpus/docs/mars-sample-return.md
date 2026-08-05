---
repo: mars-sample-return
description: Interactive Mars Sample Return mission planner — universal-variable Kepler propagator, patched conics, Hohmann transfers with live dv budget. Three.js + TypeScript.
language: TypeScript
stars: 0
forks: 0
created: 2026-07-28
updated: 2026-07-28
topics: 
is_fork: False
kb: 179
---

# mars-sample-return
# Mars Sample Return Mission Planner

An interactive, browser-based orbital-mechanics planner for a Mars Sample Return
campaign. The solar system runs on a universal-variable Kepler propagator — every
position is a pure function of the epoch, so you can scrub time backwards and
forwards exactly. A Hohmann transfer to Mars is planned, drawn, and flown, with
Δv budget, sphere-of-influence handovers, and launch-window phasing all computed
from classical two-body mechanics.

**Fly it:** https://az9713.github.io/mars-sample-return/ (or `npm install && npm run dev`)

Phases 0–1 of the spec (`f1-digital-twin/docs/three-ambitious-simulation-specs.html`,
Mars tab): solar-system view with accelerated time, Keplerian propagator,
patched-conic SOI transitions, Hohmann + bi-elliptic transfer calculators, Δv
vectors in-scene.

## Controls

| Key | Action |
| --- | --- |
| `Space` (or Pause button) | pause / resume time |
| `,` / `.` | time-warp down / up |
| scrub bar | jump to any epoch (exact — no integration drift) |
| `1` `2` `3` `4` | focus Sun / Earth / Mars / spacecraft |
| `C` | cycle camera focus |
| `R` | replan from the current epoch — jumps to the next launch window |
| mouse | orbit / zoom (OrbitControls) |

## The numbers (all asserted in `npm run check`)

| Quantity | Computed | Reference |
|---|---|---|
| Hohmann departure v∞ | 2.9447 km/s | ~2.94 km/s |
| Hohmann arrival v∞ | 2.6489 km/s | ~2.65 km/s |
| Transfer time | 258.87 d | ~259 d |
| Launch-window phase angle | Mars leads 44.34° | ~44° |
| Synodic period | 779.9 d | 780 d |
| Earth / Mars SOI radius | 0.9246 / 0.5772 ×10⁶ km | 0.929 / 0.578 ×10⁶ km |

13 assertions: propagator invariant drift < 2×10⁻⁹ over an orbit, orbit closure to
1.6×10⁻¹⁴, element round-trips, hyperbolic arcs, the bi-elliptic crossover, and a
planned mission that reaches Mars with zero miss distance.

## The physics

- **Propagator** (`src/kepler.ts`): universal-variable (Sundman/Stumpff) formulation —
  one code path covers elliptic, parabolic, and hyperbolic orbits, which patched
  conics needs. No numerical integration; state at epoch *t* is closed-form.
- **Transfers** (`src/transfer.ts`): Hohmann and bi-elliptic Δv, transfer-ellipse
  geometry, launch-window phasing from the synodic period.
- **Patched conics** (`src/soi.ts`): sphere-of-influence radii and nearest-SOI frame
  selection; the HUD shows planet-relative (hyperbolic) elements and both handover
  epochs.
- Physics modules import no three.js — the test bundle is 20 kB.

## Scale honesty

Orbit radii are true to scale (1 unit = 10⁶ km). Planet bodies are ~350× oversize
so they are visible at solar-system zoom; SOI shells carry a separate ~9×
exaggeration that preserves the true Earth : Mars SOI ratio. The HUD states the lie.

## Known simplifications (marked `// ponytail:` in source)

- Planets on circular, coplanar orbits at their true semi-major axes — no
  eccentricity (Earth 0.0167, Mars 0.0934), no 1.85° mutual inclination yet.
- The trajectory propagates as one heliocentric conic: SOI handovers are displayed,
  but the integrator does not yet switch frames, so reported Δv is really v∞.
  Escape/capture hyperbolae from a parking orbit are Phase 2.
- The craft parks at the planet's exact position (a 300 km LEO is 1/150th of a
  pixel at this scale).

Later phases per spec: rocket equation + mass budget, EDL, Mars ascent, Earth
return, fault injection, SPICE validation.
