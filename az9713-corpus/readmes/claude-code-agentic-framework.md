# Codebase Singularity

A Claude Code plugin implementing the "Codebase Singularity" concept by IndyDevDan. This framework creates an agentic layer around your codebase, enabling AI agents to operate autonomously through planning, building, reviewing, and fixing workflows.

## What is the Codebase Singularity?

The Codebase Singularity is the point where AI agents can run your codebase better than you can. The framework provides:

- **Structured Workflows**: Plan-Build-Review-Fix cycle for all development
- **Specialized Agents**: 9 agents for different tasks (planning, building, reviewing, etc.)
- **Quality Assurance**: Automated code review with scoring and feedback
- **Multi-Agent Orchestration**: Complex tasks coordinated across agents
- **Feedback Loops**: Self-reviewing, self-correcting automation

## Classification

This implementation is **Class 3, Grade 1+** - the highest level of the agentic layer framework:

| Class | Description | Status |
|-------|-------------|--------|
| **Class 1** | Foundation (memory, agents, tools, hooks) | ✓ Complete |
| **Class 2** | Workflows (portable layers, E2E flows) | ✓ Complete |
| **Class 3** | Orchestration (multi-agent coordination) | ✓ Complete |

## Quick Start

### In This Project

1. **Open Claude Code** in this directory
2. **Activate with context**:
   ```
   /prime
   ```
3. **Start developing**:

### In Other Projects

1. **Install globally** (one-time):
   ```bash
   # Copy commands and agents to ~/.claude/
   cp -r .claude/commands/project ~/.claude/commands/singularity
   cp -r agents/*.md ~/.claude/agents/
   cp -r skills/* ~/.claude/skills/
   ```

2. **Initialize in new project**:
   ```
   /setup
   ```

3. **Start developing**:
   ```
   /plan Add user authentication
   /build
   /review
   /fix
   ```

   Or use the complete cycle:
   ```
   /cycle Add user authentication
   ```

## Commands

### Core Workflow

| Command | Purpose |
|---------|---------|
| `/prime` | Activate with full context |
| `/plan` | Create implementation plan |
| `/build` | Implement from plan |
| `/review` | Quality analysis |
| `/fix` | Address issues |

### E2E Workflows

| Command | Purpose |
|---------|---------|
| `/cycle` | Complete Plan-Build-Review-Fix |
| `/feature` | Full feature development |
| `/bugfix` | Bug investigation and fix |

### Orchestration

| Command | Purpose |
|---------|---------|
| `/orchestrate` | Multi-agent coordination |
| `/delegate` | Direct agent invocation |

### Utility

| Command | Purpose |
|---------|---------|
| `/setup` | Initialize in new project |

## Agents

| Agent | Model | Specialty |
|-------|-------|-----------|
| orchestrator | opus | Multi-agent coordination |
| planner | opus | Planning, architecture |
| builder | sonnet | Code implementation |
| reviewer | opus | Quality analysis |
| fixer | sonnet | Issue resolution |
| test-writer | sonnet | Test creation |
| doc-fetcher | haiku | Documentation research |
| security-auditor | opus | Security analysis |
| refactorer | sonnet | Code improvement |

## Structure

```
├── .claude-plugin/plugin.json   # Plugin manifest
├── commands/                     # 11 workflow commands
├── agents/                       # 9 specialized agents
├── skills/                       # 4 skill modules
├── hooks/hooks.json             # Lifecycle hooks
├── scripts/                      # Hook scripts
├── templates/settings.json      # Project settings
├── specs/                        # Plans and reviews
├── ai_docs/                      # AI reference docs
├── CLAUDE.md                     # Claude-specific memory
├── AGENTS.md                     # Universal agent instructions
├── .mcp.json                     # MCP configuration
└── README.md                     # This file
```

## Core Workflow

The Plan-Build-Review-Fix cycle is the foundation:

```
    ┌─────────┐    ┌─────────┐    ┌─────────┐    ┌─────────┐
    │  PLAN   │───►│  BUILD  │───►│ REVIEW  │───►│   FIX   │
    └─────────┘    └─────────┘    └─────────┘    └────┬────┘
         ▲                                            │
         └────────── Loop until quality passes ◄──────┘
```

## Documentation

| Document | Purpose |
|----------|---------|
| `CLAUDE.md` | Claude-specific memory - read first |
| `AGENTS.md` | Universal AI agent instructions |
| `docs/QUICKSTART.md` | 20 hands-on use cases |
| `docs/USER_GUIDE.md` | How to use the framework |
| `docs/DEVELOPER_GUIDE.md` | Technical deep-dive |
| `docs/AGENTIC_LAYER.md` | Core concept explanation |
| `docs/CLASSIFICATION.md` | Class/Grade system reference |
| `docs/HOOKS_GUIDE.md` | Hooks and feedback loops |
| `docs/CONFIGURATION_GUIDE.md` | All settings and options |

## Using in New Projects

### Prerequisites

Install commands globally (one-time setup):

```bash
# From this project directory:
cp -r .claude/commands/project ~/.claude/commands/singularity
cp -r agents/*.md ~/.claude/agents/
cp -r skills/* ~/.claude/skills/
```

### Initialize New Project

```bash
cd /path/to/your/project
claude

# Run setup command
/setup
```

This creates:
- `CLAUDE.md` - Project memory
- `AGENTS.md` - Agent instructions
- `commands/` - Workflow commands
- `hooks/` - Automation hooks
- `specs/` - Plans and reviews

## Configuration

### Settings (`templates/settings.json`)

Configure agents, commands, hooks, and preferences.

### MCP Servers (`.mcp.json`)

External tool integrations (filesystem, GitHub, memory).

### Hooks (`hooks/hooks.json`)

Lifecycle automation (auto-lint, file protection, logging).

## Acknowledgements

This project is inspired by the YouTube video:

**[The Codebase Singularity: "My agents run my codebase better than I can"](https://www.youtube.com/watch?v=fop_yxV-mPo&t=34s)** by [IndyDevDan](https://www.youtube.com/@indydevdan)

All code and documentation were generated by **Claude Code** powered by **Claude Opus 4.5**.

## License

MIT
