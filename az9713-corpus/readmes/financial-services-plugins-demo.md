# Claude for Financial Services — Plugin Demo

> **How this was created — the exact prompts used:**
>
> *"please install the financial services plugins from https://github.com/anthropics/financial-services/"*
>
> That single prompt, entered into [Claude Code](https://claude.ai/code), triggered the full installation of all 20 plugins in this suite.
>
> After installation, `/reload-plugins` was run **without exiting Claude Code** — this hot-reloaded all 20 plugins (77 skills, 38 agents, 6 hooks, 15 MCP servers) into the active session instantly, making every command available without restarting.
>
> Everything in this repo — the sample outputs, onboarding guide, Excel comps file, and workflows — was produced in the same Claude Code session that followed.

Sample outputs and onboarding guide for the [Claude for Financial Services](https://github.com/anthropics/financial-services) plugin suite, tested using Claude Code.

> ⚠️ **All outputs in this repo use Claude's training-data knowledge (cutoff ~early 2026), not real-time market data.**
> Stock prices, valuations, earnings figures, and multiples are illustrative estimates — they will differ from current market values.
> For production use, authenticate a live data connector (LSEG, S&P Global, FactSet, or Morningstar) so the plugins pull current figures automatically. See [Data note](#data-note) below.

## What's here

| File | Command | Description |
|---|---|---|
| [`00_onboarding_guide.md`](00_onboarding_guide.md) | — | **Start here.** Full guide to all plugins, every command with examples, and 8 multi-command power workflows |
| [`01_ic_memo.md`](01_ic_memo.md) | `/private-equity:ic-memo` | Investment Committee memo — CloudPay Inc (B2B payroll SaaS, $75M deal) |
| [`02_lbo_msft.md`](02_lbo_msft.md) | `/financial-analysis:lbo` | Azure divisional LBO — 3 scenarios, debt schedule, IRR/MOIC, sensitivity tables |
| [`03_one_pager.md`](03_one_pager.md) | `/investment-banking:one-pager` | IB sell-side one-pager — RetailAI Inc, $5.4B TAM, M&A comps |
| [`04_financial_plan.md`](04_financial_plan.md) | `/wealth-management:financial-plan` | Personal financial plan — retirement projections, college funding, 20-item action plan |
| [`05_gl_recon.md`](05_gl_recon.md) | `/fund-admin:gl-recon` | GL reconciliation — $2.3M break traced and resolved with NAV impact |
| [`06_sector_cloud_computing.md`](06_sector_cloud_computing.md) | `/equity-research:sector` | Cloud computing sector landscape — TAM, competitive dynamics, investment implications |
| [`07_screen_midcap_tech.md`](07_screen_midcap_tech.md) | `/equity-research:screen` | Stock screen — 7 undervalued mid-cap tech ideas with full analysis |
| [`08_thesis_googl.md`](08_thesis_googl.md) | `/equity-research:thesis` | GOOGL investment thesis — bull/bear/valuation/catalysts |
| [`09_comps_googl.md`](09_comps_googl.md) | `/financial-analysis:comps` | GOOGL comparable company analysis vs META, MSFT, AMZN, AAPL, NFLX |
| [`GOOGL_Comps_Analysis_2026-05-09.xlsx`](GOOGL_Comps_Analysis_2026-05-09.xlsx) | `/financial-analysis:comps` | Excel file — formatted comps with live formulas, statistical rows |
| [`build_comps.py`](build_comps.py) | — | Python script used to generate the Excel comps file (openpyxl) |

Each markdown file opens with an **"About This Command"** section explaining what the command does, how to invoke it, and what it produces — readable by someone with no prior finance background.

## Quick start

### 1. Install the plugins

```bash
# Add the marketplace
claude plugin marketplace add anthropics/claude-for-financial-services

# Install core + all plugins
claude plugin install financial-analysis@claude-for-financial-services
claude plugin install investment-banking@claude-for-financial-services
claude plugin install equity-research@claude-for-financial-services
claude plugin install private-equity@claude-for-financial-services
claude plugin install wealth-management@claude-for-financial-services
claude plugin install fund-admin@claude-for-financial-services
claude plugin install operations@claude-for-financial-services
claude plugin install pitch-agent@claude-for-financial-services
claude plugin install market-researcher@claude-for-financial-services
claude plugin install earnings-reviewer@claude-for-financial-services
claude plugin install meeting-prep-agent@claude-for-financial-services
claude plugin install model-builder@claude-for-financial-services
claude plugin install gl-reconciler@claude-for-financial-services
claude plugin install kyc-screener@claude-for-financial-services
claude plugin install valuation-reviewer@claude-for-financial-services
claude plugin install month-end-closer@claude-for-financial-services
claude plugin install statement-auditor@claude-for-financial-services
claude plugin install lseg@claude-for-financial-services
claude plugin install sp-global@claude-for-financial-services
```

### 2. Try your first command

```
/equity-research:sector cloud computing
/equity-research:screen undervalued mid-cap tech
/financial-analysis:comps AAPL
/private-equity:ic-memo
```

### 3. Read the onboarding guide

Open [`00_onboarding_guide.md`](00_onboarding_guide.md) for the full command reference and power workflows.

## Data note

**All outputs in this repo are based on Claude's training data, not real-time market data.**

| What this means | Detail |
|---|---|
| **Knowledge cutoff** | ~early 2026. Prices, earnings, and guidance from after that date are not reflected. |
| **Stock prices** | The GOOGL thesis, for example, used a ~$170 price from training data. The actual price at time of generation (May 2026) was ~$400 — a significant divergence. |
| **Financial figures** | Revenue, EBITDA, and multiples are estimates based on publicly reported data Claude was trained on. They may be stale or approximate. |
| **What is correct** | The analytical structure, methodology, and workflow logic are sound. The frameworks (DCF, LBO, comps, IC memo structure) reflect real institutional practice. |
| **For production use** | Authenticate a live data connector — LSEG, S&P Global Capital IQ, FactSet, or Morningstar — so the plugins pull current figures automatically instead of relying on training data. |

The data connectors ship with the plugin suite and are activated by running the authenticate command for each provider (e.g. `/lseg:macro-rates` will prompt for LSEG credentials if not yet authenticated). API pricing for these services is typically lower than full desktop licensing — contact each provider's sales team for API-tier quotes.

## This repo

[github.com/az9713/financial-services-plugins-demo](https://github.com/az9713/financial-services-plugins-demo)

## Plugin source

[github.com/anthropics/financial-services](https://github.com/anthropics/financial-services)
