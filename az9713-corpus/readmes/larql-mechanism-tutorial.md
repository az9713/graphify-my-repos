# larql + the-mechanism — a documentation deep dive

This repository is a **guided tour of two connected projects** and the documentation suite that ties them together:

- **[the-mechanism](the-mechanism/)** — a Python research artifact that *empirically proves*, on Gemma-3-4B, how a transformer stores facts: as **addressable key→value slots, read by lookup — not by de-mixing a packed channel.**
- **[larql](larql/)** — a Rust platform that turns that proof into a *product*: it decompiles a transformer into a queryable **vindex** and gives you **LQL** to browse, infer over, and edit a model's knowledge, without retraining and (for browsing) without a GPU. *The model IS the database.*

They are two halves of one idea. **the-mechanism is the proof; larql is the product built on it.**

> **Provenance.** Both `larql/` and `the-mechanism/` originate from
> [chrishayuk/larql](https://github.com/chrishayuk/larql) and
> [chrishayuk/the-mechanism](https://github.com/chrishayuk/the-mechanism).
> This repository bundles them with a new, purpose-built documentation suite so
> the connection between the two can be read in one place.

---

## The journey

This repo is the output of a deep dive that asked a simple question: *how do these two codebases relate, and what is the minimal set of docs that explains both?*

1. **Read both codebases.** `larql` is a mature 17-crate Rust workspace; `the-mechanism` is ten self-contained Python "captures" that each prove one claim about Gemma-3-4B.
2. **Found the connection.** The two converged on the *same architecture independently* — and they cite each other in source. `the-mechanism/native.py` annotates its method as *"(This is LARQL MODE COMPOSE.)"*; larql's `fleet-routing-extensions.md` cites `the-mechanism/address.py` and `wall.py` by path. They share a model (Gemma-3-4B), a layer map (the fact band ≈ L23–28), a name ("Lazarus" / LQL), and an experiment lineage (fleet E10–E17 ↔ larql FR1–FR4).
3. **Wrote a minimal, high-signal documentation suite** — one doc per load-bearing idea, no stubs, every number traced to a real measured output. 15 files in three sets, instead of sprawling per-file coverage.

---

## Where to start

**→ Begin at the suite hub: [`docs/index.md`](docs/index.md).** One sentence: *because a transformer **addresses** its memory instead of **de-mixing** it, larql can extract that memory into an index, query it, and edit it — and the-mechanism is the proof that this is what the model actually does.*

The documentation is organised in three sets:

| Set | Entry point | What it covers |
|---|---|---|
| **the-mechanism** (the proof) | [the-mechanism/docs/index.md](the-mechanism/docs/index.md) | Ten captures proving "addressing, not de-mixing," with an evidence table of measured numbers. |
| **larql** (the product) | [larql/docs/index.md](larql/docs/index.md) | The vindex format, LQL, the 17-crate architecture, inference (WalkFfn), routing (FR1–FR4), and editing. |
| **The bridge** (the connection) | [docs/index.md](docs/index.md) | [The addressing thesis](docs/the-addressing-thesis.md) and [mechanism → larql](docs/mechanism-to-larql.md) — the proof→product mapping and shared lineage. |

### Suggested reading order

1. [the-mechanism: the thesis](the-mechanism/docs/the-thesis.md) — the claim and its evidence table.
2. [The addressing thesis](docs/the-addressing-thesis.md) — why that proof makes the product *possible*, not just faster.
3. [larql: what is it?](larql/docs/onboarding/what-is-this.md) → [quickstart](larql/docs/onboarding/quickstart.md) — the product, hands-on.
4. [Mechanism → larql](docs/mechanism-to-larql.md) — the full correspondence, once you know both sides.

---

## Repository layout

```
.
├── README.md                  ← you are here
├── docs/                      ← the bridge: proof ↔ product
│   ├── index.md
│   ├── the-addressing-thesis.md
│   └── mechanism-to-larql.md
├── the-mechanism/             ← the proof (Python, Gemma-3-4B captures)
│   └── docs/                  ← paper-style: thesis, captures, reproduce, visuals
└── larql/                     ← the product (Rust: vindex + LQL)
    └── docs/                  ← onboarding layer + existing specs/ADRs
```

---

## Running the code

- **the-mechanism** — `python3 the-mechanism/mechanism.py all`. The CPU captures (`pack`, `ladder`, `ffn`) run anywhere; the Gemma captures need Apple Silicon + MLX. See [reproduce.md](the-mechanism/docs/reproduce.md).
- **larql** — `cargo build --release` in `larql/`, then `larql extract …` / `larql lql …`. See the [quickstart](larql/docs/onboarding/quickstart.md).

## License

`larql/` and `the-mechanism/` retain their upstream licenses (Apache-2.0). The documentation suite added here is provided under the same terms.
