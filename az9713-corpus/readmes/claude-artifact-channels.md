# Interactive Artifacts for Claude Code

Three Claude Code skills that progressively eliminate friction from the human ↔ Claude design feedback loop. Inspired by [Even Anthropic Engineers Use This Claude Code Workflow](https://www.youtube.com/watch?v=ASAaKhK1B5w).

## Demo

https://github.com/user-attachments/assets/1bb6ae7f-7e0f-43d1-9378-97f111d2e473

**[Channel Architecture — interactive diagram](https://az9713.github.io/claude-artifact-channels/channel-architecture.html)**
How the browser, Bun server, and Claude Code agent connect via MCP.

## The Three Layers

| Layer | Skill | What it does |
|-------|-------|-------------|
| 1 | `/static-html-artifacts` | Generate N design variations in one self-contained HTML file — pick the winner visually |
| 2 | `/interactive-bun-artifacts` | Promote to a Bun server with hot reload, click-to-comment, and Export to JSON |
| 3 | `/channel-connected-artifacts` | Wire the artifact directly to Claude Code via MCP — no copy-paste, comments trigger live queries |

## Quickstart

```bash
git clone https://github.com/az9713/claude-artifact-channels
cd claude-artifact-channels
claude
```

Type `/` in Claude Code — you should see `static-html-artifacts`, `interactive-bun-artifacts`, and `channel-connected-artifacts` in the list.

See [docs/getting-started/quickstart.md](docs/getting-started/quickstart.md) for a step-by-step walkthrough.

## Documentation

- [What is this?](docs/overview/what-is-this.md)
- [Prerequisites](docs/getting-started/prerequisites.md)
- [Quickstart](docs/getting-started/quickstart.md)
- [Layer 1 — Static artifacts](docs/guides/layer1-static-artifacts.md)
- [Layer 2 — Bun artifacts](docs/guides/layer2-bun-artifacts.md)
- [Layer 3 — Channel artifacts](docs/guides/layer3-channels.md)
- [Picking the right layer](docs/guides/picking-the-right-layer.md)
- [Channel server API reference](docs/reference/channel-server-api.md)
- [Troubleshooting](docs/troubleshooting/common-issues.md)

## Requirements

- Claude Code v2.1.80+ with a claude.ai login
- Bun (Layer 2 and 3 only) — `curl -fsSL https://bun.sh/install | bash`
- Node/Bun package install for Layer 3 — `cd [channel-name] && bun install`

## Credits

Workflow design and video by Ray. Skills, docs, and reference implementation by this repo.
