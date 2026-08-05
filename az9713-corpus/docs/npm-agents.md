---
repo: npm-agents
description: NPM Agent System - Replace MCPs with direct NPM package execution in Claude Code
language: Python
stars: 0
forks: 0
created: 2026-01-13
updated: 2026-01-13
topics: 
is_fork: False
kb: 128
---

# npm-agents
# NPM Agent System

> **Replace MCPs with direct NPM package execution in Claude Code**

A flexible, powerful system that enables Claude Code to use NPM (Node Package Manager) packages as AI agent tools. Instead of building complex MCP (Model Context Protocol) servers, this system lets Claude directly execute any of 289+ curated, high-quality NPM packages.

---

## What is This Project?

### The Problem
When building AI agents (like Claude Code), you often need tools to:
- Process images (resize, convert formats)
- Parse data files (CSV, JSON, XML, Excel)
- Make HTTP requests to APIs
- Generate PDFs, UUIDs, or formatted dates
- And hundreds of other tasks...

Traditionally, you'd need to build custom "MCP servers" for each capability. This is time-consuming and creates maintenance burden.

### The Solution
This project provides a **curated library of 289+ NPM packages** that Claude can execute directly via bash commands. Think of it as giving Claude access to a massive toolbox of pre-built, battle-tested tools.

---

## Why NPM Agents Over MCP?

### What is MCP?

**MCP (Model Context Protocol)** is Anthropic's official protocol for building tools that AI assistants can use. It requires:
- Writing a custom server for each tool
- Handling communication protocols
- Managing authentication and state
- Deploying and maintaining separate services

### Why NPM Agents May Be Better

| Aspect | MCP Approach | NPM Agent Approach |
|--------|-------------|-------------------|
| **Setup Time** | Hours to days per tool | Minutes (just install packages) |
| **Maintenance** | Must maintain custom servers | NPM community maintains packages |
| **Flexibility** | Fixed to what you build | 289+ packages, easily extensible |
| **Updates** | Manual updates required | Automated weekly refresh |
| **Learning Curve** | Learn MCP protocol | Just describe what you need |
| **Code Required** | Write custom server code | Zero code - just bash commands |
| **Reliability** | Depends on your implementation | Battle-tested by millions of users |

### When to Use Each

**Choose NPM Agents when:**
- You need common capabilities (image processing, data parsing, API calls)
- You want quick setup without writing code
- You prefer leveraging existing, well-tested tools
- You need flexibility to combine multiple tools dynamically
- You want automatic updates from the NPM ecosystem

**Choose MCP when:**
- You need persistent connections (WebSockets, streaming)
- You're building a proprietary tool with custom logic
- You need fine-grained control over tool behavior
- You're integrating with internal systems requiring authentication
- Real-time bidirectional communication is required

### The Best of Both Worlds

NPM Agents and MCPs are **not mutually exclusive**. You can:
- Use NPM Agents for common tasks (80% of use cases)
- Build custom MCPs only for specialized needs (20%)
- Reduce development time by orders of magnitude

---

## Quick Start (5 Minutes)

