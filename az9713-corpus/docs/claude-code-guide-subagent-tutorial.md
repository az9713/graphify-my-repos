---
repo: claude-code-guide-subagent-tutorial
description: 50 practical use cases for the claude-code-guide subagent, a built-in specialized subagent that ships with Claude Code.
language: None
stars: 0
forks: 0
created: 2026-02-14
updated: 2026-02-14
topics: 
is_fork: False
kb: 20
---

# claude-code-guide-subagent-tutorial
# claude-code-guide Subagent Tutorial

A collection of **50 practical use cases** for the `claude-code-guide` subagent, a built-in specialized subagent that ships with Claude Code.

## What's Inside

The tutorial (`claude-code-guide-subagent-tutorial.md`) covers:

- **What the subagent is** -- a read-only research agent that answers questions about Claude Code, the Claude Agent SDK, and the Claude API
- **How it works** -- it researches using Glob, Grep, Read, WebFetch, and WebSearch, then hands findings back to the main session for implementation
- **50 use cases** across five categories:
  1. **Hooks & Automation** -- auto-formatting, lint gating, commit enforcement, security scans, branch protection, notifications, audit logging, and more
  2. **MCP Server Configuration** -- database queries, REST API bridges, Docker management, cloud CLI wrappers, ticket integrations, and documentation bridges
  3. **Agent SDK & Custom Agents** -- code review agents, migration agents, test coverage finders, incident response, onboarding buddies, multi-agent teams, and permission boundaries
  4. **Claude API Integration** -- streaming, tool definitions, prompt caching, context window management, retry logic, batch processing, extended thinking, and multimodal document processing
  5. **IDE & Workflow Integration** -- VS Code shortcuts, project-scoped settings, CLAUDE.md optimization, custom slash commands, git workflow automation, and permission mode tuning

Each use case includes a ready-to-paste **prompt** and step-by-step **testing instructions**.

The tutorial also includes a **real-world example** showing the full Claude Code session log from running Cat Wu's original prompt -- setting up a Windows notification hook for permission prompts. It demonstrates the complete workflow: Claude spawning the guide agent to research hooks, then implementing the PowerShell notification script and wiring up `settings.json` automatically.

## Usage

Copy any prompt from the tutorial into your Claude Code CLI session. Claude will use the `claude-code-guide` subagent internally to research the best approach, then implement the solution for you.

## Acknowledgement

This tutorial was inspired by the X post by [@_catwu](https://x.com/_catwu):
https://x.com/_catwu/status/2021650827233169662
