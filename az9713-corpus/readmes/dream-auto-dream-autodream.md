# dream auto dream autodream

A full conversation log of reverse-engineering Claude Code's undocumented **Auto Dream** memory consolidation feature — extracted directly from the `claude.exe` binary.

## Background

This repository documents a conversation exploring the Auto Dream feature discovered by Ray (Amjad) in the video:

**"Anthropic Just Dropped Memory 2.0 for Claude Code"**
https://www.youtube.com/watch?v=OnQ4BGN8B-s

Ray noticed Claude Code randomly displaying "improved 6 memories", inspected the binary, and uncovered an unannounced feature that consolidates Claude's memory across sessions — analogous to REM sleep in humans.

## Contents

- [`autodream.md`](./autodream.md) — Full conversation in Markdown
- [`autodream.html`](./autodream.html) — Full conversation as a styled HTML page

## What's inside

The conversation covers:

1. Triggering the Auto Dream feature with the phrase `dream auto dream autodream`
2. A detailed explanation of how the 4-phase consolidation works
3. Inferring how Ray discovered the feature
4. A step-by-step replication guide for inspecting Claude Code's binary yourself
5. A reverse-engineering prompt — and its full execution — extracting verbatim source code from `claude.exe` including:
   - The exact system prompt injected during a dream session
   - The trigger gate logic (`minHours: 24`, `minSessions: 5`)
   - The lock file mechanism (`.consolidate-lock`)
   - Telemetry event names (`tengu_auto_dream_fired`, etc.)
   - The key finding: the phrase is **not keyword-detected** — any message triggers the check

## Credit

Feature discovered and documented by Ray in the video linked above.
Binary analysis performed in this conversation using Claude Code v2.1.81.
