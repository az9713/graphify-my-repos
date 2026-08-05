---
repo: open-coworker
description: Personal fork of andrewyng/openworker (MIT, (c) Andrew Ng) - adds segment-aware shell allowlisting, DPAPI-encrypted secrets, FTS5 memory + workspace search, token metering with context compaction, ntfy push, and OS-native TTS. Not affiliated with upstream.
language: Python
stars: 0
forks: 0
created: 2026-07-28
updated: 2026-07-28
topics: ai-agent, fork, openworker, python
is_fork: False
kb: 1738
---

# open-coworker
# open-coworker

> ### This is a clone of [andrewyng/openworker](https://github.com/andrewyng/openworker)
>
> All original code, design, and credit belong to the upstream project (MIT, © Andrew Ng).
> This repo is an unaffiliated personal fork that adds hardening and features on top of
> the downloaded source. Baseline commit `c64f55d` is the pristine upstream download, so
> everything added here is reviewable with `git diff c64f55d..HEAD`.
>
> For the real project, downloads, and support, go upstream. Do not file issues about this
> fork on the upstream tracker.

## What this fork adds

Twelve items, each with tests. Full suite: **968 passed, 10 failed, 1 skipped** — the same
10 fail on the pristine upstream baseline (Windows/network environment issues), so this
work adds **89 passing tests and zero new failures**.

**Security & permissions**
- **Segment-aware shell allowlisting** — `git log | head` auto-runs when both segments are
  allowlisted, instead of any metacharacter blocking the whole command. Substitution,
  redirection, grouping, and background `&` still always ask.
- **Secrets encrypted at rest** — Windows DPAPI envelope; legacy plaintext still loads;
  `COWORKER_SECRETS_PLAINTEXT=1` opts out.

**Search & memory**
- **Memory full-text search** — SQLite FTS5 plus a `memory_search` tool, with a LIKE fallback.
- **Workspace content search** — incremental FTS5 index over granted roots, skipping binaries
  and oversized files.

**Engine**
- **Token-usage metering** — normalized usage from OpenAI, Anthropic, and Gemini, surfaced on
  `TURN_END`.
- **Context compaction** — history past a configurable threshold is summarized, optionally on a
  cheaper model. The cut point snaps to a user-message boundary so a tool call is never split
  from its results.

**Reach & I/O**
- **Phone push for Inbox items** via ntfy — throttled, generic text only, never raises.
- **Voice out** — OS-native TTS and a `speak_text` tool; text is passed via temp file, never the
  command line.
- **Automation delivery** — a scheduled run's summary can be sent through any connector.

**Personas & tooling**
- **Persona install/uninstall/list** from a local path or URL.
- **CI docs checker** — broken links, unbalanced fences, and zero-byte files fail the build.
- **CLI argument dedupe** — parsers extracted to a shared module, zero behavior change.

## What is not finished

- **Session export/import across machines** — not started; nothing landed.
- **OS-level sandboxing of shell tools** — not started. Safety is approval-gating only.
- **Windows code signing** — blocked; needs a purchased certificate.
- **Cost/token display** — the numbers reach `TURN_END`, but no GUI renders them and there is no
  tokens-to-dollars conversion.
- **Mobile approvals** — push notification works; approving from the phone does not.
- **Persona sharing** — works as a module, but there is no `persona` CLI subcommand and no registry.
- **Cost-aware routing** — only compaction can use a cheaper model; no per-turn escalation.
- **Secrets on macOS/Linux** — Windows DPAPI only; the backend seam is ready for a Keychain
  implementation.
- **Docs are stale** — `docs/concepts/*.md` still describe pre-fork behavior (notably
  `permissions-and-risk.md` on the shell allowlist).
- **`packaging/setup_dev_env.sh` is POSIX-only** — it assumes `.venv/bin/`, so it fails on Windows.

See [HANDOFF.md](HANDOFF.md) for the commit-by-commit inventory and design notes.

---

*Everything below is the upstream README, unchanged.*

---

