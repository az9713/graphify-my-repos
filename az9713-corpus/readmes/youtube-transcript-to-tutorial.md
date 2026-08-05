# YouTube to Tutorial: 10 Claude Code Tricks

A case study in converting a 12-minute YouTube video into a comprehensive, self-contained developer tutorial — using Claude Code itself as the conversion tool.

## What This Is

This repository demonstrates a repeatable pipeline for turning video content into actionable written documentation. The source material is an [AI Labs video](https://www.youtube.com/watch?v=TmsH-RIHvas) covering 10 Claude Code power tricks. The output is a 1,750-line tutorial that a developer with zero Claude Code experience can follow from start to finish.

### The 10 Tricks

| # | Trick | What It Does |
|---|-------|-------------|
| 1 | `/insights` | Analyzes past sessions, generates improvement reports |
| 2 | CLAUDE.md Context | 4 foundational docs (PRD, architecture, decisions, feature tracking) for rich project context |
| 3 | Context7 MCP | Live library/framework documentation via MCP |
| 4 | Hooks + Exit Code 2 | Shell hooks that control agent behavior with blocking errors |
| 5 | Test Protection | Blocks test file modifications during TDD |
| 6 | MCP Tool Search | On-demand MCP tool loading to save context window space |
| 7 | Git Worktrees | Parallel isolated sessions on separate features |
| 8 | Strict Mode | Catch bugs at compile time (TypeScript, Python, Go, Rust) |
| 9 | Adversarial Agents | Multi-agent fact-checking and code review |
| 10 | Browser Verification | Accessibility tree-based UI testing with 95%+ token savings |

## Why This Exists

Video tutorials have a fundamental limitation: information is locked in a format that can't be searched, copied, or version-controlled. A 60-second video segment becomes 150-200 lines of written tutorial because written formats require:

- Complete setup steps (videos assume you'll figure it out)
- Full config file contents (videos show a brief flash on screen)
- Multiple examples (videos typically show one)
- Troubleshooting (videos don't cover what happens when things break)
- Platform-specific notes (videos show one OS)

This project solves that by extracting the knowledge from the video and repackaging it as a self-contained reference.

## Repository Structure

```
.
├── README.md                              # This file
├── .claude/
│   ├── settings.json                      # Claude Code config (agent teams enabled)
│   └── skills/
│       └── transcript-to-tutorial/        # Reusable skill for video-to-tutorial conversion
│           ├── SKILL.md                   # 7-phase pipeline skill definition
│           └── tutorial-template.md       # Output template for generated tutorials
├── docs/
│   ├── 10_claude_code_tricks_tutorial.md   # The tutorial (main deliverable)
│   ├── conversion_process.md              # How the conversion was done
│   ├── README_transcript.txt              # Raw video transcript + metadata
│   └── gemini3_summary.txt               # AI-generated structured summary
└── .gitignore
```

## The Conversion Pipeline

The tutorial was produced through a 7-phase pipeline, fully documented in [`docs/conversion_process.md`](docs/conversion_process.md):

```
  Video Transcript          AI Summary
       │                        │
       └──────────┬─────────────┘
                  │
          ┌───────▼────────┐
          │  Cross-reference │
          │  against official │
          │  Claude Code docs │
          └───────┬────────┘
                  │
          ┌───────▼────────┐
          │  Plan tutorial   │
          │  structure with  │
          │  parallel agents │
          └───────┬────────┘
                  │
          ┌───────▼────────┐
          │  Write complete  │
          │  tutorial in one │
          │  pass            │
          └───────┬────────┘
                  │
          ┌───────▼────────┐
          │  Automated       │
          │  review (9/10)   │
          └───────┬────────┘
                  │
          ┌───────▼────────┐
          │  Fix issues,     │
          │  commit          │
          └────────────────┘
```

### Key Insight: Fact-Checking Caught Outdated Information

The video referenced an `MCP_CLI` experimental flag for reducing context bloat. Cross-referencing against the official docs revealed this had been replaced by `ENABLE_TOOL_SEARCH`, enabled by default since v2.1.7. Without the fact-checking phase, the tutorial would have taught a deprecated approach.

## Quick Start

**Read the tutorial**: Open [`docs/10_claude_code_tricks_tutorial.md`](docs/10_claude_code_tricks_tutorial.md) and start from the Prerequisites section.

**Understand the process**: Read [`docs/conversion_process.md`](docs/conversion_process.md) for the full methodology.

**Replicate for your own video**: The conversion process doc includes a step-by-step template in its final section.

**Use the Claude Code skill**: Run `/transcript-to-tutorial <path-to-transcript>` in Claude Code to automate the pipeline. The skill is at [`.claude/skills/transcript-to-tutorial/SKILL.md`](.claude/skills/transcript-to-tutorial/SKILL.md).

## What Makes the Tutorial Self-Contained

Every trick includes:
- **Setup**: Dependencies, configs, and commands — nothing left to guess
- **Invocation**: Exact steps to trigger the trick inside Claude Code CLI
- **Examples**: 2-3 practical scenarios with complete, copy-pasteable code
- **Verification**: How to confirm the trick is working
- **Tips**: Power-user advice and platform-specific gotchas

Supporting sections:
- **Prerequisites**: All dependencies consolidated in one place
- **Cheat Sheet**: One-row-per-trick quick reference table
- **Troubleshooting**: 7 common issues with fixes
- **Glossary**: 15 key terms defined

## Human Effort

~30 minutes of oversight across two Claude Code sessions:
1. Provide the initial prompt with source material
2. Approve the plan
3. Request commit
4. Request process documentation
5. Request this README

Everything else — research, fact-checking, planning, writing, reviewing, fixing — was autonomous.

## License

This project is provided as-is for educational purposes. The source video is by [AI Labs](https://www.youtube.com/@ailaboratoriespro). Claude Code is by [Anthropic](https://anthropic.com).
