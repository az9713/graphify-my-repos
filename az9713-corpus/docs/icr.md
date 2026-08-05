---
repo: icr
description: 🛡️ Make AI show its work before it does the work. The intent problem? Fixed.
language: Shell
stars: 0
forks: 0
created: 2026-01-03
updated: 2026-01-03
topics: ai-agents, ai-safety, audit-trail, claude-code, intent-verification, llm-safety
is_fork: False
kb: 147
---

# icr
# ICR - Intent-Check-Receipt

A Claude Code plugin that implements the Intent-Check-Receipt pattern for safer AI agent operations.

> **Acknowledgement**: This project is inspired by the YouTube video ["The AI Failure Mode Nobody Warned You About (And how to prevent it from happening)"](https://www.youtube.com/watch?v=T74uZgfu6mU&t=11s) which brilliantly articulates the intent problem in AI agents.

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| **[Quick Start](docs/QUICK_START.md)** | New Users | Get started in 5 minutes with 10 practical examples |
| **[User Guide](docs/USER_GUIDE.md)** | All Users | Comprehensive guide to all features |
| **[Architecture](docs/ARCHITECTURE.md)** | Everyone | Big-picture system design and data flow |
| **[Developer Guide](docs/DEVELOPER_GUIDE.md)** | Developers | Implementation details and code walkthrough |
| **[Contributing](docs/CONTRIBUTING.md)** | Contributors | How to contribute to the project |
| **[Troubleshooting](docs/TROUBLESHOOTING.md)** | Everyone | Common issues and solutions |
| **[Full Specification](docs/ICR_PLUGIN_SPEC.md)** | Reference | Complete 4700+ line specification |

> **New to ICR?** Start with the [Quick Start Guide](docs/QUICK_START.md) for step-by-step tutorials.
>
> **AI Assistants:** See [CLAUDE.md](CLAUDE.md) for codebase context.

---

## What is ICR?

ICR (Intent-Check-Receipt) addresses the **intent problem** in AI agents: the gap between what users mean and what AI interprets. Before executing actions, ICR:

1. **Intent**: Generates a structured document showing what the AI believes the user wants
2. **Check**: Pauses for verification based on action severity and confidence
3. **Receipt**: Logs the full audit trail including interpretation, approval, and outcome

## Quick Start

### Installation

```bash
# Clone or copy the icr directory to your plugins folder
cp -r icr ~/.claude/plugins/icr

# Or install via Claude Code
claude plugin install ./icr
```

### First Use

ICR works automatically once installed. When Claude attempts a significant action:

> **Want more examples?** See [Quick Start Guide](docs/QUICK_START.md) for 10 step-by-step use cases.

```
ICR INTENT CHECK
----------------
Task: Delete all .tar.gz files in /tmp/old-builds/ older than 30 days

Affected:
  - /tmp/old-builds/*.tar.gz (47 files, 2.3GB)

Excluded:
  - Files newer than 30 days
  - Non-.tar.gz files

Severity: CRITICAL | Confidence: 0.62 | Route: HUMAN_REVIEW

[1] Proceed  [2] Edit  [3] Abort  [4] Explain  [5] Bypass
```

## Commands

| Command | Description |
|---------|-------------|
| `/icr:receipts` | View receipt history |
| `/icr:config` | View or edit configuration |
| `/icr:check` | Manually trigger check on next action |
| `/icr:trust` | Enable/disable trust mode |
| `/icr:audit` | Deep analysis of receipts |
| `/icr:export` | Export receipts to file |
| `/icr:stats` | Session statistics |
| `/icr:debug` | Show confidence calculation details |
| `/icr:simulate` | Dry-run intent check |

## How It Works

### Severity Classification

Actions are classified into 4 severity levels:

| Level | Examples | Default Behavior |
|-------|----------|------------------|
| LOW | Read, Glob, Grep | Auto-approve |
| MEDIUM | Write, Edit | Confidence-based |
| HIGH | Bash | Usually review |
| CRITICAL | Delete, rm -rf | Always review |

### Confidence Scoring

ICR calculates confidence using 4 weighted signals:

- **Ambiguity Analysis** (30%): How many valid interpretations exist
- **Intent-to-Action Distance** (25%): Semantic gap between request and tool
- **Historical Patterns** (20%): Similarity to past successful actions
- **Uncertainty Markers** (25%): Hedging language in the request

### Decision Routes

Based on severity and confidence, actions route to:

- **AUTO_APPROVE**: Proceeds immediately, logs receipt
- **AI_REVIEW**: AI reviewer validates, may escalate
- **HUMAN_REVIEW**: User must approve/reject

## Configuration

Edit `.claude/icr/config.json` or use `/icr:config set`:

```json
{
  "thresholds": {
    "CRITICAL": {
      "autoApprove": 1.01,
      "aiReview": 0.90,
      "humanReview": 0.00
    }
  },
  "hooks": {
    "preToolUse": {
      "excludeTools": ["Read", "Glob", "Grep", "Ls"]
    }
  }
}
```

## Trust Mode

For known-safe workflows, enable trust mode:

```
> /icr:trust on

Trust mode ENABLED
  - LOW/MEDIUM actions auto-approve
  - HIGH actions use AI review only
  - CRITICAL actions still require human review
```

## Receipts & Auditing

All checks are logged to `.claude/icr/receipts/`:

```
> /icr:receipts

 #   | Time     | Tool       | Severity | Decision      | Outcome
---------------------------------------------------------------------
 001 | 10:00:00 | Write      | MEDIUM   | AUTO_APPROVE  | Proceeded
 002 | 10:00:15 | Bash       | CRITICAL | HUMAN_REVIEW  | Approved
 003 | 10:00:30 | Edit       | MEDIUM   | AI_REVIEW     | AI Approved
```

## File Structure

```
icr/
├── .claude-plugin/plugin.json    # Plugin manifest
├── commands/                      # Slash commands (9 commands)
├── skills/                        # AI-invocable skills
├── hooks/hooks.json              # Hook configuration
├── scripts/                       # Hook implementations
│   └── lib/                      # Core library (7 scripts)
├── config/defaults.json          # Default configuration
├── schemas/                       # JSON validation schemas
├── prompts/                       # AI prompt templates
├── docs/                          # Documentation
│   ├── QUICK_START.md            # Quick start with 10 use cases
│   ├── USER_GUIDE.md             # Comprehensive user guide
│   ├── DEVELOPER_GUIDE.md        # Developer documentation
│   ├── ARCHITECTURE.md           # System architecture
│   ├── CONTRIBUTING.md           # Contribution guidelines
│   ├── TROUBLESHOOTING.md        # Common issues & solutions
│   └── ICR_PLUGIN_SPEC.md        # Full specification
├── CLAUDE.md                      # AI assistant context
├── CHANGELOG.md                   # Version history
└── LICENSE                        # MIT License
```

> See [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for detailed file descriptions and dependency graphs.

## Customization

### Adding Severity Rules

```json
{
  "severity": {
    "userRules": [
      {
        "pattern": "Bash",
        "condition": "args.command.includes('rm')",
        "severity": "CRITICAL",
        "reason": "Any rm command is critical"
      }
    ]
  }
}
```

### Adjusting Thresholds

```bash
# More permissive for HIGH severity
/icr:config set thresholds.HIGH.autoApprove 0.80

# Stricter for MEDIUM severity
/icr:config set thresholds.MEDIUM.autoApprove 0.85
```

## Philosophy

ICR operates on the principle that **the cost of asking is low, but the cost of wrong action can be high**. It:

- Makes invisible AI interpretation visible
- Provides verification proportional to risk
- Maintains full audit trails
- Supports both real-time safety and forensic analysis

## Prerequisites

- **jq** 1.6 or higher (for JSON processing)
- **Claude Code** (the plugin host)
- **Bash** (Git Bash on Windows, native on macOS/Linux)

See [QUICK_START.md](docs/QUICK_START.md) for installation instructions.

## Getting Help

| Need | Resource |
|------|----------|
| **Installation issues?** | [Troubleshooting Guide](docs/TROUBLESHOOTING.md#installation-issues) |
| **Commands not working?** | [Troubleshooting Guide](docs/TROUBLESHOOTING.md#commands-not-found) |
| **Too many prompts?** | [Troubleshooting Guide](docs/TROUBLESHOOTING.md#performance-issues) |
| **Understanding a feature?** | [User Guide](docs/USER_GUIDE.md) |
| **Want to contribute?** | [Contributing Guide](docs/CONTRIBUTING.md) |
| **System architecture?** | [Architecture](docs/ARCHITECTURE.md) |

## License

MIT License - See [LICENSE](LICENSE) file for details.

---

**Version:** 1.0.0 | **Full Spec:** [docs/ICR_PLUGIN_SPEC.md](docs/ICR_PLUGIN_SPEC.md)
