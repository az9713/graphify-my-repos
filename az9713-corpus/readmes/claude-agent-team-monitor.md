# Agent Team Surveillance Dashboard

A real-time web dashboard that monitors Claude Code agent team activity - watch your agents collaborate, communicate, and complete tasks in real-time.

<video src="docs/demo.mp4" controls width="100%"></video>

---

## Quick Start (3 Commands)

```bash
# 1. Navigate to the server directory
cd surveil/server

# 2. Install dependencies (one-time setup)
npm install

# 3. Start the dashboard
node index.js
```

Then open your browser to: **http://localhost:3847**

That's it! The dashboard will automatically detect and display your active agent teams.

---

## What It Does

The surveillance dashboard provides real-time monitoring of Claude Code agent teams:

- **Agent Roster**: See all active agents with their roles, models, and status indicators
- **Live Message Stream**: Watch inter-agent communications in real-time (task assignments, status updates, shutdown requests)
- **Task Board**: Kanban-style view of pending, in-progress, and completed tasks with dependency tracking
- **Session History**: Review past agent team sessions stored in SQLite database
- **Auto-Reconnect**: Automatically reconnects if connection is lost, with visual status indicators

### Dashboard Features

#### Header
- **Status Indicator**: Green (connected) / Red (disconnected)
- **Team Badge**: Shows team name and member count
- **Team Selector**: Dropdown to switch between multiple active teams
- **Live/History Tabs**: Toggle between real-time monitoring and historical sessions
- **Live Clock**: Current time display

#### Agent Roster (Left Sidebar)
- **Colored Avatar Circles**: Each agent has a unique color with initials
- **Agent Details**: Name, type (coordinator/builder/etc.), and model information
- **Lead Badge**: Visual indicator for team leaders

#### Messages Panel (Center)
- **Reverse Chronological**: Most recent messages at top
- **Sender → Recipient**: Color-coded dots matching agent avatars
- **Type Badges**: Visual indicators for message types
  - `TASK_ASSIGNMENT` (blue)
  - `SHUTDOWN_REQUEST` (orange)
  - `IDLE_NOTIFICATION` (yellow)
  - `SHUTDOWN_APPROVED` (green)
  - `TEXT` (gray)
- **Structured Fields**: Renders message content with proper formatting
- **Expand/Collapse**: Long messages can be expanded for full viewing
- **Unread Counter**: Badge showing number of new messages

#### Task Board (Bottom)
- **3-Column Kanban**: Pending / In Progress / Completed
- **Task Cards**: Display task ID, subject, owner badge
- **Dependency Badges**: Shows "blocks" and "blocked-by" relationships
- **Active Form Indicator**: Spinner for tasks currently being worked on
- **Smart Filtering**: Hides internal and deleted tasks

#### History Tab
- **Session List**: All past agent team sessions from database
- **Click to Load**: View full session with roster, messages, and tasks
- **Persistent Storage**: Sessions survive server restarts

#### Connection Management
- **Auto-Reconnect**: Attempts reconnection every 5 seconds
- **Visual Banner**: Warning displayed when disconnected from server

---

## Architecture Overview

```
┌─────────────────────────────────────────────────────────────┐
│                       Browser Dashboard                      │
│  (HTML/CSS/JavaScript - displays agents, messages, tasks)   │
└────────────────────────┬────────────────────────────────────┘
                         │ WebSocket (real-time bidirectional)
                         │ HTTP (serves dashboard.html)
┌────────────────────────┴────────────────────────────────────┐
│                      Express Server                          │
│  - HTTP endpoints (serve dashboard, REST API)                │
│  - WebSocket handler (broadcast updates to clients)          │
└─┬────────────────┬────────────────┬────────────────────────┬┘
  │                │                │                        │
  │                │                │                        │
┌─┴──────────┐ ┌──┴──────────┐ ┌──┴──────────┐  ┌──────────┴──────┐
│FileWatcher │ │DataAggregator│ │SQLiteStore │  │WebSocketHandler │
│            │ │              │ │            │  │                 │
│ chokidar   │ │ JSON parser  │ │ Session DB │  │ Connection mgmt │
│ watches    │ │ unifies state│ │ (WAL mode) │  │ + heartbeat     │
└─┬──────────┘ └──────────────┘ └────────────┘  └─────────────────┘
  │
  │ watches filesystem
  │
┌─┴─────────────────────────────────────────────────────────────┐
│               ~/.claude/ directories                          │
│  - teams/ (team config JSON files)                            │
│  - tasks/ (task state JSON files)                             │
└───────────────────────────────────────────────────────────────┘
```

