# SOLO — a particle river

[![SOLO — the particle river pouring from the wordmark's final O (click to open the live page)](screenshot.png)](https://az9713.github.io/particle-river/)

**[▶ Open the live page](https://az9713.github.io/particle-river/)** — scroll slowly; the river does the rest.

A scrollytelling essay page where a river of ~10,000 canvas particles pours out
of the masthead's final **O**, threads between the text columns, parts around
every paragraph, freezes with pinned cards, fans into a sheet that fills the
title letterforms bottom-up, and plays perfectly in reverse — because scroll is
the clock.

Plain HTML + one CSS file + one JS file + one 2D `<canvas>`. No animation
libraries, no WebGL, no frameworks.

## Inspiration

The technique is a from-scratch reimplementation of the particle-river design
language in Every's article
[**"Before the Deluge"** (every.to/p/openai-infrastructure)](https://every.to/p/openai-infrastructure)
— a beautiful piece of scroll-driven canvas work. All content, copy, and
branding here are original; only the technique is borrowed, with admiration.

- `DESIGN.md` — a full deconstruction of the original's design system
- `RIVER-SECRETS.md` — every trick and how the physics is implemented

## Run it

Serve the folder (any static server) and open `index.html`:

```sh
python -m http.server 8000
# → http://localhost:8000/index.html
```

Opening `index.html` directly from disk also works in most browsers.

## The tricks, in brief

- **Scroll is the clock** — every choreographed value is a pure clamped
  function of scroll position; scrolling up replays everything backwards.
- **Fake fluid** — velocity from the curl of a sum of three sines
  (divergence-free by construction), with the noise phase advected
  downstream so the pattern rides the current instead of shimmering in place.
- **Continuity** — `A·v ≈ const`: where the stream widens into the title
  sheet it slows and pools; the tail below runs narrow and fast.
- **Text avoidance** — a smootherstep divergence field around every text
  block; the stream splits, bows around, and rejoins. Rings around centered
  captions are emergent.
- **The freeze** — a scroll accumulator holds the water still while pinned
  cards are locked, then bleeds the residual back slowly.
- **Title as stones and vessels** — an offscreen-rasterized alpha mask
  deflects the water around the glyphs, then captures dots to fill the
  letters bottom-up.
- **140fps at 10k dots** — `fillRect` squares snapped to the device-pixel
  grid, 8 alpha buckets, zero allocation in the frame loop.

## Tuning

- Type `tune` anywhere on the page (or open with `?tune`) — a hidden panel
  with live sliders for density, flow, coupling, dot size/opacity, band
  width, colors, and type sizes. Settings persist in `localStorage`.
- `?stats` shows an fps / particle / title-fill readout.

## Credits

Technique inspired by [Every](https://every.to)'s "Before the Deluge"
(design and engineering of the original: Every's team). This implementation,
text, and design system: original work.
