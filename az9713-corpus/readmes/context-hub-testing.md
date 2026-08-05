# Context Hub (chub) Testing

Real-world stress test of [Context Hub](https://github.com/andrewyng/context-hub) (chub) — a CLI that provides coding agents with curated, versioned API documentation.

We used chub to build a full-stack todo app on Windows and documented every issue encountered along the way.

## What We Found

**8 issues** across CLI bugs, doc staleness, and structural gaps:

| # | Issue | Severity |
|---|-------|----------|
| 1 | Windows path handling crashes `chub get` for non-bundled docs | Critical |
| 2 | Prisma doc covers 6.19.0 but npm installs 7.5.0 (breaking changes) | High |
| 3 | Tailwind v4 + Next.js Turbopack = build failure, cascading into invisible UI bug | High |
| 4 | Next.js doc has no CSS/Tailwind section | Medium |
| 5 | No version-pinning guidance when docs target specific versions | Medium |
| 6 | Docs are siloed per library — no cross-cutting integration docs | Systemic |
| 7 | `chub search` defaults to 20 results, hiding 1540 of 1560 docs | Medium |
| 8 | npm package contains older code than repo (same version number) | Medium |

Full analysis with root causes, code traces, and recommendations: **[TEST-REPORT.md](TEST-REPORT.md)**

## Key Takeaway

chub's individual library docs are well-structured and genuinely useful for LLM consumption. But three structural gaps undermine the value:

- **Version drift** — docs freeze at a specific version while `npm install` moves on
- **Siloed docs** — no integration layer between commonly-combined libraries
- **Unpublished fixes** — the npm package lags behind the repo

## chub vs Context7 MCP — Comparison

Both tools solve the same problem (getting up-to-date docs to LLMs) but take fundamentally different approaches.

### How They Differ

| Aspect | Context Hub (chub) | Context7 MCP |
|--------|-------------------|--------------|
| **Approach** | Human-curated markdown, reviewed via PRs | Automated scraping from doc sites |
| **Coverage** | 1560 docs (curated subset) | Broad — scrapes most popular libraries |
| **Format** | LLM-optimized with structured examples | Raw scraped docs, variable quality |
| **Integration** | CLI tool — works with any agent | MCP server — requires MCP-compatible tools |
| **Versioning** | Each doc targets a specific version | Scrapes latest docs automatically |
| **Feedback** | Up/down voting flows back to maintainers | No feedback mechanism |
| **Annotations** | Persistent agent notes across sessions | No annotation support |
| **Discoverability** | `chub search` (default limit 20 of 1560) | Search across all scraped libraries |

### Where chub Wins

- **Doc quality**: Curated markdown with clear code examples, structured for LLM consumption
- **Agent features**: Annotations persist across sessions, feedback loop improves docs over time
- **Transparency**: All content is open markdown in a GitHub repo — you can read exactly what your agent reads
- **Portability**: CLI works with any agent or workflow, not tied to MCP

### Where Context7 Wins

- **Coverage breadth**: Scrapes docs automatically, so new libraries are available without waiting for someone to write a curated doc
- **Always current**: Scrapes latest docs, so version drift (our Issue 2) doesn't happen
- **No integration gaps**: Since it scrapes each library's own docs, cross-library gotchas are less likely to be wrong (though they may be absent)
- **Zero maintenance**: No human curation needed — scales without contributor effort

### What Our Testing Revealed

chub's curation model has real strengths, but our stress test exposed its weaknesses:

- **Version drift** (Issue 2): Prisma doc was frozen at 6.19.0 while npm installs 7.5.0. Context7's scraping approach avoids this entirely.
- **Siloed docs** (Issues 3, 4, 6): Each chub doc is correct for its library but nobody documents the integration points. Context7 has the same gap, but at least it doesn't teach you the *wrong* integration path (like chub's Tailwind v4 PostCSS setup that breaks Turbopack).
- **Coverage**: chub has 1560 docs vs Context7's broader automated coverage. But chub's docs are genuinely better structured for LLM consumption when they exist and are up to date.

### Bottom Line

They're complementary, not competing:

- Use **Context7** for broad coverage and always-current docs — good default for most development
- Use **chub** for critical APIs where you need high-quality, LLM-optimized docs with annotations — worth the trade-off if the doc is up to date
- **Neither** solves the cross-library integration problem well

## The Todo App

A working Next.js app built entirely by following chub docs, used as the test vehicle.

**Stack** (informed by chub docs):
- Next.js 16 (App Router + Turbopack)
- Prisma 6.19.0 (SQLite)
- Tailwind CSS v3 (downgraded from v4 due to Turbopack incompatibility)
- TypeScript

### Run Locally

```bash
cd todo-app
cp .env.example .env
npm install
npx prisma migrate dev --name init
npm run dev
```

Open http://localhost:3000

## chub Stress Test Results

22 CLI operations tested after fixing the Windows path bug — all passed:

- `chub get` — 13 different docs (Next.js, React, Prisma, Tailwind, TypeScript, Vercel, ESLint, Anthropic)
- `chub search` — with and without query
- `chub get --json` — machine-readable output
- `chub get` — multiple docs in one call
- `chub annotate` — save, list, clear
- `chub feedback` — upvote/downvote
