# Nested Claude Code (Supervibes) — Windows Edition

> **This project is a clone of the original [Supervibes](https://github.com/Ejae-dev/supervibes) repository, adapted and extended for Windows environments (Git Bash / MSYS2 / tmux).**

https://github.com/user-attachments/assets/5d064330-2b83-4418-8bc6-10dfb6b6fda1

**Run multiple Claude Code AI instances in parallel, orchestrated by a controller that acts as a tech lead.**

Nested Claude Code takes a development goal and automatically decomposes it into focused sub-tasks. Each sub-task is assigned to an independent Claude Code instance running in its own terminal. All instances work simultaneously — like a team of developers — while a controller instance monitors progress, verifies results, and coordinates the work.

```
                          +----------------------------------+
                          |        YOU (the human)           |
                          +----------------+-----------------+
                                           |
                                    type a goal
                                           |
                                           v
                          +----------------------------------+
                          |     Web Dashboard (:3456)        |
                          |     or CLI (start.cjs)           |
                          +----------------+-----------------+
                                           |
                                   POST /api/start
                                           |
                                           v
                          +----------------------------------+
                          |   Controller (Claude Code)       |
                          |   "I'm the tech lead.            |
                          |    I delegate, I don't code."    |
                          +----+-------+-------+-------+----+
                               |       |       |       |
                               v       v       v       v
                          +------+ +------+ +------+ +------+
                          |  ui  | | api  | |  db  | |tests |
                          |Claude| |Claude| |Claude| |Claude|
                          | Code | | Code | | Code | | Code |
                          +------+ +------+ +------+ +------+
                          (each in its own tmux terminal window)
```

## Table of Contents

- [Requirements](#requirements)
- [Quick Start](#quick-start)
- [How It Works](#how-it-works)
- [Project Structure](#project-structure)
- [Documentation](#documentation)
- [Limitations](#limitations)
- [Troubleshooting](#troubleshooting)
- [License](#license)

## Requirements

### macOS

| Requirement | Why It's Needed | How to Install |
|-------------|----------------|----------------|
| **macOS** | Uses Terminal.app + AppleScript for window management | (your OS) |
| **Node.js** (v18+) | Runs the server and all scripts | `brew install node` |
| **tmux** | Terminal multiplexer for managing sessions | `brew install tmux` |
| **Claude Code CLI** | The AI coding assistant that does the actual work | [Install guide](https://docs.anthropic.com/en/docs/claude-code) |

### Windows (Git Bash or MSYS2)

| Requirement | Why It's Needed | How to Install |
|-------------|----------------|----------------|
| **Git Bash** or **MSYS2** | Provides bash shell + tmux on Windows | [Git for Windows](https://gitforwindows.org/) or [MSYS2](https://www.msys2.org/) |
| **Node.js** (v18+) | Runs the server and all scripts | `winget install OpenJS.NodeJS` or [nodejs.org](https://nodejs.org/) |
| **tmux** | Terminal multiplexer for managing sessions | Comes with MSYS2; for Git Bash: `pacman -S tmux` (see [Windows Setup](#windows-setup)) |
| **Claude Code CLI** | The AI coding assistant that does the actual work | [Install guide](https://docs.anthropic.com/en/docs/claude-code) |

**No npm install needed.** This project uses zero external dependencies — only Node.js built-in modules.

## Quick Start

### macOS Quick Start

```bash
# 1. Clone the repository
git clone <repo-url>
cd supervibes

# 2. Start the server
node server.cjs

# 3. Open in browser
# Navigate to http://localhost:3456
```

You'll see a dark-themed dashboard with:
- A **goal input field** at the top
- Dropdowns for **terminal count**, **model**, and **iterations**
- An **activity log** (left panel) and **terminals sidebar** (right panel)

**To run your first task:**
1. Type: `Build a simple counter app with vanilla HTML, CSS, and JavaScript`
2. Leave Terminal Count on "Auto"
3. Leave Model on "Sonnet"
4. Leave Iterations at "0"
5. Click **Start**

Watch as Terminal windows pop up on your screen and Claude Code instances begin working in parallel.

### Windows Quick Start (Git Bash)

```bash
# 1. Open Git Bash (NOT PowerShell, NOT cmd.exe)
# Right-click desktop -> "Git Bash Here", or launch from Start menu

# 2. Clone and enter the directory
git clone <repo-url>
cd supervibes

# 3. Apply the Windows compatibility patch (required, one-time)
#    See "Windows Setup" section below for details, or run:
node windows-setup.cjs

# 4. Start the server
node server.cjs

# 5. Open http://localhost:3456 in your browser
```

**Important for Windows users:** The tmux child terminals will NOT open as visible windows automatically (that feature uses macOS-only AppleScript). Instead, the sessions run in the background. You can manually attach to any session from a separate Git Bash window using `tmux attach -t cc-<name>`. See [Windows Setup](#windows-setup) for the full details.

### CLI Mode (All Platforms)

```bash
node start.cjs
```

Follow the interactive prompts to enter your goal and terminal count.

---

## Windows Setup

This project was originally built for macOS. On Windows, it works with modifications. This section walks you through everything step-by-step.

### What Works on Windows

| Feature | Status | Notes |
|---------|--------|-------|
| Dashboard (server.cjs) | Works | HTTP server + SSE streaming work identically |
| Controller spawning | Works | `claude -p` runs fine on Windows |
| tmux sessions | Works | Create, send-keys, capture-pane, kill all work |
| Terminal auto-open | Does NOT work | Uses macOS AppleScript — see workaround below |
| Window auto-arrange | Does NOT work | Uses macOS AppleScript — cosmetic only |
| `--list` command | Needs fix | tmux format strings break under cmd.exe — patch required |

### Step 1: Install Prerequisites

#### Option A: Git Bash (Easiest)

If you already have **Git for Windows** installed, you have Git Bash. But you need tmux too.

1. **Install Git for Windows** (if not already): https://gitforwindows.org/
2. **Install MSYS2** for tmux: https://www.msys2.org/
   - Download and run the installer
   - Open "MSYS2 UCRT64" from Start menu
   - Run: `pacman -S tmux`
3. **Add MSYS2 to Git Bash's PATH**: Add this line to your `~/.bashrc` in Git Bash:
   ```bash
   export PATH="/c/msys64/usr/bin:$PATH"
   ```
   Then restart Git Bash. Verify: `tmux -V`

#### Option B: MSYS2 (Most Complete)

MSYS2 comes with bash, tmux, and a package manager. This is the most reliable approach.

1. **Install MSYS2**: https://www.msys2.org/
2. **Open MSYS2 UCRT64** terminal
3. **Install tmux**: `pacman -S tmux`
4. **Ensure Node.js is on PATH**: If you installed Node.js via the Windows installer, it should already be accessible. Verify: `node --version`
5. **Ensure Claude Code is on PATH**: Verify: `claude --version`

#### Option C: Windows PowerShell

PowerShell **cannot run tmux directly**. However, you can use it alongside Git Bash:

1. Install Node.js and Claude Code CLI as normal
2. Install Git Bash or MSYS2 for tmux (see above)
3. **Run the server from PowerShell** (this part works):
   ```powershell
   cd C:\path\to\supervibes
   node server.cjs
   ```
4. The server will spawn the controller, but tmux commands will only work if `tmux` is on your system PATH (i.e., MSYS2's `/usr/bin` is in PATH)
5. **Recommended**: Just use Git Bash for everything — it's simpler

### Step 2: Apply the Windows Compatibility Patch

The `tmux-control.cjs` file has two Windows issues that need fixing:

**Issue 1: `tmux list-sessions` quoting**
Node.js on Windows uses `cmd.exe` as its default shell. The tmux format string `'#{session_name}'` uses single quotes and `#{}` syntax that `cmd.exe` cannot handle.

**Issue 2: AppleScript calls**
Functions `openTerminalWindow()` and `rearrangeWindows()` call `osascript` which doesn't exist on Windows.

**The fix** — edit `tmux-control.cjs` and make these two changes:

**Change 1:** In the `listSessions()` function (around line 36), change:

```javascript
// BEFORE (macOS):
const raw = run("tmux list-sessions -F '#{session_name}' 2>/dev/null");

// AFTER (cross-platform):
const raw = run(
  process.platform === "win32"
    ? 'bash -c "tmux list-sessions -F \'#{session_name}\' 2>/dev/null"'
    : "tmux list-sessions -F '#{session_name}' 2>/dev/null"
);
```

**Change 2:** In the `openTerminalWindow()` function (around line 117) and `rearrangeWindows()` function (around line 133), add a platform guard:

```javascript
function openTerminalWindow(sess) {
  if (process.platform === "win32") {
    // On Windows, tmux sessions run in the background.
    // Users can attach manually: tmux attach -t <session-name>
    console.log(`[Windows] Session '${sess}' running in background. Attach with: tmux attach -t ${sess}`);
    return;
  }
  // ... existing AppleScript code ...
}

function rearrangeWindows() {
  if (process.platform === "win32") return; // No-op on Windows
  // ... existing AppleScript code ...
}
```

### Step 3: Verify the Setup

Open **Git Bash** (not PowerShell, not cmd.exe) and run:

```bash
# Check all prerequisites
node --version          # Should show v18+
tmux -V                 # Should show tmux 3.x+
claude --version        # Should show Claude Code version

# Test tmux works
tmux new-session -d -s test-session
tmux send-keys -t test-session -l 'echo hello'
tmux send-keys -t test-session Enter
sleep 1
tmux capture-pane -t test-session -p -S -5   # Should show "hello"
tmux kill-session -t test-session

# Start the server
cd /path/to/supervibes
node server.cjs
# Should show: Dashboard: http://localhost:3456
```

### Step 4: Working with Invisible Terminals (Windows)

On macOS, each tmux session opens a visible Terminal.app window. On Windows, sessions run in the background. Here's how to observe them:

**To see all active sessions:**
```bash
tmux list-sessions
```

**To watch a child Claude Code working in real-time:**
```bash
# Open a new Git Bash window and run:
tmux attach -t cc-ui       # Replace "ui" with the terminal name
# Press Ctrl+B then D to detach without killing it
```

**To watch multiple sessions** — open separate Git Bash windows and attach to different sessions:
```
Git Bash Window 1:  tmux attach -t cc-ui
Git Bash Window 2:  tmux attach -t cc-api
Git Bash Window 3:  tmux attach -t cc-tests
```

**The dashboard still works perfectly** — you can monitor all activity from the web UI at `http://localhost:3456` regardless of whether terminal windows are visible.

### Windows + PowerShell Specifics

If you prefer to run the server from PowerShell:

```powershell
# Navigate to the project
cd C:\Users\YourName\path\to\supervibes

# Start the server (this works from PowerShell)
node server.cjs

# The server spawns tmux through Node's child_process.
# tmux must be on your system PATH for this to work.
# Add MSYS2 to PATH in PowerShell:
$env:PATH = "C:\msys64\usr\bin;$env:PATH"
node server.cjs
```

**Note:** The controller process (Claude Code in prompt mode) will use whatever shell Node.js resolves. On Windows this is `cmd.exe`. The controller then runs `node tmux-control.cjs` commands — which themselves call `tmux` via `execSync`. As long as `tmux` is on the system PATH, this chain works.

### Known Windows Limitations

| Limitation | Impact | Workaround |
|-----------|--------|------------|
| No auto-opening terminal windows | You can't visually watch all terminals pop up | Use `tmux attach` from separate Git Bash windows, or just use the dashboard |
| No window grid arrangement | Terminal windows aren't auto-positioned | Arrange them manually, or rely on the dashboard |
| `2>/dev/null` in cmd.exe | Some error suppression fails, producing harmless stderr messages | Ignore "The system cannot find the path specified" messages — they're cosmetic |
| Path format differences | MSYS2 translates `/c/Users/...` automatically | Use Git Bash; avoid raw Windows paths like `C:\` in tmux commands |

---

## How It Works

1. **You enter a goal** (e.g., "Build a weather app with React")
2. **A controller Claude Code instance starts** — it receives a system prompt telling it to act as a tech lead who delegates work
3. **The controller decomposes the goal** into 3-6 parallel sub-tasks
4. **Each sub-task gets its own terminal** — a tmux session with a dedicated Claude Code instance
5. **All instances work simultaneously** — each owns specific files/directories to avoid conflicts
6. **The controller monitors progress** by reading terminal output every few seconds
7. **Once complete, the controller verifies** the project works (runs it, checks for errors)
8. **Optional iteration rounds** review, improve, and add features to the initial build

## Project Structure

```
supervibes/
+-- server.cjs            Main HTTP server: API routes, SSE streaming,
|                         controller process management (556 lines)
+-- tmux-control.cjs      tmux session manager: start/stop sessions,
|                         send commands, read output, window layout (293 lines)
+-- start.cjs             CLI launcher: terminal-based alternative to
|                         the web dashboard (198 lines)
+-- windows-setup.cjs     One-time Windows patch script: fixes tmux quoting
|                         and disables AppleScript calls (118 lines)
+-- public/
|   +-- index.html        Web dashboard: single-file app with embedded
|                         CSS and JavaScript (714 lines)
+-- docs/
|   +-- ARCHITECTURE.md   System architecture with diagrams
|   +-- DEVELOPER_GUIDE.md  Step-by-step guide for developers
|   +-- USER_GUIDE.md     User guide with 10+ example use cases
|   +-- STUDY_PLAN.md     Zero-to-hero learning plan
+-- system.md             Technical explanation of the nesting mechanism
+-- system_explainer.md   Simplified walkthrough for non-technical readers
+-- tmux.md               Deep tmux reference (originally for Twitch streaming)
+-- CLAUDE.md             Project context for Claude Code
+-- README.md             This file
```

## Documentation

| Document | Audience | Purpose |
|----------|----------|---------|
| [Architecture Guide](docs/ARCHITECTURE.md) | Developers | System design, component diagrams, data flows |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | New developers | Step-by-step setup, codebase walkthrough, extending the system |
| [User Guide](docs/USER_GUIDE.md) | End users | How to use the dashboard, 10+ example use cases |
| [Study Plan](docs/STUDY_PLAN.md) | Learners | Zero-to-hero learning path using this repo |
| [CLAUDE.md](CLAUDE.md) | Claude Code | Project context for AI assistance |

## Limitations

- **macOS has full support** — Terminal.app windows auto-open and auto-arrange via AppleScript
- **Windows has partial support** — core functionality works via Git Bash/MSYS2 + tmux, but terminal windows don't auto-open (see [Windows Setup](#windows-setup))
- **No Linux support yet** — would need a terminal emulator launcher (e.g., `gnome-terminal`, `xterm`)
- **Controller quality varies** — sometimes the AI under-parallelizes or sends overly broad prompts
- **No structured communication** — the controller talks to children by typing into terminals and reading screen output via tmux; there is no API or message-passing between instances
- **No persistence** — all state is in-memory; restarting the server loses history
- **No authentication** — the dashboard is open on localhost; intended for local development only

## Troubleshooting

### All Platforms

| Problem | Cause | Fix |
|---------|-------|-----|
| "Cannot launch inside another Claude Code" | `CLAUDECODE` env var not unset | This should be automatic; check `tmux-control.cjs` |
| No colors in terminal | TERM set to `tmux-256color` | System sets `TERM=xterm-256color` automatically |
| Ghost text eats commands | Claude Code autocomplete | System sends blank Enter after each command |
| `claude` command not found | Not on PATH | Ensure Claude Code CLI is installed and on your PATH |
| Port 3456 already in use | Another process | Kill the other process or change `PORT` in server.cjs |

### macOS Only

| Problem | Cause | Fix |
|---------|-------|-----|
| Terminal windows don't appear | AppleScript blocked | Check System Preferences > Privacy > Automation |
| `tmux` command not found | Not installed | Run `brew install tmux` |

### Windows Only

| Problem | Cause | Fix |
|---------|-------|-----|
| "The system cannot find the path specified" | `2>/dev/null` fails in cmd.exe | Harmless cosmetic error — ignore it, or apply the Windows patch |
| `tmux` command not found | MSYS2 not installed or not on PATH | Install MSYS2, run `pacman -S tmux`, add `/c/msys64/usr/bin` to PATH |
| `--list` shows "No active sessions" when sessions exist | Single-quote quoting breaks in cmd.exe | Apply the Windows compatibility patch (see [Windows Setup](#windows-setup)) |
| `'osascript' is not recognized` | AppleScript doesn't exist on Windows | Apply the Windows compatibility patch — this error is expected and harmless |
| Terminal windows don't auto-open | AppleScript not available | Use `tmux attach -t cc-<name>` from Git Bash to view sessions |
| Server won't start from PowerShell | tmux not on PATH | Add MSYS2 to PATH: `$env:PATH = "C:\msys64\usr\bin;$env:PATH"` |
| Claude Code fails to spawn in tmux | Wrong shell environment | Make sure to run from Git Bash, not cmd.exe or PowerShell |

## License

MIT
