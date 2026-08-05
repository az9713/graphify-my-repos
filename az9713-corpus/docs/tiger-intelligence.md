---
repo: tiger-intelligence
description: Claude Code plugin suite for identifying and protecting tiger teams - the key people who actually keep organizations running
language: None
stars: 0
forks: 0
created: 2026-01-04
updated: 2026-01-04
topics: 
is_fork: False
kb: 93
---

# tiger-intelligence
# Tiger Intelligence

**Identify and protect the tiger teams that actually run your organization.**

Tiger Intelligence is a Claude Code plugin suite that helps organizations understand where real value comes from - not the org chart, but the actual network of people who fix things when they break.

Based on [Nate Jones' framework](https://natesnewsletter.substack.com/p/grab-the-4-prompts-i-use-to-make) for making messy work legible without killing what made it valuable.

## The Problem

Every organization has two structures:
- **The official structure**: Org charts, RACI matrices, dashboards, OKRs
- **The real structure**: The people who actually get called when something is on fire

AI makes it cheap to generate beautiful dashboards that look authoritative. But these "single pane of glass" tools often strangle the very people who keep organizations running - while leadership becomes overconfident in the wrong map.

## The Solution

Tiger Intelligence flips the script:
- Instead of surveillance dashboards, give small teams execution power
- Instead of AI bureaucrats dictating work, use AI as a historian reconstructing what happened
- Instead of fake legibility, create real understanding of where value comes from

## System Architecture

```
┌─────────────────────────────────────────────────────────┐
│                   DATA INTEGRATION LAYER                 │
│  MCP Servers: GitHub, Slack, Jira, Linear, Notion,      │
│               PagerDuty, Google Docs, Calendar          │
└─────────────────────────────────────────────────────────┘
                            │
        ┌───────────────────┼───────────────────┐
        ▼                   ▼                   ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│  FOR LEADERS  │   │   FOR ICs     │   │  FOR PM/LEADS │
├───────────────┤   ├───────────────┤   ├───────────────┤
│ Tiger Team    │   │ "Am I a       │   │ Tiger         │
│ Identifier    │   │  Tiger?"      │   │ Dependency    │
│               │   │               │   │ Map           │
│ Map Audit     │   │ Visibility    │   │ Tiger Health  │
│               │   │ Gap Finder    │   │ Monitor       │
└───────────────┘   └───────────────┘   └───────────────┘
```

## Quick Start

### Installation

Add the Tiger Intelligence marketplace to Claude Code:

```bash
claude plugin marketplace add github:your-username/tiger-intelligence
```

Then install the plugins you need:

```bash
# For Individual Contributors
claude plugin install tiger-ics@tiger-intelligence

# For Leaders/Executives
claude plugin install tiger-leaders@tiger-intelligence

# For PMs and Team Leads
claude plugin install tiger-leads@tiger-intelligence

# Shared data layer (recommended - enables richer analysis)
claude plugin install tiger-core@tiger-intelligence
```

### Local Development

Test the plugins locally:

```bash
git clone https://github.com/your-username/tiger-intelligence.git
cd tiger-intelligence
claude --plugin-dir ./plugins/tiger-ics
```

## Plugins & Skills

### tiger-core (Data Integration Layer)

Shared MCP server configurations for connecting to:
- **GitHub**: Commits, PRs, code ownership, incident patterns
- **Slack**: @mentions, DMs during crises, channel activity
- **Jira/Linear**: Issue assignments, escalations, sprint patterns
- **Notion**: Documentation ownership, wiki contributions
- **PagerDuty**: On-call patterns, incident response
- **Google Docs**: Document collaboration patterns
- **Google Calendar**: Meeting patterns, 1:1s, war rooms

Configure credentials in your environment - skills gracefully degrade when data sources aren't available.

### tiger-ics (For Individual Contributors)

**Am I a Tiger?**
> Discover if you're carrying more organizational weight than your job title suggests.

Analyzes your contribution patterns to reveal if you're a "tiger" - one of those key people who actually keeps things running. Get a Tiger Score, contribution map, and visibility strategy.

**Visibility Gap Finder**
> Find where your valuable work falls through the cracks.

Maps the gap between what you actually do and what shows up in formal systems. Creates impact briefs, proof lists, and visibility plans - without turning you into a self-promoter.

### tiger-leaders (For Leaders & Executives)

**Tiger Team Identifier**
> Map who actually keeps your organization running.

Analyzes emergency patterns, escalation paths, and informal influence to find your tiger teams. Produces risk assessments, de-risking plans, and protection recommendations.

**Map Audit**
> Evaluate if your dashboards measure reality or generate noise.

Audits metrics, dashboards, and AI-generated reports for validity, gaming potential, and blind spots. Trust more, trust less, or trust differently.

### tiger-leads (For PMs & Team Leads)

**Tiger Dependency Map**
> Understand which key people your roadmap secretly depends on.

Maps single points of failure, knowledge dependencies, and bottleneck patterns. Creates risk matrices and mitigation plans.

**Tiger Health Monitor**
> Prevent burnout and knowledge loss in your key contributors.

Analyzes workload patterns, off-hours activity, on-call burden, and stress signals. Provides early warning and intervention recommendations.

## Usage Examples

### Am I a Tiger?

```
You: Am I a tiger on this team?

Claude: I'll help you figure that out. Let me start by asking:
What do you actually spend your time on in a typical week -
not your job title, the actual work?
```

> **See a real conversation**: [Full test run transcript](https://gisthost.github.io/?bda76c838b3cb0786333867f96bd0a52/index.html) | [Annotated analysis](examples/test-runs/am-i-a-tiger-test-run.md)

### Tiger Team Identifier

```
You: Help me identify the tiger teams in my org

Claude: Let's start with a concrete situation. Tell me about
the last real emergency in your organization - something that
was genuinely high-stakes - and who handled it.
```

### Map Audit

```
You: I want to audit our engineering velocity dashboard

Claude: Let's dig in. What is this dashboard called,
and what does it claim to measure?
```

## Data Source Configuration

Set environment variables for the integrations you want to use:

```bash
# GitHub
export GITHUB_TOKEN=your_github_pat

# Slack
export SLACK_BOT_TOKEN=xoxb-...
export SLACK_TEAM_ID=T...

# Jira
export JIRA_URL=https://your-company.atlassian.net
export JIRA_EMAIL=your-email@company.com
export JIRA_API_TOKEN=your_api_token

# Linear
export LINEAR_API_KEY=lin_api_...

# Notion
export NOTION_API_KEY=secret_...

# PagerDuty
export PAGERDUTY_API_TOKEN=your_token

# Google (for Drive and Calendar)
export GOOGLE_CLIENT_ID=...
export GOOGLE_CLIENT_SECRET=...
export GOOGLE_REFRESH_TOKEN=...
```

Skills work without data sources (using conversational exploration), but get significantly better with access to real data.

## Philosophy

This toolkit is based on several key ideas:

1. **Tiger teams are the real production engine** - Small groups of trusted people with shared context produce more value than large formal structures

2. **AI as historian, not bureaucrat** - Use AI to reconstruct what happened after messy work is done, not to dictate structure from above

3. **Legibility should follow work** - Make work visible to leadership without strangling the people doing it

4. **Protect fast paths** - Don't stuff everything into controlled pipelines; let teams spike on problems

5. **Measure outcomes, not adherence** - Track what teams deliver, not whether they followed an AI-generated plan

## Contributing

Contributions welcome! See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines.

## Acknowledgements

This project was inspired by the YouTube video **["The Fork Most Leaders Don't See: Visibility vs. Execution"](https://www.youtube.com/watch?v=s1eqzfXCgXI)** by Nate Jones, which articulates the critical difference between "magnifying-glass companies" (using AI for surveillance) and "tiger-team companies" (using AI for execution power).

### AI-Generated Project

**All code and documentation in this project were generated by Claude Code using Anthropic's Claude Opus 4.5 model.**

The product specification ([docs/SPEC.md](docs/SPEC.md)) was developed through an interactive interview process using Claude Code's `AskUserQuestion` tool, which gathered requirements about:
- Target audience and roles
- Problems to address
- Product form and distribution
- Data sources and integrations
- Design philosophy

This demonstrates how AI can assist in the entire product development lifecycle - from requirements gathering through implementation and documentation.

## Credits

- **Conceptual Framework**: [Nate Jones](https://natesnewsletter.substack.com/) - "The Visibility Trap" and prompts for making messy work legible
- **Original Video**: ["The Fork Most Leaders Don't See: Visibility vs. Execution"](https://www.youtube.com/watch?v=s1eqzfXCgXI)
- **Development Platform**: [Claude Code](https://claude.ai/code) by Anthropic
- **AI Model**: Claude Opus 4.5 (`claude-opus-4-5-20251101`)
- **Integration Protocol**: [Model Context Protocol (MCP)](https://modelcontextprotocol.io/)

## License

MIT
