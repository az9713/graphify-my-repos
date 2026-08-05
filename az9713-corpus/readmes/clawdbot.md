> ## 📚 Enhanced Documentation Fork
>
> This is a community fork of [clawdbot/clawdbot](https://github.com/clawdbot/clawdbot) with **comprehensive beginner-friendly documentation**.
>
> ### What We Added
>
> | Documentation | Description |
> |---------------|-------------|
> | **[Complete Setup Walkthrough](./tutorials/15-complete-setup-walkthrough.md)** | Step-by-step guide from zero to working WhatsApp, Telegram, and Slack integration |
> | **[14 Tutorial Documents](./tutorials/README.md)** | For users with no technical experience and developers new to the stack |
> | **[Messaging Channels Reference](./tutorials/12-messaging-channels-reference.md)** | All 16 channels with configuration and features |
> | **[AI Providers Reference](./tutorials/13-ai-providers-reference.md)** | All 15+ AI providers with models and setup |
> | **[CLI Commands Reference](./tutorials/14-cli-commands-reference.md)** | All 25+ CLI commands with options and examples |
>
> ### Highlights
>
> - **Real user experience**: Every gotcha, error, and solution documented
> - **Windows native support**: Detailed daemon/service setup for Windows (not just WSL2)
> - **Messaging app guides**: WhatsApp (QR linking), Telegram (BotFather), Slack (Socket Mode)
> - **Known issues documented**: Discord setup attempts and current limitations
> - **No assumptions**: Written for users who have never used Node.js or messaging bots
>
> **🚀 Start here:** [Complete Setup Walkthrough](./tutorials/15-complete-setup-walkthrough.md)
>
> ---

# 🦞 Clawdbot — Personal AI Assistant

<p align="center">
  <img src="https://raw.githubusercontent.com/clawdbot/clawdbot/main/docs/whatsapp-clawd.jpg" alt="Clawdbot" width="400">
</p>

<p align="center">
  <strong>EXFOLIATE! EXFOLIATE!</strong>
</p>

<p align="center">
  <a href="https://github.com/clawdbot/clawdbot/actions/workflows/ci.yml?branch=main"><img src="https://img.shields.io/github/actions/workflow/status/clawdbot/clawdbot/ci.yml?branch=main&style=for-the-badge" alt="CI status"></a>
  <a href="https://github.com/clawdbot/clawdbot/releases"><img src="https://img.shields.io/github/v/release/clawdbot/clawdbot?include_prereleases&style=for-the-badge" alt="GitHub release"></a>
  <a href="https://deepwiki.com/clawdbot/clawdbot"><img src="https://img.shields.io/badge/DeepWiki-clawdbot-111111?style=for-the-badge" alt="DeepWiki"></a>
  <a href="https://discord.gg/clawd"><img src="https://img.shields.io/discord/1456350064065904867?label=Discord&logo=discord&logoColor=white&color=5865F2&style=for-the-badge" alt="Discord"></a>
  <a href="LICENSE"><img src="https://img.shields.io/badge/License-MIT-blue.svg?style=for-the-badge" alt="MIT License"></a>
</p>

**Clawdbot** is a *personal AI assistant* you run on your own devices.
It answers you on the channels you already use (WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, Microsoft Teams, WebChat), plus extension channels like BlueBubbles, Matrix, Zalo, and Zalo Personal. It can speak and listen on macOS/iOS/Android, and can render a live Canvas you control. The Gateway is just the control plane — the product is the assistant.

If you want a personal, single-user assistant that feels local, fast, and always-on, this is it.

[Website](https://clawdbot.com) · [Docs](https://docs.clawd.bot) · [Getting Started](https://docs.clawd.bot/start/getting-started) · [Updating](https://docs.clawd.bot/install/updating) · [Showcase](https://docs.clawd.bot/start/showcase) · [FAQ](https://docs.clawd.bot/start/faq) · [Wizard](https://docs.clawd.bot/start/wizard) · [Nix](https://github.com/clawdbot/nix-clawdbot) · [Docker](https://docs.clawd.bot/install/docker) · [Discord](https://discord.gg/clawd)

Preferred setup: run the onboarding wizard (`clawdbot onboard`). It walks through gateway, workspace, channels, and skills. The CLI wizard is the recommended path and works on **macOS, Linux, and Windows (via WSL2; strongly recommended)**.
Works with npm, pnpm, or bun.
New install? Start here: [Getting started](https://docs.clawd.bot/start/getting-started)

**Subscriptions (OAuth):**
- **[Anthropic](https://www.anthropic.com/)** (Claude Pro/Max)
- **[OpenAI](https://openai.com/)** (ChatGPT/Codex)

Model note: while any model is supported, I strongly recommend **Anthropic Pro/Max (100/200) + Opus 4.5** for long‑context strength and better prompt‑injection resistance. See [Onboarding](https://docs.clawd.bot/start/onboarding).

## Models (selection + auth)

- Models config + CLI: [Models](https://docs.clawd.bot/concepts/models)
- Auth profile rotation (OAuth vs API keys) + fallbacks: [Model failover](https://docs.clawd.bot/concepts/model-failover)

## Install (recommended)

Runtime: **Node ≥22**.

```bash
npm install -g clawdbot@latest
# or: pnpm add -g clawdbot@latest

clawdbot onboard --install-daemon
```

The wizard installs the Gateway daemon (launchd/systemd user service) so it stays running.

## Quick start (TL;DR)

Runtime: **Node ≥22**.

Full beginner guide (auth, pairing, channels): [Getting started](https://docs.clawd.bot/start/getting-started)

```bash
clawdbot onboard --install-daemon

clawdbot gateway --port 18789 --verbose

# Send a message
clawdbot message send --to +1234567890 --message "Hello from Clawdbot"

# Talk to the assistant (optionally deliver back to any connected channel: WhatsApp/Telegram/Slack/Discord/Google Chat/Signal/iMessage/BlueBubbles/Microsoft Teams/Matrix/Zalo/Zalo Personal/WebChat)
clawdbot agent --message "Ship checklist" --thinking high
```

Upgrading? [Updating guide](https://docs.clawd.bot/install/updating) (and run `clawdbot doctor`).

## Development channels

- **stable**: tagged releases (`vYYYY.M.D` or `vYYYY.M.D-<patch>`), npm dist-tag `latest`.
- **beta**: prerelease tags (`vYYYY.M.D-beta.N`), npm dist-tag `beta` (macOS app may be missing).
- **dev**: moving head of `main`, npm dist-tag `dev` (when published).

Switch channels (git + npm): `clawdbot update --channel stable|beta|dev`.
Details: [Development channels](https://docs.clawd.bot/install/development-channels).

## From source (development)

Prefer `pnpm` for builds from source. Bun is optional for running TypeScript directly.

```bash
git clone https://github.com/clawdbot/clawdbot.git
cd clawdbot

pnpm install
pnpm ui:build # auto-installs UI deps on first run
pnpm build

pnpm clawdbot onboard --install-daemon

# Dev loop (auto-reload on TS changes)
pnpm gateway:watch
```

**Note:** When running from source, use `pnpm clawdbot ...` (e.g., `pnpm clawdbot gateway`). The global `clawdbot` command (shown in Quick Start above) is for users who installed via `npm install -g clawdbot`.

Technical detail: `pnpm clawdbot ...` runs TypeScript directly (via `tsx`). `pnpm build` produces `dist/` for running via Node / the packaged `clawdbot` binary.

## Security defaults (DM access)

Clawdbot connects to real messaging surfaces. Treat inbound DMs as **untrusted input**.

Full security guide: [Security](https://docs.clawd.bot/gateway/security)

Default behavior on Telegram/WhatsApp/Signal/iMessage/Microsoft Teams/Discord/Google Chat/Slack:
- **DM pairing** (`dmPolicy="pairing"` / `channels.discord.dm.policy="pairing"` / `channels.slack.dm.policy="pairing"`): unknown senders receive a short pairing code and the bot does not process their message.
- Approve with: `clawdbot pairing approve <channel> <code>` (then the sender is added to a local allowlist store).
- Public inbound DMs require an explicit opt-in: set `dmPolicy="open"` and include `"*"` in the channel allowlist (`allowFrom` / `channels.discord.dm.allowFrom` / `channels.slack.dm.allowFrom`).

Run `clawdbot doctor` to surface risky/misconfigured DM policies.

## Highlights

- **[Local-first Gateway](https://docs.clawd.bot/gateway)** — single control plane for sessions, channels, tools, and events.
- **[Multi-channel inbox](https://docs.clawd.bot/channels)** — WhatsApp, Telegram, Slack, Discord, Google Chat, Signal, iMessage, BlueBubbles, Microsoft Teams, Matrix, Zalo, Zalo Personal, WebChat, macOS, iOS/Android.
- **[Multi-agent routing](https://docs.clawd.bot/gateway/configuration)** — route inbound channels/accounts/peers to isolated agents (workspaces + per-agent sessions).
- **[Voice Wake](https://docs.clawd.bot/nodes/voicewake) + [Talk Mode](https://docs.clawd.bot/nodes/talk)** — always-on speech for macOS/iOS/Android with ElevenLabs.
- **[Live Canvas](https://docs.clawd.bot/platforms/mac/canvas)** — agent-driven visual workspace with [A2UI](https://docs.clawd.bot/platforms/mac/canvas#canvas-a2ui).
- **[First-class tools](https://docs.clawd.bot/tools)** — browser, canvas, nodes, cron, sessions, and Discord/Slack actions.
- **[Companion apps](https://docs.clawd.bot/platforms/macos)** — macOS menu bar app + iOS/Android [nodes](https://docs.clawd.bot/nodes).
- **[Onboarding](https://docs.clawd.bot/start/wizard) + [skills](https://docs.clawd.bot/tools/skills)** — wizard-driven setup with bundled/managed/workspace skills.

## Star History

[![Star History Chart](https://api.star-history.com/svg?repos=clawdbot/clawdbot&type=date&legend=top-left)](https://www.star-history.com/#clawdbot/clawdbot&type=date&legend=top-left)

## Everything we built so far

### Core platform
- [Gateway WS control plane](https://docs.clawd.bot/gateway) with sessions, presence, config, cron, webhooks, [Control UI](https://docs.clawd.bot/web), and [Canvas host](https://docs.clawd.bot/platforms/mac/canvas#canvas-a2ui).
- [CLI surface](https://docs.clawd.bot/tools/agent-send): gateway, agent, send, [wizard](https://docs.clawd.bot/start/wizard), and [doctor](https://docs.clawd.bot/gateway/doctor).
- [Pi agent runtime](https://docs.clawd.bot/concepts/agent) in RPC mode with tool streaming and block streaming.
- [Session model](https://docs.clawd.bot/concepts/session): `main` for direct chats, group isolation, activation modes, queue modes, reply-back. Group rules: [Groups](https://docs.clawd.bot/concepts/groups).
- [Media pipeline](https://docs.clawd.bot/nodes/images): images/audio/video, transcription hooks, size caps, temp file lifecycle. Audio details: [Audio](https://docs.clawd.bot/nodes/audio).

### Channels
- [Channels](https://docs.clawd.bot/channels): [WhatsApp](https://docs.clawd.bot/channels/whatsapp) (Baileys), [Telegram](https://docs.clawd.bot/channels/telegram) (grammY), [Slack](https://docs.clawd.bot/channels/slack) (Bolt), [Discord](https://docs.clawd.bot/channels/discord) (discord.js), [Google Chat](https://docs.clawd.bot/channels/googlechat) (Chat API), [Signal](https://docs.clawd.bot/channels/signal) (signal-cli), [iMessage](https://docs.clawd.bot/channels/imessage) (imsg), [BlueBubbles](https://docs.clawd.bot/channels/bluebubbles) (extension), [Microsoft Teams](https://docs.clawd.bot/channels/msteams) (extension), [Matrix](https://docs.clawd.bot/channels/matrix) (extension), [Zalo](https://docs.clawd.bot/channels/zalo) (extension), [Zalo Personal](https://docs.clawd.bot/channels/zalouser) (extension), [WebChat](https://docs.clawd.bot/web/webchat).
- [Group routing](https://docs.clawd.bot/concepts/group-messages): mention gating, reply tags, per-channel chunking and routing. Channel rules: [Channels](https://docs.clawd.bot/channels).

### Apps + nodes
- [macOS app](https://docs.clawd.bot/platforms/macos): menu bar control plane, [Voice Wake](https://docs.clawd.bot/nodes/voicewake)/PTT, [Talk Mode](https://docs.clawd.bot/nodes/talk) overlay, [WebChat](https://docs.clawd.bot/web/webchat), debug tools, [remote gateway](https://docs.clawd.bot/gateway/remote) control.
- [iOS node](https://docs.clawd.bot/platforms/ios): [Canvas](https://docs.clawd.bot/platforms/mac/canvas), [Voice Wake](https://docs.clawd.bot/nodes/voicewake), [Talk Mode](https://docs.clawd.bot/nodes/talk), camera, screen recording, Bonjour pairing.
- [Android node](https://docs.clawd.bot/platforms/android): [Canvas](https://docs.clawd.bot/platforms/mac/canvas), [Talk Mode](https://docs.clawd.bot/nodes/talk), camera, screen recording, optional SMS.
- [macOS node mode](https://docs.clawd.bot/nodes): system.run/notify + canvas/camera exposure.

### Tools + automation
- [Browser control](https://docs.clawd.bot/tools/browser): dedicated clawd Chrome/Chromium, snapshots, actions, uploads, profiles.
- [Canvas](https://docs.clawd.bot/platforms/mac/canvas): [A2UI](https://docs.clawd.bot/platforms/mac/canvas#canvas-a2ui) push/reset, eval, snapshot.
- [Nodes](https://docs.clawd.bot/nodes): camera snap/clip, screen record, [location.get](https://docs.clawd.bot/nodes/location-command), notifications.
- [Cron + wakeups](https://docs.clawd.bot/automation/cron-jobs); [webhooks](https://docs.clawd.bot/automation/webhook); [Gmail Pub/Sub](https://docs.clawd.bot/automation/gmail-pubsub).
- [Skills platform](https://docs.clawd.bot/tools/skills): bundled, managed, and workspace skills with install gating + UI.

### Runtime + safety
- [Channel routing](https://docs.clawd.bot/concepts/channel-routing), [retry policy](https://docs.clawd.bot/concepts/retry), and [streaming/chunking](https://docs.clawd.bot/concepts/streaming).
- [Presence](https://docs.clawd.bot/concepts/presence), [typing indicators](https://docs.clawd.bot/concepts/typing-indicators), and [usage tracking](https://docs.clawd.bot/concepts/usage-tracking).
- [Models](https://docs.clawd.bot/concepts/models), [model failover](https://docs.clawd.bot/concepts/model-failover), and [session pruning](https://docs.clawd.bot/concepts/session-pruning).
- [Security](https://docs.clawd.bot/gateway/security) and [troubleshooting](https://docs.clawd.bot/channels/troubleshooting).

### Ops + packaging
- [Control UI](https://docs.clawd.bot/web) + [WebChat](https://docs.clawd.bot/web/webchat) served directly from the Gateway.
- [Tailscale Serve/Funnel](https://docs.clawd.bot/gateway/tailscale) or [SSH tunnels](https://docs.clawd.bot/gateway/remote) with token/password auth.
- [Nix mode](https://docs.clawd.bot/install/nix) for declarative config; [Docker](https://docs.clawd.bot/install/docker)-based installs.
- [Doctor](https://docs.clawd.bot/gateway/doctor) migrations, [logging](https://docs.clawd.bot/logging).

## How it works (short)

```
WhatsApp / Telegram / Slack / Discord / Google Chat / Signal / iMessage / BlueBubbles / Microsoft Teams / Matrix / Zalo / Zalo Personal / WebChat
               │
               ▼
┌───────────────────────────────┐
│            Gateway            │
│       (control plane)         │
│     ws://127.0.0.1:18789      │
└──────────────┬────────────────┘
               │
               ├─ Pi agent (RPC)
               ├─ CLI (clawdbot …)
               ├─ WebChat UI
               ├─ macOS app
               └─ iOS / Android nodes
```

## Key subsystems

- **[Gateway WebSocket network](https://docs.clawd.bot/concepts/architecture)** — single WS control plane for clients, tools, and events (plus ops: [Gateway runbook](https://docs.clawd.bot/gateway)).
- **[Tailscale exposure](https://docs.clawd.bot/gateway/tailscale)** — Serve/Funnel for the Gateway dashboard + WS (remote access: [Remote](https://docs.clawd.bot/gateway/remote)).
- **[Browser control](https://docs.clawd.bot/tools/browser)** — clawd‑managed Chrome/Chromium with CDP control.
- **[Canvas + A2UI](https://docs.clawd.bot/platforms/mac/canvas)** — agent‑driven visual workspace (A2UI host: [Canvas/A2UI](https://docs.clawd.bot/platforms/mac/canvas#canvas-a2ui)).
- **[Voice Wake](https://docs.clawd.bot/nodes/voicewake) + [Talk Mode](https://docs.clawd.bot/nodes/talk)** — always‑on speech and continuous conversation.
- **[Nodes](https://docs.clawd.bot/nodes)** — Canvas, camera snap/clip, screen record, `location.get`, notifications, plus macOS‑only `system.run`/`system.notify`.

## Tailscale access (Gateway dashboard)

Clawdbot can auto-configure Tailscale **Serve** (tailnet-only) or **Funnel** (public) while the Gateway stays bound to loopback. Configure `gateway.tailscale.mode`:

- `off`: no Tailscale automation (default).
- `serve`: tailnet-only HTTPS via `tailscale serve` (uses Tailscale identity headers by default).
- `funnel`: public HTTPS via `tailscale funnel` (requires shared password auth).

Notes:
- `gateway.bind` must stay `loopback` when Serve/Funnel is enabled (Clawdbot enforces this).
- Serve can be forced to require a password by setting `gateway.auth.mode: "password"` or `gateway.auth.allowTailscale: false`.
- Funnel refuses to start unless `gateway.auth.mode: "password"` is set.
- Optional: `gateway.tailscale.resetOnExit` to undo Serve/Funnel on shutdown.

Details: [Tailscale guide](https://docs.clawd.bot/gateway/tailscale) · [Web surfaces](https://docs.clawd.bot/web)

## Remote Gateway (Linux is great)

It’s perfectly fine to run the Gateway on a small Linux instance. Clients (macOS app, CLI, WebChat) can connect over **Tailscale Serve/Funnel** or **SSH tunnels**, and you can still pair device nodes (macOS/iOS/Android) to execute device‑local actions when needed.

- **Gateway host** runs the exec tool and channel connections by default.
- **Device nodes** run device‑local actions (`system.run`, camera, screen recording, notifications) via `node.invoke`.
In short: exec runs where the Gateway lives; device actions run where the device lives.

Details: [Remote access](https://docs.clawd.bot/gateway/remote) · [Nodes](https://docs.clawd.bot/nodes) · [Security](https://docs.clawd.bot/gateway/security)

## macOS permissions via the Gateway protocol

The macOS app can run in **node mode** and advertises its capabilities + permission map over the Gateway WebSocket (`node.list` / `node.describe`). Clients can then execute local actions via `node.invoke`:

- `system.run` runs a local command and returns stdout/stderr/exit code; set `needsScreenRecording: true` to require screen-recording permission (otherwise you’ll get `PERMISSION_MISSING`).
- `system.notify` posts a user notification and fails if notifications are denied.
- `canvas.*`, `camera.*`, `screen.record`, and `location.get` are also routed via `node.invoke` and follow TCC permission status.

Elevated bash (host permissions) is separate from macOS TCC:

- Use `/elevated on|off` to toggle per‑session elevated access when enabled + allowlisted.
- Gateway persists the per‑session toggle via `sessions.patch` (WS method) alongside `thinkingLevel`, `verboseLevel`, `model`, `sendPolicy`, and `groupActivation`.

Details: [Nodes](https://docs.clawd.bot/nodes) · [macOS app](https://docs.clawd.bot/platforms/macos) · [Gateway protocol](https://docs.clawd.bot/concepts/architecture)

## Agent to Agent (sessions_* tools)

- Use these to coordinate work across sessions without jumping between chat surfaces.
- `sessions_list` — discover active sessions (agents) and their metadata.
- `sessions_history` — fetch transcript logs for a session.
- `sessions_send` — message another session; optional reply‑back ping‑pong + announce step (`REPLY_SKIP`, `ANNOUNCE_SKIP`).

Details: [Session tools](https://docs.clawd.bot/concepts/session-tool)

## Skills registry (ClawdHub)

ClawdHub is a minimal skill registry. With ClawdHub enabled, the agent can search for skills automatically and pull in new ones as needed.

[ClawdHub](https://ClawdHub.com)

## Chat commands

Send these in WhatsApp/Telegram/Slack/Google Chat/Microsoft Teams/WebChat (group commands are owner-only):

- `/status` — compact session status (model + tokens, cost when available)
- `/new` or `/reset` — reset the session
- `/compact` — compact session context (summary)
- `/think <level>` — off|minimal|low|medium|high|xhigh (GPT-5.2 + Codex models only)
- `/verbose on|off`
- `/usage off|tokens|full` — per-response usage footer
- `/restart` — restart the gateway (owner-only in groups)
- `/activation mention|always` �