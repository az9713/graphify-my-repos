---
repo: my-pi-setup-windows
description: Windows port of Ben Davis's pi coding-agent setup: three-backend subagents (pi/codex/claude), routing policy + empirical routing log, and the win32 spawn fixes that make it all work
language: HTML
stars: 0
forks: 0
created: 2026-07-28
updated: 2026-07-28
topics: 
is_fork: False
kb: 2857
---

# my-pi-setup-windows
# Pi Agent Config (Windows)

Windows port of [davis7dotsh/my-pi-setup](https://github.com/davis7dotsh/my-pi-setup): the `~/.pi/agent` configuration for the [pi coding agent](https://www.npmjs.com/package/@earendil-works/pi-coding-agent), with TypeScript extensions, skills, and themes. The upstream setup assumes POSIX; this fork keeps it working on Windows (Git Bash / cmd.exe / Node-on-win32), where process spawning, `.cmd` shims, and process-tree killing all behave differently.

Key pieces:

- `extensions/` — pi extensions (subagents, background-terminals, file-search, workflows, …). `extensions/subagents` is the largest: it lets the parent agent spawn headless child agents on three different backends.
- `skills/` — skill documents the agent loads on demand. `skills/subagents/SKILL.md` is the routing policy described below.
- `package.json` scripts: `npm run check` (tsc), `npm run format` / `format:check` (prettier), `npm test` (node test runner over `extensions/*/*.test.ts`).

## Subagent backends

`extensions/subagents` defines one `SubagentBackend` per runtime (`src/backends/`), all normalized to the same session/event shape:

| Backend  | How it runs                                                                                       |
| -------- | ------------------------------------------------------------------------------------------------- |
| `pi`     | In-process `createAgentSession()` via the pi SDK. Inherits the parent's model and thinking level. |
| `claude` | Claude Code via `@anthropic-ai/claude-agent-sdk` `query()` in streaming-input mode.               |
| `codex`  | `codex app-server --stdio` child process speaking JSON-RPC over stdio.                            |

### Routing

Routing is by task type (policy in `skills/subagents/SKILL.md`), not by whim:

- **`codex`** (`gpt-5.6-sol`, high effort): browser/computer use, long-running mechanical grunt work, independent research.
- **`claude`** (fable, high effort): planning and architecture, docs/copy/READMEs, code where beauty and maintainability matter.
- **`pi`** (inherit parent): small one-off edits, test execution, verification runs, menial tasks.

At most four subagents run concurrently. Every settled run is appended to `~/.pi/agent/routing-log.jsonl` so the choice can eventually be driven by observed outcomes instead of static policy (see below).

## Windows-specific fixes

- **Vendored `codex.exe` preferred over the `.cmd` shim** (`extensions/subagents/src/backends/codex.ts`, `vendoredCodexExe`). Node on Windows refuses to spawn `.cmd` shims without a shell (`EINVAL`, since CVE-2024-27980). When PATH resolution finds `codex.cmd`, the backend instead uses the real binary the npm package vendors next to it (`node_modules/@openai/codex/node_modules/@openai/codex-win32-x64/vendor/x86_64-pc-windows-msvc/bin/codex.exe`), falling back to the shim only if the exe is missing. Claude resolution similarly tries `claude.exe` before `claude.cmd`.
- **`windowsVerbatimArguments` for background terminals** (`extensions/background-terminals/src/manager.ts`). Commands run through `cmd.exe /c <command>`; Node's default argument re-quoting mangles quotes inside the command string, so on win32 the spawn passes arguments verbatim and lets cmd.exe parse them. (`detached` — the POSIX process-group trick — is also disabled on win32; codex uses `taskkill /pid <pid> /T` instead to kill the whole process tree, since there are no POSIX process groups to signal.)
- **Routing-log append during settle** (`extensions/subagents/src/manager.ts`, `logRouting` called from `settle()`). When a subagent run settles (done/failed/interrupted), one JSONL line — timestamp, backend, model, title, status, duration, tokens — is appended to `~/.pi/agent/routing-log.jsonl`. It runs fire-and-forget with dynamic `node:fs` imports and a swallowed catch, so logging can never delay or fail settlement; the file is gitignored. Its purpose is empirical routing: check the log for the backend with the better completion record when the static policy leaves you unsure.

## Recovering after a bad `pi` update

A `pi` update (or the agent itself) can clobber files in this directory. Because the working config is committed, recover by inspecting first and restoring only what actually broke — no blanket resets:

```sh
cd ~/.pi/agent
git status                    # what changed? (note: settings.json / models-store.json churn is normal)
git diff <file>               # is the change damage or legitimate drift?
git checkout -- <file>        # restore ONE damaged tracked file from HEAD
git restore --source=HEAD <file>   # same thing, newer syntax
```

Avoid `git checkout .` / `git reset --hard`: they also wipe legitimate local changes (theme, model store, settings) that haven't been committed yet. Restore file-by-file, then commit a fresh snapshot once things work again.

Untracked runtime state (`sessions/`, `auth.json`, `routing-log.jsonl`, `node_modules/`) is gitignored and never at risk from git commands above.
