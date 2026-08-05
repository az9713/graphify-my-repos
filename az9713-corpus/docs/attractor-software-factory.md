---
repo: attractor-software-factory
description: Attractor software factory - clone of strongdm/attractor with implementation, 5 new DOT pipelines, and extensive documentation
language: Python
stars: 2
forks: 1
created: 2026-02-20
updated: 2026-06-03
topics: 
is_fork: False
kb: 416
---

# attractor-software-factory
# Attractor Software Factory

> **This project is a clone of [strongdm/attractor](https://github.com/strongdm/attractor).** We added extensive documentation and 5 new DOT pipeline blueprints to explain and demonstrate the software factory concept. Inspired by Simon Willison's blog post [How StrongDM's AI team build serious software without even looking at the code](https://simonwillison.net/2026/Feb/7/software-factory/).

---

This repository contains [NLSpecs](#terminology) to build your own version of Attractor to create your own software factory.

Although bringing your own agentic loop and unified LLM SDK is not required to build your own Attractor, we highly recommend controlling the stack so you have a strong foundation.

## Specs

- [Attractor Specification](./attractor-spec.md)
- [Coding Agent Loop Specification](./coding-agent-loop-spec.md)
- [Unified LLM Client Specification](./unified-llm-spec.md)

## Building Attractor

Supply the following prompt to a modern coding agent (Claude Code, Codex, OpenCode, Amp, Cursor, etc):

```
codeagent> Implement Attractor as described by https://factory.strongdm.ai/
```

## Example Pipelines

Once built, the same factory runs any `.dot` blueprint. Each produces different artifacts:

| Blueprint | What It Builds | Key Output Files |
|-----------|---------------|-----------------|
| `add-login.dot` | Login page with validation | `login.html`, `styles.css`, `login.js` |
| `build-rest-api.dot` | Task management REST API | `server.py`, `models.py`, `validators.py` |
| `build-cli-tool.dot` | File organizer CLI | `organize.py`, `classifier.py`, `mover.py` |
| `build-landing-page.dot` | Product landing page | `index.html`, `styles.css`, `app.js` |
| `build-data-pipeline.dot` | CSV-to-dashboard pipeline | `pipeline.py`, `analyzer.py`, `report.py` |
| `build-static-site-generator.dot` | Markdown-to-HTML site generator | `ssg.py`, `parser.py`, `theme.css` |

```bash
# Same factory, different blueprints, different outputs
python your_engine.py add-login.dot
python your_engine.py build-rest-api.dot
python your_engine.py build-cli-tool.dot --provider openai --model gpt-4o
python your_engine.py build-landing-page.dot --dry-run --auto-approve
```

See [The Software Factory](./docs/software-factory.md) for the concept and
[docs/](./docs/) for full documentation.

## Terminology

- **NLSpec** (Natural Language Spec): a human-readable spec intended to be  directly usable by coding agents to implement/validate behavior.
