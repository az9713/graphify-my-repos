---
repo: saga-lite
description: A multi-agent goal-evolving framework for code and prompt optimization
language: Python
stars: 1
forks: 0
created: 2025-12-31
updated: 2026-01-01
topics: 
is_fork: False
kb: 15945
---

# saga-lite
# SAGA-Lite

> **Note:** This project is under active development. APIs and features may change.

A multi-agent goal-evolving framework for code and prompt optimization, inspired by the [SAGA (Scientific Autonomous Goal-evolving Agent)](https://arxiv.org/pdf/2512.21782) research paper.

## What is SAGA-Lite?

SAGA-Lite implements a **bi-level optimization architecture** where AI agents don't just optimize solutions—they also evolve the objectives themselves to avoid "reward hacking" (when AI finds loopholes in scoring functions).

```
┌─────────────────────────────────────────────────────────────────┐
│                        OUTER LOOP                                │
│                   (Objective Evolution)                          │
│  ┌──────────┐    ┌─────────────┐    ┌───────────┐               │
│  │ ANALYZER │───►│   PLANNER   │───►│IMPLEMENTER│               │
│  └────▲─────┘    └─────────────┘    └─────┬─────┘               │
│       │                                    │                     │
│       │         objectives.json            ▼                     │
│       │        ┌───────────────┐    ┌───────────┐               │
│       │        │  Objectives   │◄───│  Scorers  │               │
│       │        │  & Weights    │    │  (Python) │               │
│       │        └───────┬───────┘    └───────────┘               │
│       │                │                                         │
│  ┌────┴────────────────▼────────────────────────┐               │
│  │              INNER LOOP                       │               │
│  │           (Solution Optimization)             │               │
│  │  ┌───────────┐                               │               │
│  │  │ OPTIMIZER │  Generates & evolves          │               │
│  │  │           │  candidate solutions          │               │
│  │  └───────────┘                               │               │
│  └──────────────────────────────────────────────┘               │
└─────────────────────────────────────────────────────────────────┘
```

## The Four Agents

| Agent | Role | What It Does |
|-------|------|--------------|
| **Planner** | Strategist | Translates goals into computable objectives with weights |
| **Implementer** | Builder | Writes Python scoring functions for each objective |
| **Optimizer** | Explorer | Generates and evolves candidate solutions (inner loop) |
| **Analyzer** | Critic | Detects reward hacking, suggests objective refinements |

## Three Autonomy Modes

| Mode | Human Involvement | Use Case |
|------|-------------------|----------|
| **Autopilot** | None | High-throughput screening, well-understood problems |
| **Semi-pilot** | Reviews Analyzer output | Clear strategy, validation at checkpoints |
| **Co-pilot** | Reviews Planner + Analyzer | Frontier problems, maximum control |

## Quick Start

```bash
# Install
pip install -e ".[dev]"

# Copy example
cp -r examples/prompt_optimization my_task/

# Edit configuration
vim my_task/config.yaml  # Set your LLM API keys
vim my_task/task.yaml    # Define your optimization goal

# Run SAGA-Lite
saga run my_task/config.yaml
```

## Supported LLM Providers

- **Anthropic** (Claude)
- **OpenAI** (GPT-4)
- **Google** (Gemini)
- **Ollama** (Local models)

Configure per-agent or use a default for all:

```yaml
llm:
  default:
    provider: anthropic
    model: claude-sonnet-4-20250514
  agents:
    optimizer:
      provider: ollama
      model: llama3  # Use fast local model for many iterations
```

## Documentation

| Document | Description |
|----------|-------------|
| [Getting Started](docs/GETTING_STARTED.md) | Installation and first run |
| [Architecture](docs/ARCHITECTURE.md) | Technical deep-dive |
| [Development Guide](docs/DEVELOPMENT_GUIDE.md) | Contributing and development workflow |
| [Glossary](docs/GLOSSARY.md) | Terms explained for traditional programmers |
| [Design Document](docs/plans/2025-12-30-saga-lite-design.md) | Original design decisions |
| [Implementation Plan](docs/plans/2025-12-30-saga-lite-implementation.md) | 16-task build plan |

## Project Structure

```
saga_lite/
├── saga/
│   ├── agents/           # The four SAGA agents
│   │   ├── planner.py
│   │   ├── implementer.py
│   │   ├── optimizer.py
│   │   └── analyzer.py
│   ├── llm/              # LLM provider abstractions
│   ├── domains/          # Domain-specific helpers
│   └── orchestrator.py   # Main loop coordination
├── examples/
│   └── prompt_optimization/
├── tests/
└── runs/                 # Output from optimization runs
```

## Research Background

This project implements concepts from:

- **SAGA Paper**: [Accelerating Scientific Discovery with Autonomous Goal-evolving Agents](https://arxiv.org/pdf/2512.21782)
- **Authors**: Yuanqi Du, Botao Yu, Tianyu Liu, et al. from Cornell, Ohio State, Yale, EPFL, UC Berkeley, and others

## Development

This project was developed using [Claude Code](https://claude.com/claude-code) with the [Superpowers plugin](https://github.com/obra/superpowers).

See [Development Guide](docs/DEVELOPMENT_GUIDE.md) for the complete development workflow.

## License

MIT License - See LICENSE file for details.
