---
repo: cliproxyapi-console
description: A polished local console, launcher, and development guide for routing Claude Code through CLIProxyAPI.
language: HTML
stars: 0
forks: 0
created: 2026-07-27
updated: 2026-07-27
topics: 
is_fork: False
kb: 3621
---

# cliproxyapi-console
# CLIProxyAPI Console

A small, public companion for routing **Claude Code** through a local [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI) instance and into an OpenAI/Codex-backed model route.

This repository contains the parts that are useful to share:

- a safe launcher that starts the local proxy when needed;
- a minimal example configuration;
- an offline architecture dashboard;
- a reproducible smoke-test checklist;
- the complete development journey from upstream install to working Claude Code session.

It does **not** fork or redistribute CLIProxyAPI. It does not contain the upstream binary, OAuth files, provider credentials, logs, or a live monitoring service.

> [!IMPORTANT]
> CLIProxyAPI and provider subscriptions are separate projects and services. Review their current documentation and terms before routing traffic. Model names in this repository are an example local mapping, not a promise that a provider will offer those identifiers.

## Showcase

### Offline route dashboard

The dashboard is one self-contained HTML file. It has inline CSS and JavaScript, a pure SVG architecture diagram, model-route cards, and an interactive launch timeline. It makes no live proxy requests.

[![CLIProxyAPI Console dashboard](screenshots/dashboard.png)](dashboard.html)

_Click the image to open `dashboard.html` in the repository. Download or clone the repository and open the file locally for the full interactive version._

### Upstream management center

CLIProxyAPI serves its official management interface from the local proxy. The screenshot below shows the neutral login page; no account or credential data is included.

