---
repo: claude-plugins-tutorials
description: Detailed documentation and tutorials for all Claude Code official and external plugins
language: None
stars: 1
forks: 1
created: 2026-03-10
updated: 2026-03-29
topics: 
is_fork: False
kb: 232
---

# claude-plugins-tutorials
# Claude Code Plugins Tutorials

Detailed documentation and tutorials for every plugin in the [official Claude Code plugins registry](https://github.com/anthropics/claude-code-plugins).

Each plugin has its own markdown file covering what it does, how to install it, how to use it, and real-world use-case examples.

## What's Inside

### Official Plugins (29)

Maintained by Anthropic. Install with `claude plugin add <name>`.

| Plugin | Category | Description |
|--------|----------|-------------|
| [agent-sdk-dev](plugins/agent-sdk-dev.md) | Development | Create and verify Claude Agent SDK applications |
| [clangd-lsp](plugins/clangd-lsp.md) | Language Server | C/C++ code intelligence via clangd |
| [claude-code-setup](plugins/claude-code-setup.md) | Setup | Analyze codebases and recommend Claude Code automations |
| [claude-md-management](plugins/claude-md-management.md) | Maintenance | Audit and improve CLAUDE.md files |
| [code-review](plugins/code-review.md) | Code Quality | Automated PR review with confidence-based scoring |
| [code-simplifier](plugins/code-simplifier.md) | Code Quality | Simplify and refine code for clarity and maintainability |
| [commit-commands](plugins/commit-commands.md) | Git Workflow | Streamlined commit, push, and PR creation |
| [csharp-lsp](plugins/csharp-lsp.md) | Language Server | C# code intelligence |
| [example-plugin](plugins/example-plugin.md) | Reference | Template demonstrating all plugin extension options |
| [explanatory-output-style](plugins/explanatory-output-style.md) | Output Style | Educational insights about implementation choices |
| [feature-dev](plugins/feature-dev.md) | Development | 7-phase feature development with specialized agents |
| [frontend-design](plugins/frontend-design.md) | Design | Distinctive, production-grade frontend interfaces |
| [gopls-lsp](plugins/gopls-lsp.md) | Language Server | Go code intelligence via gopls |
| [hookify](plugins/hookify.md) | Automation | Create hooks to prevent unwanted behaviors |
| [jdtls-lsp](plugins/jdtls-lsp.md) | Language Server | Java code intelligence via Eclipse JDT.LS |
| [kotlin-lsp](plugins/kotlin-lsp.md) | Language Server | Kotlin code intelligence |
| [learning-output-style](plugins/learning-output-style.md) | Output Style | Interactive learning mode with code contribution requests |
| [lua-lsp](plugins/lua-lsp.md) | Language Server | Lua code intelligence via LuaLS |
| [php-lsp](plugins/php-lsp.md) | Language Server | PHP code intelligence via Intelephense |
| [playground](plugins/playground.md) | Development | Interactive HTML playgrounds with live preview |
| [plugin-dev](plugins/plugin-dev.md) | Development | Toolkit for creating and validating plugins |
| [pr-review-toolkit](plugins/pr-review-toolkit.md) | Code Quality | Comprehensive PR review with 6 specialized agents |
| [pyright-lsp](plugins/pyright-lsp.md) | Language Server | Python static type checking via Pyright |
| [ralph-loop](plugins/ralph-loop.md) | Automation | Continuous self-referential AI loops for iterative development |
| [rust-analyzer-lsp](plugins/rust-analyzer-lsp.md) | Language Server | Rust code intelligence via rust-analyzer |
| [security-guidance](plugins/security-guidance.md) | Security | Warns about potential security issues when editing files |
| [skill-creator](plugins/skill-creator.md) | Development | Create, improve, and benchmark skills |
| [swift-lsp](plugins/swift-lsp.md) | Language Server | Swift code intelligence via SourceKit-LSP |
| [typescript-lsp](plugins/typescript-lsp.md) | Language Server | TypeScript/JavaScript code intelligence |

### External Plugins (13)

Third-party integrations from service providers. Install with `claude plugin add <name>`.

| Plugin | Author | Description |
|--------|--------|-------------|
| [asana](external_plugins/asana.md) | Asana | Project management - tasks, projects, assignments |
| [context7](external_plugins/context7.md) | Upstash | Up-to-date documentation lookup from source repos |
| [firebase](external_plugins/firebase.md) | Google | Firestore, auth, cloud functions, hosting, storage |
| [github](external_plugins/github.md) | GitHub | Issues, PRs, code review, repository management |
| [gitlab](external_plugins/gitlab.md) | GitLab | Repos, merge requests, CI/CD, issues, wikis |
| [greptile](external_plugins/greptile.md) | Greptile | AI code review agent for GitHub and GitLab |
| [laravel-boost](external_plugins/laravel-boost.md) | Laravel | Artisan, Eloquent, routing, migrations |
| [linear](external_plugins/linear.md) | Linear | Issue tracking, projects, status management |
| [playwright](external_plugins/playwright.md) | Microsoft | Browser automation and end-to-end testing |
| [serena](external_plugins/serena.md) | Oraios | Semantic code analysis and refactoring suggestions |
| [slack](external_plugins/slack.md) | Slack | Search messages, access channels, read threads |
| [stripe](external_plugins/stripe.md) | Stripe | Payments, checkout, subscriptions, webhooks |
| [supabase](external_plugins/supabase.md) | Supabase | Database, auth, storage, real-time subscriptions |

## Each Doc Includes

- **Overview** - what the plugin does and who it's for
- **Installation** - step-by-step setup instructions
- **Commands / Skills / Agents** - every component explained
- **How to Use** - practical workflow guidance
- **Use Case Examples** - real-world scenarios with example prompts
- **Requirements** - dependencies and prerequisites

## Quick Start

```bash
# Install any plugin
claude plugin add <plugin-name>

# Verify installation
claude plugin list

# Remove a plugin
claude plugin remove <plugin-name>
```

## How These Docs Were Generated

These 42 documentation files were generated entirely by **Claude Code (Opus 4.6)** using a multi-agent parallel workflow. No docs were written by hand.

### Process

1. **Source reading** - Two research agents were launched in parallel to read every file in the official [`plugins/`](https://github.com/anthropics/claude-code-plugins/tree/main/plugins) and [`external_plugins/`](https://github.com/anthropics/claude-code-plugins/tree/main/external_plugins) directories. Each agent read all `plugin.json`, `README.md`, `.mcp.json`, `commands/*.md`, `skills/*/SKILL.md`, `agents/*.md`, and `hooks/` files, returning the complete raw contents.

2. **Parallel doc generation** - Up to 16 builder agents were launched simultaneously, each assigned one plugin (or a small batch of similar plugins like the LSP servers). Every agent received the full plugin metadata and source content, then wrote a standalone markdown file following a consistent structure.

3. **Gap detection and second pass** - After the first pass produced 17 of 29 plugin docs, a directory listing (`ls`) revealed 12 were missed due to truncated `Glob` output. A second wave of 7 agents was launched to cover the missing plugins.

4. **Verification** - A `diff` between source directories and output files confirmed 29/29 plugins and 13/13 external plugins were documented.

### Architecture

```
User prompt
    |
    v
[Research Agent 1]  ──→  Read all plugins/ source files
[Research Agent 2]  ──→  Read all external_plugins/ source files
    |
    v
[Builder Agent 1]   ──→  agent-sdk-dev.md
[Builder Agent 2]   ──→  claude-code-setup.md
[Builder Agent 3]   ──→  claude-md-management.md
    ...                   (up to 16 agents in parallel)
[Builder Agent 16]  ──→  serena.md, slack.md, stripe.md, supabase.md
    |
    v
[Verification]      ──→  diff source vs output: 42/42 match
```

### What Each Agent Did

Each builder agent received:
- The plugin's `plugin.json` metadata (name, author, description)
- The full contents of all commands, skills, agents, hooks, and MCP configs
- Instructions to produce a doc with: Overview, Installation, Commands/Skills/Agents, How to Use, Use Case Examples (3+), and Requirements

Agents wrote docs independently and in parallel. No agent saw another agent's output.

### Stats

| Metric | Value |
|--------|-------|
| Total agents launched | 25 (2 research + 23 builders) |
| Docs produced | 42 plugin docs + 1 README + 1 lessons-learned |
| Total lines of documentation | 16,883 |
| Passes required | 2 (first pass missed 12 plugins due to truncated enumeration) |

### Lessons Learned

The first pass missed 12 of 29 plugins because `Glob("**/*")` truncated its output, and the incomplete list was passed downstream without verification. The fix was simple: use `ls` for directory enumeration (never truncates), then verify output count matches source count before declaring done.

Full write-up: [LESSONS-LEARNED.md](LESSONS-LEARNED.md)

## Source

These docs are based on the [official Claude Code plugins repository](https://github.com/anthropics/claude-code-plugins) by Anthropic.
