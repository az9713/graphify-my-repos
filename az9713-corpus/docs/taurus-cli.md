---
repo: taurus-cli
description: like gemini-cli
language: TypeScript
stars: 1
forks: 0
created: 2025-11-18
updated: 2026-01-21
topics: 
is_fork: False
kb: 505
---

# taurus-cli
# 🐂 Taurus CLI

A complete Claude Code clone with subagents, skills, slash commands, hooks, full MCP integration, and all features present in Claude Code.

## Features

### 🛠️ Complete Tool System
- **Bash** - Execute shell commands with timeout support
- **Read** - Read files with line numbers and formatting
- **Write** - Create new files with proper validation
- **Edit** - Perform exact string replacements in files
- **Glob** - Fast file pattern matching
- **Grep** - Powerful content search with regex support
- **TodoWrite** - Task list management for complex workflows
- **Task** - Launch specialized subagents for autonomous execution
- **WebFetch** - Fetch and analyze web content
- **WebSearch** - Search the web for up-to-date information
- **Skill** - Execute specialized skills
- **SlashCommand** - Custom command execution

### 🤖 Subagent System
Launch specialized agents for different tasks:
- **general-purpose** - Complex multi-step tasks
- **Explore** - Fast codebase exploration
- **Plan** - Planning and analysis

### 🎣 Hooks System
Event-based hooks for automation:
- `session-start` - Triggered when a session begins
- `session-end` - Triggered when a session ends
- `user-prompt-submit` - Triggered when user submits input
- `before-tool-call` - Triggered before tool execution
- `after-tool-call` - Triggered after tool execution

### ⚡ Slash Commands
Create custom commands in `.taurus/commands/` directory:
```markdown
# File: .taurus/commands/review.md
Review the current code changes and provide detailed feedback.
```

Usage: `/review`

### 🎯 Skills System
Create reusable skills in `.taurus/skills/` directory:
```markdown
# File: .taurus/skills/refactor.md
Help refactor code following best practices and modern patterns.
```

Usage: Execute via Skill tool

### 💾 Session Persistence
- Automatic conversation history saving
- Resume previous sessions
- Session management commands

### 🔌 MCP (Model Context Protocol) Integration
Full support for MCP servers to dynamically extend capabilities:
- **Stdio Transport** - Connect to local MCP servers via stdin/stdout
- **HTTP/SSE Transport** - Connect to remote MCP servers via HTTP with Server-Sent Events
- **Dynamic Tool Loading** - Tools from MCP servers automatically become available
- **Resource Access** - Read files, databases, and other resources through MCP
- **Prompt Templates** - Use predefined prompts from MCP servers
- **Multiple Servers** - Connect to multiple MCP servers simultaneously

See [MCP.md](./MCP.md) for complete documentation.

### ⚙️ Configuration
Flexible configuration via YAML files:
- Global config: `~/.taurus/config.yaml`
- Project config: `.taurus/config.yaml`
- Environment variables

## Installation

```bash
# Clone the repository
git clone https://github.com/az9713/taurus-cli.git
cd taurus-cli

# Install dependencies
npm install

# Build the project
npm run build

# Link for global usage
npm link

# Or run directly
node dist/index.js
```

## Quick Start

1. **Set up your API key:**
```bash
export ANTHROPIC_API_KEY="your-api-key-here"
```

2. **Initialize a project:**
```bash
taurus init
```

3. **Start chatting:**
```bash
taurus chat
```

## Configuration

### Global Configuration
Create `~/.taurus/config.yaml`:

```yaml
# Claude API settings
model: claude-sonnet-4-5-20250929
maxTokens: 8096
temperature: 1.0

# Paths
workingDirectory: .
sessionDirectory: ~/.taurus/sessions

# Features
hooksEnabled: true

# MCP Servers (optional)
mcpServers:
  - name: example-server
    command: node
    args:
      - /path/to/server.js
    env:
      KEY: value
```

### Project Configuration
Create `.taurus/config.yaml` in your project:

```yaml
model: claude-sonnet-4-5-20250929
maxTokens: 8096
temperature: 1.0
```

### Hooks Configuration
Create `.taurus/hooks.yaml`:

```yaml
hooks:
  - name: session-start
    event: session-start
    command: echo "Welcome to Taurus!"
    enabled: true

  - name: git-safety
    event: before-tool-call
    command: |
      if [[ "$TAURUS_TOOL" == "Bash" ]] && [[ "$TAURUS_COMMAND" == *"git push"* ]]; then
        echo "⚠️  Git push detected - be careful!"
      fi
    enabled: true
```

## Usage

### Interactive Mode (Default)
```bash
taurus chat
```

### With Options
```bash
# Use a specific model
taurus chat --model claude-opus-4-20250514

# Resume a session
taurus chat --session session_1234567890_abc123

# Disable hooks
taurus chat --no-hooks
```

### Configuration Management
```bash
# Show current configuration
taurus config show

# Get a specific value
taurus config get model

# Set a value
taurus config set model claude-sonnet-4-5-20250929
```

## Creating Custom Commands

### Slash Commands
Create `.taurus/commands/mycommand.md`:

```markdown
# My Custom Command

This command does something useful.

Steps:
1. Analyze the current context
2. Perform the required action
3. Report the results
```

Usage in chat:
```
taurus> /mycommand
```

### Skills
Create `.taurus/skills/myskill.md`:

```markdown
# My Skill

This skill provides specialized knowledge for a specific task.

When invoked, you should:
- Do this
- Then that
- Finally this
```

Skills are invoked programmatically by the agent when needed.

## Architecture

