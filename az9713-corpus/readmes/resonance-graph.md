# Resonance Graph

**The AI Social Graph for Intellectual Connection**

Resonance Graph is an AI Social Graph that connects people based on intellectual resonance - using artificial intelligence to match users who consume similar content in real-time.

## Overview

Resonance Graph is an **AI Social Graph** - a Chrome extension + FastAPI backend system that uses AI (LLMs and vector embeddings) to:

1. **Passively tracks** what content you consume (with dwell-time thresholds)
2. **Summarizes** content using LLM providers (OpenAI, Anthropic, Gemini, or Ollama)
3. **Generates embeddings** to create semantic fingerprints of your interests
4. **Matches** you with other users exploring similar intellectual territory
5. **Displays** resonance connections in real-time

## Architecture

```
┌─────────────────────────────────────────────────────────────┐
│                    CHROME EXTENSION                         │
│  ┌─────────────┐   ┌─────────────┐   ┌─────────────────┐   │
│  │  Content    │──▶│  Service    │──▶│     Popup       │   │
│  │  Script     │   │  Worker     │   │     UI          │   │
│  └─────────────┘   └──────┬──────┘   └─────────────────┘   │
└───────────────────────────│─────────────────────────────────┘
                            │ POST /api/v1/sync_mind
                            ▼
┌─────────────────────────────────────────────────────────────┐
│                    FASTAPI BACKEND                          │
│  ┌───────────┐   ┌───────────┐   ┌───────────────────────┐  │
│  │    LLM    │   │ Embedding │   │      ChromaDB         │  │
│  │ Providers │   │ Providers │   │   (Vector Store)      │  │
│  └───────────┘   └───────────┘   └───────────────────────┘  │
└─────────────────────────────────────────────────────────────┘
```

## Quick Start

### Prerequisites

- Python 3.10+
- Chrome browser
- API key for at least one LLM provider (or Ollama installed locally)

### Backend Setup

```bash
# Navigate to backend directory
cd resonance-graph/backend

# Create virtual environment
python -m venv .venv

# Activate virtual environment
# On Windows:
.venv\Scripts\activate
# On macOS/Linux:
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Copy environment template
cp .env.example .env

# Edit .env with your API keys
# At minimum, set one of:
#   OPENAI_API_KEY=sk-...
#   ANTHROPIC_API_KEY=sk-ant-...
#   GEMINI_API_KEY=...
# Or use Ollama (no key needed)

# Start the server
uvicorn app.main:app --reload --port 8000
```

Verify the backend is running: http://localhost:8000/docs

### Extension Setup

1. Generate placeholder icons (or create your own):
   ```bash
   pip install Pillow
   python scripts/generate_icons.py
   ```

2. Load the extension in Chrome:
   - Open `chrome://extensions/`
   - Enable "Developer mode" (top right)
   - Click "Load unpacked"
   - Select the `resonance-graph/extension` folder

3. The Resonance icon should appear in your toolbar

### Test the System

Seed the database with test users:
```bash
python scripts/seed_test_data.py
```

Or run the demo showing two users matching:
```bash
python scripts/seed_test_data.py demo
```

## Configuration

### Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `LLM_PROVIDER` | `openai` | LLM provider: `openai`, `anthropic`, `gemini`, `ollama` |
| `EMBEDDING_PROVIDER` | `openai` | Embedding provider: `openai`, `gemini`, `ollama` |
| `OPENAI_API_KEY` | - | OpenAI API key |
| `ANTHROPIC_API_KEY` | - | Anthropic API key |
| `GEMINI_API_KEY` | - | Google Gemini API key |
| `OLLAMA_BASE_URL` | `http://localhost:11434` | Ollama server URL |
| `SIMILARITY_THRESHOLD` | `0.75` | Minimum similarity to report a match (0-1) |
| `TIME_WINDOW_HOURS` | `24` | Only match events within this time window |
| `MAX_MATCHES` | `5` | Maximum number of matches to return |

### Using Different Providers

**OpenAI (Recommended for best results):**
```env
LLM_PROVIDER=openai
EMBEDDING_PROVIDER=openai
OPENAI_API_KEY=sk-...
```

