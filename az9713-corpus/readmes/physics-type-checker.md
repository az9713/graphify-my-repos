# Type Systems as Conservation Laws

A toy project exploring how computer science concepts — **type systems**,
**linear types**, and the **Curry-Howard correspondence** — can be adopted
to solve problems in physics domains.

The core idea: what if **type-checking a program** could **prove a physical
law**? We build a small language for describing 3D particle collisions, and
a type checker that verifies conservation of momentum, energy, and mass.
A well-typed program is a proof that the described system obeys physics.

## Motivation

Physics and computer science share deep structural parallels that are rarely
explored in practical tools:

| Physics | Computer Science |
|---------|-----------------|
| Conservation law (momentum, energy) | Type constraint |
| A valid collision configuration | A well-typed program |
| "No particle created or destroyed" | Linear type discipline |
| Verifying a conservation claim | Type checking |

This project makes these parallels concrete and executable. It is a study in
how formal methods from programming language theory — originally designed for
software correctness — map naturally onto physical law verification.

## Quick Start

```bash
# Clone and install
git clone https://github.com/your-username/physics_cs_grok.git
cd physics_cs_grok
pip install -e ".[dev]"

# Type-check a collision program
python -m conservation check examples/elastic_2body.cons

# Run the test suite (393 tests)
pytest
```

**Requirements:** Python 3.10+, no external dependencies for the core.

## The Language

Programs are written in `.cons` files. You declare particles with mass and
3D velocity, then describe collisions. The type checker verifies that
conservation laws hold across the `->` arrow:

```python
# Two billiard balls — classic elastic collision
particle ball_a:  mass = 1.0, velocity = (2.0, 0.0, 0.0)
particle ball_b:  mass = 1.0, velocity = (0.0, 0.0, 0.0)

particle ball_a': mass = 1.0, velocity = (0.0, 0.0, 0.0)
particle ball_b': mass = 1.0, velocity = (2.0, 0.0, 0.0)

collide ball_a, ball_b -> ball_a', ball_b'
```

```
$ python -m conservation check examples/elastic_2body.cons

  Collision (line 10, elastic): OK
    Momentum: Vec3(2.0, 0.0, 0.0) -> Vec3(2.0, 0.0, 0.0)
    KE:       2 -> 2

WELL-TYPED: Conservation proof verified.
```

The user specifies **all** particle states. The checker only **verifies** —
it is a proof checker, not a proof search engine.

## How CS Meets Physics

### The Type Hierarchy

Each layer of the type system corresponds to a physical concept:

```
ParticleType(m, v)              <-- one per particle declaration
     |                              (mass + velocity = the particle's "type")
     | momentum = m * v
     | KE = 0.5 * m * |v|^2
     v
SystemType.synthesize(...)      <-- one per collision side
     |                              (aggregate: total momentum, KE, mass)
     | total_momentum = sum(p_i)
     | total_KE = sum(KE_i)
     | total_mass = sum(m_i)
     v
CollisionType(before, after, mode)
     |                              (the "type" of a collide statement)
     | check: before.p == after.p       [P-CONS]  momentum conservation
     | check: before.KE == after.KE     [E-CONS]  energy conservation
     | check: before.m == after.m       [M-CONS]  mass conservation
     v
CollisionJudgment(OK / FAIL)    <-- the typing judgment: did the proof step hold?
```

### Three-Pass Type Checker

```
Source (.cons)
     |
     v
  +-------+     +--------+     +--------+
  | Lexer | --> | Parser | --> |  AST   |
  +-------+     +--------+     +--------+
                                    |
                                    v
                          +------------------+
                          |  Type Checker    |
                          |  (3-pass)        |
                          |                  |
                          |  Pass 1: DECL    |  Build the type environment
                          |  Gamma = {}      |  (map: name -> ParticleType)
                          |  for each decl:  |
                          |    name -> PT    |
                          |                  |
                          |  Pass 2: COLLIDE |  Synthesize SystemTypes,
                          |  for each stmt:  |  check conservation premises
                          |    synthesize    |
                          |    SystemTypes   |
                          |    check premises|
                          |                  |
                          |  Pass 3: LINEAR  |  Every particle used exactly
                          |  global check    |  once (no duplication/discard)
                          +------------------+
                                    |
                                    v
                          +------------------+
                          | ProgramJudgment  |  The derivation tree —
                          |  .decl_judgments |  a structured proof certificate
                          |  .collision_     |
                          |    judgments     |
                          |  .final_linearity|
                          |  .valid          |
                          +------------------+
```

