---
repo: claude-managed-agent-skills
description: Tutorial and reference docs for Claude Managed Agents skills in the /claude-api skill
language: TypeScript
stars: 0
forks: 0
created: 2026-04-13
updated: 2026-04-13
topics: 
is_fork: False
kb: 30
---

# claude-managed-agent-skills
# Claude Managed Agents — Skills Tutorial & Reference

A tutorial collection with deep-dive documentation for the **Claude Managed Agents** skills built into the `/claude-api` skill in Claude Code.

Use this repo to understand how the Managed Agents API works, how to invoke the `/claude-api` skill effectively, and as reference when building real production agents.

---

## What are Claude Managed Agents?

Claude Managed Agents is Anthropic's hosted agent platform. You supply an agent config (model, system prompt, tools); Anthropic runs the agent loop and provisions an isolated container per session where tools execute — bash, file I/O, web search, MCP integrations. No infrastructure to manage.

Architecture: `Agent (config, versioned)` → `Session (stateful run)` → `Container (tool execution sandbox)`

---

## Source Skills This Repo Documents

This repo is a tutorial and reference companion to the official Anthropic skill files:

### `shared/` — Concept & API Reference
[`anthropics/skills/.../claude-api/shared/`](https://github.com/anthropics/skills/tree/main/skills/claude-api/shared)

| File | Covers |
|------|--------|
| [`managed-agents-overview.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-overview.md) | Architecture, mandatory Agent→Session flow, beta headers, common pitfalls |
| [`managed-agents-core.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-core.md) | Agents, Sessions, Environments — full field reference + versioning |
| [`managed-agents-environments.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-environments.md) | Container networking config, file uploads, GitHub repo mounts |
| [`managed-agents-tools.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-tools.md) | Built-in toolset, MCP servers, custom tools, skills, vaults/credentials |
| [`managed-agents-events.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-events.md) | SSE streaming, polling, all event types, reconnect patterns |
| [`managed-agents-client-patterns.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-client-patterns.md) | 9 concrete client patterns: idle-break gate, reconnect, interrupt, file gotchas |
| [`managed-agents-api-reference.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-api-reference.md) | Full endpoint + SDK method reference (Python, TypeScript, Go) |
| [`managed-agents-onboarding.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/shared/managed-agents-onboarding.md) | Interview script used by `/claude-api managed-agents-onboard` |

### `python/managed-agents/` — Python SDK Examples
[`anthropics/skills/.../claude-api/python/managed-agents/`](https://github.com/anthropics/skills/tree/main/skills/claude-api/python/managed-agents)

| File | Covers |
|------|--------|
| [`README.md`](https://github.com/anthropics/skills/blob/main/skills/claude-api/python/managed-agents/README.md) | Python SDK bindings — create agent, session, stream events, custom tools, vaults, MCP |

---

## Docs in This Repo

### [`managed-agents-docs.md`](./managed-agents-docs.md)
Comprehensive reference covering the full Managed Agents API:
- Agent vs Session vs Environment — what each is, what fields belong where
- The mandatory `agents.create()` → `sessions.create()` flow and why
- All 8 built-in tools (`agent_toolset_20260401`)
- MCP server setup + vault credentials (OAuth, token refresh)
- Custom tools — the host-side credentials pattern
- Prebuilt skills (xlsx, docx, pptx, pdf)
- SSE event streaming — all event types, stream-first ordering rule
- The critical idle-break gate (`stop_reason.type !== "requires_action"`)
- Complete Python and TypeScript examples

### [`claude-api-invocation-guide.md`](./claude-api-invocation-guide.md)
How to use the `/claude-api` skill in Claude Code:
- The one explicit subcommand: `/claude-api managed-agents-onboard`
- What the onboarding interview covers (3 rounds + session setup → 2 code blocks)
- Natural language triggers for each of the 8 source skill files
- Quick reference: what to say to get guidance on any Managed Agents topic

---

## How to Use the `/claude-api` Skill

### Guided setup from scratch
```
/claude-api managed-agents-onboard
```
Runs an interactive interview → emits a setup script (run once) + runtime script (run per invocation).

### Natural language — no slash command needed
```
"I'm building a Managed Agent that reads from a GitHub repo and sends to Slack"
"How do I store OAuth credentials for MCP servers?"
"My session breaks idle too early after custom tool calls"
"Show me how to mount a private GitHub repo into a session"
"I want to require approval before the agent runs bash"
```

---

## Example App

The `example/` directory contains a production-ready **GitHub + Slack agent**:

- Reads files from a private GitHub repository
- Answers questions about the repo content via a Slack bot
- Demonstrates: GitHub repo mount, Slack MCP, custom tools, SSE event loop, vault credentials

See [`example/README.md`](./example/README.md) for setup and prompts.

---

## Key Concepts at a Glance

| Concept | Key point |
|---------|-----------|
| **Agents are persistent** | Create once, reference by ID. Never call `agents.create()` per invocation |
| **Sessions are per-run** | Create per invocation, reference agent ID + version |
| **Stream before send** | Open SSE stream before sending the kickoff message |
| **Idle-break gate** | Check `stop_reason.type !== "requires_action"` before breaking |
| **Credentials in vaults** | MCP auth goes in vaults, not inline on the agent |
| **Custom tools = host-side secrets** | Your app handles the call; the container never sees your API keys |
| **First-party only** | Managed Agents not available on Bedrock, Vertex, or Foundry |

---

## Related Links

- [Anthropic Skills Repo](https://github.com/anthropics/skills/tree/main/skills/claude-api)
- [Managed Agents Docs](https://platform.claude.com/docs/en/managed-agents/)
- [Claude Code](https://claude.ai/code)
