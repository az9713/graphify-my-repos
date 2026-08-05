# Claude Code Workflow Tutorial

[![Live Demo](https://img.shields.io/badge/Live%20Demo-Open%20Tutorial-34D399?style=for-the-badge)](https://az9713.github.io/claude-code-workflow-tutorial/tutorial.html)

> **A study in agentic development:** this entire project — the research, the interactive guide, and the video — was built inside a single Claude Code session using the primitives it teaches.

## What's in this repo

| File | What it is |
|---|---|
| `tutorial.html` | Self-contained interactive guide — open in any browser |
| `video/renders/video_2026-06-02_21-07-46.mp4` | 2-minute 6-second MP4 tutorial video |
| `docs/` | Source transcripts and reference docs |

---

## The Tutorial

**[`tutorial.html`](./tutorial.html)** covers the six Claude Code orchestration primitives — when to use each, how they differ, and where people go wrong:

| Primitive | Shape | Cost | When |
|---|---|---|---|
| 💬 Direct / Goal | Single pass | ● Lowest | Simple, focused, one-shot |
| 📋 Skills | Template + Claude | ● Low | Repeatable standardized processes |
| 🤖 Subagents | Delegate one task | ●● Medium | Side tasks that'd pollute your context |
| ⚡ Dynamic Workflows | N agents in parallel | ●●●● High | Large-scale, cross-checked, resumable |
| 🔁 Loop | Repeat on schedule | ●×N | Monitoring, polling, recurring tasks |
| 👥 Agent Teams | Lead + specialists | ●●● High | Complex projects with persistent roles |

Open `tutorial.html` in Chrome or serve locally:

```bash
cd claude-code-workflow-tutorial
python -m http.server 8765
# → http://localhost:8765/tutorial.html
```

---

## The Video

<video src="https://github.com/user-attachments/assets/87d891cf-b61b-4db4-b6a4-9702f52f54cb" controls width="100%"></video>

**2:06 · 1920×1080 · 30fps · 7.3 MB**

The video was generated programmatically from an HTML composition using [HyperFrames](https://github.com/heygen-com/hyperframes).

---

## How This Was Built

### 1. Research with `@claude-code-guide`

The starting point was invoking the built-in **`claude-code-guide`** subagent — a specialist Claude instance whose entire role is to know the Claude Code documentation.

```
@claude-code-guide teach me how to use Claude Code dynamic workflows
```

**On the `@agent-name` syntax:** In Claude Code, prefixing a prompt with `@name` guarantees that specific agent handles the task rather than leaving it to Claude's discretion. A typeahead picker appears as you type. The difference from the `Agent tool` (which Claude uses automatically) is control: `@` is explicit, the Agent tool is automatic.

> **On the `(agent)` in `@"claude-code-guide (agent)"`:** This was a user clarification, not part of the name. The actual syntax is `@claude-code-guide` — no parenthetical. The `(agent)` suffix in quotes just means "the claude-code-guide thing, which is an agent." The real name has no spaces.

The `claude-code-guide` agent fetched the official Hyperframes and Workflows documentation, then synthesized a nuanced comparison of all six orchestration primitives across technical and non-technical domains.

---

### 2. Interactive HTML — `tutorial.html`

Built as a **self-contained single HTML file** with no build step.

**Tech choices:**

| Choice | Why |
|---|---|
| [Tailwind CSS via CDN](https://cdn.tailwindcss.com) | Zero config, works offline once cached, fine for a local tutorial |
| Vanilla JS | No framework overhead; the interactivity (tabs, accordion, decision tree) is simple enough |
| Inline SVG | Animated topology diagrams without external image files |
| `data-primitive` CSS custom properties | Color-codes each primitive consistently across all sections |

**Key interactive features:**
- **Topology cards** — animated SVG diagrams showing the agent fan-out shape of each primitive
- **Comparison matrix** — click rows to highlight; color-coded by primitive
- **Decision Navigator** — Q&A flowchart: answer 3 questions, get a concrete primitive recommendation
- **Domain examples** — tabbed by Engineering / Research / Personal / Business / Creative / Finance
- **Anti-patterns** — wrong vs right side-by-side for the 6 most common mis-matches

> **Note on Tailwind CDN + SRI:** The Tailwind Play CDN generates CSS dynamically based on which classes appear in the page, making it incompatible with Subresource Integrity hashes (which require static, deterministic content). Acceptable for a local tutorial; use a pinned build for production.

---

### 3. Video — HyperFrames

> *"Write HTML. Render video. Built for agents."*  
> — [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes)

**HyperFrames** is HeyGen's open-source framework that renders HTML compositions into deterministic MP4 videos by seeking each frame in headless Chrome and encoding with FFmpeg. Same input → identical output, every time.

#### How it works

```
index.html  (Hyperframes composition)
    ↓
npx hyperframes render
    ↓
Headless Chrome seeks to each frame (3,780 frames @ 30fps)
    ↓
FFmpeg encodes → MP4
```

#### The composition structure

```html
<!-- Root: declares composition ID, dimensions, total duration -->
<div id="root"
     data-composition-id="main"
     data-start="0"
     data-duration="126"
     data-width="1920"
     data-height="1080">

  <!-- Each scene: clip class + timing data attributes -->
  <div id="s1" class="clip s"
       data-start="0" data-duration="8" data-track-index="1">
    <!-- content -->
  </div>

</div>

<script>
  // Paused GSAP timeline — Hyperframes seeks to each frame position
  const tl = gsap.timeline({ paused: true });
  tl.from('#s1 .h1', { opacity: 0, y: 55, duration: 0.9 }, 0.5);
  window.__timelines['main'] = tl;
</script>
```

**Key rules:**
- Every timed element needs `class="clip"` — the framework manages visibility lifecycle
- Timelines must be `paused: true` and registered on `window.__timelines`
- No `Date.now()`, `Math.random()`, or runtime network fetches — determinism requires it
- GSAP, CSS animations, Lottie, Three.js, Anime.js, and WAAPI are all supported

#### The 13 scenes (126 seconds)

| Scene | Time | Content |
|---|---|---|
| Hero | 0–8s | Title + 6 primitive pills animate in |
| The Gap | 8–15s | "Most people use one. There are six." |
| Direct/Goal | 15–23s | Topology SVG + trigger examples |
| Skills | 23–31s | Template topology + built-in skill list |
| Subagents | 31–39s | Delegation topology + trigger patterns |
| Dynamic Workflows | 39–53s | Fan-out topology + 3 trigger methods + key properties |
| Loop | 53–61s | Circular topology + recurring patterns |
| Agent Teams | 61–69s | Hierarchy topology + Teams vs Workflows |
| Core Insight | 69–80s | Loop≠Workflow≠Skill comparison |
| Decision Framework | 80–94s | 5 rules appear one by one |
| Examples | 94–108s | 6 real scenarios mapped to primitives |
| Anti-patterns | 108–120s | 3 wrong/right pairs |
| Outro | 120–126s | Summary + links |

#### Commands

```bash
cd video
npm install          # install hyperframes
npm run dev          # live preview at localhost
npm run check        # lint + validate + layout check
npm run render       # render to MP4 → renders/video_YYYY-MM-DD_HH-MM-SS.mp4
```

#### Render stats

```
3,780 frames · 4 parallel workers · GPU: hardware (WebGL)
7.3 MB · 3 min 10 sec render time · exit 0
```

---

## Session Architecture

This project was itself an example of the primitives it teaches:

| Task | Primitive used | Why |
|---|---|---|
| Fetch official docs | `@claude-code-guide` subagent | Keep docs research out of main context |
| WebFetch Hyperframes README | Direct fetch tool | Single bounded lookup |
| Write tutorial.html | Direct (in-session) | Creative work, fits in context |
| GIF of tutorial | Browser automation (claude-in-chrome) | Side task, isolated |
| Video composition | Direct (in-session) | Code generation |
| Hyperframes render | Background shell command | Long-running, non-blocking |

No dynamic workflows were needed — the tasks were sequential and bounded. A workflow would have been overkill.

---

## References

- [Claude Code Workflows docs](https://code.claude.com/docs/en/workflows)
- [Claude Code Sub-agents docs](https://code.claude.com/docs/en/sub-agents)
- [HyperFrames GitHub](https://github.com/heygen-com/hyperframes)
- [HyperFrames docs](https://hyperframes.heygen.com)
- [Tailwind CSS CDN](https://cdn.tailwindcss.com)
- Original video by [Mark Kashef](https://www.youtube.com/watch?v=9_ExDZFlaNc) — the inspiration for this tutorial