**Anthropic Claude:**
```env
LLM_PROVIDER=anthropic
EMBEDDING_PROVIDER=openai  # Claude doesn't have embeddings
ANTHROPIC_API_KEY=sk-ant-...
OPENAI_API_KEY=sk-...      # Still needed for embeddings
```

**Google Gemini:**
```env
LLM_PROVIDER=gemini
EMBEDDING_PROVIDER=gemini
GEMINI_API_KEY=...
```

**Ollama (Local, Free):**
```bash
# Install Ollama from https://ollama.ai
ollama pull llama3.2
ollama pull nomic-embed-text
```

```env
LLM_PROVIDER=ollama
EMBEDDING_PROVIDER=ollama
OLLAMA_BASE_URL=http://localhost:11434
OLLAMA_MODEL=llama3.2
OLLAMA_EMBEDDING_MODEL=nomic-embed-text
```

## API Endpoints

| Endpoint | Method | Description |
|----------|--------|-------------|
| `/api/v1/sync_mind` | POST | Main endpoint: process content, find matches |
| `/api/v1/health` | GET | Health check |
| `/api/v1/config` | GET | Current configuration (no secrets) |
| `/api/v1/stats` | GET | Database statistics |
| `/api/v1/user/{user_id}` | DELETE | Delete user data (GDPR) |

### Sync Mind Request

```json
{
  "user_id": "uuid-string",
  "url": "https://example.com/article",
  "title": "Article Title",
  "raw_text": "The full text content...",
  "dwell_time_seconds": 45,
  "timestamp": "2024-01-15T10:30:00Z"
}
```

### Sync Mind Response

```json
{
  "success": true,
  "event_id": "event-uuid",
  "resonating_users": [
    {
      "user_id": "other-user-uuid",
      "source_url": "https://other.com/similar-article",
      "content_summary": "Summary of what they read...",
      "similarity": 0.89,
      "context_tags": "AI,Transformers,NLP"
    }
  ],
  "content_summary": "Summary of your content...",
  "context_tags": ["AI", "Machine Learning", "NLP"]
}
```

## Local Testing with Multiple Users

Since this is a social matching system, testing requires simulating multiple users. Options:

### 1. Chrome Profiles
Create multiple Chrome profiles, each with its own extension instance:
- Click profile icon → Add → Create new profile
- Load the extension separately in each profile
- Each profile gets a unique user ID

### 2. Seeding Script
Use the provided script to create synthetic users:
```bash
python scripts/seed_test_data.py
```

### 3. Multiple Browser Windows
- Open Chrome with different user data directories:
```bash
chrome.exe --user-data-dir="C:\temp\chrome-user-a"
chrome.exe --user-data-dir="C:\temp\chrome-user-b"
```

## Project Structure

```
resonance-graph/
├── backend/
│   ├── app/
│   │   ├── main.py              # FastAPI entry point
│   │   ├── config.py            # Settings and configuration
│   │   ├── api/
│   │   │   ├── routes/
│   │   │   │   └── resonance.py # API endpoints
│   │   │   └── dependencies.py  # DI providers
│   │   ├── core/
│   │   │   ├── llm/             # LLM provider abstraction
│   │   │   ├── embeddings/      # Embedding provider abstraction
│   │   │   └── vectordb/        # ChromaDB client
│   │   └── models/
│   │       └── resonance.py     # Pydantic models
│   ├── requirements.txt
│   └── .env.example
├── extension/
│   ├── manifest.json            # Chrome extension manifest
│   ├── background/
│   │   └── service-worker.js    # Core extension logic
│   ├── content/
│   │   └── content-script.js    # Page content extraction
│   ├── popup/
│   │   ├── popup.html
│   │   ├── popup.js
│   │   └── popup.css
│   ├── options/
│   │   ├── options.html
│   │   └── options.js
│   └── icons/
├── scripts/
│   ├── seed_test_data.py        # Test data generation
│   └── generate_icons.py        # Icon generation
└── README.md
```

## How It Works

> **Note**: For a deep dive into what the "Resonance Graph" actually is (and how it relates to traditional graph data structures from CS), see [Resonance Graph Explained](docs/RESONANCE_GRAPH_EXPLAINED.md).

1. **Content Detection**: When you stay on a page for 30+ seconds, the extension extracts the main content

2. **Summarization**: The LLM creates a 2-3 sentence summary capturing key concepts

