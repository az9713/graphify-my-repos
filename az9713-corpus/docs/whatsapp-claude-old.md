---
repo: whatsapp-claude-old
description: WhatsApp-Claude: Bridge WhatsApp messaging with Claude Code CLI for autonomous AI agent tasks
language: TypeScript
stars: 0
forks: 0
created: 2026-02-01
updated: 2026-02-03
topics: 
is_fork: False
kb: 367
---

# whatsapp-claude-old
# WhatsApp-Claude (Security-Hardened Edition)

> **The secure way to connect WhatsApp to Claude Code.**

[![Security](https://img.shields.io/badge/Security-Hardened-green.svg)](docs/security.md)
[![Safe Mode](https://img.shields.io/badge/Safe%20Mode-Default-blue.svg)](#security-features)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

---

## Why This Fork?

The original whatsapp-claude runs with `--dangerously-skip-permissions` **always on**, giving Claude unrestricted system access. One prompt injection attack could compromise your entire system.

**This fork fixes that** with enterprise-grade security layers enabled by default.

| Feature | Original | This Fork |
|---------|:--------:|:---------:|
| Dangerous mode | Always ON | **Opt-in (OFF)** |
| Input validation | None | **17 blocked patterns** |
| Sensitive data protection | None | **30+ types detected** |
| PIN authentication | None | **Optional 2FA** |
| Rate limiting | None | **10/min default** |
| Audit logging | None | **Full JSON trail** |
| Environment isolation | Leaks all vars | **Safe vars only** |

---

## Security Features

### Defense in Depth

```
┌─────────────────────────────────────────────────────────────────┐
│                    SECURITY ARCHITECTURE                         │
├─────────────────────────────────────────────────────────────────┤
│                                                                 │
│   /claude PIN task                                              │
│         │                                                       │
│         ▼                                                       │
│   ┌─────────────┐                                              │
│   │ PIN Check   │ ◄── "Wrong PIN? Blocked + logged"            │
│   └──────┬──────┘                                              │
│          ▼                                                      │
│   ┌─────────────┐                                              │
│   │ Rate Limit  │ ◄── "Too many requests? Throttled"           │
│   └──────┬──────┘                                              │
│          ▼                                                      │
│   ┌─────────────┐                                              │
│   │ Input Check │ ◄── "rm -rf? curl|bash? BLOCKED"             │
│   └──────┬──────┘                                              │
│          ▼                                                      │
│   ┌─────────────┐                                              │
│   │ Claude Code │ ◄── Safe mode: asks before danger            │
│   └──────┬──────┘                                              │
│          ▼                                                      │
│   ┌─────────────┐                                              │
│   │ Output Scan │ ◄── "API key detected? Need approval"        │
│   └──────┬──────┘                                              │
│          ▼                                                      │
│   ┌─────────────┐                                              │
│   │ Audit Log   │ ◄── Everything logged to logs/audit.log      │
│   └─────────────┘                                              │
│                                                                 │
└─────────────────────────────────────────────────────────────────┘
```

### What's Protected

| Layer | Protection |
|-------|------------|
| **Input** | Blocks `rm -rf`, `curl\|bash`, `/etc/passwd`, `.ssh/` access, `eval()`, and 12 more dangerous patterns |
| **Output** | Detects SSN, credit cards, API keys (OpenAI/AWS/GitHub/Stripe), private keys, passwords, and 25+ more |
| **Access** | Optional PIN required for every command |
| **Abuse** | Rate limiting prevents runaway commands |
| **Audit** | Every action logged with timestamps |

### Sensitive Data Approval Flow

When Claude's output contains sensitive data, you're asked to approve:

```
⚠️ SENSITIVE DATA DETECTED

The response contains:
  - OpenAI API Key: sk-a****...xyz (critical)
  - Password: mys****ret (critical)

To approve: /approve 1
To redact:  /deny 1

⏰ Expires in 5 minutes
```

---

## Quick Start

### 1. Install

```bash
git clone https://github.com/az9713/whatsapp-claude.git
cd whatsapp-claude
npm install
```

### 2. Configure Security

```bash
cp .env.example .env
```

Edit `.env`:

```bash
# SECURITY (recommended)
ENABLE_DANGEROUS_MODE=false      # Keep OFF for safety
COMMAND_PIN=your-secret-pin      # Require PIN for commands
ENABLE_SENSITIVE_DATA_PROTECTION=true
REQUIRE_APPROVAL_SEVERITY=medium

# Optional
RATE_LIMIT_MAX=10
OPENAI_API_KEY=sk-...            # For TTS features
```

### 3. Run

```bash
npm start
```

You'll see the security status on startup:

```
╔════════════════════════════════════════════════════════════╗
║       WhatsApp-Claude Bot (Security Hardened)              ║
╠════════════════════════════════════════════════════════════╣
║  Dangerous Mode: OFF (safe) ✅                             ║
║  PIN Protection: ON 🔒                                     ║
║  Sensitive Data: Protected ✅                              ║
║  Rate Limit: 10/min                                        ║
╚════════════════════════════════════════════════════════════╝
```

### 4. Connect WhatsApp

1. Scan QR code with WhatsApp → Settings → Linked Devices
2. Send a message to yourself:

```
/claude 1234 hello
       ^^^^
       Your PIN
```

---

## Usage

### With PIN Protection (Recommended)

```
/claude PIN your-command-here
```

### Without PIN

```
/claude your-command-here
```

### Examples

```
/claude 1234 list files in this project
/claude 1234 create a python script that prints hello
/claude 1234 summarize README.md
/claude 1234 research "AI agents" on X
/claude 1234 create a code explainer video
```

### Security Commands

| Command | Description |
|---------|-------------|
| `/approve N` | Approve sending sensitive data |
| `/deny N` | Redact sensitive data and send |

---

## Extended Features

This fork includes all features from the original plus security:

### Capabilities

| Feature | Description |
|---------|-------------|
| **X/Twitter** | Research, post, analyze content |
| **Video Production** | Create videos with Remotion |
| **TTS Voiceover** | Generate narration with OpenAI |
| **Chrome Automation** | Control browser with Claude-in-Chrome |
| **Scheduled Tasks** | Run commands via cron |
| **Email** | Gmail automation |

### Video Compositions

| Composition | Description |
|-------------|-------------|
| `CodeExplainer` | Animated code tutorials |
| `GitHubRecap` | Weekly GitHub activity summary |
| `ThreadToVideo` | Convert Twitter threads to videos |
| `VerticalShort` | 9:16 TikTok/Reels format |
| `KineticTypography` | Animated quotes |
| `Audiogram` | Audio waveform visualization |

---

## Configuration Reference

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `ENABLE_DANGEROUS_MODE` | `false` | Set `true` to skip Claude's safety prompts |
| `COMMAND_PIN` | (none) | Require this PIN with every command |
| `ENABLE_SENSITIVE_DATA_PROTECTION` | `true` | Scan output for PII/secrets |
| `REQUIRE_APPROVAL_SEVERITY` | `medium` | Threshold: `critical`, `high`, `medium`, `low` |
| `RATE_LIMIT_MAX` | `10` | Commands per minute |
| `MAX_TASK_LENGTH` | `10000` | Max characters per command |
| `SENSITIVE_DATA_ALLOWLIST` | (none) | Comma-separated values to ignore |
| `OPENAI_API_KEY` | (none) | For TTS features |

### Blocked Patterns

These patterns are **always blocked** regardless of mode:

- `rm -rf`, `rm --no-preserve-root`
- `mkfs.`, `dd if=`
- `curl | bash`, `wget | bash`
- `> /etc/`, `> /dev/`
- `chmod 777`
- `.ssh/id_`, `.ssh/authorized_keys`
- `/etc/passwd`, `/etc/shadow`
- `eval()`, `exec()`
- `base64 -d |`

---

## Documentation

| Document | Description |
|----------|-------------|
| [Security Guide](docs/security.md) | Complete security documentation |
| [Quick Start](docs/quick-start.md) | 10-minute setup with security |
| [User Guide](docs/user-guide.md) | All features + security section |
| [API Reference](docs/api-reference.md) | Full API including `sensitiveDataFilter.js` |
| [Architecture](docs/architecture.md) | System design |

---

## Project Structure

```
whatsapp-claude/
├── whatsapp-bot.js           # Main bot (security-hardened)
├── sensitiveDataFilter.js    # Sensitive data detection
├── logs/
│   └── audit.log             # Security audit trail
├── .claude/
│   ├── settings.json
│   └── skills/               # X, video, productivity skills
├── remotion-videos/          # Video compositions
├── video-pipeline/           # Python TTS/audio tools
└── docs/                     # Documentation
```

---

## How It Works

```
┌─────────────┐      ┌───────────────────┐      ┌─────────────┐
│  WhatsApp   │ ───▶ │  Security Layer   │ ───▶ │ Claude Code │
│  (Phone)    │ ◀─── │  (This Project)   │ ◀─── │    CLI      │
└─────────────┘      └───────────────────┘      └─────────────┘
                              │
                     ┌────────┴────────┐
                     │   Audit Log     │
                     │ (logs/audit.log)│
                     └─────────────────┘
```

1. You send `/claude PIN task` to yourself on WhatsApp
2. Bot validates PIN, rate limit, and input patterns
3. Claude Code executes (in safe mode by default)
4. Output is scanned for sensitive data
5. If sensitive data found → approval required
6. Result sent to WhatsApp
7. Everything logged to `logs/audit.log`

---

## Acknowledgements

### Inspiration

This project was inspired by the YouTube video **"My Most INSANE AI Agent Ever (OpenClaw Clone)"**.

📺 [Watch the original video](https://www.youtube.com/watch?v=_KN5iAQfz6I)

### Generated with AI

All code and documentation were generated by **Claude Code** powered by **Claude Opus 4.5**.

---

## Security Disclaimer

This security-hardened version significantly reduces risk but is still intended for **experimentation and learning**. For production use:

- Run on dedicated/isolated hardware
- Use a separate WhatsApp account
- Review audit logs regularly
- Keep software updated

See [Security Guide](docs/security.md) for complete security documentation.

---

## License

MIT
