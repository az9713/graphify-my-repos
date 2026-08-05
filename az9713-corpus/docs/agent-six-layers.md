---
repo: agent-six-layers
description: Solo builder project proposals for the six-layer AI agent infrastructure stack
language: None
stars: 0
forks: 0
created: 2026-04-06
updated: 2026-04-07
topics: 
is_fork: False
kb: 128
---

# agent-six-layers
# Agent Infrastructure Stack — Solo Builder Project Proposals

> Based on Nate's six-layer agent infrastructure framework (Apr 2026)

A collection of project proposals, architectural deep dives, and implementation plans for building on the emerging AI agent infrastructure stack. All projects are scoped for solo builders and grounded in open source tools.

---

## Documentation

Full documentation lives in [`docs/`](./docs/index.md).

| Section | Description |
|---------|-------------|
| [What is this?](./docs/overview/what-is-this.md) | The Agent Runtime concept and why it exists |
| [Key concepts](./docs/overview/key-concepts.md) | Glossary of every important term |
| [Quickstart](./docs/getting-started/quickstart.md) | Working in under 15 minutes |
| [Onboarding](./docs/getting-started/onboarding.md) | Zero-to-hero for newcomers |
| [Six-layer framework](./docs/concepts/six-layer-framework.md) | Full framework with durability ratings |
| [agent.yaml reference](./docs/reference/agent-yaml.md) | Complete config field reference |
| [System design](./docs/architecture/system-design.md) | Architecture, data flow, event log schema |
| [Project proposals](./docs/projects/overview.md) | All 12 projects + 3-product consolidation |
| [Open source audit](./docs/reference/open-source-components.md) | Which components are OSS vs. commercial |

---

## The Six Layers at a Glance

| Layer | What it covers | Durability | Key open source tools |
|-------|---------------|------------|-----------------------|
| L1: Compute & Sandboxing | Isolated agent execution | High | E2B, Daytona, Browserbase |
| L2: Identity & Communication | Agent identity, auth | Medium | AgentMail, MCP |
| L3: Memory & State | Cross-session agent memory | Uncertain | Mem0 |
| L4: Tool Access & Integration | SaaS integrations, tool calls | High (near-term) | Composio, MCP |
| L5: Provisioning & Billing | Agent-speed provisioning, budgets | High | Stripe Projects |
| L6: Orchestration & Coordination | Multi-agent lifecycle, supervision | Critical gap | LangChain, CrewAI, AutoGen |

---

## The Single 6-Layer Product: Agent Runtime

One product, one config file (`agent.yaml`), all six layers.

```yaml
agent:
  name: research-agent
  identity:
    provider: agentmail
    address: research@agents.yourdomain.com
  compute:
    default: ephemeral
    when_stateful: persistent
    when_web: browser
  memory:
    backend: mem0
    portable: true
  tools:
    provider: composio
    integrations: [slack, github, google-workspace]
  billing:
    monthly_ceiling_usd: 50.00
    per_run_ceiling_usd: 2.00
  orchestration:
    supervision:
      eval_method: llm_judge
      score_floor: 0.7
      on_failure: retry_with_correction
```

See [system design](./docs/architecture/system-design.md) for the full technical blueprint.

---

## Source

Framework by [Nate Jones](https://natesnewsletter.substack.com) — *Your AI Agent Depends on Six Layers — Here's Which Ones Won't Last* (Apr 2026)
