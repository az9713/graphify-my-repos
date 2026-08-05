---
repo: agents-five-question-filter
description: Analysis, prompt docs, and adversarial critique of the 5-question AI agent launch filter framework
language: None
stars: 0
forks: 0
created: 2026-04-29
updated: 2026-04-29
topics: 
is_fork: False
kb: 15
---

# agents-five-question-filter
# The Five-Question Agent Filter

Analysis, critique, and prompt documentation based on Nate's framework for cutting through AI agent launch noise.

> **Source video:** [Salesforce Killed The Browser. Every Agent Runs Your CRM Now.](https://www.youtube.com/watch?v=dQK_pTXrGDk&t=975s)
> **Source Substack:** [The 5-question filter I run every agent launch through](https://natesnewsletter.substack.com/p/the-5-question-filter-i-run-every)

---

## The Core Idea

The AI agent conversation has shifted from **model quality → infrastructure**. Most agent launches fail a simple five-question filter. The teams pulling ahead aren't chasing benchmarks — they're building routing judgment to assign work to the right layer.

### The Five-Question Filter

| # | Question | What It Tests |
|---|----------|---------------|
| 1 | Does it plug into tools my team already uses? | Migration cost |
| 2 | Does it let other agents build on top? | Open vs. closed |
| 3 | Does it own or access data I care about? | Data fabric match |
| 4 | Is there an ecosystem forming around it? | Longevity signal |
| 5 | Can I stack my agents on top? | Multiplier vs. adder |

---

## Contents

### [`report_summary.md`](report_summary.md)
High-signal summary of the video and Substack post. Covers:
- The five-question filter with scoring criteria
- All five launches scored: ChatGPT Workspace Agents, Salesforce Headless 360, Microsoft Copilot Wave 3, Kimi K2.6, Perplexity Personal Computer
- Anthropic's three distribution shapes (direct / embedded / managed)
- The layering-vs-switching framework
- Full routing table by work type

### [`report_prompts.md`](report_prompts.md)
What / why / how breakdown of the three reusable prompts from Nate's prompt kit:
- **Prompt 1 — Launch Filter:** Scores any agent launch against the five questions in ~2 minutes
- **Prompt 2 — License Spend Audit:** Audits current AI tool spend against actual work patterns; produces a CIO/CFO memo
- **Prompt 3 — Layering Audit:** Builds a routing decision tree for sharing with your team in Slack or Notion

### [`report_critique.md`](report_critique.md)
Adversarial critique with justifications and proposed solutions. Seven charges:
1. Pro-Anthropic framing without disclosure
2. Prompt 1 has a literal bug (Question 5 missing from analysis instructions)
3. No cost/exit dimension in the filter
4. Layering framework underestimates ongoing maintenance overhead
5. Infrastructure/feature binary ignores trajectory
6. Data residency scrutiny applied asymmetrically
7. No falsifiable predictions

Each critique includes a proposed fix or new feature.

---

## Quick Routing Reference

| Work Type | Right Tool |
|-----------|-----------|
| Recurring team workflows in Slack/ChatGPT | ChatGPT Workspace Agents |
| CRM data, RevOps, Salesforce-native | Salesforce Headless 360 / Agentforce |
| M365-native: Excel, Outlook, SharePoint, Teams | Copilot Cowork + Work IQ |
| Frontier agents, self-hosted, open weights | Kimi K2.6 or Qwen 3.6 |
| Research-heavy → polished artifact | Perplexity Personal Computer |
| Coding, reasoning, custom agent logic | Claude direct / Claude Code |

---

*Analysis generated April 29, 2026.*
