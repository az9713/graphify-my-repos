---
repo: two-agent-architecture
description: Two-agent architecture: Admin Agent (compiler) + Help Desk Agent (runtime). LLMs compile workflows once; execution is deterministic.
language: Python
stars: 0
forks: 0
created: 2026-05-21
updated: 2026-05-21
topics: 
is_fork: False
kb: 31
---

# two-agent-architecture
# Two-Agent Architecture

An implementation of the **agent compiler pattern**: split creation authority from execution authority to build enterprise AI automation that is safe, auditable, and governed.

> Inspired by the architecture described in **[The Two-Agent Architecture Behind AI-Native IT](https://www.youtube.com/watch?v=j7ypvRUFY7M&t=16s)** — a talk by Jake Stauch on how to build AI-native enterprise service management platforms using a compiler/runtime agent split.

---

## The Core Idea

> *"Use LLMs to compile workflows. Do not use LLMs as the workflow engine."*

Most enterprise AI demos use a single agent that reasons and acts on every request — every request is a fresh LLM call against the live system. This architecture splits that into two roles:

```
Admin Agent  ──── compiles ────▶  spec.yaml + handler.py  ──── stored in ────▶  Registry
                                                                                     │
                                                                               (human approves)
                                                                                     │
Help Desk Agent  ◀──── loads approved tools ─────────────────────────────────────────┘
      │
      └──── executes handler deterministically ──── logs AuditEvent
```

- **Admin Agent** is the compiler: natural language → executable workflow artifact. Runs **once**. Expensive.
- **Help Desk Agent** is the runtime: resolves requests using only approved tools. Runs **many times**. Cheap and deterministic.
- The two agents never share context — they communicate only through the shared SQLite registry.

---

## Repository Structure

```
two-agent-architecture/
├── agents/
│   ├── admin_agent.py       # Admin Agent: two-pass compiler (duplicate check + codegen)
│   └── helpdesk_agent.py    # Help Desk Agent: constrained runtime
├── core/
│   ├── models.py            # Pydantic: WorkflowSpec, Tool, AuditEvent
│   ├── registry.py          # SQLite: tools + audit_events
│   └── executor.py          # importlib: loads handler.py, calls handler(inputs)
├── workflows/               # Compiled workflow artifacts (one folder per workflow)
│   └── <id>/
│       ├── spec.yaml        # Parameters, permissions, risk level
│       ├── handler.py       # Claude-generated Python function
│       └── evals.jsonl      # Generated test cases
├── seed_data.py             # Seeds 4 pre-approved example tools
├── cli.py                   # Entry point: admin / helpdesk / audit commands
├── requirements.txt
├── .env.example
├── README.md                # This file
└── TESTING.md               # Full test report
```

---

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# Add your ANTHROPIC_API_KEY to .env

python seed_data.py
```

---

## Commands

```bash
python cli.py admin list                    # List all workflows + status
python cli.py admin create "<description>"  # Compiler: NL → workflow artifacts
python cli.py admin approve <workflow_id>   # Human approval gate
python cli.py helpdesk "<request>"          # Help Desk Agent resolves a request
python cli.py helpdesk "<request>" --user <email>
python cli.py audit                         # Show last 20 audit events
```

---

## Quick Start Walkthrough

### 1. Verify the seeded registry

```bash
python cli.py admin list
```

Expected: four pre-approved tools — `password_reset`, `software_access_request`, `vpn_setup`, `employee_onboarding`.

---

### 2. Help Desk Agent — request it CAN handle

```bash
python cli.py helpdesk "I forgot my password and can't log in" --user alice@corp.com
```

What happens:
1. Help Desk Agent loads approved tools from registry
2. Claude selects `password_reset`, extracts `user_email` from context
3. Executor loads `workflows/password_reset/handler.py` via `importlib`, calls `handler(inputs)`
4. Claude formats the result into a human response
5. `AuditEvent` logged

```
Tool executed: password_reset
Result: {'status': 'ok', 'reset_token': 'DF9E5396378B', 'expires_in': '15 minutes', ...}
```

---

### 3. Help Desk Agent — request it CANNOT handle (escalation)

```bash
python cli.py helpdesk "Can you book me a flight to New York?"
```

```
No tool used (escalated or clarification needed)

Response: I don't have an approved workflow for that. I'll escalate this to a human support agent.
```

---

### 4. Admin Agent — compile a new workflow

```bash
python cli.py admin create "page the on-call engineer when a P1 incident is reported"
```

**Pass 1 — Duplicate check:** Claude compares the request against all existing workflows. None overlap → PROCEED.

**Pass 2 — Compilation:** Claude calls the `compile_workflow` tool (structured output enforced via `tool_choice`) and returns:
- `spec` — WorkflowSpec with id, parameters, risk_level, permissions
- `handler_code` — complete Python module: `def handler(inputs: dict) -> dict`
- `evals` — 3–5 test cases

Artifacts written to `workflows/p1_incident_oncall_page/`, registered with `status=pending`.

```
Pass 1: PROCEED: Genuinely new — incident alerting has no overlap with existing workflows.

Compiled: p1_incident_oncall_page (status: pending)

spec.yaml:
  risk_level: high
  parameters: [incident_title, incident_description, reporter_name, reporter_email, affected_service]
  permissions.requires_approval: false
```

---

### 5. Approve and use the compiled workflow

```bash
python cli.py admin approve p1_incident_oncall_page

python cli.py helpdesk "P1 incident: payment service down. Title: Payment Outage. Reporter: Sarah Chen. Affected: payment-gateway." --user ops@corp.com
```

```
Tool executed: p1_incident_oncall_page
Result: {'incident_id': 'INC-P1-06DCE7B8', 'oncall_engineer_paged': 'morgan.kim@company.com', ...}
```

---

### 6. Audit log

```bash
python cli.py audit
```

Every tool execution, escalation, and slot-filling response is logged with agent, action, tool, user, and result status.

---

## The Compiler Is General

The Admin Agent has no hardcoded workflow types. The same compiler pipeline handles any enterprise domain:

| Description | Compiled ID | Risk | Requires Approval |
|---|---|---|---|
| Page on-call engineer for P1 incidents | `p1_incident_oncall_page` | high | no |
| Provision GitHub repo with branch protection | `github_repo_provisioning` | medium | yes |
| Lock account on suspicious login | `lock_user_account_suspicious_activity` | high | no |
| Route expense report for manager approval | `expense_report_approval` | medium | yes |
| Escalate support ticket after 48h SLA breach | `escalate_ticket_to_engineering` | medium | yes |

**Duplicate detection** blocks redundant workflows. Asking for "Salesforce access" when `software_access_request` already exists returns:

```
Duplicate detected: MERGE: recommend merging with software_access_request
because Salesforce is a value for software_name, not a new workflow category.
```

### What the generated handler.py looks like

Every compiled `handler.py` follows the same contract:

```python
def handler(inputs: dict) -> dict:
    # 1. Validate required inputs
    # 2. Simulate the action (stub comments show the real API calls)
    # 3. Return {"status": "ok"|"error", ...result fields}
```

Stub comments mark exactly what a production implementation replaces:

```python
# In production: POST https://api.github.com/orgs/{org}/repos
repo_id = random.randint(100_000_000, 999_999_999)

# In production: PUT /repos/{org}/{repo}/branches/main/protection
protection_rules = {"required_status_checks": {"strict": True, ...}, ...}
```

---

## Key Invariants

| Property | How it's enforced |
|---|---|
| Help Desk Agent bounded to approved tools only | Registry query `WHERE status='approved'` at request time |
| Help Desk Agent cannot create tools | System prompt prohibition + no write access |
| Compilation happens once | `handler.py` written to disk; loaded via `importlib` on each call |
| Every action is auditable | `AuditEvent` written to SQLite after every execution or escalation |
| Duplicate workflows blocked | Pass 1 checks all existing descriptions before compiling |
| Missing required fields caught | Agent asks before calling; handler validates on entry |

---

## Extending to Production

| MVP | Production |
|---|---|
| Stdlib handlers (simulated) | Real API connectors (Okta, Jira, Salesforce, GitHub, PagerDuty, ...) |
| SQLite registry | Postgres |
| `importlib` dynamic import | Sandboxed subprocess / containerized execution |
| CLI approval | Web UI approval inbox |
| Single-turn Help Desk | Multi-turn chat with session state |
| No RBAC | Full RBAC/ABAC from `spec.yaml` permissions block |

---

## Model

Both agents use `claude-sonnet-4-6`.
