---
repo: self-improving-trading-agent
description: Autonomous S&P 500 paper trading system that improves its own strategy weekly using AI agents
language: Python
stars: 1
forks: 0
created: 2026-05-26
updated: 2026-07-09
topics: 
is_fork: False
kb: 128
---

# self-improving-trading-agent
# Self-Improving S&P 500 Paper Trader

A fully autonomous paper trading system that improves its own strategy every week — no human required after setup.

Three processes run on a shared codebase. Each has one job:

- **The Trader** (`python main.py schedule`) — executes weekly rebalances every Monday at 09:35. Fetches live S&P 500 prices, scores stocks using signal plugins, selects the top 20, and records paper buy/sell orders to the ledger. It reads its parameters from the state directory and never changes anything itself.

- **The Reviewer** (Hermes `trading-review` skill, Monday 09:35) — reads the trade ledger, computes Sharpe/drawdown/win rate, checks a persistent memory of past experiments, identifies the biggest weakness, and writes **one parameter change** to `state/learned_parameters.json`. Never touches the market.

- **The Gatekeeper** (Cornelius `cornelius-filter` skill, Thursday 09:35) — controls which stocks are even eligible before signals score them. Owns minimum market cap, minimum price, stop-loss thresholds, and sector exclusions. The Thursday offset keeps its experiments isolated from the Reviewer's Monday experiments.

The Trader picks up new parameters on its next run. No code changes, no manual tuning — the system converges on better parameters through structured one-variable-at-a-time experiments.

```
┌─────────────────────────────────────────────────────────┐
│                    HUMAN LAYER                           │
│  config/goals.yaml    config/risk_limits.yaml   mode    │
└──────────────────────────┬──────────────────────────────┘
                           │ read
          ┌────────────────┴───────────────┐
          │                                │
┌─────────▼──────────┐        ┌────────────▼─────────────┐
│  Hermes (Mon 09:35) │        │  Cornelius (Thu 09:35)   │
│  trading-review     │        │  cornelius-filter        │
│  writes:            │        │  writes:                 │
│  learned_params     │        │  filter_params           │
└─────────┬───────────┘        └────────────┬─────────────┘
          │                                 │
          └──────────────┬──────────────────┘
                         │ read by
┌────────────────────────▼────────────────────────────────┐
│               Python Engine (Mon 09:35)                  │
│   fetch prices → score signals → rebalance → ledger     │
└─────────────────────────────────────────────────────────┘
```

## Autonomous operation

Once set up, the system runs without human involvement:

1. **Hermes gateway** runs as a Windows background process (Startup folder). It fires cron jobs every Monday and Thursday at 09:35.
2. **Python scheduler** runs as a background process (Startup folder). It executes the Monday rebalance.
3. **Neither agent can set `live` mode.** Only the human can do that by editing `config/goals.yaml`. The system self-improves in paper mode indefinitely until you decide it has earned real money.

After 4+ weeks of paper trading with Sharpe ≥ 1.0, you can promote to live.

## Quick start

Full instructions: [`docs/getting-started/quickstart.md`](docs/getting-started/quickstart.md)

**Prerequisites:** Python 3.11+, Hermes Agent, OpenRouter API key.

```powershell
# 1. Install Python dependencies
pip install -r requirements.txt

# 2. Run your first rebalance cycle
python main.py run

# 3. Check metrics
python main.py metrics

# 4. Seed 8 weeks of backtest data so Hermes has something to review
python main.py backtest --weeks 8 --seed --yes
```

For persistent autonomous operation, follow the [Persistent operation guide](docs/guides/persistent-operation.md) to install the Hermes gateway and Python scheduler as Windows Startup entries.

## How the self-improvement works

Each Monday at 09:35 Hermes:

1. Reads `data/trades.jsonl` and computes rolling 30-day Sharpe
2. Compares to baseline metrics recorded before the last experiment
3. If the experiment improved Sharpe by ≥ 0.1 → **promotes** the change to baseline
4. If Sharpe dropped by ≥ 0.2 → **reverts** the change, logs it in the Hypothesis Graveyard
5. Identifies the single biggest current weakness
6. Proposes **one variable change** with a clear hypothesis
7. Writes `reviews/YYYY-MM-DD-hermes-review.md` and updates `state/learned_parameters.json`