### How It Works

1. **FileWatcher** uses `chokidar` to monitor `~/.claude/teams/` and `~/.claude/tasks/` directories
2. When files change, **FileWatcher** emits typed events (`team-config-changed`, `inbox-changed`, `task-changed`)
3. **DataAggregator** parses JSON files and builds unified in-memory state
4. **SQLiteStore** persists session history for later review
5. **WebSocketHandler** broadcasts state updates to all connected browser clients
6. **Express** serves the dashboard HTML and provides REST API endpoints
7. **Browser** connects via WebSocket, receives updates, and renders the dashboard in real-time

---

## Technology Stack (Explained for C/C++/Java Developers)

If you're coming from C, C++, or Java, here's how the technologies map to concepts you already know:

| Technology | What It Is | Analogy |
|------------|-----------|---------|
| **Node.js** | JavaScript runtime for server-side code | Like the JVM for Java, or a C++ executable - runs your application |
| **npm** | Package manager for Node.js | Like Maven for Java, or pip for Python - downloads and manages dependencies |
| **Express** | HTTP server framework | Like Spring Boot (Java) or Flask (Python) - handles HTTP requests/responses |
| **WebSocket (ws)** | Full-duplex communication protocol | Like TCP sockets in C/C++, but designed for browsers - bidirectional, persistent connection |
| **chokidar** | File system watcher | Like inotify on Linux or FileSystemWatcher in .NET - detects file changes |
| **better-sqlite3** | SQLite database driver | Like JDBC for Java, or sqlite3 library for C - provides database connectivity |
| **SQLite** | Embedded SQL database | Like H2 for Java or Berkeley DB for C++ - no server needed, just a file |

### Node.js Concepts

#### What is Node.js?
Node.js is a runtime that lets you run JavaScript outside the browser. Just like you compile C++ code into an executable, or run Java bytecode in the JVM, Node.js executes JavaScript code.

```javascript
// JavaScript (similar to Java/C++)
const message = "Hello World";  // const = final in Java
console.log(message);           // System.out.println() in Java
```

#### What is npm?
`npm` (Node Package Manager) is like Maven or Gradle for Java. It:
- Downloads third-party libraries (dependencies)
- Manages version compatibility
- Runs build scripts

The `package.json` file is like `pom.xml` (Maven) or `build.gradle` - it lists dependencies and project metadata.

#### What are Node.js modules?
Node.js uses a module system similar to Java packages or C++ header files:

```javascript
// Importing (like #include or import)
const express = require('express');  // CommonJS style (older)
import express from 'express';       // ES6 style (newer)

// Exporting (like public class or header declarations)
module.exports = { myFunction };     // CommonJS
export { myFunction };               // ES6
```

---

## Configuration

The dashboard can be configured using environment variables:

| Variable | Default | Description |
|----------|---------|-------------|
| `SURVEIL_PORT` | `3847` | HTTP server port |
| `SURVEIL_TEAMS_DIR` | `~/.claude/teams/` | Directory containing team config JSON files |
| `SURVEIL_TASKS_DIR` | `~/.claude/tasks/` | Directory containing task state JSON files |

### Setting Environment Variables

**Windows (Command Prompt):**
```cmd
set SURVEIL_PORT=8080
node index.js
```

**Windows (PowerShell):**
```powershell
$env:SURVEIL_PORT=8080
node index.js
```

**macOS/Linux (Bash):**
```bash
export SURVEIL_PORT=8080
node index.js

# Or inline:
SURVEIL_PORT=8080 node index.js
```

---

## Directory Structure

```
surveil/
├── README.md              # This file
├── SKILL.md              # Claude Code skill definition
├── server/               # Node.js backend server
│   ├── package.json      # Dependencies and npm scripts
│   ├── index.js          # Main entry point (200 lines)
│   ├── lib/              # Core server modules
│   │   ├── file-watcher.js      # chokidar directory watcher (430 lines)
│   │   ├── data-aggregator.js   # JSON parser + state builder (170 lines)
│   │   ├── sqlite-store.js      # Session history persistence (350 lines)
│   │   └── websocket-handler.js # WebSocket connection manager (325 lines)
│   ├── public/           # Frontend assets
│   │   └── dashboard.html       # Complete single-file dashboard (1838 lines)
│   └── data/             # Runtime data (created automatically)
│       └── surveillance.db      # SQLite database (created at runtime)
└── docs/                 # Documentation assets
    └── agent_surveillance.jpg   # Screenshot
```

### Key Files Explained

