---
repo: claude-repurpose-talk
description: A Claude Code skill that repurposes any information source into multiple derivative artifacts. Includes 11 artifacts generated from Nathan Lambert's CMU talk on Olmo.
language: HTML
stars: 0
forks: 0
created: 2026-02-15
updated: 2026-02-15
topics: 
is_fork: False
kb: 68
---

# claude-repurpose-talk
# claude-repurpose-talk

A Claude Code skill that repurposes any information source — lectures, papers, blog posts, transcripts — into multiple high-quality derivative artifacts. Also includes the 11 artifacts generated from the talk that inspired the skill.

## The Story

This project grew out of a single experiment: taking Nathan Lambert's 113-slide CMU talk "Building Olmo in the Era of Agents" and seeing how many useful derivative artifacts Claude Code could produce from it.

### Step 1: Repurposing a Talk

Lambert gave an LTI Colloquium at Carnegie Mellon on February 13, 2026, covering AI2's work on the Olmo open language model — architecture decisions, RL training infrastructure, evaluation methodology, and a vision for open models in the agent era.

We fed the slide text to Claude Code and asked it to produce a full suite of companion artifacts: a printable cheat sheet, a key numbers dashboard, a blog post, a Twitter thread, annotated bibliography, open research questions, a reproducibility guide, reconstructed speaker notes, a modular deck outline, Q&A prep, and a diagram pack.

All 11 artifacts were generated in parallel using Claude Code's Task agent system. Each agent received the full source text and a specific artifact brief, wrote its output, and returned. The entire generation step took about 3-5 minutes.

The results are in the [`artifacts/`](artifacts/) directory.

### Step 2: From One-Off to Reusable Skill

After the Lambert run worked, the natural question was: can we generalize this into a reusable workflow for *any* information source?

That turned out to be a harder design problem than expected. Three concerns came up immediately:

**1. Not all artifacts apply to all sources.**
A "Key Numbers Card" makes sense for a data-heavy ML talk but not for a philosophy essay. "Speaker Notes" only apply to presentations. A "Blog Post" artifact is pointless if the source is already a blog post. A rigid "generate all 11 every time" approach would produce low-quality filler.

**Resolution:** Instead of hardcoding a source-type-to-artifact mapping, the skill uses a two-phase approach. First, it analyzes the source and checks for *content signals* (has quantitative data? has citations? is a presentation? is long-form?). Then it scores each artifact type as strong fit, moderate fit, or skip — and presents the proposed list to the user for approval before generating anything. The intelligence is in the analysis, not in a lookup table.

**2. Source types vary wildly in structure.**
A 113-slide PDF, an arXiv paper, a YouTube transcript, and a podcast episode all have completely different structures, information densities, and authorial conventions. The skill needs to know how to extract the right things from each.

**Resolution:** A reference file ([`source-analysis-guide.md`](skill/repurpose/references/source-analysis-guide.md)) describes 9 common source types: what makes each unique, what to extract, and which artifacts tend to work well. Claude consults this during the analysis phase, but it's guidance, not rules — the content signals from the actual source override any source-type heuristics.

**3. Artifact quality depends on knowing what "good" looks like.**
Without clear templates and quality criteria, generated artifacts tend toward generic summaries. Each artifact type has a distinct purpose, audience, and structure.

**Resolution:** An artifact catalog ([`artifact-catalog.md`](skill/repurpose/references/artifact-catalog.md)) defines 13 artifact types, each with: purpose, audience, include/skip criteria, content structure, and quality gates. This catalog is the design-critical piece — it's what makes the difference between a generic "summarize this" tool and a skill that produces genuinely useful outputs.

### The Resulting Skill

