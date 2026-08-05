---
repo: writer-voice-skills
description: Claude plugin for creating, auditing, and updating writing voice skills
language: None
stars: 0
forks: 0
created: 2026-05-06
updated: 2026-05-06
topics: 
is_fork: False
kb: 11
---

# writer-voice-skills
# Voice Plugin for Claude

This project packages three Claude writing skills into a reusable plugin:

- `voice-create` builds a persona-based voice profile from writing samples.
- `voice-audit` checks an existing voice profile against recent writing.
- `voice-update` refreshes a voice profile with audits, new samples, or feedback.

The project is inspired by the video
["Every writer NEEDS these 3 Claude skills."](https://www.youtube.com/watch?v=Hd0AH6k21iI)
and Alex McFarland's Substack article
["Every writer needs these 3 Claude skills."](https://alexmcfarland.substack.com/p/every-writer-needs-these-3-claude).

Readers should watch the YouTube video and read the Substack article for the
original framing, motivation, and workflow explanation behind this voice-profile
system.

This plugin was created by ChatGPT 5.5 Thinking Extended and Codex with 5.5
High.

## Directory Structure

```text
.
├── README.md
├── voice-audit.md
├── voice-create.md
├── voice-update.md
└── voice-plugin/
    ├── README.md
    ├── .claude-plugin/
    │   └── plugin.json
    └── skills/
        ├── voice-audit/
        │   └── SKILL.md
        ├── voice-create/
        │   ├── SKILL.md
        │   └── references/
        │       └── .gitkeep
        └── voice-update/
            └── SKILL.md
```

The root `voice-*.md` files are editable source copies. The plugin-ready copies
live under `voice-plugin/skills/*/SKILL.md`.

The `voice-create/references/` folder is a placeholder for reusable skill
materials such as schemas, sample-analysis rubrics, or interview prompts. Keep
private writing samples and client transcripts outside the plugin and point the
skill to them from the active workspace.

## Plugin Layout

The plugin follows Claude Code's plugin structure:

- `.claude-plugin/plugin.json` defines the plugin identity.
- `skills/<skill-name>/SKILL.md` contains each skill.
- Installed plugin skills are namespaced as `/voice-plugin:voice-create`,
  `/voice-plugin:voice-audit`, and `/voice-plugin:voice-update`.

References:

- [Create plugins](https://code.claude.com/docs/en/plugins)
- [Extend Claude with skills](https://code.claude.com/docs/en/skills)

## Local Test

From this directory, load the plugin in Claude Code:

```bash
claude --plugin-dir ./voice-plugin
```

Then test the skills:

```text
/voice-plugin:voice-create
/voice-plugin:voice-audit
/voice-plugin:voice-update
```

After editing a plugin file inside an active Claude Code session, run:

```text
/reload-plugins
```

## Skill Workflow

Use the skills as a loop:

1. Run `voice-create` to build the first voice profile.
2. Use the generated voice profile before drafting public writing.
3. Run `voice-audit` against recent work to find drift and weak sections.
4. Run `voice-update` to patch the profile with new evidence.

For active publishers, audit and update every 6-8 weeks. For steadier phases,
audit quarterly.
