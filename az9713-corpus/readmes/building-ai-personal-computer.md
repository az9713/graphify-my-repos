# Building a Personal AI Computer

> A synthesized reference guide based on Nate's video and Substack deep-dive, extended with gap analysis and additional guidance not covered in the original.

---

## Source Material

**YouTube:** [RTX 5090, Mac Studio, or DGX Spark? I tried all three.](https://www.youtube.com/watch?v=iUSdS-6uwr4&t=1772s) — Nate Jones  
**Substack:** [The buying rule for your personal AI computer (and how to skip the $5,000 mistake)](https://natesnewsletter.substack.com/p/personal-ai-computer-stack) — Nate's Newsletter, May 1 2026

---

## What This Repo Contains

### [`ai_pc_choices_report.md`](./ai_pc_choices_report.md)
The main reference document. It summarizes every hardware option, runtime, model class, memory architecture, application, and workflow that Nate recommends — organized as a structured decision guide rather than a linear narrative.

Covers:
- All six layers of the personal AI stack (hardware → runtime → models → memory → apps → workflows)
- Every specific hardware option Nate evaluates (Mac Mini, Mac Studio, DGX Spark, dual RTX 5090s, AMD Strix Halo) with the reasoning and trade-offs behind each
- Three complete reference builds: knowledge worker, all-local maximalist, local-first builder
- Ten bottom-line guidelines for choosing hardware and components

**New: Gap Analysis section** — 14 gaps in Nate's original analysis, added for completeness:
- Missing ROI/cost numbers
- Windows platform entirely absent from hardware discussion
- Quantization decisions glossed over
- Fine-tuning vs. RAG decision framework missing
- Maintenance burden understated
- Privacy threat model undefined
- Latency vs. throughput trade-offs not distinguished
- Backup and disaster recovery for the memory layer
- LAN/multi-device sharing not mentioned
- Model licensing for commercial use
- Data ingestion tooling absent
- Hybrid inference patterns
- Small team use case missing
- On-device/mobile AI layer not addressed

---

## The Core Idea in One Paragraph

The personal AI computer is not a purity test against cloud AI. It is a routing system: some work stays local because it is private, repetitive, or context-heavy; some work goes to the cloud because it is rare, hard, or needs frontier capability. The long-term reason to build the stack is not cost savings — it is compounding your own knowledge over time through a memory layer you own. The model changes every few months. The memory gets better every year.

---

## Quick Navigation

| Decision | Where to Look |
|---|---|
| Which hardware to buy | [Layer 1: Hardware Choices](./ai_pc_choices_report.md#layer-1-hardware-choices) |
| Which runtime to install | [Layer 2: Runtime Choices](./ai_pc_choices_report.md#layer-2-runtime-choices) |
| Which models to run | [Layer 3: Model Choices](./ai_pc_choices_report.md#layer-3-model-choices) |
| How to structure memory | [Layer 4: Memory & Retrieval](./ai_pc_choices_report.md#layer-4-memory--retrieval-choices) |
| Which apps to use | [Layer 5: Applications & Interfaces](./ai_pc_choices_report.md#layer-5-applications--interfaces) |
| Which workflows to automate | [Layer 6: Workflow Choices](./ai_pc_choices_report.md#layer-6-workflow-choices) |
| Complete build recipes | [Three Complete Builds](./ai_pc_choices_report.md#three-complete-builds) |
| Buying decision rules | [Bottom Line Guidelines](./ai_pc_choices_report.md#bottom-line-guidelines-for-choosing-an-ai-pc) |
| What Nate missed | [Gaps in Nate's Analysis](./ai_pc_choices_report.md#gaps-in-nates-analysis) |

---

*All model recommendations and hardware specs reflect the state of the ecosystem as of late April / May 2026.*
