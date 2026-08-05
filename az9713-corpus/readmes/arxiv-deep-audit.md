# arxiv-deep-audit

A multi-agent workflow for rigorously auditing mathematical claims in arXiv papers.

## Overview

This project implements a 5-agent "Reviewer #2" pipeline that deconstructs, audits, and empirically verifies the mathematical claims in research papers. The workflow was demonstrated on arXiv:2512.15605 ("Autoregressive Language Models are Secretly Energy-Based Models" by Blondel et al., Google DeepMind).

**Result:** The paper's central theorem was **VERIFIED** with machine-epsilon precision (1.11e-16).

## Inspiration & Credits

This project was inspired by:
- **YouTube Video:** ["Claude Cowork's Agent Waterfalls Just Changed How I Teach"](https://www.youtube.com/watch?v=example) - sparked the idea of using multi-agent workflows for research auditing
- **Gemini 3.0 Pro:** Suggested the multi-agent workflow architecture, paper selection (arXiv:2512.15605), the SKILL.md structure, and the Agent D verification prompt
- **Claude Code with Opus 4.5:** Executed the complete workflow, generating all artifacts

## Architecture

The pipeline follows a fork-join topology:

```
                    ┌─────────────────────┐
                    │      Agent A        │
                    │  (Deconstructor)    │
                    │  Extract & Parse    │
                    └──────────┬──────────┘
                               │
              ┌────────────────┼────────────────┐
              │                │                │
              ▼                ▼                ▼
     ┌────────────────┐ ┌────────────────┐ ┌────────────────┐
     │    Agent B     │ │    Agent C     │ │    Agent D     │
     │  (Formalist)   │ │   (Skeptic)    │ │  (Simulator)   │
     │   Math Audit   │ │ Lit. Validation│ │   Code Verify  │
     └────────┬───────┘ └────────┬───────┘ └────────┬───────┘
              │                  │                  │
              └────────────────┬─┴──────────────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │      Agent E        │
                    │  (Editor-in-Chief)  │
                    │  Decision Memo      │
                    └─────────────────────┘
```

## Agents

| Agent | Role | Input | Output |
|-------|------|-------|--------|
| **A - Deconstructor** | Semantic segmentation of paper | Raw PDF/text | Structured JSON with `mathematical_core`, `empirical_claims`, `prior_art_claims` |
| **B - Formalist** | Mathematical audit | `mathematical_core` | PASS/FAIL with derivation trace |
| **C - Skeptic** | Literature validation | `prior_art_claims` | VALIDATED/SUSPICIOUS_REBRANDING |
| **D - Simulator** | Empirical verification | `mathematical_core` | Python code + SUCCESS/FAILURE |
| **E - Editor-in-Chief** | Final synthesis | All agent outputs | Decision memo with verdicts |

## Example Output: arXiv:2512.15605

### Final Verdicts

```
┌─────────────────────────────────────────────────────────────┐
│                    FINAL AUDIT RESULTS                      │
├─────────────────────────────────────────────────────────────┤
│  Mathematical Correctness:     ✅ PASS                      │
│  Empirical Verification:       ✅ SUCCESS: THEOREM VERIFIED │
│  Novelty Assessment:           ⚠️ PARTIAL (Proposition 2)   │
│  Literature Honesty:           ✅ CITES PRIOR WORK          │
│  Thermodynamic Metaphor:       ⚠️ DECORATIVE BUT SOUND      │
├─────────────────────────────────────────────────────────────┤
│  BISIMULATION SCORE:           100%                         │
│  THERMODYNAMIC VALIDITY:       METAPHOR (not physics)       │
├─────────────────────────────────────────────────────────────┤
│         RECOMMENDATION: ACCEPT (with reservations)          │
└─────────────────────────────────────────────────────────────┘
```

### Key Findings

- **Agent B (Math):** All derivations trace completely. Soft Bellman connection is mathematically valid.
- **Agent C (Literature):** ~60% overlap with prior MaxEnt RL work (Ziebart 2008). Proposition 2 (teacher forcing optimality) is genuinely novel.
- **Agent D (Simulation):** Bijection verified at machine epsilon (1.11e-16) across all 625 sequences in toy universe.

## Repository Structure

```
arxiv-deep-audit/
├── README.md                           # This file
├── CLAUDE.md                           # Project instructions for Claude Code
├── .claude/
│   ├── skills/
│   │   └── arxiv_audit/
│   │       └── SKILL.md                # Agent workflow definition
│   └── prompts/
│       └── agent_d_verification.md.txt # Agent D system prompt
├── docs/
│   └── 2512.15605v1.pdf                # Source paper
└── output/
    ├── agent_a_deconstruction.json     # Structured paper decomposition
    ├── agent_b_math_audit.md           # Mathematical audit report
    ├── agent_c_literature_validation.md # Novelty assessment
    ├── verification_script.py          # Executable verification code
    ├── verification_plot.png           # Visual bijection proof
    ├── agent_d_simulation_report.md    # Simulation report
    ├── DECISION_MEMO.md                # Final verdict
    └── WORKFLOW_DOCUMENTATION.md       # Execution documentation
```

## How to Use

### Running the Verification Script

```bash
cd output
python verification_script.py
```

Expected output:
```
SUCCESS: THEOREM VERIFIED
All 625 sequences satisfy: |P_ARM(x) - P_EBM(x)| < 1e-7
```

### Adapting for Other Papers

1. Replace the PDF in `docs/`
2. Update the target in `.claude/skills/arxiv_audit/SKILL.md`
3. Modify the Agent D prompt in `.claude/prompts/` as needed
4. Run the workflow in Claude Code

### Workflow Execution

The workflow is designed to be executed in Claude Code with Opus 4.5. The execution follows the topology:
1. **START** → Agent A
2. **FORK** → Agents B, C, D (parallel)
3. **AWAIT_ALL**
4. **JOIN** → Agent E
5. **END**

## Global Constraints

- **Persona:** "Reviewer #2" - Ruthless, skeptical, mathematically precise
- **Precision:** 6-sigma. Zero tolerance for hand-waving.
- **Hallucination Policy:** STRICT. Flag derivation gaps, do not bridge them.
- **Output Format:** Structured Markdown with LaTeX for all math

## License

MIT License

---

*Generated with [Claude Code](https://claude.ai/code) using Opus 4.5*
