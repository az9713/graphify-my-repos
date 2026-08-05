---
repo: superoptimizer-foundry
description: Superoptimizer for a pinned 8-bit ISA: exhaustive enumeration proves shortest-program floors, LLM agents search above them, every result verified on all inputs
language: HTML
stars: 0
forks: 0
created: 2026-07-28
updated: 2026-07-29
topics: 
is_fork: False
kb: 122
---

# superoptimizer-foundry
# Superoptimizer Foundry

Search for the shortest correct instruction sequence for small integer
operations, and prove when nothing shorter exists.

Every result is checked by running a candidate against a reference on **every
possible input** — 256 combinations at 8 bits with one input, 65,536 with two.
Not a sample. There is no judgement anywhere in the correctness loop.

## Why both halves matter

Two search methods, deliberately paired:

* **Exhaustive enumeration** tries every possible program up to a short length.
  When it finishes it has established a fact: either it found the shortest
  program, or it proved none that short exists.
* **Language-model agents** propose candidates far beyond the length where
  enumeration dies, repairing each failure from the specific counterexample the
  oracle hands back.

Enumeration proves things but cannot reach far. Agents reach far but prove
nothing. Together, enumeration sets a certified floor and the agents explore
above it.

## Documents

* [`CONTEXT.md`](CONTEXT.md) — full project context: objective, implementation,
  results and how to interpret them, outstanding issues.
* [`superoptimizer-foundry-plan.html`](superoptimizer-foundry-plan.html) — the
  original plan: phases, the three ways to fake a result, autonomy analysis.
* [`SPEC.md`](SPEC.md) — the pinned instruction set every claim is relative to.
* [`HANDOFF.md`](HANDOFF.md) — live resume point for development.

This is why the project cannot come back empty-handed. If the agents never beat
a published sequence, but enumeration has proved nothing shorter exists, then
the published sequence has been *proved optimal* — a stronger result than a win
on some obscure operation.

## Quick start

```
python test_isa.py        # evaluator self-check -- run this first
python test_oracle.py     # oracle self-check against known-good sequences
python verify.py --list   # the targets
python phase1.py 8 3      # exhaustive enumeration, ~6 minutes
python assemble.py        # build results/index.html
```

Check one candidate:

```
python verify.py abs --text "t0 = sar x, 7\nt1 = xor x, t0\nt2 = sub t1, t0\nret t2"
PASS  abs w=8  all 256 inputs agree  |  3 instructions, depth 3, weighted 3
```

Exit code 0 means correct on every input. Otherwise the output names an input
where it goes wrong:

```
FAIL  abs w=8  126 of 256 inputs disagree
      first divergence at x=0x82   got 0x82   expected 0x7e
```

## Files

| File | Role |
|---|---|
| `SPEC.md` | The pinned instruction set. Every claim is relative to this. |
| `isa.py` | Parser, evaluator, cost model |
| `refs.py` | Reference implementations — deliberately slow and obvious |
| `oracle.py` | Exhaustive equivalence checking |
| `bruteforce.py` | Phase 1 enumeration with observational-equivalence pruning |
| `phase1.py` | Phase 1 driver |
| `phase2_workflow.js` | Phase 2 agent search |
| `harvest.py` | Re-verifies agent claims from scratch — the trust boundary |
| `assemble.py` | Builds the results page, with a sanitation gate |
| `test_isa.py`, `test_oracle.py` | Self-checks. If these fail, nothing else means anything. |

## Things that are easy to get wrong

Recorded because each one cost real debugging time:

1. **Level accounting.** A program of length L ends in one operation whose
   operand subexpressions cost `i` and `j` with `i + j + 1 == L`. Building level
   L from "the newest level combined with everything" silently produces much
   longer programs mislabelled as short ones.
2. **Shift counts must resolve to literals.** Looking up a shift count by
   *value* can return a derived expression that happens to equal that constant,
   which then gets emitted as a register operand — illegal under the spec. Keep
   a separate map of literal positions.
3. **A two-input domain at 8 bits is 65,536 wide.** Multiplied by a pool of
   hundreds of thousands of vectors, that is tens of gigabytes. Two-input
   targets are enumerated at 4 bits and the claim is stated for 4 bits.
4. **The estimate is not the answer.** An early draft of the plan asserted that
   a broken absolute-value sequence would fail on 128 of 256 inputs — the
   obvious guess, since the bug only affects negatives. The real number is 126;
   two inputs agree by coincidence. Exhaustive checking caught it in seconds.
5. **Enumeration covers trees, not DAGs — and this bit us.** Pool entries are
   trees, so a parent is charged `cost(a) + cost(b) + 1`, which pays twice for a
   value used twice. Impossibility claims therefore only cover programs where
   every intermediate is used at most once. See below.

## The most useful thing that happened

Enumeration reported that no `is_pow2` program of length ≤ 3 existed. An agent
then found one:

```
t0 = sub x, 1
t1 = xor x, t0
t2 = ult t0, t1
```

Three instructions, verified on all 256 inputs, using only operations and
constants **inside** the space enumeration had searched. The impossibility claim
was false as stated.

The cause is limitation 5 above: `t0` is used twice. Written without reuse the
same computation needs four instructions, so the enumerator filed it at level 4
and never considered it at level 3 — while reporting level 3 as empty.

This is the whole argument for running both methods. Enumeration alone would
have published a false impossibility claim with total confidence. Agent search
alone would have found a good sequence with no idea whether it was optimal.
Each caught what the other structurally could not.

## Status

Phase 1 and Phase 2 complete; all claims restated as tree-shaped. **No claim of
beating any published sequence is made** — the baseline audit has not run.
