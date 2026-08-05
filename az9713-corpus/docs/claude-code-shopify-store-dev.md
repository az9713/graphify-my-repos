---
repo: claude-code-shopify-store-dev
description: Shopify Product Quiz app built with Claude Code, React Router, and Theme App Extensions
language: TypeScript
stars: 0
forks: 0
created: 2026-05-16
updated: 2026-05-16
topics: 
is_fork: False
kb: 589
---

# claude-code-shopify-store-dev
# product-quiz-app

A Shopify app featuring a **Product Quiz + Recommendation Widget** built as a Theme App Extension. Shoppers answer two questions on a product page and receive personalized product recommendations fetched live from the Shopify Storefront API — no page reload required.

> Built live in the session: [Claude Code Just Killed Every Shopify Agency](https://www.youtube.com/watch?v=x2pRavsHdls&t=6s)

---

## Demo

https://github.com/user-attachments/assets/29fc642d-170a-4e12-ae69-b0ce771a4f1f

---

## Features

- **Theme App Extension** — drag-and-drop quiz block merchants add to any product page via the Shopify theme editor
- **Storefront API integration** — fetches product recommendations client-side using tag-based filtering
- **Two-step quiz** — fully configurable questions, answer labels, and product tags via block settings (no code changes needed)
- **Zero-reload UX** — quiz flow and results render inline with vanilla JS
- **Remix / React Router backend** — embedded Shopify admin panel with Polaris web components

---

## Tech Stack

| Layer | Technology |
|---|---|
| App framework | [React Router v7](https://reactrouter.com/) (Shopify's recommended template) |
| Storefront UI | Shopify Theme App Extension (Liquid + vanilla JS + CSS) |
| Product data | [Shopify Storefront API](https://shopify.dev/docs/api/storefront) (GraphQL) |
| Admin API | [Shopify Admin GraphQL API](https://shopify.dev/docs/api/admin-graphql) |
| Database | SQLite via [Prisma](https://www.prisma.io/) |
| Auth | Shopify OAuth via `@shopify/shopify-app-react-router` |
| Dev tunnel | Cloudflare (via Shopify CLI) |

---

## Development Process

This app was scaffolded and developed end-to-end using the **Shopify CLI** and **Claude Code**.

### 1. Prerequisites

```bash
npm install -g @shopify/cli @shopify/theme
```

### 2. Scaffold the app

```bash
npm init @shopify/app@latest
# Select: Build a React Router app
# Language: TypeScript
# App name: product-quiz-app
```

### 3. Generate the Theme App Extension

```bash
cd product-quiz-app
shopify app generate extension
# Select: Theme app extension
# Name: product-quiz
```

### 4. Extension file structure

```
extensions/product-quiz/
  blocks/
    product-quiz.liquid    # Quiz UI block + schema (merchant-configurable settings)
  assets/
    product-quiz.js        # Quiz logic + Storefront API fetch
    product-quiz.css       # Styles
  shopify.extension.toml
```

### 5. Configure access scopes

In `shopify.app.toml`:

```toml
[access_scopes]
scopes = "write_products,write_metaobjects,write_metaobject_definitions,unauthenticated_read_product_listings,unauthenticated_read_product_inventory"
```

### 6. Start the dev server

```bash
shopify app dev
```

This starts a local Remix server, opens a Cloudflare tunnel, hot-reloads theme extension changes, and spins up a GraphiQL explorer for the Admin API.

### 7. Generate a Storefront API token

With the dev server running, open GraphiQL (`http://localhost:3457/graphiql`) and run:

```graphql
mutation {
  storefrontAccessTokenCreate(input: {title: "Product Quiz Token"}) {
    storefrontAccessToken {
      accessToken
    }
  }
}
```

Copy the returned token and paste it into the **Storefront API Token** field in the theme editor block settings.

### 8. Add the quiz to your theme

1. Open the Shopify theme editor
2. Switch to **Products → Default product** template
3. Click **Add section → Apps → Product Quiz**
4. Configure questions, answer labels, and matching product tags
5. Save

### 9. Tag your products

Products need tags that match your quiz options. Example:

| Product | Tags |
|---|---|
| Budget Everyday Item | `everyday, budget` |
| Premium Special Item | `special-occasion, premium` |

### 10. Deploy

```bash
shopify app deploy
```

---

## How the Quiz Works

1. Shopper sees **Question 1** with pill-style answer buttons
2. Selecting an answer records the associated product tag and reveals **Question 2**
3. After answering Question 2, the JS calls the Storefront API:
   ```
   products(query: "tag:everyday AND tag:budget")
   ```
4. Matching products render as clickable cards with image, title, and price

---

## Project Structure

```
product-quiz-app/
  app/
    routes/
      app._index.tsx       # Admin UI
      app.tsx              # App layout + auth
      auth.$.tsx           # OAuth handler
      webhooks.*.tsx        # Webhook handlers
    shopify.server.ts      # Shopify auth config
  extensions/
    product-quiz/          # Theme App Extension
  prisma/
    schema.prisma          # Session storage schema
  shopify.app.toml         # App config (scopes, URLs)
```

---

## Local Development

```bash
# Install dependencies
npm install

# Start dev server (handles tunnel + hot reload)
shopify app dev

# Preview theme extension
# Open: https://<your-store>.myshopify.com/products/<handle>?preview_theme_id=<id>
```

---

## Resources

- [Shopify App Development Docs](https://shopify.dev/docs/apps)
- [Theme App Extensions](https://shopify.dev/docs/apps/build/online-store/theme-app-extensions)
- [Storefront API Reference](https://shopify.dev/docs/api/storefront)
- [Shopify CLI Reference](https://shopify.dev/docs/apps/tools/cli)
- [Claude Code](https://claude.ai/claude-code)