**[openworker.com](https://openworker.com)** · [Download](#download) · [Issues](https://github.com/andrewyng/openworker/issues)

> **Beta** - OpenWorker is in open beta: fully usable, updates itself, and we're actively polishing rough edges. [Issues](https://github.com/andrewyng/openworker/issues) welcome.

**AI that gets your everyday tasks done.** OpenWorker is an open-source AI coworker that lives on your desktop and delivers **finished work**, not just chat: a polished document, a Slack reply with the numbers, an updated calendar, a triaged inbox.

It runs on your machine and doesn't lock you into any model: bring your own API key for OpenAI, Anthropic, Google, or an open-weight provider, or run fully local with Ollama. Your data leaves your machine only through the model and integrations *you* choose.

[![How OpenWorker works](docs/assets/how-it-works.png)](https://openworker.com)

## Download

[**⬇ macOS (Apple Silicon)**](https://download.openworker.com/mac)
<sub>macOS 12+ · signed & notarized · auto-updates</sub>

[**⬇ Windows 10/11 (x64)**](https://download.openworker.com/windows)
<sub>builds are not yet code-signed, so SmartScreen will warn; signing is in progress</sub>

Open the app, add a model key (or point it at Ollama), and ask for something real.

## How it works

1. Tell OpenWorker the outcome you want - "prepare a customer brief," "untangle my calendar," "draft a report," "check where the release stands across Jira and GitHub."
2. It breaks the task into steps and works across your desktop, files, and connected apps.
3. Before anything consequential - sending a message, changing a calendar, running a command - it checks in and you approve or redirect.
4. You get the finished deliverable, not a to-do list.

Under the hood:

```text
┌────────────────────────────────────────────────┐
│              OpenWorker desktop app            │  native shell + GUI
├────────────────────────────────────────────────┤
│           local agent server (Python)          │  engine · tools · connectors - built on aisuite
├───────────────┬────────────────┬───────────────┤
│  your files   │   your tools   │  your model   │  everything runs with your keys,
│  & terminal   │ 25+ connectors │  any provider │  on your machine
└───────────────┴────────────────┴───────────────┘
```

## What it can do

- **Produce real deliverables** - documents, spreadsheets, reports, and web pages land as files you can open and share.
- **Work from Slack** - mention `@OpenWorker` in a channel; a session opens on your desktop, the work happens with your tools, and the answer comes back as a thread reply.
- **Use your everyday tools** - 25+ integrations including GitHub, Slack, Jira, Notion, Linear, HubSpot, Outlook, monday.com, Gmail, and Google Calendar, plus your **terminal and local files**. Any tool reachable over [MCP](https://modelcontextprotocol.io/) plugs in too, with per-tool control.
- **Run on a schedule** - automations for recurring work: a morning brief, a weekly report, a standing watch over a channel. Runs land in the app with full transcripts.
- **Ask before acting** - writes, sends, and shell commands are approval-gated. Unattended runs park their asks in an inbox instead of acting on their own.

## Bring your own model

Model access is yours: pick a provider, paste your key, switch anytime. Supported out of the box:

**OpenAI · Anthropic · Google Gemini · Inkling (Thinking Machines) · GLM (Z.ai) · DeepSeek · Kimi (Moonshot) · Qwen · MiniMax · Mistral · Grok (xAI)** - plus open-weight models via **Together** and **Fireworks**, and fully local models via **Ollama**.

A curated model list marks what we've verified for tool-calling work. Adding any model string works at your own risk.

## Privacy

OpenWorker is local-first. Everything lives on your machine: the agent loop, your conversations, connector tokens, and model keys - all in the app's local secret store. The only cloud piece is a small service that brokers OAuth handshakes for connectors. You can always use the App without signing-in - use the connectors via manually-created credentials/API-keys.

## Run from source

Prerequisites: Python 3.10+, Node 20+, and (for the desktop shell) the Rust toolchain via [rustup](https://rustup.rs/).

```shell
git clone https://github.com/andrewyng/openworker
cd openworker

# 1. One-time bootstrap - creates the Python venv at .venv
#    (on Windows, run from Git Bash or WSL)
bash packaging/setup_dev_env.sh

# 2. Start the local agent server
.venv/bin/openworker-server --cwd ~/some/project --port 8765
#    (Windows: .venv\Scripts\openworker-server.exe)

# 3. In a second terminal, start the UI
cd surfaces/gui
npm install
npm run dev        # browser UI on the Vite dev port
```

The standalone server creates a per-launch token at
`<state-dir>/sidecar-8765.token`; Vite reads that user-only file when it starts.
For direct API calls, send its value in the `X-OpenWorker-Token` header. The
desktop app uses an in-memory launch token instead and never writes it to disk.

To run the full desktop app instead of the browser UI, replace step 3 with `npm run tauri dev` (from `surfaces/gui/`) - the Tauri shell launches the window and supervises the server itself.

Tests: `.venv/bin/pytest` (server), `npm test` and `npm run e2e` in `surfaces/gui` (GUI unit + hermetic end-to-end). Desktop bundles are built with `packaging/build_dmg.sh` / `packaging/build_windows.ps1`.

## Repository layout

| Directory | What's in it |
|---|---|
| `coworker/` | Python backend - agent engine, model providers, connectors, MCP client, memory, automations |
| `surfaces/gui/` | Desktop app - React UI + Tauri shell that supervises the server |
| `stt/` | Speech-to-text sidecar (Rust) for voice input |
| `packaging/` | Installer builds (macOS DMG, Windows), auto-update manifest, dev bootstrap |
| `docs/` | Design specs and decision logs |
| `tests/` | Backend test suite |

## Built on aisuite

OpenWorker's engine is built on [**aisuite**](https://github.com/andrewyng/aisuite), a lightweight Python library providing a unified chat-completions API across LLM providers and an agents layer with tools, toolkits, and MCP support. If you want to build your own agent harness rather than use ours, start there; this repo is a working reference for what aisuite can carry.

OpenWorker was originally developed inside the aisuite repository before moving to its own home here; thanks to the aisuite contributors whose work it builds on.

## Contributing

Contributions and bug reports are welcome - open an [issue](https://github.com/andrewyng/openworker/issues) or a pull request. The app updates itself, so fixes reach installs quickly.
For any PR, please attach screenshots of what was broken and how it is fixed now. We will shortly add features that you can contribute to.
Please note that we are actively developing based off a internal list and goal, so we may not approve PRs that add features that are already under-development or deviates from our vision.

## License

MIT - see [LICENSE](LICENSE).
