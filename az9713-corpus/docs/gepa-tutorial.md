---
repo: gepa-tutorial
description: A learning-focused clone of gepa-ai/gepa: zero-to-hero interactive onboarding docs + a new program-synthesis example with a 100% local scorer.
language: Jupyter Notebook
stars: 0
forks: 0
created: 2026-06-05
updated: 2026-06-05
topics: 
is_fork: False
kb: 24756
---

# gepa-tutorial
<!-- ============================================================================ -->
<!--  gepa-tutorial — a learning-focused clone of gepa-ai/gepa                    -->
<!-- ============================================================================ -->

> # 🎓 gepa-tutorial
>
> **This repository is a clone of the original [`gepa-ai/gepa`](https://github.com/gepa-ai/gepa), enhanced for learning.**
> It is the same GEPA library, plus a friction-free, zero-to-hero path to understanding it:
>
> - 📚 **[Zero-to-Hero onboarding documentation →](onboarding/README.md)**
>   Explains GEPA from scratch for readers with **no prior knowledge** — concepts, the optimization
>   loop, the Pareto frontier, and reflection — with a glossary, quickstart, and recipes.
>   **👉 [Open the interactive guide as a live web page](https://az9713.github.io/gepa-tutorial/onboarding/index.html)**
>   (animated, clickable; [source](onboarding/index.html)).
>
> - 🧪 **[A new runnable example: program synthesis from examples →](examples/program_synthesis_from_examples/)**
>   GEPA **writes a Python function from labeled data**, scored **100% locally** (no task LLM — only the
>   reflection LLM thinks). Runs offline with `--smoke`, no API key required.
>
> All credit for GEPA itself goes to the original authors and contributors; it is distributed here under
> the original **MIT License** (see [`LICENSE`](LICENSE)). The unmodified upstream README follows. ⬇️

---

<p align="center">
  <img src="https://raw.githubusercontent.com/gepa-ai/gepa/refs/heads/main/docs/docs/assets/gepa_logo_with_text.svg" alt="GEPA Logo" width="450">
</p>

<p align="center">
  <strong>Optimize any text parameter — prompts, code, agent architectures, configurations — using LLM-based reflection and Pareto-efficient evolutionary search.</strong>
</p>

<p align="center">
  <a href="https://gepa-ai.github.io/gepa/"><strong>Website</strong></a> &ensp;|&ensp;
  <a href="https://gepa-ai.github.io/gepa/guides/quickstart/"><strong>Quick Start</strong></a> &ensp;|&ensp;
  <a href="https://arxiv.org/abs/2507.19457"><strong>Paper</strong></a> &ensp;|&ensp;
  <a href="https://gepa-ai.github.io/gepa/blog/"><strong>Blog</strong></a> &ensp;|&ensp;
  <a href="https://discord.gg/WXFSeVGdbW"><strong>Discord</strong></a>
</p>

<p align="center">
  <a href="https://pypi.org/project/gepa/"><img src="https://img.shields.io/pypi/v/gepa?logo=python&logoColor=white&color=3776ab" alt="PyPI"></a>
  <a href="https://pepy.tech/projects/gepa"><img src="https://static.pepy.tech/badge/gepa" alt="Downloads"></a>
  <a href="https://github.com/gepa-ai/gepa"><img src="https://img.shields.io/github/stars/gepa-ai/gepa?style=flat&logo=github&color=181717" alt="GitHub stars"></a>
  <a href="https://opensource.org/licenses/MIT"><img src="https://img.shields.io/badge/License-MIT-green?style=flat" alt="License"></a>
</p>

<p align="center">
  <a href="https://join.slack.com/t/gepa-ai/shared_invite/zt-3o352xhyf-QZDfwmMpiQjsvoSYo7M1_w"><img src="https://badgen.net/badge/icon/Slack?icon=slack&label&color=4A154B" alt="Slack"></a>
  <a href="https://discord.gg/WXFSeVGdbW"><img src="https://dcbadge.limes.pink/api/server/https://discord.gg/WXFSeVGdbW?style=flat" alt="Discord"></a>
</p>

---

> ### 👋 New to GEPA? Start with the [**Zero‑to‑Hero onboarding**](onboarding/README.md)
> A friction‑free path for readers with **no prior knowledge** of GEPA or related tech. It includes an
> [**interactive guide**](onboarding/index.html) (a single, self‑contained HTML page — no install, works
> offline) that animates the optimization loop and lets you *see* GEPA's per‑example Pareto frontier.
> Most people get the core idea in ~10 minutes.

---

## What is GEPA?

**GEPA** (Genetic-Pareto) is a framework for optimizing any system with textual parameters against any evaluation metric. Unlike RL or gradient-based methods that collapse execution traces into a single scalar reward, GEPA uses LLMs to *read* full execution traces — error messages, profiling data, reasoning logs — to diagnose *why* a candidate failed and propose targeted fixes. Through iterative reflection, mutation, and Pareto-aware selection, GEPA evolves high-performing variants with minimal evaluations.

**If you can measure it, you can optimize it**: prompts, code, agent architectures, scheduling policies, vector graphics, and more.

### Key Results

| | |
|---|---|
| **90x cheaper** | Open-source models + GEPA beat Claude Opus 4.1 at [Databricks](https://www.databricks.com/blog/building-state-art-enterprise-agents-90x-cheaper-automated-prompt-optimization) |
| **35x faster than RL** | 100–500 evaluations vs. 5,000–25,000+ for GRPO ([paper](https://arxiv.org/abs/2507.19457)) |
| **32% → 89%** | ARC-AGI agent accuracy via [architecture discovery](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/#5-agent-architecture-discovery) |
| **40.2% cost savings** | Cloud scheduling policy [discovered by GEPA](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/#3-systems-research), beating expert heuristics |
| **55% → 82%** | Coding agent resolve rate on Jinja via [auto-learned skills](https://gepa-ai.github.io/gepa/blog/automatically-learning-skills-for-coding-agents/) |
| **50+ production uses** | Across Shopify, Databricks, Dropbox, OpenAI, Pydantic, MLflow, Comet ML, and [more](https://gepa-ai.github.io/gepa/guides/use-cases/) |

> *"Both DSPy and (especially) **GEPA are currently severely under hyped** in the AI context engineering world"* — **Tobi Lutke**, CEO, Shopify

---

## Installation

```bash
pip install gepa
```

To install the latest from `main`:

```bash
pip install git+https://github.com/gepa-ai/gepa.git
```

---

## Quick Start

### Simple Prompt Optimization

Optimize a system prompt for math problems from the AIME benchmark in a few lines of code ([full tutorial](https://dspy.ai/tutorials/gepa_aime/)):

```python
import gepa

trainset, valset, _ = gepa.examples.aime.init_dataset()

seed_prompt = {
    "system_prompt": "You are a helpful assistant. Answer the question. "
                     "Put your final answer in the format '### <answer>'"
}

result = gepa.optimize(
    seed_candidate=seed_prompt,
    trainset=trainset,
    valset=valset,
    task_lm="openai/gpt-4.1-mini",
    max_metric_calls=150,
    reflection_lm="openai/gpt-5",
)

print("Optimized prompt:", result.best_candidate['system_prompt'])
```

**Result:** GPT-4.1 Mini goes from 46.6% → 56.6% on AIME 2025 (+10 percentage points).

### With DSPy (Recommended for AI Pipelines)

The most powerful way to use GEPA for prompt optimization is within [DSPy](https://dspy.ai/), where it's available as `dspy.GEPA`. See [dspy.GEPA tutorials](https://dspy.ai/tutorials/gepa_ai_program/) for executable notebooks.

```python
import dspy

optimizer = dspy.GEPA(
    metric=your_metric,
    max_metric_calls=150,
    reflection_lm="openai/gpt-5",
)
optimized_program = optimizer.compile(student=MyProgram(), trainset=trainset, valset=valset)
```

### optimize_anything: Beyond Prompts

The [`optimize_anything`](https://gepa-ai.github.io/gepa/blog/introducing-optimize-anything/) API optimizes *any* text artifact — code, agent architectures, configurations, SVGs — not just prompts. You provide an evaluator; the system handles the search.

```python
import gepa.optimize_anything as oa
from gepa.optimize_anything import optimize_anything, GEPAConfig, EngineConfig

def evaluate(candidate: str) -> float:
    result = run_my_system(candidate)
    oa.log(f"Output: {result.output}")      # Actionable Side Information
    oa.log(f"Error: {result.error}")         # feeds back into reflection
    return result.score

result = optimize_anything(
    seed_candidate="<your initial artifact>",
    evaluator=evaluate,
    objective="Describe what you want to optimize for.",
    config=GEPAConfig(engine=EngineConfig(max_metric_calls=100)),
)
```

---

## How It Works

Traditional optimizers know *that* a candidate failed but not *why*. GEPA takes a different approach:

1. **Select** a candidate from the Pareto frontier (candidates excelling on different task subsets)
2. **Execute** on a minibatch, capturing full execution traces
3. **Reflect** — an LLM reads the traces (error messages, profiler output, reasoning logs) and diagnoses failures
4. **Mutate** — generate an improved candidate informed by accumulated lessons from all ancestors
5. **Accept** — add to the pool if improved, update the Pareto front

GEPA also supports **system-aware merge** — combining strengths of two Pareto-optimal candidates excelling on different tasks. The key concept is **Actionable Side Information (ASI)**: diagnostic feedback returned by evaluators that serves as the text-optimization analogue of a gradient.

For details, see the [paper](https://arxiv.org/abs/2507.19457) and the [documentation](https://gepa-ai.github.io/gepa/guides/).

---

## Adapters: Plug GEPA into Any System

GEPA connects to your system via the [`GEPAAdapter`](src/gepa/core/adapter.py) interface — implement `evaluate` and `make_reflective_dataset`, and GEPA handles the rest.

**Built-in adapters:**

| Adapter | Description |
|---|---|
| [DefaultAdapter](src/gepa/adapters/default_adapter/) | System prompt optimization for single-turn LLM tasks |
| [ConfidenceAdapter](src/gepa/adapters/confidence_adapter/) | Logprob-aware classification optimization — penalizes lucky guesses and feeds confidence diagnostics into reflection. `pip install "gepa[confidence]"` |
| [DSPy Full Program](src/gepa/adapters/dspy_full_program_adapter/) | Evolves entire DSPy programs (signatures, modules, control flow). **67% → 93%** on MATH. |
| [Generic RAG](src/gepa/adapters/generic_rag_adapter/) | Vector store-agnostic RAG optimization (ChromaDB, Weaviate, Qdrant, Pinecone) |
| [MCP Adapter](src/gepa/adapters/mcp_adapter/) | Optimize [MCP](https://modelcontextprotocol.io/) tool descriptions and system prompts |
| [TerminalBench](src/gepa/adapters/terminal_bench_adapter/) | Optimize the [Terminus](https://www.tbench.ai/terminus) terminal-use agent |
| [AnyMaths](src/gepa/adapters/anymaths_adapter/) | Mathematical problem-solving and reasoning tasks |
| [LangChain](src/gepa/adapters/langchain_adapter/) | Optimize prompts for any LangChain pipeline — chat models, tool-using agents, LangGraph. `pip install "gepa[langchain]"` |

See the [adapters guide](https://gepa-ai.github.io/gepa/guides/adapters/) for how to build your own, and [DSPy's adapter](https://github.com/stanfordnlp/dspy/tree/main/dspy/teleprompt/gepa/gepa_utils.py) as a reference.

---

## Integrations

GEPA is integrated into several major frameworks:

- **[DSPy](https://dspy.ai/)** — `dspy.GEPA` for optimizing DSPy programs. [Tutorials](https://dspy.ai/tutorials/gepa_ai_program/).
- **[MLflow](https://mlflow.org/docs/latest/genai/prompt-registry/optimize-prompts/)** — `mlflow.genai.optimize_prompts()` for automatic prompt improvement.
- **[Comet ML Opik](https://www.comet.com/docs/opik/agent_optimization/algorithms/gepa_optimizer)** — Core optimization algorithm in Opik Agent Optimizer.
- **[Pydantic](https://pydantic.dev/articles/prompt-optimization-with-gepa)** — Prompt optimization for Pydantic AI.
- **[OpenAI Cookbook](https://cookbook.openai.com/examples/partners/self_evolving_agents/autonomous_agent_retraining)** — Self-evolving agents with GEPA.
- **[HuggingFace Cookbook](https://huggingface.co/learn/cookbook/en/dspy_gepa)** — Prompt optimization guide.
- **[Google ADK / Gemini Enterprise Agent Platform](https://docs.cloud.google.com/gemini-enterprise-agent-platform/optimize/evaluation/optimize-agent)** — `adk optimize` powered by GEPA, also shipped inside Google Cloud's Gemini Enterprise Agent Platform Quality Flywheel. [ADK docs](https://adk.dev/optimize/) · [Community tutorial](https://raphaelmansuy.github.io/adk_training/blog/gepa-optimization-tutorial/).
- **[Microsoft AI: MAI-Thinking-1](https://microsoft.ai/wp-content/uploads/2026/06/main_20260602_2.pdf)** — Uses GEPA / DSPy to optimize the Qwen3-30B LLM-judge prompt that filters Code pages in the model's pre-training pipeline (~233B tokens of curated data).

---

## Example Optimized Prompts

GEPA can be thought of as precomputing reasoning during optimization to produce a plan for future task instances. Here are examples of the detailed prompts GEPA discovers:

<table>
  <tr>
  <td colspan="2" align="center">Example GEPA Prompts</td>
  </tr>
  <tr>
    <td align="center">HotpotQA (multi-hop QA) Prompt</td>
    <td align="center">AIME Prompt</td>
  </tr>
  <tr>
    <td width="52%" valign="top">
      <img src="https://raw.githubusercontent.com/gepa-ai/gepa/refs/heads/main/assets/gepa_prompt_hotpotqa.png" alt="HotpotQA Prompt" width="1400">
      <!-- <td> -->
      <details>
<summary><mark>Click to view full HotpotQA prompt</mark></summary>
<mark>[HotpotQA Prompt Begin]</mark>

You will be given two input fields: `question` and `summary_1`.

Your task is to generate a new search query (`query`) optimized for the **second hop** of a multi-hop retrieval system. The original user question is typically complex and requires information from multiple documents to answer. The first hop query is the original question used to retrieve an initial set of documents. Your goal is to generate a **second hop query** that retrieves *additional relevant documents* that were *not* found in the first hop but are necessary to answer the original question completely.

Detailed task instructions and hints:

1. **Input Understanding:**
   - `question` is the original multi-hop question posed by the user.
   - `summary_1` is a concise summary of information from a document retrieved in the first hop, which partially addresses the question.

2. **Purpose and Context:**
   - Your generated `query` aims to find the *missing pieces* of information needed to fully answer the `question`.
   - The multi-hop retrieval system works in stages:
     - First hop: The original question returns some documents.
     - Second hop: Your query must help retrieve any *other relevant documents* NOT found in the first hop that hold complementary or broader context necessary for final answer extraction.

3. **Key Observations from Examples and Feedback:**
   - First-hop documents often cover one entity or aspect in the question.
   - Remaining relevant documents often involve connected or higher-level concepts mentioned in `summary_1` but not explicitly asked in the original question.
   - The `query` should be formulated to explicitly target these *missing*, but logically linked, documents.
   - Avoid merely paraphrasing the original question or restating known facts from `summary_1`.
   - Instead, infer what broader or related entities/concepts might provide the crucial missing information.
   - For example, if `summary_1` describes a population for a small civil parish, but the question wants total population of the wider region, your `query` should target that wider region (e.g., "Madeira archipelago population in 2011").
   - Similarly, if `summary_1` covers a song and the question wants the album it came from, but first hop got song-level documents, your query should retrieve documents about the album itself.

4. **How to Build the Query:**
   - Identify the entities or topics mentioned in `summary_1` that appear related but different from first-hop documents.
   - Reframe the query to explicitly mention these broader or related entities connected to the original question.
   - Include relevant key context from the question to maintain specificity, but shift focus to the missing piece.
   - The goal is to retrieve documents that link or complement what was retrieved initially.

5. **Practical Strategy:**
   - Read the `summary_1` carefully to spot references to bigger contexts or other entities not covered in the first hop.
   - Ask yourself, "What entity or aspect does this summary hint at that could answer the original question but was not found yet?"
   - Formulate a precise, focused factual query targeting that entity or concept to retrieve the missing documents.

6. **Output:**
   - Produce only the field `query` as a clear, concise question or keyword phrase designed for efficient retrieval of **second-hop documents**.
   - Ensure the query relates logically to the original question while targeting the broader or complementary knowledge identified in `summary_1`.
   - Do **not** include the original question or simply rephrase it.
   - Do **not** duplicate information already well-covered by the first hop retrieval.

By following these principles, you will help the multi-hop retrieval system find all necessary documents to answer the multi-faceted original question completely.

<mark>[HotpotQA Prompt End]</mark>
</details>
    <!-- </td> -->
    </td>
    <td width="48%" valign="top">
      <img src="https://raw.githubusercontent.com/gepa-ai/gepa/refs/heads/main/assets/aime_prompt.png" alt="AIME Prompt" width="2500">
      <details>
<summary><mark>Click to view full AIME prompt</mark></summary>

<mark>[AIME Prompt Begin]</mark>

You will be given one math problem as plain text under a key like "problem." Your job is to solve it correctly and return:

- reasoning: a concise, logically ordered solution that uses identities/structure to avoid brute force, ends with a quick verification.
- answer: the final requested number/expression only (no extra words).

Formatting:
- Use exactly two top-level fields named "reasoning" and "answer."
- Keep reasoning succinct but complete. Bullet points are fine.
- The answer field must contain only the final value requested (e.g., 227, 585, 601).

General problem-solving guidance:
- Parse the problem type (e.g., base representation, intersecting families of subsets, avoiding arithmetic progressions, symmetric sums with constraints, ordered tuples counting).
- Always enforce domain constraints (e.g., base-b digits in 0..b−1; no leading zero for base-10 "three-digit"; ordered vs unordered families; strict increase conditions in sequences).
- Use algebraic identities and modular arithmetic to reduce the search space; prefer structural arguments over naive enumeration.
- For "greatest/least" questions, derive tight bounds and give a construction that attains them.

Domain-specific strategies and pitfalls (learned from typical contest problems and prior feedback):

1) Base-conversion/digit rearrangement:
- Translate positional notation correctly: in base b, (a b c)_b = a·b^2 + b·b + c; in base 10: abc = 100a + 10b + c.
- Enforce digit ranges strictly (e.g., in base 9, digits ∈ {0,…,8}; if also a is a base-10 leading digit, then a ∈ {1,…,8}).
- Set up equality and simplify. Use modular constraints to prune:
  • Mod 9 often collapses coefficients; e.g., 99a = 71b + 8c ⇒ mod 9 gives b + c ≡ 0 (mod 9).
  • Mod 8: 99 ≡ 3, 71 ≡ 7 ⇒ 3a ≡ 7b (mod 8) ⇒ b ≡ −3a (mod 8).
- Solve within digit bounds and verify numerically.

2) Palindromes across bases:
- Bound the base length by magnitude (e.g., n < 1000 ⇒ octal has 3–4 digits).
- Characterize palindromes:
  • 3-digit octal: (A B A)_8 = 65A + 8B.
  • 4-digit octal: (A B B A)_8 = 513A + 72B (with A ≥ 1).
- Enumerate small parameter ranges and test the other-base palindrome constraint. For "greatest", check candidates in descending order with justification.

3) Symmetric sums with a + b + c fixed (ordered triples of nonnegative integers):
- Use identities to compress expressions:
  S = ab(a + b) + bc(b + c) + ca(c + a) = (a + b + c)(ab + bc + ca) − 3abc.
- With a + b + c known (e.g., 300), convert the given sum into a relation among ab + bc + ca and abc.
- Use the shift a = A + x etc. to isolate a product like (a−A)(b−A)(c−A) and deduce factorization constraints, enabling clean counting.
- Count ordered solutions carefully; include/exclude symmetric/degenerate cases precisel