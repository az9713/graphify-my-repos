---
repo: agent-scripts-windows
description: Windows port of steipete/agent-scripts: 23 Claude Code agent skills re-tooled from macOS/symlinks/Ruby to Windows/junctions/Bun. Not the original - all skill content credit to Peter Steinberger.
language: JavaScript
stars: 0
forks: 0
created: 2026-08-02
updated: 2026-08-02
topics: 
is_fork: False
kb: 170
---

# agent-scripts-windows
# agent-scripts-windows

> Windows port of Peter Steinberger's [steipete/agent-scripts](https://github.com/steipete/agent-scripts): 23 agent skills for Claude Code, re-tooled from macOS/symlinks/Ruby to Windows/junctions/Bun.

This is **not the original project**. The original is
[steipete/agent-scripts](https://github.com/steipete/agent-scripts) — Peter
Steinberger's shared agent instructions, skills, and helpers for his macOS
machines. This repo is an independent Windows port of the portable subset,
produced by classifying all 67 upstream skills, porting the 23 that survive
off macOS, and rewriting the toolchain that couldn't run (Ruby validator →
Bun/TypeScript, bash+symlink installer → PowerShell junctions). All credit for
the skills' content and design belongs to Peter; the port introduced no new
skills, only Windows adaptations.

## What's inside

- `skills/` — 23 ported skills (GitHub review/triage, Codex delegation,
  markdown conversion, media download, image generation, Obsidian, Cloudflare,
  and more). Each is a `SKILL.md` Claude Code loads directly; deliberate
  divergences from upstream are marked inline with `(Windows port: ...)`.
- `scripts/install-skills.ps1` — junction-based installer into
  `~/.claude/skills` (no admin rights needed; `-DryRun` / `-Copy` flags).
- `scripts/validate-skills.ts` — skill front-matter linter for Bun.
- `hooks/pre-commit` — runs the validator on commit
  (`git config core.hooksPath hooks`).
- `docs/` — upstream playbooks, kept as reference reading.
- [PORT-MANIFEST.md](PORT-MANIFEST.md) — full inventory: every upstream entry's
  fate, per-skill patches and prerequisites, runbook.
- [TESTING-REPORT.md](TESTING-REPORT.md) / [TEST-EVIDENCE.md](TEST-EVIDENCE.md) —
  every component tested on a real Windows machine; issues found and fixed.
- [DEVELOPMENT-JOURNEY.md](DEVELOPMENT-JOURNEY.md) — the porting story: the
  seven macOS/Windows gaps, decisions, and how the port was executed.

## Quick start

```powershell
git clone https://github.com/az9713/agent-scripts-windows
cd agent-scripts-windows
powershell -File scripts\install-skills.ps1 -DryRun   # preview
powershell -File scripts\install-skills.ps1           # install
```

Restart Claude Code; the skills route automatically from your requests.
Junctions keep edits live — changing a `SKILL.md` here changes the installed
skill. Validate after edits:

```powershell
bun scripts/validate-skills.ts
```

Per-skill prerequisites (API keys, CLIs like `gh`, `yt-dlp`, `wrangler`) are
in the [runbook](PORT-MANIFEST.md#runbook).

## What was left behind, and why

30 upstream skills were skipped: 16 sit on macOS-only toolchains (Xcode,
Instruments, Sparkle, Parallels, AppleScript, Peekaboo), 14 are bound to the
original author's private infrastructure (Mac fleet, 1Password vault items,
private repos and databases). 14 more arrived as broken symlink pointers in a
zip download. The complete accounting is in
[PORT-MANIFEST.md](PORT-MANIFEST.md).

## License

MIT, inherited from the original — see [LICENSE](LICENSE).
