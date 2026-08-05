# Claude Code binary inspect: a discovery workflow

This repository documents a hands-on learning process for inspecting the Claude
Code executable, extracting its embedded JavaScript, and understanding how
binary inspection, prompt extraction, feature-flag research, and local patching
workflows relate to each other.

The exploration was inspired by two public references:

- Reddit discussion: [Claude Code v2.1.150 now allows Anthropic to perform remote system prompt injection](https://www.reddit.com/r/ClaudeCode/comments/1tmizuy/claude_code_v21150_now_allows_anthropic_to/)
- Piebald AI prompt corpus: [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)

This is an educational reverse-engineering and inspection workflow. It does not
publish extracted Claude Code source or bundled prompt corpora. The focus is on
how to reproduce the investigation locally, how to think about the moving
parts, and how to avoid confusing binary string search, JavaScript extraction,
prompt extraction, endpoint and feature-flag inspection, and binary patching.

## Why this exists

Claude Code is normally launched with a simple command:

```powershell
claude
```

Behind that command is a packaged application. The platform-specific native
package, such as `@anthropic-ai/claude-code-linux-x64`, contains a large
executable named `claude`. Tools such as `tweakcc` can extract embedded,
minified JavaScript from that executable. Once extracted, the JavaScript can be
searched for endpoints, feature flags, environment variables, and prompt-like
strings.

That gives technical readers a practical way to answer questions like:

- What strings are present in a given Claude Code version?
- Where do specific feature flags or endpoints appear?
- What does "patching the Claude Code executable" mean in practice?
- How do prompt corpora like Piebald's relate to the compiled package?
- What is the difference between inspecting, extracting, and patching?

## Repository contents

```text
README.md
CLAUDE_CODE_BINARY_INSPECTION_WORKFLOW.md
USEFUL_INFO_FROM_EXTRACTED_CLAUDE_JS.md
artifacts/
  prompts-generated-2.1.150.json
bucket-reports/
  README.md
  01-startup-and-network-behavior.md
  ...
scripts/
  extract-claude-code-js.ps1
  generate-bucket-reports.cjs
  scan-claude-code-js.ps1
```

`CLAUDE_CODE_BINARY_INSPECTION_WORKFLOW.md` is the detailed onboarding guide. It
assumes technical competence but no prior domain knowledge about Claude Code
binaries, Bun-packed executables, `tweakcc`, prompt fragments, or the Piebald
workflow.

The `scripts/` directory contains the reproducible PowerShell workflow used
during the investigation.

`bucket-reports/` contains one current-version markdown report per inspection
bucket. Each report is generated from the current Claude Code native binary
package and includes the resolved Claude binary version.

Large generated files are intentionally ignored:

- downloaded npm tarballs
- unpacked native packages
- extracted JavaScript files
- local clones of reference repositories

The generated prompt JSON for the documented `2.1.150` run is checked in as a
small, inspectable artifact:

```text
artifacts/prompts-generated-2.1.150.json
```

## Quick start

Install or verify the basic tools:

```powershell
node --version
npm --version
tar --version
```

Extract the embedded JavaScript from a downloaded Claude Code native package:

```powershell
.\scripts\extract-claude-code-js.ps1 -Version 2.1.150 -OutDir .\artifacts
```

Or use the current npm release:

```powershell
.\scripts\extract-claude-code-js.ps1 -Version latest -OutDir .\artifacts
```

Scan the extracted JavaScript for the indicators discussed in the Reddit post:

```powershell
.\scripts\scan-claude-code-js.ps1 -JsPath .\artifacts\claude-code-2.1.150.js
```

The scan script looks for markers such as:

- `function nAA`
- `function n0A`
- `tengu_heron_brook`
- `Rv("heron_brook", ...`
- `/api/claude_cli/bootstrap`
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`
- `DISABLE_GROWTHBOOK`
- `GrowthBook`

Minified function names are version-specific. Prefer stable anchors such as
endpoint paths, environment variable names, and feature flag keys when
investigating a different release.

## What the extraction script does

`scripts/extract-claude-code-js.ps1`:

1. Resolves a Claude Code package version through npm.
2. Downloads `@anthropic-ai/claude-code-linux-x64` with `npm pack`.
3. Unpacks the `.tgz` package locally.
4. Finds the native `package/claude` executable.
5. Runs `npx tweakcc unpack` against that downloaded executable.
6. Writes extracted JavaScript to `artifacts/claude-code-<version>.js`.

The script passes the downloaded binary path explicitly to `tweakcc unpack`, so
it inspects a package copy rather than modifying your installed Claude Code.

## What the scan script does

`scripts/scan-claude-code-js.ps1`:

1. Reads an extracted JavaScript file.
2. Searches for a fixed list of markers from the Reddit discussion.
3. Prints the byte position and a small context snippet for each match.

It is not a parser or proof of runtime behavior. It is a fast confirmation tool
for finding whether specific strings and minified function names exist in the
extracted code.

## How this relates to Piebald's system prompt repository

The public Piebald prompt repository publishes readable markdown prompt
fragments and token counts. Its public `tools/updatePrompts.js` script consumes
structured prompt JSON and turns it into markdown files.

The lower-level extraction primitive is in `Piebald-AI/tweakcc`, specifically
`tools/promptExtractor.js`. That script parses extracted JavaScript and emits
prompt records with fields such as:

```json
{
  "name": "Agent Prompt: Example",
  "description": "Prompt description",
  "pieces": ["text before ${", "} text after"],
  "identifiers": [0],
  "identifierMap": {
    "0": "VARIABLE_NAME"
  },
  "version": "2.1.150"
}
```

Conceptually, the workflow is:

```text
npm registry
  -> platform package tarball
    -> native Claude Code executable
      -> embedded minified JavaScript
        -> extracted prompt JSON
          -> readable markdown prompt files
```

This repository focuses on the broader binary-inspection learning path through
the first four stages. System prompt extraction is one follow-up use case. The
detailed guide explains how to run the raw prompt extractor after extracting
the JavaScript.

## Inspecting vs extracting vs patching

These are different activities:

- Inspecting: search a downloaded package or extracted JavaScript without
  changing anything.
- Extracting: convert embedded JavaScript or prompt-like strings into separate
  files for analysis.
- Patching: modify a local Claude Code installation.

The safest learning path is inspection first:

```text
download package copy
extract JavaScript
search JavaScript
extract prompt JSON
compare public prompt corpus
only then consider local patching
```

If you do patch a local installation, understand exactly which file is being
modified and how to restore it. `tweakcc --apply` is the intended prompt
customization path; `adhoc-patch`, manual unpack/edit/repack workflows, and
direct string replacement are more direct and riskier.

## Notes from the v2.1.150 exploration

For Claude Code `2.1.150`, local extraction and scanning confirmed that the
extracted JavaScript contained the markers discussed in the Reddit post,
including:

- `/api/claude_cli/bootstrap`
- `tengu_heron_brook`
- `Rv("heron_brook", ...`
- `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC`
- `DISABLE_GROWTHBOOK`

Finding code paths and strings confirms that the extracted code contains those
mechanisms. It does not, by itself, prove every runtime behavior in every
configuration. Runtime behavior depends on authentication state, provider mode,
environment variables, settings, startup path, and network availability.

## Bucket reports

The current generated bucket reports are in:

- [Claude Code binary inspection bucket reports](./bucket-reports/README.md)

Each bucket report is stamped with the Claude binary version used for
extraction.

## Safety and policy

Use this workflow for legitimate inspection, compatibility research, auditing,
and personal learning.

Do not use it to bypass organizational controls, hide behavior from users or
administrators, redistribute patched proprietary binaries, or run untrusted
patch scripts against developer tools with filesystem and shell access.

This project is not affiliated with Anthropic or Piebald AI.

## Further reading

Start with the detailed guide:

- [Claude Code binary inspection onboarding](./CLAUDE_CODE_BINARY_INSPECTION_WORKFLOW.md)

Then compare with the public inspiration sources:

- [Reddit discussion](https://www.reddit.com/r/ClaudeCode/comments/1tmizuy/claude_code_v21150_now_allows_anthropic_to/)
- [Piebald-AI/claude-code-system-prompts](https://github.com/Piebald-AI/claude-code-system-prompts)
- [Piebald-AI/tweakcc](https://github.com/Piebald-AI/tweakcc)