The skill lives in [`skill/repurpose/`](skill/repurpose/) and follows the [Agent Skills](https://agentskills.io) open standard. To install it in Claude Code:

```bash
cp -r skill/repurpose ~/.claude/skills/repurpose
```

Then in any Claude Code session:

```
/repurpose path/to/slides.pdf
/repurpose https://arxiv.org/abs/2501.12345
/repurpose transcript.txt
```

The skill will:
1. Read and analyze the source
2. Propose which artifacts to generate (with reasoning)
3. Wait for your approval
4. Generate all approved artifacts in parallel
5. Output to an `artifacts/` directory

## Repository Structure

```
claude-repurpose-talk/
├── README.md
├── skill/
│   └── repurpose/
│       ├── SKILL.md                          # Main skill (138 lines)
│       ├── references/
│       │   ├── artifact-catalog.md           # 13 artifact types with templates
│       │   └── source-analysis-guide.md      # 9 source type profiles
│       └── examples/
│           └── example-run.md                # The Lambert talk run
└── artifacts/                                # Generated from Lambert's CMU talk
    ├── cheat_sheet.html                      # One-page visual summary
    ├── key_numbers.html                      # Quantitative dashboard
    ├── diagrams.html                         # Pipeline, architecture, eval diagrams
    ├── blog_post.md                          # Thematic essay (~2000 words)
    ├── twitter_thread.md                     # 18-post thread
    ├── annotated_bibliography.md             # 22 cited works with annotations
    ├── open_research_questions.md            # 10 extracted research problems
    ├── reproducibility_guide.md              # Links, configs, hardware details
    ├── modular_deck_outline.md               # 5 standalone modules
    ├── speaker_notes.md                      # Reconstructed delivery for key moments
    └── qa_prep.md                            # 15 predicted hard questions
```

## Artifact Types (Catalog)

The skill's artifact catalog includes 13 types. Not all will apply to every source — that's the point of the analysis phase.

| # | Artifact | Format | Best For |
|---|----------|--------|----------|
| 1 | Cheat Sheet | HTML | Dense frameworks, recipes, taxonomies |
| 2 | Key Numbers Card | HTML | Data-heavy content with 5+ metrics |
| 3 | Blog Post | Markdown | Any non-blog source with enough substance |
| 4 | Twitter/X Thread | Markdown | Anything with quotable insights |
| 5 | Annotated Bibliography | Markdown | Sources that cite 5+ other works |
| 6 | Open Research Questions | Markdown | Frontier-of-knowledge content |
| 7 | Reproducibility Guide | Markdown | Experiments, code, configs |
| 8 | Speaker Notes | Markdown | Presentations and talks |
| 9 | Modular Outline | Markdown | Long-form content (>30 min / 5000 words) |
| 10 | Q&A Prep | Markdown | Talks with controversial or technical claims |
| 11 | Diagram Pack | HTML | Processes, architectures, comparisons |
| 12 | Executive Summary | Markdown | Almost anything (broad audience briefing) |
| 13 | Slide Deck Outline | Markdown | Non-presentation sources worth presenting |

## Source Acknowledgment

The artifacts in this repository were generated from Nathan Lambert's talk at Carnegie Mellon University. We are grateful for his work on open models and his willingness to share it publicly.

- **Talk:** "Building Olmo in the Era of Agents" — Nathan Lambert, Allen Institute for AI. LTI Colloquium @ Carnegie Mellon University, February 13, 2026.
- **Slides:** [Google Slides](https://docs.google.com/presentation/d/1K3bM3K7q_CBcXzUCX7a1YvUHAycpvTKZbJElKSOdiok/edit?slide=id.p#slide=id.p)
- **Announcement:** [Nathan Lambert on X](https://x.com/natolambert/status/2022774820702724204?s=20)
- **More from Lambert:** [natolambert.com](https://natolambert.com) and [interconnects.ai](https://interconnects.ai)
- **Olmo project:** [allenai.org](https://allenai.org)

The artifacts are transformative derivatives intended for educational purposes. The raw slide content is not included in this repository. All factual claims, numbers, and technical details in the artifacts originate from Lambert's public talk.

## Built With

- [Claude Code](https://claude.ai/claude-code) (Claude Opus 4.6)
- The `/repurpose` skill in this repo
- No other dependencies

## License

The `/repurpose` skill is released under MIT. The artifacts are derivative works of Lambert's publicly shared talk and are provided for educational and reference purposes with attribution.
