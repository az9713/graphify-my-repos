# playwright-cli (enhanced documentation fork)

> **This is a clone of Microsoft's [`@playwright/cli`](https://github.com/microsoft/playwright-cli) enhanced with comprehensive documentation, including AI workflow guides for coding agents like Claude Code.**

The original repo provides the CLI source code and npm package. This fork adds:

- **[User Guide](docs/USER_GUIDE.md)** — 10 hands-on use cases from hello world to multi-session automation
- **[Developer Guide](docs/DEVELOPER_GUIDE.md)** — complete contributor guide for the JavaScript/TypeScript ecosystem
- **[Architecture Guide](docs/ARCHITECTURE.md)** — deep dive into the thin-wrapper design and daemon pattern
- **[AI Workflows](docs/AI_WORKFLOWS.md)** — 25 production-ready browser automation workflows with bash scripts
- **[Claude Code integration](#using-playwright-cli-with-claude-code)** — natural language browser automation via skill system
- **[Test transcripts](outputs/)** — real Claude Code session transcripts demonstrating playwright-cli in action

Original repo: https://github.com/microsoft/playwright-cli

---

> A CLI wrapper around Playwright for browser automation, optimized for coding agents like Claude Code and GitHub Copilot.

[![npm version](https://img.shields.io/npm/v/@playwright/cli)](https://www.npmjs.com/package/@playwright/cli)
[![License: Apache-2.0](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Node.js 18+](https://img.shields.io/badge/node-%3E%3D18-brightgreen)](https://nodejs.org/)
[![Playwright](https://img.shields.io/badge/powered%20by-Playwright-45ba4b)](https://playwright.dev)

---

## Table of Contents

- [What is playwright-cli?](#what-is-playwright-cli)
- [playwright-cli vs Playwright MCP](#playwright-cli-vs-playwright-mcp)
- [Key Features](#key-features)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using playwright-cli with Claude Code](#using-playwright-cli-with-claude-code)
- [Quick Start: 5-Minute Guide](#quick-start-5-minute-guide)
- [Headed vs Headless Operation](#headed-vs-headless-operation)
- [Sessions](#sessions)
- [Monitoring with `playwright-cli show`](#monitoring-with-playwright-cli-show)
- [Understanding Snapshots and Refs](#understanding-snapshots-and-refs)
- [Command Reference](#command-reference)
  - [Core Commands](#core-commands)
  - [Navigation](#navigation)
  - [Keyboard](#keyboard)
  - [Mouse](#mouse)
  - [Save As](#save-as)
  - [Tabs](#tabs)
  - [Storage](#storage)
  - [Network Mocking](#network-mocking)
  - [DevTools](#devtools)
  - [Session Management](#session-management)
- [Configuration File](#configuration-file)
- [Environment Variables](#environment-variables)
- [Skills Installation for Agent Integration](#skills-installation-for-agent-integration)
- [Specific Task Guides](#specific-task-guides)
- [Running Tests](#running-tests)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)

---

## What is playwright-cli?

### The building blocks: browsers, automation, and CLIs

A **web browser** (Chrome, Firefox, Safari) is software that downloads and displays web pages.
Normally a human sits at a keyboard and controls it. **Browser automation** means writing code that
controls the browser instead — clicking buttons, filling in forms, taking screenshots — all without
a human.

**Playwright** is a library made by Microsoft that makes browser automation easy. It can drive
Chromium, Firefox, and WebKit browsers. Developers use it to write automated tests and scraping
scripts in JavaScript, Python, Java, and other languages.

A **CLI** (Command-Line Interface) is a program you run by typing commands in a terminal (the black
window where you compile C++ programs). Instead of calling library functions inside a program, you
run short shell commands like:

```
playwright-cli open https://example.com
playwright-cli click e3
playwright-cli screenshot
```

**playwright-cli** wraps the full Playwright engine behind these short shell commands. Each command
connects to a running browser, performs one action, and exits. Your browser session stays alive
between calls so you can build up complex workflows command by command.

### What are coding agents?

A **coding agent** is an AI assistant (like Claude Code or GitHub Copilot Workspace) that can read
your codebase, reason about tasks, and take actions — including running shell commands — to complete
work. When you ask Claude Code to "write a Playwright test for the login page", it can run
`playwright-cli` commands directly to explore the page, discover element references, and verify its
work, all without leaving your terminal.

playwright-cli is specifically optimized for this agent-plus-human workflow.

---

## playwright-cli vs Playwright MCP

Microsoft also makes **Playwright MCP**, which exposes Playwright through the Model Context Protocol.
Both tools automate browsers for AI agents, but they make different trade-offs.

### The core difference: token efficiency

Every word sent to an AI model costs **tokens** — think of tokens as the AI's working memory.
Context windows (the amount the AI can hold in mind at once) are limited, and loading heavy tool
schemas eats into that budget fast.

```
Playwright CLI skill loaded into agent context: ~68 tokens
Playwright MCP tools loaded into agent context: ~3,600 tokens
```

That 50x difference matters when your agent also needs to hold a large codebase, test files, and
reasoning steps in context simultaneously.

### When to use which

| Situation | Best choice |
|-----------|-------------|
| Coding agents (Claude Code, Copilot) with large codebases | **playwright-cli** |
| High-throughput automation inside tight context windows | **playwright-cli** |
| Simple bash scripts for end-to-end testing | **playwright-cli** |
| Exploratory autonomous agents that reason over page structure | **Playwright MCP** |
| Self-healing tests that need rich DOM introspection | **Playwright MCP** |
| Cross-platform standardized integrations (mobile/desktop/browser) | **Playwright MCP** |

From a real-world comparison: the same automation task used 16% of the context window with
playwright-cli vs 18% with MCP — and playwright-cli makes all advanced features (PDF, tracing, etc.)
available by default, while MCP restricts them to manage token costs.

Learn more: [Playwright MCP](https://github.com/microsoft/playwright-mcp)

---

## Key Features

- **Token-efficient** — the skill definition is tiny (~68 tokens); page data is never forced into
  the model context
- **Full Playwright engine** — all 52+ commands covering navigation, interaction, storage, network
  mocking, video, tracing, PDF generation
- **Multi-session support** — run several isolated browsers side by side with named sessions
- **State persistence** — optionally persist cookies and storage across browser restarts
- **Visual monitoring dashboard** — watch your agent's browser sessions live with `playwright-cli show`
- **Test code generation** — every action produces the equivalent Playwright TypeScript code
- **Agent-ready skills** — install structured skill files that Claude Code and GitHub Copilot
  understand natively
- **Cross-platform** — Windows, macOS, Linux
- **Config file + env vars** — flexible configuration without hard-coded values

---

## Prerequisites

Before installing playwright-cli, you need:

### 1. Node.js 18 or newer

Node.js is a runtime that lets you execute JavaScript outside a browser — the same role the JVM
plays for Java programs. npm (Node Package Manager) comes bundled with Node.js and is how you
install JavaScript packages, similar to how `apt` or `brew` installs system packages.

**Check if you already have it:**

```bash
node --version
# Should print: v18.x.x or higher

npm --version
# Should print: 9.x.x or higher
```

**If you don't have Node.js:**

Go to https://nodejs.org and download the **LTS** (Long Term Support) version for your operating
system. Run the installer and follow the prompts. When the installer finishes, open a new terminal
window and run the version checks above.

### 2. A terminal

- **Windows**: Use Git Bash, WSL, or Windows Terminal with PowerShell
- **macOS/Linux**: Use Terminal or any shell

### 3. A coding agent (optional but recommended)

playwright-cli works perfectly well as a standalone CLI tool. If you also want to use it with an
AI coding agent, you'll need one installed:

- [Claude Code](https://docs.anthropic.com/claude-code) — Anthropic's coding agent (recommended)
- [GitHub Copilot](https://github.com/features/copilot) — GitHub's coding agent

---

## Installation

### Step 1: Install playwright-cli globally

The `-g` flag installs the package globally so the `playwright-cli` command is available everywhere
on your system, not just inside one project folder.

```bash
npm install -g @playwright/cli@latest
```

You will see npm downloading and installing the package. This may take a minute.

### Step 2: Install browser binaries

Playwright needs browser executables to drive. This command downloads Chromium (and optionally
Firefox and WebKit):

```bash
npx playwright install chromium
```

To install all three browsers:

```bash
npx playwright install
```

### Step 3: Verify the installation

```bash
playwright-cli --help
```

You should see a list of available commands. If you see a "command not found" error, see
[Troubleshooting](#troubleshooting).

### Local installation (alternative)

If you prefer not to install globally (or if the global install fails), install locally inside
a project folder:

```bash
mkdir my-automation && cd my-automation
npm init -y
npm install @playwright/cli
```

Then prefix every command with `npx`:

```bash
npx playwright-cli open https://example.com
npx playwright-cli click e1
```

---

## Using playwright-cli with Claude Code

Every command in this README can also be invoked through natural language in
[Claude Code](https://docs.anthropic.com/en/docs/claude-code) — Anthropic's AI coding agent for
the terminal. Instead of typing individual commands, you describe what you want and Claude Code
translates it into the correct playwright-cli commands.

### Setup

**Step 1 — Install Claude Code** (if you haven't already)

```bash
npm install -g @anthropic-ai/claude-code
```

**Step 2 — Install the playwright-cli skill** (choose one)

```bash
# Option A: Per-project skill
playwright-cli install --skills

# Option B: Global plugin
claude plugin add @playwright/cli
```

### What happens when the skill loads

When you start Claude Code, it discovers installed skills and matches them to your prompts.
The playwright-cli skill (`skills/playwright-cli/SKILL.md`) contains:

```yaml
name: playwright-cli
description: Automates browser interactions for web testing, form filling, screenshots...
allowed-tools: Bash(playwright-cli:*)
```

When Claude Code loads this skill, you'll see a line like:

```
● Skill(playwright-cli)
  ⎿  Successfully loaded skill · 1 tool allowed
```

This means Claude Code has read the skill definition and now has permission to run
`playwright-cli` commands via Bash. The `allowed-tools: Bash(playwright-cli:*)` directive
pre-authorizes these commands so you won't be prompted for each one.

> **Note:** The exact skill name shown (e.g., `playwright-cli`, `browser-use`, `agent-browser`)
> depends on how the skill was installed and whether you have custom skill wrappers. What matters
> is that the loaded skill grants `Bash(playwright-cli:*)` tool access.

**Step 3 — Start Claude Code and try it**

```bash
claude
```

```
> Open https://demo.playwright.dev/todomvc/, add three todo items, check the
  first one off, and screenshot the result as todos.png
```

Claude Code reads the snapshot output, picks the right element refs, and runs each command
automatically.

### Important: ensuring Claude Code uses playwright-cli

If Claude Code has other browser tools available (such as MCP browser extensions), a generic
prompt like "open a website" may not use playwright-cli. To ensure playwright-cli is used:

**Option A — Mention it in your prompt** (simplest):

```
> Using playwright-cli, open https://example.com and take a screenshot
```

**Option B — Add a directive to your project's CLAUDE.md** (recommended for teams):

Add this line to your project's `CLAUDE.md` file:

```markdown
For all browser automation, use playwright-cli commands (not MCP browser tools).
```

Claude Code reads `CLAUDE.md` at the start of every session, so this ensures consistent routing.

**Option C — Use the skill name as a prefix**:

```
> Use playwright skills to test the login form on https://myapp.com
```

The phrase "playwright skills" triggers Claude Code to load the playwright-cli skill, which
contains the `allowed-tools: Bash(playwright-cli:*)` directive.

### Natural language instead of commands

```
Manual commands                              Claude Code prompt
─────────────────────────────────────        ────────────────────────────────────────
playwright-cli open https://example.com      "Go to example.com, search for
playwright-cli snapshot                       'playwright', and screenshot the
playwright-cli fill e5 "playwright"           results page as search.png"
playwright-cli press Enter
playwright-cli screenshot --filename=search.png
playwright-cli close
```

### Tips

- **Say what you want, not how.** Claude Code knows the commands.
- **Include URLs.** Claude Code cannot guess your site's address.
- **Ask for files.** "Save the screenshot as docs/hero.png" tells Claude Code where to write.
- **Claude Code handles refs.** It reads snapshots and picks element refs for you.
- **Chain tasks.** "Log in, navigate to settings, change the theme to dark mode, and screenshot."

---

## Quick Start: 5-Minute Guide

Let's automate the TodoMVC demo app — a classic to-do list web app used to demonstrate browser
automation.

### Step 1: Open a browser

```bash
playwright-cli open https://demo.playwright.dev/todomvc/ --headed
```

The `--headed` flag makes the browser window visible so you can watch what's happening. Without it,
the browser runs invisibly in the background (headless mode).

You will see output like:

```
### Page
- Page URL: https://demo.playwright.dev/todomvc/
- Page Title: React • TodoMVC
### Snapshot
[Snapshot](.playwright-cli/page-2026-02-18T12-00-00-000Z.yml)
```

### Step 2: Understand the snapshot

The **snapshot** is playwright-cli's way of describing the current page. Open the `.yml` file it
created, or run:

```bash
playwright-cli snapshot
```

The snapshot output looks something like this (simplified):

```
- textbox "What needs to be done?" [ref=e1]
- button "Toggle All" [ref=e2]
```

Each interactive element on the page gets a **ref** — a short label like `e1`, `e2`, `e21`. You
use these refs to target elements in subsequent commands. Think of them like line numbers: they
change when the page changes, so always take a fresh snapshot if you're unsure.

### Step 3: Add some todos

```bash
playwright-cli type "Buy groceries"
playwright-cli press Enter
playwright-cli type "Water flowers"
playwright-cli press Enter
playwright-cli type "Call the dentist"
playwright-cli press Enter
```

`type` sends keystrokes to whatever element is currently focused (the input box in this case).
`press Enter` submits the todo.

### Step 4: Take a fresh snapshot and check some boxes

```bash
playwright-cli snapshot
```

Look at the snapshot output for the checkboxes. They will have refs like `e21`, `e35`, etc.

```bash
playwright-cli check e21
playwright-cli check e35
```

### Step 5: Take a screenshot

```bash
playwright-cli screenshot --filename=todos.png
```

The screenshot is saved to `.playwright-cli/todos.png` (or the path you specify).

### Step 6: Close the browser

```bash
playwright-cli close
```

Congratulations — you just automated a browser from the command line. The same commands work inside
shell scripts, CI pipelines, and agent instructions.

### In Claude Code

The entire quick start above can be done with a single prompt:

```
> Open the TodoMVC demo at https://demo.playwright.dev/todomvc/ in headed mode.
  Add three todos: "Buy groceries", "Water flowers", "Call the dentist". Check
  off the first two. Take a screenshot called todos.png. Then close the browser.
```

---

## Headed vs Headless Operation

### Headless mode (default)

By default, playwright-cli runs the browser with no visible window. The browser process runs in the
background, invisible to you:

```
Your terminal ----command----> playwright-cli ----drives----> [invisible browser]
```

Headless mode is faster, uses less memory, and works on servers without displays. Use it in CI
pipelines and agent workflows.

```bash
playwright-cli open https://example.com
# Browser is invisible
```

### Headed mode

Adding `--headed` to `open` makes the browser window appear on screen. This is useful when:

- Debugging: you want to see exactly what is happening
- Learning: you want to watch the automation run
- Interacting: you want to take over from your agent

```bash
playwright-cli open https://example.com --headed
```

Once the browser is open, subsequent commands (`click`, `type`, etc.) work the same regardless of
whether the browser is headed or headless. The `--headed` flag only affects the `open` command.

### Mixing modes

You can open one session headed and another headless at the same time using [named sessions](#sessions):

```bash
playwright-cli -s=visible open https://example.com --headed
playwright-cli -s=background open https://example.com
```

---

## Sessions

### What is a session?

A **session** is a single browser instance managed by playwright-cli. Each session has its own:

- Cookies
- localStorage and sessionStorage
- IndexedDB
- Browsing history
- Open tabs

Sessions are how playwright-cli keeps the browser running between commands. When you run
`playwright-cli open`, it starts a browser. When you run `playwright-cli click e3`, it finds that
browser and sends the click. When you run `playwright-cli close`, it shuts the browser down.

```
playwright-cli open   ---> [browser starts, session created]
playwright-cli click  ---> [browser receives click, stays open]
playwright-cli type   ---> [browser receives keystrokes, stays open]
playwright-cli close  ---> [browser shuts down, session ends]
```

### The default session

When you don't specify a session name, commands use the **default** session. All the Quick Start
examples above used the default session.

### Named sessions

Named sessions let you run multiple browsers simultaneously, each completely isolated from the
others. Use the `-s=name` flag:

```bash
# Browser 1: logged in as admin
playwright-cli -s=admin open https://myapp.com/login

# Browser 2: logged in as regular user
playwright-cli -s=user open https://myapp.com/login

# Commands go to whichever session you specify
playwright-cli -s=admin fill e1 "admin@example.com"
playwright-cli -s=user fill e1 "user@example.com"
```

Name sessions descriptively so you can tell them apart:

```bash
# GOOD: purpose is clear
playwright-cli -s=github-auth open https://github.com
playwright-cli -s=staging-test open https://staging.myapp.com

# AVOID: generic names
playwright-cli -s=s1 open https://github.com
```

### In-memory vs persistent profiles

By default, browser profiles are kept **in memory**. Your cookies and storage survive across
multiple CLI commands within the same session, but are lost when the browser closes.

To save the profile to disk so it survives browser restarts, use `--persistent`:

```bash
playwright-cli open https://github.com --persistent
# Log in to GitHub...
playwright-cli close
# Later:
playwright-cli open https://github.com --persistent
# Still l