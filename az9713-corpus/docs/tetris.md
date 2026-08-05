---
repo: tetris
description: A modern Tetris game built with HTML5 Canvas and vanilla JavaScript
language: JavaScript
stars: 0
forks: 0
created: 2025-09-03
updated: 2025-09-03
topics: 
is_fork: False
kb: 124
---

# tetris
# Tetris Game

🎮 A modern, web-based Tetris game built with HTML5 Canvas and vanilla JavaScript. Features classic Tetris gameplay with smooth animations, procedurally generated sound effects, and a responsive design.

[![Live Demo](https://img.shields.io/badge/Live-Demo-brightgreen?style=for-the-badge)](https://az9713.github.io/tetris)
[![GitHub](https://img.shields.io/badge/GitHub-Repository-blue?style=for-the-badge)](https://github.com/az9713/tetris)
[![Claude Code](https://img.shields.io/badge/Built%20with-Claude%20Code-purple?style=for-the-badge)](https://claude.ai/code)

## ✨ Features

- 🎮 **Classic Tetris Gameplay**: All 7 authentic tetromino pieces with proper rotation
- 🎵 **Dynamic Audio**: Procedurally generated sound effects and background music using Web Audio API
- 📱 **Cross-Platform**: Responsive design that works seamlessly on desktop and mobile browsers
- 💾 **Persistent Storage**: High score tracking with localStorage
- ⚡ **Smooth Performance**: 60fps gameplay with optimized Canvas rendering
- 🎯 **Progressive Challenge**: Increasing difficulty with level progression
- ⏸️ **Game Controls**: Pause/resume functionality and intuitive keyboard controls
- 👻 **Visual Aids**: Ghost piece preview showing drop location
- 🌐 **No Dependencies**: Pure vanilla JavaScript with no external libraries
- 🔧 **Developer Friendly**: Modular ES6 architecture with comprehensive testing

## 🎮 Controls

| Key | Action |
|-----|--------|
| **← →** | Move piece left/right |
| **↑** | Rotate piece clockwise |
| **↓** | Soft drop (faster fall) |
| **Space** | Hard drop (instant drop to bottom) |
| **P** | Pause/Resume game |
| **Enter** | Start new game |
| **Escape** | Pause game |

> **Tip**: Use the ghost piece (faded outline) to see where your piece will land!

## 🚀 Quick Start

### Option 1: Play Online (Easiest)
Just visit the [**Live Demo**](https://az9713.github.io/tetris) - no installation required!

### Option 2: Run Locally

1. **Clone the repository:**
   ```bash
   git clone https://github.com/az9713/tetris.git
   cd tetris
   ```

2. **Install dependencies:**
   ```bash
   npm install
   ```

3. **Start the development server:**
   ```bash
   npm run dev
   # or alternatively:
   python -m http.server 8000
   ```

4. **Open your browser:**
   - Go to `http://localhost:8000` for the modular version
   - Or open `game.html` directly for the standalone version

### Option 3: Offline Play
Simply download and open `game.html` in any modern browser - works completely offline!

## 🛠️ Development Scripts

| Command | Description |
|---------|-------------|
| `npm run dev` | Start development server with live reload |
| `npm start` | Serve the game in production mode |
| `npm test` | Run Jest test suite with coverage |
| `npm run test:watch` | Run tests in watch mode |
| `npm run lint` | Check code style with ESLint |
| `npm run lint:fix` | Fix linting issues automatically |
| `npm run format` | Format code with Prettier |
| `npm run typecheck` | TypeScript-style type checking with JSDoc |
| `npm run build` | Production build (runs lint, test, and optimizations) |
| `npm run deploy` | Deploy to GitHub Pages |

## 🎯 Game Rules & Scoring

### Basic Rules
- **Objective**: Fill complete horizontal lines to clear them and earn points
- **Speed**: Game automatically speeds up as you progress through levels  
- **Game Over**: When pieces reach the top of the playing field
- **Level Up**: Every 10 lines cleared increases your level

### Scoring System
| Line Clear | Base Score | Formula |
|------------|------------|----------|
| **Single** | 40 points | 40 × current level |
| **Double** | 100 points | 100 × current level |
| **Triple** | 300 points | 300 × current level |
| **Tetris** (4 lines) | 1200 points | 1200 × current level |
| **Soft Drop** | 1 point per cell | - |
| **Hard Drop** | 2 points per cell | - |

### Strategy Tips
- **Save the I-piece**: Keep one column open for Tetris clears (4-line bonus)
- **Stack efficiently**: Avoid creating holes that are hard to fill
- **Plan ahead**: Use the next piece preview to optimize placement

## 📁 Project Structure

```
tetris/
├── 📄 index.html              # Main HTML file (requires server)
├── 📄 game.html               # Standalone version (works offline)
├── 📄 CLAUDE.md              # Claude Code integration guide
├── 📄 HOW-TO-PLAY.md         # Detailed gameplay instructions
├── 📄 CONTRIBUTING.md        # Developer contribution guide
├── 📁 src/                    # Source code
│   ├── 📄 main.js             # Application entry point
│   ├── 📄 styles.css          # Game styling
│   ├── 📁 classes/            # Core game classes
│   │   ├── 📄 Game.js         # Main game controller
│   │   ├── 📄 Board.js        # Game board logic
│   │   ├── 📄 Tetromino.js    # Individual piece logic
│   │   ├── 📄 TetrominoFactory.js # Piece generation system
│   │   ├── 📄 Renderer.js     # Canvas rendering engine
│   │   ├── 📄 InputHandler.js # Keyboard input management
│   │   ├── 📄 SoundManager.js # Web Audio API sound system
│   │   └── 📄 ScoreManager.js # Scoring and localStorage
│   └── 📁 constants/          # Game configuration
│       ├── 📄 gameConstants.js
│       ├── 📄 tetrominoShapes.js
│       └── 📄 colors.js
├── 📁 tests/                  # Jest test suite
├── 📁 docs/                   # Documentation
└── 📁 .github/
    └── 📁 workflows/          # GitHub Actions CI/CD
        └── 📄 claude-code.yml # Claude Code integration
```

## 🔧 Technology Stack

### Core Technologies
- **HTML5 Canvas** - High-performance 2D rendering
- **Vanilla JavaScript (ES6+)** - Modern JavaScript without dependencies
- **Web Audio API** - Procedural sound generation
- **CSS3** - Responsive styling and animations

### Development Tools
- **Jest** - Unit testing with 90%+ coverage
- **ESLint** - Code quality and consistency
- **Prettier** - Automatic code formatting
- **GitHub Actions** - Automated CI/CD pipeline
- **Claude Code Integration** - AI-powered development workflow

### Browser Compatibility
- ✅ Chrome 60+
- ✅ Firefox 60+ 
- ✅ Safari 12+
- ✅ Edge 79+
- 📱 Mobile browsers (iOS Safari, Chrome Mobile)

## 🤝 Contributing

We welcome contributions! This project is built with Claude Code and follows modern development practices.

### Quick Contribution Guide
1. **Fork** the repository
2. **Create** a feature branch: `git checkout -b feature/amazing-feature`
3. **Make** your changes following our coding standards
4. **Test** your changes: `npm test`
5. **Commit** with conventional format: `git commit -m 'feat: add amazing feature'`
6. **Push** to your branch: `git push origin feature/amazing-feature`
7. **Open** a Pull Request

### Development Setup
```bash
# Fork and clone the repo
git clone https://github.com/yourusername/tetris.git
cd tetris

# Install dependencies
npm install

# Start development server
npm run dev

# Run tests
npm test
```

📖 **Read our detailed [CONTRIBUTING.md](CONTRIBUTING.md) for coding standards, testing guidelines, and development workflows.**

## 📸 Screenshots

<div align="center">

| Menu Screen | Gameplay | Game Over |
|-------------|----------|----------|
| ![Menu](docs/screenshots/menu.png) | ![Gameplay](docs/screenshots/gameplay.png) | ![Game Over](docs/screenshots/game-over.png) |

</div>

## 🏆 Achievements & Goals

### Beginner Goals
- 🎯 Score 1,000+ points
- 📏 Clear 10+ lines  
- ⏱️ Play for 5+ minutes

### Intermediate Goals
- 🎯 Score 10,000+ points
- 📏 Clear 50+ lines
- 📶 Reach level 5+
- 💎 Achieve a Tetris (4-line clear)

### Advanced Goals
- 🎯 Score 100,000+ points
- 📏 Clear 200+ lines
- 📶 Reach level 10+
- 🚄 Master high-speed gameplay

## 🙏 Acknowledgments

- **Classic Tetris** - Inspired by the timeless puzzle game by Alexey Pajitnov
- **Modern Web Standards** - Built with HTML5, ES6+, and Web APIs
- **Claude Code** - AI-powered development workflow
- **Open Source Community** - Thank you to all contributors!

## 📄 License

This project is licensed under the **MIT License** - see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**🎮 [Play Now](https://az9713.github.io/tetris) | 🐙 [View Source](https://github.com/az9713/tetris) | 🤖 [Built with Claude Code](https://claude.ai/code)**

*Built with ❤️ and modern web technologies*

</div>