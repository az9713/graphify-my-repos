---
repo: git-indexer
description: Index GitHub repos by what they can do, not just keywords
language: Python
stars: 1
forks: 0
created: 2026-01-18
updated: 2026-01-31
topics: 
is_fork: False
kb: 275
---

# git-indexer
# git-indexer

> Discover what software can do, not just what it's called.

git-indexer indexes GitHub repositories by their **capabilities** (what they can do) rather than just keywords. It helps developers discover tools they didn't know existed and find opportunities to combine existing tools into new applications.

---

## What Problem Does This Solve?

**The Problem:** When you search GitHub, you need to know what to search for. But what if you don't know the right words? A developer who's never heard of "dotfiles" can't search for dotfile managers. A developer who doesn't know "TUI" exists can't discover terminal UI frameworks.

**The Solution:** git-indexer analyzes repositories and extracts:
- **What they do** (capabilities like "renders tables", "scrapes websites")
- **What domain they belong to** (technical: CLI tools, web frameworks; vertical: finance, health)
- **What they connect to** (inputs, outputs, integrations)

This enables discovery by browsing capability space, not by knowing magic keywords.

---

## Quick Start (5 Minutes)

### Prerequisites

- **Python 3.10 or higher** - [Download Python](https://www.python.org/downloads/)
- **Git** (optional) - [Download Git](https://git-scm.com/downloads/)

### Step 1: Get the Code

```bash
# Option A: Clone with Git
git clone https://github.com/az9713/git-indexer.git
cd git-indexer

# Option B: Download ZIP and extract
# Then open terminal/command prompt in the extracted folder
```

### Step 2: Initialize the Database

```bash
python src/db/init_db.py
```

You should see:
```
Database initialized:
  - Technical domains: 37
  - Vertical domains: 21
```

### Step 3: Index Your First Repository

```bash
python src/indexer/indexer.py index Textualize/rich --skip-semantic
```

This indexes the "rich" library (a terminal formatting tool) using only rule-based extraction (free, no API key needed).

### Step 4: Search Your Index

```bash
python src/indexer/indexer.py search "terminal"
```

**Congratulations!** You've indexed your first repository.

---

## Documentation

| Document | Description | Who Should Read |
|----------|-------------|-----------------|
| [Quick Start Guide](docs/QUICK_START.md) | 10 hands-on tutorials | Everyone (start here!) |
| [User Guide](docs/USER_GUIDE.md) | Complete usage instructions | Users who want to use the tool |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Setup, architecture, contributing | Developers who want to modify/extend |
| [Architecture](docs/ARCHITECTURE.md) | System design and concepts | Developers who want deep understanding |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common problems and solutions | Anyone stuck on an issue |
| [Glossary](docs/GLOSSARY.md) | Technical terms explained | Anyone confused by terminology |

---

## Project Structure

```
git-indexer/
├── README.md                 # You are here
├── CLAUDE.md                 # Instructions for AI assistants
├── .env.example              # Template for API keys
├── .env                      # Your API keys (create this)
│
├── src/                      # Source code
│   ├── db/                   # Database layer
│   │   ├── schema.sql        # Database structure
│   │   ├── init_db.py        # Database initialization
│   │   └── capability_index.db  # SQLite database (generated)
│   │
│   └── indexer/              # Indexing pipeline
│       ├── github_client.py  # Fetches data from GitHub
│       ├── domain_extractor.py   # Extracts domain tags (free)
│       ├── semantic_extractor.py # Extracts capabilities (uses LLM)
│       └── indexer.py        # Main CLI tool
│
├── data/                     # Data files
│   └── sample_repos.txt      # Example repo list
│
└── docs/                     # Documentation
    ├── plans/                # Design documents
    ├── QUICK_START.md        # Tutorials
    ├── USER_GUIDE.md         # User documentation
    ├── DEVELOPER_GUIDE.md    # Developer documentation
    ├── ARCHITECTURE.md       # System design
    ├── TROUBLESHOOTING.md    # Problem solving
    └── GLOSSARY.md           # Terminology
```

---

## Features

### 1. Multi-Layer Indexing

| Layer | What It Extracts | Method | Cost |
|-------|------------------|--------|------|
| **Domain** | Technical + vertical categories | Rules + dependency analysis | Free |
| **Semantic** | Capability verb phrases | LLM (Claude/GPT) | ~$0.005/repo |
| **Interface** | Inputs, outputs, integrations | Code analysis | Free |

### 2. Cost Controls

Never get a surprise bill:

```bash
# See cost estimate before spending
python src/indexer/indexer.py batch repos.txt --dry-run

# Limit spending
python src/indexer/indexer.py batch repos.txt --budget 1.0   # Max $1
python src/indexer/indexer.py batch repos.txt --max-llm 10   # Max 10 LLM calls
```

### 3. Dual LLM Support

Choose your provider:
- **Anthropic Claude** (claude-sonnet-4-20250514)
- **OpenAI GPT** (gpt-4o-mini)

---

## Use Cases

1. **"I want to build something but don't know what"** - Browse capability intersections
2. **"What tools exist for X?"** - Search by capability
3. **"What can I build by combining A and B?"** - Explore combinations
4. **"What am I missing in my toolbox?"** - Compare with similar developers

---

## Getting Help

1. **Read the docs** - Start with [Quick Start](docs/QUICK_START.md)
2. **Check troubleshooting** - See [Troubleshooting](docs/TROUBLESHOOTING.md)
3. **Ask Claude Code** - This project includes `CLAUDE.md` for AI assistance

---

## License

MIT License - See LICENSE file for details.

---

## Acknowledgments

Inspired by the a16z article ["Software's YouTube Moment is Happening"](https://www.a16z.news/p/softwares-youtube-moment-is-happening).