#### `index.js` (Main Entry Point)
The application's "main method" - wires together all components:
- Creates Express HTTP server
- Initializes FileWatcher to monitor directories
- Sets up DataAggregator to parse JSON files
- Creates SQLiteStore for persistence
- Configures WebSocketHandler for real-time updates
- Defines HTTP routes and starts the server

#### `lib/file-watcher.js` (File System Monitor)
Uses `chokidar` to watch `~/.claude/` directories and emit events when files change:
- `team-config-changed` - Team roster or configuration updated
- `inbox-changed` - New inter-agent message
- `task-changed` - Task created, updated, or completed

#### `lib/data-aggregator.js` (State Builder)
Parses JSON files from watched directories and builds unified in-memory state:
- Reads team JSON files to build agent roster
- Reads inbox JSON files to extract messages
- Reads task JSON files to build task board
- Provides snapshot of current state for new WebSocket connections

#### `lib/sqlite-store.js` (Database Persistence)
Manages SQLite database for session history:
- WAL (Write-Ahead Logging) mode for better concurrency
- Stores complete session snapshots (roster, messages, tasks)
- Provides query methods for history tab

#### `lib/websocket-handler.js` (Real-Time Communication)
Manages WebSocket connections to browser clients:
- Handles connection lifecycle (connect, disconnect, error)
- Implements heartbeat/ping-pong to detect dead connections
- Broadcasts state updates to all connected clients
- Provides individual message sending

#### `public/dashboard.html` (Frontend Dashboard)
Complete single-file web application with inline CSS and JavaScript:
- Dark theme UI with responsive layout
- WebSocket client for real-time updates
- Agent roster rendering with color-coded avatars
- Message panel with type badges and expand/collapse
- Kanban task board with dependency visualization
- History browser for past sessions
- Auto-reconnect logic with status indicators

---

## Claude Code Skill Integration

This dashboard is designed to work seamlessly with Claude Code's agent team system.

### Skill Definition (`SKILL.md`)

The skill can be triggered with any of these phrases:
- "surveil my agents"
- "agent dashboard"
- "monitor agents"
- "agent surveillance"
- "launch dashboard"

When triggered, Claude Code will:
1. Check if dependencies are installed (`npm install` if needed)
2. Start the server with `node index.js`
3. Provide the URL to open in your browser

### Manual Launch

You can also run it manually without the skill:

```bash
cd surveil/server
node index.js
```

Or use the npm script defined in `package.json`:

```bash
cd surveil/server
npm start
```

---

## Development

Want to customize or extend the dashboard? Here's how to get started.

### Prerequisites

