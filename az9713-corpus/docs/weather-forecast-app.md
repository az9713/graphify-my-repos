---
repo: weather-forecast-app
description: Prompt 2 weather forecasting benchmark: append-only development journey and milestone source history.
language: TypeScript
stars: 0
forks: 0
created: 2026-07-19
updated: 2026-07-19
topics: 
is_fork: False
kb: 2939
---

# weather-forecast-app
# FIELD / NORTH

FIELD / NORTH is a live North American weather observatory that compares a transparent browser-computed temperature projection with Open-Meteo's hourly forecast. It combines real weather data, an independently trained local statistical model, explicit provenance, and a fully documented verification journey.

[![Live app](https://img.shields.io/badge/Live_app-Open_FIELD_%2F_NORTH-fb7a2d?style=for-the-badge)](https://field-north-02-kimi-k3-prompt2.vercel.app/)

<p align="center">
  <a href="https://field-north-02-kimi-k3-prompt2.vercel.app/">
    <img src="docs/qa/localhost-desktop-1440x900.png" alt="FIELD / NORTH live weather observatory showing current Seattle conditions and a 48-hour model comparison" width="100%">
  </a>
</p>

**[Open the live application](https://field-north-02-kimi-k3-prompt2.vercel.app/)** — the deployed Vite `index.html` is served by the isolated Vercel project. The image above is a clickable repository-owned render because GitHub does not execute or embed an interactive webpage inside a README.

## What it does

- Searches populated places across the full UN M49 North American region, including Central America and the Caribbean.
- Shows live current conditions, pressure, humidity, and a seven-day outlook.
- Computes a 48-hour ridge-regularized harmonic autoregression entirely in the browser.
- Compares the independent local projection with Open-Meteo's hourly forecast using timestamp-aligned series.
- Reports a withheld 24-hour MAE and same-timestamp persistence baseline.
- Preserves official weather when the custom model fails and preserves the last safe view during transient service failure.
- Provides keyboard search, reduced motion, labeled SVG values, and a complete 48-row table alternative.

## Forecast model

The educational forecast uses the preceding 14 days of model-derived hourly temperature:

```text
T(t) = beta0
     + beta1 * scaledTrend(t)
     + beta2 * sin(2*pi*localHour(t)/24)
     + beta3 * cos(2*pi*localHour(t)/24)
     + beta4 * T(t-1h)
     + beta5 * T(t-24h)
     + error(t)
```

The model uses ridge regularization with `lambda = 1.0`, exact timestamp-addressed lags, recursive prediction, and a strict forecast-origin boundary. Future Open-Meteo values never enter the local model. The displayed holdout result is a recent diagnostic, not a claim of general forecast superiority.

## Data and privacy

Weather, forecast, geocoding, and historical-forecast data come from [Open-Meteo](https://open-meteo.com/) under [CC BY 4.0](https://creativecommons.org/licenses/by/4.0/) and are transformed by FIELD / NORTH.

Open-Meteo “current conditions” and historical inputs are model-derived values, not readings from a nearby physical station. If the user explicitly invokes browser geolocation, the app uses BigDataCloud's client reverse-geocoding endpoint to establish the country code required by the continental policy. Exact coordinates are not persisted by the application.

## Run locally

Requires a current Node.js and npm installation.

```bash
npm install
npm run dev
```

Create and preview a production build:

```bash
npm run build
npm run preview
```

## Verification

```bash
npm run typecheck
npm run lint
npm test
npm run build
npm audit --audit-level=high
```

The completed release gate includes 14 passing tests, Browser gray-box QA on localhost and production, Lighthouse scores of 100 for Accessibility, Best Practices, and SEO, responsive verification, a 30-second performance measurement, and an ordinary foreground-Chrome Computer Use pass.

## Development journey

| Document | Contents |
| --- | --- |
| [Final development journey](docs/journey/prompt-2-development-journey-final.md) | Original-prompt critique, prompt hardening, design board, model decisions, implementation, defects, deployment, and closure |
| [API and model contract](docs/contracts/api-data-model-contract.md) | Data sources, timestamps, geography, privacy, model equation, and backtest contract |
| [System design](docs/architecture/system-design.md) | Runtime flow, module boundaries, state machine, and failure isolation |
| [Reference board](docs/design/reference-board.md) | FIELD / NORTH visual direction, negative references, and acceptance rubric |
| [Localhost QA](docs/qa/localhost-report.md) | Functional, accessibility, responsive, failure, and performance evidence |
| [Production QA](docs/qa/production-report.md) | Deployment isolation and critical deployed regression |
| [Journey events](docs/journey/events/) | Immutable chronological audit trail |

## Benchmark context

This application implements Prompt 2 from the Kimi K3 benchmark discussed in the YouTube video [**Kimi K3 Is Here! (Better Than Opus 4.8?)**](https://www.youtube.com/watch?v=lPP6iBRuzgA).

The project deliberately strengthens the benchmark prompt before execution: it makes model independence, target leakage, geographic coverage, licensing, accessibility, failure states, performance, deployment isolation, and autonomous verification measurable rather than implicit.

## Project status

- Intended use: non-commercial demonstration and engineering study.
- Live deployment: [field-north-02-kimi-k3-prompt2.vercel.app](https://field-north-02-kimi-k3-prompt2.vercel.app/).
- Repository: public after the publication operation described in this README's commit.
- Software licence: none has been granted yet; public repository visibility alone does not create permission to reuse the source code.
