# Day Trading Toolkit

**Five ready-to-use tools that give individual traders the operational infrastructure of an institutional desk.**

Built from the workflows in [*How to Use Claude to Gain a Huge Day Trading Edge*](https://www.youtube.com/watch?v=Rqmdw4xyIMM&t=1464s) by SMB Training.

> *"The edge in trading isn't what you trade anymore. The edge is in how efficiently you operate."*
> — SMB Training

---

## Why this toolkit exists

Most traders have access to the same strategies, indicators, and market data. The differentiator is **operational infrastructure** — custom alerts that filter noise, consistent pre-market prep, objective performance analysis, disciplined exit mechanics, and honest post-trade review.

Institutional desks have teams of people building that infrastructure. Individual traders do it manually, inconsistently, or not at all.

This toolkit closes that gap with five production-ready tools. No API key. No web server. No build step. Copy scripts into your platform, run the Python journal locally, paste prompt templates into Claude.ai.

---

## The five tools

### 1 · Opening Range Breakout (ORB) Alert
**Files:** [`alerts/orb_alert.pine`](alerts/orb_alert.pine) · [`alerts/orb_alert.think`](alerts/orb_alert.think)

A precision alert that fires only when **all four conditions are simultaneously true**:
- Price closes above the 30-minute Opening Range High (9:30–10:00 AM ET)
- Current bar volume ≥ 1.5× the average volume of the opening range
- Price is above VWAP
- Time is before 11:30 AM ET (first two hours of session)

Includes a visual ORB high line, green breakout triangle, and background highlight. Optional filter: only fire when the breakout bar closes in the top 50% of its range (confirms buying pressure, not just a wick).

Available for **TradingView** (Pine Script v5) and **ThinkorSwim** (ThinkScript).

---

### 2 · Pre-Market Game Plan
**File:** [`prompts/premarket_game_plan.md`](prompts/premarket_game_plan.md)

A structured prompt template that turns 45–60 minutes of manual pre-market prep into a 5–10 minute process. Paste your watchlist, overnight news, and pre-market price/volume data into Claude.ai — get back a **priority-ranked table** (High / Medium / Low) with catalyst, price action, key levels, and setup potential for each name, plus a 2–3 sentence market context summary.

---

### 3 · Trade Journal Analyzer
**File:** [`journal/analyze_trades.py`](journal/analyze_trades.py)

A Python script that finds the behavioral patterns hidden inside your P&L. Export a CSV from any broker, add a Setup Type column, run the script — get five analysis sections:

| Section | What it surfaces |
|---|---|
| Overall statistics | Win rate, expectancy, avg win/loss, largest win/loss |
| By setup type | Which setups are profitable and which are leaking money |
| By time of day | Which hourly blocks help vs. hurt your P&L |
| By day of week | Monday–Friday performance breakdown |
| Pattern detection | Best/worst hour, best/worst setup, flagged losing periods |

```bash
pip install -r journal/requirements.txt
python journal/analyze_trades.py your_trades.csv
python journal/analyze_trades.py --sample   # test with generated data
```

---

### 4 · 2-Bar Trailing Stop
**Files:** [`strategies/trailing_stop.pine`](strategies/trailing_stop.pine) · [`strategies/trailing_stop.think`](strategies/trailing_stop.think)

A backtestable trailing stop strategy that converts a discretionary exit into an auditable rule. The stop initializes at the lowest low of the past N bars at entry, then **only moves up** — never down — each time price makes a new N-bar high.

- Stop line turns **red → green** after the first trail event
- Lookback period is adjustable (default: 2 bars)
- Runs in the TradingView Strategy Tester so you can inspect historical behavior

Available for **TradingView** (Pine Script v5) and **ThinkorSwim** (ThinkScript).

---

### 5 · AI Trade Autopsy
**File:** [`prompts/trade_autopsy.md`](prompts/trade_autopsy.md)

A post-trade review template that gives Claude.ai enough context to audit your rule-following rather than give generic chart commentary. Attach a chart screenshot, fill in your entry/exit rules and what actually happened — Claude answers five coaching questions:

1. Did my entry meet my rules? *(Clean / Acceptable / Marginal / Should Not Have Taken)*
2. Did I follow my exit plan? If not, which rule was violated?
3. What behavioral pattern am I showing?
4. What should I focus on improving? *(specific, not generic)*
5. If you were coaching me, what would you tell me?

Includes a **Super Prompting** meta-analysis workflow: aggregate 5+ autopsies and ask Claude to identify your top behavioral patterns, worst setups, and draft a personal trading constitution.

---

## What's included

```
day-trading-toolkit/
│
├── alerts/
│   ├── orb_alert.pine            TradingView ORB breakout alert (Pine Script v5)
│   └── orb_alert.think           ThinkorSwim ORB breakout alert (ThinkScript)
│
├── journal/
│   ├── analyze_trades.py         Python trade journal analyzer
│   ├── requirements.txt          pandas, tabulate
│   └── sample_trades.csv         Starter CSV for testing
│
├── strategies/
│   ├── trailing_stop.pine        TradingView 2-bar trailing stop (Pine Script v5)
│   └── trailing_stop.think       ThinkorSwim 2-bar trailing stop (ThinkScript)
│
└── prompts/
    ├── premarket_game_plan.md    Pre-market watchlist analysis template
    └── trade_autopsy.md          Post-trade coaching template
```

---

## Quick start

| Tool | Steps |
|---|---|
| ORB Alert (TradingView) | tradingview.com → Pine Editor → paste `alerts/orb_alert.pine` → Add to chart → Create alert |
| Pre-Market Game Plan | Open `prompts/premarket_game_plan.md` → fill in watchlist + news + data → paste into claude.ai |
| Trade Journal | `cd journal && pip install -r requirements.txt && python analyze_trades.py your_trades.csv` |
| Trailing Stop | tradingview.com → Pine Editor → paste `strategies/trailing_stop.pine` → Add to chart |
| Trade Autopsy | Take chart screenshot → open `prompts/trade_autopsy.md` → upload screenshot + paste into claude.ai |

---

## Documentation

| Guide | What it covers |
|---|---|
| [TradingView Setup Guide](TRADINGVIEW_SETUP_GUIDE.md) | Complete beginner walkthrough for TradingView: loading Pine Script files, reading the chart visuals, setting up alerts, using the Strategy Tester |
| [Claude Prompts Guide](CLAUDE_PROMPTS_GUIDE.md) | How to use Claude.ai (no prior experience needed): Pre-Market Game Plan step by step, Trade Autopsy step by step, Super Prompting meta-analysis |
| [Trade Journal Guide](TRADE_JOURNAL_GUIDE.md) | Python install, Command Prompt basics, exporting CSV from your broker (Schwab/TOS, IBKR, Webull), preparing the CSV, reading all five output sections |
| [PRD](PRD.md) | Full product requirements document: module specs, design decisions, dependencies, testing results, limitations |

---

## No API key required

The prompt templates (#2 and #5) use [Claude.ai](https://claude.ai) — free to sign up, no API key, no per-use charges on the free plan. The Pine Script and ThinkScript files run inside your trading platform. The Python journal runs locally. Nothing in this toolkit phones home or requires a subscription beyond a free TradingView or Claude.ai account.

---

## Source material

This toolkit was built from two SMB Training resources:

- **YouTube:** [How to Use Claude to Gain a Huge Day Trading Edge](https://www.youtube.com/watch?v=Rqmdw4xyIMM&t=1464s)
- **Blog post:** [5 Best Practices for Using Claude in Trading](https://www.smbtraining.com/blog/ai-trading-prompts-from-the-video-5-best-practices-for-using-claude-in-trading)

---

## Disclaimer

All scripts and templates are for **educational and backtesting purposes only**. A plotted stop line is not an automatically placed broker order. Past backtest performance does not guarantee future results. Nothing in this toolkit constitutes financial advice. Always paper trade and backtest before relying on any logic in live trading.
