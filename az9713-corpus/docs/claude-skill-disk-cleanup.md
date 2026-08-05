---
repo: claude-skill-disk-cleanup
description: Claude Code Skill for Windows disk cleanup with WizTree analysis. Three PowerShell scripts with dry-run/execute safety model.
language: PowerShell
stars: 0
forks: 0
created: 2026-02-07
updated: 2026-02-07
topics: 
is_fork: False
kb: 22
---

# claude-skill-disk-cleanup
# Windows Disk Cleanup -- Claude Code Skill

A [Claude Code Skill](https://docs.anthropic.com/en/docs/claude-code/skills) that reclaims tens of gigabytes from Windows developer machines. Built from a real cleanup session that freed **~255 GB** on a single drive.

## Disclaimer

The primary purpose of this project is to demonstrate how to **distill lessons and experience from an interactive Claude Code session into a reusable skill**. The cleanup scripts and workflow are real and were used successfully, but they delete files from your system. Review the scripts, run the dry-run mode first, and use them for disk cleanup at your own risk.

## How This Skill Was Learned

This skill was not written from a template. It was **extracted from a live, interactive disk-cleanup session** between a developer and Claude Code, then hardened through iterative audit.

### The session

1. The developer ran [WizTree](https://wiztree.com/) and shared screenshots showing **642.5 GB used** on a 930 GB drive.
2. Claude Code analyzed the screenshots, identified the top space consumers, and proposed a cleanup plan with estimated savings per category.
3. The developer approved the plan. Claude Code generated three PowerShell scripts on the fly, each with a **dry-run mode** so nothing was deleted without review.
4. Scripts were executed in rounds -- dry-run first, review output, then execute with user approval. Errors surfaced real Windows constraints (path length limits, locked files, encoding quirks) that were fixed in-session.
5. After cleanup, drive free space went from **288 GB to 543 GB** -- roughly **255 GB reclaimed**.

### From session to skill

The entire workflow -- the two-phase approach, the scripts, the safety checks, and every hard-won lesson -- was then distilled into a reusable Claude Code Skill so that future sessions on any Windows machine can follow the same proven process without re-discovering the pitfalls.

An automated cross-reference audit verified that every feature in the scripts is accurately documented in `SKILL.md`, and every lesson learned is captured.

## Features

### Two-Phase Safety Model

| Phase | What happens | Deletes files? |
|-------|-------------|----------------|
| **Discover** | Scripts run in dry-run mode. Sizes and categories are reported. | No |
| **Execute** | Scripts delete only what the user approved. | Yes |

Nothing is deleted without an explicit dry-run first and user approval in between.

### Three Bundled PowerShell Scripts

| Script | Purpose |
|--------|---------|
| `cleanup.ps1` | Cleans temp files, Docker, npm/uv caches, Chrome cache (multi-profile), Windows Update cache, thumbnail cache, Recycle Bin, Android SDK. Includes a Downloads analysis with top files, file types, and duplicate detection. |
| `clean_venvs.ps1` | Finds and removes Python virtual environments. Verifies each folder contains `pyvenv.cfg` before deletion. Supports Recycle Bin or permanent delete. |
| `downloads_report.ps1` | Read-only analysis of any directory: largest files, space by file type, potential duplicates, `.venv` summary. Outputs to terminal and a timestamped report file. |

All scripts use `$env:` variables -- no hardcoded personal paths. Every script accepts a `-Path` parameter to target any directory.

### Timestamp Preservation

Deleting a `.venv` inside a project folder normally updates the parent folder's `LastWriteTime` to today. This skill **saves and restores parent folder timestamps** around every deletion, so file explorers and WizTree continue to show accurate modification dates.

### Native CLI Fallback Strategy

Cache cleanup prefers native tools when available (`npm cache clean --force`, `uv cache clean`) for correctness, and falls back to direct `Remove-Item` if the CLI is not installed.

### Progress and Reporting

- Color-coded terminal output (red/yellow/white by size severity)
- Elapsed time and `X/Y` progress counters during slow NTFS deletions
- Running totals during measurement phases
- Drive C: free space shown before and after execution
- Timestamped report files with per-item status (DELETED, LOCKED, WOULD DELETE, EXECUTED)

### Lessons Learned (Built Into the Skill)

These were all discovered the hard way during the live session and are now encoded as rules:

- **PowerShell 5.1 defaults to ANSI encoding** without a BOM. Unicode characters (box-drawing, em-dashes) silently corrupt scripts. All generated scripts use ASCII only.
- **NTFS small-file deletion is extremely slow.** Tens of thousands of small files (uv cache, node_modules) can take 10-30+ minutes. The scripts warn users and show progress so it doesn't look like a hang.
- **Git Bash mangles `$_`** in PowerShell one-liners. Always invoke scripts with `-File`, never `-Command`.
- **Recycle Bin Shell API fails on paths longer than 260 characters** with "The system call level is not correct." The skill always offers permanent delete as a fallback.
- **Docker cleanup has a specific order**: prune first, then stop Docker Desktop, then remove the data folder.
- **`pyvenv.cfg` is the only reliable venv marker.** Folders named `venv` without this file are not Python virtual environments and must be skipped.

## Skill Structure

```
.claude/skills/windows-disk-cleanup/
    SKILL.md                        # Skill definition (loaded by Claude Code)
    scripts/
        cleanup.ps1                 # Main cleanup (8 categories)
        clean_venvs.ps1             # Python venv cleanup
        downloads_report.ps1        # Read-only directory analysis
```

## Usage

This skill is automatically activated when Claude Code detects keywords like "disk full", "low space", "WizTree", "cleanup", or "free up storage" in a conversation. It can also be invoked directly:

```
> Help me clean up my Windows C: drive
```

Claude Code will follow the Discover-then-Execute workflow, run the bundled scripts, and guide you through approving deletions before anything is removed.

## Acknowledgements

[WizTree](https://wiztree.com/) by Antibody Software makes this workflow possible. It scans an entire C: drive in seconds using the MFT, and its visual treemap gives Claude Code (via screenshots) an immediate picture of where disk space is going -- no manual exploration needed.

The safety check "pyvenv.cfg is the only reliable venv marker -- folders named venv without this file are not Python virtual environments and must be skipped" was suggested by GPT-5.2, which also reviewed the scripts generated by Claude Code.

## Requirements

- Windows 10/11
- PowerShell 5.1+ (pre-installed on Windows)
- [WizTree](https://wiztree.com/) (optional, for initial analysis via screenshots)
- Git Bash or any terminal that can invoke `powershell -ExecutionPolicy Bypass -File`
