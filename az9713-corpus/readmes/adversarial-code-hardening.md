# Adversarial Code Hardening

**Two AIs fight to harden your code.**

A real-time web application where two [Claude Code](https://docs.anthropic.com/en/docs/claude-code) CLI instances battle in a loop: one **builds** code, one **attacks** it. A human **referee** watches in a browser and intervenes at will.

https://github.com/user-attachments/assets/70e82a4e-a419-4dd0-a8b0-472e7a819cd5

> *Demo: Builder writes an `isDivisibleBy7` function, Attacker breaks it with edge cases, Builder fixes, repeat until convergence.*

---

## How It Works

```
                        YOU (Referee)
                    browser at localhost:5173
                            |
                       WebSocket (JSON)
                            |
  Builder (Claude CLI) <-NDJSON-> Server (Bun/Hono) <-NDJSON-> Attacker (Claude CLI)
```

1. **You** give a prompt (e.g. *"Write a function isDivisibleBy7"*)
2. **Builder** writes the code
3. **Attacker** finds vulnerabilities and writes exploit tests
4. **Builder** fixes everything the Attacker broke
5. Loop continues until Attacker reports **convergence** (no more issues found)
6. You review a **session report** with the full color-coded transcript

The human referee can pause, send messages to either agent, retry rounds, or stop the session at any time.

---

## Highlights

| Feature | Details |
|---------|---------|
| **Real-time streaming** | Watch both agents think and code character-by-character |
| **10-phase state machine** | IDLE → SPAWNING → BUILDER_ACTIVE → COUNTDOWN → ATTACKER_ACTIVE → ... → CONVERGENCE |
| **Convergence detection** | Magic marker `NO_MORE_ISSUES` + 8 heuristic regex patterns |
| **Referee controls** | Pause, resume, send messages, queue for next turn, retry, continue after convergence |
| **Tool activity tracking** | See what each agent is doing: reading files, searching code, running tests |
| **Cost & context monitoring** | Per-agent cost in USD, context window usage with 80% warning |
| **Permission system** | Auto-approve safe tools, escalate risky ones to human |
| **Session reports** | Self-contained HTML with color-coded Builder/Attacker transcript |
| **NDJSON session logs** | Full bidirectional protocol logs for debugging |
| **13 bugs documented** | Every bug found during development, with root cause and fix — see [BUGS_FIXED.md](BUGS_FIXED.md) |

---

## Demo

### Video

A compressed demo of a full session (isDivisibleBy7, 3 rounds to convergence):

> `outputs/divisible_by_7_2x.mp4` (2x speed, ~1.5 min)

### Session Report

An example HTML session report from the same run:

> `outputs/session-report_divisible_by_7.html` — open in any browser

---

## Quick Start

### Prerequisites

- [Bun](https://bun.sh/) v1.2+
- [Claude Code CLI](https://docs.anthropic.com/en/docs/claude-code) v2.1+ (`npm install -g @anthropic-ai/claude-code`)
- Active Claude subscription (Pro, Team, or Enterprise)

### Run

```bash
git clone https://github.com/YOUR_USERNAME/adversarial-code-hardening.git
cd adversarial-code-hardening
bun install
bun run dev
```

Open `http://localhost:5173`, enter a prompt, click **Start Hardening**.

---

## Example Prompts

**Beginner:**
- `Write a function isPrime(n) that returns true if n is prime, false otherwise.`
- `Write a function isValidEmail(email) that validates email addresses.`
- `Write a password strength checker that returns "weak", "medium", or "strong".`

**Intermediate:**
- `Implement a token bucket rate limiter with configurable rate and burst size.`
- `Write a CSV parser that handles quoted fields, escaped characters, and multi-line values.`

**Advanced:**
- `Build a SQL query builder with SELECT, WHERE, JOIN, ORDER BY, LIMIT. Prevent SQL injection.`
- `Implement a markdown-to-HTML converter. Prevent XSS attacks.`

See the [User Guide](docs/USER_GUIDE.md) for 10 detailed use cases with expected round counts and costs.

---

## Architecture

### Three-Tier WebSocket Architecture

```
┌─────────────────┐
│     BROWSER      │  React 19 + Zustand
│  (Referee UI)    │  Real-time streaming, controls
└────────┬─────────┘
         │ WebSocket (JSON)
         │ SpectatorMessage / RefereeMessage
┌────────▼─────────┐
│   SERVER (Hono)   │  Bun.serve with native WebSocket
│   Orchestrator    │  10-phase state machine, timers,
│                   │  permission handling, convergence
└──┬────────────┬──┘
   │            │ WebSocket (NDJSON)
   │            │ Claude Code CLI protocol
┌──▼──────┐ ┌──▼────────┐
│ BUILDER │ │ ATTACKER  │  Headless Claude Code CLI
│  (CLI)  │ │   (CLI)   │  via `claude --sdk-url ws://...`
└─────────┘ └───────────┘
```

**Why two protocols?**
- **Browser ↔ Server**: JSON messages optimized for React state updates (`stream_delta`, `phase_change`, `cost_update`)
- **Server ↔ CLI**: NDJSON (newline-delimited JSON) matching the undocumented Claude Code CLI WebSocket protocol

For the full architecture deep-dive, see [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md).

---

## Tech Stack

| Technology | Purpose |
|-----------|---------|
| [Bun](https://bun.sh/) | Runtime + package manager, native WebSocket |
| [Hono](https://hono.dev/) | Lightweight web framework on Bun.serve |
| [React 19](https://react.dev/) | UI with function components |
| [Zustand](https://zustand.docs.pmnd.rs/) | Minimal state management |
| [Tailwind CSS v4](https://tailwindcss.com/) | Utility-first styling |
| [Vite 6](https://vite.dev/) | Dev server with HMR |
| TypeScript | Strict mode throughout |
| NDJSON | Claude Code CLI WebSocket protocol |

---

## Project Structure

```
├── server/                       # Backend (Bun + Hono)
│   ├── index.ts                  # HTTP + WebSocket routes
│   ├── orchestrator.ts           # State machine, turn management, convergence
│   ├── ws-bridge.ts              # NDJSON parsing, message routing, logging
│   ├── cli-launcher.ts           # Spawns Claude CLI with env cleanup
│   ├── prompts.ts                # Builder & Attacker system prompts
│   ├── report-generator.ts       # HTML session report export
│   └── types.ts                  # All TypeScript types
│
├── src/                          # Frontend (React 19 + Zustand)
│   ├── App.tsx                   # Root component
│   ├── store.ts                  # Zustand store (single source of truth)
│   ├── ws.ts                     # Browser WebSocket client
│   └── components/
│       ├── AgentPanel.tsx        # Split view: streaming text + messages
│       ├── StatusBar.tsx         # Phase, activity, cost, context
│       ├── RefereePanel.tsx      # Human controls
│       ├── StartForm.tsx         # Session creation
│       ├── PermissionDialog.tsx  # Tool approval overlay
│       ├── CodeBlock.tsx         # Syntax-highlighted code
│       ├── CopyCodeButton.tsx    # Copy code to clipboard
│       ├── ContextWarning.tsx    # Context window alert
│       └── ErrorBanner.tsx       # Error display with retry
│
├── docs/                         # Documentation
│   ├── ARCHITECTURE.md           # System design deep-dive
│   ├── NDJSON_PROTOCOL.md        # Claude Code CLI protocol spec
│   ├── USER_GUIDE.md             # Step-by-step user guide
│   └── DEVELOPER_GUIDE.md       # Developer reference
│
├── outputs/                      # Demo outputs
│   ├── divisible_by_7_2x.mp4    # Demo video (2x speed)
│   └── session-report_*.html    # Example session report
│
├── .claude/skills/claude-ws-app/ # Reusable skill for Claude Code
│   ├── SKILL.md                  # Skill overview + checklists
│   ├── protocol-reference.md     # NDJSON protocol types
│   └── known-bugs.md             # 8 generic bugs to avoid
│
├── BUGS_FIXED.md                 # All 13 bugs found during development
├── BRAINSTORM.md                 # Original brainstorm (12 project ideas)
└── CLAUDE.md                     # Project instructions for Claude Code
```

---

## Documentation

| Document | What's in it |
|----------|-------------|
| [User Guide](docs/USER_GUIDE.md) | Step-by-step walkthrough, 10 use cases, tips, glossary |
| [Architecture](docs/ARCHITECTURE.md) | Component design, state machine, message flows, timers, data model |
| [NDJSON Protocol](docs/NDJSON_PROTOCOL.md) | Claude Code CLI WebSocket protocol specification |
| [Bugs Fixed](BUGS_FIXED.md) | All 13 bugs with root causes, fixes, and reusability analysis |
| [CLAUDE.md](CLAUDE.md) | Project conventions for Claude Code AI assistant |

---

## Bugs Fixed & Lessons Learned

During development, 13 bugs were discovered, documented, and fixed. Of these, **8 are generic** and will hit anyone building on the Claude Code CLI WebSocket protocol. See [BUGS_FIXED.md](BUGS_FIXED.md) for the full write-up.

**Protocol landmines** (will crash your app silently):

| # | Bug | Failure Mode |
|---|-----|-------------|
| 1 | User messages require nested `{type:"user", message:{role:"user", content:"..."}}` | CLI crashes with TypeError |
| 2 | `control_request` fields are at `msg.request.subtype`, not `msg.request_type` | Permissions silently drop, CLI hangs |
| 3 | CLI sends text via both `stream_event` AND `assistant` messages | UI shows doubled output |
| 4 | `system/init` can be delayed 15s+ by hooks; gate on WS open instead | Connection timeout on first run |
| 5 | `CLAUDECODE` env var must be stripped from child processes | CLI exits immediately with code 1 |

The remaining 3 generic bugs cover timer resets, tool activity detection, and Vite HMR — see the full document for details.

---

## Bonus: `claude-ws-app` Skill

This project includes a reusable [Claude Code skill](https://docs.anthropic.com/en/docs/claude-code/skills) at `.claude/skills/claude-ws-app/` that encapsulates everything learned about building applications on top of the Claude Code CLI WebSocket protocol.

**What's in the skill:**

- **[SKILL.md](.claude/skills/claude-ws-app/SKILL.md)** — Quick-reference checklists, design patterns, and the 8 generic pitfalls to avoid
- **[protocol-reference.md](.claude/skills/claude-ws-app/protocol-reference.md)** — Full NDJSON message type definitions with exact TypeScript types for every message the CLI sends and receives
- **[known-bugs.md](.claude/skills/claude-ws-app/known-bugs.md)** — The 8 generic bugs that affect any `claude --sdk-url` integration, with code-level fixes

**How to use it:** Copy the `.claude/skills/claude-ws-app/` directory into your own project's `.claude/skills/` folder. When you invoke Claude Code in your project and ask it to build WebSocket + CLI features, it will automatically apply the protocol knowledge and avoid the known pitfalls.

This skill was extracted from the bugs and patterns discovered while building this project, so you don't have to rediscover them yourself.

---

## Acknowledgments

This project was inspired by [**The Vibe Companion**](https://github.com/The-Vibe-Company/companion), which reverse-engineered the undocumented WebSocket protocol hidden inside the Claude Code CLI and built a web UI on top of it.

Adversarial Code Hardening uses the same **NDJSON protocol** (newline-delimited JSON over WebSocket via `claude --sdk-url`) to enable three-way real-time communication among the **human referee**, the **Builder agent**, and the **Attacker agent**. The protocol knowledge, message formats, and several architectural patterns in this project were informed by studying the Companion's implementation — particularly its WebSocket bridge, CLI launcher, and session type definitions.

The [`claude-ws-app` skill](.claude/skills/claude-ws-app/) bundled with this project distills these protocol details and the [13 bugs discovered during development](BUGS_FIXED.md) into a reusable reference for anyone building similar applications on top of the Claude Code CLI.

---

## License

MIT License. See [LICENSE](LICENSE) for details.
