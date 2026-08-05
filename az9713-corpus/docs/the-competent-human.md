---
repo: the-competent-human
description: A gamified skill tracker based on Heinlein's 21 skills every human should master
language: TypeScript
stars: 0
forks: 0
created: 2026-01-31
updated: 2026-01-31
topics: 
is_fork: False
kb: 903
---

# the-competent-human
# The Competent Human

A gamified skill tracker based on Robert A. Heinlein's famous quote about the 21 skills every well-rounded human should master.

> "A human being should be able to change a diaper, plan an invasion, butcher a hog, conn a ship, design a building, write a sonnet, balance accounts, build a wall, set a bone, comfort the dying, take orders, give orders, cooperate, act alone, solve equations, analyze a new problem, pitch manure, program a computer, cook a tasty meal, fight efficiently, die gallantly. Specialization is for insects."
>
> — Robert A. Heinlein, *Time Enough for Love* (1973)

---

## About Robert A. Heinlein

**Robert Anson Heinlein** (1907–1988) was an American science fiction author, aeronautical engineer, and naval officer. Often called the "Dean of Science Fiction Writers," he was one of the most influential and controversial authors of the genre.

Heinlein's works include classics such as *Stranger in a Strange Land*, *Starship Troopers*, *The Moon Is a Harsh Mistress*, and *Time Enough for Love*. His writing explored themes of individualism, self-reliance, libertarianism, and the importance of practical competence.

The quote that inspired this app comes from his character Lazarus Long in *Time Enough for Love*, reflecting Heinlein's belief that a well-rounded human should be capable in many areas rather than narrowly specialized. This philosophy of competence and self-sufficiency runs throughout his body of work.

Heinlein won four Hugo Awards for Best Novel and was the first science fiction writer to appear on the New York Times Best Seller list. His influence extends beyond literature into science, technology, and popular culture.

---

## Screenshot

![The Competent Human Dashboard](public/images/competent_human_dashboard.jpg)

*The dashboard showing all 21 skills with the retro sci-fi CRT aesthetic*

---

## Features

- **21 Skills** - Track all skills from Heinlein's quote
- **XP System** - Earn 10/25/50 XP based on effort level
- **Tier Progression** - Novice → Apprentice → Journeyman → Master
- **Streak Bonuses** - Up to 2x XP for consistent daily practice
- **Competence Score** - See your overall progress percentage
- **Activity History** - Track what you've practiced and when
- **Reset Options** - Reset individual skills or start fresh
- **Retro Sci-Fi Theme** - CRT-style visuals with amber/green terminal aesthetic
- **Offline Ready** - All data stored locally in your browser

---

## Quick Start

```bash
# Install dependencies
npm install

# Start development server
npm run dev

# Open http://localhost:5173 in your browser
```

See [docs/QUICK_START.md](docs/QUICK_START.md) for a 2-minute user guide.

---

## Documentation

| Document | Audience | Description |
|----------|----------|-------------|
| [QUICK_START.md](docs/QUICK_START.md) | Users | 2-minute guide to get tracking |
| [USER_GUIDE.md](docs/USER_GUIDE.md) | Users | Complete user manual with 10 use cases |
| [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | Developers | Comprehensive dev guide for web newcomers |
| [CLAUDE.md](CLAUDE.md) | AI Assistants | Context for AI coding assistants |

---

## Tech Stack

| Technology | Version | Purpose |
|------------|---------|---------|
| React | 19 | UI library |
| TypeScript | 5.9 | Type-safe JavaScript |
| Vite | 7 | Build tool & dev server |
| Tailwind CSS | 4 | Utility-first styling |
| React Router | 7 | Client-side routing |

---

## Project Structure

```
src/
├── components/       # Reusable UI components
├── context/          # Global state (UserDataContext)
├── data/             # Static data (21 skills)
├── pages/            # Page components (Dashboard, SkillDetail)
├── services/         # Data operations (localStorage)
├── types/            # TypeScript definitions
├── utils/            # Helper functions (XP, dates)
├── App.tsx           # Root component
├── index.css         # Global styles
└── main.tsx          # Entry point
```

---

## Available Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server |
| `npm run build` | Build for production |
| `npm run preview` | Preview production build |

---

## XP & Progression System

### Effort Levels
| Level | XP |
|-------|-----|
| Light | 10 |
| Moderate | 25 |
| Intensive | 50 |

### Tier Thresholds
| Tier | XP Required |
|------|-------------|
| Novice | 0 |
| Apprentice | 100 |
| Journeyman | 300 |
| Master | 600 |

### Streak Multipliers
| Days | Bonus |
|------|-------|
| 3+ | 1.1x |
| 7+ | 1.25x |
| 14+ | 1.5x |
| 30+ | 2.0x |

---

## Deployment

Configured for Netlify:

```bash
# Build
npm run build

# Output directory
dist/
```

Or connect your GitHub repo to Netlify for automatic deployments.

---

## Browser Support

- Chrome (recommended)
- Firefox
- Safari
- Edge

Data is stored in localStorage. Private/incognito mode will not persist data between sessions.

---

## Contributing

1. Read [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md)
2. Make changes
3. Test with `npm run dev` and `npm run build`
4. Submit a pull request

---

## License

MIT

---

## Acknowledgments

- **Robert A. Heinlein** (1907–1988) for the inspiring quote from *Time Enough for Love*
- **Original Inspiration:** This work was inspired by [The Competent Human](https://thriving-puffpuff-8d2c77.netlify.app/)
- **Development:** All code and documentation were generated by [Claude Code](https://claude.ai/code) (Anthropic's AI coding assistant)
- The retro computing aesthetic that never goes out of style
