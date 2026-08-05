---
repo: second-brain-no-obsidian
description: A local Markdown second-brain scaffold inspired by Jay's no-Obsidian Claude Code workflow.
language: HTML
stars: 0
forks: 0
created: 2026-06-08
updated: 2026-07-27
topics: 
is_fork: False
kb: 205
---

# second-brain-no-obsidian
# Second Brain Knowledge Base

This folder is the durable knowledge-base root for the local second-brain system.

```text
<knowledge-base-root>
```

It stores a linked source mount, synthesized wiki pages, lint state, and output artifacts. Reusable agent operations now live in the global toolkit at:

```text
<global-toolkit-root>
```

Claude-discoverable copies of the global skills and commands are installed under:

```text
<claude-config-root>\skills
<claude-config-root>\commands
```

## What lives here

| Path | Purpose |
|---|---|
| `raw/` | Local-only read-only source mount pointing at the user's projects/source tree. |
| `wiki/` | Synthesized source pages, concept pages, registries, logs, and lint state. |
| `outputs/` | Generated briefs, memos, reports, and other artifacts. |
| `templates/` | Source, concept, and dream-report templates. |
| `docs/` | Architecture and usage documentation. |

## What no longer lives here

Reusable operating files (skills, commands, scripts, `AGENTS.md`, `CLAUDE.md`) were moved to the global toolkit; the full mapping is in [Global toolkit split](docs/global-toolkit-split.md).

## Root resolution

Global skills resolve the knowledge-base root in this order:

1. Use the `SECOND_BRAIN_ROOT` environment variable if set.
2. Otherwise use `<knowledge-base-root>`.

## Minimal workflow

From any project folder, use:

```text
capture <external-source-folder>
run dream sequence
```

`capture <external-source-folder>` registers text-like source files already available under:

```text
<knowledge-base-root>\raw\
```

By default, capture skips build artifacts, dependency folders, caches, binaries, and oversized files. It writes metadata to `wiki/source_manifest.jsonl`; it does not copy source files.

`run dream sequence` updates:

```text
<knowledge-base-root>\wiki\
<knowledge-base-root>\outputs\
```

## Documentation

- [Architecture and usage guide](docs/second-brain-architecture-and-usage.md)
- [Docs index](docs/index.md)
- [Global toolkit split](docs/global-toolkit-split.md)
- [Selective capture policy](docs/selective-capture.md)
- [Two-brain boundary policy](docs/two-brain-boundary.md)

## Development origin

This system was inspired by Jay's YouTube walkthrough of a Claude Code-maintained second brain that avoids Obsidian, vector databases, and heavy RAG infrastructure.

