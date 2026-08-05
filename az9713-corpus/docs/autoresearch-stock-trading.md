---
repo: autoresearch-stock-trading
description: AI that autonomously evolves stock trading strategies through trial and error. Inspired by Karpathy's autoresearch. For educational purposes only.
language: Python
stars: 1
forks: 1
created: 2026-03-14
updated: 2026-03-22
topics: 
is_fork: False
kb: 208
---

# autoresearch-stock-trading
# autoresearch-stock

**An AI that evolves stock trading strategies through autonomous trial and error.**

Inspired by [Karpathy's autoresearch](https://github.com/karpathy/autoresearch) — where an LLM autonomously improves a neural network training script — this project applies the same pattern to stock trading strategies. An LLM proposes changes to a trading strategy, a backtest harness evaluates them, and only improvements are kept. The loop runs unattended until it plateaus.

> **This project is for fun and educational purposes only. It is NOT intended for live trading or real investment decisions.** The Sharpe ratios reported are inflated by survivorship bias, and the strategies have not been validated on live markets. Do not risk real money based on these results.

## How It Works

```
┌─────────────┐     ┌──────────────┐     ┌──────────────┐
│  LLM edits  │────▶│  Backtest    │────▶│  Keep or     │
│  strategy.py│     │  evaluate.py │     │  discard?    │
└─────────────┘     └──────────────┘     └──────┬───────┘
       ▲                                        │
       └────────────────────────────────────────┘
                    repeat forever
```

1. The LLM reads the current strategy and its performance history
2. It proposes a hypothesis and writes new strategy code
3. The backtest harness evaluates it on historical data with transaction costs
4. If test_sharpe improves → keep. Otherwise → revert.
5. Everything is logged. The loop runs until a plateau is detected.

### Anti-Overfitting Design

The evaluation enforces strict temporal separation to prevent the AI from memorizing historical patterns:

| Period | Range | What the AI sees |
|--------|-------|------------------|
| Train | 2015–2020 | Full details (per-stock returns, drawdowns, monthly breakdown) |
| Test | 2021–2023 | **Only the Sharpe ratio** — one number, nothing else |
| Holdout | 2024–2025 | **Never touched** — reserved for final human review |

Transaction costs (15 bps per trade) penalize high-turnover strategies automatically.

## Results

Starting from a simple 200-day moving average crossover (Sharpe 2.44), the AI evolved a multi-layered strategy (Sharpe 7.86) in **32 iterations over 14 minutes** at zero cost (Gemini free tier).

![Strategy Evolution](progress.png)

The biggest improvement came from adding an RSI momentum filter — one change that more than doubled the Sharpe ratio. Note the sharp oscillations after iteration 24 — those are repeated crashes where the AI tried to write more advanced code but kept hitting the same numpy/pandas type confusion bug. The crashes are reverted (plotted as 0), creating the zigzag pattern. See the [crash analysis in REPORT_CONCISE.md](REPORT_CONCISE.md#the-oscillations-after-iteration-24) for a full breakdown of what went wrong and why.

## Quick Start

### 1. Get the data

Download Stooq daily US NASDAQ stock data and place it at:
```
data/daily/us/nasdaq stocks/{1,2,3}/*.us.txt
```

Update `DATA_DIR` in `config.py` to point to the parent directory containing `1/`, `2/`, `3/`.

### 2. Install dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure

Create a `.env` file:
```
PROVIDER=gemini
GOOGLE_API_KEY=your_key_here

MAX_ITERATIONS=100
MAX_COST_USD=0
PLATEAU_WINDOW=10
```

### 4. Run

```bash
# Run the autonomous experiment loop
python run_autoresearch.py

# Generate progress.png and REPORT.md after the run
python generate_report.py
```

### 5. Or run just the backtest

```bash
# Evaluate the current strategy without the LLM loop
python evaluate.py
```

## Project Structure

```
├── strategy.py           # The ONLY file the AI modifies — trading logic
├── evaluate.py           # Walk-forward backtest harness (read-only)
├── config.py             # Constants: time splits, costs, universe (read-only)
├── data_loader.py        # Stooq CSV loading (read-only)
├── run_autoresearch.py   # Autonomous experiment runner (uses Gemini)
├── generate_report.py    # Generates progress.png and REPORT.md
├── program.md            # Agent instructions (for Claude Code usage)
├── requirements.txt      # pandas, numpy, google-genai, matplotlib
├── REPORT_CONCISE.md     # Detailed experiment report
└── progress.png          # Evolution plot
```

## Stock Universe

24 curated NASDAQ stocks across 3 Stooq subdirectories:

- **Subdir 1**: AAPL, ABNB, ADBE, AMD, AMZN, AVGO, CDNS, COST, CSCO, GOOG, GOOGL
- **Subdir 2**: INTC, META, MRNA, MSFT, NFLX, NVDA, PANW, PYPL, QCOM, REGN, SBUX, SNPS
- **Subdir 3**: TSLA

## Key Learnings

- **Combining signals beats refining one.** Adding RSI to a moving average crossover doubled performance. Further tuning of either signal alone yielded marginal gains.
- **Position sizing is secondary.** Inverse volatility weighting, ATR, Parkinson vol — all produced tiny improvements compared to signal selection.
- **The AI hits a wall.** After exhausting simple improvements, the LLM repeatedly crashed trying to write more complex code (cross-sectional ranking, multi-indicator combinations). Feeding error messages back would help.
- **Survivorship bias inflates everything.** A Sharpe of 7.86 on 24 hand-picked tech winners is not realistic. The holdout period exists for honest assessment.

## Credits

- Pattern: [Karpathy's autoresearch](https://github.com/karpathy/autoresearch)
- Data: [Stooq](https://stooq.com/db/h/)
- LLM: Gemini 2.5 Flash (free tier)
- Built with [Claude Code](https://claude.ai/claude-code)

## Disclaimer

This is a research/learning project. The strategies, results, and code are provided as-is for educational purposes. **Do not use this for live trading.** Past performance on historical data — especially survivorship-biased data — does not predict future results. The authors assume no responsibility for any financial losses.
