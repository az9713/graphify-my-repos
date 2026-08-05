---
repo: claude-code-dynamic-workflows
description: 
language: None
stars: 0
forks: 0
created: 2026-05-29
updated: 2026-05-29
topics: 
is_fork: False
kb: 4
---

# claude-code-dynamic-workflows
# Claude Code Dynamic Workflows

A concise, hands-on cheatsheet for using **dynamic workflows** in the Claude Code CLI.

Dynamic workflows let Claude Code write and run a JavaScript orchestration script that
coordinates many subagents in the background — useful for codebase-wide audits, large
migrations, cross-checked research, and multi-angle planning, where a task needs more
agents than one conversation turn can coordinate.

## Contents

- **[claude-code-workflows-cheatsheet.md](./claude-code-workflows-cheatsheet.md)** — the cheatsheet.

The cheatsheet focuses on **workflow usage from the CLI**: how to invoke a workflow,
monitor progress, stop a run, view and save the generated script, and keep token usage
under control. It includes a quick-reference table of the relevant slash commands and
keyboard shortcuts.

## Source

Distilled from the official Claude / Claude Code documentation:

- Dynamic workflows docs: <https://code.claude.com/docs/en/workflows>
- Introducing dynamic workflows in Claude Code: <https://claude.com/blog/introducing-dynamic-workflows-in-claude-code>
- Claude Opus 4.8 announcement: <https://www.anthropic.com/news/claude-opus-4-8>

Refer to the official docs for the authoritative and most up-to-date details. Dynamic
workflows are a research preview feature and require Claude Code `v2.1.154` or later.