### Linear Types = Conservation of Matter

In CS, a **linear type system** requires every resource to be used exactly
once — no duplication, no discard. This maps directly to physics:

- A particle **cannot appear on both sides** of a collision (no cloning matter)
- A particle **cannot be declared and never used** (no silently dropping matter)
- Each particle participates in **exactly one collision**

When a particle is declared but unused, the type checker rejects the program —
just as a linear type system rejects code that leaks a resource:

```
$ python -m conservation check examples/missing_particle.cons

  Collision (line 10, elastic): OK
    Momentum: Vec3(0.0, 0.0, 0.0) -> Vec3(0.0, 0.0, 0.0)
    KE:       1 -> 1
  Linearity error for 'c': declared but never used in a collision

TYPE ERROR: 1 violation(s) found.
```

The collision itself is fine — but particle `c` was declared and never
accounted for. The conservation "proof" is incomplete.

### Multi-Collision Chains

Particles produced by one collision can be consumed by a later one,
enabling sequential reasoning — like function composition in a linear
lambda calculus:

```python
# Newton's cradle: momentum transfers through a chain
particle a:   mass = 1.0, velocity = (2.0, 0.0, 0.0)
particle b:   mass = 1.0, velocity = (0.0, 0.0, 0.0)
particle c:   mass = 1.0, velocity = (0.0, 0.0, 0.0)
particle a':  mass = 1.0, velocity = (0.0, 0.0, 0.0)
particle b':  mass = 1.0, velocity = (2.0, 0.0, 0.0)
particle b'': mass = 1.0, velocity = (0.0, 0.0, 0.0)
particle c':  mass = 1.0, velocity = (2.0, 0.0, 0.0)

collide a, b -> a', b'           # step 1: a hits b
collide b', c -> b'', c'         # step 2: b' hits c
```

The linearity tracker handles this naturally:

```
  Name  | Produced by  | Consumed by  | Status
  ------|--------------|--------------|--------
  a     | (initial)    | collision 1  | OK
  b     | (initial)    | collision 1  | OK
  b'    | collision 1  | collision 2  | OK  (chain link!)
  c     | (initial)    | collision 2  | OK
  a'    | collision 1  | (final)      | OK
  b''   | collision 2  | (final)      | OK
  c'    | collision 2  | (final)      | OK
```

### Inelastic Collisions

The `inelastic` keyword switches the energy check from strict equality to
an inequality — kinetic energy may decrease (converted to heat) but cannot
increase:

```
$ python -m conservation check examples/inelastic.cons

  Collision (line 11, inelastic): OK
    Momentum: Vec3(4.0, 0.0, 0.0) -> Vec3(4.0, 0.0, 0.0)
    KE:       10 -> 2
    Heat loss: 8

WELL-TYPED: Conservation proof verified.
```

### Type Errors = Physics Violations

When conservation laws are violated, the type checker reports exactly what
went wrong:

```
$ python -m conservation check examples/bad_momentum.cons

  Collision (line 13, elastic): FAIL
    Momentum: Vec3(4.0, 2.0, 0.0) -> Vec3(4.0, 0.0, 0.0)
    KE:       11 -> 4
    ERROR: Momentum violation: delta=Vec3(0.0, 2.0, 0.0)
    ERROR: Energy violation: KE_before=11, KE_after=4, delta=7

TYPE ERROR: 2 violation(s) found.
```

## The Curry-Howard Reading

