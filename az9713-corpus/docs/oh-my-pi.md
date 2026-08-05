---
repo: oh-my-pi
description: Fork of can1357/oh-my-pi with agent harness enhancements (telemetry, MCP resilience, test infrastructure, compaction metrics)
language: TypeScript
stars: 0
forks: 1
created: 2026-02-15
updated: 2026-02-15
topics: 
is_fork: False
kb: 25666
---

# oh-my-pi
<p align="center">
  <img src="https://github.com/can1357/oh-my-pi/blob/main/assets/hero.png?raw=true" alt="Oh My Pi">
</p>

<p align="center">
  <strong>AI coding agent for the terminal</strong>
</p>

<p align="center">
  <a href="https://www.typescriptlang.org"><img src="https://img.shields.io/badge/TypeScript-3178C6?style=flat&colorA=222222&logo=typescript&logoColor=white" alt="TypeScript"></a>
  <a href="https://www.rust-lang.org"><img src="https://img.shields.io/badge/Rust-DEA584?style=flat&colorA=222222&logo=rust&logoColor=white" alt="Rust"></a>
  <a href="https://bun.sh"><img src="https://img.shields.io/badge/runtime-Bun-f472b6?style=flat&colorA=222222" alt="Bun"></a>
  <a href="https://github.com/can1357/oh-my-pi/blob/main/LICENSE"><img src="https://img.shields.io/github/license/can1357/oh-my-pi?style=flat&colorA=222222&colorB=58A6FF" alt="License"></a>
</p>

