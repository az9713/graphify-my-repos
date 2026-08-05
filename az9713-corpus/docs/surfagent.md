---
repo: surfagent
description: Browser automation API for AI agents — structured page recon, form filling, clicking, and navigation via Chrome CDP
language: TypeScript
stars: 0
forks: 0
created: 2026-04-15
updated: 2026-04-15
topics: 
is_fork: False
kb: 402
---

# surfagent
# surfagent

> **This repository is a fork** of [AllAboutAI-YT/surfagent](https://github.com/AllAboutAI-YT/surfagent) enhanced with comprehensive documentation and 8 new features. See [What's new in v1.3.0](#whats-new-in-v130) for details.

**Browser automation API for AI agents.** Give any AI agent the ability to see, navigate, and interact with real web pages through Chrome.

`npm install -g surfagent` — two commands to give your agent a browser.

[![npm version](https://img.shields.io/npm/v/surfagent.svg)](https://www.npmjs.com/package/surfagent)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](https://opensource.org/licenses/MIT)

---

**surfagent** connects to a local Chrome browser via CDP and exposes a simple HTTP API that returns structured page data — every interactive element, form field, link, and CSS selector — so AI agents can navigate websites fast and precisely without screenshots or trial-and-error.

**Works with any AI agent framework:** LangChain, CrewAI, AutoGPT, Claude Code, OpenAI Agents, custom agents — anything that can make HTTP calls.

## Quick Start

```bash
npm install -g surfagent
surfagent start
```

A **new Chrome window** opens with debug mode — your personal Chrome is not affected. The API starts on `http://localhost:3456`.

## Why surfagent?

| Without surfagent | With surfagent |
|---|---|
| Agent takes screenshots, sends to vision model | Agent calls `/recon`, gets structured JSON in 30ms |
| Guesses CSS selectors, fails, retries | Gets exact selectors from recon response |
| Can't read forms, dropdowns, or modals | Gets form schemas with labels, types, required flags |
| Breaks on SPAs, iframes, shadow DOM | Handles all of them out of the box |
| Slow (2-5s per screenshot round-trip) | Fast (20-60ms per API call on existing tabs) |

## How Agents Use It

The workflow is: **recon → act → read**.

```
1. POST /recon   → get the page map (selectors, forms, elements)
2. POST /click   → click something using a selector from step 1
   POST /fill    → fill a form using selectors from step 1
3. POST /read    → check what happened (success? error? new content?)
4. POST /recon   → if the page changed, map it again
```

### Example: search on any website

```bash
# 1. Recon the page — find the search input
curl -X POST localhost:3456/recon -H 'Content-Type: application/json' \
  -d '{"tab":"0"}'
# Response includes: { "selector": "input[name='search']", "text": "Search..." }

# 2. Type and submit
curl -X POST localhost:3456/fill -H 'Content-Type: application/json' \
  -d '{"tab":"0", "fields":[{"selector":"input[name=\"search\"]","value":"AI agents"}], "submit":"enter"}'

# 3. Read the results
curl -X POST localhost:3456/read -H 'Content-Type: application/json' \
  -d '{"tab":"0"}'
```

## All Endpoints

| Endpoint | Method | Description |
|---|---|---|
| `/recon` | POST | Full page map — every element, form, selector, heading, nav link, metadata, captcha detection |
| `/read` | POST | Structured page content — headings, tables, code blocks, notifications, result areas |
| `/fill` | POST | Fill form fields with real CDP keystrokes (works with React, Vue, SPAs) |
| `/click` | POST | Click by selector or text, including dropdown options. Optional `waitAfter` for SPAs |
| `/dismiss` | POST | Auto-dismiss cookie banners, consent dialogs, modals (multi-language) |
| `/scroll` | POST | Scroll page, returns visible content preview and scroll position |
| `/navigate` | POST | Go to URL, back, or forward in the same tab |
| `/eval` | POST | Run JavaScript in any tab or cross-origin iframe |
| `/captcha` | POST | Detect and interact with captchas — Arkose, reCAPTCHA, hCaptcha (experimental) |
| `/type` | POST | Raw CDP key typing without clearing — for Google Sheets, contenteditable, canvas apps |
| `/focus` | POST | Bring a tab to the front in Chrome |
| `/screenshot` | POST | Capture full-page or element-cropped screenshot as PNG or JPEG |
| `/hover` | POST | Move the mouse cursor over an element by selector, text, or coordinates |
| `/wait-for` | POST | Poll until a selector, text, URL, or JS expression condition is met |
| `/extract` | POST | Schema-driven scraping — extract fields or repeat rows from a page |
| `/tabs` | GET | List all open Chrome tabs |
| `/health` | GET | Check if Chrome and API are connected |

Full API reference with request/response schemas: **[API.md](./API.md)**

## What's new in v1.3.0

Eight new features added in this fork:

1. **Submit error surfacing** — `/fill` now captures and returns CDP-level form submission errors in a `submitError` field instead of silently discarding them.

2. **Improved CSS selector strategies** — `/recon` generates more stable selectors: href-based for links, placeholder-based for inputs, stable class name combinations, and ancestor-id + nth-of-type fallbacks. Reduces positional selectors that break on page changes.

3. **Slim recon mode** — `POST /recon` accepts `"mode": "slim"`. Returns only the top 20 scored interactive elements and strips headings, navigation, metadata, and content summary. Cuts payload size by up to 91% for token-constrained agents.

4. **CDP Connection Pool** — New `src/chrome/pool.ts` module with health-checked idle connection pooling, automatic eviction of stale connections, and `acquire`/`release`/`invalidate`/`drain`/`stats` API. Available for future integration into high-concurrency workloads.

5. **Screenshot** — `POST /screenshot` captures full-page or element-cropped screenshots. Supports PNG and JPEG formats, JPEG quality control, and viewport-only or full-page capture modes.

6. **Hover** — `POST /hover` dispatches a CDP mouse-move event over any element, identified by CSS selector, visible text, or explicit x/y viewport coordinates.

7. **Wait-for** — `POST /wait-for` polls the page until a condition is met: element selector present, text visible, URL matches a substring, or arbitrary JavaScript expression evaluates truthy. Configurable timeout and interval.

8. **Extract** — `POST /extract` performs schema-driven scraping. Pass a map of field names to CSS selectors; use `root` + `multiple: true` to extract repeated rows. Automatically returns `.href` for links, `.src` for images, `.value` for inputs, and `textContent` for everything else.

## Key Features

**Page reconnaissance** — one call returns every interactive element with stable CSS selectors, form schemas with field labels and validation, navigation structure, metadata, and content summary.

**Real keyboard input** — fills forms using CDP `Input.dispatchKeyEvent`, not JavaScript value injection. Works with React, Vue, Angular, and any framework-controlled inputs.

**Cross-origin iframe support** — target iframes by domain (`"tab": "stripe.com"`). CDP connects to them as separate targets, bypassing same-origin restrictions.

**SPA navigation** — handles single-page apps (YouTube, Gmail, Google Flights). Enter key submission, client-side routing, dynamic content — all work.

**Captcha detection** — `/recon` automatically detects captcha iframes (Arkose, reCAPTCHA, hCaptcha) and flags them. `/captcha` endpoint provides basic interaction.

**Overlay detection** — modals, cookie banners, and blocking overlays are detected and reported so agents can dismiss them before interacting.

**Same-tab navigation** — links with `target="_blank"` are automatically opened in the same tab instead of spawning new ones.

## Tab Targeting

Every endpoint accepts a `tab` field:

```json
{"tab": "0"}           // by index
{"tab": "github"}      // partial match on URL or title
{"tab": "stripe.com"}  // matches cross-origin iframes too
```

## Commands

```bash
surfagent start     # Start Chrome + API (one command)
surfagent chrome    # Start Chrome debug session only
surfagent api       # Start API only (Chrome must be running)
surfagent health    # Check if everything is running
surfagent help      # Show all options
```

## Tested On

Google Flights, YouTube, GitHub, Supabase, Hacker News, Reddit, CodePen, Polymarket, npm — including autocomplete dropdowns, date pickers, complex forms, SPA navigation, cross-origin iframes, and captchas.

## Platform Support

| Platform | Status |
|---|---|
| macOS | Fully supported |
| Linux | Fully supported |
| Windows | Not yet supported — coming soon |

## Requirements

- macOS or Linux
- Chrome or any Chromium-based browser (Arc, Brave, Edge, Vivaldi, etc.)
- Node.js 18+

### Using a non-Chrome browser

surfagent detects Chrome by default. For other Chromium-based browsers, set `BROWSER_PATH`:

```bash
# Arc
BROWSER_PATH="/Applications/Arc.app/Contents/MacOS/Arc" surfagent start

# Brave
BROWSER_PATH="/Applications/Brave Browser.app/Contents/MacOS/Brave Browser" surfagent start

# Microsoft Edge
BROWSER_PATH="/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge" surfagent start
```

## Contributing

Issues and PRs welcome at [github.com/AllAboutAI-YT/surfagent](https://github.com/AllAboutAI-YT/surfagent).

## License

MIT