[![CLIProxyAPI Management Center login](screenshots/management.png)](http://127.0.0.1:8317/management.html)

_Click the image after starting CLIProxyAPI, or read the official [Web UI guide](https://help.router-for.me/management/webui)._

## Architecture

```text
Claude Code
    │  Anthropic-compatible request
    │  local client token
    ▼
CLIProxyAPI on 127.0.0.1:8317
    │  translate request format
    │  select an authenticated provider account
    │  apply round-robin/retry policy
    ▼
OpenAI / Codex route
    │  provider response
    ▼
CLIProxyAPI translates the response back
    │
    ▼
Claude Code
```

Claude Code continues to use its normal client protocol. `ccx.sh` changes the base URL to the local proxy and supplies model aliases. CLIProxyAPI handles protocol translation and provider authentication, then returns a response Claude Code understands.

Two secrets have different jobs:

| Secret | Used by | Purpose |
|---|---|---|
| Local client token | Claude Code → CLIProxyAPI | Allows local API requests. It appears in both `config.yaml` and `.env`. |
| Management key | Browser/management API → CLIProxyAPI | Protects configuration, OAuth, auth-file, log, and provider-management operations. |

Use different random values for them. Both stay local and untracked.

## Repository contents

```text
.
├── README.md
├── ccx.sh                 # Claude Code launcher and proxy supervisor
├── config.example.yaml    # safe template; copy to ignored config.yaml
├── .env.example           # safe template; copy to ignored .env
├── .gitattributes         # keeps the Bash launcher on LF line endings
├── dashboard.html         # static, offline product-style route map
└── screenshots/
    ├── dashboard.png
    └── management.png
```

Runtime files are deliberately absent:

```text
config.yaml    config.docker.yaml    .env    auths/    logs/    static/    cli-proxy-api(.exe)
```

## Prerequisites

1. [Claude Code](https://docs.anthropic.com/en/docs/claude-code/overview).
2. [CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI), installed separately.
3. A provider login or API credential supported by CLIProxyAPI.
4. `curl`.
5. Bash. On Windows, use Git Bash for `ccx.sh`.

## 1. Install CLIProxyAPI

Use the official [Quick Start](https://help.router-for.me/introduction/quick-start) for the latest commands and release notes.

### Windows

1. Download the current Windows archive from [CLIProxyAPI Releases](https://github.com/router-for-me/CLIProxyAPI/releases).
2. Extract `cli-proxy-api.exe`.
3. Either place it in this repository beside `ccx.sh`, or set its absolute path as `CLIPROXYAPI_BIN` in `.env`.

### macOS with Homebrew

```bash
brew install cliproxyapi
brew services start cliproxyapi
```

Homebrew normally uses:

- Apple Silicon: `/opt/homebrew/etc/cliproxyapi.conf`
- Intel: `/usr/local/etc/cliproxyapi.conf`

If the service is already listening on `127.0.0.1:8317`, `ccx.sh` uses it and does not need a local binary.

### Linux

Download a versioned Linux release from [CLIProxyAPI Releases](https://github.com/router-for-me/CLIProxyAPI/releases), or use a package documented in the official [Quick Start](https://help.router-for.me/introduction/quick-start). Avoid piping an unpinned remote installer directly into a shell; download and inspect installation scripts before running them.

Arch Linux packages are also available:

```bash
yay -S cli-proxy-api-bin
systemctl --user enable --now cli-proxy-api
```

### Docker

A container must listen on its network interface, not only its own loopback address. Create an ignored Docker-specific copy and change its `host` value:

```bash
cp config.example.yaml config.docker.yaml
# Edit config.docker.yaml:
#   host: "0.0.0.0"
#   auth-dir: "/root/.cli-proxy-api"
```

Publish the container port only to the host loopback interface:

```bash
docker run --rm -p 127.0.0.1:8317:8317 \
  -v "$PWD/config.docker.yaml:/CLIProxyAPI/config.yaml" \
  -v "$PWD/auths:/root/.cli-proxy-api" \
  eceasy/cli-proxy-api:latest
```

The `0.0.0.0` bind is inside the container. The `127.0.0.1:8317:8317` publish rule keeps host access local. When Docker is serving that port, the launcher verifies the CLIProxyAPI root response and reuses it.

### Build upstream from source

CLIProxyAPI currently requires Go 1.26 or newer.

```bash
git clone https://github.com/router-for-me/CLIProxyAPI.git
cd CLIProxyAPI
go build -o cli-proxy-api ./cmd/server
```

On Windows:

```powershell
git clone https://github.com/router-for-me/CLIProxyAPI.git
Set-Location CLIProxyAPI
go build -o cli-proxy-api.exe ./cmd/server
```

Copy the built executable beside `ccx.sh`, or reference it with `CLIPROXYAPI_BIN`.

## 2. Clone this companion

```bash
gh repo clone az9713/cliproxyapi-console
cd cliproxyapi-console
```

Plain Git works too:

```bash
git clone https://github.com/az9713/cliproxyapi-console.git
cd cliproxyapi-console
```

## 3. Create local configuration

Copy the safe templates:

```bash
cp config.example.yaml config.yaml
cp .env.example .env
```

Generate two separate long random values. Python's standard library works on Windows, macOS, and Linux:

```bash
python -c "import secrets; print(secrets.token_urlsafe(48))"
python -c "import secrets; print(secrets.token_urlsafe(48))"
```

Use the first value for `remote-management.secret-key` in `config.yaml`.

Use the second value in both places below:

```yaml
# config.yaml
api-keys:
  - "YOUR_LOCAL_CLIENT_TOKEN"
```

```dotenv
# .env
CLIPROXYAPI_CLIENT_TOKEN=YOUR_LOCAL_CLIENT_TOKEN
```

If the upstream binary is installed elsewhere and the proxy is not managed as a service, add its absolute path:

```dotenv
CLIPROXYAPI_BIN=C:/tools/cliproxyapi/cli-proxy-api.exe
```

The public templates bind the server to `127.0.0.1`, leave remote management disabled, store OAuth files under ignored `auths/`, use round-robin routing, and retry eligible failures up to three times.

> [!NOTE]
> CLIProxyAPI can load environment variables, but the YAML `api-keys` list is still configuration. Keep the same local client token in the ignored `config.yaml` and `.env` files.

See the official [Basic Configuration](https://help.router-for.me/configuration/basic) reference for every available setting.

## 4. Connect a provider account

Start the proxy first:

```bash
# Windows Git Bash
./cli-proxy-api.exe --config ./config.yaml

# Linux/macOS local binary
./cli-proxy-api --config ./config.yaml
```

Then open:

```text
http://127.0.0.1:8317/management.html
```

Log in with the management key from `config.yaml`.

### Codex OAuth through the management UI

1. Open the management center.
2. Choose the Codex OAuth provider.
3. Start the Codex authorization flow.
4. Complete the provider login in the browser.
5. Return to **Auth Files** and confirm that the Codex credential appears.

The equivalent upstream command is:

```bash
./cli-proxy-api --codex-login
```

Use `--no-browser` when the server should print the authorization URL instead:

```bash
./cli-proxy-api --codex-login --no-browser
```

The documented local Codex OAuth callback uses port `1455`. Read the official [Codex provider guide](https://help.router-for.me/configuration/provider/codex) and [Codex client guide](https://help.router-for.me/agent-client/codex) if the flow changes.

CLIProxyAPI also supports other provider login modes. For example, upstream documents:

```bash
./cli-proxy-api --claude-login
```

The Claude OAuth callback normally uses port `54545`. See the official [Claude Code OAuth guide](https://help.router-for.me/configuration/provider/claude-code).

## 5. Start the app

There are three useful entry points.

### A. Start only the proxy

```bash
# Windows Git Bash
./cli-proxy-api.exe --config ./config.yaml

# Linux/macOS
./cli-proxy-api --config ./config.yaml
```

The API and management UI are then available at:

```text
http://127.0.0.1:8317
http://127.0.0.1:8317/management.html
```

### B. Open the offline dashboard

Double-click `dashboard.html`, or run a small local static server:

```bash
python -m http.server 8080
```

Then open:

```text
http://127.0.0.1:8080/dashboard.html
```

The dashboard is explanatory. Its timeline does not execute system commands or inspect live proxy state.

### C. Launch Claude Code through the complete route

```bash
./ccx.sh
```

Any Claude Code arguments are passed through unchanged:

```bash
./ccx.sh --model fable
./ccx.sh --continue
./ccx.sh path/to/project
```

If CLIProxyAPI is already running—through Homebrew, systemd, Docker, or another terminal—the launcher reuses it. Otherwise, it starts the configured local executable and waits up to ten seconds.

## What `ccx.sh` automates

The launcher is intentionally small:

1. Resolve the repository directory, so it works from any current folder.
2. Load the ignored `.env` when present.
3. Require the local client token.
4. Verify that `curl` and Claude Code are available.
5. Probe `http://127.0.0.1:8317/` with a two-second timeout and require the CLIProxyAPI marker `"message":"CLI Proxy API Server"`.
6. Refuse to send the local token if another HTTP service owns port `8317`.
7. If the proxy is down, find `cli-proxy-api.exe`, `cli-proxy-api`, or `CLIPROXYAPI_BIN`.
8. Start the proxy with the ignored `config.yaml`.
9. Poll twenty times at half-second intervals and validate the same server marker.
10. Stop with a clear error if the proxy is still unavailable.
11. Export the local base URL, token, and model aliases.
12. Replace the shell with `claude "$@"`, preserving signals and exit status.

Runtime output goes to ignored `logs/proxy.log`.

### Expected failure messages

| Failure | Fix |
|---|---|
| `CLIPROXYAPI_CLIENT_TOKEN` is missing | Copy `.env.example` to `.env` and set the same token as `config.yaml`. |
| Port `8317` answers but is not CLIProxyAPI | Stop the other service or move one application to a different port. |
| Proxy is down and no binary is found | Place the binary beside `ccx.sh` or set `CLIPROXYAPI_BIN`. |
| `config.yaml` is missing | Copy and edit `config.example.yaml`. |
| Proxy does not become ready in ten seconds | Read `logs/proxy.log`; check port conflicts and YAML syntax. |
| OAuth is absent or expired | Reconnect the provider in the management center. |
| A mapped model is unavailable | Change the alias in `ccx.sh` to one exposed by your provider route. |

## Example model map

| Claude Code tier | Routed identifier |
|---|---|
| Opus | `gpt-5.6-terra` |
| Sonnet | `gpt-5.6-terra` |
| Haiku | `gpt-5.6-luna` |
| Fable | `gpt-5.6-sol` |
| Subagents | `gpt-5.6-terra` |

These are environment-variable aliases in `ccx.sh`. They are not built-in CLIProxyAPI defaults. Edit them to match the models available through your own OAuth account, API key, or compatible upstream.

## Smoke-test checklist

### 1. Check shell syntax

```bash
bash -n ccx.sh
```

No output means the script parsed successfully.

### 2. Check proxy health

```bash
curl -s http://127.0.0.1:8317/
```

The root JSON should include:

```json
{"message":"CLI Proxy API Server"}
```

The launcher checks this marker before exporting the token to Claude Code. If a different service owns port `8317`, it stops instead of treating any HTTP response as trusted.

### 3. Check management protection

Open `http://127.0.0.1:8317/management.html` in a private browser window. The page should request the management key rather than expose configuration.

The Management API lives under `/v0/management` and requires the management key even from localhost. See the official [Management API reference](https://help.router-for.me/management/api).

### 4. Check OAuth state

After login, open **Auth Files** and confirm the intended provider credential exists and is enabled. Do not paste or screenshot the underlying token JSON.

### 5. Launch the routed client

```bash
./ccx.sh
```

### 6. Verify the mapped identity

Inside the routed Claude Code session, use the short showcase prompt at the end of this README. With this example Fable mapping, the expected routed identifier is `gpt-5.6-sol`, built by OpenAI.

That result demonstrates the configured route. It is not a universal CLIProxyAPI default and should not be treated as independent cryptographic attestation of the upstream service.

## Security boundary

This repository is public because all operational state stays outside Git:

- `host` is `127.0.0.1`.
- `remote-management.allow-remote` is `false`.
- The client token and management key are separate.
- `.env` and `config.yaml` are ignored.
- OAuth files under `auths/` are ignored.
- logs, downloaded management assets, and binaries are ignored.
- `dashboard.html` contains no token and performs no network requests.
- screenshots use a neutral, unauthenticated management view.

The management key is privileged. It protects configuration, auth files, OAuth sessions, logs, provider keys, plugins, and credentialed management operations. Do not expose the management interface to a network unless you understand and secure that boundary.

The Web UI can remember its key in browser storage. Upstream warns that this storage is reversibly obfuscated rather than cryptographically protected. Use a trusted local browser profile, avoid untrusted same-origin plugins, and leave **Remember password** off when taking screenshots or using a shared machine.

If a secret is ever committed, revoke or rotate it first. Removing it from Git history does not make the old value safe again.

## Development journey

### Stage 1: begin with upstream, not a rewrite

The project starts with [router-for-me/CLIProxyAPI](https://github.com/router-for-me/CLIProxyAPI), an MIT-licensed Go proxy that already provides the hard parts:

- Claude-, OpenAI-, Gemini-, Codex-, and Grok-compatible interfaces;
- protocol translation;
- streaming and tool calls;
- OAuth login flows;
- multiple credential files;
- round-robin account selection;
- retries and cooldown behavior;
- a management API and browser UI.

Rebuilding that server would add risk and maintenance without improving this use case. The companion therefore treats upstream as an installed dependency.

### Stage 2: make the local security boundary explicit

A small project-specific `config.yaml` narrows the listener to `127.0.0.1:8317`, disables remote management, stores OAuth material in a project-local `auths/` directory, and separates the browser management key from the API token Claude Code sends.

The real file stays private. Only `config.example.yaml` is published.

### Stage 3: remove the repetitive startup steps

The first manual workflow was:

1. start CLIProxyAPI;
2. wait for port `8317`;
3. set Claude Code environment variables;
4. map each Claude tier to the desired provider model;
5. launch Claude Code;
6. remember to inspect logs when startup fails.

`ccx.sh` turns that sequence into one command. It does not become a service manager or configuration framework. If the proxy is already running, it gets out of the way. If not, it performs the minimum bounded startup sequence.

### Stage 4: visualize the translation layer

The proxy is easier to understand as a flow than as environment variables. `dashboard.html` was built as a single offline document:

- no package manager;
- no external fonts or JavaScript;
- no build step;
- no framework;
- pure SVG for the architecture;
- CSS cards for model mappings;
- small JavaScript interactions for the smoke-test timeline.

It explains the system but intentionally does not call the Management API. That keeps the dashboard publishable and prevents browser storage from becoming another credential surface.

### Stage 5: turn local work into a safe public companion

The working directory also contains everything that must never be published: OAuth refresh tokens, management credentials, client tokens, logs, a downloaded binary, generated management assets, and local research notes.

Instead of initializing Git there, this repository was created separately. The launcher was recreated without its embedded token. The dashboard was scrubbed of secret-derived fragments. The management screenshot came from an isolated unauthenticated browser context. Only the documented companion artifacts were staged.

This separation is the most important engineering decision in the repository: **publish the recipe, not the runtime state**.

## Official references

- [CLIProxyAPI repository](https://github.com/router-for-me/CLIProxyAPI)
- [Quick Start](https://help.router-for.me/introduction/quick-start)
- [Basic Configuration](https://help.router-for.me/configuration/basic)
- [Management Web UI](https://help.router-for.me/management/webui)
- [Management API](https://help.router-for.me/management/api)
- [Codex provider OAuth](https://help.router-for.me/configuration/provider/codex)
- [Codex client setup](https://help.router-for.me/agent-client/codex)
- [Claude Code OAuth](https://help.router-for.me/configuration/provider/claude-code)

CLIProxyAPI is MIT licensed by its upstream authors. This companion links to and operates alongside upstream; it does not redistribute upstream source or binaries.

## Final showcase prompts

### 1. Build the visual explanation

```text
Build a single self-contained dashboard.html (no external libraries, inline CSS/JS) that
visualizes this project: parse config.yaml and ccx.sh from this folder, then render a polished
dark-theme dashboard explaining how this proxy setup works — an architecture flow diagram in
pure SVG (Claude Code → localhost:8317 → OpenAI), a card for each configured model tier, and the
smoke-test checklist as an interactive timeline. Make it look like a product landing page, not
a dev tool. Then open it and screenshot it to verify your own work.
```

For a public repository, parse only sanitized example files or remove all credential-derived values before publishing the HTML or screenshot.

### 2. Verify the routed model identity

```text
Don't use any skills. What AI model is this and who built it?
```

With the example Fable route in `ccx.sh`, the expected answer is:

```text
GPT-5.6 Sol, built by OpenAI.
```

Again, that answer reflects this local alias and provider route. Change the expected result when you change the mapping.
