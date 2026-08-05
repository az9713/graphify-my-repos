# Claude Code Monitor Tool — Complete Tutorial

A production-quality documentation set for the [Monitor tool](https://docs.anthropic.com/en/docs/claude-code/tools-reference#monitor-tool) in Claude Code. Covers everything from the mental model to copy-pasteable use cases, with parameters verified against the live tool schema during a real test session.

---

## What's inside

13 documentation files across 3 layers:

### Core docs

| File | What it covers |
|------|---------------|
| [What is Monitor?](docs/monitor-tool/what-is-monitor.md) | Mental model, how events flow, comparison with `/loop` and `run_in_background` |
| [Quickstart](docs/monitor-tool/quickstart.md) | First monitor in under 2 minutes, with annotated output |
| [Reference](docs/monitor-tool/reference.md) | All 4 parameters (`description`, `command`, `timeout_ms`, `persistent`), filter patterns, event model, constraints |
| [Troubleshooting](docs/monitor-tool/troubleshooting.md) | 8 common failures with exact fixes |

### Use cases

| File | Pattern | Scenario |
|------|---------|---------|
| [Natural language invocation](docs/monitor-tool/use-cases/natural-language.md) | — | How to actually talk to Claude Code — one-liners, conversations, mid-session corrections |
| [Dev server watcher](docs/monitor-tool/use-cases/dev-server.md) | Stream filter | Watch for runtime errors while coding |
| [Test suite monitor](docs/monitor-tool/use-cases/test-suites.md) | Stream filter | Diagnose failures as each test fails (Jest, pytest, Go, RSpec, Cargo) |
| [File drop processor](docs/monitor-tool/use-cases/file-watcher.md) | Poll & diff | React when new files arrive in a folder |
| [API & price polling](docs/monitor-tool/use-cases/api-polling.md) | Poll & diff | Alert when a value crosses a threshold |
| [Deployment monitor](docs/monitor-tool/use-cases/deployments.md) | Both | Watch error rates after a production push |
| [Multi-service watcher](docs/monitor-tool/use-cases/multi-service.md) | Both | Aggregate events from multiple services |

---

## Key things this tutorial clarifies

Things that aren't obvious from the official docs alone:

**The event split** — the `description` is the only thing the user sees in their notification. The stdout from the command goes to Claude. Users learn what happened through Claude's response, not a raw event.

**`persistent` vs `timeout_ms`** — `persistent: true` removes the timeout cap entirely (runs until `TaskStop` or session end). `timeout_ms` caps at 3,600,000ms (1 hour). Any watch longer than an hour needs `persistent: true`.

**`--line-buffered` is mandatory** — without it, grep holds output in an internal buffer and events arrive late or not at all. Every pipe in a stream filter needs this flag.

**Two filter patterns** — stream filter (`tail -f ... | grep --line-buffered`) for real-time log tailing; poll & diff (`while true; do ... sleep N; done`) for remote APIs and slow-changing values.

---

## Live test session

The docs were written and corrected during a live Claude Code session with an active Monitor watching the `docs/` directory for `.md` file changes. The monitor command used:

```bash
touch docs/.watch_sentinel
while true; do
  CHANGED=$(find docs -name "*.md" -newer docs/.watch_sentinel 2>/dev/null)
  if [ -n "$CHANGED" ]; then
    echo "Modified: $CHANGED"
    touch docs/.watch_sentinel
  fi
  sleep 3
done
```

**What the test revealed:**

- The `description` parameter is the only field surfaced to the user in the notification — the echo output goes to Claude, not the user directly
- The correct parameter name is `timeout_ms` (milliseconds), not `timeout` (seconds) as initially documented
- `persistent: true` means session-lifetime with no timeout cap — it does not mean auto-restart on crash
- The sentinel file approach works correctly on Windows with Git Bash

Every parameter correction in this tutorial was triggered by a live monitor event caught during the session:

| Event | File changed | Correction made |
|-------|-------------|-----------------|
| 1 | `index.md` | User edit |
| 2 | `what-is-monitor.md` | User edit; then event model clarification |
| 3 | `reference.md` | `timeout` → `timeout_ms`, `persistent` semantics, event model table |
| 4 | `use-cases/deployments.md` | Timeout table corrected for 1-hour cap |
| 5 | `quickstart.md` | User/Claude event split added |

---

## Official reference

- [Monitor tool](https://docs.anthropic.com/en/docs/claude-code/tools-reference#monitor-tool)
- [All Claude Code tools](https://docs.anthropic.com/en/docs/claude-code/tools-reference)
- [Permissions](https://docs.anthropic.com/en/docs/claude-code/permissions)
- [Settings](https://docs.anthropic.com/en/docs/claude-code/settings)
- [Scheduled tasks & /loop](https://docs.anthropic.com/en/docs/claude-code/scheduled-tasks)
