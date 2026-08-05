---
repo: present-follow-along
description: 
language: HTML
stars: 0
forks: 0
created: 2026-03-22
updated: 2026-03-22
topics: 
is_fork: False
kb: 70
---

# present-follow-along
# Present — Web-Based URL Presentation Tool

> **Status: Prototype / Work in Progress.** This project is functional but still under active development. Expect rough edges, missing features, and breaking changes. Contributions and feedback welcome.

A cross-platform web app where each slide is a URL. Build presentations as a list of web pages and present them fullscreen with keyboard navigation and mobile remote control.

## Motivation

This project was inspired by Simon Willison's blog post ["I Vibe Coded My Dream macOS Presentation App"](https://simonwillison.net/2026/Feb/25/present/), where he built a SwiftUI macOS app called [Present](https://github.com/simonw/present) in ~45 minutes using AI-assisted coding. His app displays a sequence of URLs fullscreen — perfect for technical talks where the "slides" are live web pages, documentation, and code repos.

We wanted to run it on Windows. Since SwiftUI is macOS-only, we ported it to a **pure web app** (Node.js + vanilla HTML/CSS/JS) with zero npm dependencies, then added several new features on top.

## What's New (beyond the original)

| Feature | Description |
|---------|-------------|
| **Speaker Notes & Timer** | Per-slide notes visible on your phone remote, elapsed timer during presentation |
| **URL Embed Checker** | Pre-scans all URLs and warns which sites block iframe embedding (the web app's main limitation vs native) |
| **Live Audience View** | Audience members open a URL on their phones and auto-follow your slides in real-time via Server-Sent Events |
| **Slide Strip Overlay** | Press `G` during presentation to show a horizontal thumbnail bar for visual navigation |
| **QR Code Overlay** | Press `L` to display a QR code so audience can join the live view |
| **SSE Real-Time Sync** | All views (editor, presentation, remote, live) sync instantly — an upgrade over the original's polling |

## Quick Start

```bash
cd web-app
node server.js
```

Then open:

| Page | URL | Who uses it |
|------|-----|-------------|
| Editor | http://localhost:9123 | Presenter (build your slide list) |
| Presentation | http://localhost:9123/present | Audience sees this (fullscreen) |
| Remote | http://\<your-ip\>:9123/remote | Presenter (control from phone) |
| Live | http://\<your-ip\>:9123/live | Audience (follow along on their device) |

**Requirements:** Node.js 18+ and a modern browser. No `npm install` needed.

## How It Works

1. Create a text file with one URL per line (optionally add speaker notes after a tab)
2. Start the server, open the editor, load your file
3. Click **Check** to verify all URLs will display (some sites block iframe embedding)
4. Click **Play** or press `Ctrl+Shift+P` — presentation opens in a new tab
5. Use arrow keys to navigate, or control from your phone

## Known Limitation

The web app displays URLs inside `<iframe>` elements. Many major websites (GitHub, Reddit, Twitter, Google, Substack, etc.) block iframe embedding via security headers. The original Swift app doesn't have this limitation because `WKWebView` ignores these headers.

The **Check** button in the editor scans all URLs and warns you before presenting. Sites that work well: Wikipedia, Python docs, personal blogs, direct image URLs, and your own websites.

## Documentation

| Document | Contents |
|----------|----------|
| [User Guide](docs/USER-GUIDE.md) | How to use the app — for presenters and audience members |
| [Feature Mapping](docs/FEATURE-MAPPING.md) | 54-feature comparison across blog post, Swift app, and web app |
| [Development Journey](docs/DEVELOPMENT-JOURNEY.md) | Detailed account of porting from Swift to web, every problem and solution |

## Project Structure

```
web-app/                         # The web app (this is what you run)
    server.js                    # Node.js server — state, API, SSE
    public/
        editor.html              # Slide editor with sidebar + preview
        present.html             # Fullscreen presentation view
        remote.html              # Mobile remote control
        live.html                # Read-only audience view

Present/                         # Reference: SwiftUI macOS implementation
    Present/
        Slide.swift              # Data model
        WebView.swift            # WKWebView wrapper
        ContentView.swift        # Editor UI
        PresentationWindow.swift # Fullscreen + overlays
        RemoteServer.swift       # HTTP server
        PresentApp.swift         # App entry point

docs/
    USER-GUIDE.md                # End-user documentation
    FEATURE-MAPPING.md           # Feature comparison across all versions
    DEVELOPMENT-JOURNEY.md       # How we built it, what went wrong, lessons learned
    presentations.txt            # Sample presentation file (verified working URLs)
```

## Acknowledgments

This project is motivated by and based on Simon Willison's [Present](https://github.com/simonw/present) app, described in his blog post ["I Vibe Coded My Dream macOS Presentation App"](https://simonwillison.net/2026/Feb/25/present/) (February 25, 2026). The original is a 716-line SwiftUI macOS app with zero dependencies. Our web port aims to bring the same experience to any platform with a browser.

## License

This project is for educational and personal use. The original Present app by Simon Willison is licensed under [Apache 2.0](https://github.com/simonw/present/blob/main/LICENSE).
