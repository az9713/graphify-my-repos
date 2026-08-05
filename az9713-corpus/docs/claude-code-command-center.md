---
repo: claude-code-command-center
description: Personal AI command center — 8 microapps backed by agent-readable JSON, with Claude Code session auto-logging via Haiku 4.5
language: HTML
stars: 0
forks: 0
created: 2026-05-27
updated: 2026-05-27
topics: 
is_fork: False
kb: 174
---

# claude-code-command-center
# AI Command Center

A personal agentic OS built on Claude Code — 8 microapps served locally, backed by agent-readable JSON files that Claude can read and write directly.

Inspired by [Jay E's microapp pattern](https://www.youtube.com/watch?v=...): thin visual UIs over structured files give AI agents a better input/output surface than chat alone.

---

## What it looks like

```
┌─────────────────────────────────────────────────────────────────┐
│  ⬡ AI Command Center          PERSONAL AGENTIC OS    14:32:07  │
├─────────────────────────────────────────────────────────────────┤
│  🎯 Research Radar  │  📚 Artifact Vault  │  🤖 Agent Map      │
│  5 unread signals   │  3 docs     [STUB]  │  6 agents          │
│─────────────────────│─────────────────────│─────────────────────│
│  📋 Backlog+Sprint  │  🔬 Paper Compiler  │  📈 Signal Dash    │
│  7 open tasks       │  2 analyzed         │  4 signals  [STUB] │
│─────────────────────│─────────────────────│─────────────────────│
│  🏥 Health Dash     │  💡 Prompt Library  │                    │
│  29% this week [STUB]│  5 prompts  [STUB] │                    │
├─────────────────────────────────────────────────────────────────┤
│  Agents: 🔬 Researcher  ⚙️ Builder  📈 Quant  🏥 HealthOps    │
└─────────────────────────────────────────────────────────────────┘
```

---

## Core idea

```
  YOU ←→ Browser UI (localhost:8080)
                 ↕
         data/*.json files
                 ↕
  AI  ←→ Claude Code (reads & writes JSON directly)
```

You interact with the visual dashboard. Claude Code reads and writes the same JSON files.
No database, no API layer, no sync issues — just flat files.

The dashboard also **auto-updates** after every Claude Code session via a `SessionEnd` hook
that classifies your work using Claude Haiku 4.5 and updates the relevant agent cards.

---

## Quickstart

### Requirements
- Python 3 (for the local HTTP server) — or Node.js as fallback
- Claude Code CLI

### 1. Clone and serve

```powershell
git clone https://github.com/az9713/claude-code-command-center
cd claude-code-command-center
.\start.ps1          # Windows
# or
bash start.sh        # Mac/Linux
```

Open **http://localhost:8080**

### 2. Configure auto-logging (optional but recommended)

Add your Anthropic API key to `.env`:

```env
ANTHROPIC_API_KEY=sk-ant-api03-...
```

Get a key at [console.anthropic.com/settings/keys](https://console.anthropic.com/settings/keys).

This enables Claude Haiku 4.5 to intelligently classify your Claude Code sessions and
auto-update the dashboard. Without a key, keyword matching is used instead (free, slightly
less accurate). See [docs/HOOKS.md](docs/HOOKS.md) for setup.

### 3. Register the session hook

Copy the hook script to your Claude Code hooks directory:

```powershell
# Windows
Copy-Item hooks/sync-command-center.ps1 "$HOME\.claude\hooks\"
```

Then add this entry to `~/.claude/settings.json` under `hooks.SessionEnd`:

```json
{
  "hooks": [{
    "type": "command",
    "command": "powershell.exe -NoProfile -ExecutionPolicy Bypass -File \"C:\\Users\\YOUR_NAME\\.claude\\hooks\\sync-command-center.ps1\"",
    "async": true
  }]
}
```

---

## The 8 microapps

### Deep (fully functional)

| App | Description |
|-----|-------------|
| 🎯 **Research Radar** | Track AI model releases, benchmarks & research signals. Score 1–10, category filters, mark-reviewed workflow. |
| 🔬 **Paper Compiler** | Convert research papers into buildable projects. 8 tabs: Claims, Math, Architecture, Implementation, Checklist, Project Ideas, Open Questions. Export to Markdown. |
| 🤖 **Agent Map** | Agent status, skills, context load, recent tasks. Two views: Agent Grid + Skill Tree. |
| 📋 **Backlog + Sprint** | Task backlog with epic/priority/assignee filters + kanban sprint view. |

### Stub (UI shell + real JSON schema, ready for enrichment)

| App | Description |
|-----|-------------|
| 📚 **Artifact Vault** | Document browser with tag chips and agent comments. |
| 📈 **Signal Dashboard** | Investment/tech signal tracker with bull/bear/neutral scoring. |
| 🏥 **Health Dashboard** | Exercise plan, fall-risk checklist, appointments, profile stats. |
| 💡 **Prompt Library** | Saved prompts and workflow templates with usage tracking. |

---

## File structure

```
claude-code-command-center/
├── index.html              # Command center hub
├── start.ps1               # Windows server launcher
├── start.sh                # Mac/Linux server launcher
├── .env.example            # API key template (copy to .env)
├── hooks/
│   └── sync-command-center.ps1   # SessionEnd hook for auto-logging
├── apps/
│   ├── radar.html
│   ├── paper-compiler.html
│   ├── agents.html
│   ├── backlog.html
│   ├── vault.html
│   ├── signals.html
│   ├── health.html
│   └── prompts.html
├── data/
│   ├── agents.json         # 6 agent definitions
│   ├── backlog.json        # Task backlog
│   ├── sprint.json         # Current sprint
│   ├── radar.json          # AI signals
│   ├── paper.json          # Paper analysis
│   ├── vault.json          # Document index
│   ├── signals.json        # Investment signals
│   ├── health.json         # Health plan
│   └── prompts.json        # Prompt library
└── docs/
    └── HOOKS.md            # Auto-logging system reference
```

---

## How Claude Code interacts with it

The data files are the interface. Tell Claude Code what to do in plain English:

```
"Add a new radar signal: GPT-5 launched, score 9, category Models"
"Mark the attention curriculum task as done"
"Set the Researcher agent to busy, working on scaling laws analysis"
"What tasks are currently in the sprint?"
```

Claude reads `data/*.json`, makes the change, and writes back. Refresh the browser.

---

## Auto-logging hook

After every Claude Code session, a background script:
1. Reads your session transcript
2. Classifies the work using **Claude Haiku 4.5** (or keyword matching as fallback)
3. Updates `data/agents.json` — `lastActive`, `recentTasks`, `status`
4. Updates `data/backlog.json` — moves matching tasks from `todo` → `in-progress`
5. Logs to `data/sync-log.jsonl` for debugging

**Cost:** ~$0.003–0.008 per session with Haiku (~$0.10–0.30/month). Free with keyword fallback.

See [docs/HOOKS.md](docs/HOOKS.md) for full setup and debugging guide.

---

## The 6 agents

Agents are roles Claude Code adopts — not autonomous processes. The Agent Map shows
which role was most recently active.

| Agent | Role |
|-------|------|
| 🔬 Researcher | Deep research, paper reading, literature synthesis |
| ⚙️ Builder | Code generation, implementation, debugging |
| 📈 Quant | Finance modeling, market signal detection |
| 🏥 HealthOps | Exercise planning, fall-risk, Medicare research |
| 📚 Tutor | Curriculum design, quizzes, concept explanation |
| 🗄️ Archivist | Memory management, document indexing |

---

## Design principles

1. **Agent-native data** — flat, human-readable JSON. Claude modifies it directly, no schema needed.
2. **UI is a view** — browser renders JSON. JSON is the record. localStorage is scratch space only.
3. **No build step** — every app is self-contained HTML/CSS/JS.
4. **Graceful degradation** — apps embed fallback demo data if the server is down.
5. **One file per app** — add a new workflow: one JSON file + one HTML file.

---

## Adapting for yourself

1. Edit `data/*.json` to replace demo data with your real tasks, signals, papers, and agents
2. Tell Claude Code to update any file in plain English
3. Add new microapps by creating `data/newapp.json` + `apps/newapp.html`
4. Customize the 6 agents in `data/agents.json` to match your actual workflows

---

## License

MIT — fork freely.
