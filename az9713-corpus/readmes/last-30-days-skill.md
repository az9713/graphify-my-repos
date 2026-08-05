# Last 30 Days Research Skill

A Claude Code skill that researches any topic using real-time data from X/Twitter, Reddit, and web sources. Get up-to-date insights, trends, and actionable takeaways from the last 30 days of online discussions.

## What This Project Does

This skill allows you to:
- **Research any topic** using current data from multiple sources
- **Get insights from X/Twitter** including top posts, influential accounts, and trending angles
- **Analyze Reddit discussions** for community sentiment, consensus, and contrarian views
- **Search the web** for recent articles, expert opinions, and emerging trends
- **Generate audit trails** so you can verify and explore sources yourself
- **Save research** to markdown files for future reference

## Who Is This For?

- **Researchers** who need current information on any topic
- **Content creators** looking for trending topics and discussions
- **Business analysts** tracking industry trends
- **Developers** learning about new technologies
- **Anyone** who wants to understand what people are saying about a topic right now

## Quick Start (5 Minutes)

### Prerequisites

1. **Python 3.10+** installed on your computer
2. **Claude Code CLI** installed ([installation guide](https://docs.anthropic.com/en/docs/claude-code))
3. **API Keys** (see [Getting API Keys](#getting-api-keys) below)

### Installation

```bash
# 1. Clone or download this repository
git clone https://github.com/yourusername/last-30-days.git
cd last-30-days

# 2. Install Python dependencies
pip install -r .claude/skills/last-30-days/scripts/requirements.txt

# 3. Create your .env file with API keys
cp .env.example .env
# Edit .env and add your API keys (see Getting API Keys below)

# 4. Start Claude Code in this directory
claude
```

### Your First Research

In Claude Code, you can invoke the skill in two ways:

**Option 1: Natural language**
```
Use last-30-days skill to research artificial intelligence trends
```

**Option 2: Slash command**
```
/last-30-days artificial intelligence trends
```

Both methods work the same way. Claude will research the topic and present findings from X/Twitter, Reddit, and the web.

## Getting API Keys

### XAI API Key (for X/Twitter search)

1. Go to https://console.x.ai
2. Create an account or sign in
3. Navigate to API Keys section
4. Create a new API key
5. Copy the key and add to your `.env` file as `XAI_API_KEY=your_key_here`
6. Add credits to your account (required for API usage)

### OpenAI API Key (for Reddit search)

1. Go to https://platform.openai.com
2. Create an account or sign in
3. Navigate to API Keys (https://platform.openai.com/api-keys)
4. Create a new secret key
5. Copy the key and add to your `.env` file as `OPENAI_API_KEY=your_key_here`
6. Add credits to your account (pay-as-you-go)

## Documentation

| Document | Description |
|----------|-------------|
| [Quick Start Guide](docs/QUICK_START.md) | Get started in 5 minutes with 10 example use cases |
| [User Guide](docs/USER_GUIDE.md) | Complete guide for using the skill |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Technical documentation for developers |
| [Architecture](docs/ARCHITECTURE.md) | System design and how components work together |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Common issues and solutions |
| [API Reference](docs/API_REFERENCE.md) | Detailed API documentation |

## Project Structure

```
last-30-days/
├── .claude/
│   └── skills/
│       └── last-30-days/
│           ├── skill.md              # Skill definition
│           └── scripts/
│               ├── search_x.py       # X/Twitter search script
│               ├── search_reddit.py  # Reddit search script
│               ├── requirements.txt  # Python dependencies
│               └── README.md         # Scripts documentation
├── output/                           # Saved research results
├── docs/                             # Documentation
├── .env.example                      # Example environment file
├── .gitignore                        # Git ignore rules
├── CLAUDE.md                         # Claude Code configuration
└── README.md                         # This file
```

## Example Output

When you run `/last-30-days AI coding assistants`, you get:

- **Key Discoveries**: Top insights with source attribution
- **X/Twitter Section**: Top posts, influential accounts, engagement metrics
- **Reddit Section**: Active subreddits, popular discussions, community sentiment
- **Web Section**: Recent articles, expert opinions, emerging trends
- **Actionable Takeaways**: Practical recommendations
- **Audit Trail**: Tables linking every insight to its source

## Support

- **Issues**: Open an issue on GitHub
- **Documentation**: See the [docs/](docs/) folder

## License

MIT License - see LICENSE file for details

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines on contributing to this project.

## Acknowledgements

- This project was inspired by the YouTube video ["The Claude Code Skill My Smartest Friends Use"](https://www.youtube.com/watch?v=71ES9jzqa0Q&t=5s)
- All code and documentation were generated by [Claude Code](https://claude.ai/code) powered by Claude Opus 4.5
