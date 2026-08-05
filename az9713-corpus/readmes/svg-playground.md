# SVG Playground

**46 interactive demos proving SVG is code, not just another image format.**

<!-- Badges (fill in URLs when you have a live deployment) -->
![Status](https://img.shields.io/badge/status-active-brightgreen)
![Node](https://img.shields.io/badge/node-18%2B-blue)
![License](https://img.shields.io/badge/license-MIT-lightgrey)

https://github.com/user-attachments/assets/932a0399-8e13-4066-ab1e-6c3e5cddcd20

---

## What is this?

Most developers think of SVG as a file you export from Illustrator and drop into an `<img>` tag.
That mental model undersells it enormously.

SVG is a full XML-based programming environment living inside the browser:

- Geometry is declared in code, so it scales to any resolution without a single blurry pixel
- Every element is in the DOM — you can query, mutate, animate, and bind events to shapes the same way you would a `<div>`
- Filters, gradients, masks, and clipping paths compose like functions
- SMIL lets you declare animations in markup with no JavaScript at all
- Accessibility attributes (`role`, `aria-label`, `<title>`, `<desc>`) make graphics readable by screen readers
- The format is plain text, so file sizes are tiny and diffs are human-readable

SVG Playground is a hands-on tour of all of it. Each of the 46 demos isolates one capability, lets you see the live SVG source, and invites you to edit the code and watch the result update in real time.

---

## Quick Start

**Prerequisites:** Node.js 18 or newer, npm

```bash
# 1. Clone the repository
git clone <repo-url>
cd svg-playground

# 2. Install dependencies
npm install

# 3. Start the dev server (opens in your browser automatically)
npm run dev
```

The hub page at `http://localhost:5173` lists all 46 demos with search and category filtering.
Click any card to open the demo with the live code editor and SVG inspector available.

---

## Available Scripts

| Command | What it does |
|---|---|
| `npm run dev` | Start Vite dev server with hot reload, opens browser |
| `npm run build` | Generate `demos-catalog.json` then bundle everything to `dist/` |
| `npm run preview` | Serve the production build locally for final checks |
| `npm run catalog` | Regenerate `demos-catalog.json` without a full build |
| `npm run new-demo` | Scaffold a new demo from the template (see below) |

---

## Project Structure

```
svg-playground/
|
|-- index.html                  # Hub/gallery page (entry point)
|-- vite.config.js              # Vite config — auto-discovers all demos
|-- package.json
|-- demos-catalog.json          # Auto-generated list of all demos (do not edit)
|
|-- demos/                      # One folder per demo
|   |-- _template/              # Starter template for new demos
|   |   |-- index.html          # Demo page structure
|   |   |-- demo.js             # Demo logic (imports shared contract)
|   |   `-- manifest.json       # Metadata: title, category, difficulty, etc.
|   |
|   |-- 01-infinite-scaling/    # Each demo follows the same layout
|   |-- 02-file-size/
|   |-- ...                     # 03 through 46
|   `-- 46-svg-vs-photo/
|
|-- shell/                      # The outer UI that wraps demos
|   |-- shell.js                # Hub logic, iframe management, routing
|   |-- shell.css               # Shell styles
|   |-- code-panel.js           # Live CodeMirror editor panel
|   |-- inspector.js            # SVG element inspector (DevTools-like)
|   `-- skins/                  # SVG skin files
|       |-- default.svg         # "Midnight" dark theme
|       `-- minimal.svg         # Clean light theme
|
|-- shared/                     # Code shared between shell and demos
|   |-- demo-contract.js        # postMessage protocol + iframe helpers
|   |-- svg-utils.js            # Small SVG utility functions
|   `-- styles/
|       |-- reset.css           # CSS reset
|       `-- demo-chrome.css     # Common demo page styles
|
`-- scripts/
    |-- build-catalog.js        # Scans demos/ and writes demos-catalog.json
    `-- new-demo.js             # Scaffolds a new demo from _template
```

---

## The 46 Demos

### Core Differentiators (1-4)
What makes SVG fundamentally different from raster images.

| # | Demo | What you will see |
|---|---|---|
| 01 | Infinite Scaling | SVG vs PNG side-by-side at any zoom — zero pixelation |
| 02 | File Size | SVG markup vs equivalent PNG byte counts |
| 03 | View Source | The live DOM of an SVG, editable in place |
| 04 | Resolution Independence | One file, every screen density |

### Shapes & Paths (5-6)
| # | Demo | What you will see |
|---|---|---|
| 05 | Path Commands | Interactive path `d` attribute builder |
| 06 | Shape Primitives | Every basic shape element with live controls |

### Paint & Style (7-10)
| # | Demo | What you will see |
|---|---|---|
| 07 | Gradient Studio | Linear and radial gradient editor |
| 08 | Pattern Creator | `<pattern>` tile designer |
| 09 | Stroke Explorer | Stroke dasharray, linecap, linejoin playground |
| 10 | CSS Restyler | Apply CSS classes and custom properties to SVG |

### Text (11-13)
| # | Demo | What you will see |
|---|---|---|
| 11 | Text on Path | Typography flowing along any SVG path |
| 12 | Living Text | SVG text animated with filters and transforms |
| 13 | Text Animation | Letter-by-letter and word-level animation |

### Transforms & Coordinates (14-16)
| # | Demo | What you will see |
|---|---|---|
| 14 | ViewBox Explorer | How viewBox and preserveAspectRatio work |
| 15 | Transform Playground | translate, rotate, scale, skew in real time |
| 16 | Nested Worlds | SVG inside SVG with independent coordinate systems |

### Filters & Effects (17-21)
| # | Demo | What you will see |
|---|---|---|
| 17 | Filter Pipeline | Build `<filter>` chains from primitives |
| 18 | Turbulence Lab | feTurbulence for textures, clouds, and distortion |
| 19 | Lighting Studio | feDiffuseLighting and feSpecularLighting |
| 20 | Blend Modes | feBlend and feComposite mixing modes |
| 21 | Displacement Warper | feDisplacementMap for liquid and warp effects |

### Animation (22-25)
| # | Demo | What you will see |
|---|---|---|
| 22 | SMIL Animator | Declarative animation with no JavaScript |
| 23 | CSS Motion | CSS transitions and keyframes on SVG elements |
| 24 | Motion Path | Elements travelling along an SVG path |
| 25 | Shape Shifter | Morphing between path shapes |

### Interactivity (26-29)
| # | Demo | What you will see |
|---|---|---|
| 26 | DOM Surgery | Live add, remove, and reorder SVG elements |
| 27 | Event Playground | Mouse, touch, and pointer events on shapes |
| 28 | Drag & Drop Builder | Compose a scene by dragging SVG parts |
| 29 | HTML Inside SVG | `<foreignObject>` embedding HTML inside SVG |

### Composability & Reuse (30-32)
| # | Demo | What you will see |
|---|---|---|
| 30 | Symbol Library | Define once with `<symbol>`, reuse with `<use>` |
| 31 | Clip Path | `<clipPath>` for precise masking |
| 32 | Mask Workshop | `<mask>` with luminance and alpha channels |

### Data-Driven (33-35)
| # | Demo | What you will see |
|---|---|---|
| 33 | Data → Chart | JSON in, live SVG charts out |
| 34 | Generative Art | Algorithmic SVG from code |
| 35 | Interactive Map | SVG as a data-bound geographic canvas |

### Accessibility (36-37)
| # | Demo | What you will see |
|---|---|---|
| 36 | Screen Reader View | `<title>`, `<desc>`, ARIA roles in SVG |
| 37 | Motion Respect | `prefers-reduced-motion` in SVG animations |

### Performance (38-39)
| # | Demo | What you will see |
|---|---|---|
| 38 | SVG Optimizer | Paste SVG, see cleaned and minified output |
| 39 | Complexity Profiler | Element count and render cost visualised |

### Meta (40)
| # | Demo | What you will see |
|---|---|---|
| 40 | Skin Editor | Edit the playground's own SVG skin live |

### Realism (41-46)
How far SVG can go toward photorealistic imagery.

| # | Demo | What you will see |
|---|---|---|
| 41 | Gradient Painting | Photorealistic art from layered gradients |
| 42 | Path Stacking | Depth and realism from overlapping paths |
| 43 | Filter Photorealism | Camera-like effects using filter primitives |
| 44 | Mesh Gradient | Complex colour meshes via SVG |
| 45 | Hybrid Masterpiece | Every technique combined |
| 46 | SVG vs Photo Challenge | Side-by-side: spot the raster |

---

## How Demos Work

### Iframe Isolation

Each demo runs inside a sandboxed `<iframe>` in the shell. This gives every demo its own document, its own JavaScript scope, and prevents one demo's code from breaking another. It also means each demo is a completely normal web page you can open directly in your browser without the shell at all — just navigate to `demos/01-infinite-scaling/index.html`.

```
Browser
  |
  +-- index.html  (shell)
        |
        +-- <iframe sandbox="allow-scripts allow-same-origin">
                  |
                  +-- demos/01-infinite-scaling/index.html  (standalone page)
```

### postMessage Protocol

The shell and the demo inside the iframe communicate through `window.postMessage`. The protocol is defined in `shared/demo-contract.js` and covers:

```
Shell  -->  Demo    SKIN_CHANGE     Apply a new CSS variable theme
Shell  -->  Demo    CODE_UPDATE     Push live-edited SVG source into the demo
Shell  -->  Demo    REQUEST_SOURCE  Ask the demo for its current SVG markup

Demo   -->  Shell   DEMO_READY      Announce readiness and send initial source
Demo   -->  Shell   SOURCE_RESPONSE Reply to a REQUEST_SOURCE
Demo   -->  Shell   TITLE_UPDATE    Let the shell know the demo's current title
```

All messages carry a `protocol: "svg-playground"` field so unrelated messages from third-party scripts are ignored.

### Standalone Capability

Because demos detect `window.parent === window` (i.e. they are not inside an iframe), every demo degrades gracefully when opened directly. `initDemo()` simply skips sending messages to the shell, and the demo works as a self-contained page.

---

## Creating a New Demo

The fastest way is the scaffold script:

```bash
npm run new-demo -- <folder-id> "Human Title" <category-slug>

# Example
npm run new-demo -- 47-clip-art-builder "Clip Art Builder" composability
```

This copies `demos/_template/` to `demos/47-clip-art-builder/`, updates `manifest.json`, and sets the page title. Then:

1. **Edit `demos/47-clip-art-builder/index.html`** — add your SVG markup and any controls inside `.demo-area` and `.controls`.

2. **Edit `demos/47-clip-art-builder/demo.js`** — write your demo logic. Call `initDemo()` at the top to wire up shell communication automatically.

3. **Edit `demos/47-clip-art-builder/manifest.json`** — fill in `description`, `svgElements`, and `svgAttributes` so the hub card is accurate.

4. **Run `npm run catalog`** — regenerate `demos-catalog.json` so the hub picks up your new demo.

5. **Run `npm run dev`** — your demo appears in the gallery.

### Manifest Fields

```json
{
  "id":           "47-clip-art-builder",
  "title":        "Clip Art Builder",
  "category":     "composability",
  "difficulty":   2,
  "tech":         ["vanilla"],
  "description":  "One-sentence description shown on the hub card.",
  "svgElements":  ["clipPath", "use", "symbol"],
  "svgAttributes": ["clip-path", "href", "viewBox"]
}
```

Valid `category` values (matching the hub filter):
`core`, `shapes-paths`, `paint-style`, `text`, `transforms`, `filters`,
`animation`, `interactivity`, `composability`, `data-driven`,
`accessibility`, `performance`, `meta`, `realism`

Valid `difficulty` values: `1` (beginner), `2` (intermediate), `3` (advanced)

---

## Skin System

The shell's visual theme is driven by SVG skin files in `shell/skins/`. Two skins ship by default:

| File | Name | Style |
|---|---|---|
| `default.svg` | Midnight | Dark navy with cyan accent, subtle grid background |
| `minimal.svg` | Minimal | Light parchment with blue accent, dot-grid background |

Each skin file is an SVG document with a `<style>` block that sets CSS custom properties on `:root`. When the user picks a skin, the shell reads those properties and broadcasts them to the active demo via `postMessage`. The demo applies them with `document.documentElement.style.setProperty()`.

```
Skin SVG file
  |
  +-- <style> block with --bg, --accent, --text, --border etc.
        |
        +-- shell reads variables
              |
              +-- postMessage SKIN_CHANGE --> demo iframe
                    |
                    +-- demo applies CSS custom properties to its :root
```

Because demos already use `var(--accent)`, `var(--bg)`, and so on in `demo-chrome.css`, theme switching is free for any demo that does not override these properties.

To add a new skin, create an SVG file in `shell/skins/` with the required `data-skin` and `data-name` attributes, define the CSS variables, and optionally add decorative SVG shapes as the background.

---

## Key Technologies

| Technology | Role |
|---|---|
| [Vite 5](https://vitejs.dev) | Dev server and bundler — auto-discovers all demo pages as separate entry points |
| [CodeMirror 6](https://codemirror.net) | Live code editor with XML/SVG syntax highlighting and the One Dark theme |
| `@codemirror/lang-xml` | XML/SVG grammar for syntax highlighting and token parsing |
| Vanilla HTML/CSS/JS | Zero framework dependencies in demos — every demo is plain web platform code |
| `window.postMessage` | Shell-to-iframe communication without shared globals |
| CSS Custom Properties | Theme variables passed from skin files through to demo pages |

CodeMirror is loaded lazily when the code panel is first opened. If it fails to load (network error, very old browser), the panel falls back to a plain `<textarea>` so editing still works.

---

## Documentation

The `docs/` folder (to be added) is the place for deeper write-ups:

- `docs/architecture.md` — shell layout, routing, and iframe lifecycle
- `docs/demo-contract.md` — full postMessage protocol reference
- `docs/skin-authoring.md` — guide to creating and publishing new skins
- `docs/contributing.md` — code style, PR process, demo quality bar

For now, the source code is the documentation. The files are short, focused, and commented — `shared/demo-contract.js` and `shell/code-panel.js` are good starting points.

---

## License

MIT — see `LICENSE` for details.

You are free to use, copy, modify, and distribute this project. If you build something interesting with it, consider opening a PR to add your demo to the collection.
