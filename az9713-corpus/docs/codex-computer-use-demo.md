---
repo: codex-computer-use-demo
description: 
language: None
stars: 0
forks: 0
created: 2026-05-30
updated: 2026-05-30
topics: 
is_fork: False
kb: 3797
---

# codex-computer-use-demo
# Codex Computer Use — MSPaint Demo

Codex Desktop's **Computer Use** plugin controlling MSPaint to draw a busy village marketplace from scratch — no image generation, pure brush strokes.

## Demo

https://github.com/user-attachments/assets/6926e391-523d-47a2-b64a-ad03be6c33ed

## What it does

Codex autonomously:

1. Launched MSPaint via the Computer Use helper
2. Captured a window screenshot to get a valid coordinate reference
3. Selected colors from the Paint palette by pixel coordinate
4. Drew the entire scene using `drag` brush strokes — sky, buildings, market stalls, bunting, baskets, and 20 stick-figure people

Nothing was pasted or generated. Every pixel was painted by Codex clicking and dragging inside the real MSPaint window.

## How it works

The Computer Use plugin exposes a named Windows pipe:

```
\\.\pipe\codex-computer-use-<session-id>
```

Codex communicates with it using a length-prefixed JSON protocol (little-endian frame headers on Windows). The key actions used:

| Action | Purpose |
|---|---|
| `launch_app` | Open MSPaint |
| `list_windows` | Find the Paint window handle |
| `get_window_state` | Capture a screenshot + get `screenshotId` |
| `click` | Select brush tool, change palette color |
| `drag` | Draw brush strokes on the canvas |

Every coordinate input requires a current `screenshotId` — Computer Use rejects clicks without a fresh window snapshot.

## Drawing approach

The scene was built in layers using helper functions:

```js
async function color(name) {
  const [x, y] = colors[name];
  await click(x, y);            // click palette swatch
}

async function drag(x1, y1, x2, y2) {
  await req(s, "drag", { window: w, screenshotId, from_x: x1, from_y: y1, to_x: x2, to_y: y2 });
}

async function person(x, y, bodyColor) {
  await color("orange");
  await drag(x - 3, y, x + 3, y);   // head
  await drag(x, y - 3, x, y + 3);
  await color(bodyColor);
  await drag(x, y + 5, x, y + 28);  // body
  await drag(x, y + 13, x - 9, y + 23); // left arm
  await drag(x, y + 13, x + 9, y + 23); // right arm
  await drag(x, y + 28, x - 7, y + 42); // left leg
  await drag(x, y + 28, x + 7, y + 42); // right leg
}
```

**Layers drawn:**
- Sky (light blue strokes) + sun
- Village buildings with rooftops
- Three market stalls with striped awnings (red/yellow, blue/green, orange/pink)
- Support poles, tables, baskets, and produce
- Hanging bunting across the top
- 20 stick-figure people in various colors throughout the square

## Key technical issues solved

**Node REPL tool missing** — the Computer Use plugin was installed but its normal `mcp__node_repl__js` execution surface never appeared. The workaround was to talk to the named pipe directly from a small Node.js client.

**Wrong byte order** — the first pipe client used big-endian frame lengths. Inspecting `computer-use-client.mjs` revealed Windows requires little-endian (`writeUInt32LE`). Switching to LE unblocked all responses.

**`screenshotId` required** — coordinate input fails with `call get_window_state before issuing coordinate input` unless a fresh screenshot id is attached to every action.
