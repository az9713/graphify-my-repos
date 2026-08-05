# Council — Claude Code Skill for Multi-Model Second Opinions

Keep Claude Code as your daily driver while tapping into Gemini, GPT, Codex, DeepSeek, or any model on [OpenRouter](https://openrouter.ai) for second opinions. Right model, right task, right time.

## What It Does

Council routes specific questions to specialist AI models via OpenRouter, then Claude synthesizes the advice and implements the best approach. No app-switching, no copy-pasting between chat windows.

```
You:     /council audit this page — send frontend to Gemini, copy to Codex
Claude:  [packages context, calls both models]
Gemini:  "The grid breaks at 768px, spacing is inconsistent, add focus states..."
Codex:   "Headlines are generic, CTAs lack urgency, pricing copy buries the value..."
Claude:  "I agree with both on the high-priority items. Here's my plan..."
```

## Quick Start

### 1. Get an OpenRouter API key

Sign up at [openrouter.ai/keys](https://openrouter.ai/keys) and create a key.

### 2. Set your key

```bash
cp .env.example .env
# Edit .env and add your key:
# OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

### 3. Use it

Copy `.claude/skills/council/` into your project's `.claude/skills/` directory (or `~/.claude/skills/` for global access), then in Claude Code:

```
/council audit this app from a frontend and copy perspective
```

Or use natural language:

```
Get a second opinion on this bug
Ask Gemini to review the UI
What would GPT think about this schema?
```

## Default Model Routing

| Category | Model | When |
|---|---|---|
| Frontend/UI | Gemini 2.5 Pro | Layout, responsive design, CSS, visual hierarchy |
| Bug fixes | Codex | Debugging, error diagnosis, stuck-in-a-loop scenarios |
| Architecture | Claude Sonnet | System design, patterns, database schema |
| Copy/Content | Codex | Headlines, CTAs, tone, UX writing |
| Quick check | Gemini 2.5 Flash | Fast, cheap sanity checks |
| Refactoring | Claude Sonnet | Code cleanup, optimization, DRY |

All routing is configurable in `council_config.json`.

## Project Structure

```
.claude/skills/council/
├── SKILL.md              # Skill definition and instructions
├── council_config.json   # Model routing configuration
└── scripts/
    └── council.py        # OpenRouter API wrapper (zero dependencies)
```

## Requirements

- **Claude Code** — [claude.com/claude-code](https://claude.com/claude-code)
- **Python 3.7+** — no pip installs needed (stdlib only)
- **OpenRouter API key** — [openrouter.ai/keys](https://openrouter.ai/keys)

## Documentation

See [SETUP_GUIDE.md](SETUP_GUIDE.md) for the complete walkthrough:
- Step-by-step setup for beginners
- 5 detailed usage examples
- When to use Council (and when not to)
- Customization guide (add models, providers, categories)
- Troubleshooting every common error

## Example: Evaluating "Some Simple Economics of AGI"

The Council skill was used to evaluate the following sources on AGI economics:

1. YouTube video: [AI Just Gave You Superpowers — Now What?](https://www.youtube.com/watch?v=Rv3IqA4cLEk)
2. a16z crypto Substack: [AI just gave you superpowers — now what?](https://a16zcrypto.substack.com/p/ai-just-gave-you-superpowers-now)
3. arXiv paper: [Some Simple Economics of AGI](https://arxiv.org/pdf/2602.20946)

Gemini 2.5 Pro and GPT-4o were consulted in parallel, and Claude Opus 4.6 synthesized the results. See the full evaluations in [`AGI_economics/*.md`](AGI_economics/).

## Acknowledgments

1. This project was inspired by the YouTube video **"You've Never Seen Claude Code Skills Do This"** by Mark Kashef — [watch it here](https://www.youtube.com/watch?v=EeX7ovArylU&t=2s).

2. All code and documentation in this repository were created by **Claude Code** (powered by Claude Opus 4.6).

## License

MIT
