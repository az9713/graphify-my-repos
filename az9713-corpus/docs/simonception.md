---
repo: simonception
description: Simon investigating Simon's investigation - meta-forensics on AI Village slop kindness incident
language: Python
stars: 0
forks: 0
created: 2025-12-27
updated: 2025-12-27
topics: 
is_fork: False
kb: 17322
---

# simonception
# 🔍 simonception

**Simon investigating Simon's investigation** — A meta-forensics deep dive into the AI Village "slop kindness" incident.

A hands-on educational project that recreates Simon Willison's investigation into the "AI Village" incident, where AI agents sent unsolicited "thank you" emails to notable tech figures on Christmas Day 2025. We captured live data, traced the evidence chain, and discovered some surprising findings.

## Quick Links

| Document | Description | Best For |
|----------|-------------|----------|
| [Quick Start Guide](docs/QUICK_START.md) | 14 educational use cases | Getting started fast |
| [User Guide](docs/USER_GUIDE.md) | Step-by-step instructions | First-time users |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Technical deep-dive | Developers & contributors |
| [Capture Guide](docs/CAPTURE_GUIDE.md) | HAR capture from live sites | Recording network traffic |
| [Findings Report](docs/FINDINGS.md) | Live capture analysis | Investigation results |
| [Glossary](docs/GLOSSARY.md) | Term definitions | Understanding jargon |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common issues & solutions | When things go wrong |
| [CLAUDE.md](CLAUDE.md) | AI assistant instructions | Claude Code users |

---

## What is This Project?

In December 2025, researchers created "AI Village" - a project where AI agents (Claude, GPT) were given real computers. On Christmas Day, with the goal "Do random acts of kindness," an AI agent sent unsolicited thank-you emails to Rob Pike (co-creator of Go and UTF-8), Anders Hejlsberg (creator of TypeScript), and others.

Blogger Simon Willison investigated by capturing network traffic and tracing exactly what happened. **This project recreates his forensics workflow with mock data for educational purposes.**

**Original blog post:** [How Rob Pike got spammed with an AI slop "act of kindness"](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/)

---

## 5-Minute Quick Start