> **This is a fork of [can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)** (itself a fork of [badlogic/pi-mono](https://github.com/badlogic/pi-mono) by [@mariozechner](https://github.com/mariozechner)).
>
> This fork focuses on **agent harness enhancements** -- strengthening the infrastructure around the LLM that covers the agent loop, tool execution, context management, MCP connectivity, and subagent orchestration.

---

## What This Fork Adds

This fork adds 8 targeted enhancements to the agent harness with full test coverage and documentation. These changes do not modify the user-facing CLI or TUI -- they strengthen the internal infrastructure that makes the agent reliable and observable.

### 1. Mock Stream Utilities & Extended Agent Loop Tests
Reusable test infrastructure for simulating multi-turn LLM conversations. Enables testing of exclusive tool concurrency, steering interrupts, follow-up message queuing, and error handling without real API calls.

### 2. Subagent Executor Utility Tests
55 unit tests for the pure utility functions that normalize model patterns, extract tool argument previews, handle usage token variants across providers, deduplicate report findings, and manage abort timeouts.

### 3. Agent Loop Telemetry (TurnMetrics)
A per-turn metrics callback (`onTurnMetrics`) that surfaces LLM latency, tool execution timing, per-tool breakdowns, context message counts, and token usage. Enables dashboards and performance monitoring.

### 4. TTSR (Time-Traveling Streamed Rules) Unit Tests
22 tests covering the pattern-matching rule injection system. Validates regex compilation, once vs repeat-after-gap triggering, buffer management, and state persistence across sessions.

### 5. MCP Connection Resilience
Timeout protection and abort signal support for MCP server connections. The manager starts servers in parallel with tracked promises, isolates failures, and returns partial results so the agent can work with available servers even if some fail.

### 6. Swarm Extension Tests
Tests for the DAG dependency graph algorithms (cycle detection, execution wave computation) and YAML schema validation used by the swarm orchestration system.

### 7. Compaction Quality Metrics
Token estimation, file operation tracking, and compaction trigger logic for long-running sessions. Chains file access metadata across compaction cycles so context-critical files are preserved.

### 8. Extended Streaming Edit Abort Tests
Integration tests for abort handling during streaming tool calls. Validates that partial diff state is captured for error reporting when users cancel mid-stream.

For full details on each enhancement, see [docs/ENHANCEMENTS.md](docs/ENHANCEMENTS.md).

---

## Learning the Agent Harness

The [`docs_by_omp/`](docs_by_omp/) directory contains introspective documentation written by omp itself while exploring this codebase. These docs demystify the agent harness internals -- how the agent loop works, how subagents are orchestrated in parallel, and how the pieces fit together.

| Document | What it covers |
|---|---|
| [Agent Harness Tutorial](docs_by_omp/AGENT_HARNESS_TUTORIAL.md) | Comprehensive walkthrough of the agent harness architecture -- core components, agent loop, session management, event system, tool execution, and extensibility |
| [Subagent Orchestration Code Path](docs_by_omp/SUBAGENT_ORCHESTRATION_CODE_PATH.md) | Traces the exact code path when spawning 3 parallel research subagents -- from task tool dispatch through the executor to result aggregation |
| [Code Path Analysis](docs_by_omp/CODE_PATH_ANALYSIS.md) | Maps a real read-only analysis task to the agent harness components, showing how each layer (discovery, tool execution, report generation) contributed |
| [Enhancement Proposals](docs_by_omp/OH_MY_PI_ENHANCEMENT_PROPOSALS.md) | 12 concrete enhancements identified by 3 parallel research agents across performance, extensibility, and developer experience |
| [TypeScript Migration Analysis](docs_by_omp/TYPESCRIPT_MIGRATION_ANALYSIS.md) | Feasibility analysis for strict TypeScript migration, produced as a worked example of multi-file codebase analysis |

These are particularly useful if you want to understand how parallel subagent orchestration works in practice, or if you're planning to extend the agent harness yourself.

---

## Relationship to Upstream

| | Upstream ([can1357/oh-my-pi](https://github.com/can1357/oh-my-pi)) | This Fork |
|---|---|---|
| **Focus** | Full-featured AI coding agent | Agent harness reliability & observability |
| **Changes** | CLI, TUI, tools, providers, extensions | Agent loop, test infrastructure, metrics, resilience |
| **User-facing** | Yes (new features, UI changes) | No (internal infrastructure only) |
| **Test coverage** | Baseline | +8 enhancement test suites |
| **Documentation** | User guides, developer guides | Added ENHANCEMENTS.md with why/how/what |

This fork is intended to stay compatible with upstream. The enhancements are additive and do not break existing functionality.

---

## Table of Contents

- [Learning the Agent Harness](#learning-the-agent-harness)
- [Project Overview](#project-overview)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Quick Start](#quick-start)
- [CLI Commands](#cli-commands)
- [Slash Commands (Interactive TUI)](#slash-commands-interactive-tui)
- [Keyboard Shortcuts](#keyboard-shortcuts)
- [Configuration](#configuration)
- [Feature Deep Dive](#feature-deep-dive)
- [Packages](#packages)
- [License](#license)

---

## Project Overview

**oh-my-pi** is an AI-powered coding assistant that runs directly in your terminal. Think of it as having an expert programmer sitting next to you, ready to help with any coding task, right from your command line.

### What is an AI coding assistant?

If you're coming from C/C++/Java and are new to the world of AI-powered development tools, here's what you need to know:

An AI coding assistant is a program that uses large language models (LLMs) — the same technology behind ChatGPT — to help you write code, debug problems, refactor projects, and understand codebases. Instead of searching Stack Overflow or reading documentation for hours, you can ask the AI directly, and it can:

- **Read your code files** and understand what they do
- **Write new code** based on your requirements
- **Edit existing files** to fix bugs or add features
- **Run terminal commands** to test, build, or deploy your project
- **Search your codebase** to find patterns or problematic code
- **Explain complex code** in plain English
- **Generate git commits** with meaningful messages

### Why oh-my-pi?

oh-my-pi is designed for developers who live in the terminal. Instead of copying code back and forth between a web browser and your editor, the AI works directly in your development environment. It can:

- Access your files without you manually copying them
- Run commands and see the output immediately
- Make edits to multiple files in one go
- Remember the context of your entire conversation
- Work with any programming language or framework

This project is built with **Bun** (a modern JavaScript runtime, like Node.js but faster) and uses **Rust** (a systems programming language known for speed and safety) for performance-critical operations. Don't worry if you're not familiar with these technologies — as a user, you don't need to understand them to use oh-my-pi effectively.

### What makes oh-my-pi special?

- **Multi-provider support**: Works with Claude (Anthropic), GPT (OpenAI), Gemini (Google), and many others
- **Built-in tools**: File operations, terminal commands, code search, web browsing, Python execution, and more
- **Native performance**: Critical operations are implemented in Rust for speed
- **Extensible**: Plugin system, custom slash commands, hooks, and extensions
- **Session management**: Resume conversations, branch off into new contexts, view conversation history
- **Beautiful TUI**: Modern terminal interface with syntax highlighting, themes, and smart rendering

---

## Key Features

### AI-Powered Coding Assistant in Your Terminal

Talk to the AI directly from your command line. Ask questions, request code changes, debug issues — all without leaving your terminal.

### Multi-Provider LLM Support

Choose from multiple AI providers based on your needs and budget:

- **Anthropic Claude**: Industry-leading reasoning and code generation (Claude Opus, Sonnet, Haiku)
- **OpenAI GPT**: Including GPT-4o, o1, o3-mini
- **Google Gemini**: Cost-effective with large context windows (Gemini 2.0, Flash, Pro)
- **AWS Bedrock**: Enterprise-grade AI with various models
- **Mistral**: European AI provider with strong multilingual support
- **Groq**: Ultra-fast inference for supported models
- **Ollama**: Run AI models locally on your own hardware (no API key required)
- **Cursor**: Use your Cursor Pro subscription
- **GitHub Copilot**: Leverage your existing Copilot license

### Comprehensive Built-In Tools

The AI can use these tools automatically as it works:

- **File operations**: Read, write, edit files with fuzzy matching for reliable edits
- **Bash commands**: Execute any terminal command and see the results
- **Grep/Find**: Search your codebase using powerful regex patterns (powered by ripgrep)
- **Web search**: Look up documentation, packages, security vulnerabilities
- **Web fetch**: Scrape content from 80+ sites (GitHub, npm, Stack Overflow, arXiv, etc.)
- **Python REPL**: Execute Python code with a persistent IPython kernel
- **LSP integration**: Get IDE-like features (diagnostics, formatting, symbol lookup) for 40+ languages
- **Browser automation**: Control a headless browser for web scraping and testing
- **SSH**: Execute commands on remote servers
- **AST analysis**: Understand code structure at a deep level
- **Replace**: Find and replace across multiple files
- **Git operations**: View diffs, inspect commits, analyze changes

### AI-Powered Git Commits

Run `omp commit` to automatically generate meaningful commit messages:

- Analyzes your changes intelligently (file-by-file, hunk-by-hunk)
- Splits unrelated changes into separate atomic commits
- Follows conventional commit format (feat:, fix:, refactor:, etc.)
- Generates and applies changelog entries
- Validates commit messages to avoid filler words and meta phrases

### Session Management

Never lose your context:

- **Resume**: Pick up where you left off (`omp --resume` or `/resume` command)
- **Branch**: Create a new conversation branch from any point (`/branch`)
- **Tree navigation**: View and navigate your conversation history (`/tree`)
- **Auto-titling**: Sessions are automatically named based on your first message

### Extension/Plugin/Hook System

Extend oh-my-pi with custom functionality:

- **Plugins**: Install MCP (Model Context Protocol) servers for external tools
- **Extensions**: Write TypeScript modules that add new capabilities
- **Hooks**: Inject custom behavior at key points in the agent lifecycle
- **Custom slash commands**: Create your own TUI commands with full API access

### 65+ Built-In Themes

Customize your terminal experience with themes like Catppuccin, Dracula, Nord, Gruvbox, Tokyo Night, and many more. Switch themes on-the-fly with `/theme`.

### Native Performance via Rust N-API Addons

Performance-critical operations are implemented in Rust (compiled to native machine code) for maximum speed:

- **Grep**: ~1,300 lines of Rust using ripgrep internals
- **Shell**: ~1,025 lines embedding a bash interpreter (no subprocess spawning)
- **Text processing**: ANSI-aware width calculations, wrapping, truncation
- **Syntax highlighting**: Fast code highlighting for 30+ languages
- **Image processing**: Encode/decode/resize images without external tools
- **And more**: Keyboard parsing, glob matching, clipboard access, process management

### Task/Subagent System

Parallelize complex work with specialized agents:

- **5 bundled agents**: explore, plan, browser, task, reviewer
- **Parallel execution**: Run multiple tasks simultaneously with progress tracking
- **Isolated execution**: Run tasks in separate git worktrees to avoid conflicts
- **Real-time streaming**: See agent outputs as they're generated

---

## Prerequisites

Before installing oh-my-pi, you'll need a few things set up on your system. Don't worry — we'll walk through each one.

### 1. Bun Runtime (version 1.3.7 or higher)

**What is Bun?**

Bun is a JavaScript runtime — a program that runs JavaScript code. If you've heard of Node.js, Bun is similar but newer and faster. It can run JavaScript and TypeScript directly without needing a separate build step.

**Why do I need it?**

oh-my-pi is written in TypeScript (a type-safe version of JavaScript), and Bun is what executes that code.

**How to install:**

Visit [https://bun.sh](https://bun.sh) and follow the installation instructions for your operating system:

- **macOS/Linux**: Run `curl -fsSL https://bun.sh/install | bash` in your terminal
- **Windows**: Run `powershell -c "irm bun.sh/install.ps1|iex"` in PowerShell

After installation, verify it works by running:

```bash
bun --version
```

You should see version 1.3.7 or higher.

### 2. Git

**What is Git?**

Git is version control software that tracks changes to your code. Most software projects use Git.

**Why do I need it?**

oh-my-pi needs Git to track your project's history and generate intelligent commit messages.

**How to install:**

- **macOS**: Install Xcode Command Line Tools by running `xcode-select --install`, or use Homebrew: `brew install git`
- **Linux**: Use your package manager (e.g., `sudo apt install git` on Ubuntu/Debian, `sudo dnf install git` on Fedora)
- **Windows**: Download from [https://git-scm.com](https://git-scm.com)

Verify installation:

```bash
git --version
```

### 3. An API Key from an LLM Provider

**What is an API key?**

An API key is like a password that lets oh-my-pi access AI services on your behalf. When the AI generates code or answers questions, it's actually sending your request to a cloud service (like OpenAI or Anthropic) that runs the large language model.

**Why do I need it?**

oh-my-pi doesn't run the AI models itself — they're too large. Instead, it sends your requests to a provider's servers, which requires authentication via an API key.

**Which provider should I choose?**

Popular options for beginners:

1. **Anthropic Claude** (recommended for coding)
   - Sign up at [https://console.anthropic.com](https://console.anthropic.com)
   - Navigate to "API Keys" and create a new key
   - Claude Sonnet is excellent for coding tasks
   - Pricing: Pay-as-you-go (usually a few cents per conversation)

2. **OpenAI GPT**
   - Sign up at [https://platform.openai.com](https://platform.openai.com)
   - Go to "API keys" and generate a new key
   - GPT-4o is a good all-around model
   - Pricing: Pay-as-you-go

3. **Google Gemini**
   - Get a key at [https://aistudio.google.com/apikey](https://aistudio.google.com/apikey)
   - Free tier available with generous limits
   - Good for larger context windows

You only need **one** provider to get started. You can add more later.

### 4. Rust Nightly Toolchain (Optional)

**What is Rust?**

Rust is a programming language known for safety and performance. oh-my-pi uses Rust for speed-critical operations.

**Why do I need it?**

You only need Rust if you plan to build oh-my-pi from source or develop native addons. If you're installing via the prebuilt binary or Bun package, you can skip this.

**How to install:**

If you do need Rust:

```bash
# Install rustup (the Rust installer)
curl --proto '=https' --tlsv1.2 -sSf https://sh.rustup.rs | sh

# Install nightly toolchain (required for this project)
rustup toolchain install nightly
rustup default nightly
```

Verify installation:

```bash
rustc --version
```

---

## Installation

Choose the method that works best for you. We recommend the Bun method for most users.

### Method 1: Via Bun (Recommended)

This is the easiest method and ensures you always get the latest version.

**Prerequisites**: Bun must be installed (see [Prerequisites](#prerequisites) above).

```bash
bun install -g @oh-my-pi/pi-coding-agent
```

The `-g` flag means "global" — it installs the `omp` command system-wide so you can run it from any directory.

After installation, verify it works:

```bash
omp --version
```

### Method 2: Via Installer Script

These installer scripts automatically download the appropriate version for your system.

**Linux / macOS:**

```bash
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.sh | sh
```

**Windows (PowerShell):**

```powershell
irm https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.ps1 | iex
```

**What does the installer do?**

By default, it checks if you have Bun installed:
- If yes: Uses Bun to install oh-my-pi (Method 1 above)
- If no: Downloads a prebuilt binary for your platform

**Advanced installer options:**

Force Bun installation (installs Bun first if needed):

```bash
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.sh | sh -s -- --source
```

Force prebuilt binary:

```bash
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.sh | sh -s -- --binary
```

Install a specific version:

```bash
# Install version 3.20.1 as a binary
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.sh | sh -s -- --binary --ref v3.20.1

# Install from the main branch (source install)
curl -fsSL https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.sh | sh -s -- --source --ref main
```

**Windows PowerShell advanced options:**

```powershell
# Install a specific version
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.ps1))) -Binary -Ref v3.20.1

# Install from main branch
& ([scriptblock]::Create((irm https://raw.githubusercontent.com/can1357/oh-my-pi/main/scripts/install.ps1))) -Source -Ref main
```

### Method 3: Manual Download from GitHub Releases

If you prefer to download the binary yourself:

1. Go to [https://github.com/can1357/oh-my-pi/releases/latest](https://github.com/can1357/oh-my-pi/releases/latest)
2. Download the appropriate file for your system:
   - **macOS Intel**: `omp-darwin-x64`
   - **macOS Apple Silicon**: `omp-darwin-arm64`
   - **Linux x64**: `omp-linux-x64`
   - **Linux ARM64**: `omp-linux-arm64`
   - **Windows x64**: `omp-win32-x64.exe`
3. Make it executable (macOS/Linux):
   ```bash
   chmod +x omp-*
   ```
4. Move it to a directory in your PATH:
   ```bash
   # macOS/Linux
   sudo mv omp-* /usr/local/bin/omp

   # Windows: Move to C:\Windows\System32\ or add to PATH
   ```

### Method 4: From Source (For Developers)

If you want to contribute to oh-my-pi or customize it heavily:

**Prerequisites**: Bun and Rust nightly toolchain (see [Prerequisites](#prerequisites)).

```bash
# Clone the repository
git clone https://github.com/can1357/oh-my-pi.git
cd 