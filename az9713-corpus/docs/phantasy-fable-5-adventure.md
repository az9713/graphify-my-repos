---
repo: phantasy-fable-5-adventure
description: A tiny action RPG in one HTML file — procedural worlds, perfect-dodge combat, daily seeds & ghost replays. Built in Claude Code with Fable 5.
language: HTML
stars: 0
forks: 0
created: 2026-07-14
updated: 2026-07-14
topics: 
is_fork: False
kb: 11870
---

# phantasy-fable-5-adventure
# Phantasy Codex Adventure — Local Edition

A compact top-down action RPG in the Game Boy Color spirit — procedural worlds, telegraphed
real-time combat, roguelite builds, and a daily challenge — shipped as **one HTML file**.
No install, no dependencies, no assets, no internet. Double-click and play.

![Trailer](phantasy-codex-trailer.gif)

## Play it

**▶ [Play in your browser right now](https://az9713.github.io/phantasy-fable-5-adventure/)** — nothing to install.

Or run it locally:

1. Download (or clone) this repo.
2. Open **`index.html`** in any modern browser. That's it.

New to games? There's a gentle **[player's guide for absolute beginners](MANUAL.html)** —
it even explains what "WASD" means.

**Quick controls:** move <kbd>WASD</kbd>/<kbd>arrows</kbd> · attack <kbd>J</kbd> ·
dodge <kbd>K</kbd> · weapons <kbd>1</kbd><kbd>2</kbd><kbd>3</kbd> · interact <kbd>E</kbd> ·
character sheet <kbd>C</kbd> · pause <kbd>P</kbd> · mute <kbd>M</kbd>

## What makes it fun

- **Telegraphed combat + perfect dodge** — every enemy attack paints a ground marker first.
  Dodge at the last instant and time slows, your stamina refunds, and your next hits crit.
- **Kill streaks** — chain kills within 4 seconds for up to **×5 XP**, with escalating jingles.
  Getting hit resets it.
- **Synergy builds** — level-up cards combo through shared tags, and the game flags the combos
  for you (*"heal off every arc"*). Lifesteal bruiser, chain-mage, bleed-stacker — your call.
- **Cursed chests & blood altars** — opt-in gambles: survive an elite ambush for rare loot, or
  trade 30% max HP for a boon.
- **Elite affixes** — Giant, Hasted, Vampiric, Shielded, Splitting, Explosive, Frost, Thorns —
  read the name tag and adapt.
- **A world that fights with you** — knock enemies into water and spikes, ignite grass and watch
  fire spread, bait monsters into fighting each other.
- **Day/night cycle** — night is deadlier but pays ×1.5 XP.
- **Daily challenge & ghost replay** — everyone gets the same world each day (seeded procedural
  generation), and the translucent ghost of your best run races you through it.

All artwork is pixel art generated in code and every sound is synthesized with the Web Audio
API — the entire game, engine, art, and music live in a single `index.html`.

## Verify it yourself

Open **`index.html?test=1`** to run the built-in self-test suite — 22 assertions covering world
determinism, damage math, streak logic, persistence round-trips, and more.

## Documentation

| Doc | What's inside |
|---|---|
| [DOCUMENTATION.md](DOCUMENTATION.md) | Full implementation journey — architecture, asset pipeline, every bug found in testing and how it was fixed |
| [NEW_FEATURES.md](NEW_FEATURES.md) | The ten mechanics added beyond the original game, with an honest comparison |
| [MANUAL.html](MANUAL.html) | Player's guide for people who have never played a video game |
| [PLAN.md](PLAN.md) | The phased implementation plan the build followed |
| [PROMPT.txt](PROMPT.txt) | The single prompt the game was built from |

## Credits

- Inspired by — and a local, self-contained re-imagining of — **[Phantasy Codex Adventure](https://developers.openai.com/showcase/phantasy-codex-adventure)**
  from the OpenAI showcase, built by Thomas Ricouard with Codex + GPT-5.6. The original's
  ChatGPT-Sites leaderboard and AI-generated artwork are replaced here with a daily-seed
  local leaderboard and code-drawn pixel art, so everything runs offline.
- This edition was **designed, developed, and end-to-end tested in
  [Claude Code](https://claude.com/claude-code), powered by Fable 5** (Anthropic) — including
  the gameplay choreography and browser-recorded trailer above.
- Game Boy Color inspiration: *Final Fantasy Adventure* and *Sword of Mana*.
