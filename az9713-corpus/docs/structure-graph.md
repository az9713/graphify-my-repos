---
repo: structure-graph
description: Graph theory applied to classical structural mechanics with interactive 3D visualizations
language: HTML
stars: 0
forks: 0
created: 2026-03-06
updated: 2026-03-06
topics: 
is_fork: False
kb: 1540
---

# structure-graph
# truss_graph

**Graph theory applied to classical structural mechanics — with interactive animated 3D visualizations.**

truss_graph is a Python package that bridges two worlds: **Newtonian mechanics** (forces, stiffness matrices, equilibrium) and **graph theory** (Laplacians, eigenvalues, min-cut, communities). It lets you build truss and frame structures, run structural analysis, and explore the results through rich, interactive HTML visualizations — all from Python.

```
┌─────────────────────────────────────────────────────────────┐
│                     truss_graph                              │
│                                                              │
│   Newtonian Mechanics  ←──── bridge ────→  Graph Theory      │
│   ─────────────────                        ────────────      │
│   F = ma                                   Laplacian L       │
│   K·u = F                                  Eigenvalues       │
│   Stiffness EA/L                           Edge weights      │
│   Structural failure                       Min-cut           │
│   Load sharing                             Communities       │
│   Torsion GJ/L                             Graph Laplacian   │
│                                                              │
│   Output: Interactive 3D HTML visualizations with             │
│   embedded explanations tying all four domains together       │
└─────────────────────────────────────────────────────────────┘
```

## Origin Story

This project started as a brainstorming session during a commute with **Grok**, exploring whether graph theory could be used to solve Newtonian mechanics problems. The transcript from that conversation was then read by **Claude** (powered by Opus 4.6), who launched a team of four research agents to fill in knowledge gaps across structural mechanics, graph Laplacians, sparse solvers, and torsion modeling. Claude Code subsequently implemented the first version of structure-graph — the full codebase, test suite, visualizations, and documentation.

The **Codex** desktop app (powered by GPT-5.3-Codex) was then asked to critique both the science and the implementation. Codex produced a deep-dive review with seven findings, including one critical correctness bug. Those findings were fed back into Claude Code for further assessment. Claude Code agreed to fix six out of seven, with justifications for each decision — the seventh (replacing `assert` with `ValueError`) was acknowledged but deferred as low-risk for an educational package.

See [`docs/codex/deep_dive_critique.md`](docs/codex/deep_dive_critique.md) for the full Codex critique and [`docs/claude-codex-response.md`](docs/claude-codex-response.md) for Claude's response and fix details.

## Visualization Gallery

Every analysis produces an interactive 3D HTML file. Here are six examples from the `output/` folder:

<table>
  <tr>
    <td align="center"><strong>Triangle Truss</strong><br>Static analysis with deformed shape<br><img src="docs/images/triangle_truss.png" width="380"></td>
    <td align="center"><strong>Warren Truss — Forces</strong><br>Member forces color-coded<br><img src="docs/images/warren_forces.png" width="380"></td>
  </tr>
  <tr>
    <td align="center"><strong>3D Tower</strong><br>Multi-story tower static analysis<br><img src="docs/images/tower_3d.png" width="380"></td>
    <td align="center"><strong>3D Bridge</strong><br>Bridge deck with gravity loads<br><img src="docs/images/bridge_3d.png" width="380"></td>
  </tr>
  <tr>
    <td align="center"><strong>Min-Cut Failure</strong><br>Graph-theoretic failure prediction<br><img src="docs/images/warren_min_cut.png" width="380"></td>
    <td align="center"><strong>Community Detection</strong><br>Load-sharing groups via Louvain<br><img src="docs/images/warren_communities.png" width="380"></td>
  </tr>
</table>

> Run the examples yourself to get fully interactive, rotatable 3D views with hover tooltips and explanation panels.

## Why Graph Theory for Structural Mechanics?

Classical structural analysis solves F=ma with stiffness matrices — powerful but opaque. Recasting the same problem as a graph unlocks a different toolkit with practical advantages:

