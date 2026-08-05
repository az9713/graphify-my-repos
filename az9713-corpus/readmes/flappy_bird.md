# Flappy Bird (Vanilla JS)

A lightweight Flappy Bird clone built with HTML5 Canvas and plain JavaScript.

## Run
- Open `index.html` in any modern browser (no build step).

## Controls
- Space or click/tap: flap
- P: pause/resume

## Files
- `index.html` – page shell and overlays
- `style.css` – layout and HUD styling
- `game.js` – game loop, physics, drawing, input

## Optional: Publish to GitHub
1. Initialize and commit:
   ```bash
   git init
   git add .
   git commit -m "Add Flappy Bird game"
   git branch -M main
   ```
2. Create a new empty repo on GitHub (no README), then:
   ```bash
   git remote add origin https://github.com/<your-user>/<repo-name>.git
   git push -u origin main
   ```

## Notes
- Best score persists via `localStorage`.
- Canvas scales for HiDPI displays.
