---
repo: cme295-study-guide
description: Comprehensive study guide for Stanford CME 295: Transformers and Large Language Models (Fall 2025)
language: HTML
stars: 2
forks: 2
created: 2025-12-15
updated: 2026-06-28
topics: 
is_fork: False
kb: 1774
---

# cme295-study-guide
# CME 295: Transformers and Large Language Models - Course Materials

A comprehensive collection of lecture notes, transcripts, and study materials for Stanford's CME 295 course on Transformers and Large Language Models (Fall 2025).

## Table of Contents

- [Overview](#overview)
- [Quick Start](#quick-start)
- [Directory Structure](#directory-structure)
- [Lecture Notes](#lecture-notes)
- [PDF Generation](#pdf-generation)
- [Requirements](#requirements)
- [Troubleshooting](#troubleshooting)

---

## Overview

This repository contains:

1. **Lecture Transcripts** - Raw transcripts from CME 295 video lectures (9 lectures)
2. **Comprehensive Lecture Notes** - Detailed, self-contained notes with properly rendered mathematical equations
3. **PDF Generation Tools** - Python scripts to convert Markdown notes to professionally formatted PDFs
4. **Course Slides** - Original lecture slides in PDF format

### What Problem Does This Solve?

Students often need:
- Comprehensive notes that go beyond what's covered in video lectures
- Properly formatted mathematical equations (not raw LaTeX)
- Self-contained documents that can be studied without external resources
- Printable PDFs for offline study

This project provides all of the above through an automated pipeline.

### Project Status

**All 9 lectures are complete** with comprehensive notes and PDF outputs.

---

## Quick Start

### View the Lecture Notes

All lecture PDFs are in the `notes/` directory:
```
notes/CME295_Lecture1_Notes.pdf
notes/CME295_Lecture2_Notes.pdf
...
notes/CME295_Lecture9_Notes.pdf
```

Simply open these PDFs in any PDF viewer (Adobe Reader, Chrome, etc.).

### Regenerate a PDF

If you've modified the Markdown source:

```bash
cd notes
python convert_to_pdf.py 1    # For Lecture 1
python convert_to_pdf.py 9    # For Lecture 9
```

---

## Directory Structure

```
cme295_comet/
├── README.md                           # This file - main documentation
├── CLAUDE.md                           # AI assistant context file
├── DEVELOPMENT.md                      # Developer documentation
├── CHANGELOG.md                        # Version history
├── LICENSE                             # MIT License
├── .gitignore                          # Git ignore rules
│
├── notes/                              # Lecture notes and tools
│   ├── lecture*_notes.md               # Markdown source files (editable)
│   ├── CME295_Lecture*_Notes.pdf       # Generated PDFs (output)
│   ├── convert_to_pdf.py               # PDF generation script
│   └── lecture*_notes.html             # Intermediate HTML files (generated)
│
├── slides/                             # Original lecture slides (not in repo)
│   └── fall25-cme295-lecture*.pdf      # ⚠️ Copyrighted - obtain separately
│
└── transcripts/                        # Raw lecture transcripts (not in repo)
    └── transcript_lec*.txt             # ⚠️ Copyrighted - obtain separately
```

> **Note:** The `slides/` and `transcripts/` directories contain copyrighted Stanford
> course materials and are not included in this repository. You'll need to obtain
> these from the official course resources if you want to regenerate notes.

---

## Lecture Notes

### Complete Lecture List

| Lecture | Topic | Key Concepts | PDF |
|---------|-------|--------------|-----|
| **1** | Foundations & Transformers | Tokenization, Word2Vec, RNN/LSTM, Self-Attention, Multi-Head Attention | `CME295_Lecture1_Notes.pdf` |
| **2** | Transformer Improvements | RoPE, Grouped Query Attention, Pre-norm, BERT/GPT/T5 variants | `CME295_Lecture2_Notes.pdf` |
| **3** | Large Language Models | Mixture of Experts, Temperature, Decoding strategies | `CME295_Lecture3_Notes.pdf` |
| **4** | Training LLMs | Scaling Laws, Flash Attention, Parallelism, Pre-training/SFT pipeline | `CME295_Lecture4_Notes.pdf` |
| **5** | Preference Tuning & RLHF | Bradley-Terry Model, Reward Modeling, PPO, Reward Hacking | `CME295_Lecture5_Notes.pdf` |
| **6** | Reasoning Models | Chain-of-Thought, GRPO, Verifiable Rewards | `CME295_Lecture6_Notes.pdf` |
| **7** | Agentic LLMs | RAG, Bi-Encoder/Cross-Encoder, Tool Calling | `CME295_Lecture7_Notes.pdf` |
| **8** | LLM Evaluation | LLM-as-Judge, Biases, MMLU/GSM8K Benchmarks | `CME295_Lecture8_Notes.pdf` |
| **9** | Course Synthesis & Frontiers | Vision Transformers, VLMs, Diffusion LLMs, Future Research | `CME295_Lecture9_Notes.pdf` |

### Exam Coverage

- **Midterm:** Lectures 1-4
- **Final:** Lectures 5-8
- **Supplementary (not on final):** Lecture 9

### Mathematical Content

All mathematical expressions are rendered as proper formatted equations using MathML, including:
- Greek letters, fractions, square roots
- Subscripts, superscripts, matrices
- Summation and product notation
- Piecewise functions (cases)

---

## PDF Generation

### How It Works

```
Markdown (.md)
     │
     ▼
┌─────────────────────────────────────┐
│  1. Read Markdown source            │
│  2. Extract LaTeX expressions       │
│  3. Convert LaTeX → MathML          │
│  4. Convert Markdown → HTML         │
│  5. Apply CSS styling               │
│  6. Render HTML → PDF (WeasyPrint)  │
└─────────────────────────────────────┘
     │
     ▼
PDF Output
```

### Generate Single Lecture

```bash
cd notes
python convert_to_pdf.py <lecture_number>
```

### Generate All Lectures

**Bash:**
```bash
cd notes
for i in 1 2 3 4 5 6 7 8 9; do python convert_to_pdf.py $i; done
```

**PowerShell:**
```powershell
cd notes
1..9 | ForEach-Object { python convert_to_pdf.py $_ }
```

### Key Technologies

| Component | Technology | Purpose |
|-----------|------------|---------|
| Markdown Parser | `markdown` (Python) | Convert MD to HTML |
| Math Rendering | `latex2mathml` | LaTeX → MathML conversion |
| PDF Generation | `weasyprint` | HTML/CSS → PDF |

---

## Requirements

### Python Version
- Python 3.10 or higher

### Python Packages

```bash
pip install markdown weasyprint latex2mathml
```

| Package | Purpose |
|---------|---------|
| `markdown` | Markdown to HTML conversion |
| `weasyprint` | HTML to PDF rendering |
| `latex2mathml` | LaTeX to MathML conversion |

### System Dependencies (WeasyPrint)

**Windows:** Usually bundled with WeasyPrint wheel.

**Ubuntu/Debian:**
```bash
sudo apt-get install libpango-1.0-0 libpangocairo-1.0-0 libgdk-pixbuf2.0-0
```

**macOS:**
```bash
brew install pango gdk-pixbuf libffi
```

---

## Troubleshooting

### 1. "Permission denied" when generating PDF

**Cause:** The PDF file is open in another application.

**Solution:** Close the PDF viewer and try again.

### 2. Math not rendering correctly

**Cause:** LaTeX syntax error or unsupported command.

**Solution:**
- Check the console output for warnings about failed conversions
- Simplify complex expressions
- Use `\mathrm{}` instead of `\text{}` for text in math mode

### 3. WeasyPrint font warnings

**Cause:** Missing fonts on the system.

**Solution:** These warnings are usually harmless. The PDF will use fallback fonts.

### 4. GLib warnings on Windows

**Cause:** Windows-specific UWP app warnings

**Solution:** Ignore - these are harmless and don't affect PDF generation.

---

## Usage Examples

### Viewing Notes

```bash
# Open the PDF directly
start notes/CME295_Lecture9_Notes.pdf    # Windows
open notes/CME295_Lecture9_Notes.pdf     # macOS
xdg-open notes/CME295_Lecture9_Notes.pdf # Linux
```

### Editing Notes

1. Edit the Markdown source:
   ```bash
   notepad notes/lecture9_notes.md   # Windows
   code notes/lecture9_notes.md      # VS Code
   ```

2. Regenerate the PDF:
   ```bash
   cd notes && python convert_to_pdf.py 9
   ```

### Writing Mathematical Expressions

**Inline Math:** Use single dollar signs
```markdown
The formula $E = mc^2$ is famous.
```

**Display Math:** Use double dollar signs
```markdown
$$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
```

---

## Contributing

### Improving Existing Notes

1. Edit the Markdown source file in `notes/`
2. Test by generating HTML (check console for LaTeX errors)
3. Generate final PDF
4. Update CHANGELOG.md with your changes

### Adding New Content

1. Follow the existing document structure
2. Use consistent LaTeX notation (see CLAUDE.md for conventions)
3. Include practice problems at the end

---

## File Descriptions

| File | Description |
|------|-------------|
| `README.md` | This file - user documentation |
| `CLAUDE.md` | AI assistant context and project overview |
| `DEVELOPMENT.md` | Technical documentation for developers |
| `CHANGELOG.md` | Version history and change log |
| `.gitignore` | Git ignore rules |

---

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

**Important:** The original course slides and transcripts are copyrighted by Stanford University
and are not included in this repository. The generated lecture notes are derivative educational
works created for personal study purposes.

---

## Acknowledgments

- **Instructors:** Afshine Amidi and Shervine Amidi
- **Course:** CME 295 - Transformers and Large Language Models, Stanford University
- **Resources:** Course textbook "Super Study Guide - Transformer LLMs"
- **Notes Generation:** All lecture notes were created by [Claude Code](https://claude.ai/claude-code) powered by Claude Opus 4.5 (Anthropic)
