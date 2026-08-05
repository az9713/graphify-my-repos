# Open Skills, Refactored

A one-page, personal-navigation version of Nate B. Jones' excellent [Open Skills](https://unlock-ai.natebjones.com/open-skills) library.

This project keeps the spirit and inventory of the original Open Skills work, but presents it as a compact static page for easier personal browsing. The page groups skills by practical tasks, lets users jump from task groups to individual skill cards, and includes install prompts for each skill.

This is not an official Open Skills site and is not meant to replace the original. It is a local refactor for more convenient navigation of the original excellent content.

## What It Includes

- A single-page static site in `index.html`
- 31 skill cards
- 7 use-case chains
- 31 install prompts
- Skill-group navigation with clickable skill links
- A task launcher in the hero that jumps directly to relevant skills
- A prompt browser with copy support
- Detail panels for outputs, requirements, and verification steps

## View The Page

- [Open the local static page](./index.html)
- Live page: <https://az9713.github.io/open-skills-refactored/>

## Design

The visual style imports the local `Anthropic Design System/` materials from Claude Design. The page uses the Anthropic-inspired warm paper background, Crail accent, restrained borders, editorial type direction, and the provided Anthropic mark asset.

Only the design-system files required by this static page are included in the published project.

## Build And Testing Notes

This was built with Codex using a persistent `/goal` workflow.

Codex's built-in browser tooling was used to test component functionality. In practical terms, the page was opened in the built-in browser/Chrome DevTools environment and checked for:

- Skill, use-case, and prompt counts
- Search behavior
- Skill-group jump links
- Hero task-launcher links
- Prompt selection
- Detail panel open/close behavior
- Responsive overflow on desktop, tablet, and mobile

Additional headless Edge checks were used to capture responsive screenshots during development.

## Keeping This Page In Sync

A GitHub Action (`.github/workflows/sync-open-skills.yml`) checks the source Open Skills site on a weekly schedule — and on demand via the Actions tab's **Run workflow** button — and opens a pull request when new skills or runbooks appear. The sync logic lives in `.claude/sync-open-skills.md`; the workflow needs a `CLAUDE_CODE_OAUTH_TOKEN` repository secret (generate it with `claude setup-token`).

### Reusable skill and command

The sync pattern is generalized into a Claude Code skill so it can be reused for any repo that tracks an external source:

- `.claude/skills/external-source-sync-action/` — the skill. It investigates where the repo stores its data and whether the source is fetchable, then generates the workflow plus a per-repo instruction file and walks you through the secret and first run.
- `.claude/commands/sync-setup.md` — a `/sync-setup [source URL]` slash command that invokes the skill.

## Run Locally

Open `index.html` directly in a browser, or serve the folder locally:

```powershell
python -m http.server 8765 --bind 127.0.0.1
```

Then visit:

```text
http://127.0.0.1:8765/index.html
```

## Source Credit

All credit for the Open Skills concept and original library goes to Nate B. Jones:

- [Open Skills](https://unlock-ai.natebjones.com/open-skills)
- [Open Skills directory](https://unlock-ai.natebjones.com/open-skills/skills)
- [Open Skills runbooks](https://unlock-ai.natebjones.com/open-skills/runbooks)