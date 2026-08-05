---
repo: resume-list-polish
description: Resume bullet rewriter SaaS — paste a weak resume bullet, get a recruiter-ready rewrite back. Free 5/day, Pro 100/day for $5/month.
language: TypeScript
stars: 0
forks: 0
created: 2026-07-16
updated: 2026-07-16
topics: 
is_fork: False
kb: 130
---

# resume-list-polish
# resume-list-polish

**resume-list-polish helps job seekers rewrite weak resume bullet points so they stop
getting filtered out by recruiters.** Free: 5 rewrites/day. Pro: 100/day,
$5/month via Stripe.

Built following `../SOLO_DEV_PLAYBOOK.md`. Requirement-by-requirement coverage:
[`PLAYBOOK_COMPLIANCE.md`](PLAYBOOK_COMPLIANCE.md). Ops guide: [`RUNBOOK.md`](RUNBOOK.md).

**Full documentation:** [`docs/`](docs/index.md) — overview, concepts (auth, RLS,
rate limiting, payments, the rewrite pipeline), guides, API/schema/env reference,
and architecture decision records.

## Stack (the playbook's, exactly)
Next.js (front + API routes) · Vercel · Supabase (Postgres + Auth + RLS) ·
Stripe (Checkout + Billing Portal + webhook) · Upstash (rate limiting) ·
Anthropic (the AI rewrite) · Zod (server-side validation).

## Setup

**New here? Follow [`SETUP_GUIDE.md`](SETUP_GUIDE.md) top to bottom** — it walks
through every account, key, and the auth/Stripe/Upstash wiring step by step. The
condensed version:

1. **Keys** — copy `.env.local.example` to `.env.local` and fill in every value
   (Supabase, Stripe, Upstash, Anthropic). Comments in the file say where each
   one comes from.
2. **Database** — Supabase Dashboard → SQL Editor → paste `supabase/schema.sql`
   → Run. Creates tables, RLS policies, and the profile-on-signup trigger.
3. **Supabase auth config** — Auth → URL Configuration: set Site URL. Auth →
   Email Templates → Confirm signup: link to
   `{{ .SiteURL }}/auth/confirm?token_hash={{ .TokenHash }}&type=signup`.
4. **Stripe** — create a $5/month recurring price → its id is `STRIPE_PRICE_ID`.
   Webhook endpoint `https://<your-app>/api/stripe-webhook` with events
   `checkout.session.completed`, `customer.subscription.updated`,
   `customer.subscription.deleted`. Locally:
   `stripe listen --forward-to localhost:3000/api/stripe-webhook`.
5. **Run** — `npm install && npm run dev` → http://localhost:3000
6. **Deploy** — push to GitHub, import in Vercel, add the same env vars
   (Production + Preview). Full go-live checklist: `PLAYBOOK_COMPLIANCE.md` Part 6.

## Layout

```
app/page.tsx              landing (logged out) / the app (logged in)
app/rewriter.tsx          client UI: rewrite, upgrade, billing, history
app/login/page.tsx        Supabase email+password auth
app/auth/confirm/route.ts email-confirmation link handler
app/api/rewrite/route.ts  THE endpoint: auth → validate → rate limit → AI → save
app/api/checkout/route.ts Stripe Checkout session (subscription)
app/api/portal/route.ts   Stripe Billing Portal (self-serve cancel)
app/api/stripe-webhook/…  signature-verified webhook → flips is_pro
lib/supabase/*            server/browser Supabase clients
lib/ratelimit.ts          Upstash limiters (free 5/day, pro 30/min)
proxy.ts                  session refresh on every request (Next 16 middleware)
supabase/schema.sql       tables + RLS + signup trigger
```
