---
repo: astryx-demo
description: Hands-on, educational showcase of Meta's Astryx design system + a reverse-engineered astryx-max Claude Code skill
language: TypeScript
stars: 0
forks: 0
created: 2026-07-04
updated: 2026-07-04
topics: 
is_fork: False
kb: 1392
---

# astryx-demo
# Astryx Demo — exploring Meta's design system (and building `astryx-max`)

A hands-on, educational showcase of **[Astryx](https://github.com/facebook/astryx)**, Meta's open-source, agent-first design system. It's a small analytics dashboard built with Astryx + Vite + React, wired with three interactive demos that make the *invisible* value of a design system visible — plus a Claude Code skill we reverse-engineered, called **`astryx-max`**, for pushing an Astryx build past "generic."

> **For new users.** The goal here is to **educate, showcase, and explore**. Read the journey, run the app, click the toggles, and you'll understand *what a design system actually buys you* — not from a screenshot, but from watching change happen cheaply.

- **Astryx repo:** https://github.com/facebook/astryx
- **Inspiration (walkthrough video):** https://www.youtube.com/watch?v=-HEdqzzYKco (AI Labs)
- This project was built collaboratively with **Claude Code** as a live coding + design session; the README doubles as a lab notebook of the real turns and gotchas.

## ▶ Live demo

### **https://az9713.github.io/astryx-demo/**

The dashboard below is running live — **click any screenshot to open the real, interactive app** (toggle the themes, flip Raw/Refined, switch dark mode).

[![Astryx demo — refined analytics dashboard, neutral theme](docs/01-refined-neutral.png)](https://az9713.github.io/astryx-demo/)

---

## Table of contents

1. [Quickstart](#quickstart)
2. [The three demos (how to showcase Astryx)](#the-three-demos)
3. [Primer: what's a design system, a token, a token set?](#primer)
4. [What Astryx buys you / what `astryx-max` buys you](#what-it-buys)
5. [Building our own `astryx-max`](#building-astryx-max)
6. [The development journey (turns & nuances)](#the-journey)
7. [How we test Astryx](#how-we-test)
8. [Project structure](#project-structure)
9. [Honest caveats](#caveats)

---

## Quickstart

**Prerequisites:** Node.js **≥ 22.13** (Astryx's minimum), npm.

```bash
npm install
npm run dev
# open the localhost URL it prints (e.g. http://localhost:5173)
```

You'll see the **Acme Analytics** dashboard. In the header:

- **Neutral / Butter / Y2K** — reskin the entire dashboard live (Demo 1).
- **Raw / Refined** — toggle the stock template vs. the `astryx-max` pass (Demo 2).
- **Dark** — flip light/dark mode (one prop).

---

## The three demos

The dashboard itself is unremarkable on purpose — the point isn't the picture, it's what happens when you *change* something.

### Demo 1 — Theming (what Astryx centralizes)
Click **Neutral → Butter → Y2K**. The whole surface — every card, chart, table, and sparkline — reskins together: colors, fonts, corner radius, chart gridlines. **No component code changes.** `src/DashboardTemplate.tsx` is byte-for-byte identical across all three looks.

Why it works: every component reads its appearance from a **theme** (a set of design tokens) instead of hardcoding colors/fonts. Swap the theme object and everything follows — completely, with nothing left behind. The switcher is ~15 lines in `src/App.tsx`; Astryx provides the swappable themes and the 150+ components pre-wired to them.

> The value isn't "users can pick a theme." It's that **rebranding or restyling later costs one line instead of an afternoon of find-and-replace CSS — and never drifts.**

The same dashboard, same code, under two other themes — each is *one import line* (click to open live):

| Butter | Y2K |
|:---:|:---:|
| [![Butter theme](docs/03-refined-butter.png)](https://az9713.github.io/astryx-demo/) | [![Y2K theme](docs/04-refined-y2k.png)](https://az9713.github.io/astryx-demo/) |

### Demo 2 — `astryx-max` (pushing past generic)
Toggle **Raw ↔ Refined**.
- **Raw** = the stock Astryx `dashboard` template: chart-first, four equal-weight metric cards.
- **Refined** = after our `astryx-max` pass: KPI-first hierarchy, one **hero** metric + three recessed (`muted`) supporting cards, chart below.

Every refinement stays **token-driven**, so Refined still reskins with Demo 1's themes and flips with dark mode. (Try Refined + Y2K + Dark together.)

| Raw — stock template (chart-first, 4 equal cards) | Refined — `astryx-max` (KPI-first, hero + muted) |
|:---:|:---:|
| [![Raw dashboard](docs/02-raw-neutral.png)](https://az9713.github.io/astryx-demo/) | [![Refined dashboard](docs/01-refined-neutral.png)](https://az9713.github.io/astryx-demo/) |

### Demo (bonus) — Dark mode
Click **Dark**. One `mode` prop on `<Theme>` re-tokenizes the entire surface. Hand-rolled, dark mode is a project; here it's free because components read from tokens.

[![Dark mode](docs/05-refined-neutral-dark.png)](https://az9713.github.io/astryx-demo/)

---

## Primer

**Design system** — a library of reusable UI components plus the shared rules (spacing, color, type, elevation) that keep them consistent. You compose screens from the parts instead of hand-writing CSS.

**Token** — a *named design decision*. Instead of `color: #1a1a1a`, a component asks for the token named `text-primary`. The name is the token.

**Token set (theme)** — the full list of what every token name equals for one look. Think of it as a shelf of labeled paint buckets: components ask for labels (`accent`, `surface`, `font-body`), the theme decides what's in each bucket. Swap the shelf → every component repaints at once. **That's the entire trick behind Demo 1.**

You can see real token names in `src/DashboardTemplate.tsx`, e.g. `var(--color-data-categorical-blue, …)` and `var(--font-size-sm, …)`.

---

## What it buys

### What Astryx buys you
- **You don't build primitives.** Cards, tables, charts, progress bars, a responsive grid, spacing, type hierarchy, accessibility — all shipped. We wrote ~50 lines of app shell; the rest came from `npx astryx template dashboard`.
- **Consistency you can't drift from** — every component reads one source of truth.
- **Theming & dark mode for one prop** — Demo 1 and dark mode.
- **An agent-friendly API** — the CLI (`npx astryx manifest / search / component / template`) gives an AI the *real* component list and props to build from, instead of hallucinating class-name soup. This is Astryx's genuinely differentiated pitch.

### What `astryx-max` buys you (honestly)
On this project, `astryx-max`'s biggest wins were **not** a facelift — the Meta template was already competent. They were:
1. **Catching a real bug via screenshots** — the "Active users" chart rendered *empty* (a data/axis bug a text-only agent ships blind). The look-at-the-page loop caught it.
2. **Avoiding an anti-pattern** — grounding on Astryx's own `Badge` docs steered us *away* from putting a colored trend pill on every card ("if all show green, none stand out").
3. **Iterating on layout** — the critique loop caught an awkward stretched-thin hero sparkline and reworked it into a two-column featured card.

The Raw→Refined aesthetic delta is real but **modest**, precisely because we started from a good template. `astryx-max` shines brightest on *from-scratch* builds (where agents produce genuine slop) and as a **bug-catching + anti-pattern-avoidance** loop — arguably more valuable than polish.

---

## Building `astryx-max`

`astryx-max` is a **Claude Code skill**, reverse-engineered from the behavior described in the [YouTube walkthrough](https://www.youtube.com/watch?v=-HEdqzzYKco) (AI Labs' own "Astryx Max" is proprietary; this is an open educational reconstruction of the *mechanism*, not their files). It lives in [`.claude/skills/astryx-max/`](.claude/skills/astryx-max) — clone this repo, open it in Claude Code, and the skill is available.

**What it does (the workflow in `SKILL.md`):**
1. **Ground** on the CLI capability manifest (`npx astryx manifest --json`) so the model builds from real commands/flags/components instead of guessing.
2. **Discover** existing templates/components (`search`, `component`, `template`).
3. **Build** against `references/design-rules.md` (positive rules derived from the specific ways Astryx builds look generic).
4. **Render & look** — drive a headless browser, screenshot the running page.
5. **Critique** against `references/review-rubric.md` + `references/slop-patterns.md`.
6. **Fix & loop** (up to 3 rounds).
7. **Verify** — objective evals (no console errors, non-default palette, real heading hierarchy, responsive).

**Files:**
```
.claude/skills/astryx-max/
├── SKILL.md                     the 7-step workflow + trigger description
└── references/
    ├── design-rules.md          how to build so it isn't generic
    ├── slop-patterns.md         the "AI slop" tells to detect & remove
    └── review-rubric.md         screenshot grading + final eval checklist
```

The skill is designed to **grow**: when something still looks AI-made, you add the pattern to `slop-patterns.md`. (This session already added a note to `review-rubric.md` — see the journey below.)

---

## The journey

The interesting part — the real turns, in order. Every gotcha below actually happened.

1. **Verify before installing (supply-chain caution).** Before running any `npm install`, we confirmed the packages were genuinely Meta's — checked the npm registry metadata (maintainers include `fb <opensource+npm@fb.com>` and `astryxdesign@meta.com`, repo `facebook/astryx`). A package name alone is never proof.
2. **Install.** `@astryxdesign/core`, `@astryxdesign/theme-neutral`, and `@astryxdesign/cli` (dev). The CLI is the agent's bridge to the library.
3. **The Next.js `pages/` vs `app/` gotcha** (from the video). `astryx init`'s template installs into a `pages/` folder (old Pages Router); modern Next.js uses `app/` (App Router); the two can't coexist for the same routes. Not relevant here (we used Vite), but documented in `CLAUDE.md` so future work doesn't trip on it.
4. **StyleX is *not* required.** A common misconception: you don't need a StyleX build plugin to *use* Astryx. Components get their look from theme CSS/tokens via `<Theme>` (runtime injection) + `@astryxdesign/core/reset.css` + `astryx.css`. StyleX is only for authoring *custom* overrides. This made a plain Vite setup viable.
5. **Babel v7-vs-v8 conflict.** Astryx's CLI drags in `@babel/core@7` (via `jscodeshift`); the newest `@vitejs/plugin-react` wanted `@babel/core@8` → `ERESOLVE`. Fix: use `@vitejs/plugin-react-swc` (SWC, no Babel) — the conflict vanishes.
6. **recharts v2 vs v3.** The template targets recharts v2's axis API; npm pulled v3. Pinned `recharts@^2.15`.
7. **The empty-chart saga (two bugs hiding as one).** The "Active users" chart rendered empty.
   - Bug A (real): the `XAxis` `domain={[0, 23]}` while the data's `hour` runs 0–95 — three-quarters of the data plotted off-axis. Fixed to `[0, 95]`.
   - "Bug" B (a false alarm): even after the fix, screenshots looked empty. It was recharts' **entrance animation** — the line's clip-path expands from zero over ~1.5s, so a screenshot taken during mount shows axes but no line. The sparklines (which set `isAnimationActive={false}`) showed instantly, which is what gave it away. **Lesson banked into the skill** (`review-rubric.md`): wait for chart animations before grading, or you'll report a non-bug.
8. **Dark mode = one prop** — `<Theme mode="light|dark">`, wired to a toggle.
9. **Demo 1** — added a theme switcher (Neutral/Butter/Y2K) to prove token-swapping.
10. **Demo 2** — ran `astryx-max` on the dashboard: grounded on the manifest, applied KPI-first hierarchy + hero/muted cards, deliberately avoided badge-spam, and fixed the hero sparkline in one critique loop — all kept token-driven so it still themes.

---

## How we test

Testing an Astryx build (and the `astryx-max` loop) is **visual and behavioral**, not just "does it compile":

- **Drive a real browser.** Start the dev server, load the page in a headless/automated browser, take screenshots at desktop *and* mobile widths. A `.tsx` that compiles can still render an empty chart — you only catch that by looking.
- **Read the console.** Errors mean the build is broken; grade the picture only after the console is clean. (Tip: browser-extension noise like `mce-autosize-textarea` is not your app.)
- **Inspect the DOM when a screenshot lies.** When the chart looked empty, we queried the SVG directly — the line `<path>` existed with valid geometry and a blue stroke, which is what pointed us at *animation timing*, not a data bug.
- **Grade against a rubric.** `astryx-max`'s `review-rubric.md`: alignment, spacing, hierarchy, depth, palette, copy, responsive — each pass/fail with a concrete note, then cross-checked against `slop-patterns.md`.
- **Toggle-driven manual demos.** The Raw/Refined and theme toggles double as a test surface: flip them and confirm nothing breaks and everything re-themes.

---

## Project structure

```
.
├── index.html                    Vite entry
├── vite.config.mjs               React (SWC) plugin
├── src/
│   ├── main.tsx                  mounts app + Astryx base CSS
│   ├── App.tsx                   <Theme> + Demo 1 (themes) + Demo 2 (Raw/Refined) + dark
│   └── DashboardTemplate.tsx     Astryx `dashboard` template; takes `refined?: boolean`
├── .claude/skills/astryx-max/    the reverse-engineered skill (see above)
├── .github/workflows/deploy.yml  builds + deploys to GitHub Pages on every push to main
├── docs/                         README screenshots
├── CLAUDE.md                     project notes, incl. the pages/app gotcha
└── README.md                     you are here
```

**Live deployment:** pushing to `main` triggers a GitHub Actions workflow that runs `npm ci && npm run build` and publishes `dist/` to GitHub Pages at the URL above. `vite.config.mjs` sets `base: '/astryx-demo/'` for the build so assets resolve under the Pages sub-path (local `npm run dev` stays at `/`).

Key libraries: `@astryxdesign/core`, `@astryxdesign/theme-{neutral,butter,y2k}`, `@astryxdesign/cli` (dev), `recharts@^2`, `@heroicons/react`, `vite` + `@vitejs/plugin-react-swc`.

---

## Caveats

- **Astryx is beta** (v0.1.x). APIs and templates may change.
- **`astryx-max` is an educational reconstruction**, not AI Labs' proprietary skill. It reproduces the *mechanism* (manifest grounding + screenshot-critique-fix loop + slop checklist) described in their video, from scratch.
- **The Raw→Refined delta is intentionally modest** — see [What it buys](#what-it-buys). Don't read this repo as "the skill makes everything gorgeous"; read it as "here's an honest look at where an agent-first design workflow helps."
- One small non-Astryx line: the hero card uses a raw `<div style={{flex…}}>` wrapper because recharts' `ResponsiveContainer` needs a sized parent. Flagged for honesty.

---

## License

[MIT](LICENSE) © 2026 az9713 — covering this project's original work (the app shell, the `astryx-max` skill, and the refinements).

Note: `src/DashboardTemplate.tsx` is derived from Astryx's `dashboard` template and remains **© Meta Platforms, Inc.** under Astryx's own [MIT license](https://github.com/facebook/astryx) — its copyright header is left intact. React, Vite, recharts, and heroicons are likewise MIT.

## Credits

- **Astryx** — Meta / Facebook open source: https://github.com/facebook/astryx
- **Walkthrough video** — AI Labs: https://www.youtube.com/watch?v=-HEdqzzYKco
- Built with **Claude Code**.

Explore, fork, and swap a theme. If it still looks AI-made somewhere, that's a pattern for `slop-patterns.md`.
