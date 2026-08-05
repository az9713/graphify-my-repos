# YAST — Yet Another Stock Terminal

A real-time stock trading terminal built as a single-page web application. Features live quotes, interactive charts, market movers, sector heatmaps, sentiment analysis, and a news feed — all in a Bloomberg-inspired dark terminal aesthetic.

![HTML](https://img.shields.io/badge/HTML-single--file-orange)
![Python](https://img.shields.io/badge/proxy-Python%203-blue)
![License](https://img.shields.io/badge/license-MIT-green)

![YAST Screenshot](docs/yast.jpg)

## How This Was Built

This project started as a test of **Claude Cowork Dispatch**. The request was sent from Dispatch on the **Claude mobile app**, which instructed **Claude Desktop** to use **Perplexity Computer** to build the initial application — a fully functional Bloomberg-style trading terminal in a single HTML file.

**Claude Code CLI** then further improved the application by diagnosing and fixing two issues:

### 1. CORS Proxy Reliability

The original app routed all Yahoo Finance requests through `allorigins.win`, a free public CORS proxy. This caused frequent failures — the app fires ~50 parallel requests on startup, overwhelming the proxy's rate limits. Charts and quotes would silently fail to load.

**Fix:** Added a lightweight local Python proxy server (`proxy.py`) with automatic detection and fallback. See [docs/cors-issue-and-fix.md](docs/cors-issue-and-fix.md) for the full technical writeup.

### 2. Chart Not Updating on Symbol Search

When searching for a new ticker (e.g., "BE"), the sentiment panel would update but the center panel (hero quote + chart) would remain stuck on the previous symbol.

**Root cause:** When `fetchQuotesDirect()` failed for a searched symbol (CORS timeout or rate limit), it returned an empty array. The code only updated the hero display if the fetch succeeded (`if (q) renderHero(q)`), but `loadTickerSentiment()` always ran because it uses simulated data — creating a split-brain UI where different panels showed different symbols.

**Fix:**
- The hero now updates immediately with the searched symbol name before any fetch completes
- Quote and chart fetches retry once automatically on failure
- A visible error message appears in the chart area if data remains unavailable after retry
- Error messages are cleared when selecting the next symbol

## Features

- **Live Market Data** — Real-time quotes from Yahoo Finance for stocks, ETFs, indices, and crypto
- **Interactive Charts** — TradingView Lightweight Charts with line, candlestick, and area modes
- **7 Timeframes** — 1D, 5D, 1M, 3M, 6M, 1Y, 2Y
- **Watchlist** — 12 tracked symbols with live price and change percentage
- **Sector Heatmap** — All 11 S&P 500 SPDR sector ETFs with performance bars
- **Market Movers** — Top gainers, losers, and most active stocks
- **Sentiment Gauge** — Bull/bear sentiment breakdown per ticker
- **News Feed** — Market headlines with bull/bear/neutral tags
- **Ticker Tape** — Scrolling banner with 17 symbols including BTC/ETH and major indices
- **Dark/Light Theme** — Toggle between Bloomberg dark and light modes
- **Symbol Search** — Look up any ticker with Enter or Ctrl+K
- **Auto-Refresh** — Watchlist and tape update every 30 seconds
- **Responsive** — 3-column, 2-column, and single-column layouts

## Quick Start

### 1. Start the local proxy (recommended)

```bash
python proxy.py
```

This runs a lightweight CORS proxy on `http://localhost:8901` that forwards requests to Yahoo Finance. No dependencies beyond Python 3 standard library.

### 2. Open the terminal

Open `index.html` in your browser.

Check the browser console — you should see:
```
[PROXY] Using local proxy (fast)
```

### Without the proxy

The app still works without `proxy.py` — it falls back to `allorigins.win`, a free public CORS proxy. This is slower and less reliable due to rate limiting. See [docs/cors-issue-and-fix.md](docs/cors-issue-and-fix.md) for details.

## Project Structure

```
yet-another-stock-terminal/
├── index.html                  # Complete app (HTML + CSS + JS)
├── proxy.py                    # Local CORS proxy server (Python 3)
├── README.md
├── LICENSE
└── docs/
    ├── yast.jpg                # Screenshot
    ├── cors-issue-and-fix.md   # Technical writeup of the CORS problem and solution
    └── cors-documentation.docx # Original CORS documentation
```

## Requirements

- A modern web browser (Chrome, Firefox, Edge, Safari)
- Python 3.6+ (for the local proxy — optional but recommended)
- No npm, no build step, no API keys

## How It Works

The app is a single HTML file with embedded CSS and JavaScript. It fetches data from Yahoo Finance's public API endpoints:

- `v8/finance/chart` — price history, OHLC, volume
- `v10/finance/quoteSummary` — P/E, market cap, EPS, beta, dividend yield, etc.

Since Yahoo Finance doesn't send CORS headers, browser requests are blocked by default. The local proxy (`proxy.py`) sits between the browser and Yahoo Finance, forwarding requests and adding the necessary `Access-Control-Allow-Origin` header.

## Keyboard Shortcuts

| Shortcut | Action |
|----------|--------|
| `Ctrl+K` / `Cmd+K` | Focus symbol search |
| `Enter` (in search) | Load symbol |

## Tech Stack

- **HTML/CSS/JS** — No framework, no build tools
- **[Lightweight Charts](https://github.com/tradingview/lightweight-charts)** — TradingView's charting library (CDN)
- **Yahoo Finance API** — Public market data endpoints
- **Python `http.server`** — Standard library CORS proxy

## Credits

- Initial application built with [Perplexity Computer](https://www.perplexity.ai/computer) via Claude Cowork Dispatch
- CORS fix, chart bug fix, and improvements by [Claude Code CLI](https://claude.ai/claude-code)

## License

MIT
