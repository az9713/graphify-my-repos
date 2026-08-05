# Claude for Legal

> **This is a tutorial fork of [anthropics/claude-for-legal](https://github.com/anthropics/claude-for-legal).** The plugins and skills are identical to the original. This fork adds a [`docs/`](./docs/) directory with deep-dive documentation that dissects how every plugin and skill is constructed — surfacing the design patterns, best practices, and architectural decisions behind the system. If you want to understand how to build on this, extend it, or replicate the patterns in your own plugins, start with the docs.

## Deep-dive documentation

| Doc | What it covers |
|---|---|
| [Overview: what is this?](docs/overview/what-is-this.md) | Mental model, ASCII architecture diagram, end-to-end session narrative, scope boundaries |
| [Key concepts glossary](docs/overview/key-concepts.md) | 38-term glossary — every concept used across plugins and skills defined precisely |
| [Quickstart](docs/getting-started/quickstart.md) | Working in under 15 minutes — dual path for Claude Cowork and Claude Code |
| [Onboarding guide](docs/getting-started/onboarding.md) | Zero-to-confident: the linter analogy, the three things you must understand, a full NDA walkthrough |
| [Plugin anatomy](docs/concepts/plugin-anatomy.md) | Every file in a plugin directory dissected — plugin.json, CLAUDE.md, skills/, agents/, hooks/, .mcp.json |
| [Skill anatomy](docs/concepts/skill-anatomy.md) | SKILL.md structure, frontmatter fields, all 8 recurring design patterns, skill design checklist |
| [Practice profile](docs/concepts/practice-profile.md) | Config path contract, shared company profile, every CLAUDE.md section and its reasoning |
| [Guardrails](docs/concepts/guardrails.md) | All 18 shared guardrails dissected — no-silent-supplement, citation hygiene, destination check, cross-skill severity floor, and more |
| [Agents](docs/concepts/agents.md) | Scheduled agent anatomy, how agents call skills, managed-agent cookbook deployment |
| [Connectors](docs/concepts/connectors.md) | MCP connector config, full connector table by practice area, the four behavior requirements |
| [Hooks](docs/concepts/hooks.md) | hooks.json format, all hook events, practical legal-context examples |
| [Build a skill](docs/guides/build-a-skill.md) | Step-by-step guide to authoring a SKILL.md that follows all 9 design principles |
| [Build a plugin](docs/guides/build-a-plugin.md) | Full plugin creation guide — directory layout, required files, 3 mandatory skills, CLAUDE.md construction |
| [Customize a plugin](docs/guides/customize-a-plugin.md) | Three-level customization: cold-start interview, customize skill, direct editing |
| [SKILL.md frontmatter reference](docs/reference/skill-frontmatter.md) | Every frontmatter field with valid values, defaults, and source examples |
| [plugin.json reference](docs/reference/plugin-json.md) | plugin.json and marketplace.json fields, version bump rules, author vs. owner distinction |
| [Tag vocabulary reference](docs/reference/tag-vocabulary.md) | All 20+ inline tags — factual accuracy, source provenance, judgment, severity, cell states |
| [System design](docs/architecture/system-design.md) | Full ASCII architecture diagram, 5 data flows, component breakdown, scaling characteristics |
| [ADR 001: Two-layer instruction architecture](docs/architecture/adr/001-two-layer-instruction-architecture.md) | Why SKILL.md + CLAUDE.md — alternatives analyzed, trade-offs, consequences |
| [ADR 002: Practice profile as plain text](docs/architecture/adr/002-practice-profile-as-plain-text.md) | Why markdown over YAML/JSON/database — alternatives analyzed, trade-offs, consequences |
| [commercial-legal deep-dive](docs/plugins/commercial-legal.md) | Sales vs. purchasing playbook, GREEN gate, scope check, dual severity, playbook monitor |
| [corporate-legal deep-dive](docs/plugins/corporate-legal.md) | Modular profile, typed column schema, verbatim enforcement, fan-out pattern |
| [employment-legal deep-dive](docs/plugins/employment-legal.md) | Jurisdiction-first analysis, worker classification, investigation four-skill pattern |
| [privacy-legal deep-dive](docs/plugins/privacy-legal.md) | Three-tier triage, DPA auto-detection, DSAR statutory timelines, policy drift monitoring |
| [product-legal deep-dive](docs/plugins/product-legal.md) | Proportionality-first is-this-a-problem, risk calibration, launch tracker integration |
| [regulatory-legal deep-dive](docs/plugins/regulatory-legal.md) | Materiality filter, Monday digest format, policy diff, gap tracker |
| [ai-governance-legal deep-dive](docs/plugins/ai-governance-legal.md) | Per-system classification, use-case registry, red lines, intentional no-auto-derive design |
| [ip-legal deep-dive](docs/plugins/ip-legal.md) | Triage vs. opinion distinction, DMCA three-way, enforcement posture, OSS license classification |
| [litigation-legal deep-dive](docs/plugins/litigation-legal.md) | Dual-surface pattern, FRE 408 gate, chronology builder, privilege log review |
| [legal-clinic deep-dive](docs/plugins/legal-clinic.md) | ABA Formal Op. 512, three supervision models, hard deadline do-not-compute gate |
| [law-student deep-dive](docs/plugins/law-student.md) | Learning mode cardinal rule, Socratic push-back loop, Leitner buckets, bar prep |
| [legal-builder-hub deep-dive](docs/plugins/legal-builder-hub.md) | Six-gate trust layer, LSDF scoring, SHA-pinned updates, restrictive-by-default allowlist |
| [Troubleshooting](docs/troubleshooting/common-issues.md) | Top 10 issues with exact fix commands and escalation paths |

---

Reference agents, skills, and data connectors for the legal workflows we see most — in-house commercial, privacy, product, corporate, employment, litigation, regulatory, AI governance, IP, and the learning side of the practice (law school clinics and students).

> **New here?** Start with [QUICKSTART.md](QUICKSTART.md) — install in 60 seconds. This README is the full reference.

Everything here is available **two ways from one source**: install it as a [Claude Cowork](https://claude.com/product/cowork) or [Claude Code](https://claude.com/product/claude-code) plugin, or deploy it through the [Claude Managed Agents API](https://docs.claude.com/en/api/managed-agents) behind your own workflow engine. Same system prompt, same skills — you choose where it runs.

## Getting started in Cowork
- [Install Claude Desktop](https://claude.com/download)
- Get access to Claude Cowork
- Follow the instructions in the video below:

https://github.com/user-attachments/assets/51394f0a-5277-4fe2-b81c-5c5e9ac876b5

> [!IMPORTANT]
> **Every output from these plugins is a draft for attorney review — not legal advice, not a legal conclusion, not a substitute for a lawyer.** They are built with guardrails that reflect that: source attribution on every citation, conservative defaults on privilege and subjective legal calls, jurisdiction assumptions surfaced, and explicit gates before anything is filed, sent, or relied on. A lawyer reviews, verifies, and takes professional responsibility for anything that leaves the building. These plugins make that review faster; they do not replace it.
>
> **These plugins do not represent Anthropic's legal positions.** They are tools that help lawyers analyze issues. Where a skill includes a checklist item, a suggested framework, a risk flag, or a characterization of case law or regulatory guidance, that is an aid to the reviewing attorney's own analysis, not a statement of Anthropic's view of the law. The law in many of these areas is unsettled and evolving. The attorney using the plugin — not the plugin, and not Anthropic — is responsible for the legal positions taken in their work product.

What's in the repo:

- **Practice-area plugins** covering in-house, firm, and academic legal work — each one built around a cold-start interview that learns your playbook and a `CLAUDE.md` practice profile that every skill reads from.
- **Managed-agent cookbooks** for the scheduled, eyes-on-the-feed workflows (renewal watcher, docket watcher, regulatory feed monitor, diligence grid, launch radar).
- **MCP connectors** across general productivity (Slack, Google Drive, Box) and legal-specific systems (Ironclad, DocuSign, iManage, Everlaw, CourtListener, and more).
- **[Named agents](#agents)** — end-to-end workflow agents (Vendor Agreement Reviewer, DSAR Responder, Termination Reviewer, Claim Chart Builder, …) with job-style names and a single command to run each one.

## Agents

Each agent is named for the workflow it runs. They're the most common surface — start with the ones that match your work, then tune the underlying skill, the practice profile, and the connectors to how your team does it.

| Agent | What it does | Plugin | Command |
|---|---|---|---|
| **Vendor Agreement Reviewer** | Reviews a vendor MSA against your playbook and produces a redline memo | `commercial-legal` | `/commercial-legal:review` |
| **NDA Triager** | GREEN/YELLOW/RED triage of inbound NDAs so only the hard ones hit a lawyer's desk | `commercial-legal` | `/commercial-legal:review` |
| **Amendment Tracer** | Traces how a contract has changed across its base agreement and every amendment | `commercial-legal` | `/commercial-legal:amendment-history` |
| **Renewal Watcher** | Scans the contract register for cancel-by and renewal deadlines | `commercial-legal` | scheduled agent |
| **Deal Debrief** | Weekly sweep of signed agreements with playbook deviations — prompts the attorney to log context while memory is fresh | `commercial-legal` | scheduled agent |
| **Playbook Monitor** | Watches the deviation log and proposes playbook updates when a clause has drifted | `commercial-legal` | scheduled agent |
| **Escalation Router** | Routes contract issues to the right approver and drafts the ask | `commercial-legal` | `/commercial-legal:escalation-flagger` |
| **Tabular Diligence Review** | Tabular review over a data room with one row per document and every cell cited | `corporate-legal` | `/corporate-legal:tabular-review` |
| **Issue Extractor** | Reads VDR documents and extracts issues per house categories and materiality thresholds | `corporate-legal` | `/corporate-legal:diligence-issue-extraction` |
| **Board Consent Drafter** | Drafts unanimous written consents in house format with precedent search | `corporate-legal` | `/corporate-legal:written-consent` |
| **Material Contracts Schedule Builder** | Builds the disclosure schedule from diligence findings against the purchase-agreement threshold | `corporate-legal` | `/corporate-legal:material-contract-schedule` |
| **Entity Compliance Tracker** | Computes filing deadlines across jurisdictions and entity types, runs health audits | `corporate-legal` | `/corporate-legal:entity-compliance` |
| **Closing Checklist Driver** | Tracks every condition, consent, document, and filing blocking close | `corporate-legal` | `/corporate-legal:closing-checklist` |
| **Integration Runbook** | Phased post-closing integration plan with consent tracking and weekly status | `corporate-legal` | `/corporate-legal:integration-management` |
| **Data Room Watcher** | Monitors the VDR for new uploads and posts closing checklist status on schedule | `corporate-legal` | scheduled agent |
| **Termination Reviewer** | Runs a proposed termination against jurisdiction-specific risk flags | `employment-legal` | `/employment-legal:termination-review` |
| **Hire Reviewer** | Reviews offer letters and restrictive covenants with a jurisdiction check | `employment-legal` | `/employment-legal:hiring-review` |
| **Worker Classification Screener** | Tests a proposed engagement against the controlling state test | `employment-legal` | `/employment-legal:worker-classification` |
| **Leave Tracker** | Monitors open leaves with FMLA/CFRA/PFL/ADA deadlines and decision-point alerts | `employment-legal` | scheduled agent |
| **Investigation Lead** | Opens, tracks, adds to, and summarizes internal investigation matters | `employment-legal` | `/employment-legal:investigation-open` |
| **Policy Drafter** | Drafts employment policies with state supplements where law differs | `employment-legal` | `/employment-legal:policy-drafting` |
| **International Expansion Planner** | Kicks off EOR-vs-entity planning and outside-counsel briefing for a new country | `employment-legal` | `/employment-legal:expansion-kickoff` |
| **Wage & Hour Q&A** | Jurisdiction-aware employment Q&A for the "quick question" channel | `employment-legal` | `/employment-legal:wage-hour-qa` |
| **DSAR Responder** | Drafts DSAR acknowledgments and substantive responses within statutory timelines | `privacy-legal` | `/privacy-legal:dsar-response` |
| **DPA Reviewer** | Reviews a DPA against your playbook as controller or processor | `privacy-legal` | `/privacy-legal:dpa-review` |
| **PIA Generator** | Generates a Privacy Impact Assessment in house format for a new feature or activity | `privacy-legal` | `/privacy-legal:pia-generation` |
| **Privacy Triager** | Decides whether a processing activity needs a PIA, a mandatory GDPR DPIA, or can proceed | `privacy-legal` | `/privacy-legal:use-case-triage` |
| **Privacy Reg Gap Checker** | Diffs a new or changed regulation against current privacy policy and practice | `privacy-legal` | `/privacy-legal:reg-gap-analysis` |
| **Privacy Policy Monitor** | Sweeps saved PIAs, DPA reviews, and triage results for policy drift | `privacy-legal` | `/privacy-legal:policy-monitor` |
| **Launch Reviewer** | Reviews a product launch against your risk calibration | `product-legal` | `/product-legal:launch-review` |
| **Marketing Claims Checker** | Flags copy that needs substantiation, reframing, or cutting | `product-legal` | `/product-legal:marketing-claims-review` |
| **"Is this a problem?" Triage** | Fast answer for the quick Slack question — pattern-matches your calibration | `product-legal` | `/product-legal:is-this-a-problem` |
| **Launch Watcher** | Watches the launch tracker for upcoming launches that need legal review | `product-legal` | scheduled agent |
| **Reg Feed Watcher** | Polls regulatory feeds and writes the Monday-morning digest | `regulatory-legal` | scheduled agent |
| **On-demand Reg Check** | Check regulatory feeds now and report what's new since last check | `regulatory-legal` | `/regulatory-legal:reg-feed-watcher` |
| **Policy Diff** | Diffs a specific regulatory change against the indexed policy library | `regulatory-legal` | `/regulatory-legal:policy-diff` |
| **Gap Tracker** | Open gaps tracker — what's flagged and not yet closed | `regulatory-legal` | `/regulatory-legal:gaps` |
| **Policy Redrafter** | Marked-up policy redraft closing a gap — a proposal for the policy owner's review, not a direct edit to source documents | `regulatory-legal` | `/regulatory-legal:policy-redraft` |
| **NPRM Comment Tracker** | Review open NPRM comment periods, log decisions, track deadlines | `regulatory-legal` | `/regulatory-legal:comments` |
| **AI Use Case Triager** | Classifies proposed AI use cases against your registry | `ai-governance-legal` | `/ai-governance-legal:use-case-triage` |
| **AI Impact Assessor** | Runs an AIA across the regimes in scope | `ai-governance-legal` | `/ai-governance-legal:aia-generation` |
| **Vendor AI Reviewer** | Reviews vendor AI terms for training-on-data, liability, model-change, and policy gaps | `ai-governance-legal` | `/ai-governance-legal:vendor-ai-review` |
| **AI Reg Gap Checker** | Diffs a new AI regulation against your current governance posture | `ai-governance-legal` | `/ai-governance-legal:reg-gap-analysis` |
| **AI Policy Monitor** | Sweeps saved AIAs, triage results, and vendor reviews for AI-policy drift | `ai-governance-legal` | `/ai-governance-legal:policy-monitor` |
| **Trademark Clearance Screener** | First-pass clearance with knockout check and confusion heuristics | `ip-legal` | `/ip-legal:clearance` |
| **Cease & Desist Drafter** | Drafts or triages a C&D, calibrated to your enforcement posture | `ip-legal` | `/ip-legal:cease-desist` |
| **DMCA Takedown** | Drafts a takedown, triages one received, or drafts a §512(g) counter-notice | `ip-legal` | `/ip-legal:takedown` |
| **OSS Compliance Checker** | Classifies open source licenses against your deployment model | `ip-legal` | `/ip-legal:oss-review` |
| **FTO Triager** | Structured first look at potentially blocking patents — triage, not an opinion | `ip-legal` | `/ip-legal:fto-triage` |
| **Infringement Triager** | Triage across TM / copyright / patent / trade secret — factors, not a finding | `ip-legal` | `/ip-legal:infringement-triage` |
| **IP Clause Reviewer** | Reviews assignment, ownership, license grants, warranties, and indemnities | `ip-legal` | `/ip-legal:ip-clause-review` |
| **IP Portfolio Tracker** | Registrations, renewals, maintenance fees, use declarations | `ip-legal` | `/ip-legal:portfolio` |
| **IP Renewal Watcher** | Scheduled deadline report from the IP portfolio register | `ip-legal` | scheduled agent |
| **Claim Chart Builder** | Element-by-element claim chart, patent or civil cause of action | `litigation-legal` | `/litigation-legal:claim-chart` |
| **Docket Watcher** | Monitors court dockets for filings and deadlines | `litigation-legal` | scheduled agent |
| **Demand Letter Drafter** | Drafts a demand with FRE 408 awareness and a send gate | `litigation-legal` | `/litigation-legal:demand-draft` |
| **Demand Intake** | Pre-drafting context gathering — parties, facts, basis, leverage, privilege | `litigation-legal` | `/litigation-legal:demand-intake` |
| **Demand Received Triage** | Triages an inbound demand — options, portfolio cross-check, handoff | `litigation-legal` | `/litigation-legal:demand-received` |
| **Subpoena Triage** | Classifies, scopes, and plans compliance with a new subpoena | `litigation-legal` | `/litigation-legal:subpoena-triage` |
| **Chronology Builder** | Builds or updates a chronology from declared sources and uploads | `litigation-legal` | `/litigation-legal:chronology` |
| **Deposition Prep** | Builds a deposition outline tied to case theory with docs and impeachment | `litigation-legal` | `/litigation-legal:deposition-prep` |
| **Brief Section Drafter** | Drafts a brief section in house style, consistent with case theory | `litigation-legal` | `/litigation-legal:brief-section-drafter` |
| **Privilege Log Reviewer** | First-pass privilege log review — obvious calls + flags for attorney review | `litigation-legal` | `/litigation-legal:privilege-log-review` |
| **Legal Hold** | Issue, refresh, release, or report on legal holds | `litigation-legal` | `/litigation-legal:legal-hold` |
| **Matter Intake** | Uniform intake for a new matter — writes matter.md, history.md, appends to log | `litigation-legal` | `/litigation-legal:matter-intake` |
| **Matter Briefing** | Deep briefing on one matter — ready for a GC or outside counsel call | `litigation-legal` | `/litigation-legal:matter-briefing` |
| **Portfolio Status** | Risk distribution, upcoming deadlines, stale matters | `litigation-legal` | `/litigation-legal:portfolio-status` |
| **Outside Counsel Status** | Generates weekly status-request drafts across the active portfolio | `litigation-legal` | `/litigation-legal:oc-status` |
| **Clinic Intake** | Structured client intake with cross-area issue spotting and conflict flags | `legal-clinic` | `/legal-clinic:client-intake` |
| **Case Memo Scaffold** | IRAC-scaffolded case analysis memo with research gaps flagged | `legal-clinic` | `/legal-clinic:memo` |
| **Research Roadmap** | Statutes to check, case law areas, Westlaw search terms — leads, not cites | `legal-clinic` | `/legal-clinic:research-start` |
| **Clinic Deadline Tracker** | Add, report, update, and close case deadlines with malpractice-aware warnings | `legal-clinic` | `/legal-clinic:deadlines` |
| **Case Status Summarizer** | Case status by audience — client, professor, or court-ready | `legal-clinic` | `/legal-clinic:statu