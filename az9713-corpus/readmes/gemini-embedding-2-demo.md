# Multimodal Search — Gemini Embedding 2 Demo

A browser-based semantic search playground that finds conceptually similar items across text, images, and audio simultaneously. Type a word, upload an image, or upload an audio clip — the app ranks all 30 items in its library by how closely they match your query, across all three content types at once.

This is an extended clone of the [Multimodal Search](https://aistudio.google.com/apps/bundled/multimodal_search?showPreview=true&showAssistant=true) app from Google AI Studio, with the addition of a **2D embedding map** that visualises the entire vector space using PCA.

Powered by [`gemini-embedding-2-preview`](https://ai.google.dev/gemini-api/docs/embeddings).

---

## What's new vs the original

| Feature | Original AI Studio app | This repo |
|---------|----------------------|-----------|
| Tri-lane search (text / image / audio) | ✓ | ✓ |
| Item inspector with embedding vector | ✓ | ✓ |
| Add custom text, image, audio items | ✓ | ✓ |
| **2D embedding map (PCA scatter plot)** | ✗ | ✓ |
| **Full documentation** (`docs/`) | ✗ | ✓ |

---

## Embedding map

The map view projects all 3072-dimensional embedding vectors down to 2D using PCA (Principal Component Analysis) and renders them as an interactive scatter plot. Toggle it with the ⊞ grid icon in the top-right header.

- **Dots are coloured by modality** — blue = text, purple = image, green = audio
- **Without a search seed**, natural clusters appear: images group on one side of the canvas, text and audio on the other, because Gemini Embedding 2 encodes visual content differently from language-based content
- **With a search seed**, the seed appears as a yellow dot; strong matches glow and show their similarity percentage; non-matches fade
- **Hover** any dot to see its name; **click** to open the item inspector

PCA preserves global structure (large cluster separations) but loses fine-grained local distances. It runs in milliseconds in the browser, which is why it can recompute every time the seed changes. See [`docs/concepts/embedding-map.md`](docs/concepts/embedding-map.md) for a step-by-step explanation.

![Embedding map — "apple" seed](docs/apple.jpg)

*Searching for "apple" in the embedding map (dark mode). The yellow dot is the seed. The green dot to its right is `apple_crunch.wav` — a cross-modal match the model finds semantically related. The image cluster (purple dots, left) is spatially separated from the text/audio cluster, showing how PCA exposes the structural difference between visual and language-based embeddings. Non-matching items are faded.*

---

## Run locally

**Prerequisites:** Node.js 18+, a [Gemini API key](https://aistudio.google.com)

1. Install dependencies:
   ```bash
   npm install
   ```

2. Create `.env.local` in the project root:
   ```bash
   NEXT_PUBLIC_GEMINI_API_KEY=your-api-key-here
   ```

3. Start the dev server:
   ```bash
   npm run dev
   ```

4. Open [http://localhost:3000](http://localhost:3000)

The app loads and initialises embeddings for all 30 dataset items (≈15 seconds on first load). Search, upload files, or switch to the map view once initialisation completes.

> **Note:** `NEXT_PUBLIC_GEMINI_API_KEY` is the correct variable name. The original AI Studio README uses `GEMINI_API_KEY`, which does not work.

---

## Documentation

Full documentation lives in [`docs/`](docs/):

| Doc | Contents |
|-----|---------|
| [`docs/overview/what-is-this.md`](docs/overview/what-is-this.md) | Mental model, architecture |
| [`docs/getting-started/quickstart.md`](docs/getting-started/quickstart.md) | Step-by-step setup |
| [`docs/concepts/embeddings.md`](docs/concepts/embeddings.md) | Cosine similarity, what 3072 dims means |
| [`docs/concepts/embedding-map.md`](docs/concepts/embedding-map.md) | PCA: how high-dim vectors become 2D positions |
| [`docs/concepts/gemini-embedding-2.md`](docs/concepts/gemini-embedding-2.md) | How the model is used for text, images, and audio |
| [`docs/concepts/multimodal-search.md`](docs/concepts/multimodal-search.md) | Lane view, similarity thresholds |
| [`docs/architecture/system-design.md`](docs/architecture/system-design.md) | Component map, data flows, design decisions |
| [`docs/troubleshooting/common-issues.md`](docs/troubleshooting/common-issues.md) | Common failures and fixes |

---

## Tech stack

- **Next.js 15** (App Router) + **React 19** + **TypeScript**
- **Gemini API** via `@google/genai` — `gemini-embedding-2-preview` model
- **Tailwind CSS 4** + **Motion** (animations)
- **ml-pca** — PCA for the embedding map
- **D3** — scales for SVG coordinate mapping
