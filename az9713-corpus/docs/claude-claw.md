---
repo: claude-claw
description: Personal AI assistant bridging Claude Code to Telegram and WhatsApp with bidirectional voice and 3-layer memory
language: TypeScript
stars: 0
forks: 0
created: 2026-02-25
updated: 2026-02-25
topics: 
is_fork: False
kb: 148
---

# claude-claw
# ClaudeClaw

A personal AI assistant that bridges **Claude Code** (Anthropic's AI coding assistant) to **Telegram** and **WhatsApp** with bidirectional voice and a 3-layer memory system.

Send a message from your phone, and ClaudeClaw routes it through an 8-stage pipeline to the real Claude Code CLI running on your computer — giving you access to all of Claude's tools, skills, MCP servers, and file system access, right from your messaging app.

```
+------------------+          +------------------+          +------------------+
|   Your Phone     |          |   ClaudeClaw     |          |   Claude Code    |
|   (Telegram or   | <------> |   (Node.js on    | <------> |   (CLI on your   |
|    WhatsApp)     |          |    your PC)      |          |    computer)     |
+------------------+          +------------------+          +------------------+
                                      |
                              +-------+-------+
                              |               |
                        +-----+-----+   +-----+-----+
                        | OpenAI    |   | SQLite    |
                        | Voice     |   | Memory    |
                        | STT + TTS |   | FTS5      |
                        +-----------+   +-----------+
```

## Features

- **Dual Platform**: Telegram + WhatsApp simultaneously, same codebase
- **Bidirectional Voice**: Send voice messages, get voice replies (OpenAI Whisper + TTS)
- **Full Claude Code Access**: All tools, MCP servers, CLAUDE.md, skills — via Agent SDK
- **3-Layer Memory**: Session resumption + semantic/episodic memories with FTS5 search + context injection
- **Media Support**: Photos, videos, documents — all passed to Claude for analysis
- **Auth Whitelist**: Only authorized users can interact
- **Graceful Everything**: One platform can fail without killing the other, voice falls back to text, memory search failures are skipped

## Quick Start

### Prerequisites

- **Node.js** v22+ ([nodejs.org](https://nodejs.org))
- **Claude Code CLI** installed and configured (`npm install -g @anthropic-ai/claude-code`)
- **Telegram Bot Token** (from [@BotFather](https://t.me/BotFather))
- **OpenAI API Key** (from [platform.openai.com](https://platform.openai.com))

### Setup

```bash
# 1. Navigate to the project
cd claudeclaw

# 2. Install dependencies
npm install --legacy-peer-deps

# 3. Configure environment
cp .env.example .env
# Edit .env with your actual API keys and settings

# 4. Start the bot
npm start
```

### First Run

1. **Telegram**: Search for your bot in Telegram and send it a message
2. **WhatsApp**: Scan the QR code shown in the terminal with WhatsApp (Settings > Linked Devices > Link a Device)
3. Start chatting!

## Configuration

Copy `.env.example` to `.env` and fill in:

| Variable | Required | Description |
|----------|----------|-------------|
| `TELEGRAM_BOT_TOKEN` | For Telegram | Token from @BotFather |
| `OPENAI_API_KEY` | Yes | OpenAI API key (for voice) |
| `TELEGRAM_ALLOWED_USERS` | No | Comma-separated Telegram user IDs (empty = allow all) |
| `WHATSAPP_ALLOWED_USERS` | No | Comma-separated WhatsApp JIDs (empty = allow all) |
| `VOICE_ENABLED` | No | `true` (default) or `false` |
| `TTS_MODEL` | No | `tts-1` (default) or `tts-1-hd` |
| `TTS_VOICE` | No | `nova` (default), `alloy`, `echo`, `fable`, `onyx`, `shimmer` |
| `SESSION_TIMEOUT_MINUTES` | No | `30` (default) |
| `CLAUDE_WORKING_DIR` | No | Directory for Claude Code to work in |
| `CLAUDE_MODEL` | No | `claude-sonnet-4-6` (default) |

## Chat Commands

| Command | Action |
|---------|--------|
| `/newchat` | Start a fresh conversation (clears Claude's context) |
| `/voice` | Toggle voice replies on/off |
| `/memory` | Show memory statistics |

## How It Works

### The 8-Stage Pipeline

Every message flows through 8 stages:

```
1. YOUR PHONE         -- Send text, voice, photo, video, or document
2. PLATFORM API       -- Telegram Bot API or WhatsApp Web protocol
3. ADAPTER + AUTH     -- grammY/Baileys receives message, checks whitelist
4. MEDIA HANDLER      -- Voice→Whisper STT, media→temp files
5. MEMORY INJECTION   -- FTS5 search (top 3 memories) + recent messages (last 5)
6. CLAUDE CODE BRIDGE -- Agent SDK spawns claude CLI with session resume
7. RESPONSE FORMAT    -- Markdown→HTML, split long messages, optional TTS
8. BACK TO PHONE      -- Platform adapter delivers response
```

### 3-Layer Memory System

| Layer | What | How | Duration |
|-------|------|-----|----------|
| **Session** | Claude Code conversation context | Agent SDK `resume` | Until 30min timeout or `/newchat` |
| **Semantic** | Facts about you ("my name is...", "I prefer...") | SQLite + FTS5, slow decay (0.99/day) | ~229 days without access |
| **Episodic** | Conversation events | SQLite + FTS5, fast decay (0.98/day) | ~55 days without access |

Memories strengthen with use (+0.1 weight per access, capped at 5.0) and naturally fade without use (daily decay). Frequently recalled memories persist indefinitely.

### Voice Pipeline

No ffmpeg required. All formats are OGG/Opus natively:

```
Voice in (Telegram .oga / WhatsApp .ogg)
    --> OpenAI Whisper (STT) --> text
    --> Claude Code processes text
    --> OpenAI TTS (response_format: 'opus') --> OGG/Opus audio
    --> Voice out (native to both platforms)
```

## Project Structure

```
claudeclaw/
├── package.json              # Dependencies and scripts
├── tsconfig.json             # TypeScript configuration
├── .env.example              # Configuration template
├── .gitignore                # Excludes data/, node_modules/, .env
├── CLAUDE.md                 # Project conventions for Claude Code
├── README.md                 # This file
├── docs/
│   ├── ARCHITECTURE.md       # Detailed architecture with diagrams
│   ├── DEVELOPER_GUIDE.md    # Step-by-step guide for new developers
│   ├── USER_GUIDE.md         # Non-technical user guide with 12 use cases
│   └── STUDY_PLAN.md         # Zero-to-hero learning plan (15 modules)
├── data/                     # Runtime data (gitignored)
│   ├── memory.db             # SQLite database (auto-created)
│   ├── auth/                 # WhatsApp auth state
│   └── temp/                 # Temporary media files
└── src/
    ├── index.ts              # Entry point — boots both bots
    ├── config.ts             # .env loader + typed validation
    ├── logger.ts             # pino structured logging
    ├── bridge/
    │   └── claude.ts         # Agent SDK bridge (most critical file)
    ├── voice/
    │   ├── stt.ts            # OpenAI Whisper (speech-to-text)
    │   └── tts.ts            # OpenAI TTS (text-to-speech)
    ├── memory/
    │   ├── database.ts       # SQLite schema + FTS5 virtual tables
    │   ├── store.ts          # CRUD + FTS5 search + salience decay
    │   └── context.ts        # Memory injection (search + recent + dedup)
    ├── session/
    │   └── manager.ts        # Session lifecycle + voice toggle
    ├── pipeline/
    │   ├── handler.ts        # 8-stage pipeline orchestrator
    │   ├── media.ts          # Temp media save/cleanup
    │   └── response.ts       # Markdown→HTML + message splitting
    └── platforms/
        ├── types.ts          # IncomingMessage, OutgoingMessage, PlatformAdapter
        ├── telegram.ts       # grammY adapter (long polling)
        └── whatsapp.ts       # Baileys adapter (WebSocket + QR auth)
```

**17 source files, ~1,685 lines of TypeScript.**

## Technology Stack

| Technology | Role | Why |
|-----------|------|-----|
| **TypeScript** | Language | Type safety without a build step (via tsx) |
| **grammY** | Telegram | Modern, well-typed Telegram bot framework |
| **Baileys** | WhatsApp | First-class WhatsApp Web client |
| **Claude Agent SDK** | AI Bridge | Spawns real Claude Code CLI as subprocess |
| **OpenAI** | Voice | Whisper (STT) + TTS — single SDK for both |
| **better-sqlite3** | Database | Synchronous SQLite with FTS5 built in |
| **pino** | Logging | Structured JSON logging with child loggers |

## Documentation

| Document | Audience | Contents |
|----------|----------|----------|
| [ARCHITECTURE.md](docs/ARCHITECTURE.md) | Developers | System design, ASCII diagrams, component deep dives, data flow |
| [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | New developers | Step-by-step setup, debugging, adding features, glossary |
| [USER_GUIDE.md](docs/USER_GUIDE.md) | End users | 12 use cases, tips, troubleshooting, FAQ |
| [STUDY_PLAN.md](docs/STUDY_PLAN.md) | Learners | 15-module zero-to-hero learning path |
| [CLAUDE.md](CLAUDE.md) | Claude Code | Project conventions and structure reference |

## Development

```bash
# Development mode (auto-restart on file changes)
npm run dev

# Type checking
npx tsc --noEmit

# Debug logging
LOG_LEVEL=debug npm start
```

## Security Notes

- **Whitelist auth**: Only configured user IDs can interact with the bot
- **Local data**: All data (database, auth state, temp files) stored locally on your machine
- **bypassPermissions**: Claude Code runs with full tool access — only authorized users should have access
- **API keys**: Stored in `.env` (gitignored), never committed to version control
- **Temp cleanup**: Media files auto-deleted after 1 hour

## Troubleshooting

| Problem | Solution |
|---------|----------|
| Bot doesn't respond | Check whitelist config, verify API keys, check logs |
| WhatsApp QR not showing | Delete `data/auth/` and restart |
| Claude hangs | Check Claude Code CLI works standalone (`claude -p "hello"`), check 5-min timeout in logs |
| Voice not working | Verify `VOICE_ENABLED=true`, check `/voice` toggle, verify OpenAI key |
| Database errors | Delete `data/memory.db` to reset (loses all memories) |
| npm install fails | Use `--legacy-peer-deps` flag |

## Credits

This project was inspired by the excellent YouTube video ["I Turned Claude Code Into a Better OpenClaw"](https://www.youtube.com/watch?v=9Svv-n11Ysk) by Mark Kashef. Built with Claude Code using the Claude Agent SDK.
