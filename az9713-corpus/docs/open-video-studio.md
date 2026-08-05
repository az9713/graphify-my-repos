---
repo: open-video-studio
description: Local-first AI video studio for OpenRouter models — fork of tonbistudio/open-video-studio with 12 new features
language: TypeScript
stars: 1
forks: 0
created: 2026-05-02
updated: 2026-07-08
topics: 
is_fork: False
kb: 113
---

# open-video-studio
# Open Video Studio

A local-first studio for generating and comparing AI videos through OpenRouter video models.

> **Based on** [tonbistudio/open-video-studio](https://github.com/tonbistudio/open-video-studio) — this fork adds 11 new features on top of the original. See [What's New](#whats-new) below.

> **Watch the original build:** [I Built an Open-Source Local AI Video Studio for OpenRouter Models](https://www.youtube.com/watch?v=69uN_e3qhfw&t=33s) by tonbistudio.

## What Works

- Save an OpenRouter API key locally.
- Sync video model metadata from OpenRouter.
- Generate text-to-video, image-to-video, and start+end-frame jobs.
- Persist jobs, prompts, payloads, model settings, and statuses in SQLite.
- Poll async jobs and save completed videos to a local output directory.
- Browse jobs, gallery items, and compare 2–4 completed local videos.
- Submit controlled batches with up to 3 selected models and up to 3 videos per model.
- **Enhance prompts** with LLM rewriting via OpenRouter chat completions (Claude Haiku).
- **Chain generations** — extract the last or first frame of a completed video and use it as the start frame of a new generation.
- Search and filter the Jobs list by prompt, model, status, or project.
- Drag-and-drop or paste images into frame upload zones.
- Bulk select, download, and delete jobs.
- View OpenRouter credit balance in Settings.
- Auto-download completed videos on poll.
- Track actual spend by model in Settings.
- Prompt history with favorites.
- Save and load model presets.
- Organize jobs into projects/folders.

## What's New

Features added in this fork on top of the original:

| Feature | Description |
|---------|-------------|
| **Prompt enhancer** | Click ✨ Enhance to rewrite any rough prompt into a detailed cinematic prompt using Claude Haiku via OpenRouter |
| **Frame chaining** | ↗ Chain extracts the last frame of a completed video as the first frame of a new generation — build multi-shot sequences |
| **Reuse frame** | ↺ Reuse frame re-extracts the first frame for another attempt from the same starting image |
| **Prompt history** | Every submitted prompt is saved and accessible from a dropdown; star favorites to pin them |
| **Model presets** | Save named parameter sets (model + duration + resolution + aspect ratio) and load them in one click |
| **Projects** | Assign jobs to named color-coded projects and filter the Jobs and Gallery tabs by project |
| **Job search & filter** | Search jobs by prompt text or model name; filter by status or project |
| **Bulk operations** | Multi-select jobs for bulk download or bulk delete |
| **Drag-and-drop / paste upload** | Drop images or paste from clipboard directly into the frame upload zones |
| **Spend tracking** | Settings tab shows actual costs by model, aggregated from completed job results |
| **Credit balance** | Settings tab shows your current OpenRouter credit balance |
| **Auto-download** | Optional setting to automatically save completed videos without a manual Download click |

## Run Locally

```bash
npm install
npm run build
npm start
```

Open:

```text
http://127.0.0.1:4317
```

For development with Vite and the local API:

```bash
npm run dev
```

Then open:

```text
http://127.0.0.1:5173
```

## Local Data

Runtime data is stored under `.ovstudio/`:

- `studio.sqlite` for settings, model cache, jobs, batches, assets, prompt history, presets, and projects
- `assets/` for uploaded frame images
- `outputs/` for downloaded videos unless changed in Settings

The app is designed for local use. Do not host it publicly with a saved API key.

## API Surface

The local backend exposes:

- `GET /api/settings`
- `PATCH /api/settings`
- `POST /api/settings/test`
- `GET /api/models/video`
- `POST /api/models/sync`
- `POST /api/assets/upload`
- `POST /api/jobs`
- `POST /api/batches`
- `GET /api/jobs`
- `GET /api/jobs/:id`
- `POST /api/jobs/:id/poll`
- `POST /api/jobs/poll-active`
- `POST /api/jobs/:id/download`
- `POST /api/jobs/:id/retry`
- `POST /api/jobs/:id/duplicate`
- `PATCH /api/jobs/:id/project`
- `DELETE /api/jobs/:id`
- `GET /api/gallery`
- `GET /api/account`
- `GET /api/stats/spend`
- `POST /api/prompts/enhance`
- `GET /api/prompts`
- `POST /api/prompts/use`
- `PATCH /api/prompts/:id/favorite`
- `DELETE /api/prompts/:id`
- `GET /api/presets`
- `POST /api/presets`
- `DELETE /api/presets/:id`
- `GET /api/projects`
- `POST /api/projects`
- `DELETE /api/projects/:id`

## Notes

Node 22's built-in SQLite module is used to avoid a native SQLite dependency. It may print an experimental warning depending on the installed Node build.

## Contributing

See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

See [SECURITY.md](SECURITY.md). This app stores API keys locally and should not be hosted publicly with a saved key.

## License

MIT. See [LICENSE](LICENSE).
