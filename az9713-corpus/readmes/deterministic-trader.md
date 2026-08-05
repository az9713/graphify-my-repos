# Deterministic Trading System

A Python implementation of the quantitative research infrastructure described in [**"Everything I've Learned Trading With Claude In 18 Minutes"**](https://www.youtube.com/watch?v=CPkrCoIbBIA) — covering Layers 1 and 2 of the three-layer architecture: the macro deployment gate and the quantitative stock scanner.

> "Claude is useful for trading when it helps you build, validate, and stress-test deterministic systems. It is dangerous when treated as a predictive black box."

---

## What this implements

The video proposes a three-layer trading system. This repo implements the two deterministic layers:

| Layer | Description | Status |
|---|---|---|
| **Layer 1 — Macro deployment gate** | Scores 6 macro signals (VIX, credit spreads, market breadth, put/call ratio, VIX term structure, factor crowding) into a composite deployment decision | Implemented |
| **Layer 2 — Quantitative scanner** | Ranks stocks on 8 factors (momentum, relative strength, volatility, sector-adjusted performance, liquidity, trend quality, earnings yield, earnings revision strength) | Implemented |
| Layer 3 — Claude analyst overlay | Non-deterministic qualitative review of filtered candidates via Claude API | Not in scope |

Layers 1 and 2 are fully deterministic: same data in → same result out, every time. This makes them backtestable, reproducible, and validatable.

---

## Demo: Magnificent 7 paper trade

```bash
pip install numpy pandas scipy pytest yfinance lxml requests
python mag7_paper_trade.py
```

Downloads real market data, runs both layers against AAPL, MSFT, NVDA, AMZN, GOOGL, META, TSLA, and writes a full report to `MAG7_PAPER_TRADE_REPORT.md`.

Sample output:

```
  Macro gate score : 74.4  (FULL)
  Size factor      : 100%
  Scanner picks    : GOOGL, AMZN, NVDA, AAPL, MSFT

  Scanner scores per stock (rank-normalised 0-1):
  Ticker    Comp     Mom      RS     Vol     Sec     Liq      TQ      EY      ER
  GOOGL    0.843   1.000   1.000   0.571   1.000   0.143   0.857   0.714   1.000  <--
  AMZN     0.740   0.571   0.857   0.714   0.857   0.429   1.000   0.571   0.857  <--
  NVDA     0.666   0.857   0.714   0.429   0.714   1.000   0.714   0.286   0.429  <--
  AAPL     0.629   0.714   0.571   1.000   0.571   0.571   0.571   0.429   0.571  <--
  MSFT     0.509   0.143   0.429   0.857   0.429   0.714   0.429   0.857   0.714  <--
  META     0.283   0.286   0.143   0.286   0.143   0.286   0.143   1.000   0.143
  TSLA     0.331   0.429   0.286   0.143   0.286   0.857   0.286   0.143   0.286
```

---

## What's included

Beyond the two signal layers, the repo includes the full validation and risk infrastructure needed to evaluate a strategy before trusting it with capital:

- **Backtesting engine** — equal-weight portfolio simulation with realistic transaction costs
- **Walk-forward validation** — 21 quarterly out-of-sample windows from 2020–2026
- **Monte Carlo simulation** — 1,000 bootstrapped equity paths with p5/p95 Sharpe range
- **Sensitivity analysis** — robustness check across parameter perturbations
- **Risk layer** — beta adjustment, sector neutrality, factor decomposition, mean-variance optimisation
- **106 unit tests** — all passing, using deterministic mock data

---

## Documentation

Comprehensive onboarding and reference documentation lives in `docs/`. Start here:

| If you are... | Go to |
|---|---|
| New to the system | [docs/getting-started/onboarding.md](docs/getting-started/onboarding.md) |
| Ready to run your first trade | [docs/getting-started/quickstart.md](docs/getting-started/quickstart.md) |
| Looking up a specific function | [docs/reference/scanner-api.md](docs/reference/scanner-api.md) |
| Trying to understand the macro gate | [docs/concepts/layer-1-macro-gate.md](docs/concepts/layer-1-macro-gate.md) |
| Adding a new factor | [docs/guides/add-a-factor.md](docs/guides/add-a-factor.md) |
| Debugging an error | [docs/troubleshooting/common-issues.md](docs/troubleshooting/common-issues.md) |

Full documentation index: [docs/index.md](docs/index.md)

---

## Project structure

```
trading_system/
├── src/
│   ├── macro_gate/      # Layer 1: VIX, breadth, credit, put/call, crowding
│   ├── scanner/         # Layer 2: 8 quantitative factors
│   ├── backtest/        # Engine, cost model, walk-forward, Monte Carlo, sensitivity
│   ├── risk/            # Beta, sector, factor decomposition, optimizer
│   └── data/            # yfinance + FRED data fetcher
├── tests/               # 106 deterministic unit tests
├── docs/                # Full documentation (20 files)
├── mag7_paper_trade.py  # End-to-end Mag 7 demo
├── paper_trade.py       # Full S&P 500 runner (in progress)
└── MAG7_PAPER_TRADE_REPORT.md  # Latest run output
```

---

## Suggested repo name

**`quant-gate`**

Captures the two core ideas: quantitative (systematic, data-driven, measurable) and gate (the macro filter that controls when capital is deployed). Short, memorable, and searchable. Alternative options if taken:

| Name | Rationale |
|---|---|
| `quant-gate` | Primary suggestion — concise, captures both layers |
| `deterministic-trader` | Explicit about the core design principle |
| `macro-quant-stack` | Describes the macro gate + quant scanner architecture |
| `signal-layers` | Refers directly to the layered signal architecture from the video |
| `claude-quant-system` | Highlights the Claude Code origin without implying Claude is in the signal path |

---

## Disclaimer

This is an educational implementation of quantitative research infrastructure. It is not financial advice and does not constitute a recommendation to buy or sell any security. Paper trading results do not guarantee future live performance. See the video for the original author's context and disclaimers.