The Python runner picks up the new parameters on the following Monday. Over many cycles, the strategy converges.

Cornelius runs the same loop on Thursday but for universe filters — minimum market cap, stop-loss thresholds, sector exclusions — keeping signal-domain and filter-domain experiments from contaminating each other.

## Strategy

Three signal plugins score every eligible S&P 500 stock:

| Signal | What it measures | Why |
|--------|-----------------|-----|
| Momentum | 12-1 month price return | Trending stocks tend to keep trending |
| Dividend yield | Trailing yield | Higher yield = cheaper relative to income |
| Volatility penalty | 3-month return std dev | Lower volatility = more predictable |

Each signal is cross-sectionally ranked 0→1 (percentile across all stocks), then combined with learned weights:

```
score = momentum_weight × momentum_rank
      + yield_weight    × yield_rank
      + volatility_weight × (1 - volatility_rank)
```

Top 20 stocks by composite score form the portfolio, held in equal weight. All weights, position count, and lookback windows are tunable by Hermes via `state/learned_parameters.json`.

## Project structure

```
config/
  strategy.yaml            Base strategy parameters
  goals.yaml               Success thresholds and trading mode (read_only / paper / live)
  risk_limits.yaml         Hard kill-switch limits (drawdown, daily loss)

src/
  data_ingest/             yfinance S&P 500 price and dividend fetcher
  strategy/signals/        Signal plugins (auto-discovered)
  executor/                Paper trading executor ($100k virtual portfolio)
  ledger/                  Append-only JSONL trade ledger
  metrics/                 Sharpe, Sortino, drawdown, win rate, kill switch
  runner/                  Orchestrates one full rebalance cycle

state/
  learned_parameters.json  Hermes writes signal weights here
  filter_parameters.json   Cornelius writes eligibility thresholds here
  active_experiment.yaml   Current one-variable experiment (Hermes)
  cornelius_experiment.yaml Current one-variable experiment (Cornelius)
  baseline_metrics.json    Performance snapshot before each experiment

data/
  trades.jsonl             Append-only trade ledger (source of truth for all metrics)

hermes/
  TRADING_MEMORY.md        Shared persistent memory: experiments, graveyard, insights
  skills/trading-review/   Hermes skill procedure
  skills/cornelius-filter/ Cornelius skill procedure

reviews/
  YYYY-MM-DD-*.md          Weekly review output files

scripts/
  trader-schedule.cmd      Wrapper script for background scheduler startup

logs/
  scheduler.log            Python scheduler output log
```

## Trading modes

| Mode | Trades recorded | Hermes improves params | Real money |
|------|----------------|----------------------|-----------|
| `read_only` | No | No | No |
| `paper` | Yes (simulated) | Yes | No |
| `live` | Yes (real) | Yes | **Yes** |

Set in `config/goals.yaml`. **Only a human can set `live` — neither agent touches this field.**

## Kill switches

Automatic circuit breakers in `src/metrics/metrics.py`:
- Max drawdown exceeds `risk_limits.yaml` → trading halts, `live` demotes to `paper`
- Daily loss exceeds limit → trading halts

## Running tests

```powershell
python -m pytest tests/ -v
# Expected: 34 passed
```

## Documentation

Full docs at [`docs/index.md`](docs/index.md).

| Guide | What it covers |
|-------|---------------|
| [Quickstart](docs/getting-started/quickstart.md) | Working in under 15 minutes |
| [Onboarding](docs/getting-started/onboarding.md) | Mental model for newcomers |
| [Persistent operation](docs/guides/persistent-operation.md) | Keep everything running on Windows |
| [Signal architecture](docs/concepts/signal-architecture.md) | How signals are scored and composed |
| [Two-agent coordination](docs/concepts/two-agent-coordination.md) | How Hermes and Cornelius split ownership |
| [Experiment protocol](docs/concepts/experiment-protocol.md) | The one-variable scientific method loop |
| [Promote to live](docs/guides/promote-to-live.md) | Checklist before using real money |

## Disclaimer

This system is for **educational and paper trading purposes only**. Nothing here constitutes financial or investment advice. Past performance does not guarantee future results. Never risk money you cannot afford to lose.