- **Node.js**: Version 18 or higher ([download here](https://nodejs.org/))
- **Text Editor**: VS Code, Sublime Text, or any editor you prefer

To check if Node.js is installed:
```bash
node --version  # Should print v18.x.x or higher
npm --version   # Should print 9.x.x or higher
```

### Installing Dependencies

The first time you work with the project (or after pulling updates), install dependencies:

```bash
cd surveil/server
npm install
```

This reads `package.json` and downloads all required libraries to `node_modules/` directory.

**Note**: The `node_modules/` directory contains ~50MB of code and is NOT committed to version control (listed in `.gitignore`). Every developer must run `npm install` to get dependencies.

### Running in Development Mode

```bash
cd surveil/server
node index.js
```

The server will print:
```
Agent Surveillance Dashboard started
HTTP server: http://localhost:3847
Watching: /home/user/.claude/teams
Watching: /home/user/.claude/tasks
```

Press `Ctrl+C` to stop the server.

### Project Structure for Development

```
server/
├── index.js                 # START HERE - main entry point
├── lib/
│   ├── file-watcher.js     # Modify to watch additional directories
│   ├── data-aggregator.js  # Modify to parse additional JSON fields
│   ├── sqlite-store.js     # Modify to add database tables/queries
│   └── websocket-handler.js # Modify to add WebSocket message types
└── public/
    └── dashboard.html      # Modify to change UI layout/styling
```

### Making Changes

#### 1. Changing the UI (dashboard.html)

The dashboard is a single HTML file with embedded CSS and JavaScript. To modify:

1. Open `server/public/dashboard.html` in your editor
2. Find the section you want to change:
   - **CSS styles**: Inside `<style>` tag (lines 10-400 approx.)
   - **HTML structure**: Inside `<body>` tag (lines 400-600 approx.)
   - **JavaScript logic**: Inside `<script>` tag (lines 600-1838 approx.)
3. Make your changes
4. Restart the server (`Ctrl+C`, then `node index.js`)
5. Refresh your browser (`Ctrl+R` or `F5`)

**Example**: Change the theme color from purple to blue:

```css
/* Find this in the <style> section: */
:root {
  --accent: #9333ea;  /* Purple */
}

/* Change to: */
:root {
  --accent: #2563eb;  /* Blue */
}
```

#### 2. Adding a New File Watcher Event

Want to watch additional files? Modify `lib/file-watcher.js`:

```javascript
// In the _handleChange method, add a new case:
if (filePath.includes('new-directory')) {
  this.emit('new-event-type', { filePath, data: jsonData });
}
```

Then handle the event in `index.js`:

```javascript
fileWatcher.on('new-event-type', (payload) => {
  console.log('New event detected:', payload);
  // Process and broadcast to clients
});
```

#### 3. Adding a New Database Table

Want to store additional data? Modify `lib/sqlite-store.js`:

```javascript
// In the _initDatabase method:
this.db.exec(`
  CREATE TABLE IF NOT EXISTS my_new_table (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    timestamp INTEGER NOT NULL
  )
`);
```

Then add query methods:

```javascript
insertRecord(name) {
  const stmt = this.db.prepare(`
    INSERT INTO my_new_table (name, timestamp) VALUES (?, ?)
  `);
  stmt.run(name, Date.now());
}

getAllRecords() {
  return this.db.prepare('SELECT * FROM my_new_table').all();
}
```

#### 4. Adding a New WebSocket Message Type

Want to send custom data to the dashboard? Modify `lib/websocket-handler.js`:

```javascript
// Add a new broadcast method:
broadcastCustomData(data) {
  this.broadcast({
    type: 'custom-data',
    payload: data
  });
}
```

Then handle it in `dashboard.html`:

```javascript
// In the WebSocket message handler:
ws.onmessage = (event) => {
  const message = JSON.parse(event.data);

  if (message.type === 'custom-data') {
    console.log('Custom data received:', message.payload);
    // Update UI accordingly
  }
};
```

### Testing Changes

After making changes:

1. **Restart the server**: `Ctrl+C`, then `node index.js`
2. **Refresh the browser**: `Ctrl+R` or `F5`
3. **Check browser console**: Press `F12`, go to "Console" tab for errors
4. **Check server logs**: Look at terminal output for error messages

### Common Development Tasks

#### Add a new HTTP endpoint:
```javascript
// In index.js, add:
app.get('/api/my-endpoint', (req, res) => {
  res.json({ message: 'Hello from new endpoint' });
});
```

#### Add a new configuration option:
```javascript
// In index.js, add:
const myOption = process.env.SURVEIL_MY_OPTION || 'default-value';
console.log('My option:', myOption);
```

#### Log debugging information:
```javascript
// Add anywhere in your code:
console.log('Debug info:', variableName);
console.error('Error occurred:', error);
console.warn('Warning:', message);
```

---

## Troubleshooting

### Problem: "node: command not found"

**Cause**: Node.js is not installed or not in your system PATH.

**Solution**:
1. Download Node.js from https://nodejs.org/ (LTS version recommended)
2. Run the installer with default options
3. **Close and reopen your terminal** (important!)
4. Verify: `node --version` should print the version number

**Windows Note**: The installer should add Node.js to PATH automatically. If not, add `C:\Program Files\nodejs\` to your PATH environment variable.

---

### Problem: "npm: command not found"

**Cause**: npm is not installed (usually comes with Node.js).

**Solution**:
1. Reinstall Node.js (npm is bundled with it)
2. Verify: `npm --version`

---

### Problem: Port 3847 is already in use

**Error Message**:
```
Error: listen EADDRINUSE: address already in use :::3847
```

**Cause**: Another process is using port 3847, or you have a zombie server process running.

**Solution 1 - Kill the existing process**:

**Windows:**
```cmd
netstat -ano | findstr :3847
taskkill /PID <PID> /F
```

**macOS/Linux:**
```bash
lsof -i :3847
kill -9 <PID>
```

**Solution 2 - Use a different port**:
```bash
SURVEIL_PORT=8080 node index.js
```

---

### Problem: "npm install" fails

**Error Message**: Various errors during `npm install`

**Common Causes**:
1. **Network issues**: npm cannot reach package registry
2. **Permission issues**: Cannot write to node_modules directory
3. **Corrupted cache**: npm cache is corrupted

**Solution**:

**Step 1 - Clear npm cache**:
```bash
npm cache clean --force
```

**Step 2 - Delete existing node_modules and try again**:
```bash
rm -rf node_modules package-lock.json  # macOS/Linux
# OR
rmdir /s node_modules & del package-lock.json  # Windows

npm install
```
