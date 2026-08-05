# Transformers.js — A Deep-Dive Tutorial

Onboarding documentation for [🤗 Transformers.js](https://github.com/huggingface/transformers.js) — built to take someone with **zero prior knowledge** from "what is this?" to running every demo in the examples collection without friction.

The full docs live in **[`docs/`](docs/)** — start at **[`docs/index.md`](docs/index.md)**.

---

## Why this exists

Transformers.js runs real machine-learning models — LLMs, Whisper, image models — **directly in the browser with no server**. That's remarkable, but the official docs assume you already know the Hugging Face ecosystem. This tutorial fills the gap with two goals:

1. **Fastest possible onboarding** for someone who has never touched transformers.js.
2. **Run every example** in the examples repo without hitting a wall.

## The two reference repositories

This tutorial documents two upstream Hugging Face projects:

| Repo | What it is | What we documented |
|------|-----------|--------------------|
| [**huggingface/transformers.js**](https://github.com/huggingface/transformers.js) | The library itself (`@huggingface/transformers`, v4.2.0 source) | Pipelines, the `Auto*` API, devices/dtypes, model loading & caching, generation/streaming, internals |
| [**huggingface/transformers.js-examples**](https://github.com/huggingface/transformers.js-examples) | ~58 standalone demo apps | A preflight + universal run recipe, plus a full catalog of every example with exact commands, GPU needs, and download sizes |

Everything here was written by reading those repos directly — every API table is checked against the v4.2.0 source, not from memory.

## ⚡ Highlight: how WebGPU lets a browser run an LLM

The centerpiece of this tutorial is a from-scratch explanation of the thing that surprises everyone — **how a billion-parameter language model fits in a browser tab and runs fast enough to be usable.** It comes down to two tricks: **quantization** (shrink the weights to fit in GPU memory) and **WebGPU** (do the matrix math on the GPU in parallel).

### ▶ Try the live interactive explainer

[![Interactive WebGPU explainer — quantization lab, VRAM tank, ONNX pipeline, and a WASM-vs-WebGPU token race](docs/assets/webgpu-explainer-preview.png)](https://az9713.github.io/transformer.js-tutorial/docs/concepts/how-browsers-run-models.html)

**→ [Open it as a live web page](https://az9713.github.io/transformer.js-tutorial/docs/concepts/how-browsers-run-models.html)** (hosted on GitHub Pages — renders as a real page, nothing to download)

The page has no build step and four hands-on widgets:

| Widget | What you do |
|--------|-------------|
| 🟠 **Quantization lab** | Pick a model × precision (fp32 → q4f16); watch the size bars shrink and the "bits per weight" grid light up |
| 🟠 **VRAM fit tank** | Drag your GPU memory; the tank turns red + "✗ TOO BIG" when the model overflows |
| 🔵 **ONNX pipeline** | Animated PyTorch → ONNX → Runtime, forking into slow WASM vs fast WebGPU |
| 🔵 **Token race** | Generate the same sentence at ~1.5 tok/s (CPU) vs ~24 tok/s (GPU), side by side |

### The three written pieces behind it

- **[How a browser runs a language model](docs/concepts/how-browsers-run-models.md)** — the concept, from "a model is just numbers" through quantization memory math, the ONNX → WASM/WebGPU execution path, and why only small models fit.
- **[Interactive explainer source](docs/concepts/how-browsers-run-models.html)** — the no-build HTML behind the live page above. Open the file directly and it just runs, mirroring the `vanilla-js` example it describes.
- **[WebGPU guide](docs/guides/webgpu.md)** — the practical side: enabling it per browser, feature-detecting in code, and debugging the common failures.

## What's in the docs

```
docs/
├── index.md                         ← navigation hub — start here
├── overview/                        what it is · key-concepts glossary
├── getting-started/                 prerequisites · quickstart · onboarding
├── concepts/                        how-browsers-run-models (+ interactive .html)
│                                    pipelines · models/tokenizers/processors
│                                    devices-and-dtypes · model-loading-and-caching
│                                    generation-and-streaming
├── guides/                          running-the-examples · examples-catalog
│                                    server-side-node · webgpu
├── reference/                       pipeline-tasks · env-settings · api-exports
├── architecture/                    library-internals
└── troubleshooting/                 common-issues
```

### Suggested reading path

1. **[Onboarding](docs/getting-started/onboarding.md)** — zero-to-confident narrative (~15 min).
2. **[Quickstart](docs/getting-started/quickstart.md)** — first inference in under 5 minutes (CDN path needs no install).
3. **[How a browser runs a model](docs/concepts/how-browsers-run-models.md)** — the WebGPU/quantization deep dive (+ the interactive version).
4. **[Running the examples](docs/guides/running-the-examples.md)** + **[catalog](docs/guides/examples-catalog.md)** — get the demos going.

## The development journey

This tutorial was built in a single guided session that doubled as a tour of the codebase:

1. **Audited both repos** — surveyed all ~58 examples (commands, frameworks, model sizes, WebGPU/mic/webcam needs) and mapped the library's source architecture.
2. **Designed the information architecture** — a unified docs site spanning library *and* examples, so a newcomer never has to cross-reference two projects.
3. **Wrote 20+ docs, verified against source** — the pipeline task list, `env` fields, dtype/device tables, and streamer options were read straight from the v4.2.0 source rather than recalled.
4. **Ran an example end-to-end** — `node-esm` was executed on Windows to seed the quickstart and troubleshooting docs with *real* output, not imagined output.
5. **Caught the version trap** — the examples pin v3.x from npm while the library source is v4.2.0; defaults for some tasks differ, and every doc now flags this.
6. **Built the interactive WebGPU explainer** — turning the hardest concept into something you can poke at, with no build step (mirroring the `vanilla-js` example it describes).

> **Note:** this is community tutorial material, not official Hugging Face documentation. For the canonical API reference, see the [official docs](https://huggingface.co/docs/transformers.js).

## License

Documentation in this repository is provided under the [MIT License](LICENSE). Transformers.js and its examples are © Hugging Face under the Apache-2.0 license.
