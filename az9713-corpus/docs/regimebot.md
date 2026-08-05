---
repo: regimebot
description: Regime-gated drawdown-control trading prototype — an HMM/Markov regime classifier gates equity exposure; hard circuit breakers, leak-free walk-forward backtests, Monte Carlo + sensitivity validation, honest reporting. Not an alpha bot.
language: HTML
stars: 0
forks: 0
created: 2026-07-22
updated: 2026-07-22
topics: 
is_fork: False
kb: 405
---

# regimebot
# RegimeBot

A regime-gated **drawdown-control** system with a paper-trading-bot shape. An HMM/Markov
market-regime classifier gates equity exposure; hard circuit breakers (independent of the
model) bound the damage; a validation harness reports honestly — including how little data
the conclusions rest on.

**This is not an alpha-seeking bot.** Benchmark is buy-and-hold; the question every report
answers is *"how much drawdown did regime-gating avoid, at what cost?"* First full run on
SPY 2008–2026 (HMM classifier, execution at the t+1 close): max drawdown
**−12.6% vs −51.5%** buy-and-hold, Sharpe 0.74 vs 0.65 (a tie per the honesty spec),
CAGR 6.20% vs 11.43%; 130 regime transitions (median regime length 24 days), sensitivity
grid robust. See [CHANGES.md](CHANGES.md) for the full results table and
[reports/spy.html](reports/spy.html) for the rendered report.

Design spec, hard constraints, and acceptance tests: [BLUEPRINT.md](BLUEPRINT.md).
Successor to [HMM-regime-terminal](https://github.com/az9713/HMM-regime-terminal).

## Quickstart

```
python -m venv .venv
.venv\Scripts\pip install pandas numpy yfinance hmmlearn matplotlib pytest
.venv\Scripts\python -m pytest                      # 16 tests
.venv\Scripts\python -m regimebot fetch             # SPY daily data -> data/
.venv\Scripts\python -m regimebot report            # full pipeline -> reports/spy.html
```

Paper trading: `SimBroker` (offline) by default; set `ALPACA_KEY`/`ALPACA_SECRET` to use
Alpaca's paper tier via `python -m regimebot paper-step`.

Not investment advice. Past performance — especially on ~130 regime transitions — proves nothing.
