---
repo: nori-craft
description: Organic ramen eatery landing page - Tesla minimalism meets Claude warmth
language: TypeScript
stars: 0
forks: 0
created: 2025-12-24
updated: 2025-12-24
topics: 
is_fork: False
kb: 81
---

# nori-craft
# Nori Craft

A landing page for an organic ramen eatery, featuring Tesla-inspired minimalism with Claude's warm aesthetic.

![Next.js](https://img.shields.io/badge/Next.js-16.1-black?style=flat-square&logo=next.js)
![React](https://img.shields.io/badge/React-19-61DAFB?style=flat-square&logo=react)
![Tailwind CSS](https://img.shields.io/badge/Tailwind-v4-38B2AC?style=flat-square&logo=tailwind-css)
![TypeScript](https://img.shields.io/badge/TypeScript-5.x-3178C6?style=flat-square&logo=typescript)

## Preview

**Design Direction**: "Refined Industrial Warmth" — the tension between cold tech precision and warm organic craft.

### Features

- Massive responsive typography (up to 11rem headlines)
- Scroll-triggered animations with Intersection Observer
- Floating glass-morphic navigation
- Featured menu cards with inverted themes
- Dark philosophy section with giant watermarks
- Warm cream backgrounds with terracotta accents

## Tech Stack

- **Framework**: Next.js 16.1 (App Router)
- **UI**: React 19, shadcn/ui components
- **Styling**: Tailwind CSS v4
- **Typography**: Unbounded (display) + Outfit (body)
- **Language**: TypeScript

## Getting Started

```bash
# Install dependencies
npm install

# Run development server
npm run dev

# Build for production
npm run build

# Start production server
npm start
```

Open [http://localhost:3000](http://localhost:3000) to view the site.

## Project Structure

```
src/
├── app/
│   ├── globals.css      # Theme variables, animations
│   ├── layout.tsx       # Root layout, fonts
│   └── page.tsx         # Landing page components
├── components/
│   └── ui/              # shadcn components
└── lib/
    └── utils.ts         # Utility functions
```

## Design System

### Color Palette

| Token | Light | Dark | Usage |
|-------|-------|------|-------|
| `--background` | `#FFFCF9` | `#0D0D0D` | Page background |
| `--foreground` | `#1A1A1A` | `#FAFAFA` | Primary text |
| `--coral` | `#DA7756` | `#DA7756` | Accent color |
| `--cream` | `#FEF8F3` | `#151311` | Hover states |

### Typography

- **Display**: Unbounded — bold, geometric, modern
- **Body**: Outfit — clean, readable, approachable

## Sections

1. **Hero** — Massive "Pure craft" headline with floating stats card
2. **Menu** — Four bowls grid with featured signature dish
3. **Philosophy** — Dark section with "Less, but better" messaging
4. **Location** — Contact info with styled map placeholder
5. **Footer** — Minimal with social links

## Development

This project was built using:

- **Claude Code** — AI pair programming
- **Anthropic frontend-design skill** — Design guidance
- **Claude in Chrome** — Browser automation & visual testing

See [DESIGN.md](./DESIGN.md) for detailed design documentation.

## Deploy

[![Deploy with Vercel](https://vercel.com/button)](https://vercel.com/new/clone?repository-url=https://github.com/az9713/nori-craft)

## License

MIT
