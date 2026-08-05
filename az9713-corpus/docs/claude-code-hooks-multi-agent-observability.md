---
repo: claude-code-hooks-multi-agent-observability
description: Real-time monitoring for Claude Code agents through simple hook event tracking.
language: TypeScript
stars: 0
forks: 0
created: 2025-11-14
updated: 2025-11-15
topics: 
is_fork: True
kb: 4406
---

# claude-code-hooks-multi-agent-observability
# Multi-Agent Observability System

Real-time monitoring and visualization for Claude Code agents through comprehensive hook event tracking. You can watch the [full breakdown here](https://youtu.be/9ijnN985O_c) and watch the latest enhancement where we compare Haiku 4.5 and Sonnet 4.5 [here](https://youtu.be/aA9KP7QIQvM).

## 🎯 Overview

This system provides complete observability into Claude Code agent behavior by capturing, storing, and visualizing Claude Code [Hook events](https://docs.anthropic.com/en/docs/claude-code/hooks) in real-time. It enables monitoring of multiple concurrent agents with session tracking, event filtering, and live updates. 

<img src="images/app.png" alt="Multi-Agent Observability Dashboard" style="max-width: 800px; width: 100%;">

## 🏗️ Architecture

```
Claude Agents → Hook Scripts → HTTP POST → Bun Server → SQLite → WebSocket → Vue Client
```

![Agent Data Flow Animation](images/AgentDataFlowV2.gif)

## 📋 Setup Requirements

Before getting started, ensure you have the following installed:

- **[Claude Code](https://docs.anthropic.com/en/docs/claude-code)** - Anthropic's official CLI for Claude
- **[Astral uv](https://docs.astral.sh/uv/)** - Fast Python package manager (required for hook scripts)
- **[Bun](https://bun.sh/)**, **npm**, or **yarn** - For running the server and client
- **Anthropic API Key** - Set as `ANTHROPIC_API_KEY` environment variable
- **OpenAI API Key** (optional) - For multi-model support with just-prompt MCP tool
- **ElevenLabs API Key** (optional) - For audio features

### Configure .claude Directory

To setup observability in your repo,we need to copy the .claude directory to your project root.

To integrate the observability hooks into your projects:

1. **Copy the entire `.claude` directory to your project root:**
   ```bash
   cp -R .claude /path/to/your/project/
   ```

2. **Update the `settings.json` configuration:**
   
   Open `.claude/settings.json` in your project and modify the `source-app` parameter to identify your project:
   
   ```json
   {
     "hooks": {
       "PreToolUse": [{
         "matcher": "",
         "hooks": [
           {
             "type": "command",
             "command": "uv run .claude/hooks/pre_tool_use.py"
           },
           {
             "type": "command",
             "command": "uv run .claude/hooks/send_event.py --source-app YOUR_PROJECT_NAME --event-type PreToolUse --summarize"
           }
         ]
       }],
       "PostToolUse": [{
         "matcher": "",
         "hooks": [
           {
             "type": "command",
             "command": "uv run .claude/hooks/post_tool_use.py"
           },
           {
             "type": "command",
             "command": "uv run .claude/hooks/send_event.py --source-app YOUR_PROJECT_NAME --event-type PostToolUse --summarize"
           }
         ]
       }],
       "UserPromptSubmit": [{
         "hooks": [
           {
             "type": "command",
             "command": "uv run .claude/hooks/user_prompt_submit.py --log-only"
           },
           {
             "type": "command",
             "command": "uv run .claude/hooks/send_event.py --source-app YOUR_PROJECT_NAME --event-type UserPromptSubmit --summarize"
           }
         ]
       }]
       // ... (similar patterns for Notification, Stop, SubagentStop, PreCompact, SessionStart, SessionEnd)
     }
   }
   ```
   
   Replace `YOUR_PROJECT_NAME` with a unique identifier for your project (e.g., `my-api-server`, `react-app`, etc.).

3. **Ensure the observability server is running:**
   ```bash
   # From the observability project directory (this codebase)
   ./scripts/start-system.sh
   ```

Now your project will send events to the observability system whenever Claude Code performs actions.

## 🚀 Quick Start

**New to this? Start with the [Complete Installation Guide](INSTALLATION.md)** - A step-by-step guide assuming zero prior experience!

**Already have prerequisites installed?** Use the quick start below:

```bash
# 1. Start both server and client
./scripts/start-system.sh

# 2. Open http://localhost:5173 in your browser

# 3. Open Claude Code and run the following command:
Run git ls-files to understand the codebase.

# 4. Watch events stream in the client

# 5. Copy the .claude folder to other projects you want to emit events from.
cp -R .claude <directory of your codebase you want to emit events from>
```

**Need detailed installation instructions?** See [INSTALLATION.md](INSTALLATION.md) for complete setup with zero assumptions.

## 📁 Project Structure

```
claude-code-hooks-multi-agent-observability/
│
├── apps/                    # Application components
│   ├── server/             # Bun TypeScript server
│   │   ├── src/
│   │   │   ├── index.ts    # Main server with HTTP/WebSocket endpoints
│   │   │   ├── db.ts       # SQLite database management & migrations
│   │   │   └── types.ts    # TypeScript interfaces
│   │   ├── package.json
│   │   └── events.db       # SQLite database (gitignored)
│   │
│   └── client/             # Vue 3 TypeScript client
│       ├── src/
│       │   ├── App.vue     # Main app with theme & WebSocket management
│       │   ├── components/
│       │   │   ├── EventTimeline.vue      # Event list with auto-scroll
│       │   │   ├── EventRow.vue           # Individual event display
│       │   │   ├── FilterPanel.vue        # Multi-select filters
│       │   │   ├── ChatTranscriptModal.vue # Chat history viewer
│       │   │   ├── StickScrollButton.vue  # Scroll control
│       │   │   └── LivePulseChart.vue     # Real-time activity chart
│       │   ├── composables/
│       │   │   ├── useWebSocket.ts        # WebSocket connection logic
│       │   │   ├── useEventColors.ts      # Color assignment system
│       │   │   ├── useChartData.ts        # Chart data aggregation
│       │   │   └── useEventEmojis.ts      # Event type emoji mapping
│       │   ├── utils/
│       │   │   └── chartRenderer.ts       # Canvas chart rendering
│       │   └── types.ts    # TypeScript interfaces
│       ├── .env.sample     # Environment configuration template
│       └── package.json
│
├── .claude/                # Claude Code integration
│   ├── hooks/             # Hook scripts (Python with uv)
│   │   ├── send_event.py  # Universal event sender
│   │   ├── pre_tool_use.py    # Tool validation & blocking
│   │   ├── post_tool_use.py   # Result logging
│   │   ├── notification.py    # User interaction events
│   │   ├── user_prompt_submit.py # User prompt logging & validation
│   │   ├── stop.py           # Session completion
│   │   └── subagent_stop.py  # Subagent completion
│   │
│   └── settings.json      # Hook configuration
│
├── scripts/               # Utility scripts
│   ├── start-system.sh   # Launch server & client
│   ├── reset-system.sh   # Stop all processes
│   └── test-system.sh    # System validation
│
└── logs/                 # Application logs (gitignored)
```

## 🔧 Component Details

### 1. Hook System (`.claude/hooks/`)

> If you want to master claude code hooks watch [this video](https://github.com/disler/claude-code-hooks-mastery)

The hook system intercepts Claude Code lifecycle events:

- **`send_event.py`**: Core script that sends event data to the observability server
  - Supports `--add-chat` flag for including conversation history
  - Validates server connectivity before sending
  - Handles all event types with proper error handling

- **Event-specific hooks**: Each implements validation and data extraction
  - `pre_tool_use.py`: Blocks dangerous commands, validates tool usage
  - `post_tool_use.py`: Captures execution results and outputs
  - `notification.py`: Tracks user interaction points
  - `user_prompt_submit.py`: Logs user prompts, supports validation (v1.0.54+)
  - `stop.py`: Records session completion with optional chat history
  - `subagent_stop.py`: Monitors subagent task completion
  - `pre_compact.py`: Tracks context compaction operations (manual/auto)
  - `session_start.py`: Logs session start, can load development context
  - `session_end.py`: Logs session end, saves session statistics

### 2. Server (`apps/server/`)

Bun-powered TypeScript server with real-time capabilities:

- **Database**: SQLite with WAL mode for concurrent access
- **Endpoints**:
  - `POST /events` - Receive events from agents
  - `GET /events/recent` - Paginated event retrieval with filtering
  - `GET /events/filter-options` - Available filter values
  - `WS /stream` - Real-time event broadcasting
- **Features**:
  - Automatic schema migrations
  - Event validation
  - WebSocket broadcast to all clients
  - Chat transcript storage

### 3. Client (`apps/client/`)

Vue 3 application with real-time visualization:

- **Visual Design**:
  - Dual-color system: App colors (left border) + Session colors (second border)
  - Gradient indicators for visual distinction
  - Dark/light theme support
  - Responsive layout with smooth animations

- **Features**:
  - Real-time WebSocket updates
  - Multi-criteria filtering (app, session, event type)
  - Live pulse chart with session-colored bars and event type indicators
  - Time range selection (1m, 3m, 5m) with appropriate data aggregation
  - Chat transcript viewer with syntax highlighting
  - Auto-scroll with manual override
  - Event limiting (configurable via `VITE_MAX_EVENTS_TO_DISPLAY`)

- **Live Pulse Chart**:
  - Canvas-based real-time visualization
  - Session-specific colors for each bar
  - Event type emojis displayed on bars
  - Smooth animations and glow effects
  - Responsive to filter changes

## 🔄 Data Flow

1. **Event Generation**: Claude Code executes an action (tool use, notification, etc.)
2. **Hook Activation**: Corresponding hook script runs based on `settings.json` configuration
3. **Data Collection**: Hook script gathers context (tool name, inputs, outputs, session ID)
4. **Transmission**: `send_event.py` sends JSON payload to server via HTTP POST
5. **Server Processing**:
   - Validates event structure
   - Stores in SQLite with timestamp
   - Broadcasts to WebSocket clients
6. **Client Update**: Vue app receives event and updates timeline in real-time

## ✨ Features

### Core Features

- **Real-Time Monitoring**: Watch AI agents work through WebSocket connections
- **Multi-Agent Support**: Monitor multiple concurrent agents across different projects
- **Event Filtering**: Filter by app, session, or event type
- **Live Pulse Chart**: Visualize agent activity with real-time charts
- **Chat Transcripts**: View full conversation history for each session
- **Theme System**: Customize the UI with built-in or custom themes

### 🆕 Priority 0 Features (NEW!)

#### 💰 Token Usage & Cost Tracking
Monitor and track the API costs of your AI agents in real-time:
- **Real-Time Cost Calculation**: Automatic token counting and cost estimation
- **Session Metrics**: Track tokens and costs per session
- **Model-Specific Pricing**: Accurate pricing for Sonnet, Opus, and Haiku models
- **Cost Dashboard**: Visual metrics showing total usage and costs
- **Budget Monitoring**: Keep track of API spending across all projects

**Dashboard View**: See total tokens used, estimated costs, and per-session breakdowns at a glance.

#### 🔧 Tool Success/Failure Analytics
Understand tool reliability and identify issues:
- **Success Rate Tracking**: Monitor which tools succeed or fail
- **Error Classification**: Automatic categorization of errors (permission, not found, timeout, etc.)
- **Tool Statistics**: See usage patterns and reliability metrics
- **Error Summary**: View most common errors across all tools
- **Reliability Dashboard**: Visual charts showing tool performance

**Analytics View**: Real-time success rates, failure patterns, and error summaries for all tools used by agents.

### 🆕 Priority 1 Features (NEW!)

#### ⭐ Session Bookmarking & Tagging
Organize and categorize your important sessions:
- **Bookmark Sessions**: Star sessions for quick access later
- **Custom Tags**: Add descriptive tags to categorize sessions (e.g., "debugging", "production", "successful")
- **Tag-Based Filtering**: Find sessions by tag across all projects
- **Session Notes**: Add notes to bookmarked sessions for context
- **Quick Access**: View all bookmarked sessions in dedicated dashboard

**Bookmarks View**: Star important sessions and add custom tags for easy organization and retrieval.

#### ⚡ Agent Performance Metrics
Analyze and optimize AI agent performance:
- **Response Time Tracking**: Monitor average time between agent actions
- **Tools-Per-Task Analysis**: Understand tool usage efficiency
- **Success Rate Monitoring**: Track overall agent effectiveness
- **Session Duration Metrics**: See how long agents take to complete tasks
- **Performance Dashboard**: Visual charts comparing sessions
- **Trend Analysis**: Identify patterns in agent performance over time

**Performance View**: Comprehensive metrics showing response times, success rates, and efficiency scores for all sessions.

#### 🔍 Event Pattern Detection & Insights
Automatically discover agent behavior patterns:
- **Workflow Detection**: Identify common tool sequences (read-before-edit, search-then-read)
- **Retry Pattern Analysis**: Detect when agents retry tools multiple times
- **Confidence Scoring**: Pattern reliability ratings (0-100%)
- **Pattern Trends**: See which patterns occur most frequently
- **Example Sequences**: View actual tool sequences that triggered patterns
- **Insights Dashboard**: Visual analysis of detected patterns across sessions

**Pattern Types**:
- **workflow**: Common work sequences (e.g., Read → Edit, Grep → Read)
- **retry**: Tool retry attempts (same tool 3+ times)
- **sequence**: Multi-step operation patterns

**Patterns View**: Visual diagrams showing detected patterns with occurrence counts and confidence scores.

### 🆕 Priority 2 Features (NEW!)

#### 🔔 Webhook/Alert System
Get real-time notifications when critical events occur:
- **Custom Webhooks**: Configure webhooks to trigger on specific events (e.g., errors, tool failures, Stop events)
- **Event Filtering**: Filter by tool names, error types, sessions, or source apps
- **Delivery Tracking**: Monitor webhook delivery success/failure rates
- **Retry Logic**: Automatic retry for failed deliveries
- **Slack/Discord Integration**: Send alerts to team channels
- **Secret Signing**: Secure webhook payloads with HMAC signatures
- **Enable/Disable**: Toggle webhooks on/off without deletion

**Use Cases**: Get Slack alerts on production errors, Discord notifications when expensive API calls occur, email alerts for session failures.

#### 📊 Session Export & Reports
Export complete session data for documentation and sharing:
- **Multiple Formats**: Export as JSON, Markdown, or HTML
- **Comprehensive Data**: Includes events, metrics, performance data, patterns, and analytics
- **Professional Reports**: Beautifully formatted HTML reports with charts
- **Markdown Documentation**: Human-readable session summaries
- **JSON for Analysis**: Raw data for custom processing and analysis
- **Selective Export**: Choose what data to include (chat, metrics, patterns, analytics)

**Use Cases**: Document successful workflows, share session reports with team, analyze patterns offline, create training materials.

#### 🔍 Session Comparison View
Compare multiple agent sessions side-by-side:
- **Multi-Session Analysis**: Compare 2+ sessions simultaneously
- **Performance Comparison**: See which session was more efficient
- **Cost Analysis**: Compare token usage and costs across sessions
- **Tool Usage Patterns**: Identify which session used tools more effectively
- **Pattern Differences**: Detect behavioral variances between sessions
- **Winner Detection**: Automatic identification of best-performing session
- **Save Comparisons**: Bookmark comparisons for future reference
- **Add Notes**: Annotate comparisons with insights and observations

**Use Cases**: Compare Sonnet vs Haiku performance, analyze before/after optimization, identify regression in agent behavior, A/B test prompting strategies.

### 🆕 Priority 3 Features (NEW!)

#### 🌳 Decision Tree Visualization
Visualize agent decision-making processes as interactive trees:
- **Node Types**: Prompts, tool uses, results, and completions
- **Edge Relationships**: Triggers, uses, produces, leads-to connections
- **Event Timeline**: Chronological flow of agent decisions
- **Interactive Exploration**: Click nodes to see event details
- **Tool Sequences**: Visualize complex multi-step workflows
- **D3.js Powered**: Professional, interactive tree diagrams
- **Metadata Access**: View tool inputs/outputs on nodes

**Node Types**:
- **prompt**: User prompt submissions
- **tool**: Tool execution steps
- **result**: Tool completion results
- **completion**: Final response completion

**Use Cases**: Debug complex agent workflows, understand decision paths, identify inefficient sequences, document agent behavior patterns.

#### 👥 Multi-Agent Collaboration Tracking
Track and visualize hierarchies of multi-agent systems:
- **Parent-Child Relationships**: Track when agents spawn subagents
- **Hierarchy Visualization**: See full agent trees with depth metrics
- **Task Delegation**: Record why and what tasks were delegated
- **Collaboration Metrics**: Measure efficiency of multi-agent workflows
- **Relationship Types**: Subagent, parallel, sequential collaboration modes
- **Depth Analysis**: Understand multi-level agent nesting
- **Task Descriptions**: Document what each subagent was tasked with
- **Timeline Tracking**: See when subagents started and completed

**Relationship Types**:
- **subagent**: Parent delegates subtask to child
- **parallel**: Multiple agents work simultaneously
- **sequential**: Agents execute in sequence

**Use Cases**: Monitor agent orchestration systems, optimize task delegation strategies, measure multi-agent efficiency, debug agent collaboration issues.

## 🎨 Event Types & Visualization

| Event Type       | Emoji | Purpose                | Color Coding  | Special Display                       |
| ---------------- | ----- | ---------------------- | ------------- | ------------------------------------- |
| PreToolUse       | 🔧     | Before tool execution  | Session-based | Tool name & details                   |
| PostToolUse      | ✅     | After tool completion  | Session-based | Tool name & results                   |
| Notification     | 🔔     | User interactions      | Session-based | Notification message                  |
| Stop             | 🛑     | Response completion    | Session-based | Summary & chat transcript             |
| SubagentStop     | 👥     | Subagent finished      | Session-based | Subagent details                      |
| PreCompact       | 📦     | Context compaction     | Session-based | Compaction details                    |
| UserPromptSubmit | 💬     | User prompt submission | Session-based | Prompt: _"user message"_ (italic)     |
| SessionStart     | 🚀     | Session started        | Session-based | Session source (startup/resume/clear) |
| SessionEnd       | 🏁     | Session ended          | Session-based | End reason (clear/logout/exit/other)  |

### UserPromptSubmit Event (v1.0.54+)

The `UserPromptSubmit` hook captures every user prompt before Claude processes it. In the UI:
- Displays as `Prompt: "user's message"` in italic text
- Shows the actual prompt content inline (truncated to 100 cha