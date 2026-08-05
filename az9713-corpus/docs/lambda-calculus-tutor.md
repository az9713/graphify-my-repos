---
repo: lambda-calculus-tutor
description: Interactive lambda calculus learning tool — step-by-step reductions, JS compiler, type inference
language: TypeScript
stars: 0
forks: 0
created: 2026-03-07
updated: 2026-03-07
topics: 
is_fork: False
kb: 740
---

# lambda-calculus-tutor
# Lambda Playground

An interactive lambda calculus learning tool for CS students. Type expressions, watch step-by-step reductions, compile to JavaScript, and infer types — all in the browser.

https://github.com/user-attachments/assets/f2d549e1-89cc-4aaa-9f21-31122f45520f

> **Type `\` (backslash) and it automatically converts to `λ` (Greek lambda).**

## Getting Started

```bash
npm install
npm run dev
```

Open `http://localhost:5173` in your browser.

## Typing Lambda Expressions

**Type `\` (backslash) and it automatically converts to `λ` (Greek lambda).**

For example, type `\x. x` and it becomes `λx. x` — the identity function.

You can also:
- Click the **λ** button below the editor to insert the lambda symbol
- Click the **→** button for the arrow symbol
- Press **Ctrl+Enter** to reduce the expression

### Syntax

| Syntax | Meaning | Example |
|--------|---------|---------|
| `λx. body` or `\x. body` | Lambda abstraction | `λx. x` (identity) |
| `f x` | Application | `(λx. x) y` → `y` |
| `let N = e in body` | Named definition | `let TRUE = λx. λy. x in TRUE a b` |
| `(expr)` | Grouping | `(λx. x) (λy. y)` |

Application is left-associative: `f a b` means `(f a) b`.

## Reduction Strategies

The strategy picker in the header controls which redex (reducible expression) gets reduced next.

### Normal Order (default)
Reduces the **leftmost, outermost** redex first. Reduces under lambdas. Always finds the normal form if one exists (Church-Rosser theorem). Best for exploration.

### Applicative Order
Reduces the **leftmost, innermost** redex first. Reduces under lambdas. Evaluates arguments before applying functions. May diverge even when a normal form exists.

### Call-by-Value (CBV)
Like Applicative Order, but **never reduces under lambdas**. Arguments are evaluated to values before substitution. This is how **JavaScript**, **Python**, and most languages work.

### Call-by-Name (CBN)
Substitutes arguments **unevaluated** and **never reduces under lambdas**. Finds weak head normal form. This is how **Haskell** works (without sharing/memoization).

## Reduction Rules

Each step in the reduction trace is labeled with a rule:

- **β (beta)** — Function application: `(λx. body) arg` → `body[x := arg]`
- **η (eta)** — Simplification: `λx. f x` → `f` (when `x` is not free in `f`)
- **δ (delta)** — Let expansion: `let X = v in body` → `body[X := v]`

## Features

- **Step-by-step reduction** with play/pause/back/forward and speed control
- **4 reduction strategies**: Normal Order, Applicative Order, Call-by-Value, Call-by-Name
- **Standard Library**: 21 Church-encoded combinators (booleans, numerals, arithmetic, pairs, Y combinator)
- **6 interactive tutorials** with 22 guided steps
- **Lambda-to-JavaScript compiler** with Church numeral/boolean detection
- **Hindley-Milner type inference** (Algorithm W)
- **Auto-replace**: type `\` for `λ` — no special keyboard needed

## Standard Library

Click any entry in the Library sidebar tab to load its example.

| Category | Names |
|----------|-------|
| Booleans | TRUE, FALSE, AND, OR, NOT, IF |
| Numerals | ZERO, ONE, TWO, THREE, FOUR, FIVE |
| Arithmetic | SUCC, ADD, MUL, PRED, ISZERO |
| Pairs | PAIR, FST, SND |
| Recursion | Y |

## Reference Traces

The `docs/reductions/` directory contains step-by-step reduction traces for all standard library examples. These traces use the same reduction engine as the interactive app, so they are always in sync.

## Tests

```bash
npm test
```

80 tests covering parser, reducer, stepper, compiler, and type checker.

## Acknowledgements

- **[Grok](https://grok.com/)** for the original idea as one of its lambda calculus project suggestions
- **[Claude Code](https://claude.ai/claude-code)** powered by Opus 4.6 for implementation and documentation
