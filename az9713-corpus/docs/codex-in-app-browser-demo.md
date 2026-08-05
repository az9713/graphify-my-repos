---
repo: codex-in-app-browser-demo
description: Test of the Codex app in-app browser feature
language: HTML
stars: 0
forks: 0
created: 2026-05-04
updated: 2026-05-04
topics: 
is_fork: False
kb: 6849
---

# codex-in-app-browser-demo
# Codex In-App Browser — Daily AI Coding Test

A hands-on test of the **Codex app's in-app browser** feature, exploring whether it can replace external browser testing tools like Playwright.

## YouTube Video

**I Tried NEW Codex In-App Browser: No Need for Playwright Tests?**
[https://www.youtube.com/watch?v=nkN45mVXdj8&t=133s](https://www.youtube.com/watch?v=nkN45mVXdj8&t=133s)

## Demo Video

https://github.com/user-attachments/assets/4a55d9de-2a5c-4fa7-9a09-72142f178d98

## What Was Tested

The Codex in-app browser lets you open a local web page directly inside the Codex app and interact with it via `@Browser` — annotating elements, leaving comments, and having Codex act on them automatically.

**Session walkthrough:**

1. **Coffee landing page** — asked Codex to create a landing page for a high-end coffee shop. It generated `coffee_landing_page.html` and served it at `http://localhost:8000`.

2. **In-app browser annotation** — opened the page via `@Browser`, right-clicked the hero heading "Aurelia Coffee", added a comment: *"Change Aurelia Coffee to Auralia Coffee in the entire web page"*, and submitted it. Codex processed the annotation, updated all 6 occurrences in the HTML, reloaded the tab, and verified the change.

**Result: it works** — once the in-app browser pane is open, `@Browser` can bind to it and act on annotations in the live page.

## Files

| File | Description |
|------|-------------|
| `coffee_landing_page.html` | Landing page generated during the test session |
| `codex_in_app_browser_demo_compressed.mp4` | Compressed screen recording of the session (6.98 MB) |

## References

- [Codex In-App Browser — Official Docs](https://developers.openai.com/codex/app/browser)
