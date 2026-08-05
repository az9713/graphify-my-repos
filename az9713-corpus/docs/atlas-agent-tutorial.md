---
repo: atlas-agent-tutorial
description: Tutorial edition of Atlas Agents with extensive documentation and an interactive course hub
language: Python
stars: 0
forks: 0
created: 2026-06-08
updated: 2026-06-08
topics: 
is_fork: False
kb: 239
---

# atlas-agent-tutorial
# Atlas Agents

Atlas Agents is a chapter-by-chapter Python example repository for learning how AI agents are built, extended, guarded, evaluated, and deployed. It starts with a raw ReAct loop and ends with a capstone autonomous engineering assistant built around LangGraph, Claude, tool execution, review, and human approval.

This tutorial edition is based on the original repository, [agulli/atlas-agents](https://github.com/agulli/atlas-agents). This version adds extensive tutorial documentation and an interactive HTML course hub for learners who want a guided path through the agent development journey.

## Interactive Course Hub

Open the learning hub:

- [View the live HTML course hub](https://az9713.github.io/atlas-agent-tutorial/docs/course/)
- [Open the local course file](docs/course/index.html)

The hub turns the repository into an end-to-end course with module navigation, progress tracking, search and filters, lab commands, knowledge checks, and links into the relevant docs and source files.

## Documentation

Start with the documentation hub:

- [Interactive course hub](docs/course/index.html)
- [Docs index](docs/index.md)
- [What this repo is](docs/overview/what-is-this.md)
- [Quickstart](docs/getting-started/quickstart.md)
- [Onboarding guide](docs/getting-started/onboarding.md)
- [Chapter and command reference](docs/reference/chapter-and-command-reference.md)

Recommended reading order:

1. [Interactive course hub](https://az9713.github.io/atlas-agent-tutorial/docs/course/)
2. [Onboarding](docs/getting-started/onboarding.md)
3. [Quickstart](docs/getting-started/quickstart.md)
4. [Key concepts](docs/overview/key-concepts.md)
5. [Agent patterns by chapter](docs/concepts/agent-patterns-by-chapter.md)
6. [Skills, tools, and safety](docs/concepts/skills-tools-and-safety.md)
7. [System design](docs/architecture/system-design.md)
8. [Chapter and command reference](docs/reference/chapter-and-command-reference.md)
9. [Common issues](docs/troubleshooting/common-issues.md)

## Fast Start

1. Create a virtual environment.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

2. Install the shared dependency set.

```powershell
python -m pip install -r requirements.txt
```

3. Copy the environment template and add at least one model provider key.

```powershell
Copy-Item .env.example .env
```

4. Run the first Atlas agent from the repository root.

```powershell
python ch01_react_from_scratch\atlas_v01.py "What is the Model Context Protocol?"
```

## Current Verification Notes

The docs were written from the current repository contents. There is no `TOC.md`, no package manifest, no test suite at the root, and no existing `docs/` directory before this documentation pass.

`python -m compileall -q .` passes after removing trailing literal `\n` artifacts from four online examples. See [common issues](docs/troubleshooting/common-issues.md) for remaining setup caveats.
