# Mechanism Space Cartographer

A Claude Code skill that maps every causal lever available to improve a business metric — before writing a single line of code or a single product spec.

---

## Origin

This project began with a YouTube video: **[I Built a $1M/y SaaS with Claude Code, Here's How](https://www.youtube.com/watch?v=K65vd9EYbDU&t=13s)**.

The host describes building Clarvo — an AI-powered outbound dialer — to $1M ARR using Claude Code. The method that made it work wasn't better code or a better model. It was a specific process for figuring out *what to build* before building anything: asking Claude to enumerate every possible causal mechanism that could improve a target metric, forcing divergence across orthogonal categories, mining hundreds of ideas to find the five or six worth pursuing.

That process, formalized and turned into a repeatable Claude Code skill, is what lives in this repository.

---

## The concept: mechanism space

A **mechanism** is a plausible causal intervention that moves a target metric. A **mechanism space** is the full set of such mechanisms for a given system.

Most product teams jump from problem to features. The better path:

```
Problem → Metric → Mechanism → Simulation → Feature → Product → Pricing
```

The mechanism step is where almost everyone skips. It's where the 90% of opportunity that doesn't get built lives.

A mechanism is not a feature. "Build a dashboard" is a feature. "Change the timing of outreach so the lead is contacted within 60 seconds of inquiry, when intent is at its peak, increasing contact probability by 3x" is a mechanism. Features implement mechanisms. Without mapping mechanisms first, you build the wrong features confidently.

---

## What's in this repo

### The skill

The `mechanism-space-cartographer` Claude Code skill runs a five-phase process:

1. **Interactive intake** — six questions, one at a time, with pushback on vague metrics
2. **Mechanism taxonomy derivation** — derives domain-specific mechanism families from the causal structure of the system, not a generic list
3. **Parallel agent exploration** — spawns one agent per mechanism family, each generating 15 mechanisms with forced orthogonal divergence
4. **Synthesis and ranking** — scores every mechanism using `(V × C × D × T) / (R + F + K)`, surfaces the top 15
5. **Output** — writes `mechanism-space.md` to the project root

**Skill files:**
- [`.claude/skills/mechanism-space-cartographer/SKILL.md`](.claude/skills/mechanism-space-cartographer/SKILL.md) — the skill definition
- [`.claude/skills/mechanism-space-cartographer/mechanism-families-reference.md`](.claude/skills/mechanism-space-cartographer/mechanism-families-reference.md) — the 14 universal mechanism families, domain-specific libraries, mechanism grammar, and system-type lookup table

### Documentation

- [`mechanism-space-cartographer-guide.md`](mechanism-space-cartographer-guide.md) — comprehensive guide covering the intellectual journey from the video to the framework to the skill, with five fully worked examples (outbound sales, dental no-shows, medical claims denial, B2B SaaS churn, AI coding agent PR acceptance)

- [`example-run-web-design-agency.md`](example-run-web-design-agency.md) — detailed capture of the first live run of the skill: the trigger prompt, the full interview Q&A, the mechanism taxonomy derivation, the parallel agent deployment, a post-mortem on the rogue agent problem, and the four fixes needed in the next version of the skill

### Example output

- [`mechanism-space.md`](mechanism-space.md) — the actual `mechanism-space.md` produced during the web design agency example run: 65 mechanisms across 6 families, top 15 ranked with scores, economic equation, data requirements, and a "what to do this week" action section

### Additional explorations

Three live runs demonstrating the skill on economically distinct domains:

- [`mechanism-space-outbound-sdr.md`](mechanism-space-outbound-sdr.md) — **Outbound B2B SDR agency**: target metric = qualified meetings booked per 100 contacts worked. 30 mechanisms across 6 families. Key finding: the highest-ranked mechanisms are all in the conversion leakage recovery family — no-shows, almost-booked contacts, and negative-reply reactivation sitting unused in every agency's CRM. Three product opportunities: no-show rescue automation, stalled contact reactivation engine, rep performance gap closer.

- [`mechanism-space-insurance-retention.md`](mechanism-space-insurance-retention.md) — **Independent P&C insurance agency**: target metric = policy renewal retention rate. 35 mechanisms across 7 families. Economic equation: each 1% retention improvement ≈ $2,900/year per agency; ~$116M aggregate annual value per 1% industry-wide. Key finding: a phone call made within 24 hours of a claim being filed moves retention from 74% to 91% on the highest-risk segment — the single highest-ROI lever, almost universally ignored. Three product opportunities: churn prioritization engine, claims response automation, household consolidation intelligence.

- [`mechanism-space-cre-tenant-renewal.md`](mechanism-space-cre-tenant-renewal.md) — **Commercial real estate**: target metric = tenant renewal rate. 30 mechanisms across 6 families. Economic equation: single prevented vacancy on a 10,000 SF space saves $600K–$1.6M in turnover cost. Key finding: the tenant's broker is the primary adversary in every renewal — financially incentivized to relocate rather than renew — yet almost no landlord has a deliberate broker relationship strategy. Three product opportunities: tenant churn intelligence platform, renewal playbook automation, tenant broker relationship manager.

- [`mechanism-space-personal-savings-rate.md`](mechanism-space-personal-savings-rate.md) — **Individual — personal savings rate**: target metric = monthly savings rate (income − spending) / income. 32 mechanisms across 6 families. Economic equation: each 5% increase in savings rate = 3–5 fewer years of mandatory work. Key finding: the top 6 mechanisms all share one structural property — they remove the recurring decision entirely. Pay-yourself-first, savings escalators, high-friction accounts, and raise capture outperform budgets and willpower because discipline is never required again after one-time setup. Three product opportunities: financial autopilot setup wizard, savings rate accountability system, raise capture service.

---

## Quick start

Install the skill into your Claude Code project:

```bash
mkdir -p .claude/skills
cp -r .claude/skills/mechanism-space-cartographer .claude/skills/
```

Then invoke it:

```
/mechanism-space-cartographer
```

Or describe a business problem and it will auto-trigger. The skill will ask you six questions before doing anything. Budget 5–10 minutes for the intake conversation — the quality of the mechanism space depends entirely on the precision of the metric you define.

---

## The scoring formula

Every mechanism is scored:

```
Score = (V × C × D × T) / (R + F + K)

V = economic value if the mechanism works
C = causal plausibility
D = data availability to validate it
T = testability (A/B test or replay simulation)
R = regulatory / compliance risk
F = implementation friction
K = complexity
```

Each dimension is rated 1–5. The formula is not meant to produce precise numbers — it's meant to force explicit reasoning about every mechanism across all dimensions simultaneously, so you don't unconsciously rank "build a dashboard" above "restructure the incentive system" because the former is easier to implement.

---

## The 14 universal mechanism families

| Family | Core question |
|--------|--------------|
| Timing | Does the same action have higher value at a different time? |
| Selection | Are some opportunities much more valuable than others? |
| Routing / matching | Does outcome depend on which actor handles which case? |
| Pacing / queueing | Is value lost to idleness or overload? |
| Information | Would better info at decision time change the action? |
| Trust / identity | Does the target hesitate due to lack of trust? |
| Behavioral / psychological | Does human attention, habit, or fear drive the outcome? |
| Incentives | Are people behaving rationally under bad incentives? |
| Constraints / compliance | Is value blocked by rules, approvals, or credentials? |
| Infrastructure | Does the technical substrate affect deliverability? |
| Sequencing | Would a different step order reduce drop-off? |
| Automation | Can a high-volume human step be replaced? |
| Friction removal | Where do users abandon due to effort or ambiguity? |
| Learning loops | Does each transaction produce data to improve future decisions? |

The right families for any given system are derived from its causal structure — not copied from this list.

---

## Known issues

**Rogue agents in Phase 3.** During the first live run, 4 of 6 parallel sub-agents overstepped their brief: instead of returning 15 structured mechanisms in the assigned family, they independently completed the full skill run, wrote `mechanism-space.md` themselves, and returned a summary. The final file was the last agent's version (which happened to be comprehensive), but the process was uncontrolled.

The fix — explicit file-write prohibition, sub-component framing, and hard stop instructions in sub-agent prompts — is documented in [`example-run-web-design-agency.md`](example-run-web-design-agency.md) and will be applied in the next version of the skill.

---

## License

MIT
