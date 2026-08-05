# Early Market Signal Discovery Workflow OS

> Inspired by the a16z Speedrun article [Early-stage markets rarely look like markets](https://speedrun.substack.com/p/early-stage-markets-rarely-look-like-markets) — finding startup opportunities before a category name exists.

This folder turns the early-market-signal playbook into a lightweight research operating system. Use it to notice small groups changing behavior before analysts, incumbents, or investors have a clean market category for the behavior.

The doctrine is simple: behavior before category, intensity before scale, demand before hype.

## Installation

**Prerequisites:** [Claude Code](https://claude.ai/code) installed and running.

### 1. Clone the repo

```bash
git clone https://github.com/az9713/early-market-signal.git
cd early-market-signal
```

### 2. Install the skills

The `skills/` folder contains seven Claude Code skills that power the workflow. Copy them to your Claude skills directory so they are available in every session.

**Mac / Linux:**
```bash
cp -r skills/ems-* ~/.claude/skills/
```

**Windows (PowerShell):**
```powershell
Copy-Item -Recurse skills\ems-* $env:USERPROFILE\.claude\skills\
```

### 3. Verify

Start a Claude Code session in the cloned directory and type:

```
What ems skills are available?
```

Claude should list all seven skills. If it does not, check that the `~/.claude/skills/` directory contains the `ems-*` folders.

### 4. Start your first scan

Open Claude Code in the cloned directory — the workflow files (`source_map.csv`, `weirdness_ledger.md`, `signal_scorecard.csv`) are your live data layer. Then describe a behavioral frontier:

```
Scan for evidence around people who are maintaining handwritten memory
files around AI coding agents because the agents keep losing context.
```

See `USER_GUIDE.md` for a full first-run walkthrough.

---

## What This Is For

Use this workflow when you want to find startup ideas, investment theses, or product wedges from real user behavior.

You are not looking for:

- Polished market maps
- Viral product launches
- Big TAM claims
- Generic AI trend commentary
- Products that look good but have passive users

You are looking for:

- Repeated complaints in overlooked communities
- Users hacking together ugly workflows
- People tolerating rough tools because the outcome matters
- Unpaid tutorials, explainers, scripts, forks, templates, or plugins
- A tool or behavior replacing an existing process
- New vocabulary forming before a category stabilizes

## Folder Contents

| File | Purpose |
| --- | --- |
| `USER_GUIDE.md` | Friendly first-run walkthrough using a concrete emerging-topic example. |
| `source_map.csv` | Tracks communities, URLs, pains, workarounds, evidence, replacement targets, and maturity. |
| `weirdness_ledger.md` | Captures strange behaviors that may point to unnamed markets. |
| `signal_scorecard.csv` | Scores demand quality with a 0-16 rubric. |
| `power_user_interview_script.md` | Guides interviews toward concrete behavior instead of opinions. |
| `early_market_thesis_template.md` | Converts repeated signal clusters into startup theses. |
| `community_tracking_targets.md` | Lists communities to monitor, grouped by signal type. |
| `search_queries.md` | Reusable searches for GitHub, Reddit, forums, HN, Google, and YouTube. |
| `examples.md` | Filled-in examples using agentic workflow infrastructure as the first hunting ground. |

If this is your first time using the system, start with `USER_GUIDE.md`. It walks through a concrete example step by step and shows what to write into each file.

## Claude Code Skills

The workflow is implemented as seven Claude Code skills stored in `~/.claude/skills/`. In a Claude Code session, these trigger automatically from plain English — no prompts to copy and paste.

| Skill | When It Triggers | What It Does |
| --- | --- | --- |
| `ems-scan` | You name a behavioral frontier | Scans communities and web sources, updates `source_map.csv` and `weirdness_ledger.md` |
| `ems-score` | You ask how strong a signal is | Applies the 0–16 rubric to a signal, updates `signal_scorecard.csv` |
| `ems-cluster` | You want to review accumulated signals | Groups pains by community, triages noise vs candidates, kills weak signals |
| `ems-interview` | A signal scores 9+ | Drafts 5 outreach messages and a 10-question interview plan |
| `ems-thesis` | A cluster has 3+ independent sources | Creates a `thesis-[name].md` file from the template |
| `ems-decide` | Signals are accumulating without decisions | Assigns ignore / watch / interview / concierge to every open signal |
| `ems-concierge` | Interviews confirm urgency | Drafts a specific, priced, time-bound manual offer to test willingness to pay |

### Full Loop

```
ems-scan → ems-score → ems-cluster → ems-decide → ems-interview → ems-thesis → ems-concierge
```

Steps 1–4 repeat as new scans add evidence. Steps 5–7 activate when a signal earns them.

### Example Invocations

| Invocation | Skill | Output |
| --- | --- | --- |
| "Scan for evidence around people maintaining memory files around AI coding agents" | `ems-scan` | [`source_map.csv`](source_map.csv), [`weirdness_ledger.md`](weirdness_ledger.md) |
| "How strong is the agent-memory signal?" | `ems-score` | [`signal_scorecard.csv`](signal_scorecard.csv) |
| "Are there patterns across the ledger?" | `ems-cluster` | [`signal_scorecard.csv`](signal_scorecard.csv) (next_action fields updated) |
| "What should I do next with each signal?" | `ems-decide` | [`signal_scorecard.csv`](signal_scorecard.csv) (next_action fields updated) |
| "Prepare interviews for the last-mile app signal" | `ems-interview` | [`interview_plan_S002_S003_builders.md`](interview_plan_S002_S003_builders.md) |
| "Turn the agent-memory cluster into a thesis" | `ems-thesis` | [`thesis-developer-maintained-agent-memory.md`](thesis-developer-maintained-agent-memory.md) |
| "Interviews on the last-mile app signal showed urgency — write me an offer" | `ems-concierge` | [`concierge_offer_agent_memory.md`](concierge_offer_agent_memory.md) |

See `SKILLS_GUIDE.md` for the full conversion reference and more workflow examples.

## The Workflow

### 1. Choose a Behavioral Frontier

Start with a behavior, not a market category.

Weak framing:

```text
I want to study the AI agent market.
```

Better framing:

```text
I want to find people who are restructuring real work around AI agents despite poor reliability, memory, tooling, or deployment support.
```

A useful behavioral frontier should sound awkward. If it sounds like a clean analyst category, you are probably late.

Examples:

| Market Category | Behavioral Frontier |
| --- | --- |
| AI agents | People delegating multi-step work to unstable systems. |
| AI coding | Non-programmers building software by supervising agents. |
| Local AI | Users keeping sensitive workflows offline despite painful setup. |
| AI design | Founders generating product UI without designers, then fighting quality drift. |
| AI deployment | People whose AI-generated apps work locally but fail at auth, payments, hosting, or iteration. |
| Agent observability | Users trying to understand what agents did, why they failed, and how to recover. |

### 2. Scan Communities

Open `community_tracking_targets.md` and pick 5-10 places to scan. Use `search_queries.md` to find pain-heavy discussions.

Look for:

- Complaints
- Repeated questions
- Workarounds
- Scripts
- Forks
- Templates
- Tutorials
- Requests for integrations or APIs
- Users comparing the behavior to an old tool or process
- People saying they cannot go back to the old way

Do not overvalue likes, launch traffic, or influencer attention. Those are attention signals. The workflow is trying to find demand signals.

### 3. Add Sources To `source_map.csv`

When a community, thread, repo, or forum looks useful, add it to `source_map.csv`.

Capture:

- Community
- URL
- Topic cluster
- Repeated pain
- Workaround
- Evidence quote or link
- Tool or process being replaced
- User sophistication
- Monetization hint
- Category maturity
- Notes

Use exact evidence. A vague note like "people are annoyed" is not enough. A useful row says what people are trying to do, what fails, and what they do instead.

### 4. Log Weird Behavior In `weirdness_ledger.md`

Every time you see behavior that seems too intense for the current product quality or category maturity, add an entry.

Each entry should answer:

- What behavior did you observe?
- Why is it weird?
- What pain is behind it?
- What workaround exists?
- What is the evidence?
- What product wedge might this imply?
- How confident are you?
- What should happen next?

This ledger is the raw material. Do not try to force every entry into a startup idea immediately.

### 5. Score Signals In `signal_scorecard.csv`

Score each serious signal from 0 to 16.

Each criterion gets:

- `0`: absent
- `1`: weak or occasional
- `2`: repeated and strong

Criteria:

- Users tolerate rough UX
- Users create tutorials or explainers
- Users replace an incumbent tool or process
- Users ask for APIs or integrations
- Users hack new use cases
- Vocabulary is forming
- Copycats are appearing
- Outside curiosity is growing

Interpretation:

| Total Score | Meaning |
| ---: | --- |
| 0-4 | Probably noise |
| 5-8 | Watchlist |
| 9-12 | Early market candidate |
| 13-16 | Serious founder attention |

Only move a signal toward interviews or prototype offers when it has behavior-level evidence, not just attention.

### 6. Interview Power Users

For any signal scoring 9 or higher, use `power_user_interview_script.md`.

The goal is not to ask whether users like an idea. The goal is to observe how they already behave.

The key question:

```text
Show me the last time this problem happened.
```

Strong interviews reveal:

- Current workflow
- Tool being replaced
- Time spent
- Error rate
- Cost
- Urgency
- Workarounds
- Existing budget
- Who else has the same pain
- What the user would pay for immediately

### 7. Convert Clusters Into Theses

When the same pain appears across multiple communities, copy `early_market_thesis_template.md` and create a new thesis file.

Suggested naming:

```text
thesis-agent-memory-context-loss.md
thesis-local-private-agent-workspaces.md
thesis-ai-generated-app-last-mile.md
```

A good thesis names the behavior before it names the market. For example, "context babysitting" is more useful than "agent memory platform" at the research stage.

### 8. Decide The Next Action

Every signal should end in one of four states:

| State | Use When |
| --- | --- |
| Ignore | The signal is hype, isolated, or too weak. |
| Watch | The pain is real but not intense enough yet. |
| Interview users | The signal scores 9+ or repeats across multiple communities. |
| Test concierge/prototype offer | Users show urgency, replacement behavior, and plausible willingness to pay. |

## Flexible Cadence

This workflow does not require a rigid day-by-day schedule. Use whichever mode fits the time available.

### Quick Scan: 20-30 Minutes

Use when you have limited time.

1. Pick one behavioral frontier.
2. Scan 3-5 communities or searches.
3. Add 3-5 raw signals to `weirdness_ledger.md`.
4. Add only the strongest source rows to `source_map.csv`.
5. Mark next action as `ignore`, `watch`, or `score later`.

### Deep Scan: 60-90 Minutes

Use when you want a meaningful batch.

1. Scan 8-12 communities, issue trackers, or search results.
2. Capture at least 10 weird behaviors.
3. Add source rows for evidence-rich threads.
4. Score 3-5 strongest signals.
5. Pick 1-2 signals for interviews.

### Cluster Review

Use after the ledger has at least 20 entries.

1. Group entries by repeated pain.
2. Look for the same workaround showing up in different language.
3. Identify tool replacement targets.
4. Promote promising clusters into thesis files.
5. Kill weak clusters explicitly so they do not linger.

### Interview Sprint

Use when one signal scores 9+.

1. Find 5-10 users who posted about the workflow.
2. Send a specific research message.
3. Ask them to show the workflow, not describe the hypothetical need.
4. Update the thesis with evidence and counterevidence.
5. Decide whether to make a concierge/prototype offer.

### Thesis Review

Use whenever new evidence changes your confidence.

1. Update the thesis with the latest evidence.
2. Add counterevidence, especially reasons the wedge may be too small.
3. Decide the next test.
4. Mark the thesis as `active`, `watch`, `killed`, or `prototype-test`.

## What Counts As Strong Evidence

Strong evidence:

- "I stopped using X for this."
- "I built a script to make this bearable."
- "This breaks every week but I still use it."
- "I made a guide because everyone kept asking me."
- "I keep this open all day."
- "My team copy-pastes this manually every day."
- "I would pay if someone handled this end to end."

Weak evidence:

- "Looks cool."
- "This is the future."
- "Huge market."
- "Lots of likes."
- "A famous person demoed it."
- "A market map includes this category."

## First Hunting Ground

Start with agentic workflow infrastructure because it has many visible sources of behavior change:

- Agent memory and context loss
- Agent reliability and recovery
- Coding-agent workflow orchestration
- Local/private AI setups
- AI-generated app deployment and last-mile assembly
- Agent observability and evaluation
- Nontechnical automation builders

Use `examples.md` for a starting model.
