---
repo: autoresearch-tinystories
description: AI-driven hyperparameter optimization on TinyStories using Karpathy autoresearch framework. 43 experiments, 8.9% BPB improvement, ~$3 total cost.
language: Python
stars: 0
forks: 1
created: 2026-03-17
updated: 2026-03-17
topics: 
is_fork: False
kb: 155
---

# autoresearch-tinystories
# Autoresearch TinyStories

**An AI that autonomously improves another AI — no human in the loop.**

This project replicates [Andrej Karpathy's autoresearch framework](https://github.com/karpathy/autoresearch) on the TinyStories dataset, demonstrating how an AI agent (Google Gemini) can autonomously optimize a language model by running experiments, keeping improvements, and discarding failures.

Inspired by the video **["Karpathy's Autoresearch: We Achieved Near-Human Scores in 2 Hours!"](https://www.youtube.com/watch?v=9jxrmk_Xses&t=662s)** by Tonbi (Onchain AI Garage), which walks through the entire autoresearch workflow and demonstrates the framework in action.

## What is This?

A small GPT-style language model learns to write children's stories. An AI researcher (Gemini) repeatedly modifies the training code, runs 5-minute experiments, and keeps only the changes that improve the model. Over 43 experiments, the model improved by **8.9%** — costing just **~$3 total** in compute.

```
Experiment  0: val_bpb = 0.521  (baseline — barely coherent output)
Experiment 23: val_bpb = 0.499  (Gemini Flash finds hyperparameter sweet spots)
Experiment 41: val_bpb = 0.475  (Gemini Pro discovers "more steps > bigger batches")
```

## Results at a Glance

![Autoresearch TinyStories — 43 experiments on RTX 4090](docs/progress.jpg)

| Metric | Value |
|--------|-------|
| Baseline BPB | 0.521 |
| Final Best BPB | 0.475 |
| Improvement | 8.9% |
| Total Experiments | 43 |
| Kept Improvements | 12 |
| Crashes | 5 |
| GPU | RTX 4090 (RunPod) |
| Total Cost | ~$3.05 |
| Time | ~5 hours |

See [docs/experiment-log.md](docs/experiment-log.md) for the full experiment history and analysis.

Open [docs/progress_chart.html](docs/progress_chart.html) in a browser for an interactive chart of all 43 experiments.

## How It Works (30-Second Version)

1. You have a training script (`train.py`) that trains a small language model on children's stories
2. An AI agent (Gemini) reads the code and proposes ONE modification
3. The modified code runs for exactly 5 minutes
4. If the result is better → keep it. If worse → revert. If it crashes → revert.
5. Repeat 30-50 times. The code evolves like natural selection.

For the full explanation, see [docs/how-autoresearch-works.md](docs/how-autoresearch-works.md).

## Background: What are TinyStories, Autoresearch, and BPB?

New to these concepts? Start here:

- **[docs/background.md](docs/background.md)** — What is TinyStories? What is autoresearch? What does BPB mean? Why does any of this matter?
- **[docs/how-autoresearch-works.md](docs/how-autoresearch-works.md)** — Deep dive into the framework, the model architecture, and the experiment loop
- **[docs/experiment-log.md](docs/experiment-log.md)** — Complete results with analysis and key insights

## Run It Yourself

### Option 1: RunPod (Recommended — ~$3 for 30+ experiments)

Best results. Uses an RTX 4090 GPU on RunPod cloud.

1. Read [runpod/README.md](runpod/README.md) for step-by-step setup
2. Upload the 6 files from `runpod/` to your pod
3. Run `bash setup.sh && bash baseline.sh && python run.py --experiments 30`

### Option 2: Google Colab (Free — limited by T4 GPU)

Free but slower, smaller model, and Colab may disconnect.

1. Read [docs/colab-setup-guide.md](docs/colab-setup-guide.md)
2. Upload `autoresearch_tinystories_colab.ipynb` to Colab
3. Set runtime to T4 GPU and run all cells

## Project Structure

```
autoresearch-tinystories/
├── README.md                           # This file
├── runpod/                             # Scripts to run it yourself (RTX 4090)
│   ├── README.md                       # Step-by-step RunPod instructions
│   ├── prepare.py                      # Data download + tokenizer (read-only)
│   ├── train.py                        # Training script (starting point — AI modifies this)
│   ├── program.md                      # Research plan for the AI
│   ├── run.py                          # Autonomous experiment loop
│   ├── setup.sh                        # One-time setup
│   └── baseline.sh                     # Run baseline experiment
├── results/                            # Output from our 43-experiment run
│   ├── results.tsv                     # All 43 experiment results
│   ├── train_final.py                  # Final best training script (evolved by AI)
│   └── run.log                         # Last training run output
└── docs/                               # Documentation
    ├── background.md                   # TinyStories, autoresearch, BPB explained
    ├── how-autoresearch-works.md       # Framework deep dive
    ├── experiment-log.md               # Full results + analysis
    ├── progress_chart.html             # Interactive results chart (open in browser)
    ├── colab-setup-guide.md            # Google Colab setup for beginners
    ├── what-to-expect.md               # What you'll see during runs
    └── plot_results.py                 # Generate progress chart (matplotlib)
```

## Credits

- **[Andrej Karpathy](https://github.com/karpathy/autoresearch)** — Created the autoresearch framework
- **[Tonbi / Onchain AI Garage](https://www.youtube.com/watch?v=9jxrmk_Xses&t=662s)** — Video walkthrough that inspired this project
- **[TinyStories](https://arxiv.org/abs/2305.07759)** (Eldan & Li, 2023) — The dataset
- **Google Gemini** — AI researcher agent (Flash + Pro)
- **RunPod** — GPU cloud provider

## License

This project is for educational and research purposes. The autoresearch framework is by Andrej Karpathy. TinyStories is by Ronen Eldan and Yuanzhi Li (Microsoft Research).
