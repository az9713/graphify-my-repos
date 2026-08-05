---
repo: image-search-engine-tutorial
description: AI-powered image search engine using Jina CLIP v2 and Qdrant. Based on NeuralNine/youtube-tutorials, enhanced with comprehensive documentation and HNSW deep dive.
language: Python
stars: 0
forks: 1
created: 2026-03-10
updated: 2026-03-10
topics: 
is_fork: False
kb: 49
---

# image-search-engine-tutorial
# ImageSearchEngine

An AI-powered image search engine that lets you find images using natural language queries. Upload images, tag them, and search through your collection by describing what you're looking for in plain English.

## Origin

This project is based on the **ImageSearchEngine** from
[NeuralNine/youtube-tutorials](https://github.com/NeuralNine/youtube-tutorials)
on GitHub. The original code was written by [NeuralNine](https://github.com/NeuralNine)
as part of their YouTube tutorial series on programming and machine learning.

This fork enhances the original with:
- **`--images` flag** -- point to any image folder instead of the hardcoded `images/` directory
- **Comprehensive documentation** -- architecture deep dives, developer guide, user guide, and a zero-to-hero study plan
- **HNSW algorithm deep dive** -- detailed explanation of how the vector search index works internally, including insertion, search, parameters, and tradeoffs

**How it works:** The application uses a multimodal AI model (Jina CLIP v2) to understand both images and text in the same "language" (mathematical vectors). When you search for "sunset on a beach," the AI converts your words into a vector and finds images whose vectors are most similar -- even if those images were never explicitly tagged with those words.

```
+------------------+       +-------------------+       +------------------+
|                  |       |                   |       |                  |
|   Web Browser    | <---> |   Flask Server    | <---> |  Qdrant Vector   |
|   (Frontend)     |       |   (Backend)       |       |  Database        |
|                  |       |                   |       |                  |
+------------------+       +--------+----------+       +------------------+
                                    |
                           +--------+----------+
                           |                   |
                           |  Jina CLIP v2     |
                           |  (AI Model)       |
                           |                   |
                           +-------------------+
```

## Features

- **Semantic Image Search**: Search images by natural language description (e.g., "a red car" finds car images even without tags)
- **Tag-Based Search**: Add tags to images during upload for exact-match filtering
- **Hybrid Search**: Combines tag matches (priority) with AI-powered semantic matches
- **Custom Image Folder**: Use `--images /path/to/folder` to index and serve images from any directory
- **GPU Acceleration**: Automatically uses NVIDIA GPU if available, falls back to CPU
- **Batch Indexing**: CLI tool to index an entire folder of images at once
- **Local Storage**: All data stays on your machine -- no cloud services required

## Quick Start

### Prerequisites

- **Python 3.12 or newer** -- [Download here](https://www.python.org/downloads/)
- **Git** -- [Download here](https://git-scm.com/downloads)
- **(Optional) NVIDIA GPU** with CUDA 12.1 drivers for faster processing

### Step 1: Clone and Navigate

```bash
git clone <repository-url>
cd ImageSearchEngine
```

### Step 2: Install Dependencies

**Option A -- Using uv (recommended, faster):**
```bash
pip install uv
uv sync
```

**Option B -- Using pip:**
```bash
pip install -e .
```

> **Note:** First run will download the AI model (~1.7 GB). This only happens once.

### Step 3: Add Some Images

Place image files (JPG, PNG, etc.) into the `images/` folder:
```bash
mkdir images
# Copy some images into the images/ folder
```

Or use images from any folder on your system (see Step 4).

### Step 4: Build the Search Index

```bash
# Default (uses ./images/ folder)
python main.py

# Or specify a custom image folder
python main.py --images /path/to/your/photos
```

This scans all images in the folder and creates searchable vectors.

### Step 5: Launch the Web App

```bash
# Default (serves from ./images/)
python flask_app.py

# Or use the same custom folder
python flask_app.py --images /path/to/your/photos
```

> **Important:** Use the same `--images` path for both commands.

Open your browser to **http://localhost:5000** and start searching!

## Project Structure

```
ImageSearchEngine/
  flask_app.py        # Web application (Flask server with upload + search)
  main.py             # CLI tool for batch indexing images
  pyproject.toml      # Project dependencies and configuration
  templates/
    index.html        # Web interface (upload form + search form + results)
  images/             # Default image storage directory (created at runtime)
  image_store/        # Vector database files (created at runtime)
  docs/
    ARCHITECTURE.md   # Detailed system architecture with diagrams
    DEVELOPER_GUIDE.md# Complete guide for future developers
    USER_GUIDE.md     # User manual with 10+ example use cases
    STUDY_PLAN.md     # Zero-to-hero learning plan
```

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| [Architecture](docs/ARCHITECTURE.md) | Developers | System design, component diagrams, data flows, **HNSW deep dive** |
| [Developer Guide](docs/DEVELOPER_GUIDE.md) | Developers | Setup, codebase walkthrough, how to extend |
| [User Guide](docs/USER_GUIDE.md) | End Users | How to use the app with 10+ example use cases |
| [Study Plan](docs/STUDY_PLAN.md) | Learners | Zero-to-hero learning plan covering theory + code |
| [CLAUDE.md](CLAUDE.md) | AI Assistants | Project context for AI-assisted development |

## Technology Stack

| Component | Technology | Purpose |
|-----------|-----------|---------|
| Web Framework | Flask 3.x | HTTP server, routing, template rendering |
| AI Model | Jina CLIP v2 | Converts images and text into comparable vectors |
| Vector Database | Qdrant | Stores and searches high-dimensional vectors (HNSW index) |
| ML Framework | PyTorch 2.x | GPU-accelerated tensor computation |
| Image Processing | Pillow (PIL) | Loading and processing image files |
| Model Hub | Sentence Transformers + HuggingFace | Model loading and inference |

## License

See LICENSE file for details.
