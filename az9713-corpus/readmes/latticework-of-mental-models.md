# Latticework of Mental Models

A comprehensive study of Charlie Munger's "latticework of mental models" concept — extended with Mohnish Pabrai's practical applications — compiled into a beautifully formatted, ~84-page PDF reference guide and article.

> **Inspired by:** [The Latticework of Mental Models For a Great Life!](https://www.youtube.com/watch?v=Z2J_8GHcrvQ&t=2269s) — Mohnish Pabrai's talk covering 150+ mental models drawn from Munger, Buffett, and his own investing career.

---

## What's Inside

### The PDF (`munger_latticework_mental_models.pdf`)

**Part I — The Reference Guide (~51 pages)**
A fully self-contained reference covering:
- The latticework concept and why multi-disciplinary thinking compounds
- All 6 mental disciplines: Mathematics, Physics, Biology, Psychology, Economics, Systems Thinking
- Charlie Munger's 25 cognitive biases and the Lollapalooza Effect
- The pari-mutuel analogy, fat-pitch investing strategy, and the 20-punch card
- Mohnish Pabrai's extensions: asymmetric bets, 168-hour week, shameless cloning, truth on a log scale
- A 150-model quick-reference list and implementation checklist
- AI-era case study applying the latticework to modern technology decisions

**Part II — Munger In His Own Words (~33 pages)**
Eight polished prose sections written from primary sources (Munger's 1994 USC speech, Pabrai's video talk):
1. The Man Who Read Everything
2. The Latticework — What It Is and Why It Matters
3. The Mental Disciplines — Building the Toolkit
4. The Psychology of Human Misjudgment
5. Investing Through the Latticework
6. Pabrai's Extensions — Taking Munger Further
7. Applying the Models in Real Life
8. Building Your Own Latticework

---

## Generating the PDF

**Requirements:**
```bash
pip install reportlab
```

**Run:**
```bash
python generate_munger_pdf.py
```

Output: `munger_latticework_mental_models.pdf` written next to the script.

The script has two modes:
- **Part I** is always generated — fully self-contained, no extra files needed.
- **Part II** requires the `sections/final_section_*.md` files (included in this repo). If they are absent, placeholder pages are inserted and Part I still generates cleanly.

---

## Repository Structure

```
├── generate_munger_pdf.py          # PDF generation script (ReportLab)
├── munger_latticework_mental_models.pdf  # Pre-built output PDF
├── sections/                       # Article sections fed into Part II
│   ├── final_section_1.md          # The Man Who Read Everything
│   ├── final_section_2.md          # The Latticework
│   ├── final_section_3.md          # The Mental Disciplines
│   ├── final_section_4.md          # Psychology of Human Misjudgment
│   ├── final_section_5.md          # Investing Through the Latticework
│   ├── final_section_6.md          # Pabrai's Extensions
│   ├── final_section_7.md          # Applying the Models in Real Life
│   └── final_section_8.md          # Building Your Own Latticework
├── drafts/                         # First drafts before editorial revision
│   └── draft_section_1-8.md
├── sources/                        # Primary research sources
│   ├── charlie_munger_usc_speech.txt   # Munger's 1994 USC commencement speech
│   ├── transcript.txt              # Pabrai video transcript
│   ├── gemini3_summary.txt         # Gemini AI summary of the video
│   └── gpt5_summary.txt            # GPT summary with additional models
├── docs/                           # Process documentation
│   ├── research_notes.md           # Compiled research (150+ models, quotes, structure)
│   └── agent_team_documentation.md # Full multi-agent workflow documentation
└── archive/                        # Earlier versions
    └── munger_latticework_mental_models_v0.pdf
```

---

## Primary Sources

- **Charlie Munger** — "Elementary Worldly Wisdom" commencement address, USC Business School, 1994
- **Mohnish Pabrai** — [The Latticework of Mental Models For a Great Life!](https://www.youtube.com/watch?v=Z2J_8GHcrvQ&t=2269s)
- **Charlie Munger** — *Poor Charlie's Almanack* (recommended in Pabrai's talk)
- **Robert Cialdini** — *Influence* (recommended in Pabrai's talk)
- **Kevin Kelly** — *Excellent Advice for Living* (recommended in Pabrai's talk)

---

## Key Concepts Covered

| Concept | Description |
|---|---|
| **The Latticework** | Interlocking mental models from many disciplines that compound in insight |
| **Lollapalooza Effect** | When 2–3 models converge, the result is non-linear (1+1=11) |
| **Inversion** | Solve problems backwards — ask what you want to *avoid* |
| **Asymmetric Bets** | "Heads I win, tails I don't lose much" risk framing |
| **Circle of Competence** | Know what you know, and know the boundaries |
| **Mr. Market** | Ben Graham's allegory — let volatility work for you, not against you |
| **Pari-mutuel Analogy** | The market prices in consensus; the edge comes from knowing *more* |
| **168-Hour Week** | You have 168 hours; an employer only needs 40 — build in parallel |
| **Truth on a Log Scale** | Eliminating even small lies creates exponential trust compounding |
| **Shameless Cloner** | Study and copy proven models rather than inventing from scratch |

---

## How the Article Was Written

The eight article sections in `sections/` were produced by a three-agent AI team:

1. **Researcher** — compiled `docs/research_notes.md` from primary sources
2. **Writer** — wrote first drafts (`drafts/`) from the research notes
3. **Editor** — critiqued each draft; writer revised into `sections/final_section_*.md`

Full workflow documentation: [`docs/agent_team_documentation.md`](docs/agent_team_documentation.md)
