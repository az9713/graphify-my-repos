---
repo: claude-design-handoff
description: Claude Design → Claude Code handoff: turning an AI Apple design prototype into a production Next.js + GSAP site. Includes a full deep-dive build report.
language: JavaScript
stars: 1
forks: 0
created: 2026-04-20
updated: 2026-04-30
topics: 
is_fork: False
kb: 6487
---

# claude-design-handoff
# claude-design-handoff

A worked example of taking a **Claude Design** prototype (the HTML/CSS/JS mocks produced at [claude.ai/design](https://claude.ai/design)) and shipping it as a production **Next.js + GSAP** site through **Claude Code**.

The subject: **AI Apple**, a fictional studio for personal AI hardware — glasses, pendants, earbuds, and form factors yet to be invented. The design bundle was exported from Claude Design; this repo is the Claude Code implementation.

## Deep dive: the handoff, demystified

**→ [`BUILD_REPORT.md`](./BUILD_REPORT.md)**

A full, no-steps-skipped write-up of the end-to-end process: parsing the prompt, fetching and decompressing the Claude Design bundle, reading the bundled README and chat transcripts, understanding the Apple design system tokens + brand layer, planning the Next.js port, scaffolding, porting components, designing every GSAP timeline, seven real bugs I hit (strict-mode + GSAP, `yPercent` vs. CSS transforms, `background-clip: text` not inheriting into inline-block children, CSS cascade, rAF throttling on hidden tabs, and more), and how I resolved each.

If you care about *what actually happens* when Claude Code takes a design handoff and turns it into production code, start there.

## The demo

![walkthrough](./docs/animated_web_site_by_cc.compressed.mp4)

The compressed walkthrough lives at [`docs/animated_web_site_by_cc.compressed.mp4`](./docs/animated_web_site_by_cc.compressed.mp4) (H.264, ~4.6 MB, 1280-wide).

## Run it

```bash
npm install
npm run dev
```

Open <http://localhost:3000>.

Production build:

```bash
npm run build
npm start
```

## Stack

- **Next.js 14** (App Router, JSX, no TypeScript)
- **React 18**
- **GSAP 3** + `ScrollTrigger` — all scroll/reveal/parallax motion
- Canvas 2D cinematic hero background — morphing product silhouettes, drifting gold glow, mouse + scroll parallax
- Design tokens ported 1:1 from Apple's public marketing web style (SF Pro stack, binary light/dark, Apple blue accent) and extended with AI Apple's brand forest + gold

## Layout

```
.
├── BUILD_REPORT.md      ← the deep-dive handoff report
├── app/
│   ├── globals.css      ← Apple tokens + brand layer + reveal primitives
│   ├── layout.jsx       ← html shell, metadata, theme-color
│   └── page.jsx         ← composes every section in order
├── components/          ← one client component per section, each owns its GSAP timeline
│   ├── gsap-setup.js    ← single place GSAP + ScrollTrigger are registered
│   ├── Nav.jsx
│   ├── Hero.jsx
│   ├── HeroMotionBG.jsx ← canvas silhouette loop
│   ├── SectionHeader.jsx
│   ├── StatGrid.jsx
│   ├── LogoStrip.jsx
│   ├── Services.jsx
│   ├── Process.jsx
│   ├── CaseStudies.jsx
│   ├── Testimonials.jsx
│   ├── About.jsx
│   ├── FAQ.jsx
│   ├── Contact.jsx
│   ├── FinalCTA.jsx
│   ├── Footer.jsx
│   ├── CursorDot.jsx    ← blend-mode cursor follower (pointer-fine only)
│   └── Visuals.jsx      ← product + scene SVGs
├── public/uploads/      ← assets from the original handoff (founder photo, sketches)
└── docs/                ← design docs, walkthrough video, print PDF
```

## Animation inventory

**Entrance (hero, on mount)**
- Nav brand → links → CTA stagger down
- Pill scale + fade up
- Headline fade up
- Italic gold-gradient em fade up (delayed)
- Subtitle fade up to 0.78 opacity
- CTAs stagger fade up
- Decorative rails: SVG path draw-in via `strokeDashoffset`
- Stat cards stagger fade + scale

**Scroll-triggered per section**
- Eyebrow slides in X
- Title fades up
- Kicker fades up to 0.78
- Grid items stagger with subtle scale

**Scroll-scrubbed**
- Hero content slow upward parallax as you leave
- Hero rails opposite parallax for depth
- Case-study artwork per-card parallax

**Continuous ambient**
- Canvas forest background: morphing silhouettes (glasses → pendant → earbuds → ring), drifting gold glow, secondary cool glow, ambient particles, gold rim-light on the silhouette, mouse-tracked glint, vignette
- Hero pill dot pulses
- Logo strip: infinite edge-faded marquee
- FinalCTA: slow ambient background pan

**Interaction**
- Nav link underline animates in on hover / active
- Gold button hover picks up a gold-tinted shadow
- Feature cards: lift + cursor-follow radial glow (`--mx` / `--my` written from JS)
- Case cards: lift + scale + slight rotation on product SVG
- FAQ: animated `+` rotation, `max-height` accordion
- Team cards: lift on hover
- Cursor dot: grows over interactives

**Scroll-triggered count-ups**
- `+0 → +93%` on the gold stat card
- `0 → 12,593` sessions
- `0 → 94%` retention
- `0 → 82` NPS

**Accessibility**
- `prefers-reduced-motion: reduce` collapses transitions to 0.01ms, disables the marquee, disables the cursor dot, and short-circuits the canvas loop to a single static frame.

## What's intentionally not here

- **Tweaks panel** (theme / accent / nav-layout / type-scale / density switcher). Useful in the Claude Design prototype; a prototype-side tool, not a production feature.
- **Print version** (the prototype had an `AI Apple-print.html`). A PDF of that build is in [`docs/AI Apple — Print.pdf`](./docs/).
- **Multi-page routing**. The design is one long-scroll page with in-page anchors, as specified in the original chat.

## License

The port (code in `app/`, `components/`, `public/`) is provided as-is for reference. AI Apple is a fictional brand; none of the copy, imagery, or brand marks imply a real product.

---

For the actual step-by-step play-by-play of how this was built, read **[`BUILD_REPORT.md`](./BUILD_REPORT.md)**.
