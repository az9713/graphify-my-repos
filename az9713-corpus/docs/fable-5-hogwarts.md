---
repo: fable-5-hogwarts
description: 
language: HTML
stars: 0
forks: 0
created: 2026-07-02
updated: 2026-07-02
topics: 
is_fork: False
kb: 34
---

# fable-5-hogwarts
# Fable 5 vs Opus 4.8 — One-Shot Hogwarts-Style Castle

Two fully explorable 3D wizarding castles, each generated **one-shot** by a Claude model in
Claude Code from the same prompt. Each world is a single self-contained HTML file: Three.js
from a CDN, no build step, no external assets — all geometry, textures, and effects procedural.

## Live comparison

| Page | Link |
|---|---|
| **Side-by-side comparison** | https://az9713.github.io/fable-5-hogwarts/ |
| Opus 4.8 world (full screen) | https://az9713.github.io/fable-5-hogwarts/index_opus_4.8.html |
| Fable 5 world (full screen) | https://az9713.github.io/fable-5-hogwarts/index_fable_5.html |

Or clone and double-click either HTML file — everything runs locally.

## Controls

| Key | Action |
|---|---|
| `W A S D` | Walk |
| Mouse | Look around |
| `Shift` | Run |
| `Space` | Jump |
| `Esc` | Release cursor |

## The prompt

Both models received the same brief:

> "I want to show people what you can one-shot, so aim for the top of your range - this should feel like a game studio tech demo, not a placeholder.
>
> Build me a fully explorable 3D (Hogwarts-style castle - or describe your own world) in the browser, as ONE self-contained index.html using Three.js loaded from a CDN. No build step, no external assets - all geometry procedural.
>
> It needs:
>
> - First-person controls: WASD to walk, mouse to look, shift to run, space to jump
> - At least 6 distinct named areas (great hall, two towers, courtyard, library, dungeon) with interiors I can actually walk into
> - Atmosphere: flickering torch light, fog, and a slow day-night cycle
> - An on-screen label telling me which area I'm in, plus a start screen showing the controls
> - Collision, so I can't walk through walls or fall through floors
>
> Before you build, interview me - at least 3 quick questions in one batch so we're aligned on the end result: the world, the mood, and the three places I most want to walk through. After that, act - don't give me options or a plan, give me the file. Before you report done, verify your own work: open the file, check the console for errors, and confirm every named area is reachable on foot. Only claim what you actually verified."

Interview answers given to both: classic wizard academy, epic-cinematic mood, showpieces =
Great Hall / Library / Towers / Dungeon, ~2-minute day-night cycle.

## Inspirations

- YouTube: [**Claude Fable 5 Prompts You MUST Try Now (or lose $$ next week)**](https://www.youtube.com/watch?v=_WXtkSvIDJs&t=11s)
- Website: [**hogwarts-production.up.railway.app**](https://hogwarts-production.up.railway.app/)

## The contenders

### `index_opus_4.8.html` — Claude Opus 4.8

Rectangular-keep layout: courtyard hub with a great hall, library, watchtower, astronomy
spire, and crypt. AABB collision, ramp stairs, floating candles, fog, 120-second day-night
cycle.

### `index_fable_5.html` — Claude Fable 5

Same six-area topology, rebuilt from scratch: **round towers with true spiral staircases**
(climbed with plain AABB collision via overlapping step floors), canvas-generated procedural
textures (stone, wood, stained glass, star ceiling, banners), shader-gradient sky dome,
glow-sprite torches, ember/dust/firefly particles, a library mezzanine, and a ghost drifting
through the crypt. Self-verified in-browser before delivery: zero console errors, 18/18
reachability waypoints, simulated-player physics tests (gravity, collision, jump, both
spiral stairs climbed on foot), ~6 ms/frame render time.

## Files

| File | What it is |
|---|---|
| `index.html` | Side-by-side comparison page (loads both worlds in frames) |
| `index_opus_4.8.html` | The Opus 4.8 castle |
| `index_fable_5.html` | The Fable 5 castle (Everwyn Academy) |
| `cc1_hogwarts.txt` | The original prompt as used in the session |

Built with [Claude Code](https://claude.com/claude-code).
