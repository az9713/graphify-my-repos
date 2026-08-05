---
repo: personal-strategy-system
description: A markdown-based personal strategy system using AI as an adversarial coach. Inspired by Evan Armstrong's 'New Year, New AI, New Me'.
language: None
stars: 0
forks: 0
created: 2025-12-31
updated: 2026-01-01
topics: 
is_fork: False
kb: 42
---

# personal-strategy-system
# Personal Strategy System

A markdown-based personal strategy system that uses AI as a **Cognitive Decoupling Agent** to engineer identity change.

---

## Support the Original Creator

> **This project is inspired by Evan Armstrong's brilliant article [New Year, New AI, New Me](https://substack.com/@evanarmstrong/p-183070315).**
>
> If you find this system valuable, please:
> 1. **[Read the original article](https://substack.com/@evanarmstrong/p-183070315)** - it explains the psychology and philosophy behind this approach
> 2. **[Subscribe to The Leverage](https://www.theleverage.ai/)** - Evan's newsletter on AI, business, and strategy
> 3. **Share his work** - help others discover the source material
>
> This open-source implementation exists to make the system accessible, not to replace the insights in the original article.

---

## Documentation

| Document | Description |
|----------|-------------|
| **[QUICKSTART.md](QUICKSTART.md)** | Get started in 5 minutes + 10 use cases to try |
| **[User Guide](docs/USER_GUIDE.md)** | Complete user manual (no technical experience required) |
| **[Developer Guide](docs/DEVELOPER_GUIDE.md)** | For contributors and future developers |
| **[CLAUDE.md](CLAUDE.md)** | Project context for Claude Code |
| **[PROTOCOLS.md](PROTOCOLS.md)** | Detailed reference for all 7 protocols |

---

## Quick Start

**New here?** See [QUICKSTART.md](QUICKSTART.md) for a 5-minute introduction with 10 practical use cases.

### 1. Initial Setup (2 minutes)

The folder structure is already created:
```
personal-strategy/
├── README.md              ← You are here
├── QUICKSTART.md          ← Start here! 5-minute guide
├── SYSTEM.md              ← Copy this into your AI first
├── PROTOCOLS.md           ← Reference (don't copy into AI)
├── CLAUDE.md              ← For Claude Code users
├── docs/
│   ├── USER_GUIDE.md      ← Complete user manual
│   └── DEVELOPER_GUIDE.md ← For contributors
├── examples/
│   └── protocol-a-transcript.md  ← Example conversation
├── quarterly/             ← Save quarterly sessions here
├── weekly/                ← Save weekly check-ins here
├── patterns.md            ← AI-identified patterns
└── archive/               ← Completed quarters
```

### 2. Start Your First Quarter (Protocol A)

1. Open Claude, ChatGPT, or your preferred LLM
2. **Copy the entire contents of `SYSTEM.md`** into the system prompt or first message
3. Say: **"Protocol A. Let's plan my quarter."**
4. Have a 20-30 minute **conversation** (~15-18 exchanges)
5. After the conversation, save your notes to `quarterly/2026-Q1.md`

**What to expect:** Each AI response starts with a phase tag like **[IDENTITY]** or **[GOALS]**. The conversation moves through 5 phases and ends with a summary you confirm.

### 3. Weekly Check-ins (Protocol B)

Every week (5 minutes):
1. Open your AI with `SYSTEM.md` as context
2. Paste your recent check-ins if you have them
3. Say: **"Protocol B. Weekly check-in."**
4. Answer the AI's questions
5. Save to `weekly/2026-WNN.md`

### 4. Monthly Pattern Analysis (Protocol C)

Every 4-6 weeks:
1. Open your AI with `SYSTEM.md`
2. **Include your last 4-6 weekly check-ins** in the context
3. Say: **"Protocol C. What patterns do you see?"**
4. Update `patterns.md` with findings

---

## The Seven Protocols

| Protocol | Trigger | Duration | Purpose |
|----------|---------|----------|---------|
| **A** | `Protocol A. Let's plan my quarter.` | 20-30 min | Initialize goals |
| **B** | `Protocol B. Weekly check-in.` | 5 min | Track execution |
| **C** | `Protocol C. What patterns do you see?` | 15-20 min | Pattern recognition |
| **D** | `Protocol D. I've derailed.` | 20-30 min | Crisis recovery |
| **E** | `Protocol E. Year in review.` | 60-90 min | Annual identity review |
| **F** | `Protocol F. Should I change course?` | 15-20 min | Mid-quarter pivot |
| **G** | `Protocol G. I achieved [goal].` | 10-15 min | Success analysis |

See `PROTOCOLS.md` for detailed flows.

---

## How Conversations Should Work

**WRONG:**
You: "Protocol A"
AI: *dumps a 500-word response with 5 questions, a template, and a checklist*

**RIGHT:**
You: "Protocol A. Let's plan my quarter."
AI: "What do you want to be different about yourself by the end of this quarter?"
You: "I want to be more disciplined about my health."
AI: "That's vague. What would 'disciplined about health' look like on a random Tuesday at 3pm?"
You: "I'd be eating a healthy lunch instead of fast food."
AI: "What's stopped you from doing that before now?"

*...and so on, one question at a time.*

---

## Core Philosophy

> "You are NOT a therapist or cheerleader. You are an **adversarial interlocutor** whose job is to stress-test goals, dismantle rationalizations, and optimize for probability of success."

The AI applies:
- **Karl Popper's Falsificationism** - Seek evidence that disproves your plans
- **Stoic Negative Visualization** - What could go wrong?
- **Cognitive Bias Detection** - Call out vague excuses by name

---

## Troubleshooting

**Problem:** AI dumps everything at once
**Solution:** Make sure you copied SYSTEM.md correctly, especially the "CRITICAL: Conversation Rules" section

**Problem:** AI is too nice
**Solution:** The AI should be adversarial. If it's being a cheerleader, remind it: "You're supposed to challenge me, not agree with me."

**Problem:** Conversation drags on forever
**Solution:** Each response should start with a phase tag like **[IDENTITY]**. If the AI isn't tagging, remind it: "Start each response with the phase tag." If stuck in one phase too long, say: "Move to the next phase."

**Problem:** AI not showing phase tags
**Solution:** Say: "Remember to tag each response with the current phase: [IDENTITY], [GOALS], [TRADE-OFFS], [STRESS-TEST], or [COMMIT]"

For more troubleshooting help, see the [User Guide](docs/USER_GUIDE.md#10-troubleshooting).

---

## Learn More

- **First time?** Start with [QUICKSTART.md](QUICKSTART.md) - 5 minutes to get started
- **Need help?** See the complete [User Guide](docs/USER_GUIDE.md)
- **Want to contribute?** Read the [Developer Guide](docs/DEVELOPER_GUIDE.md)
- **Using Claude Code?** See [CLAUDE.md](CLAUDE.md) for project context

---

## Acknowledgements

- **Inspiration**: This application is inspired by [New Year, New AI, New Me](https://substack.com/@evanarmstrong/p-183070315) by Evan Armstrong
- **Development**: All code and documentation were generated by [Claude Code](https://claude.ai/claude-code) powered by [Opus 4.5](https://www.anthropic.com/claude)
- **Brainstorming**: [Gemini 3.0](https://deepmind.google/technologies/gemini/) helped in brainstorming the protocol structure

---

## License

This project is provided as-is for personal use. See the original article for attribution.
