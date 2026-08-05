# Orikata — a folded journey through Japan 🏮

A scroll-scrubbed **"fly through the world"** landing page for a fictional boutique Japan travel
brand. As you scroll, a pre-rendered camera flies as one continuous take — glide to a vermillion
**torii** on a misty shore, push *through* the gate into a lantern-lit **ryokan**, then out through
the shoji screen to a mountain **onsen** at dusk. Every scene is hand-folded origami paper,
AI-generated and frame-locked into a single seamless flight.

Built in one session with **Claude Fable 5** driving the
[`scroll-world`](https://github.com/cth9191/scroll-world) skill and the **Higgsfield MCP** — total
cost **81 Higgsfield credits**.

---

## 🌐 Live demo

**▶ [az9713.github.io/scroll-world-demo](https://az9713.github.io/scroll-world-demo/)** — the
`index.html` rendered live via GitHub Pages. Scroll to fly through the world.

[![Orikata — live landing page (click to open the live site)](assets/scene1_arrival.png)](https://az9713.github.io/scroll-world-demo/)

*↑ Click the diorama to open the live, scrollable site.*

---

## 🎬 The 24-second journey (video)

[![▶ Play — Orikata: a 24-second continuous origami flight](assets/journey-thumb.png)](https://az9713.github.io/scroll-world-demo/orikata-journey.mp4)

*↑ Click to play `orikata-journey.mp4` — the whole flight concatenated into a standalone short.
(Opens the video hosted on GitHub Pages, which plays in the browser; GitHub's own file viewer
refuses to stream a file this size.)*

---

## 🙏 Credits & inspiration

This demo was made following the technique shown in Pat Simmons' video:

> **[This Skill Turns Fable 5 & GPT 5.6 Into Web Design MONSTERS](https://www.youtube.com/watch?v=KBH8P0z2AL8&t=313s)**

The `scroll-world` skill it showcases:

- **Original** by Peter Wang — [github.com/oso95/scroll-world](https://github.com/oso95/scroll-world)
- **Fork (used here)** by Chase AI — [github.com/cth9191/scroll-world](https://github.com/cth9191/scroll-world), which adds the credit/spend controls (budget tiers, anchor-still gate, spend estimate, idempotent pipeline, SSIM seam gate) that made this run viable on a limited credit balance.

---

## 📦 What's inside

| File | What it is |
|------|-----------|
| `index.html` | The landing page — mounts the scrub engine, themed in the serene washi palette, with an SEO copy block for crawlers. |
| `scrub-engine.js` | Portable, dependency-free vanilla-JS scroll-scrub engine (from the skill). Blob-loads clips, maps scroll → `video.currentTime`, crossfades seams, hardens mobile. |
| `orikata-journey.mp4` | The 3 legs concatenated into a 24.1s standalone video. |
| `assets/vid/*.mp4` | The 3 encoded camera-flight legs (720p, crf20, `-g8`). |
| `assets/*.webp` | Scene stills + loading posters (posters = each encoded clip's first frame). |
| `DEVELOPMENT_JOURNEY.md` | Full build log: the brief, every decision fork, models, costs, and artifacts. |

## ▶️ Run it locally

The engine blob-loads clips, so it works on any static server:

```bash
python -m http.server 8817
# open http://localhost:8817/index.html
```

## 🎨 How it was made (short version)

1. **Interview** → boutique Japan travel brand, origami / serene / calm.
2. **3 scene stills** with `gpt_image_2` (2k) — anchor-gated for a locked style, washi palette.
3. **3 video legs** with `seedance_2_0_mini` (720p, 8s), **architecture A**: each leg starts from
   the previous leg's *actual last frame*, so the seams are frame-continuous — one continuous
   forward flight, no cuts.
4. **Encode + posters + SSIM seam gate**, assemble the page, concat the standalone mp4, QA in a
   headless browser.

## 💳 Working within credit limits

This was built on a **limited Higgsfield credit balance** (a Starter plan), and that constraint —
not aesthetics — drove most of the technical choices:

- **Lean 3-scene journey**, not the 6–7 scenes a showcase run uses. Fewer scenes = far fewer paid
  generations; the saved budget becomes a re-roll cushion. Each scene gets more scroll dwell so
  three beats still read as a complete world.
- **Architecture A (continuous forward take)**, which needs no separate "connector" clips — every
  connector avoided is a video generation not paid for.
- **`seedance_2_0_mini` at 720p for the video**, instead of `seedance_2_0` at 1080p. Two reasons:
  the full model is **gated to Pro/Ultimate plans** (it returns a 403 on Starter), *and* it costs
  several times more per clip. Mini still frame-locks seams, so the flight stays seamless — it's a
  cheaper model, not a worse result for this low-motion, serene content.
- **`gpt_image_2` for the stills**, anchor-gated: one still is approved first and reused as the
  style reference, so a style miss costs a single image generation rather than the whole batch.
- **Every generation was cost-preflighted** before spending, and the pipeline is idempotent, so a
  crash or re-roll never re-pays for finished work.

The whole run came in comfortably under budget with credits left over for re-rolls.

Full details — the exact ledger, all 13 decision forks, and honest limitations — are in
**[DEVELOPMENT_JOURNEY.md](DEVELOPMENT_JOURNEY.md)**.

---

*Landing-page technique is the same one behind Apple's scroll-through product pages: the camera
genuinely moves, scroll only drives time.*
