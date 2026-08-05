# Grok CLI Tutorial

A complete, clickable HTML tutorial for the **Grok Build** command-line interface: every major option and subcommand with **why** and **how**, shell-syntax decoding, and a linked `grok --help` executive summary.

## Live site (GitHub Pages)

**[Open the interactive tutorial →](https://az9713.github.io/grok-cli-tutorial/)**

The live page is fully clickable: use the sidebar, the executive-summary links, and in-page anchors.

## Preview

![Grok CLI Tutorial — homepage preview](preview.png)

## What’s inside

- **Executive summary** — `grok --help` surface with every option/command linked to detail sections
- **Options vs commands** — how `-p`/`--single` flags differ from utilities like `update` and `mcp`
- **Launch flags** — sessions, models, headless scripting, permissions, worktrees, UI modes
- **Subcommands** — `login`, `sessions`, `mcp`, `plugin`, `agent`, `doctor`, `update`, and more
- **Shell syntax decoded** — `$(…)`, pipes, `tr '[:upper:]' '[:lower:]'`, globs vs regex

## Files

| File | Purpose |
|------|---------|
| [`index.html`](index.html) | Site entry for GitHub Pages (same content as the tutorial) |
| [`grok-cli-tutorial.html`](grok-cli-tutorial.html) | Same tutorial (standalone filename) |
| [`preview.png`](preview.png) | Screenshot used in this README |

## View locally

Open `index.html` in any modern browser (double-click, or drag into Chrome/Edge/Firefox). No build step.

```bash
# optional local server
python -m http.server 8080
# then visit http://localhost:8080/
```

## Repo

- GitHub: [github.com/az9713/grok-cli-tutorial](https://github.com/az9713/grok-cli-tutorial)
- Pages: [az9713.github.io/grok-cli-tutorial](https://az9713.github.io/grok-cli-tutorial/)
