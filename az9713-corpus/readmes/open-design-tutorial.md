> **Learning fork of [nexu-io/open-design](https://github.com/nexu-io/open-design)** — the original code is unchanged. This fork adds architecture infographics, a deep-dive explainer series (`docs/explainer/`), and a contributor playbook to help developers understand how Open Design clones Claude Design. For a video walkthrough comparing Claude Design, Huashu Design, and Open Design, see [**"ANOTHER Open Source Repo Just Cloned Claude Design"**](https://www.youtube.com/watch?v=BGQ9i3fvNds) below.

---

## Architecture at a glance

Three annotated diagrams — read them in order for a full mental model of the system.

### 1 · System map — apps, packages, and boundaries

<img src="codex_doc/infographics/01-system-map.svg" alt="Open Design system map — all apps, packages, and ownership boundaries" width="100%" />

The full monorepo in one picture. Shows the Next.js web app (`apps/web`), the privileged local daemon (`apps/daemon`), the optional Electron desktop shell (`apps/desktop`), and the `packages/` layer that wires them together. Annotates which layer owns the agent adapters, the skill registry, the SQLite project database, the sidecar IPC channel, and the artifact store.

### 2 · Request lifecycle — from prompt to sandboxed preview

<img src="codex_doc/infographics/02-request-lifecycle.svg" alt="Open Design request lifecycle — prompt enters the web UI and exits as a rendered artifact" width="100%" />

Follows a single user message end-to-end: web chat box → daemon SSE stream → prompt stack assembly (six layers) → spawned CLI process → artifact parser → sandboxed `srcdoc` iframe. The six-layer prompt composition and the `<artifact>` tag handoff are annotated inline.

### 3 · Sidecar lifecycle — tools-dev, IPC, and packaged runtime

<img src="codex_doc/infographics/03-sidecar-lifecycle.svg" alt="Open Design sidecar lifecycle — tools-dev, process stamps, IPC, and packaged Electron runtime" width="100%" />

How `pnpm tools-dev` starts and controls the daemon + web + desktop triad. Explains five-field process stamps (`app · mode · namespace · ipc · source`), namespace isolation for concurrent instances, the IPC JSON-RPC socket channel, and the difference between the dev sidecar and the packaged Electron runtime.

---

## Watch: "ANOTHER Open Source Repo Just Cloned Claude Design"

[![ANOTHER Open Source Repo Just Cloned Claude Design — YouTube thumbnail](https://img.youtube.com/vi/BGQ9i3fvNds/maxresdefault.jpg)](https://www.youtube.com/watch?v=BGQ9i3fvNds)

Side-by-side comparison of **Claude Design** (Anthropic, closed-source, Opus 4.7), **Huashu Design** (the design-philosophy library that inspired OD's prompt stack), and **Open Design** (this repo — open-source, BYOK, 11 CLI adapters). Covers what each product does, how they differ, and what "cloning Claude Design" actually means in practice.

---

## Onboarding documentation (added in this fork)

| Path | What it covers |
|------|---------------|
| [`docs/explainer/what-is-open-design.md`](docs/explainer/what-is-open-design.md) | Mental model, three-component architecture, six load-bearing ideas |
| [`docs/explainer/cloning-claude-design.md`](docs/explainer/cloning-claude-design.md) | Loop-by-loop mapping: what Claude Design does, what OD substitutes |
| [`docs/explainer/the-prompt-stack.md`](docs/explainer/the-prompt-stack.md) | Code-grounded walkthrough of all seven prompt layers |
| [`docs/explainer/key-concepts.md`](docs/explainer/key-concepts.md) | Glossary of every term used across the codebase and docs |
| [`codex_doc/01-product-and-repo-map.md`](codex_doc/01-product-and-repo-map.md) | Product definition, monorepo boundaries, code/doc truth |
| [`codex_doc/02-runtime-request-lifecycle.md`](codex_doc/02-runtime-request-lifecycle.md) | Full prompt-to-file execution path |
| [`codex_doc/03-agent-skill-prompt-pipeline.md`](codex_doc/03-agent-skill-prompt-pipeline.md) | Prompt stack, skill registry, agent adapters, media contract |
| [`codex_doc/04-sidecar-dev-packaged-lifecycle.md`](codex_doc/04-sidecar-dev-packaged-lifecycle.md) | `tools-dev`, desktop IPC, namespace stamps, packaged runtime |
| [`codex_doc/05-data-storage-artifacts-preview.md`](codex_doc/05-data-storage-artifacts-preview.md) | SQLite schema, project folders, export/deploy, runtime data |
| [`codex_doc/06-contributor-playbook.md`](codex_doc/06-contributor-playbook.md) | Where and how to make changes |

---

# Open Design

> **The open-source alternative to [Claude Design][cd].** Local-first, web-deployable, BYOK at every layer — **11 coding-agent CLIs** auto-detected on your `PATH` (Claude Code, Codex, Cursor Agent, Gemini CLI, OpenCode, Qwen, GitHub Copilot CLI, Hermes, Kimi, Pi, Kiro) become the design engine, driven by **31 composable Skills** and **72 brand-grade Design Systems**. No CLI? An OpenAI-compatible BYOK proxy is the same loop minus the spawn.

<p align="center">
  <img src="docs/assets/banner.png" alt="Open Design — editorial cover: design with the agent on your laptop" width="100%" />
</p>

<p align="center">
  <a href="https://github.com/nexu-io/open-design/stargazers"><img alt="Stars" src="https://img.shields.io/github/stars/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=ffd700&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/network/members"><img alt="Forks" src="https://img.shields.io/github/forks/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=2ecc71&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/issues"><img alt="Issues" src="https://img.shields.io/github/issues/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=ff6b6b&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/pulls"><img alt="Pull Requests" src="https://img.shields.io/github/issues-pr/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=9b59b6&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/graphs/contributors"><img alt="Contributors" src="https://img.shields.io/github/contributors/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=3498db&logo=github&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/commits/main"><img alt="Commit activity" src="https://img.shields.io/github/commit-activity/m/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=e67e22&logo=git&logoColor=white" /></a>
  <a href="https://github.com/nexu-io/open-design/commits/main"><img alt="Last commit" src="https://img.shields.io/github/last-commit/nexu-io/open-design?style=for-the-badge&labelColor=0d1117&color=8e44ad&logo=git&logoColor=white" /></a>
</p>

<p align="center">
  <a href="https://github.com/nexu-io/open-design/releases/latest"><img alt="Latest release" src="https://img.shields.io/github/v/release/nexu-io/open-design?style=flat-square&color=blueviolet&label=release&include_prereleases" /></a>
  <a href="LICENSE"><img alt="License" src="https://img.shields.io/badge/license-Apache%202.0-blue.svg?style=flat-square" /></a>
  <a href="#supported-coding-agents"><img alt="Agents" src="https://img.shields.io/badge/agents-10%20CLIs%20%2B%20BYOK%20proxy-black?style=flat-square" /></a>
  <a href="#design-systems"><img alt="Design systems" src="https://img.shields.io/badge/design%20systems-72-orange?style=flat-square" /></a>
  <a href="#skills"><img alt="Skills" src="https://img.shields.io/badge/skills-31-teal?style=flat-square" /></a>
  <a href="QUICKSTART.md"><img alt="Quickstart" src="https://img.shields.io/badge/quickstart-3%20commands-green?style=flat-square" /></a>
</p>

<p align="center"><b>English</b> · <a href="README.de.md">Deutsch</a> · <a href="README.zh-CN.md">简体中文</a> · <a href="README.zh-TW.md">繁體中文</a> · <a href="README.ko.md">한국어</a> · <a href="README.ja-JP.md">日本語</a></p>

---

## Why this exists

Anthropic's [Claude Design][cd] (released 2026-04-17, Opus 4.7) showed what happens when an LLM stops writing prose and starts shipping design artifacts. It went viral — and stayed closed-source, paid-only, cloud-only, locked to Anthropic's model and Anthropic's skills. There is no checkout, no self-host, no Vercel deploy, no swap-in-your-own-agent.

**Open Design (OD) is the open-source alternative.** Same loop, same artifact-first mental model, none of the lock-in. We don't ship an agent — the strongest coding agents already live on your laptop. We wire them into a skill-driven design workflow that runs locally with `pnpm tools-dev`, can deploy the web layer to Vercel, and stays BYOK at every layer.

Type `make me a magazine-style pitch deck for our seed round`. The interactive question form pops up before the model improvises a single pixel. The agent picks one of five curated visual directions. A live `TodoWrite` plan streams into the UI. The daemon builds a real on-disk project folder with a seed template, layout library, and self-check checklist. The agent reads them — pre-flight enforced — runs a five-dimensional critique against its own output, and emits a single `<artifact>` that renders in a sandboxed iframe seconds later.

That's not "AI tries to design something". That's an AI that has been trained, by the prompt stack, to behave like a senior designer with a working filesystem, a deterministic palette library, and a checklist culture — exactly the bar Claude Design set, but open and yours.

OD stands on four open-source shoulders:

- [**`alchaincyf/huashu-design`**](https://github.com/alchaincyf/huashu-design) — the design-philosophy compass. Junior-Designer workflow, the 5-step brand-asset protocol, the anti-AI-slop checklist, the 5-dimensional self-critique, and the "5 schools × 20 design philosophies" idea behind our direction picker — all distilled into [`apps/web/src/prompts/discovery.ts`](apps/web/src/prompts/discovery.ts).
- [**`op7418/guizang-ppt-skill`**](https://github.com/op7418/guizang-ppt-skill) — the deck mode. Bundled verbatim under [`skills/guizang-ppt/`](skills/guizang-ppt/) with original LICENSE preserved; magazine-style layouts, WebGL hero, P0/P1/P2 checklists.
- [**`OpenCoworkAI/open-codesign`**](https://github.com/OpenCoworkAI/open-codesign) — the UX north star and our closest peer. The first open-source Claude-Design alternative. We borrow its streaming-artifact loop, its sandboxed-iframe preview pattern (vendored React 18 + Babel), its live agent panel (todos + tool calls + interruptible generation), and its five-format export list (HTML / PDF / PPTX / ZIP / Markdown). We deliberately diverge on form factor — they are a desktop Electron app bundling [`pi-ai`][piai]; we are a web app + local daemon that delegates to your existing CLI.
- [**`multica-ai/multica`**](https://github.com/multica-ai/multica) — the daemon-and-runtime architecture. PATH-scan agent detection, the local daemon as the only privileged process, the agent-as-teammate worldview.

## At a glance

| | What you get |
|---|---|
| **Coding-agent CLIs (11)** | Claude Code · Codex CLI · Cursor Agent · Gemini CLI · OpenCode · Qwen Code · GitHub Copilot CLI · Hermes (ACP) · Kimi CLI (ACP) · Pi (RPC) · Kiro CLI (ACP) — auto-detected on `PATH`, swap with one click |
| **BYOK fallback** | OpenAI-compatible proxy at `/api/proxy/stream` — paste `baseUrl` + `apiKey` + `model` and any vendor (Anthropic-via-OpenAI, DeepSeek, Groq, MiMo, OpenRouter, your self-hosted vLLM, or any other OpenAI-compatible provider) becomes the engine. Internal-IP/SSRF blocked at the daemon edge. |
| **Design systems built-in** | **129** — 2 hand-authored starters + 70 product systems (Linear, Stripe, Vercel, Airbnb, Tesla, Notion, Anthropic, Apple, Cursor, Supabase, Figma, Xiaohongshu, …) from [`awesome-design-md`][acd2], plus 57 design skills from [`awesome-design-skills`][ads] added directly under `design-systems/` |
| **Skills built-in** | **31** — 27 in `prototype` mode (web-prototype, saas-landing, dashboard, mobile-app, gamified-app, social-carousel, magazine-poster, dating-web, sprite-animation, motion-frames, critique, tweaks, wireframe-sketch, pm-spec, eng-runbook, finance-report, hr-onboarding, invoice, kanban-board, team-okrs, …) + 4 in `deck` mode (`guizang-ppt` · `simple-deck` · `replit-deck` · `weekly-update`). Grouped in the picker by `scenario`: design / marketing / operation / engineering / product / finance / hr / sale / personal. |
| **Visual directions** | 5 curated schools (Editorial Monocle · Modern Minimal · Warm Soft · Tech Utility · Brutalist Experimental) — each ships a deterministic OKLch palette + font stack ([`apps/web/src/prompts/directions.ts`](apps/web/src/prompts/directions.ts)) |
| **Device frames** | iPhone 15 Pro · Pixel · iPad Pro · MacBook · Browser Chrome — pixel-accurate, shared across skills under [`assets/frames/`](assets/frames/) |
| **Agent runtime** | Local daemon spawns the CLI in your project folder — agent gets real `Read`, `Write`, `Bash`, `WebFetch` against a real on-disk environment, with Windows `ENAMETOOLONG` fallbacks (stdin / prompt-file) on every adapter |
| **Imports** | Drop a [Claude Design][cd] export ZIP onto the welcome dialog — `POST /api/import/claude-design` parses it into a real project so your agent can keep editing where Anthropic left off |
| **Persistence** | SQLite at `.od/app.sqlite`: projects · conversations · messages · tabs · saved templates. Reopen tomorrow, todo card and open files are exactly where you left them. |
| **Lifecycle** | One entry point: `pnpm tools-dev` (start / stop / run / status / logs / inspect / check) — boots daemon + web (+ desktop) under typed sidecar stamps |
| **Desktop** | Optional Electron shell with sandboxed renderer + sidecar IPC (STATUS / EVAL / SCREENSHOT / CONSOLE / CLICK / SHUTDOWN) — drives `tools-dev inspect desktop screenshot` for E2E |
| **Deployable to** | Local (`pnpm tools-dev`) · Vercel web layer · packaged Electron (placeholder, in-flight) |
| **License** | Apache-2.0 |

[acd2]: https://github.com/VoltAgent/awesome-design-md
[ads]: https://github.com/bergside/awesome-design-skills

## Demo

<table>
<tr>
<td width="50%">
<img src="docs/screenshots/01-entry-view.png" alt="01 · Entry view" /><br/>
<sub><b>Entry view</b> — pick a skill, pick a design system, type the brief. The same surface for prototypes, decks, mobile apps, dashboards, and editorial pages.</sub>
</td>
<td width="50%">
<img src="docs/screenshots/02-question-form.png" alt="02 · Turn-1 discovery form" /><br/>
<sub><b>Turn-1 discovery form</b> — before the model writes a pixel, OD locks the brief: surface, audience, tone, brand context, scale. 30 seconds of radios beats 30 minutes of redirects.</sub>
</td>
</tr>
<tr>
<td width="50%">
<img src="docs/screenshots/03-direction-picker.png" alt="03 · Direction picker" /><br/>
<sub><b>Direction picker</b> — when the user has no brand, the agent emits a second form with 5 curated directions (Monocle / Modern Minimal / Tech Utility / Brutalist / Soft Warm). One radio click → a deterministic palette + font stack, no model freestyle.</sub>
</td>
<td width="50%">
<img src="docs/screenshots/04-todo-progress.png" alt="04 · Live todo progress" /><br/>
<sub><b>Live todo progress</b> — the agent's plan streams as a live card. <code>in_progress</code> → <code>completed</code> updates land in real time. The user can redirect cheaply, mid-flight.</sub>
</td>
</tr>
<tr>
<td width="50%">
<img src="docs/screenshots/05-preview-iframe.png" alt="05 · Sandboxed preview" /><br/>
<sub><b>Sandboxed preview</b> — every <code>&lt;artifact&gt;</code> renders in a clean srcdoc iframe. Editable in place via the file workspace; downloadable as HTML, PDF, ZIP.</sub>
</td>
<td width="50%">
<img src="docs/screenshots/06-design-systems-library.png" alt="06 · 72-system library" /><br/>
<sub><b>72-system library</b> — every product system shows its 4-color signature. Click for the full <code>DESIGN.md</code>, swatch grid, and live showcase.</sub>
</td>
</tr>
<tr>
<td width="50%">
<img src="docs/screenshots/07-magazine-deck.png" alt="07 · Magazine deck" /><br/>
<sub><b>Deck mode (guizang-ppt)</b> — the bundled <a href="https://github.com/op7418/guizang-ppt-skill"><code>guizang-ppt-skill</code></a> drops in unchanged. Magazine layouts, WebGL hero backgrounds, single-file HTML output, PDF export.</sub>
</td>
<td width="50%">
<img src="docs/screenshots/08-mobile-app.png" alt="08 · Mobile prototype" /><br/>
<sub><b>Mobile prototype</b> — pixel-accurate iPhone 15 Pro chrome (Dynamic Island, status bar SVGs, home indicator). Multi-screen prototypes use the shared <code>/frames/</code> assets so the agent never re-draws a phone.</sub>
</td>
</tr>
</table>

## Skills

**31 skills ship in the box.** Each is a folder under [`skills/`](skills/) following the Claude Code [`SKILL.md`][skill] convention with an extended `od:` frontmatter that the daemon parses verbatim — `mode`, `platform`, `scenario`, `preview.type`, `design_system.requires`, `default_for`, `featured`, `fidelity`, `speaker_notes`, `animations`, `example_prompt` ([`apps/daemon/src/skills.ts`](apps/daemon/src/skills.ts)).

Two top-level **modes** carry the catalog: **`prototype`** (27 skills — anything that renders as a single-page artifact, from a magazine landing to a phone screen to a PM spec doc) and **`deck`** (4 skills — horizontal-swipe presentations with deck-framework chrome). The **`scenario`** field is what the picker groups them by: `design` · `marketing` · `operation` · `engineering` · `product` · `finance` · `hr` · `sale` · `personal`.

### Showcase examples

The visually distinctive skills you'll most likely run first. Each ships a real `example.html` you can open straight from the repo to see exactly what the agent will produce — no auth, no setup.

<table>
<tr>
<td width="50%" valign="top">
<a href="skills/dating-web/"><img src="docs/screenshots/skills/dating-web.png" alt="dating-web" /></a><br/>
<sub><b><a href="skills/dating-web/"><code>dating-web</code></a></b> · <i>prototype</i><br/>Consumer dating / matchmaking dashboard — left rail nav, ticker bar, KPIs, 30-day mutual-matches chart, editorial typography.</sub>
</td>
<td width="50%" valign="top">
<a href="skills/digital-eguide/"><img src="docs/screenshots/skills/digital-eguide.png" alt="digital-eguide" /></a><br/>
<sub><b><a href="skills/digital-eguide/"><code>digital-eguide</code></a></b> · <i>template</i><br/>Two-spread digital e-guide — cover (title, author, TOC teaser) + lesson spread with pull-quote and step list. Creator / lifestyle tone.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="skills/email-marketing/"><img src="docs/screenshots/skills/email-marketing.png" alt="email-marketing" /></a><br/>
<sub><b><a href="skills/email-marketing/"><code>email-marketing</code></a></b> · <i>prototype</i><br/>Brand product-launch HTML email — masthead, hero image, headline lockup, CTA, specs grid. Centered single-column, table-fallback safe.</sub>
</td>
<td width="50%" valign="top">
<a href="skills/gamified-app/"><img src="docs/screenshots/skills/gamified-app.png" alt="gamified-app" /></a><br/>
<sub><b><a href="skills/gamified-app/"><code>gamified-app</code></a></b> · <i>prototype</i><br/>Three-frame gamified mobile-app prototype on a dark showcase stage — cover, today's quests with XP ribbons + level bar, quest detail.</sub>
</td>
</tr>
<tr>
<td width="50%" valign="top">
<a href="skills/mobile-onboarding/"><img src="docs/screenshots/skills/mobile-onboarding.png" alt="mobile-onboarding" /></a><br/>
<sub><b><a href="skills/mobile-onboarding/"><code>mobile-onboarding</code></a></b> · <i>prototype</i><br/>Three-frame mobile onboarding flow — splash, value-prop, sign-in. Status bar, swipe dots, primary CTA.</sub>
</td>
<td width="50%" valign="top">
<a href="skills/motion-frames/"><img src="docs/screenshot