# idea-to-capital

> A Claude Code plugin that tries to bottle the "make Claude make you money" workflow — for fun. 🪙

## Where this came from

This plugin is a **for-fun attempt to capture the workflow Nate Herk demos** in his video:

**▶️ [I asked Claude Code to make me as much money as possible](https://www.youtube.com/watch?v=iTY8Q449YNQ)** — by [Nate Herk](https://www.youtube.com/@NateHerk).

All credit for the underlying ideas goes to Nate. He's the one who laid out the four upgrades; this repo just wires them into a single Claude Code plugin so you can run them as commands instead of remembering the recipe. If you like the workflow, **go watch the original video and support the creator** — this is a fan project, not an official anything.

The four upgrades from the video, roughly:

1. **Stop Claude from being a yes-man** → an adversarial *council* roasts your idea before you build.
2. **Build, then verify** → make Claude check and stress-test its own work instead of just claiming it's done.
3. **Beat context rot** → clean handoffs and resets so Claude stays sharp.
4. **Stop being the bottleneck** → parallel subagents and goal-driven loops.

## What it actually does

It is **not** a "type idea, receive money" magic button. It's a disciplined build-and-business loop:

```text
Idea → buyer pain → offer → minimal build → verification → break test → packaging → reusable asset
```

The whole point is to kill bad ideas *before* you spend a weekend building them.

## What's inside

```text
idea-to-capital/
├── .claude-plugin/plugin.json
├── skills/
│   ├── opportunity-triage/      # is this even worth looking at?
│   ├── buyer-validation/        # will anyone actually pay?
│   ├── offer-shaper/            # turn it into a sellable offer
│   ├── profitable-build-spec/   # smallest thing worth building
│   ├── verification-harness/    # prove it works, don't assert it
│   ├── break-test/              # try to break it on purpose
│   ├── context-reset/           # clean handoffs, no context rot
│   ├── asset-packager/          # make it reusable
│   └── council-session/         # the full adversarial roast
├── agents/                      # the council personas
│   ├── buyer-skeptic.md
│   ├── cfo-skeptic.md
│   ├── technical-architect.md
│   ├── distribution-operator.md
│   ├── verification-red-teamer.md
│   ├── packaging-strategist.md
│   └── market-researcher.md
├── commands/
│   ├── triage.md
│   ├── validate.md
│   ├── offer.md
│   ├── build-plan.md
│   ├── verify.md
│   ├── break.md
│   ├── package.md
│   └── council.md
├── hooks/hooks.example.json
├── scripts/
└── templates/
```

## Install / test locally

From the parent directory containing this plugin folder:

```bash
claude --plugin-dir ./idea-to-capital
```

Then try:

```text
/idea-to-capital:triage AI dashboard for local dental clinics
/idea-to-capital:validate weekly revenue leak report for Shopify stores
/idea-to-capital:offer AI ops assistant for solo law firms
/idea-to-capital:build-plan client reporting automation for accountants
/idea-to-capital:verify
/idea-to-capital:break
/idea-to-capital:package
/idea-to-capital:council build an AI tutor for retired engineers learning physics
```

Plugin commands are namespaced by the plugin name, so they appear as `/idea-to-capital:<command>`.

## Recommended first use

Run this in a real repo or empty project folder:

```text
/idea-to-capital:council I want to build a solo AI product that can become a small cash-flowing business within 30 days.
```

Then let the plugin march the idea through:

1. opportunity triage
2. buyer validation
3. offer shaping
4. minimal build spec
5. implementation verification
6. break testing
7. asset packaging

## Hook policy

Hooks ship as **opt-in templates only**. Active hooks can block tool use or run commands automatically, so nothing is enabled by default.

To enable them, copy:

```text
hooks/hooks.example.json → hooks/hooks.json
```

Then inspect the scripts under `scripts/` and adapt the command names for your OS and repo.

## Files the plugin may create in your project

The skills write durable project state into:

```text
docs/profit/current-opportunity.md
docs/profit/buyer-validation.md
docs/profit/offer.md
docs/profit/build-spec.md
docs/profit/verification-report.md
docs/profit/break-test-report.md
docs/profit/asset-package.md
docs/profit/decision-log.md
docs/profit/next-actions.md
```

## The one operating rule

Never build because an idea is interesting. Build only when there's a concrete buyer, urgent pain, a reachable channel, a fast validation path, and a verification plan.

## Credits & license

- **Workflow & inspiration:** [Nate Herk — "I asked Claude Code to make me as much money as possible"](https://www.youtube.com/watch?v=iTY8Q449YNQ)
- **This plugin:** a community fan project, built for fun. Not affiliated with or endorsed by Nate Herk or Anthropic.
- **License:** MIT
