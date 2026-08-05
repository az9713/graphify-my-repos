# Market Microstructure Observatory

[![The Market Microstructure Observatory — the live order book rendered as twin bid/ask mountain ranges scrolling through time, with a plain-language narrator reading the market aloud](docs/screenshot.jpg)](https://az9713.github.io/market-microstructure-observatory/web/)

### ▶ [**Click the image, or launch the live observatory here**](https://az9713.github.io/market-microstructure-observatory/web/)

No install, no build — it runs the whole market in your browser.

| Live page | What it is |
|---|---|
| 🔴 [**The Observatory**](https://az9713.github.io/market-microstructure-observatory/web/) | The app itself: 3D order book, flash-crash button, Plain English tab, validation and backtest dashboards |
| 📖 [**Reading the dashboard**](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html) | Every chart and number explained from zero — plus [what it's actually for](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html#useful) |
| 🛠 [**Development journey**](https://az9713.github.io/market-microstructure-observatory/docs/development-journey.html) | How it was built, and the six real bugs found along the way |
| ∑ [**The mathematics**](https://az9713.github.io/market-microstructure-observatory/docs/microstructure-math.html) | Full derivations — Avellaneda–Stoikov, the Hill estimator, market impact |

---

A limit-order-book market simulator, stylized-fact validator, and **real-data backtester**
with a WebGL visualization: the order book rendered as twin glowing mountain ranges scrolling
through time, trades as rising embers, and a flash-crash button that shows you exactly how
liquidity evaporates.

Everything is plain ES modules — the **same engine code** runs in Node (tests, validation,
backtests) and in the browser (live visualization via a module Worker). No build step,
no runtime dependencies (three.js is vendored for the front-end only).

## About

> **What it is.** A production-grade laboratory for how markets actually work at the level of
> individual orders. Three things in one repo: an agent-based market simulator whose realism is
> *measured* rather than claimed, a backtest engine that replays trading strategies against a real
> recorded market tape under latency and fees, and a WebGL dashboard that makes both legible.
>
> **Why it's unusual.** The simulator is held to six statistical gates derived from real markets —
> fat tails, market efficiency, volatility clustering, square-root price impact — computed by the
> *identical code path* that measures genuine Binance and Kraken data, and the build fails if any
> gate fails. The backtester is deliberately pessimistic (you join the back of every queue, every
> action costs 75 ms, every fill pays real exchange fees), so it is allowed to tell you a strategy
> loses money. Both of the shipped strategies do. That is the point: the harness is the product.

| | |
|---|---|
| **Status** | Complete and verified — 19/19 tests, 6/6 validation gates across 4 seeds, real-tape backtest run |
| **Stack** | Plain ES modules, zero runtime deps, `node:test`, vendored three.js, no build step |
| **Simulator** | 8 agents on a discrete-event scheduler; Hill α 5.04, kurtosis 2.79, impact exponent 0.45 |
| **Real data** | 5 days Binance SOL-USDT (958k orders, impact exponent 0.78) + 75 min live Kraken SOL/USD tape |
| **Backtest result** | AS maker −$4.40, momentum taker −$5.02 — honest losses under 75ms latency, 2bp/5bp fees, conservative queue fills |
| **No graphs required** | A **Plain English** tab and a live narrator restate every conclusion in words — the 3D view is optional |
| **Run it** | `npm test && npm run sim && npm run serve` → <http://localhost:8619> |
| **License** | MIT |

> **Is this an investment tool?** No. There is no valuation, no forecast, and no signal anywhere in
> it — validation gate #3 actively *requires* that price direction be unpredictable. What it measures
> is what trading **costs**: fees, spread, market impact, queue position. On the market it recorded,
> the round-trip fee was 2.3× the entire available spread — the kind of thing worth knowing before
> you start. See [what it's for](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html#useful).

## Documentation

Each links to the rendered page; the source is in `docs/`.

| Doc | What's in it |
|---|---|
| [**Reading the dashboard**](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html) | Zero-domain-knowledge tour of every chart, table, number and moving object in the web UI. Starts by defining what an order book *is*. Includes [what this is and isn't useful for](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html#useful) and [the no-graphs-required tooling](https://az9713.github.io/market-microstructure-observatory/docs/reading-the-dashboard.html#plaintab). Read this first if you don't work in markets. |
| [**Development journey**](https://az9713.github.io/market-microstructure-observatory/docs/development-journey.html) | How it was built: the stack and why, eight design decisions, the Binance geo-restriction pivot, six real bugs with their diagnostics, the parameter search that made the statistics emerge, and the known warts. |
| [**The mathematics**](https://az9713.github.io/market-microstructure-observatory/docs/microstructure-math.html) | Rigorous derivations: Avellaneda–Stoikov from the HJB indifference argument, the Hill estimator and its ±0.7 error bar, why concave impact follows from errors-in-variables attenuation, and the exact fee arithmetic that made both strategies lose. |
| [`HANDOFF.md`](HANDOFF.md) | Resume point for a future session: current state and the re-validation rules for `src/sim/*`. |

## Quick start

```bash
npm test               # 19 property/statistical/fill-model tests
npm run sim            # 8h agent-based sim → validation gates → web/data/sim.json
npm run fetch          # historical Binance SOL-USDT aggTrades + bookDepth → data/cache/
npm run capture        # live Kraken SOL/USD L1+trades → data/capture/*.jsonl (75 min)
npm run backtest       # strategies vs the captured tape → web/data/backtest.json
npm run serve          # http://localhost:8619 → the observatory
```

## What's inside

```
src/core/     order book (price-time priority, integer ticks), seeded RNG
src/sim/      discrete-event market + agent ecology
src/backtest/ event-driven engine over real L1 tapes, strategies, metrics
src/stats/    stylized-fact statistics (shared by sim validation & real data)
scripts/      runners: sim, fetch, capture, backtest, serve
test/         node:test suites — engine properties, estimator recovery, fill model
web/          the observatory (three.js scene + hand-rolled canvas charts)
docs/         development journey, dashboard guide, mathematics
```

### The simulator (`src/sim`)

Agent ecology on a discrete-event scheduler:

- **ZeroIntelligence** — Smith/Farmer baseline: Poisson limit orders with geometric price
  offsets, exponential lifetimes, market orders with persistent signs (long-memory flow) whose
  **size is conditioned on displayed liquidity** (selective liquidity taking — the mechanism
  behind concave impact).
- **MarketMaker** — Avellaneda–Stoikov: reservation price `r = s − qγσ²τ`, half-spread
  `δ = γσ²τ/2 + ln(1+γ/κ)/γ`, online EWMA σ², inventory caps. Pulls quotes during shocks —
  which is what makes flash crashes crash.
- **Momentum / MeanReverter** — destabilizing and stabilizing strategic flow.
- A **log-OU activity process** modulates arrival rates (market orders ~linearly, liquidity
  provision sublinearly): busy regimes are under-provisioned, producing volatility clustering
  and fat tails endogenously.

### Validation gates (`npm run sim`)

The sim must reproduce the stylized facts of real markets or the script exits non-zero:

| gate | target | typical result |
|---|---|---|
| Hill tail exponent (30s returns) | 2–6 (real ≈ 3, "cubic law") | 3–5 |
| excess kurtosis | > 1 | 3–12 |
| ACF of returns, lags 1–5 | ≈ 0 (efficiency) | ~0.02 |
| ACF of \|r\| lag 1 | > 0.05 and ≫ ACF r | 0.2–0.27 |
| ACF of \|r\| lags 1–10 sum | > 0.3 (clustering persists) | 1.5–2.3 |
| per-order impact exponent | 0.3–0.8 (√-law = 0.5) | 0.44–0.49 |

Verified across multiple seeds. The same statistics are computed on real data
(5 days of Binance SOL-USDT aggTrades: Hill α ≈ 2.6–4.1, impact exponent ≈ 0.78)
by the **identical code path** and shown side-by-side in the Validation tab.

> Any change to `src/sim/*` must rerun `node scripts/run-sim.js <seed> 8` on **at least three
> seeds** and require 6/6 PASS. The tuned parameters are a specific point in parameter space,
> not defaults — see the [development journey](https://az9713.github.io/market-microstructure-observatory/docs/development-journey.html#tuning).

### The backtester (`src/backtest`)

Replays strategies against a **real captured tape** (Kraken SOL/USD L1 quotes + trades,
recorded by `npm run capture`; Binance trade websockets are geo-restricted in some regions,
their historical dumps are not). Guarantees:

- **No lookahead** — event-time engine; the strategy sees only the past (tested).
- **Latency** — every action (place/cancel/market) takes `latencyMs` (default 75) to reach
  the exchange; fills before activation are impossible (tested).
- **Conservative queue modeling** — joining a level puts you behind *all* displayed size;
  your queue position advances only on real prints at your price; you fill only when prints
  exceed the queue ahead, or the market trades/quotes *through* your level (tested).
- **Fees** — maker 2bp / taker 5bp on every fill.

Strategies: Avellaneda–Stoikov maker (adapted to live tape) and an order-flow momentum
taker as the honest taker benchmark. Metrics: net/gross PnL, annualized dollar Sharpe,
max drawdown, maker/taker fill split, turnover, inventory profile.

**Honesty box**: the backtest does not model our own impact on other participants, L2 beyond
the touch, exchange rate limits, or funding. One session on one pair is evidence, not proof —
the harness is the product; rerun on longer captures before believing any single number.

**Why both strategies lost** (derived in full in the [mathematics doc](https://az9713.github.io/market-microstructure-observatory/docs/microstructure-math.html#fees)):
the mean spread over the capture was $0.0128, while a round trip costs `2 × 2bp × $73.33 = $0.0293`
in maker fees. The two-sided fee was **2.3× the entire available spread** — no market maker could
have profited on that venue in that window. The momentum taker was flat before costs (−$0.37 on
$9,296 of turnover) and lost exactly its fee bill.

### Data sources (all free, no keys)

- `data.binance.vision` — daily aggTrades + bookDepth dumps (USD-M futures)
- Kraken public WebSocket v2 — live L1 (`ticker`, bbo-triggered) + `trade` stream

## GitHub Pages

Serve the repo root (the site lives at `/web/`, importing `/src` modules directly).
Everything is static; `web/data/*.json` are build artifacts you regenerate with the
scripts above — note `.gitignore` excludes `data/` but `web/data/*.json` **must** be committed.
