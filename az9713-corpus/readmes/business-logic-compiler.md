# BizLogic Compiler

Compiles YAML business rules, SOPs, and constraints into a runnable AI-native operating system spec, then simulates customer tickets against that spec — deterministically or with live LLM agents.

Inspired by the YouTube video ["The Playbook for a $100M AI Agency"](https://www.youtube.com/watch?v=8ktcSaSTvxk&t=5378s).

**Full documentation: [docs/index.md](docs/index.md)**

---

## Quick start

### Deterministic mode (no API keys)

```powershell
python .\compile_business_os.py --input .\input --output .\compiled_os
python .\simulate_tickets.py --compiled .\compiled_os --tickets .\input\sample_tickets.yaml
```

No packages to install. Output: `compiled_os/simulation_results.yaml`.

### LLM mode (Anthropic / OpenAI / OpenRouter)

```powershell
pip install -r requirements_llm.txt
Copy-Item .env.example .env   # add your API key
python .\simulate_tickets_llm.py
```

Output: `compiled_os/simulation_results_llm.yaml`. LLM agents handle ticket classification, policy tie-breaking, and reply QA. Hard constraints remain deterministically enforced.

### Run the tests (no API keys needed)

```powershell
pip install pytest pytest-mock
pytest tests\ -v
```

Output: `191 passed`. All LLM calls are mocked.

---

## How it works

```
input/ (5 YAML/Markdown files)
  └──► compile_business_os.py
          └──► compiled_os/ (10 files including runtime_bundle.json)
                  └──► simulate_tickets[_llm].py
                          └──► simulation_results[_llm].yaml
```

The compiler reads business rules, SOP steps, KPIs, constraints, and a tool catalog, then emits a workflow graph, policy engine, agent specs, tool contracts, memory schema, eval manifest, and rollout plan. The simulator runs tickets through the compiled policy bundle and writes an auditable trace per ticket.

See [docs/overview/what-is-this.md](docs/overview/what-is-this.md) for the full mental model.

---

## The role of the LLM

The LLM is used at **simulation time only** — never during compilation. The compiler is pure data transformation: same inputs always produce the same outputs, with no network calls.

During simulation, the LLM replaces three steps that benefit from language understanding:

| Step | Deterministic fallback | LLM upgrade |
|---|---|---|
| **Ticket classification** | Regex keyword scan for intent, reason, sentiment, and risk flags | `LLMIntakeClassifier` reads the full ticket text and returns structured facts using contextual understanding |
| **Policy tie-breaking** | First matching rule by priority | `LLMPolicyReasoner` picks the best rule when multiple conditions match, weighing customer context and business goal |
| **Reply QA** | Not present | `LLMQAAgent` checks the draft customer reply for tone, liability admissions, policy citation, and invented promises |

**Hard constraints are always deterministic.** The numeric limits — maximum AI-approved refund ($200), maximum discount (20%), risk-flag escalation — are enforced by the rule engine after the LLM QA step. A passing LLM QA result cannot override them.

**Fallback on error.** If any LLM call fails, that step falls back to the deterministic logic, emits a warning, and adds a `llm_fallback` field to the trace. The simulation continues rather than stopping.

---

## MVP boundary

This is not a full agent platform. It does not call Shopify, Zendesk, or Stripe. It proves the compiler shape:

```
business rules + SOP + KPIs + constraints + tool catalog
    → workflow graph + policy engine + agents + tools + evals + memory + rollout plan
    → runnable simulation traces
```

Good next extensions: schema validation, a visual workflow viewer, a richer condition language, historical-ticket import, and shadow-mode evaluation against real human decisions.

---

## Tests

191 pytest tests across 8 files. No API keys required — all LLM calls are mocked with `pytest-mock`.

| File | Focus |
|---|---|
| `test_artifact_parser.py` | Parser, SOP step extraction, I/O round-trip |
| `test_workflow_compiler.py` | Workflow graph generation, node ID slugging |
| `test_policy_compiler.py` | Rule priority, agent registry, tool contracts |
| `test_eval_compiler.py` | Test case generation, outcome derivation |
| `test_simulator.py` | All simulator methods + 5-ticket regression |
| `test_llm_client.py` | Provider detection, JSON extraction, mocked API calls |
| `test_llm_agents.py` | Vocabulary enforcement, fallback validation |
| `test_llm_simulator.py` | LLM overrides + fallback paths |
| `test_integration.py` | End-to-end compile + simulate with real input files |

See [docs/reference/testing.md](docs/reference/testing.md) for the full coverage map and what's not tested.
