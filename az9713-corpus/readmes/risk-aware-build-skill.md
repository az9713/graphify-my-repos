# Risk-Aware Build Skill

`risk-aware-build` is a Codex skill for turning uncertain software work into a staged, evidence-backed implementation workflow. It helps agents discover unknowns, surface human-sensitive decisions, plan safely, track implementation deviations, verify with evidence, and prepare review handoffs.

Project description: A Codex skill that turns unknowns, implementation risk, and review readiness into durable AI development artifacts.

The project was inspired by Thariq's X post, ["A Field Guide to Fable: Finding Your Unknowns"](https://x.com/trq212/article/2073100352921215386), which argues that stronger agentic coding models make unknown discovery more important, not less. The skill packages that idea as an operating-system-style workflow: one router, one artifact contract, and reusable `ai/*.md` templates rather than eleven disconnected skills.

## Contents

- `risk-aware-build/` - the installable Codex skill
- `risk-aware-build-onboarding.md` - onboarding and usage examples
- `risk-aware-build-development-journey.md` - development rationale and future work

## Basic Usage

Invoke the skill directly in Codex:

```text
Use $risk-aware-build to do a blindspot pass before implementing this feature.
```

The skill creates or updates durable project artifacts such as `ai/01_unknowns.md`, `ai/03_tweakable_plan.md`, `ai/05_implementation_notes.md`, and `ai/06_verification.md` so each phase can feed the next.
