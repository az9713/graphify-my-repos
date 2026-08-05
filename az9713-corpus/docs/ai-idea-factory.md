---
repo: ai-idea-factory
description: Autonomous fictional product-ad pipeline and FORM/447 showcase, powered by GPT-5.6 Sol.
language: TypeScript
stars: 0
forks: 0
created: 2026-07-13
updated: 2026-07-13
topics: 
is_fork: False
kb: 19384
---

# ai-idea-factory
# FORM/447

FORM/447 is a public concept showcase created by an autonomous product-ad pipeline powered by GPT-5.6 Sol. The system invented seven fictional physical products, generated a hero still and two silent motion studies for each, performed visual QA with bounded retries, and assembled the accepted work into an editorial website.

## Live site

[View FORM/447 on Vercel](https://form-447.vercel.app)

## What is included

- 7 fictional product concepts across home goods, personal care, footwear, and apparel
- 7 GPT Image 2 hero stills
- 14 ten-second Kling 3.0 Turbo motion studies generated through Higgsfield
- A responsive Next.js showcase with explicit fictional and not-for-sale disclosures
- A hard Higgsfield reserve of 150 credits, with the run ending at 158.64 credits

The project was inspired by [I Gave GPT-5.6-Sol Unlimited Money to Make Ads (+Results)](https://www.youtube.com/watch?v=rbUFFMtKcaQ). This implementation deliberately replaced the video's open-ended budget framing with a bounded generation policy and auditable completion gates.

## Run locally

Requirements: Node.js 22.13 or newer.

```bash
npm install
npx vinext dev
```

Production checks:

```bash
npx next build
npm run lint
```

For the complete process, decisions, QA record, budget controls, and hosting forks, read [DEVELOPMENT_JOURNEY.md](./DEVELOPMENT_JOURNEY.md).

The reusable public workflow is available as a sanitized [master prompt](./master_prompt.md). Account balances, quotas, reserve values, credentials, personal information, and private reference assets have been removed from that template.

## Status

Every product, brand name, image, specification, and demonstration in FORM/447 is fictional. Nothing shown is manufactured, certified, endorsed, tested, or offered for sale.