### Prerequisites
Before starting, you need:
- **Node.js** (version 18 or higher) - [Download here](https://nodejs.org/)
- **Python** (version 3.9 or higher) - [Download here](https://python.org/)
- **Claude Code** - The Anthropic CLI tool

### Installation

```bash
# 1. Clone or download this project
cd npm_agents_income_stream_surfers

# 2. Install Python dependencies
pip install -r requirements.txt

# 3. Install a few NPM packages for testing
npm install dayjs nanoid js-yaml
```

### Your First Use

Ask Claude Code to use an NPM package:

```
You: Generate a unique ID for me
Claude: *uses nanoid* → jST9rs60Api8qlpElaf5e

You: What's the current date and time formatted nicely?
Claude: *uses dayjs* → 2026-01-12 23:15:42

You: Convert this YAML to JSON: "name: test\nvalue: 123"
Claude: *uses js-yaml* → {"name":"test","value":123}
```

---

## Documentation

| Document | Description | Who Should Read |
|----------|-------------|-----------------|
| [Quick Start Guide](docs/QUICK_START.md) | 10 hands-on examples to get started | Everyone |
| [User Guide](docs/USER_GUIDE.md) | Complete guide for using the system | End users |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | How to modify and extend the system | Developers |
| [Architecture](docs/ARCHITECTURE.md) | System design and how it works | Developers |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common problems and solutions | Everyone |
| [Glossary](docs/GLOSSARY.md) | Definitions of technical terms | Beginners |

---

## How It Works (Simple Explanation)

```
┌─────────────────────────────────────────────────────────────┐
│                     You ask Claude:                          │
│            "Resize this image to 300 pixels wide"            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                   Claude reads the SKILL.md                  │
│         (which teaches it how to use NPM packages)           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              Claude looks up packages.json                   │
│          (finds 'sharp' for image processing)                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                 Claude runs bash command:                    │
│   node -e "require('sharp')('image.png').resize(300)..."    │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                    Image is resized!                         │
└─────────────────────────────────────────────────────────────┘
```

---

## Available Package Categories

| Category | Examples | Use Cases |
|----------|----------|-----------|
| **Data Processing** | csv-parse, papaparse, xlsx | Parse CSV, Excel files |
| **Image Processing** | sharp, jimp, svgo | Resize, convert, optimize images |
| **PDF** | jspdf, pdfjs-dist | Create and read PDFs |
| **HTTP/APIs** | axios, got, node-fetch | Make web requests |
| **Date/Time** | dayjs, moment | Format and manipulate dates |
| **Validation** | ajv, zod, joi | Validate data against schemas |
| **File System** | glob, archiver | Find files, create ZIP archives |
| **Templating** | handlebars, ejs, marked | Render templates, convert markdown |
| **Crypto** | crypto-js, bcrypt | Hashing, encryption |
| **Testing** | jest, mocha, chai | Run tests |

**Total: 289 packages across 13 categories**

---

## Project Structure

```
npm_agents_income_stream_surfers/
│
├── .claude/                      # Claude Code configuration
│   └── skills/
│       └── npm-agent/
│           ├── SKILL.md          # Teaches Claude how to use packages
│           └── packages.json     # List of all available packages
│
├── data/                         # Generated data files
│   ├── safe_npm_gold_list.json   # Raw harvested package list
│   └── packages.json             # Enriched manifest with examples
│
├── src/                          # Source code
│   ├── harvester/                # Crawls NPM registry
│   │   ├── config.py             # Configuration settings
│   │   └── harvest_safe_npm.py   # Main harvester script
│   └── generator/                # Creates the manifest
│       ├── prompts.py            # LLM prompts (for future use)
│       └── generate_manifest.py  # Manifest generator
│
├── scripts/                      # Utility scripts
│   └── add-package.py            # Manually add packages
│
├── .github/workflows/            # Automation
│   └── refresh-manifest.yml      # Weekly auto-update
│
├── docs/                         # Documentation
│   ├── QUICK_START.md
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   └── ...
│
├── requirements.txt              # Python dependencies
├── package.json                  # Node.js configuration
├── CLAUDE.md                     # Claude Code memory file
└── README.md                     # This file
```

---

## Keeping Packages Updated

The package list is automatically refreshed weekly via GitHub Actions. To manually update:

```bash
# Re-harvest from NPM registry (takes ~10 minutes)
python src/harvester/harvest_safe_npm.py

# Regenerate the manifest
python src/generator/generate_manifest.py
```

---

## Adding New Packages

```bash
# Add a specific package (validates quality automatically)
python scripts/add-package.py lodash

# Force add (skip validation)
python scripts/add-package.py some-package --force
```

---

## Contributing

We welcome contributions! See [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for:
- How to set up your development environment
- Code style guidelines
- How to add new features
- How to submit pull requests

---

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

## Support

- **Issues**: [GitHub Issues](https://github.com/your-repo/issues)
- **Documentation**: See the `/docs` folder
- **Questions**: Check [TROUBLESHOOTING.md](docs/TROUBLESHOOTING.md) first

---

## Acknowledgements

### Inspiration

This project was inspired by the YouTube video **"FORGET MCPS: You NEED To Try NPM AI Agents (INSANE)"** by **Income Stream Surfers**.

- **Video**: [https://www.youtube.com/watch?v=RB7R8vIuPAQ](https://www.youtube.com/watch?v=RB7R8vIuPAQ)
- **Channel**: [Income Stream Surfers](https://www.youtube.com/@IncomeStreamSurfers)

The video demonstrates the powerful concept of using NPM packages directly as AI agent tools, bypassing the need for complex MCP server implementations.

### Development

**All code and documentation in this project were generated by Claude Code powered by Anthropic's Claude Opus 4.5 model.**

This includes:
- All Python scripts (harvester, generator, utilities)
- All JavaScript/Node.js code examples
- The Claude Code Skill definition
- All documentation (README, guides, troubleshooting, glossary)
- GitHub Actions workflow
- Project structure and architecture

### Technologies

- **Claude Code** - Anthropic's AI-powered CLI tool
- **Claude Opus 4.5** - The AI model powering the code generation
- **NPM Registry API** - For package discovery and metadata
- **Node.js** - Runtime for executing NPM packages
- **Python** - For harvesting and manifest generation scripts
