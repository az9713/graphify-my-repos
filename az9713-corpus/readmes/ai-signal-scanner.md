# AI Signal Scanner

A daily digest generator that surfaces high-signal AI developments from multiple sources, filtered by Claude for relevance to your specific interests.

**New to this project?** Start with the [Quick Start Guide](docs/QUICK_START.md).

---

## What It Does

```
┌──────────────┐     ┌──────────────┐     ┌──────────────┐
│    FETCH     │ --> │    SCORE     │ --> │   GENERATE   │
│              │     │              │     │              │
│ Hacker News  │     │ Claude rates │     │  Markdown    │
│ arXiv        │     │ each item    │     │  digest      │
│ GitHub       │     │ for YOU      │     │              │
└──────────────┘     └──────────────┘     └──────────────┘
```

1. **Fetches** recent items from:
   - Hacker News (AI-related stories via Algolia search)
   - arXiv (cs.AI, cs.LG, cs.CL papers)
   - GitHub (trending AI/ML repositories)

2. **Scores** each item using Claude against your personal profile

3. **Outputs** a filtered markdown digest with only high-relevance items

---

## Quick Start (5 Minutes)

```bash
# 1. Navigate to the project
cd src

# 2. Create and activate virtual environment
python -m venv venv
source venv/Scripts/activate    # Windows/GitBash
# source venv/bin/activate      # Mac/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Set up API key
cp .env.example .env
# Edit .env and add your ANTHROPIC_API_KEY

# 5. Test fetching (no API key needed)
python scanner.py --dry-run

# 6. Generate your first digest
python scanner.py
```

Output will be saved to `output/digest_YYYY-MM-DD.md`

---

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| [Quick Start Guide](docs/QUICK_START.md) | Everyone | 5-minute setup + 10 hands-on use cases |
| [User Guide](docs/USER_GUIDE.md) | Users | Complete guide to installation, configuration, and usage |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Developers | Code walkthrough, adding sources, modifying scoring |
| [Architecture](docs/ARCHITECTURE.md) | Developers | Deep dive into how the system works |
| [CLAUDE.md](CLAUDE.md) | Claude Code | Quick reference for AI assistants |

---

## How Scoring Works

Claude evaluates each item against YOUR profile and assigns a relevance score:

| Score | Meaning | Example |
|-------|---------|---------|
| 10 | Paradigm shift | GPT-4 release, Claude Code launch |
| 8-9 | Major development | Significant new tool or technique |
| 6-7 | Useful signal | Interesting but not urgent |
| 4-5 | Minor noise | Incremental, niche |
| 1-3 | Irrelevant | Hype, PR, off-topic |

Only items scoring at or above your threshold (default: 7) appear in the digest.

**What's penalized:** Rehashed news, opinion pieces, funding announcements, vaporware, minor benchmarks

**What's rewarded:** Working code, new capabilities, API changes, practical tools

### Why Some Sources May Not Appear

All sources are fetched, but only items scoring >= threshold appear in the digest. **Your profile determines which sources dominate:**

| Profile Focus | GitHub | Hacker News | arXiv |
|---------------|--------|-------------|-------|
| Practical tools | ★★★ High | ★★ Medium | ★ Low |
| Research | ★ Low | ★★ Medium | ★★★ High |

If you don't see arXiv papers, it's because your profile favors practical tools over academic research. Adjust your profile or lower the threshold to see more sources

---

## Configuration

Edit `config.yaml` to customize:

### Your Profile (MUST CUSTOMIZE!)

> **The default profile is NOT for everyone.** It was created for a specific user interested in agentic coding tools. You MUST customize it to match YOUR interests, or the digest will filter content based on someone else's preferences.

**Default Profile (in config.yaml):**
```yaml
user_profile: |
  Technical user who:
  - Builds applications with Claude Code, Codex, Gemini CLI
  - Cares about agentic coding, tool use, practical AI capabilities
  - Interested in: new models, new tools, capability breakthroughs, API changes
  - Wants to catch paradigm shifts early but ignore incremental noise
  - Does NOT care about: hype, funding announcements, opinion pieces,
    minor benchmark improvements, corporate PR, AI ethics debates
```

**What this default profile does:**
- Favors GitHub repos with working code (scores 7-10)
- Filters out most academic papers (scores 4-6)
- Penalizes benchmark improvements and theoretical advances
- Rewards practical tools and released software

**If this doesn't match your interests, CHANGE IT.** Examples:

```yaml
# For ML researchers:
user_profile: |
  ML researcher interested in:
  - New architectures, attention mechanisms, training techniques
  - State-of-the-art results and benchmark improvements
  - Theoretical advances in deep learning
  - Does NOT care about: product launches, startup tools, tutorials

# For product managers:
user_profile: |
  Product manager evaluating AI for our product:
  - Interested in: AI product launches, pricing, UX patterns
  - Cares about: case studies, adoption trends, competitor tools
  - Does NOT care about: technical implementation details, academic papers
```

The more specific your profile, the better the filtering.

### Sources

```yaml
sources:
  hackernews:
    enabled: true
    max_items: 50
    min_score: 20

  arxiv:
    enabled: true
    max_items: 30
    categories: [cs.AI, cs.LG, cs.CL]

  github:
    enabled: true
    max_items: 30
```

### Expanding Beyond Default Sources

The three built-in sources can be extended. Free APIs available:

| Category | APIs | Best For |
|----------|------|----------|
| Academic | Papers With Code, Semantic Scholar, OpenAlex | Papers with implementations |
| Developer | Reddit, DEV.to, Lobsters, Product Hunt | Discussions, tutorials |
| AI/ML | Hugging Face, Replicate | New models, datasets |
| News | NewsAPI, The Guardian | Broader coverage |

See [Developer Guide](docs/DEVELOPER_GUIDE.md#free-apis-for-additional-sources) for implementation details.

---

## Command Line Options

```bash
python scanner.py                    # Normal run
python scanner.py --dry-run          # Fetch only, no scoring (free)
python scanner.py --threshold 5      # Lower threshold = more items
python scanner.py --output ~/out.md  # Custom output path
```

---

## Cost

- ~100 items × ~300 tokens per scoring = ~$0.10-0.20 per run
- Daily for a month: ~$3-6
- Use `--dry-run` to test without API costs

---

## File Structure

```
ai-signal-scanner/
├── README.md              # This file
├── CLAUDE.md              # For Claude Code
├── docs/                  # Full documentation
│   ├── QUICK_START.md
│   ├── USER_GUIDE.md
│   ├── DEVELOPER_GUIDE.md
│   └── ARCHITECTURE.md
└── src/                   # Source code
    ├── scanner.py         # Entry point
    ├── scorer.py          # Claude scoring
    ├── config.yaml        # Configuration
    ├── requirements.txt   # Dependencies
    ├── .env.example       # API key template
    ├── sources/           # Data fetchers
    │   ├── hackernews.py
    │   ├── arxiv.py
    │   └── github.py
    └── output/            # Generated digests
```

---

## Troubleshooting

| Problem | Solution |
|---------|----------|
| "ANTHROPIC_API_KEY not set" | Create `.env` file with your key |
| "No module named 'anthropic'" | Run `pip install -r requirements.txt` |
| GitHub rate limiting | Wait 1 hour or disable GitHub in config |
| Empty digest | Lower threshold: `--threshold 5` |

See [User Guide](docs/USER_GUIDE.md#troubleshooting) for more.

---

## License

Do whatever you want with this. Built during a conversation with Claude.