The [Curry-Howard correspondence](https://en.wikipedia.org/wiki/Curry%E2%80%93Howard_correspondence)
is a fundamental result establishing a structural equivalence between logical
proofs and well-typed programs. In our domain:

| Logic / Physics | Programming |
|-----------------|-------------|
| Proposition (conservation law) | Type |
| Proof (valid collision) | Well-typed program |
| Assumption (particle exists) | Variable binding (`particle` declaration) |
| Proof step (collision conserves) | `collide` statement |
| Linear logic (use-once) | Linear type discipline |
| Proof certificate | `ProgramJudgment` (derivation tree) |

A well-typed `.cons` program **is** a proof. The `ProgramJudgment` returned
by the type checker is the proof certificate — a fully explicit derivation
tree that can be inspected with `--show-derivation`.

## Project Structure

```
physics_cs_grok/
├── src/conservation/          # Core implementation (zero dependencies)
│   ├── types.py               #   ParticleType, SystemType, CollisionType
│   ├── environment.py         #   TypeEnv (Gamma), LinearityCtx
│   ├── judgments.py            #   DeclJudgment, CollisionJudgment, ProgramJudgment
│   ├── typechecker.py         #   Three-pass type checker
│   ├── vectors.py             #   Vec3 dataclass
│   ├── physics.py             #   Particle (bridge to ParticleType)
│   ├── lexer.py               #   Tokenizer
│   ├── parser.py              #   Recursive descent parser
│   ├── ast_nodes.py           #   AST node dataclasses
│   ├── tolerance.py           #   Float comparison helpers
│   ├── errors.py              #   Error types
│   └── runner.py              #   CLI entry point
├── examples/                  # .cons programs (valid and invalid)
│   ├── elastic_2body.cons     #   Basic 2-body elastic collision
│   ├── elastic_3body.cons     #   3-body collision in 3D
│   ├── inelastic.cons         #   Perfectly inelastic (balls stick)
│   ├── chain.cons             #   Multi-collision Newton's cradle
│   ├── decay.cons             #   1-to-2 particle split
│   ├── bad_momentum.cons      #   TYPE ERROR: momentum violated
│   ├── bad_energy.cons        #   TYPE ERROR: energy violated
│   ├── bad_mass.cons          #   TYPE ERROR: mass violated
│   ├── duplicate_particle.cons#   TYPE ERROR: linearity (duplication)
│   └── missing_particle.cons  #   TYPE ERROR: linearity (unused)
├── tests/                     # 393 tests
├── output/                    # Annotated checker output for each example
├── viz/                       # Manim 3D visualization (optional)
│   ├── collision_scene.py     #   Main ThreeDScene
│   ├── particle_mobjects.py   #   Particle spheres, arrows, labels
│   ├── type_overlays.py       #   HUD, conservation check displays
│   └── render.py              #   CLI: .cons -> MP4
└── docs/
    ├── theory.md              #   Physics + CS background, architecture
    ├── formal.md              #   Formal type rules (inference notation)
    └── tutorial.md            #   Usage guide with examples
```

## CLI Reference

```bash
# Basic type checking
python -m conservation check examples/elastic_2body.cons

# Show the type environment (Gamma) and SystemTypes
python -m conservation check examples/elastic_2body.cons --show-types

# Show the full derivation tree (proof certificate)
python -m conservation check examples/elastic_2body.cons --show-derivation --verbose

# Custom tolerance
python -m conservation check examples/elastic_2body.cons --abs-tol 1e-10 --rel-tol 1e-8
```

## Python API

```python
from conservation import parse, typecheck_derivation

program = parse(open("examples/elastic_2body.cons").read())
judgment = typecheck_derivation(program)

# Inspect the type environment
for dj in judgment.decl_judgments:
    print(f"{dj.name} : {dj.particle_type}")

# Inspect a collision judgment
cj = judgment.collision_judgments[0]
print(f"Before: {cj.collision_type.before}")
print(f"After:  {cj.collision_type.after}")
print(f"Momentum OK: {cj.momentum_check.satisfied}")
print(f"Energy OK:   {cj.energy_check.satisfied}")

# Overall verdict
print(f"Well-typed: {judgment.valid}")
```

## Documentation

| Document | Description |
|----------|-------------|
| [docs/theory.md](docs/theory.md) | Physics and CS background, architecture, type system overview |
| [docs/formal.md](docs/formal.md) | Formal type rules in inference notation, metatheory, implementation correspondence |
| [docs/tutorial.md](docs/tutorial.md) | Usage guide with worked examples |
| [output/](output/) | Annotated checker output for every example, showing the type system behind the scenes |

## Acknowledgements

- **Grok** proposed the original idea.
- **Claude Code** (powered by Opus 4.6) was used to refine, implement and
  create documentations.
- **GPT-5.3-Codex** was used for a 360-degree critique
  ([docs/critique.md](docs/critique.md)).

## License

This is an educational toy project. Use it however you like.