```
taurus-cli/
├── src/
│   ├── agent/
│   │   └── orchestrator.ts      # Main agent orchestration
│   ├── api/
│   │   └── claude.ts             # Claude API client
│   ├── cli/
│   │   └── repl.ts               # Interactive REPL
│   ├── config/
│   │   ├── default.ts            # Default configuration
│   │   └── manager.ts            # Configuration management
│   ├── hooks/
│   │   └── manager.ts            # Hooks system
│   ├── session/
│   │   └── manager.ts            # Session persistence
│   ├── tools/
│   │   ├── base.ts               # Base tool class
│   │   ├── bash.ts               # Bash tool
│   │   ├── read.ts               # Read tool
│   │   ├── write.ts              # Write tool
│   │   ├── edit.ts               # Edit tool
│   │   ├── glob.ts               # Glob tool
│   │   ├── grep.ts               # Grep tool
│   │   ├── todo.ts               # TodoWrite tool
│   │   ├── task.ts               # Task/subagent tool
│   │   ├── webfetch.ts           # WebFetch tool
│   │   ├── websearch.ts          # WebSearch tool
│   │   ├── skill.ts              # Skill tool
│   │   ├── slashcommand.ts       # SlashCommand tool
│   │   └── index.ts              # Tool registry
│   ├── types/
│   │   └── index.ts              # TypeScript types
│   ├── utils/
│   │   ├── files.ts              # File utilities
│   │   ├── logger.ts             # Logging utilities
│   │   └── markdown.ts           # Markdown rendering
│   └── index.ts                  # Main entry point
├── .taurus/
│   ├── commands/                 # Custom slash commands
│   ├── skills/                   # Custom skills
│   ├── config.yaml               # Project configuration
│   └── hooks.yaml                # Hooks configuration
└── package.json
```

## Development

### Build
```bash
npm run build
```

### Watch Mode
```bash
npm run dev
```

### Lint
```bash
npm run lint
```

### Format
```bash
npm run format
```

### Test
```bash
npm test
```

## Tools Reference

### Bash
Execute shell commands with timeout and output capture.

```typescript
{
  command: "ls -la",
  description: "List files in current directory",
  timeout: 120000
}
```

### Read
Read files with line numbers and truncation.

```typescript
{
  file_path: "/path/to/file.ts",
  offset: 0,
  limit: 2000
}
```

### Write
Create new files (requires Read first for existing files).

```typescript
{
  file_path: "/path/to/file.ts",
  content: "export const foo = 'bar';"
}
```

### Edit
Perform exact string replacements.

```typescript
{
  file_path: "/path/to/file.ts",
  old_string: "const foo = 'bar'",
  new_string: "const foo = 'baz'",
  replace_all: false
}
```

### Glob
Find files by pattern.

```typescript
{
  pattern: "**/*.ts",
  path: "./src"
}
```

### Grep
Search file contents with regex.

```typescript
{
  pattern: "function.*\\(\\)",
  path: "./src",
  output_mode: "content",
  "-i": false
}
```

### TodoWrite
Manage task lists.

```typescript
{
  todos: [
    {
      content: "Implement feature X",
      status: "in_progress",
      activeForm: "Implementing feature X"
    }
  ]
}
```

### Task
Launch subagents.

```typescript
{
  subagent_type: "Explore",
  prompt: "Find all React components in the codebase",
  description: "Explore React components",
  model: "haiku"
}
```

### WebFetch
Fetch and analyze web content.

```typescript
{
  url: "https://example.com",
  prompt: "Summarize the main points"
}
```

### WebSearch
Search the web.

```typescript
{
  query: "TypeScript best practices 2025",
  allowed_domains: ["typescript.org"],
  blocked_domains: ["spam.com"]
}
```

## Examples

### Example 1: Code Review
```
taurus> Review the changes in src/app.ts and suggest improvements
```

### Example 2: Bug Fix
```
taurus> I'm getting a TypeError in the login function. Help me debug it.
```

### Example 3: Refactoring
```
taurus> Refactor the UserService class to use dependency injection
```

### Example 4: Documentation
```
taurus> Add JSDoc comments to all public methods in src/utils/
```

### Example 5: Testing
```
taurus> Create unit tests for the AuthController
```

## Advanced Features

### Parallel Tool Execution
Taurus automatically executes independent tools in parallel for maximum efficiency.

### Streaming Responses
Responses stream in real-time for a responsive experience.

### Context Management
Intelligent context management to stay within token limits.

### Error Recovery
Robust error handling and recovery mechanisms.

## Troubleshooting

### API Key Issues
```bash
# Set in environment
export ANTHROPIC_API_KEY="your-key"

# Or in config
echo "apiKey: your-key" > ~/.taurus/config.yaml
```

### Hook Execution Failures
- Check hook command syntax
- Verify file permissions
- Review hook logs
- Test commands manually

### Tool Errors
- Ensure required tools are installed (rg, git, etc.)
- Check file permissions
- Verify paths are absolute

## Contributing

Contributions are welcome! Please:

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Add tests
5. Submit a pull request

## License

MIT License - see LICENSE file for details

## Comparison with Claude Code

Wondering how Taurus CLI compares to the official Claude Code? See our comprehensive comparison:

**[Claude Code vs Taurus CLI Comparison](./CLAUDE_CODE_COMPARISON.md)**

**TL;DR:**
- **Claude Code:** Official product with web/mobile access, enterprise support, $20/month
- **Taurus CLI:** Open source with test generation, security scanning, database tools, no subscription

Both tools are compatible and can use the same MCP servers, hooks, and skills.

## Acknowledgments

- Inspired by Claude Code from Anthropic
- Built with Claude AI assistance
- Uses the Anthropic SDK

## Support

- GitHub Issues: https://github.com/az9713/taurus-cli/issues
- Documentation: https://github.com/az9713/taurus-cli/wiki

---

Built with ❤️ using Claude AI
