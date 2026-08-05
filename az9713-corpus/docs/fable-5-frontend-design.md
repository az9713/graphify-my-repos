---
repo: fable-5-frontend-design
description: Five fundamentally different showcase websites designed and built autonomously by Claude (Fable 5) — variable fonts, three.js, AI imagery, Web Audio, raw GLSL. Live on Netlify.
language: HTML
stars: 0
forks: 0
created: 2026-07-09
updated: 2026-07-09
topics: 
is_fork: False
kb: 333
---

# fable-5-frontend-design
# Fable 5 Frontend Design Showcase

Five websites, each fundamentally different in aesthetic and technique, designed and built **entirely autonomously by Claude (Fable 5)** — concept, art direction, copywriting, code, iteration, and deployment. No frameworks, no build steps: every site is a single self-contained HTML file (plus generated image assets for one of them).

## The five sites

| # | Site | Live | Technique showcase |
|---|------|------|--------------------|
| 01 | **KILTER** — a type foundry specimen | [kilter-type.netlify.app](https://kilter-type.netlify.app) | Variable fonts as UI: cursor **velocity** drives `font-variation-settings` (fast cursor = the typeface "loses its composure"), a contenteditable type tester, hover-reactive glyph grid |
| 02 | **HADAL** — a descent to the deepest water on Earth | [hadal-descent-218.netlify.app](https://hadal-descent-218.netlify.app) | Scroll position maps to depth (0 → 10,935 m); one scalar drives three.js particles, fog/background color ramp, and a live instrument HUD (pressure, light, temperature) |
| 03 | **KANOE** — a Kyoto incense atelier | [kanoe-atelier.netlify.app](https://kanoe-atelier.netlify.app) | AI photography as art direction: three Higgsfield Soul images with a consistent lighting vocabulary, dissolved into the layout with gradients; vertical kanji, quiet-luxury restraint |
| 04 | **VOLTAIC VLT-3** — a pocket synthesizer | [voltaic-vlt3.netlify.app](https://voltaic-vlt3.netlify.app) | The product page **is** the product: a playable subtractive synth in raw Web Audio — draggable CSS knobs, look-ahead-scheduled 8-step sequencer, oscilloscope, factory presets |
| 05 | **PRISMA** — a festival of light | [prisma-light.netlify.app](https://prisma-light.netlify.app) | A live aurora in ~80 lines of raw GLSL (domain-warped fbm) that bends toward your cursor; glassmorphism UI over the shader; SVG grain to kill banding |

Every site has a **`/guide` route** describing exactly how it was built — the one idea, the techniques worth stealing, and a prompt recipe to reproduce the workflow with your own model.

## How this was made

The entire project ran from a single prompt ([`prompt2.txt`](prompt2.txt)) with full creative autonomy:

1. **Divergent concepting.** Five subjects chosen so no two share a palette, typeface, or core technology (variable fonts / WebGL 3D / generated imagery / Web Audio / fragment shaders) — deliberately avoiding the default "AI look."
2. **Asset generation.** Site 03's photography was generated via the Higgsfield MCP (Soul model), art-directed with consistent lighting language across prompts. Total cost: under 1 credit.
3. **Three iteration passes per site.** Each pass = load the site in a real browser (Chrome DevTools MCP), screenshot desktop + mobile, read the console, and fix what's actually wrong. Passes caught real bugs: an instrument HUD invisible against sunlit water, square particles that should be round, a hero hint anchored to the wrong container, a mobile nav clipping off-screen, an unplayably cramped keyboard.
4. **Deploy + verify.** Each folder deployed as its own Netlify site via CLI; all 10 routes (5 sites × home + guide) verified over HTTP, plus a production render check with a clean console.

## Quality floor (all sites)

- Responsive to 360 px, touch-friendly targets
- `prefers-reduced-motion` respected (shaders freeze to a still frame, particles stop)
- Visible `:focus-visible` outlines; knobs/keys/steps keyboard-operable on the synth
- No-JS and no-WebGL fallbacks (content is plain HTML; canvases degrade to gradients)
- External scripts pinned with Subresource Integrity; images sized to prevent layout shift

## Repo structure

```
sites/
  01-kilter/    index.html + guide/
  02-hadal/     index.html + guide/
  03-kanoe/     index.html + guide/ + assets/ (generated .webp)
  04-voltaic/   index.html + guide/
  05-prisma/    index.html + guide/
prompt2.txt     the prompt that started it all
```

Deploy any folder anywhere that serves static files — there is no build step.

## Credits

- **Inspiration:** the YouTube video ["Fable 5 Is Back. Use It To Print With These $10K Websites"](https://www.youtube.com/watch?v=h6G9R4UxR6g&t=42s), which sparked the idea of a one-prompt autonomous website showcase
- **Design & code:** Claude (Fable 5) by Anthropic, running in Claude Code — autonomously, per the prompt's instructions
- **Imagery (site 03):** Higgsfield Soul via MCP
- **Fonts:** Google Fonts (Recursive, Instrument Serif/Sans, IBM Plex Mono, Shippori Mincho B1, Zen Kaku Gothic New, Space Grotesk/Mono, Unbounded, Manrope)
- **3D (site 02):** three.js r128
- **Hosting:** Netlify

All brands on these sites (Oddity Type Co., HADAL, KANOE, VOLTAIC, PRISMA) are fictional.
