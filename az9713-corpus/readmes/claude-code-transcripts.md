# claude-code-transcripts

[![PyPI](https://img.shields.io/pypi/v/claude-code-transcripts.svg)](https://pypi.org/project/claude-code-transcripts/)
[![Changelog](https://img.shields.io/github/v/release/simonw/claude-code-transcripts?include_prereleases&label=changelog)](https://github.com/simonw/claude-code-transcripts/releases)
[![Tests](https://github.com/simonw/claude-code-transcripts/workflows/Test/badge.svg)](https://github.com/simonw/claude-code-transcripts/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/simonw/claude-code-transcripts/blob/main/LICENSE)

Convert Claude Code session files (JSON or JSONL) to clean, mobile-friendly HTML pages with pagination. Features syntax highlighting, dark mode, and multiple output formats.

[Example transcript](https://static.simonwillison.net/static/2025/claude-code-microjs/index.html) produced using this tool.

Read [A new way to extract detailed transcripts from Claude Code](https://simonwillison.net/2025/Dec/25/claude-code-transcripts/) for background on this project.

## Features

### Core Features (Original)
- **HTML transcript generation** - Convert JSON/JSONL sessions to paginated HTML
- **Tool renderers** - Pretty display for Write, Edit, Bash, TodoWrite tools
- **GitHub integration** - Git commits link directly to GitHub
- **Gist publishing** - Share transcripts via GitHub Gist
- **Batch conversion** - Convert all sessions to a searchable archive
- **Session picker** - Interactive selection from local and web sessions

### Enhanced Features (New)

The following features were added to extend the original functionality:

#### UI Enhancements
- **Dark mode toggle** - Click the moon/sun icon in the header to switch themes. Preference is saved to localStorage and respects system preference.
- **Syntax highlighting** - Code blocks are highlighted using Highlight.js (loaded from CDN)
- **Image lazy loading** - Images load on-demand for better performance

#### New Tool Renderers
Seven additional tool renderers for comprehensive Claude Code support:
- **Skill** - Displays skill invocations with name and arguments
- **WebFetch** - Shows URL with clickable link and prompt
- **WebSearch** - Displays search queries
- **Task** - Shows subagent type, description, and prompt
- **Read** - Displays file path with extracted filename
- **Glob** - Shows glob patterns and search paths
- **Grep** - Displays regex patterns with output mode

#### Output Formats
- **Markdown export** - Use `--format markdown` to generate `.md` files instead of HTML
- **Custom CSS** - Use `--css-file` to append your own styles
- **Custom templates** - Use `--template-dir` to override Jinja2 templates

#### Session Filtering (for `all` command)
- **Date filtering** - `--since` and `--until` to filter by date range
- **Project filtering** - `--project` to filter by project name
- **Size filtering** - `--min-size` to filter by file size in KB

#### Performance
- **Parallel batch processing** - Uses ThreadPoolExecutor (4 workers) for faster `all` command
- **Type hints** - Core functions have type annotations for better IDE support

## Installation

Install this tool using `uv`:
```bash
uv tool install claude-code-transcripts
```
Or run it without installing:
```bash
uvx claude-code-transcripts --help
```

## Usage

This tool converts Claude Code session files into browseable multi-page HTML transcripts.

There are four commands available:

- `local` (default) - select from local Claude Code sessions stored in `~/.claude/projects`
- `web` - select from web sessions via the Claude API
- `json` - convert a specific JSON or JSONL session file
- `all` - convert all local sessions to a browsable HTML archive

The quickest way to view a recent local session:

```bash
claude-code-transcripts
```

This shows an interactive picker to select a session, generates HTML, and opens it in your default browser.

### Output options

All commands support these options:

- `-o, --output DIRECTORY` - output directory (default: writes to temp dir and opens browser)
- `-a, --output-auto` - auto-name output subdirectory based on session ID or filename
- `--repo OWNER/NAME` - GitHub repo for commit links (auto-detected from git push output if not specified)
- `--open` - open the generated `index.html` in your default browser (default if no `-o` specified)
- `--gist` - upload the generated HTML files to a GitHub Gist and output a preview URL
- `--json` - include the original session file in the output directory

The `local` and `json` commands also support:

- `--format FORMAT` - output format: `html` (default) or `markdown`
- `--css-file PATH` - custom CSS file to append to the default styles
- `--template-dir PATH` - custom template directory (templates override defaults)

The generated output includes:
- `index.html` - an index page with a timeline of prompts and commits
- `page-001.html`, `page-002.html`, etc. - paginated transcript pages

### Local sessions

Local Claude Code sessions are stored as JSONL files in `~/.claude/projects`. Run with no arguments to select from recent sessions:

```bash
claude-code-transcripts
# or explicitly:
claude-code-transcripts local
```

Use `--limit` to control how many sessions are shown (default: 10):

```bash
claude-code-transcripts local --limit 20
```

### Web sessions

Import sessions directly from the Claude API:

```bash
# Interactive session picker
claude-code-transcripts web

# Import a specific session by ID
claude-code-transcripts web SESSION_ID

# Import and publish to gist
claude-code-transcripts web SESSION_ID --gist
```

On macOS, API credentials are automatically retrieved from your keychain (requires being logged into Claude Code). On other platforms, provide `--token` and `--org-uuid` manually.

### Publishing to GitHub Gist

Use the `--gist` option to automatically upload your transcript to a GitHub Gist and get a shareable preview URL:

```bash
claude-code-transcripts --gist
claude-code-transcripts web --gist
claude-code-transcripts json session.json --gist
```

This will output something like:
```
Gist: https://gist.github.com/username/abc123def456
Preview: https://gisthost.github.io/?abc123def456/index.html
Files: /var/folders/.../session-id
```

The preview URL uses [gisthost.github.io](https://gisthost.github.io/) to render your HTML gist. The tool automatically injects JavaScript to fix relative links when served through gisthost.

Combine with `-o` to keep a local copy:

```bash
claude-code-transcripts json session.json -o ./my-transcript --gist
```

**Requirements:** The `--gist` option requires the [GitHub CLI](https://cli.github.com/) (`gh`) to be installed and authenticated (`gh auth login`).

### Auto-naming output directories

Use `-a/--output-auto` to automatically create a subdirectory named after the session:

```bash
# Creates ./session_ABC123/ subdirectory
claude-code-transcripts web SESSION_ABC123 -a

# Creates ./transcripts/session_ABC123/ subdirectory
claude-code-transcripts web SESSION_ABC123 -o ./transcripts -a
```

### Including the source file

Use the `--json` option to include the original session file in the output directory:

```bash
claude-code-transcripts json session.json -o ./my-transcript --json
```

This will output:
```
JSON: ./my-transcript/session_ABC.json (245.3 KB)
```

This is useful for archiving the source data alongside the HTML output.

### Converting from JSON/JSONL files

Convert a specific session file directly:

```bash
claude-code-transcripts json session.json -o output-directory/
claude-code-transcripts json session.jsonl --open
```
This works with both JSONL files in the `~/.claude/projects/` folder and JSON session files extracted from Claude Code for web.

The `json` command can take a URL to a JSON or JSONL file as an alternative to a path on disk.

### Exporting to Markdown

Export a session as a Markdown file instead of HTML:

```bash
claude-code-transcripts json session.jsonl -o ./output --format markdown
claude-code-transcripts local --format markdown
```

This creates a single `.md` file containing the entire transcript with tool calls formatted as code blocks.

### Converting all sessions

Convert all your local Claude Code sessions to a browsable HTML archive:

```bash
claude-code-transcripts all
```

This creates a directory structure with:
- A master index listing all projects
- Per-project pages listing sessions
- Individual session transcripts

Options:

- `-s, --source DIRECTORY` - source directory (default: `~/.claude/projects`)
- `-o, --output DIRECTORY` - output directory (default: `./claude-archive`)
- `--include-agents` - include agent session files (excluded by default)
- `--dry-run` - show what would be converted without creating files
- `--open` - open the generated archive in your default browser
- `-q, --quiet` - suppress all output except errors
- `--since DATE` - only include sessions after this date (YYYY-MM-DD)
- `--until DATE` - only include sessions before this date (YYYY-MM-DD)
- `--project NAME` - only include sessions from projects matching this name
- `--min-size KB` - only include sessions larger than this size in KB

Examples:

```bash
# Preview what would be converted
claude-code-transcripts all --dry-run

# Convert all sessions and open in browser
claude-code-transcripts all --open

# Convert to a specific directory
claude-code-transcripts all -o ./my-archive

# Include agent sessions
claude-code-transcripts all --include-agents

# Only sessions from the last week
claude-code-transcripts all --since 2024-01-08

# Only a specific project
claude-code-transcripts all --project my-project

# Only large sessions
claude-code-transcripts all --min-size 100
```

### Customizing output

Override the default CSS with a custom stylesheet:

```bash
claude-code-transcripts json session.jsonl --css-file ./custom.css
```

Use custom Jinja2 templates (must include `base.html`, `page.html`, `index.html`, `macros.html`):

```bash
claude-code-transcripts json session.jsonl --template-dir ./my-templates
```

## Development

To contribute to this tool, first checkout the code. You can run the tests using `uv run`:
```bash
cd claude-code-transcripts
uv run pytest
```
And run your local development copy of the tool like this:
```bash
uv run claude-code-transcripts --help
```

## Acknowledgements

This project is inspired by and built upon Simon Willison's work:
- **Blog post**: [A new way to extract detailed transcripts from Claude Code](https://simonwillison.net/2025/Dec/25/claude-code-transcripts/)
- **Original repository**: [simonw/claude-code-transcripts](https://github.com/simonw/claude-code-transcripts)

The enhanced features (dark mode, syntax highlighting, new tool renderers, markdown export, session filtering, custom CSS/templates, parallel processing, and type hints) along with their documentation were generated by **Claude Code** using **Claude Opus 4.5**.