3. **Tag Extraction**: The LLM identifies topic tags (e.g., "AI", "Transformers", "NLP")

4. **Embedding Generation**: The summary is converted to a vector embedding (1536 dimensions for OpenAI)

5. **Storage**: The embedding and metadata are stored in ChromaDB

6. **Matching**: When querying, the system finds other users whose embeddings are similar (cosine similarity > 0.75)

7. **Display**: Matches appear in the extension popup with similarity scores and content summaries

## Supported Content

| Content Type | Supported | Notes |
|--------------|-----------|-------|
| HTML pages | **Yes** | Articles, blogs, documentation, Wikipedia |
| Plain text | **Yes** | Extracted from HTML body |
| **PDF files** | **No** | Chrome's PDF viewer blocks content extraction |
| Images/Video | **No** | No OCR or transcription |
| Google Docs | **No** | CSP blocks extension scripts |

**PDF Workaround**: Use HTML versions when available:
- Instead of `arxiv.org/pdf/1706.03762` use `arxiv.org/abs/1706.03762`

For complete details, see [Limitations](docs/LIMITATIONS.md).

## Important Notes

1. **Provider Configuration**: The system defaults to OpenAI. Adding an API key alone does NOT switch providers. You must explicitly set:
   ```env
   LLM_PROVIDER=gemini      # or anthropic, ollama
   EMBEDDING_PROVIDER=gemini
   ```

2. **Environment Variable Precedence**: System/user environment variables override `.env` file values.

3. **Embedding Compatibility**: Different providers use different embedding dimensions. Switching providers requires resetting the database:
   ```bash
   rm -rf backend/chroma_data/
   python scripts/seed_test_data.py
   ```

## Documentation

| Document | Description |
|----------|-------------|
| [Quick Start](docs/QUICK_START.md) | Get running in under 10 minutes |
| [Limitations](docs/LIMITATIONS.md) | Known limitations and constraints |
| [Troubleshooting](docs/TROUBLESHOOTING.md) | Comprehensive problem-solving guide |
| [Resonance Graph Explained](docs/RESONANCE_GRAPH_EXPLAINED.md) | How the "graph" works |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Complete development documentation |
| [Architecture](docs/ARCHITECTURE.md) | System design deep dive |
| [Tutorials](docs/tutorials/) | Step-by-step technology tutorials |

## Troubleshooting

### Backend Issues

**"Connection refused" error:**
- Ensure backend is running: `uvicorn app.main:app --reload --port 8000`
- Check the port matches what's configured in the extension

**"Invalid API key" error:**
- Verify your API keys in `.env`
- Ensure the provider matches your API key

**Ollama not working:**
- Ensure Ollama is running: `ollama serve`
- Pull required models: `ollama pull llama3.2 && ollama pull nomic-embed-text`

### Extension Issues

**Extension not loading:**
- Check for errors in `chrome://extensions/`
- Ensure all icon files exist (or generate placeholders)
- Check manifest.json syntax

**No matches appearing:**
- Seed test data: `python scripts/seed_test_data.py`
- Lower similarity threshold in `.env`
- Increase time window in `.env`

**Content not being captured:**
- Wait 30 seconds on a page
- Check the browser console for content script errors
- Some pages block content scripts (banking, Google Docs, etc.)

## Acknowledgements

This project stands on the shoulders of giants:

- **Inspiration**: This project was inspired by [a16z's "Big Ideas" video on AI in 2026](https://www.youtube.com/watch?v=J6_nNjy3al8&t=333s), specifically the segment on [AI as a Relationship Facilitator](https://www.youtube.com/watch?v=J6_nNjy3al8&t=467s) (7:47), which explored how AI could connect people based on intellectual interests rather than surface-level attributes.

- **Development**: All code and documentation for this project were generated by [Claude Code](https://claude.ai/claude-code) powered by [Claude Opus 4.5](https://www.anthropic.com/claude), Anthropic's most capable AI model.

- **Naming**: The name "Resonance Graph" emerged from a brainstorming session with [Gemini 3.0](https://deepmind.google/technologies/gemini/), capturing the concept of intellectual harmony between minds exploring similar territories.

## License

MIT

## Contributing

Contributions welcome! Please read the architecture documentation in the plan file for context on design decisions.
