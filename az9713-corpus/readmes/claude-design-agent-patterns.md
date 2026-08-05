# Claude Design Agent Patterns

A summary of the six-pattern vertical-agent architecture behind Claude Design, based on the YouTube video **[Inside Claude's Design Agents](https://www.youtube.com/watch?v=V-djAkt0t-M&t=140s)**. Patterns extracted by **ChatGPT Thinking 5.5 Extended**.

## The Six Patterns

1. **Agentic context grounding** — the agent anchors itself to a source of truth before generating anything
2. **Structured memory** — reusable memory artifacts built from that grounded context
3. **Iterative refinement loop** — user feedback drives successive generations
4. **Self-QA / reflection loop** — the agent critiques its own output before surfacing it
5. **Multi-variation generation** — parallel variants along key decision axes
6. **Handoff pattern** — clean handoff between sub-agents or to the user

## Contents

- [`claude_design_agent_patterns.md`](claude_design_agent_patterns.md) — full pattern writeup with workflow diagrams and analysis
