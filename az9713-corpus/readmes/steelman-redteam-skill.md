# steelman-redteam

A Claude Code skill that subjects any claim, idea, or proposal to a rigorous four-argument dialectical analysis and synthesizes a final verdict.

## What it does

Given a claim like *"raising the minimum wage to $25/hour would help low-income workers"*, the skill runs five steps:

1. **Steelman the claim** — builds the strongest possible version of the original argument, better than the user put it
2. **Red-team the steelman** — attacks that best version, finding genuine vulnerabilities (not strawmen)
3. **Steelman the counter-claim** — constructs the strongest affirmative case for the opposite position
4. **Red-team the counter-claim's steelman** — attacks that with equal rigor
5. **Synthesis** — extracts the strongest signal from all four arguments, names contradictions if they exist, explains the reasoning chain, and delivers a verdict

The skill resists the natural pull toward one-sided thinking. Both sides get steelmanned as if genuinely believed, and red-teamed as if you were trying to demolish them.

## Installation

Copy `SKILL.md` into your Claude Code skills directory:

```
~/.claude/skills/steelman-redteam/SKILL.md
```

Or clone this repo and symlink/copy it in.

## Usage

Just describe your claim and invoke the skill:

> `steelman and red team this: [your claim]`
> `evaluate this proposal: [idea]`
> `is X a good idea?`

The skill also triggers automatically when you share a position and clearly want adversarial analysis rather than validation.

## Evaluation results

Benchmarked against Claude without the skill on three test cases (minimum wage policy, social media and teen mental health, annual performance reviews):

| Configuration | Pass rate |
|---|---|
| With skill | **100%** |
| Without skill | 34% |

Without the skill, Claude defaults to a two-part structure (steelman + red-team) and skips the second half of the dialectic entirely — no counter-claim steelman, no red-team of the counter-claim. The skill enforces the full four-argument structure every time.

Full evaluation outputs and grading are in [`workspace/iteration-1/`](workspace/iteration-1/).

## Output format

```
## Steelman: [the claim]
...

## Red Team: Against the Steelman
...

## Steelman: [the counter-claim]
...

## Red Team: Against the Counter-Claim's Steelman
...

## Synthesis
...
```
