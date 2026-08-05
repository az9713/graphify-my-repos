# Lagrangian Compiler

**Where compiler theory meets classical mechanics.**

This project applies compiler construction techniques -- parsing, static analysis, dead code elimination, constant folding -- to a problem from physics: automatically detecting the symmetries of a mechanical system and deriving its conservation laws.

You give it a Lagrangian (the fundamental equation describing a physical system). It returns conserved quantities, simplified equations, and phase portraits -- all derived automatically, the way a compiler optimizes source code.

```
                    Compiler                          Physics
                    ────────                          ───────
    Parsing         text → AST                        "L = 0.5*m*qdot1**2" → SymPy expression
    Static analysis liveness, constant detection      symmetry detection (Noether's theorem)
    Optimization    dead code elimination,             eliminate cyclic coordinates,
                    constant folding                   substitute conserved momenta
    Code generation emit instructions                  derive equations of motion
```

## The Core Idea

A Lagrangian `L = T - V` (kinetic minus potential energy) encodes all the physics of a system. This tool treats it as *source code* and runs compiler-style passes on it:

1. **Liveness analysis** checks which coordinates actually appear in L. A coordinate that doesn't appear (like position in `L = 0.5*m*v^2`) is *dead code* -- it corresponds to a symmetry of the system.

2. **Noether's theorem** is the physics equivalent of semantic analysis: every dead coordinate produces a *conserved quantity* (momentum, angular momentum, energy). These are compile-time constants.

3. **The optimizer** eliminates dead coordinates and folds conserved quantities as constants -- exactly like dead code elimination and constant folding in a compiler. A 2D orbital mechanics problem automatically reduces to 1D.

4. **Code generation** applies the Euler-Lagrange equation to produce the equations of motion -- the "machine code" that governs the system's evolution.

The result: conservation laws that took physicists centuries to discover (Newton's first law, Kepler's equal-areas law, angular momentum conservation) are derived *automatically* from the structure of the Lagrangian, using the same techniques a compiler uses to optimize a program.

## Quick Start

```bash
pip install sympy numpy scipy matplotlib
python -m src.main central_force
```

```
[PARSE] Lagrangian: L = 0.5*m*(qdot1**2 + q1**2*qdot2**2) - V(q1)
  Coordinates: [q1, q2]

[PASS] Running symmetry detection passes...
  [+] Translational symmetry: q2 is cyclic (dL/dq2 = 0)
  [+] Time-translation symmetry: dL/dt = 0 (energy conserved)

[NOETHER] Conserved quantities:
  p_q2 = m*q1**2*qdot2          <- angular momentum (Kepler's law)
  H = 0.5*m*qdot1**2 + V(q1)   <- total energy

[REWRITE] Reduced Lagrangian: L = 0.5*m*qdot1**2 + p_q2**2/(2*m*q1**2) - V(q1)
  Remaining coords: [q1]        <- 2D problem reduced to 1D!
```

A 2D orbital mechanics problem compiled down to a 1D equation. The angular coordinate was detected as dead code, angular momentum was derived as a conserved constant, and the system was rewritten with an effective potential -- all automatically.

## Try Your Own Lagrangian

```bash
# Particle in gravity
python -m src.main "L = 0.5*m*qdot1**2 - m*g*q1"

# Quartic oscillator
python -m src.main "L = 0.5*m*qdot1**2 - a*q1**4"

# Charged particle in a magnetic field
python -m src.main "L = 0.5*m*(qdot1**2 + qdot2**2) + B*(q1*qdot2 - q2*qdot1)"
```

## Built-in Examples

| Command | System | What the compiler finds |
|---------|--------|------------------------|
| `python -m src.main free_particle` | Free particle | Full reduction to 0 DOF -- momentum + energy |
| `python -m src.main spring_mass` | Harmonic oscillator | No reduction -- all variables live |
| `python -m src.main central_force` | Orbital mechanics | 2D to 1D reduction -- angular momentum |
| `python -m src.main free_2d` | Free 2D particle | All 5 symmetry types -- maximum symmetry |
| `python -m src.main double_pendulum` | Chaotic pendulum | Only energy -- irreducible computation |

Run with numerical simulation and plots:

```bash
python examples/central_force.py
python examples/double_pendulum.py
```

## Architecture

```
Input: "L = 0.5*m*(qdot1**2 + q1**2*qdot2**2) - V(q1)"
  |
  v
Parser (src/parser.py)              --- text -> SymPy AST + symbol classification
  |
  v
Symmetry Passes (src/passes/)      --- static analysis: 4 independent passes
  |- translation.py                     liveness check: dL/dq == 0?
  |- time.py                            constant check: dL/dt == 0?
  |- rotation.py                        infinitesimal rotation invariance
  |- scaling.py                         homogeneity analysis
  |
  v
Noether Pass (src/noether.py)       --- symmetry -> conserved quantity
  |
  v
Rewriter (src/rewriter.py)         --- dead code elimination + constant folding
  |
  v
EOM Generator (src/eom.py)         --- Euler-Lagrange -> equations of motion
  |
  v
Visualizer (src/viz.py)            --- numerical integration + phase portraits
```

## Tests

35 tests covering every pipeline stage:

```bash
python -m pytest tests/ -v
```

## How Compiler Concepts Map to Physics

| Compiler concept | Physics equivalent | Example |
|-----------------|-------------------|---------|
| Dead code (unused variable) | Cyclic coordinate (symmetry) | Angle in central force |
| Liveness analysis | `dL/dq == 0` check | Translation pass |
| Constant folding | Conserved quantity substitution | `qdot = p/(m*r^2)` |
| Dead code elimination | Coordinate reduction | Remove angle from orbit problem |
| Constant propagation | Conservation law | `p = m*v = const` |
| Program reduces to constant | Fully integrable system | Free particle: 0 DOF remain |
| Irreducible computation | Chaos | Double pendulum: no reduction possible |

## Documentation

| Document | Description |
|----------|-------------|
| [QUICKSTART](docs/QUICKSTART.md) | Setup and first runs |
| [THEORY](docs/THEORY.md) | Physics, math, and CS background |
| [DSL_REFERENCE](docs/DSL_REFERENCE.md) | Input language spec |
| [API_REFERENCE](docs/API_REFERENCE.md) | Module-by-module Python API |
| [EXAMPLES](docs/EXAMPLES.md) | All 5 worked examples |
| [COMPILER_MEETS_PHYSICS](docs/COMPILER_MEETS_PHYSICS.md) | Test-by-test compiler-to-physics mapping |

### Per-Example Deep Dives

| Document | Key concept |
|----------|-------------|
| [Free Particle](docs/examples/FREE_PARTICLE.md) | Full reduction, dead code elimination |
| [Spring-Mass](docs/examples/SPRING_MASS.md) | Live variables block optimization |
| [Central Force](docs/examples/CENTRAL_FORCE.md) | 2D to 1D reduction, effective potential |
| [Free 2D](docs/examples/FREE_2D.md) | All 5 symmetries, angular momentum |
| [Double Pendulum](docs/examples/DOUBLE_PENDULUM.md) | Chaos, irreducible computation |

## Requirements

- Python 3.10+
- SymPy, NumPy, SciPy, Matplotlib

```bash
pip install sympy numpy scipy matplotlib
```

## Acknowledgements

- Original idea proposed by [Grok](https://grok.com/)
- Idea refinement, implementation, and documentation powered by [Claude Code](https://claude.ai/claude-code) (Opus 4.6)

## License

MIT
