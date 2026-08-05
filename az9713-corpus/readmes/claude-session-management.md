# AI Agent Context Templates

A practical template library for keeping Claude, Claude Code, Cowork-style agents, and general LLM sessions focused, cheap, and recoverable.

The core idea: treat context as scarce working memory. Use explicit task contracts, scope boundaries, handoffs, compaction prompts, and local memory files instead of letting chats become unbounded transcripts.

## Background

This repository is inspired by the YouTube video **[21 Ways to STOP Hitting Your Claude Limits (Code & Cowork)](https://www.youtube.com/watch?v=MxE76CbiXOs&t=18s)**. The templates operationalize the techniques covered in that video into copy-paste-ready files.

The primary reference is [`claude_21_context_hygiene_techniques.md`](claude_21_context_hygiene_techniques.md) — a detailed write-up of all 21 techniques with replication steps, prompts, and critique. It covers:

| Group | Techniques |
|---|---|
| General Claude (9) | Edit prompts instead of corrections, batch requests, fresh chat with handoff, right model for the task, turn off extended thinking, convert files to markdown, use Projects for repeated docs, session reset timing, work off-peak |
| Claude Code (8) | `/context` before typing, disconnect unused MCP servers, prefer CLIs over MCP, `/clear` between tasks, `/compact` at mid-context, rewind/restore on bad edits, session handoff vs. compact, subagents for heavy tasks, clean `CLAUDE.md` |
| Claude Cowork (4) | Dedicated clean folder, local memory system, external tools for research, skills for repeatable workflows |

The central thesis: **context rot** — not just plan tier — drives usage limits. The cure is explicit context architecture.

> Preserve state. Delete noise. Compress deliberately. Route work to the right tool and model.

## What is included

### Reference

| File | Purpose |
|---|---|
| `claude_21_context_hygiene_techniques.md` | Full 21-technique reference with replication steps, prompts, templates, and critique |
| `template-acceptance-tests.md` | 10-point checklist for evaluating whether a template is production-grade |
| `template-acceptance-matrix.md` | How each template satisfies the acceptance tests, with scores and residual weaknesses |

### Templates

| Template | Purpose |
|---|---|
| `templates/universal-one-shot-work-order.md` | General task contract: goal, inputs, execution mode, tasks, scope, output format, acceptance tests |
| `templates/session-handoff.md` | Transfer state into a fresh chat with objective, decisions, artifacts, open questions, and next actions |
| `templates/project-instructions.md` | Compact project-level behavior instructions for Claude Projects |
| `templates/claude-code-compacting.md` | Controlled compaction prompt for Claude Code — preserve/discard specification |
| `templates/claude-code-session-handoff.md` | Full coding-session handoff covering repo context, files touched, tests run, decisions, and failures |
| `templates/subagent-task.md` | Bounded prompt for subagents: scoped investigation with explicit authority and output limits |
| `templates/CLAUDE.md` | Claude Code project instruction skeleton — core rules, safety boundaries, execution modes |
| `templates/cowork-workspace.md` | Clean folder layout for Cowork-style execution |
| `templates/instructions.md` | Local workspace operating instructions with authority, context, output, and memory policies |
| `templates/memory.md` | Durable local memory template: project, preferences, decisions, workflows, pitfalls |
| `templates/skill-template.md` | Claude Skill-style reusable workflow template with inputs, procedure, quality bar, and versioning |

### Examples

| Example | Purpose |
|---|---|
| `examples/example-coding-task.md` | Filled universal work order for a bug fix |
| `examples/example-session-handoff.md` | Filled session handoff for a multi-session coding project |

## Quick start

Copy the template you need into your project or agent workspace:

```bash
# Claude Code project
cp templates/CLAUDE.md my-project/CLAUDE.md

# Session state management
cp templates/session-handoff.md my-project/.agent/session-handoff.md

# Cowork workspace
mkdir -p cowork-workspace/inputs cowork-workspace/outputs cowork-workspace/references
cp templates/instructions.md cowork-workspace/instructions.md
cp templates/memory.md cowork-workspace/memory.md
```

For Claude Code sessions, start with:

```text
/context
/mcp
```

Inspect what is loaded. Disconnect irrelevant MCP servers. Then begin with a bounded task prompt from `universal-one-shot-work-order.md`.

## Template selection guide

| Situation | Template to use |
|---|---|
| Starting a serious one-off task | `universal-one-shot-work-order.md` |
| Chat is getting long (15–20 messages) | `session-handoff.md` |
| Starting a Claude Code repo session | `CLAUDE.md` + `universal-one-shot-work-order.md` |
| Context window is getting large | `claude-code-compacting.md` |
| Switching to a new session phase | `claude-code-session-handoff.md` |
| Delegating codebase investigation | `subagent-task.md` |
| Setting up a Cowork task folder | `cowork-workspace.md` + `instructions.md` + `memory.md` |
| Encoding a repeatable workflow | `skill-template.md` |

## Design principles

1. **Explicit authority**: every serious task prompt specifies inspect, propose, edit, test, or deploy.
2. **Scope boundaries**: define what to use and what to ignore — not just what to do.
3. **Context hygiene**: preserve decisions, discard logs and dead ends.
4. **Recoverability**: every long session should produce a handoff.
5. **Reusable artifacts**: templates, memory files, skills, and project instructions live in files, not just chat history.
6. **Acceptance tests**: every serious agent task defines what success looks like.

## Template quality bar

Each template is evaluated against ten acceptance tests (see `template-acceptance-tests.md`):

1. Reduces future turns
2. Reduces irrelevant context
3. Preserves necessary state
4. Constrains output format
5. Prevents broad unnecessary scanning
6. Specifies execution authority
7. Includes success criteria
8. Avoids vague personality instructions
9. Produces reusable artifacts
10. Executable by a different model

Templates scoring 9+ are considered production-grade. See `template-acceptance-matrix.md` for per-template scores and residual weaknesses.

## License

MIT.
