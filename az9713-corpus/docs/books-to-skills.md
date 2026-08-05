---
repo: books-to-skills
description: Turn books into Claude skills. 6 habit PDFs → 3 skills via skills-from-sources.
language: Python
stars: 1
forks: 1
created: 2026-04-07
updated: 2026-07-09
topics: 
is_fork: False
kb: 26199
---

# books-to-skills
# Books to Skills

Turn books, PDFs, articles, and videos into reusable Claude skills — automatically.

> Inspired by ["Connect Claude To Top Thinkers (1 Book = 5 Skills)"](https://www.youtube.com/watch?v=wVxTF4di2tc)

---

## What this is

This repo demonstrates how to extract Claude skills from source materials. Starting from 6 habit-formation PDFs (Atomic Habits, Tiny Habits, Mini Habits, and more), a meta-skill called `skills-from-sources` reads, understands, and synthesizes the content into ready-to-use Claude skills.

**One session. Six books. Three skills built.**

---

## Skills created

### `habit-designer`
Design a new habit that actually sticks. Synthesizes the three major habit frameworks:
- **Atomic Habits** (James Clear) — Four Laws of Behavior Change + the cue→craving→response→reward loop
- **Tiny Habits** (BJ Fogg) — anchor recipe: "After I [existing behavior], I will [new behavior]"
- **Mini Habits** (Stephen Guise) — "too small to fail" minimums that bypass psychological resistance

Tell Claude what habit you want to build. It asks a couple of questions about your daily routine, then delivers a complete recipe: a specific minimum, an anchor, environmental cues, and an immediate reward.

### `habit-audit`
Diagnose why an existing habit keeps failing. Uses the Four Laws as a diagnostic lens — every habit failure maps to one (or more) violated laws. Give Claude your current routine and what's not working; it returns a structured report with one clear fix per habit.

### `wellness-micro-habits`
A curated catalog of 60+ wellness micro-habits (sleep, energy, stress, nutrition, movement, focus) plus a personalized three-habit starter pack. Built from *21 Micro Habits to Improve Wellness* and *MicroHabits: Small Changes & Big Results*.

---

## The meta-skill: `skills-from-sources`

The fourth skill in this repo is the one that built the other three. It accepts any mix of:

| Input | How it's processed |
|-------|-------------------|
| PDF files | Extracted via PyMuPDF (`scripts/extract_content.py`) |
| URLs | Fetched with Claude's WebFetch tool |
| Text / Markdown | Read directly |
| Audio / Video | Requires a transcript file alongside the media |

It extracts, understands, identifies skill candidates, and builds proper skill directories — complete with `SKILL.md`, `references/`, and scripts where needed.

---

## How these skills were created

The three habit skills were built in a single Claude Code session using the `skills-from-sources` meta-skill. Here's exactly what happened:

### Step 1 — Provide the source materials

Six PDFs were placed in `docs/`. That's the entire input — no manual summarising, no copy-pasting.

### Step 2 — Extract and read the content

`skills-from-sources` ran `scripts/extract_content.py` (a bundled PyMuPDF script) on each PDF. For the 256-page *Atomic Habits*, it sampled representative sections — table of contents, core framework chapters, summaries — rather than reading every page.

### Step 3 — Understand each source

For each PDF, Claude identified:
- the **domain** (habit formation)
- the **core framework** (e.g. Four Laws, anchor recipe, too-small-to-fail minimum)
- the **key actionable concepts** a practitioner would use
- the **intended audience** (general public, self-improvement)

### Step 4 — Identify skill candidates

Looking across all six sources, Claude found that three books described *complementary* frameworks rather than competing ones:

| Framework | Core contribution |
|-----------|-----------------|
| Atomic Habits (Clear) | The complete behavioral model: cue→craving→response→reward, plus Four Laws for designing the environment |
| Tiny Habits (Fogg) | The practical attachment recipe: anchor an existing behavior, add the new one, celebrate |
| Mini Habits (Guise) | The psychological unlock: set a minimum so small it's impossible to fail |

These three fit together into one synthesis skill (`habit-designer`). The audit angle (diagnosing *why* habits fail) was distinct enough to become its own skill (`habit-audit`). The two catalog PDFs — lists of concrete wellness habits — formed a third (`wellness-micro-habits`). The newsletter was too thin for its own skill and was absorbed into the reference files.

### Step 5 — Write the skill files

For each skill, Claude created:

```
~/.claude/skills/<skill-name>/
├── SKILL.md              # YAML frontmatter (name + trigger description) + instructions
└── references/           # Domain content too large for SKILL.md
    └── <topic>.md
```

The `SKILL.md` frontmatter `description` field is the trigger mechanism — Claude reads it to decide when to apply the skill. Each description was written to be specific about both *what the skill does* and *which user phrases should activate it*.

### Step 6 — Skills are live immediately

Once written to `~/.claude/skills/`, the skills appear in every new Claude Code session with no further configuration. The entire process — from six raw PDFs to three working skills — took one session.

---

## Source materials

All PDFs are in `docs/`:

| File | Author | Core idea |
|------|--------|-----------|
| `atomic_habits_james_clear.pdf` | James Clear | Four Laws of Behavior Change |
| `Mini-Habits-Free-Chapter.pdf` | Stephen Guise | Too small to fail |
| `The-Official-Tiny-Habits-Toolkit-by-BJ-Fogg-Paperback-Edition.pdf` | BJ Fogg | Anchor + celebration recipe |
| `MicroHabits.pdf` | LivingLifeBlessed | Domain habit lists (health, finance, family, career, social) |
| `21-Micro-Habits-To-Improve-Wellness.pdf` | — | 21 wellness habits with explanations |
| `WBWH-Micro-Habits-Newsletter.pdf` | Chevalier College | Habit neuroscience primer |

---

## Project structure

```
.
├── README.md
├── SKILLS-GUIDE.md          # Full guide: creation process + usage examples
├── docs/                    # Source PDFs
└── .claude/
    └── skills/
        ├── skills-from-sources/   # Meta-skill: turns documents into skills
        ├── habit-designer/        # Design new habits using 3 frameworks
        ├── habit-audit/           # Diagnose failing habits
        └── wellness-micro-habits/ # Wellness habit catalog + starter packs
```

---

## How to use these skills

Install by copying `.claude/skills/` into your home directory:

```bash
cp -r .claude/skills/. ~/.claude/skills/
```

Then start a Claude Code session and the skills are immediately available. See [SKILLS-GUIDE.md](SKILLS-GUIDE.md) for full usage instructions and worked examples.

---

## Go deeper

- **Full usage guide with examples:** [SKILLS-GUIDE.md](SKILLS-GUIDE.md)
- **Inspiration:** [Connect Claude To Top Thinkers (1 Book = 5 Skills)](https://www.youtube.com/watch?v=wVxTF4di2tc)
- **Claude Code:** [claude.ai/code](https://claude.ai/code)
