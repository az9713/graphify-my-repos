# code-as-agent-harness-tutorial

This repository is a tutorial and artifact bundle for understanding the paper
**"Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems"**
from the perspective of readers who want to quickly build a mental model of agent
harness engineering.

The repository began as a worked example of a PDF-to-expert-report pipeline. The
`pdf-to-expert-report` skill remains in this repo as an artifact of the report
generation process, but the repo's primary purpose is now the Code as Agent
Harness tutorial.

---

## What This Repository Contains

| Artifact | Purpose |
|---|---|
| [`REPORT_Code_as_Agent_Harness_PDF_Grounded.md`](REPORT_Code_as_Agent_Harness_PDF_Grounded.md) | PDF-grounded expert briefing created by Codex. This is the most source-faithful report. |
| [`REPORT_Code_as_Agent_Harness.md`](REPORT_Code_as_Agent_Harness.md) | Original expert report generated from the extraction pipeline. |
| [`code_as_agent_harness_visual_explainer.html`](code_as_agent_harness_visual_explainer.html) | Standalone interactive visual explainer. Open directly in a browser. |
| `extract_pages_01_20.md` ... `extract_pages_83_102.md` | Page-batch extraction artifacts used to synthesize the reports. |
| `.agents/skills/pdf-to-expert-report/` | Agent-compatible copy of the PDF report-generation skill used to create the artifacts. |
| `.claude/skills/pdf-to-expert-report/` | Claude-compatible copy of the same skill. |

Not committed:

- `2605.18747v1.pdf`, because it is the source paper PDF.
- `pdf_pages/`, because it is a large generated cache of rendered page images.

Both can exist locally. The page images can be regenerated from the PDF with:

```bash
python .agents/skills/pdf-to-expert-report/scripts/render_pdf.py --input 2605.18747v1.pdf --output pdf_pages/
```

---

## The Paper

The source paper is [`2605.18747`](https://arxiv.org/abs/2605.18747), a 102-page
survey arguing that code is no longer merely something LLM agents produce. Code is
increasingly the **harness** around the agent: the executable, inspectable,
stateful infrastructure that lets the model reason, act, verify, remember, and
coordinate.

The paper's core thesis:

| Property | What it means | Why it matters |
|---|---|---|
| Executable | Code runs and produces observable behavior | Plans become operations, not prose |
| Verifiable | Intermediate states can be checked | Mistakes can be caught before they propagate |
| Stateful | Programs and logs persist across steps | Agents can resume, roll back, and audit |

The paper organizes the field into three connected layers:

```text
Layer 3: Multi-agent scaling
         roles, topology, shared state, synchronization, convergence

Layer 2: Harness mechanisms
         planning, memory, tool use, control, optimization

Layer 1: Harness interface
         code for reasoning, acting, and environment modeling
```

---

## Recommended Reading Path

1. Open [`code_as_agent_harness_visual_explainer.html`](code_as_agent_harness_visual_explainer.html)
   in a browser for the fastest visual orientation.
2. Read [`REPORT_Code_as_Agent_Harness_PDF_Grounded.md`](REPORT_Code_as_Agent_Harness_PDF_Grounded.md)
   for the source-grounded expert briefing.
3. Use the `extract_pages_*.md` files to audit where the report claims came from.
4. Inspect `.agents/skills/pdf-to-expert-report/` if you want to understand or reuse
   the report-generation process.

---

## How The Report Was Generated

The report-generation workflow is itself an example of code-as-harness thinking:

```text
2605.18747v1.pdf
  |
  | render_pdf.py
  v
pdf_pages/page_001.png ... page_102.png
  |
  | parallel page extraction
  v
extract_pages_01_20.md ... extract_pages_83_102.md
  |
  | synthesis
  v
REPORT_Code_as_Agent_Harness.md
REPORT_Code_as_Agent_Harness_PDF_Grounded.md
code_as_agent_harness_visual_explainer.html
```

The process is:

1. Render the PDF to page images with PyMuPDF.
2. Extract each page batch into structured Markdown.
3. Synthesize a report for PhD-level readers outside the domain.
4. Create a visual HTML explainer for rapid understanding.

The key harness properties show up directly:

| Harness property | How this repo demonstrates it |
|---|---|
| Executable | `render_pdf.py` deterministically renders the source PDF. |
| Verifiable | Page extracts and reports can be checked against the PDF and rendered pages. |
| Stateful | Intermediate artifacts persist, so the workflow can be resumed or audited. |

---

## The `pdf-to-expert-report` Skill

The `pdf-to-expert-report` skill is included as a generated artifact and reusable
tooling bundle. It transforms a research paper PDF into an expert report by:

- rendering pages to PNG,
- extracting text, figures, diagrams, tables, equations, and algorithms,
- using page-batch extraction artifacts,
- synthesizing a structured report for expert non-domain readers.

Project-local copies:

```text
.agents/skills/pdf-to-expert-report/
.claude/skills/pdf-to-expert-report/
```

The skill name intentionally remains `pdf-to-expert-report`; only the repository
has been renamed to `code-as-agent-harness-tutorial`.

---

## Repository Layout

```text
code-as-agent-harness-tutorial/
  README.md
  REPORT_Code_as_Agent_Harness.md
  REPORT_Code_as_Agent_Harness_PDF_Grounded.md
  code_as_agent_harness_visual_explainer.html
  extract_pages_01_20.md
  extract_pages_21_41.md
  extract_pages_42_62.md
  extract_pages_63_82.md
  extract_pages_83_102.md
  .agents/skills/pdf-to-expert-report/
  .claude/skills/pdf-to-expert-report/
```

---

## Notes On Source Grounding

The PDF-grounded report treats `2605.18747v1.pdf` as the source of truth. The
`pdf_pages/` directory is only a regenerable cache. This matters because visual
page extraction can be repeated whenever the cache is missing.

The older `REPORT_Code_as_Agent_Harness.md` is retained as the first generated
report artifact. For author names and paper metadata, prefer the PDF-grounded
report.

---

## Citation

If you use this tutorial, cite the source paper:

```bibtex
@article{ning2026codeagentharness,
  title={Code as Agent Harness: Toward Executable, Verifiable, and Stateful Agent Systems},
  author={Ning, Xuying and Tieu, Katherine and Fu, Dongqi and Wei, Tianxin and Li, Zihao and Bei, Yuanchen and others},
  journal={arXiv preprint arXiv:2605.18747},
  year={2026}
}
```

---

## License

The skill code under `.agents/skills/` and `.claude/skills/` is MIT licensed.
The extraction files and reports are derived educational artifacts from the
paper and are provided for research and educational purposes.