- **Failure prediction without simulation.** Min-cut identifies the weakest set of members that would collapse the structure — directly from the graph topology and capacities, without running progressive failure simulations.
- **Structural robustness as a single number.** The Fiedler value (second-smallest Laplacian eigenvalue) quantifies how well-connected a structure is. A low value flags fragile designs before any load is applied.
- **Automatic load-sharing groups.** Community detection (Louvain) partitions the structure into subgroups that carry load semi-independently, revealing which zones are overloaded without manual inspection.
- **Fast approximate modal analysis.** The graph Laplacian eigenvalue problem (1 DOF/node) runs orders of magnitude faster than the full stiffness eigenvalue problem (6 DOF/node) and gives exact results for axial and torsional modes.
- **Topology-driven insight.** Graph metrics like edge connectivity, shortest paths, and centrality expose structural behavior that is invisible in the raw stiffness matrix — letting engineers reason about a structure's "shape" rather than its numbers.
- **Natural problem decomposition.** A structure IS a graph: joints are nodes, bars are edges, stiffness is edge weight. This mapping is not an analogy — it is mathematically exact for axial and torsional problems (F = k·Δx and T = κ·Δθ share the same Laplacian form).

## Quick Start

### Prerequisites

- **Python 3.10 or later** — [Download here](https://www.python.org/downloads/)
- **pip** — comes with Python (used to install packages)
- **A web browser** — Chrome, Firefox, Edge, or Safari (to view output)

### Installation

```bash
# 1. Clone or download this repository
# 2. Open a terminal and navigate to the project folder:
cd truss_graph

# 3. Install the package and all dependencies:
pip install -e ".[dev]"
```

This installs: `networkx`, `numpy`, `scipy`, `plotly`, `python-louvain`, `pytest`.

### Run Your First Example

```bash
python -m examples.triangle_truss
```

Open `output/triangle_truss.html` in your browser. You'll see a 3D interactive truss with force arrows, deformed shape, and a detailed explanation panel covering physics, structures, math, and graph theory.

### Run All Examples

```bash
python -m examples.triangle_truss
python -m examples.warren_truss
python -m examples.tower_3d
python -m examples.bridge_3d
python -m examples.newton_to_graph
```

All outputs go to the `output/` folder as self-contained HTML files. Open `output/educational/index.html` for the 7-lesson educational series.

### Run Tests

```bash
pytest tests/ -v
```

All 64 tests should pass.

## What This Project Does

| Feature | Physics Side | Graph Theory Side |
|---|---|---|
| **Static Analysis** | Solve Ku=F for displacements | — |
| **Modal Analysis** | Find natural frequencies & mode shapes | Eigenvalues of stiffness matrix |
| **Spectral Analysis** | — | Eigenvalues of graph Laplacian |
| **Failure Prediction** | Member capacities, progressive collapse | Max-flow / min-cut |
| **Community Detection** | Load-sharing groups | Louvain clustering on force-weighted graph |
| **Torsion Modeling** | GJ/L twist stiffness | Pure torsion IS a graph Laplacian problem |
| **Educational Bridge** | 7 interactive lessons | Shows the exact mapping between worlds |

## Output Files

Running all examples generates **26 interactive HTML files**:

| File | Description |
|---|---|
| `triangle_truss.html` | Simple triangle — static analysis |
| `warren_forces.html` | Warren truss — member forces color-coded |
| `warren_deformed.html` | Warren truss — deformed shape overlay |
| `warren_min_cut.html` | Warren truss — min-cut failure analysis |
| `warren_progressive.html` | Warren truss — progressive failure animation |
| `warren_communities.html` | Warren truss — community detection |
| `warren_load_paths.html` | Warren truss — primary load path |
| `tower_3d.html` | 3D tower — static analysis |
| `bridge_3d.html` | 3D bridge — static analysis |
| `mode_1-4_spectral.html` | Mode shape animations (4 files) |
| `spectral_summary.html` | Mode shape gallery |
| `min_cut.html` | Min-cut analysis |
| `progressive_failure.html` | Progressive failure animation |
| `communities.html` | Community detection |
| `load_paths.html` | Load path analysis |
| `educational/01-07_*.html` | 7 educational lessons (+ index) |

Every HTML file includes an explanation panel that ties together **physics**, **structures**, **mathematics**, and **graph theory**.

## Project Structure

```
truss_graph/
├── pyproject.toml              # Package config & dependencies
├── README.md                   # This file
├── CLAUDE.md                   # Development conventions
│
├── truss_graph/                # Main package
│   ├── __init__.py             # Public API exports
│   ├── structure.py            # Data model (nodes, elements, materials)
│   ├── stiffness.py            # Element stiffness matrices (6x6, 12x12)
│   ├── assembly.py             # Global matrix assembly (Direct Stiffness)
│   ├── solver.py               # Static & modal solvers
│   ├── spectral.py             # Graph Laplacian spectral analysis
│   ├── failure.py              # Max-flow/min-cut failure prediction
│   ├── communities.py          # Louvain community detection
│   ├── torsion.py              # 6-DOF torsion modeling
│   └── viz/                    # Visualization sub-package
│       ├── base.py             # 3D Plotly scene creation
│       ├── forces.py           # Force arrow (Cone) traces
│       ├── mode_shapes.py      # Mode shape animations
│       ├── failure.py          # Min-cut & progressive failure viz
│       ├── communities.py      # Community coloring & load paths
│       ├── educational.py      # 7 Newton-to-Graph lessons
│       ├── explanations.py     # Explanation content for all HTML
│       └── export.py           # HTML export with explanations
│
├── examples/                   # Runnable examples
│   ├── triangle_truss.py
│   ├── warren_truss.py
│   ├── tower_3d.py
│   ├── bridge_3d.py
│   └── newton_to_graph.py
│
├── tests/                      # Test suite (64 tests)
│   ├── conftest.py             # Shared fixtures
│   ├── test_stiffness.py
│   ├── test_assembly.py
│   ├── test_solver.py
│   ├── test_spectral.py
│   ├── test_failure.py
│   ├── test_communities.py
│   └── test_torsion.py
│
├── output/                     # Generated HTML visualizations
└── docs/                       # Documentation
    ├── ARCHITECTURE.md
    ├── DEVELOPER_GUIDE.md
    ├── USER_GUIDE.md
    ├── STUDY_PLAN.md
    ├── MATH_FOUNDATIONS.md
    ├── torsion_modeling_report.md
    ├── claude-codex-response.md
    └── codex/
        └── deep_dive_critique.md
```

## Documentation

- **[Architecture Guide](docs/ARCHITECTURE.md)** — System design, component diagrams, data flow
- **[Developer Guide](docs/DEVELOPER_GUIDE.md)** — Step-by-step guide for contributing code
- **[User Guide & Quick Start](docs/USER_GUIDE.md)** — 10+ hands-on use cases for beginners
- **[Study Plan](docs/STUDY_PLAN.md)** — Zero-to-hero learning path through theory + code
- **[Math Foundations](docs/MATH_FOUNDATIONS.md)** — Step-by-step graph-to-equations walkthrough
- **[Codex Critique & Response](docs/claude-codex-response.md)** — Code review findings and fixes

## Key Dependencies

| Package | Version | Purpose |
|---|---|---|
| `networkx` | ≥ 3.0 | Graph data structure & algorithms (min-cut, Louvain) |
| `numpy` | ≥ 1.24 | Array math, linear algebra |
| `scipy` | ≥ 1.10 | Sparse matrices, eigenvalue solvers, linear system solvers |
| `plotly` | ≥ 5.15 | Interactive 3D visualizations, HTML export |
| `python-louvain` | ≥ 0.16 | Louvain community detection algorithm |
| `pytest` | ≥ 7.0 | Testing framework (dev dependency) |

## License

This project is for educational and research purposes.
