# Claude Cowork & Claude Code: Best Practices Report

A comprehensive, exhaustive report on best practices for Claude Cowork and Claude Code — synthesized from community expertise, official Anthropic documentation, and open-source tooling.

## What's Inside

**[`docs/claude_cowork_best_practices_report.md`](docs/claude_cowork_best_practices_report.md)** — The full report covering 23 best practices across 7 sections:

- **Part 1 — Context Architecture** (Practices 1–5): Manifest files, global instructions, context files, folder rules, and deliberate context scoping
- **Part 2 — Task Design** (Practices 6–10): End-state definitions, plan-before-execute, uncertainty handling, session batching, parallel subagents
- **Part 3 — Automation & Scheduling** (Practices 11–13): Recurring tasks, externalizing memory, connectors and MCP integrations
- **Part 4 — Plugins & Skills** (Practices 14–16): Composable plugins, custom skill files, conversational plugin building
- **Part 5 — Safety & Efficiency** (Practice 17): Backups, isolation, permissions, prompt injection defense, usage tracking
- **Part 6 — Official Best Practices** (Practices 18–23): Verification, explore-plan-code workflow, course-correction, writer/reviewer pattern, fan-out at scale, failure anti-patterns
- **Part 7 — Cowork Context Kit**: Open-source starter implementation with ready-to-install templates

Every practice includes **ready-to-use examples** — copy-pasteable templates for CLAUDE.md files, manifest files, context files, custom skills, subagent definitions, hooks, automation scripts, and more.

## Sources

This report was synthesized from the following sources:

1. **[The Most Important Setup To Have In Your AI Agents](https://www.youtube.com/watch?v=cop_G65D7PA&t=22s)** — AI Labs Pro video walkthrough and transcript covering tested Cowork techniques
2. **[17 Best Practices That Make Claude Cowork 100x More Powerful](https://x.com/heynavtoor/status/2028148844891152554)** — Nav Toor's comprehensive thread based on 400+ Cowork sessions
3. **[cowork-context-kit](https://github.com/hughtopian-gif/cowork-context-kit)** — Open-source tiered context management system for Claude Cowork
4. **[Anthropic Claude Code Documentation](https://code.claude.com/docs)** — Official docs including best practices, memory, skills, subagents, hooks, plugins, and cost management
5. **[Claude Code Changelog](https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md)** — Feature releases and improvements (v2.1.45–2.1.63)

## License

This report is provided for educational and reference purposes. Original source content belongs to its respective authors.
