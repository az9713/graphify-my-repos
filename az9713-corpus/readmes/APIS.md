# 🎬 APIS - Adaptive Playlist Intelligence System

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

**APIS** is an intelligent YouTube playlist analyzer that automatically classifies playlist types, extracts transcripts and visuals, and generates meaningful, type-aware summaries and insights using advanced AI models.

## 🚀 Features

- **🔍 Smart Classification**: Automatically detects playlist types (lectures, conferences, tutorials, etc.)
- **🧠 Adaptive Learning**: Creates new type definitions for novel playlist categories
- **🎥 Multimodal Analysis**: Processes both audio transcripts and visual keyframes
- **📊 Rich Artifacts**: Generates type-specific summaries, insights, and recommendations
- **💾 Persistent Storage**: Saves analysis results with JSON and Markdown export
- **⚡ Cost Efficient**: Optimized for minimal API usage with smart caching

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Configuration](#configuration)
- [Usage](#usage)
- [Architecture](#architecture)
- [Supported Playlist Types](#supported-playlist-types)
- [API Documentation](#api-documentation)
- [Contributing](#contributing)
- [License](#license)

## 🛠 Installation

### Prerequisites

- Python 3.8 or higher
- FFmpeg (for video processing)
- OpenAI API key OR Anthropic API key

### Install Dependencies

```bash
# Clone the repository
git clone <repository-url>
cd youtube_playlist

# Install Python dependencies
pip install -r requirements.txt

# Install FFmpeg (Ubuntu/Debian)
sudo apt update && sudo apt install ffmpeg

# Install FFmpeg (macOS)
brew install ffmpeg

# Install FFmpeg (Windows)
# Download from https://ffmpeg.org/download.html
```

### Configuration

1. **Copy environment template:**
   ```bash
   cp .env.example .env
   ```

2. **Add your API key to `.env`:**
   ```bash
   # For OpenAI (recommended)
   OPENAI_API_KEY=your_openai_api_key_here
   LLM_PROVIDER=openai
   LLM_MODEL=gpt-4o

   # OR for Anthropic
   ANTHROPIC_API_KEY=your_anthropic_api_key_here
   LLM_PROVIDER=anthropic
   LLM_MODEL=claude-3-sonnet-20240229
   ```

3. **Get API Keys:**
   - **OpenAI**: https://platform.openai.com/api-keys
   - **Anthropic**: https://console.anthropic.com/

## 🚀 Quick Start

### Analyze a Playlist

```bash
python cli.py analyze --url "https://www.youtube.com/playlist?list=YOUR_PLAYLIST_ID"
```

### View Saved Analyses

```bash
python cli.py list
```

### View Registered Types

```bash
python cli.py types
```

### Example Output

```
🎬 Starting analysis of playlist: https://www.youtube.com/playlist?list=PL2XFXGwNCfUZaCly5XJ2F7voIaGmutwxp
📥 Fetching playlist metadata...
✅ Found 25 videos in playlist: Machine Learning Course
🔍 Classifying playlist type...
✅ Classified as: lecture (confidence: 94.2%)
🎥 Processing videos...
📝 Generating video summaries...
🎨 Generating playlist artifacts...
💾 Saving results...
📄 Generating report...
✅ Analysis complete!
```

## ⚙️ Configuration

### Core Settings (`.env`)

| Variable | Description | Default |
|----------|-------------|---------|
| `LLM_PROVIDER` | AI provider (`openai` or `anthropic`) | `openai` |
| `LLM_MODEL` | Model to use | `gpt-4o` |
| `MAX_VIDEO_LENGTH` | Skip videos longer than (seconds) | `3600` |
| `MAX_PLAYLIST_SIZE` | Maximum videos to process | `50` |
| `WHISPER_MODEL` | Whisper model size | `base` |
| `STORAGE_PATH` | Data storage directory | `./data` |

### Advanced Configuration

```bash
# Processing limits
MAX_KEYFRAMES_PER_VIDEO=10
KEYFRAME_INTERVAL=30

# Quality settings
YOUTUBE_DL_FORMAT="best[height<=720]"
```

## 💡 Usage

### Command Line Interface

```bash
# Analyze a playlist
python cli.py analyze --url "PLAYLIST_URL" [--max-videos 10]

# List saved analyses
python cli.py list

# Show registered playlist types
python cli.py types
```

### Python API

```python
from src.main import PlaylistAnalyzer

analyzer = PlaylistAnalyzer()
result = analyzer.analyze_playlist("https://youtube.com/playlist?list=...")

print(f"Type: {result.type_classification.type}")
print(f"Summary: {result.playlist_summary}")
```

## 🏗 Architecture

```
[ YouTube Playlist URL ]
        ↓
[ Playlist Fetcher ] ──→ Extract metadata & video list
        ↓
[ Type Classifier ] ──→ Classify using LLM + heuristics
        ↓
[ Video Processor ] ──→ Extract transcripts & keyframes
        ↓
[ Video Summarizer ] ──→ Generate per-video summaries
        ↓
[ Artifact Generator ] ──→ Create type-specific insights
        ↓
[ Storage Layer ] ──→ Save JSON + Markdown reports
```

### Core Components

- **Fetcher**: YouTube playlist metadata extraction
- **Classifier**: Smart type detection with custom type creation
- **Processor**: Video transcription and visual analysis
- **Summarizer**: Multimodal content analysis
- **Generator**: Type-aware artifact creation
- **Registry**: Extensible playlist type definitions
- **Storage**: Persistent data management

## 📚 Supported Playlist Types

### Built-in Types

| Type | Description | Artifacts Generated |
|------|-------------|-------------------|
| **Lecture** | Educational courses | Course summary, learning objectives, quiz |
| **Conference** | Tech talks, presentations | Executive summary, speaker insights, trends |
| **Tutorial** | How-to guides | Learning path, step guide, troubleshooting |
| **TV Series** | Entertainment content | Series summary, character analysis, themes |
| **Music** | Albums, playlists | Genre analysis, artist profile, themes |
| **Documentary** | Investigative content | Topic overview, fact summary, research guide |

### Custom Types

APIS automatically creates new type definitions when it encounters novel playlist categories, making it truly adaptive to any content type.

## 📊 Output Formats

### Generated Files

- **JSON Data**: Complete analysis with metadata
- **Markdown Report**: Human-readable summary
- **Type Registry**: Persistent type definitions

### Sample Markdown Report

```markdown
# Machine Learning Fundamentals

## Playlist Information
- **Creator:** Stanford University
- **Classification:** lecture (95.3% confidence)
- **Total Videos:** 25

## Course Summary
Comprehensive introduction to machine learning concepts...

## Learning Objectives
- Understand supervised vs unsupervised learning
- Implement basic algorithms in Python
- Apply ML to real-world problems

## Video Breakdown
1. **Introduction to ML** (45m) - Overview of field and applications
2. **Linear Regression** (38m) - Mathematical foundations and implementation
...
```

## 🔧 Advanced Usage

### Processing Configuration

```python
# Limit processing for testing
analyzer.analyze_playlist(url, max_videos=5)

# Custom storage location
analyzer = PlaylistAnalyzer()
analyzer.storage = PlaylistStorage("./custom_data")
```

### Type Registry Management

```python
from src.registry.type_registry import PersistentTypeRegistry

registry = PersistentTypeRegistry()
types = registry.list_types()
print(f"Registered types: {types}")
```

## 🐛 Troubleshooting

### Common Issues

**"No API key found"**
- Ensure `.env` file exists with correct API key
- Check `LLM_PROVIDER` matches your API key type

**"FFmpeg not found"**
- Install FFmpeg: `sudo apt install ffmpeg` (Linux) or `brew install ffmpeg` (macOS)

**"Quota exceeded"**
- Reduce `MAX_PLAYLIST_SIZE` in `.env`
- Use `--max-videos` flag to limit processing

**"Video processing failed"**
- Some videos may be private/restricted
- Check video accessibility in browser

### Performance Tips

- Start with `--max-videos 3` for testing
- Use `WHISPER_MODEL=tiny` for faster processing
- Set `MAX_VIDEO_LENGTH=1800` to skip long videos

## 📈 Cost Estimation

### API Costs (approximate)

| Provider | Per Video | 10 Videos | 50 Videos |
|----------|-----------|-----------|-----------|
| OpenAI (GPT-4o) | $0.02-0.05 | $0.20-0.50 | $1.00-2.50 |
| Anthropic (Claude) | $0.01-0.03 | $0.10-0.30 | $0.50-1.50 |

*Costs vary based on video length and content complexity*

## 🤝 Contributing

We welcome contributions! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

### Development Setup

```bash
# Install development dependencies
pip install -r requirements.txt

# Run tests
python -m pytest tests/

# Format code
black src/
isort src/
```

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **yt-dlp** for YouTube data extraction
- **OpenAI Whisper** for audio transcription
- **OpenAI GPT-4o** and **Anthropic Claude** for content analysis
- **FFmpeg** for video processing

## 📞 Support

- 📖 **Documentation**: [API.md](API.md)
- 🐛 **Issues**: Create an issue on GitHub
- 💬 **Discussions**: Use GitHub Discussions for questions

---

**Made with ❤️ for the YouTube analysis community**