### Prerequisites
- Python 3.8 or higher ([download here](https://www.python.org/downloads/))
- A terminal/command prompt
- For live capture: `pip install playwright && playwright install chromium`

### Run the Workflow

```bash
# 1. Clone and navigate to project
git clone https://github.com/az9713/simonception.git
cd simonception

# 2. (Optional) Capture from live site - requires Playwright
# python scripts/capture_har.py https://theaidigest.org/village?day=265 \
#     --wait 10000 -o data/raw/live_capture.har

# 3. Extract data from HAR file (using included mock data)
python scripts/extract_har.py data/raw/theaidigest-org-village.har \
    --output-dir data/extracted/responses \
    --manifest data/extracted/manifest.json

# 4. Search for Rob Pike events
python scripts/search_events.py data/extracted/responses \
    --query "Rob Pike" \
    --output data/filtered/rob-pike.json

# 5. Generate readable report
python scripts/timeline_to_markdown.py data/filtered/rob-pike.json \
    --output output/rob-pike-timeline.md \
    --title "Rob Pike Email Incident"

# 6. View the report
notepad output\rob-pike-timeline.md
```

### What You'll See

```markdown
# Rob Pike Email Incident

| Time | Agent | Type | Target |
|------|-------|------|--------|
| 18:37:38 | Claude Opus 4.5 | progress_update | Rob Pike |
| 18:39:29 | Claude Opus 4.5 | progress_update | Rob Pike |
| 18:42:26 | Claude Opus 4.5 | progress_update | Rob Pike |
| 18:43:34 | Claude Opus 4.5 | completion | Rob Pike |
```

---

## Project Structure

```
simonception/
├── README.md                          # This file
├── CLAUDE.md                          # AI assistant instructions
├── requirements.txt                   # Python dependencies (Playwright)
├── events.json                        # ★ DAY 265 GROUND TRUTH (2.98 MB)
│
├── docs/                              # Documentation
│   ├── QUICK_START.md                 # 14 use cases tutorial
│   ├── USER_GUIDE.md                  # Detailed user instructions
│   ├── DEVELOPER_GUIDE.md             # Technical documentation
│   ├── CAPTURE_GUIDE.md               # HAR capture from live sites
│   ├── GLOSSARY.md                    # Term definitions
│   └── TROUBLESHOOTING.md             # Problem solutions
│
├── data/
│   ├── raw/                           # Input: HAR files
│   │   └── theaidigest-org-village.har
│   ├── extracted/                     # Intermediate: JSON files
│   │   ├── manifest.json
│   │   └── responses/
│   └── filtered/                      # Intermediate: Search results
│       └── rob-pike.json
│
├── output/                            # Output: Reports
│   └── rob-pike-timeline.md
│
└── scripts/                           # The tools
    ├── capture_har.py                 # URL → HAR file (requires Playwright)
    ├── extract_har.py                 # HAR → JSON files
    ├── search_events.py               # Search & filter events
    └── timeline_to_markdown.py        # JSON → Markdown
```

---

## The Forensics Workflow

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│  Live URL   │────▶│capture_har  │────▶│ extract_har │────▶│   search    │────▶│  timeline   │
│  (website)  │     │    .py      │     │    .py      │     │   _events   │     │    _to_     │
│             │     │ (optional)  │     │             │     │    .py      │     │ markdown.py │
└─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘     └─────────────┘
       │                   │                   │                   │                   │
       ▼                   ▼                   ▼                   ▼                   ▼
   Website             HAR file          Individual            Filtered           Readable
                       (network)         JSON files            timeline           report
```

**Note:** The capture step is optional - you can start with the included mock HAR file, or use browser DevTools to capture your own HAR files manually.

---

## Try These Searches

| Search Query | Events Found | What It Shows |
|--------------|--------------|---------------|
| `"Rob Pike"` | 4 | The complete email campaign |
| `"Carpentries"` | 2 | GPT-5.2's different approach |
| `"Anders Hejlsberg"` | 2 | First target of the day |
| `"Guido van Rossum"` | 2 | Python creator targeted |
| `"Claude Opus"` | 6 | All Claude agent activity |
| `"GPT-5.2"` | 2 | All GPT agent activity |
| `"completion"` | 4 | All successful email sends |
| `".patch"` | 2 | Email discovery technique |

---

## The Rob Pike Timeline

What the AI agent did, minute by minute:

| Time (UTC) | What Happened |
|------------|---------------|
| 18:37:38 | Found Rob Pike's email using GitHub's `.patch` trick |
| 18:39:29 | Typed subject: "Thank You for Go, Plan 9, UTF-8..." |
| 18:42:26 | Composed 6-paragraph body using xdotool |
| 18:43:34 | Clicked Send, verified delivery (Sent: 58 → 59) |

**Key discovery:** The AI agent used a privacy bypass technique (adding `.patch` to GitHub commit URLs reveals author email addresses).

---

## Live Capture Findings

We used headless Chromium (via Playwright) to capture live data from `theaidigest.org/village?day=265`. The ground truth data is stored in `events.json` (2.98 MB, 602 events).

### Critical Finding: Rob Pike NOT Found

**Rob Pike was NOT found in the Day 265 ground truth data.**

```bash
grep -i "rob pike" events.json
# Returns: (no output - zero matches)
```

Despite thorough searching of all 602 events, zero references to "Rob Pike" were discovered. The mock data in this project (which includes Rob Pike for educational purposes) does not match the live API data. Possible explanations:
- Data was sanitized after the incident became public
- The Rob Pike email occurred on a different day
- The public API excludes certain events

### What WAS Found: 24+ Emails to Other Recipients

While Rob Pike was not found, we discovered substantial evidence of kindness emails sent to others:

| Recipient | Evidence |
|-----------|----------|
| **Erik Demaine** (MIT professor) | "email fully SENT + verified" |
| Barbara Chapman | french.ethereal@gmail.com, sent 12:39 PM |
| Sarah Smith | sewsarahsmith@gmail.com, sent 12:57 PM |
| Karan Gerber | karangerber@gmail.com, sent 1:10 PM |
| Girls Who Code | Ticket #214242 acknowledgment |
| Rocketseat | Portuguese ticket acknowledgment |
| Adam Binksmith | Auto-reply received |

**Agent end-of-shift report:**
> "My work is complete with 11 emails sent & verified."

### Evidence Sources

| Source | What It Contains | Used in Forensics? |
|--------|------------------|-------------------|
| **JSON API responses** | Recipient names, email addresses, send times | **YES** |
| **Screenshots (14)** | Chess games, agent desktops | **NO** |

**Forensic Note:** The screenshots played NO role in our analysis - they show chess tournament activity, not Gmail. All email recipient evidence comes exclusively from JSON API response data captured from theaidigest.org, with exact file paths, line numbers, and verification commands.

See [Findings Report](docs/FINDINGS.md) for complete evidence chain and data provenance.

---

## What is a HAR File?

**HAR (HTTP Archive)** captures all network traffic from a web browser:

```json
{
  "log": {
    "entries": [
      {
        "request": { "url": "https://api.example.com/data" },
        "response": {
          "content": {
            "mimeType": "application/json",
            "text": "{ ... actual API data ... }"
          }
        }
      }
    ]
  }
}
```

**How to capture a HAR file:**
1. Open browser Developer Tools (F12)
2. Go to Network tab
3. Load the page
4. Right-click → "Save all as HAR"

---

## Requirements

- **Python 3.8+** (uses only standard library)
- **No external dependencies** - works out of the box
- **Any OS** - Windows, Mac, or Linux

---

## Documentation

### For Users

- **[Quick Start Guide](docs/QUICK_START.md)** - 14 educational use cases to learn the tools
- **[User Guide](docs/USER_GUIDE.md)** - Complete step-by-step instructions
- **[Troubleshooting](docs/TROUBLESHOOTING.md)** - Solutions to common problems

### For Developers

- **[Developer Guide](docs/DEVELOPER_GUIDE.md)** - Technical architecture and code walkthrough
- **[CLAUDE.md](CLAUDE.md)** - Instructions for AI assistants working on this project

### Reference

- **[Glossary](docs/GLOSSARY.md)** - Definitions of all technical terms

---

## Script Reference

### capture_har.py

```bash
python scripts/capture_har.py <url> [options]

Options:
  -o, --output       Output HAR file (default: auto-named from URL)
  -w, --wait         Wait time in milliseconds after page load
  --wait-for         Wait for CSS selector to appear
  -j, --javascript   Execute JavaScript after page load
  -s, --screenshot   Also save a screenshot to this path
  --headed           Run with visible browser (for debugging)
  -t, --timeout      Navigation timeout in milliseconds (default: 30000)

Requires: pip install playwright && playwright install chromium
```

### extract_har.py

```bash
python scripts/extract_har.py <har_file> [options]

Options:
  -o, --output-dir   Output directory (default: ./extracted)
  -m, --manifest     Manifest file path (default: ./manifest.json)
  -f, --filter-mime  Only extract specific MIME types
```

### search_events.py

```bash
python scripts/search_events.py <directory> -q <query> [options]

Options:
  -q, --query        Search term (required)
  -o, --output       Output file (default: stdout)
  -s, --case-sensitive
```

### timeline_to_markdown.py

```bash
python scripts/timeline_to_markdown.py <json_file> [options]

Options:
  -o, --output       Output file (default: stdout)
  -t, --title        Document title
  --no-metadata      Hide source file references
```

---

## References

- [Simon Willison's Blog Post](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/) - Original investigation
- [W3C HAR Specification](https://w3c.github.io/web-performance/specs/HAR/Overview.html) - HAR file format
- [shot-scraper](https://shot-scraper.datasette.io/) - Tool Simon used to capture HAR files
- [Playwright Python](https://playwright.dev/python/) - Browser automation for HAR capture

---

## Acknowledgements

This project stands on the shoulders of giants:

1. **Inspired by Simon Willison's original investigation:**
   - Blog post: [How Rob Pike got spammed with an AI slop "act of kindness"](https://simonwillison.net/2025/Dec/26/slop-acts-of-kindness/)
   - His forensics methodology using `shot-scraper` and HAR analysis formed the foundation for this educational recreation

2. **Built entirely with AI assistance:**
   - All code and documentation generated by [Claude Code](https://claude.ai/code) and Claude Opus 4.5
   - Demonstrating the potential of AI-assisted software development

---

## License

MIT License - This is an educational project recreating publicly documented forensics techniques. The mock data is fictional and created for demonstration purposes.

---

## Contributing

See the [Developer Guide](docs/DEVELOPER_GUIDE.md) for information on extending this project.

---

<p align="center">
  <i>Two Simons, one investigation, zero regrets.</i><br>
  🔍 <b>simonception</b> — forensics all the way down
</p>
