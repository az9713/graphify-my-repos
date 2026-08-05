# `fable-teach-skills` — a `/teach` stress-test collection

### ▶️ [**Open the landing page →**](https://az9713.github.io/fable-teach-skills/)

A growing collection of teaching workspaces produced by running Matt Pocock's
[`/teach`](https://github.com/mattpocock/skills) skill inside Claude Code (model: **Claude Fable 5**).
Each subfolder is one **independent, self-contained `/teach` run** in a different domain — a
stress test of how well a single slash command turns into a structured, mission-grounded
curriculum across very different subjects.

---

## Domains

| Domain | Request | Mission | Live lesson |
|--------|---------|---------|-------------|
| 🤹 [**Juggling**](./juggling/) | `/teach how to juggle 3 balls` | Land a 3-ball cascade as a party trick | [Lesson 1 →](https://az9713.github.io/fable-teach-skills/juggling/) |
| 🎵 [**Singing**](./singing/) | `/teach how to sing like Luciano Pavarotti` | Sing one iconic tenor aria, proudly | [Lesson 1 →](https://az9713.github.io/fable-teach-skills/singing/) |
| 📜 [**Tang poetry**](./tang-shi/) | `/teach me to write a "tang shi" like 唐詩三百首` | Compose a 律詩 worthy of the anthology | [Lesson 1 →](https://az9713.github.io/fable-teach-skills/tang-shi/) |

> More domains will be added as further stress tests are run.

---

## What `/teach` is

`/teach` treats the **current directory as a stateful learning workspace** that persists across
sessions, rather than answering a one-shot "explain X" prompt. Its philosophy: deep learning needs
three things —

- **Knowledge** — captured from high-trust sources, never the model's memory (`RESOURCES.md`)
- **Skills** — acquired through tight interactive feedback loops (`lessons/`)
- **Wisdom** — tested against real practitioners (communities in `RESOURCES.md`)

Everything is anchored to a single **mission** — the real reason the learner cares.

---

## Repository layout

```
.
├── index.html            # Landing page (links into every domain)
├── README.md             # You are here
├── <domain>/             # One self-contained /teach workspace per domain
│   ├── MISSION.md         # The "why" — the compass for every teaching decision
│   ├── RESOURCES.md       # Trusted knowledge sources + practitioner communities
│   ├── NOTES.md           # Learner preferences + working notes
│   ├── index.html         # Redirect to that domain's current lesson
│   ├── lessons/           # Self-contained, beautiful HTML lessons
│   ├── reference/         # Compressed cheat sheets & glossaries (revisited often)
│   └── learning-records/  # Evidence-based records of what was actually learned
```

### Adding a new domain

1. Create a new folder (e.g. `pottery/`) and run `/teach …` with that folder as the working directory.
2. Add a `<domain>/index.html` redirect to its first lesson.
3. Add one row to the **Domains** table above and one card to `index.html`.

---

## Development journal

### Domain 3 — 唐詩 Tang regulated verse (📜 `tang-shi/`)

**The prompt:**
> *"Teach me how to write a 'tang shi' like those in Tang Shi San Bai Shou. After you teach me, I should be able to write a 'tang shi' that will still be celebrated after hundreds if not thousands of years."*

This was the most demanding `/teach` stress-test in the collection so far, for two reasons:
(1) the subject domain — Tang regulated verse — has a phonological dimension (Middle Chinese tones)
that cannot be recovered from modern fluency alone; (2) the stated ambition — poetry celebrated for
a millennium — set up a mission-grounding moment: Fable 5 had to honestly bound what is and isn't
trainable before writing a single lesson.

**How Fable 5 scoped the mission**

After learning the learner reads Traditional Chinese fluently (including some classical) and
deliberately chose 律詩 (the hardest 8-line regulated form) over the simpler 絕句 quatrain, the
model wrote a `MISSION.md` that frames the aspiration honestly: canonization is decided by readers,
history, and luck — it cannot be trained. What *can* be trained is the craft that gave the 300 poems
their chance. Success is defined as passing [搜韻's 律詩校驗](https://sou-yun.cn/) with zero errors,
writing parallel couplets a literate reader credits as real craft, and submitting a finished poem to
a practitioner community for critique.

**The zone of proximal development decision for lesson 0001**

Rather than opening with poetic imagery or thematic content — the natural "interesting" entry point
— Fable 5 identified 平仄 (the tonal classification of every syllable as either level or oblique)
as the correct first rung, for a specific reason: *modern Mandarin fluency actively misleads you
here*. The entire 入聲 (entering tone) category — short syllables historically ending in -p, -t,
-k — dissolved into all four modern tones when Middle Chinese evolved into Mandarin. This means
words like 白, 國, 別, 月, 不 sound level in Mandarin (bái, guó, bié, yuè, bù) but are
**oblique in Tang prosody**. A learner who skips this step would mark half the tonal grid wrong
without knowing why.

**How lesson 0001 was constructed**

Fable 5 verified its primary sources before building anything:

| Source | Role | Verified |
|--------|------|---------|
| [唐詩三百首 — UVa Etext](https://cti.lib.virginia.edu/frame.htm) | Anchor anthology (the learner's stated target) | ✓ |
| [搜韻 sou-yun.cn](https://sou-yun.cn/) | 平水韻 tables + automated 律詩校驗 (the feedback loop for compositions) | ✓ |
| [全唐詩 — ctext.org](https://ctext.org/quantangshi) | Full Tang corpus in 繁體 for wider exemplar lookup | ✓ |
| [漢典 zdic.net](https://www.zdic.net/) | Per-character phonology incl. 廣韻 fanqie + 平水韻 category | ✓ (blocks automated fetches; browser-verified reference) |
| [詩詞吾愛 52shici.com](https://www.52shici.com/) | Practitioner community with 格律檢測 tools | ✓ |
| 王力《詩詞格律》(中華書局) | Canonical modern manual — the workspace's authoritative ruling | Print/library |
| 韻典網 ytenx.org | 廣韻-level character lookup | ✗ — TLS cert expired; excluded and noted in RESOURCES.md Gaps |

Du Fu's 《春望》was chosen as the practice poem because it is a **五言律詩** — the exact form the
learner is targeting — and because it is unusually dense with teaching material: seven 入聲 characters,
a reverse trap (勝 read as 平 in 不勝簪), and a polyphone (更). The lesson is a **click-to-mark
interactive drill**: the learner taps each of the 40 characters to label it ○ (level) or ● (oblique),
then checks against the 平水韻 answer key. Wrong characters receive per-character annotation explaining
*why* — including which ancient rime category the character belongs to and what the equivalent sounds
like in topolects (Cantonese, Minnan) that still preserve the entering tone. A perfect score unlocks
the rhyme analysis: 深心金簪 = 下平十二侵, illustrating the one-group rhyme rule for all future lessons.

**Reference documents created alongside lesson 0001**

- [`reference/pingze-cheatsheet.html`](tang-shi/reference/pingze-cheatsheet.html) — Mandarin→平仄 decision rules, high-frequency 入聲 watchlist, polyphone table (勝更看思騎過), and links to the two tool-verified arbiters.
- [`reference/glossary.html`](tang-shi/reference/glossary.html) — ~20 terms (四聲, 平仄, 入聲, 平水韻, 黏對, 孤平, 拗救, 對仗, 起承轉合, 用典, 詩眼…) with lesson-tagging; all future lessons adhere to this vocabulary.

**Planned lesson arc** (from `tang-shi/NOTES.md`, calibrated per session by learning-records):

> 平仄 ✓ → four line types & 黏對 → 押韻 / 平水韻 groups → first 五絕 as scaffolding exercise → 對仗 → composing a full 五律 → 拗救 → 用典 & imagery → 七律

---

## Credits

- Teaching method: [`/teach`](https://github.com/mattpocock/skills/tree/main/skills/productivity/teach)
  from **[mattpocock/skills](https://github.com/mattpocock/skills)** by Matt Pocock.
- Workspaces generated in [Claude Code](https://claude.com/claude-code) with **Claude Fable 5**.
