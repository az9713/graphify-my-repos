---
repo: voice-note-taker
description: Capture voice ideas anywhere, structure them with AI, save to GitHub
language: None
stars: 0
forks: 0
created: 2026-01-23
updated: 2026-01-23
topics: 
is_fork: False
kb: 100
---

# voice-note-taker
# Voice Note Taker

> **Capture ideas anywhere with your voice, structure them with AI, and save them to GitHub automatically.**

## What Is This?

This is a personal knowledge management system that lets you:

1. **Speak your ideas** into your phone using Claude's mobile app
2. **AI structures them** automatically (extracts insights, action items)
3. **Automatically pushed** to your GitHub repository
4. **Auto-merged** - PR created, merged to main, branch deleted automatically

```
┌─────────────────────────────────────────────────────────────────────┐
│                     SIMPLE WORKFLOW                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                     │
│   📱 PHONE (You do this)               ☁️ GITHUB (Automatic)        │
│   ──────────────────────               ─────────────────────        │
│   1. Open Claude app                   → Branch created             │
│   2. Select </> Code                   → PR created                 │
│   3. Speak your idea                   → Merged to main             │
│                                        → Branch deleted             │
│   That's it! Everything                                             │
│   else is automatic.                   Your idea is saved!          │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
```

## Quick Links

| I want to... | Go to... |
|--------------|----------|
| Get started in 5 minutes | [Quick Start Guide](docs/QUICK_START.md) |
| Understand how it works | [Architecture Overview](docs/ARCHITECTURE.md) |
| Learn all features | [User Guide](docs/USER_GUIDE.md) |
| Develop/extend this project | [Developer Guide](docs/DEVELOPER_GUIDE.md) |
| Fix a problem | [Troubleshooting](docs/TROUBLESHOOTING.md) |
| Understand a term | [Glossary](docs/GLOSSARY.md) |

## Prerequisites

Before you start, you need:

- [ ] A smartphone (iPhone or Android)
- [ ] A Claude account (Pro, Max, Team, or Enterprise)
- [ ] A GitHub account (free)

## 5-Minute Setup

### Step 1: Fork/Clone This Repository

```bash
git clone https://github.com/az9713/voice-note-taker.git
```

Or fork it to your own GitHub account first.

### Step 2: Install Claude Mobile App

1. Open the App Store (iPhone) or Play Store (Android)
2. Search for "Claude by Anthropic"
3. Tap "Install"
4. Open the app and sign in with your Claude account

### Step 3: Configure Claude Code on Mobile

1. Open the Claude app on your phone
2. Tap **</> Code** (Code mode)
3. Start a **New Session**
4. Set your **Default GitHub repo** to `voice-note-taker`

### Step 4: Test It!

1. Tap the microphone icon
2. Say: "I have an idea about making breakfast faster"
3. Claude will structure your idea, push to GitHub, create PR, merge, and cleanup

**That's it!** Your idea is now in your knowledge base - fully automatic!

## Project Structure

```
voice-note-taker/
├── README.md                 # You are here
├── CLAUDE.md                 # AI instructions (how Claude processes ideas)
├── .claude/
│   └── skills/
│       └── voice-note-taker/
│           └── SKILL.md      # Skill for automatic idea saving
├── knowledge-base/
│   ├── ideas/                # Raw ideas (brainstorms, thoughts)
│   ├── insights/             # Processed insights (learnings)
│   └── actions/              # Action items (tasks, plans)
└── docs/
    ├── QUICK_START.md        # 10 example use cases
    ├── USER_GUIDE.md         # Complete user documentation
    ├── DEVELOPER_GUIDE.md    # For developers
    ├── ARCHITECTURE.md       # How it all works
    ├── TROUBLESHOOTING.md    # Common problems & solutions
    └── GLOSSARY.md           # Terms explained
```

## How It Works (Simple Version)

```
┌──────────────────────────────────────────────────────────────────────────┐
│                           YOUR WORKFLOW                                   │
├──────────────────────────────────────────────────────────────────────────┤
│                                                                          │
│   1. CAPTURE              2. PROCESS              3. STORE & MERGE       │
│   ┌─────────┐            ┌─────────────┐         ┌────────────────┐     │
│   │  Phone  │───────────▶│   Claude    │────────▶│  GitHub Repo   │     │
│   │  Voice  │            │  (AI Brain) │         │  (main branch) │     │
│   └─────────┘            └─────────────┘         └────────────────┘     │
│                                                                          │
│   "I had an idea         "Here's what            All automatic:          │
│    about..."              I understood:          → Create branch         │
│                           - Summary              → Push file             │
│                           - Key points           → Create PR             │
│                           - Actions"             → Merge to main         │
│                                                  → Delete branch         │
│                                                                          │
└──────────────────────────────────────────────────────────────────────────┘
```

## Workflow Details

### On Phone (Everything happens here!)
1. Open Claude app → **</> Code**
2. Speak or type your idea
3. Claude structures it automatically
4. Claude creates branch, pushes, creates PR, merges, and cleans up

### On GitHub (Optional - just to view)
- Visit your repository to see your saved ideas in `knowledge-base/`
- All commits are automatically merged to `main` branch
- No manual action required!

## Support

- **Issues**: [GitHub Issues](https://github.com/az9713/voice-note-taker/issues)
- **Claude Help**: [Claude Documentation](https://docs.anthropic.com)

## Acknowledgement

This work was inspired by the YouTube video ["Never Lose an Idea Again | Claude Code + Telegram"](https://www.youtube.com/watch?v=Oia18Mdte1I). Instead of using Cloudflare, Telegram, GitHub, and Claude Code, this workflow uses only the latter two. All code and documentation were generated by Claude Code powered by Opus 4.5.

## License

MIT License - Use freely, modify freely, share freely.
