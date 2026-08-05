# TA Terminal — Bloomberg-Style Technical Analysis

A Bloomberg Terminal-inspired stock market app that computes **50 technical indicators** for up to 5 stock symbols simultaneously, using real market data from Yahoo Finance. No API key, no account, no subscription required.

> **Note**: This project was created as an experiment with [Perplexity Computer](https://www.perplexity.ai/computer) to explore AI-assisted code generation. It is **not intended as investment advice** or a trading tool. See [Disclaimer](#disclaimer).

![TA Terminal Screenshot](docs/ta_terminal.jpg)

```
+------------------------------------------------------------------+
| TA TERMINAL                          YAHOO FINANCE  2026-03-16   |
+------------------------------------------------------------------+
| Symbols: [ AAPL, NVDA, MSFT, GOOGL, META          ] [ANALYZE]   |
+------------------------------------------------------------------+
| [All] [Momentum] [Trend] [Volatility] [Volume] [Moving Avg]      |
+------------------------------------------------------------------+
| AAPL                          OVERALL: STRONG BUY                |
| BUY: 34  SELL: 8  NEUTRAL: 8                                     |
+------------------------------------------------------------------+
| INDICATOR        VALUE        SIGNAL      TREND                  |
| RSI(14)          67.4         BUY         up                     |
| MACD             2.31         STRONG BUY  up                     |
| Bollinger Bands  %B: 72.1%    BUY         up                     |
| ADX(14)          38.2         BUY         up  +DI: 28 | -DI: 14  |
| SMA(200)         168.42       BUY         up                     |
| ...47 more indicators...                                         |
+------------------------------------------------------------------+
```

---

## Table of Contents

1. [Quick Start](#quick-start)
2. [User Guide](#user-guide)
3. [Use Cases](#use-cases)
4. [Features](#features)
5. [Indicator Categories](#indicator-categories)
6. [All 50 Indicators](#all-50-indicators)
7. [Signal Scale](#signal-scale)
8. [Data Source](#data-source)
9. [Development](#development)
10. [Project Structure](#project-structure)
11. [Troubleshooting](#troubleshooting)
12. [Disclaimer](#disclaimer)
13. [License](#license)

---

## Quick Start

**If you are new to web development:** Node.js is a runtime that lets you run JavaScript programs from the command line, similar to how you run a compiled C++ binary. `npm` is its package manager (like `apt` or `pip`). "localhost:5000" means a web server running on your own machine at port 5000 — open that address in any browser.

### Prerequisites

- **Node.js v18 or higher** — Download from https://nodejs.org and choose the LTS version. This also installs `npm` automatically.
- A terminal / command prompt (PowerShell, cmd, bash, or Terminal on macOS/Linux)

To verify your installation:

```bash
node --version   # should print v18.x.x or higher
npm --version    # should print 9.x.x or higher
```

### Install and Run (Development Mode)

```bash
# Step 1: Install all dependencies (only needed once)
npm install

# Step 2: Start the development server
npm run dev
```

Then open your browser to **http://localhost:5000**

The development server includes hot-reload: if you edit any source file, the browser updates automatically without a manual refresh.

### Install and Run (Production Mode)

If you want the optimized, production-ready build:

```bash
# Step 1: Install dependencies (only needed once)
npm install

# Step 2: Build the app (compiles TypeScript and bundles assets)
npm run build

# Step 3: Start the production server
npm run start
```

Then open your browser to **http://localhost:5000**

---

## User Guide

### Step 1 — Enter Stock Symbols

Type up to **5 stock ticker symbols** separated by commas in the input field at the top. Ticker symbols are the short codes used by stock exchanges:

| Company | Symbol |
|---------|--------|
| Apple | AAPL |
| NVIDIA | NVDA |
| Microsoft | MSFT |
| Alphabet (Google) | GOOGL |
| Amazon | AMZN |
| Meta (Facebook) | META |
| Tesla | TSLA |
| Netflix | NFLX |
| JPMorgan Chase | JPM |
| AMD | AMD |

You can type: `AAPL` (single stock) or `AAPL, NVDA, MSFT` (multiple stocks).

### Step 2 — Click ANALYZE

Press the **ANALYZE** button or hit Enter. The app will:

1. Send the symbols to the server
2. The server fetches ~500 trading days (2 years) of daily OHLCV data from Yahoo Finance
3. The raw data is sent back to your browser
4. Your browser computes all 50 indicators locally (no extra round trips)
5. Results appear on screen

This typically takes **5 to 15 seconds** depending on your internet connection and how many symbols you requested.

### Step 3 — Read the Results

Each stock gets its own panel showing:

- **Overall Signal** — The synthesized recommendation in the top-right corner (e.g., STRONG BUY)
- **Score bar** — Counts of BUY signals, SELL signals, and NEUTRAL signals
- **Indicator table** — All 50 indicators with their current value, signal, and trend direction

### Step 4 — Filter by Category

Use the category buttons below the input bar to focus on a subset of indicators:

- **All** — Show all 50 indicators
- **Momentum** — 15 oscillators that measure speed and overbought/oversold conditions
- **Trend** — 6 indicators that identify direction and strength of trends
- **Volatility** — 8 indicators measuring price swing and range
- **Volume** — 8 indicators that use trading volume to confirm price moves
- **Moving Avg** — 13 moving averages showing price smoothing over different time windows

### Step 5 — Compare Multiple Stocks

If you entered multiple symbols, each gets its own panel side by side. Scroll right if needed on smaller screens. You can directly compare the overall signal and individual indicator values between stocks.

### Step 6 — Check the Data Source Footer

At the bottom of the page, a footer shows:

- **YAHOO FINANCE** (green) — Live data fetched successfully from Yahoo Finance
- **SIMULATED DATA** (orange) — Yahoo Finance was unreachable; the app fell back to realistic synthetic data generated from a seeded random model. Indicators still work and give educational results, but the prices are not real.

---

## Use Cases

These examples assume you have the app running at http://localhost:5000.

---

### Use Case 1: Analyze a Single Stock (AAPL)

**Goal:** Get a complete technical picture of Apple before an earnings announcement.

1. Type `AAPL` in the symbol field
2. Click ANALYZE
3. Look at the **Overall Signal** in the top-right of the AAPL panel
4. Scan the RSI(14) row — if it shows a value above 70, Apple is in overbought territory
5. Check the MACD row — a positive histogram (STRONG BUY) confirms upward momentum
6. Check SMA(200) — if the current price is above the 200-day average, the long-term trend is bullish

**What to watch for:** If Momentum and Moving Avg both show mostly BUY, but Volatility shows ATR rising sharply, the stock may be due for a large move in either direction.

---

### Use Case 2: Compare Two Tech Stocks (GOOGL vs MSFT)

**Goal:** Decide which of two similar tech stocks has stronger technical momentum right now.

1. Type `GOOGL, MSFT` in the symbol field
2. Click ANALYZE
3. Compare the **Overall Signal** for each panel side by side
4. Look at the RSI(14) row for both — which is closer to 50 (neutral), and which is above 70 (overbought)?
5. Compare ADX(14) — the stock with ADX above 25 has a stronger, more established trend
6. Compare MACD histogram values — the larger positive histogram indicates stronger upward momentum

**Interpretation:** If MSFT shows BUY on 35 out of 50 indicators and GOOGL shows BUY on 28, MSFT currently has stronger technical support.

---

### Use Case 3: Check Momentum for a Volatile Stock (TSLA)

**Goal:** Understand Tesla's short-term momentum and whether it is overbought or oversold.

1. Type `TSLA` in the symbol field
2. Click ANALYZE
3. Click the **Momentum** filter button
4. Now you see only the 15 momentum indicators
5. Check **RSI(14)** — above 70 = overbought (price may pull back), below 30 = oversold (price may bounce)
6. Check **Stochastic Oscillator (STOCH)** — if %K is above %D and both are above 80, overbought
7. Check **Williams %R** — values near 0% mean overbought; near -100% mean oversold
8. Check **Stochastic RSI (SRSI)** — a more sensitive version of RSI; useful for volatile stocks

**What to look for:** If RSI, Stochastic, and Williams %R all simultaneously show overbought, there is confluence — multiple independent indicators agree, which carries more weight than a single indicator.

---

### Use Case 4: Analyze FAANG Stocks Together (META, AAPL, AMZN, NFLX, GOOGL)

**Goal:** See which of the five major consumer tech stocks has the best technical setup right now.

1. Type `META, AAPL, AMZN, NFLX, GOOGL` in the symbol field
2. Click ANALYZE (this fetches 5 datasets — allow up to 20 seconds)
3. Compare all five **Overall Signal** labels
4. Sort them mentally by BUY count — the highest BUY count has the broadest indicator support
5. Look at SMA(50) and SMA(200) for each — a stock trading above both is in a strong uptrend
6. Look at the ADX row — above 25 means a trend is present; below 20 means sideways/choppy

**Insight:** Even if all five are in a general bull market, their individual technical readings will diverge, letting you identify which is leading and which is lagging.

---

### Use Case 5: Filter by Trend Category to Find Trend Direction

**Goal:** Use only trend-following indicators to determine whether a stock is in an uptrend, downtrend, or going sideways.

1. Type any symbol, e.g., `SPY` (S&P 500 ETF)
2. Click ANALYZE
3. Click the **Trend** filter button
4. You now see 6 indicators: ADX, Ichimoku Cloud, Parabolic SAR, Donchian Channels, Aroon Oscillator, Price Channel Position

**Reading the Trend panel:**
- **ADX** above 25 = trending (direction shown by +DI vs -DI); below 20 = range-bound
- **Ichimoku Cloud** — if price is above the cloud and Tenkan > Kijun, bullish trend
- **Parabolic SAR** — SAR dots below price = uptrend; dots above price = downtrend
- **Aroon Oscillator** — positive = uptrend; negative = downtrend; near zero = sideways
- **Donchian Channels** — price at upper band = strong uptrend; at lower band = downtrend
- **Price Channel Position** — above 50% = upper half of recent range

**Rule of thumb:** If 4 or more of these 6 indicators agree, the trend signal is reliable.

---

### Use Case 6: Filter by Volume Category to Check Volume Patterns

**Goal:** Confirm whether a recent price move is backed by strong buying/selling volume or is just noise.

1. Type a symbol that recently had a big move, e.g., `NVDA`
2. Click ANALYZE
3. Click the **Volume** filter button
4. Review the 8 volume indicators

**Reading the Volume panel:**
- **OBV (On-Balance Volume)** — rising OBV during a price rise confirms real buying pressure
- **MFI (Money Flow Index)** — above 80 = overbought on volume; below 20 = oversold on volume
- **Chaikin Money Flow (CMF)** — positive value = money flowing in; negative = flowing out
- **A/D Line** — if price rises but A/D Line falls, there is bearish divergence (warning sign)
- **Volume vs 20-SMA** — a ratio above 1.5x means current volume is 50% above average (unusual activity)
- **Force Index** — large positive value = strong buying force

**Key insight:** Price moves with high volume are more sustainable than moves on low volume. If NVDA jumps 5% but CMF is negative and OBV is flat, the move may not have real institutional backing.

---

### Use Case 7: Compare a Semiconductor Pair (NVDA vs AMD)

**Goal:** Compare two direct competitors in the same industry.

1. Type `NVDA, AMD`
2. Click ANALYZE
3. Compare Overall Signals
4. Focus on **Moving Avg** — click the Moving Avg filter
5. For each stock, check which moving averages (SMA 10/20/50/100/200, EMA variants) are BUY signals
6. A stock trading above its SMA(200) and SMA(50) is in a well-established long-term uptrend
7. Check **VWAP** — price above VWAP means institutional buying dominated today's session

**Typical finding:** NVDA and AMD often correlate but diverge during sector rotations. The one with more moving average BUYs is technically stronger at that moment.

---

### Use Case 8: Analyze JPMorgan (JPM) for Moving Average Crossovers

**Goal:** Identify whether classic moving average crossover signals (Golden Cross / Death Cross) are active.

1. Type `JPM`
2. Click ANALYZE
3. Click the **Moving Avg** filter
4. Look at SMA(50) and SMA(200) values
5. If the SMA(50) value is higher than SMA(200), a "Golden Cross" has recently occurred — historically a bullish long-term signal
6. If SMA(50) is lower than SMA(200), a "Death Cross" is in effect — historically bearish
7. Also check EMA(50) vs EMA(200) — EMA crossovers react faster than SMA crossovers

**What this tells you:** Large-cap financial stocks like JPM tend to respond well to moving average analysis because institutional investors often use these exact levels as buy/sell triggers.

---

### Use Case 9: Check Volatility Indicators During Earnings Season

**Goal:** Assess whether a stock's current volatility level is elevated and in what direction it might move.

1. Type a stock near its earnings date, e.g., `AMZN`
2. Click ANALYZE
3. Click the **Volatility** filter
4. Review the 8 volatility indicators

**Reading the Volatility panel:**
- **ATR (Average True Range)** — shows average daily price swing in dollars; the detail shows ATR as % of price
- **Bollinger Bands %B** — above 80% = price near upper band (stretched); below 20% = near lower band
- **Bollinger Bandwidth** — if BW is near a multi-year low, a big move is likely imminent (the "Bollinger Squeeze")
- **Keltner Channels** — similar to Bollinger but uses ATR; price outside channels = strong breakout or mean-reversion setup
- **Historical Volatility (HV)** — annualized volatility in %; above 40% is high for large-cap stocks
- **Mass Index** — above 27 signals a potential reversal is coming
- **Choppiness Index** — above 61.8 = choppy/ranging market; below 38.2 = strongly trending

**Pre-earnings setup:** If HV is rising, ATR is expanding, and Bollinger Bandwidth is squeezing simultaneously, the market is pricing in a large binary move around earnings.

---

### Use Case 10: Read the Overall Signal Synthesis to Make a Decision

**Goal:** Understand what the synthesized OVERALL signal actually means.

1. Type any symbol, e.g., `MSFT`
2. Click ANALYZE
3. Look at the top of the MSFT panel — it shows something like:
   - `STRONG BUY  |  BUY: 42  SELL: 6  NEUTRAL: 2`

**How the synthesis works:**
- Each STRONG BUY counts as 2 points toward the buy score
- Each BUY counts as 1 point toward the buy score
- Each STRONG SELL counts as 2 points toward the sell score
- Each SELL counts as 1 point toward the sell score
- NEUTRAL indicators are counted but do not add to buy or sell scores
- If buy score / total > 60% → STRONG BUY
- If buy score / total > 40% and buy > sell → BUY
- If sell score / total > 60% → STRONG SELL
- If sell score / total > 40% and sell > buy → SELL
- Otherwise → NEUTRAL

**Important:** This is a mechanical signal. A STRONG BUY with 42 buy signals simply means the majority of technical indicators are currently pointing up based on historical price and volume patterns. It does NOT predict the future or constitute financial advice.

---

## Features

- **50 Technical Indicators** — RSI, MACD, Bollinger Bands, Ichimoku Cloud, Stochastic, ADX, ATR, OBV, and 42 more, organized into 5 categories
- **Real Market Data** — Fetches approximately 500 trading days (2 years) of daily OHLCV data from Yahoo Finance's public API. Free, no API key required, no account needed.
- **Automatic Mock Data Fallback** — If Yahoo Finance is unreachable (network block, rate limit, maintenance), the server generates realistic synthetic data seeded to the ticker symbol so indicators still compute correctly. The footer clearly labels which mode is active.
- **Multi-Stock Comparison** — Analyze up to 5 symbols simultaneously in a side-by-side panel layout
- **Signal Synthesis** — All 50 indicators are combined into a single weighted score (STRONG BUY / BUY / NEUTRAL / SELL / STRONG SELL)
- **Category Filtering** — Instantly filter the indicator table to show only Momentum, Trend, Volatility, Volume, or Moving Average indicators
- **Bloomberg Dark Theme** — Professional dark navy background (#0a0e14) with amber accents (#ff9800)
- **Client-Side Computation** — All indicator math runs in your browser. The server only fetches raw OHLCV data.
- **No Database Required** — Zero setup beyond `npm install`. No PostgreSQL, no Redis, no accounts.
- **Windows Compatible** — Uses `cross-env` to handle NODE_ENV on Windows without extra configuration

---

## Indicator Categories

| Category | Count | Purpose |
|----------|-------|---------|
| Momentum | 15 | Measures speed of price change; identifies overbought/oversold conditions |
| Trend | 6 | Identifies direction and strength of the prevailing trend |
| Volatility | 8 | Measures magnitude of price swings and range |
| Volume | 8 | Uses trading volume to confirm or question price moves |
| Moving Avg | 13 | Smooths price over different time windows; identifies support/resistance |
| **Total** | **50** | |

---

## All 50 Indicators

### Momentum (15)

| Indicator | Parameters | What It Measures |
|-----------|-----------|-----------------|
| RSI | 14-period | Relative Strength Index — momentum oscillator 0-100; above 70 = overbought, below 30 = oversold |
| MACD | 12,26,9 | Moving Average Convergence Divergence — difference between fast and slow EMA, with signal line |
| Stochastic Oscillator | 14,3 | %K and %D lines — compares close to recent high-low range; above 80 overbought, below 20 oversold |
| Williams %R | 14-period | Similar to Stochastic but inverted; 0% = overbought, -100% = oversold |
| CCI | 20-period | Commodity Channel Index — measures deviation from average price; extreme values signal reversals |
| ROC | 12-period | Price Rate of Change — percentage change over 12 days; positive = upward momentum |
| MOM | 10-period | Momentum — raw price difference over 10 days |
| TSI | Double-smoothed | True Strength Index — doubly smoothed momentum using EMA; crosses zero signal direction changes |
| Ultimate Oscillator | 7,14,28 | Combines three time periods to reduce false divergence signals |
| Awesome Oscillator | 5,34 SMA | Difference between a 5-period and 34-period simple moving average of midpoints |
| Stochastic RSI | 14-period | Applies Stochastic formula to RSI values; more sensitive than plain RSI |
| TRIX | 15-period | Triple-smoothed EMA rate of change; zero crossings signal direction changes |
| DPO | 20-period | Detrended Price Oscillator — removes trend to identify cycle lengths |
| Elder Ray Index | 13-period | Bull Power and Bear Power relative to an EMA |
| Coppock Curve | Classic | Long-term momentum oscillator; zero crossovers historically signal major buying opportunities |

### Trend (6)

| Indicator | Parameters | What It Measures |
|-----------|-----------|-----------------|
| ADX | 14-period | Average Directional Index — strength of trend regardless of direction; above 25 = trending, above 40 = strong trend |
| Ichimoku Cloud | 9,26,52 | Multi-component Japanese trend system: Tenkan, Kijun, Senkou A/B, Chikou |
| Parabolic SAR | 0.02,0.2 | Stop and Reverse — trailing stop dots that flip above/below price at trend reversals |
| Donchian Channels | 20-period | Highest high and lowest low over 20 days; breakouts signal trend starts |
| Aroon Oscillator | 25-period | Measures how recently the highest high and lowest low occurred; +100 to -100 scale |
| Price Channel Position | 2