# MOOSE — Multiphysics Object-Oriented Simulation Environment

> **This repository is based on the original [MOOSE framework by Idaho National Laboratory](https://github.com/idaholab/moose).**
>
> This repo **does not include the MOOSE source codes**. Instead, it supplements the original
> repository with **comprehensive documentation and worked examples** designed to help new users
> learn the framework from scratch. The 103 progressive quickstart cases are fully explained — from
> the physics and governing equations, through the input file structure, to interpreting the
> simulation results — so that users can learn how to set up their own simulations and understand
> the output without any external help.
>
> This repository also includes two **Claude Code skills** that automate the entire simulation
> workflow. The **`moose-simulation`** skill is a structured 9-step checklist that governs the
> complete lifecycle of a MOOSE simulation — from prerequisite checks and input-file authoring
> through Docker execution, output validation, matplotlib visualization, and README documentation.
> The **`docker-windows`** skill handles the notoriously tricky details of running Docker from
> Git Bash / MINGW on Windows — preventing silent path mangling, volume-mount failures, and flag
> conversion issues that would otherwise break every `docker run` command. Together, these two
> skills enabled [Claude Code](https://claude.ai/claude-code) to autonomously generate all 103
> quickstart cases — from writing the input files and running simulations in Docker, through
> debugging convergence failures, to generating plots and documentation — with no manual
> intervention required.
>
> **Original repository:** https://github.com/idaholab/moose
> **Official documentation:** https://mooseframework.inl.gov

---

[![License: LGPL 2.1](https://img.shields.io/badge/License-LGPL%202.1-blue.svg)](LICENSE)

MOOSE is an open-source, parallel finite-element multiphysics framework developed and maintained
by [Idaho National Laboratory](https://www.inl.gov). It provides a high-level C++ API built on
top of [PETSc](https://petsc.org) (nonlinear solvers) and [libMesh](https://libmesh.github.io)
(finite-element discretization), enabling scientists and engineers to write tightly-coupled
multiphysics simulation codes without having to manage the underlying numerical infrastructure
themselves.

## What is MOOSE?

MOOSE was created to lower the barrier to developing rigorous, production-quality simulation
codes. Rather than forcing every research group to re-implement parallel mesh management,
nonlinear solver interfaces, and input-file parsing, MOOSE provides these as a reusable
foundation. A developer who wants to add a new physical model writes a single C++ class — a
`Kernel`, `BoundaryCondition`, or `Material` — that contributes the weak-form residual for one
equation. The framework handles assembly, Jacobian computation (analytically via automatic
differentiation, or by finite difference), load balancing, and parallel I/O.

The framework is designed around full coupling. All physics share the same nonlinear solve, so
there is no operator splitting unless you explicitly request it. This makes MOOSE especially
well-suited to problems where multiphysics feedback is strong: nuclear fuel performance, reactor
thermal-hydraulics, geological carbon storage, metal additive manufacturing, and similar
coupled-field applications. The same code that runs on a laptop with 4 cores can be submitted
unchanged to a leadership-class supercomputer; the largest MOOSE runs have exceeded
**100,000 CPU cores**.

MOOSE is used by dozens of national laboratories, universities, and industrial organizations
worldwide. Idaho National Laboratory's own suite of application codes — BISON (nuclear fuel),
RELAP-7 (system thermal-hydraulics), Grizzly (reactor structural aging), and others — are all
built on MOOSE. The framework is released under the GNU Lesser General Public License 2.1,
making it freely available for both academic and commercial derivative applications.

The repository is organized into three tiers: the **framework** (core kernel, always required),
optional **modules** (reusable physics packages), and **applications** (end-user codes that
combine a framework build with one or more modules). This layered design means that work done in
a module — a new contact algorithm, a new equation of state, a new solver strategy — is
immediately available to every application that enables that module.

---

## Key Capabilities

| Feature | Description |
|---|---|
| Fully-coupled, fully-implicit multiphysics | All field equations are assembled into a single nonlinear system and solved simultaneously via Newton's method with PETSc back-ends |
| FEM, FVM, and DG methods | Continuous Galerkin FEM, cell-centered finite volume, and discontinuous Galerkin (including mixed DG/FEM in the same simulation) |
| Parallel execution (MPI + threading) | Domain-decomposed MPI parallelism with optional threaded assembly; runs from a laptop to >100 K cores without code changes |
| Automatic mesh adaptivity | h-refinement and coarsening driven by error estimators or custom indicators; fully parallel with dynamic load balancing |
| Automatic differentiation (AD) | AD-generated exact Jacobians via dual-number arithmetic; eliminates hand-coded Jacobian maintenance |
| MultiApp multiscale coupling | Hierarchical sub-application trees with flexible data transfers, enabling macro/micro or system/component coupling |
| 25+ physics modules | Heat transfer, solid mechanics, Navier-Stokes, porous flow, phase field, contact, XFEM, ray tracing, stochastic tools, and more |
| Python tooling | TestHarness (parallel test runner), MooseDocs (documentation), pyhit (input-file parsing), mooseutils, Peacock GUI, Chigger visualization |

---

## What This Repository Provides

This repository focuses on **learning materials** for the MOOSE framework:

- **Comprehensive documentation** covering architecture, developer workflows, input-file syntax, and all 29 physics modules
- **103 progressive quickstart examples** (`quickstart-runs/`) — each with a complete input file, detailed README explaining the physics, and matplotlib visualization of the results
- **An 8-week study plan** for self-learners going from zero to productive MOOSE developer
- **Docker instructions** for running MOOSE on Windows without compiling from source

Many of the advanced quickstart cases are drawn from MIT course materials by five professors:

| Professor | Course / Textbook | Cases | Topics |
|---|---|---|---|
| **James R. Melcher** | [*Continuum Electromechanics*](https://ocw.mit.edu/ans7870/resources/melcher/resized/cem_811.pdf) (MIT Press, 1981) | 22–29 | Charge relaxation, electrohydrodynamics, MHD, ferrofluids, electroquasistatics |
| **Herman A. Haus** | [*Electromagnetic Noise and Quantum Optical Measurements*](https://engineering.purdue.edu/wcchew/ece604f19/Supplementary%20Texts/Haus_Electromagnetic%20Noise%20and%20Quantum%20Optical%20Measurements1.pdf) (Springer, 2000) — classical chapters | 30–36 | Waveguide eigenvalues, driven cavities, dielectric slabs, coupled resonators, thermal noise, dispersive pulses, solitons |
| **Jin Au Kong** | [MIT 6.635 *Advanced Electromagnetism*](https://ocw.mit.edu/courses/6-635-advanced-electromagnetism-spring-2003/pages/lecture-notes/) (Spring 2003) | 74–83 | Left-handed materials, Drude skin depth, 3D waveguides, cylinder scattering, Bragg mirrors, photonic crystals, cavity resonance, Veselago lens |
| **David H. Staelin** | [MIT 6.661 *Receivers, Antennas, and Signals*](https://ocw.mit.edu/courses/6-661-receivers-antennas-and-signals-spring-2003/pages/lecture-notes/) | 84–93 | Lossy TEM cavity Q factor, Hertzian and half-wave dipoles, phased array beamforming, single-slit diffraction, dielectric waveguide modes, parabolic reflector, radar cross section, aperture synthesis, inverse source recovery |
| **Markus Zahn** | [MIT 6.641 *Electromagnetic Fields, Forces, and Motion*](https://ocw.mit.edu/courses/6-641-electromagnetic-fields-forces-and-motion-spring-2005/pages/lecture-notes/) | 94–103 | Periodic potential sheet, dielectric relaxation, Maxwell's capacitor, skin effect, Debye shielding, cylinder scattering, elastic rod waves, RC transmission line, membrane pull-in instability, Kelvin force dielectrophoresis |

Additional cases are based on textbooks by these authors:

| Author | Textbook | Cases | Topics |
|---|---|---|---|
| **Michel Rieutord** | [*Fluid Dynamics: An Introduction*](https://weblibrary.mila.edu.my/upload/ebook/engineering/2015_Book_FluidDynamics.pdf) (Springer, 2015) — Chapters 4–10 | 37–44 | Rayleigh-Benard convection, Kelvin-Helmholtz instability, Blasius boundary layer, k-epsilon turbulence, Rayleigh-Taylor instability, Sod shock tube, Ekman spiral, Alfven wave |
| **Ralph C. Smith** | [*Uncertainty Quantification: Theory, Implementation, and Applications*](https://rsmith.math.ncsu.edu/UQ_TIA/) (SIAM, 2014) | 45–48 | Monte Carlo UQ, polynomial chaos expansion, heat source inversion (adjoint optimization), Latin Hypercube parameter study |

To actually build and run MOOSE simulations, you need the framework itself from the [original repository](https://github.com/idaholab/moose) or the official [Docker image](https://hub.docker.com/r/idaholab/moose) (`idaholab/moose:latest`).

---

## Documentation

| File | Description |
|---|---|
| [docs/architecture.md](docs/architecture.md) | System architecture with subsystem diagrams covering the Framework → Modules → Applications hierarchy |
| [docs/developer-guide.md](docs/developer-guide.md) | Step-by-step C++ developer tutorial: writing Kernels, BCs, Materials, and custom objects |
| [docs/user-guide.md](docs/user-guide.md) | Simulation user reference covering input-file syntax, all major blocks, and solver options |
| [docs/quick-start.md](docs/quick-start.md) | 103 worked examples progressing from simple diffusion through chemical reactions, mortar contact, XFEM, THM pipe flow, level-set interface tracking, advanced electromagnetism, and continuum electromechanics |
| [docs/zero-to-hero.md](docs/zero-to-hero.md) | 8-week structured study plan for new MOOSE developers |
| [docs/modules-reference.md](docs/modules-reference.md) | Physics module reference with API summaries and example input files |
| [docs/docker-guide.md](docs/docker-guide.md) | Running MOOSE on Windows with Docker — installation, volume mounts, MPI |

The official online documentation lives at **https://mooseframework.inl.gov**.

---

## Quickstart Examples

The `quickstart-runs/` directory contains **103 fully worked examples**, each in its own subdirectory with:

- **Input file** (`.i`) — ready to run with `moose_test-opt` or `combined-opt`
- **Detailed README** — explains the physics, walks through every input-file block, describes the output files, and shows how to interpret the results
- **Visualization plots** (`.png`) — matplotlib-generated 2D/3D plots of the simulation output

### Cases 01-13: Framework Fundamentals

<table>
<tr>
<td align="center" width="25%">
<a href="quickstart-runs/case01-1d-steady-diffusion"><img src="quickstart-runs/case01-1d-steady-diffusion/case01_diffusion_1d.png" width="100%"/></a><br/>
<b>Case 01</b>: 1D Steady Diffusion
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case02-2d-steady-diffusion"><img src="quickstart-runs/case02-2d-steady-diffusion/case02_contour_2d.png" width="100%"/></a><br/>
<b>Case 02</b>: 2D Steady Diffusion
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case03-transient-heat"><img src="quickstart-runs/case03-transient-heat/case03_temperature_snapshots.png" width="100%"/></a><br/>
<b>Case 03</b>: Transient Heat
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case04-manufactured-solution"><img src="quickstart-runs/case04-manufactured-solution/case04_numerical.png" width="100%"/></a><br/>
<b>Case 04</b>: Manufactured Solution
</td>
</tr>
<tr>
<td align="center">
<a href="quickstart-runs/case05-neumann-bc"><img src="quickstart-runs/case05-neumann-bc/case05_contour_2d.png" width="100%"/></a><br/>
<b>Case 05</b>: Neumann BC
</td>
<td align="center">
<a href="quickstart-runs/case06-two-material-domain"><img src="quickstart-runs/case06-two-material-domain/case06_contour_2d.png" width="100%"/></a><br/>
<b>Case 06</b>: Two-Material Domain
</td>
<td align="center">
<a href="quickstart-runs/case07-nonlinear-diffusion"><img src="quickstart-runs/case07-nonlinear-diffusion/case07_contour_2d.png" width="100%"/></a><br/>
<b>Case 07</b>: Nonlinear Diffusion
</td>
<td align="center">
<a href="quickstart-runs/case08-advection-diffusion"><img src="quickstart-runs/case08-advection-diffusion/case08_blob_snapshots.png" width="100%"/></a><br/>
<b>Case 08</b>: Advection-Diffusion
</td>
</tr>
<tr>
<td align="center">
<a href="quickstart-runs/case09-coupled-reaction-diffusion"><img src="quickstart-runs/case09-coupled-reaction-diffusion/case09_u_final.png" width="100%"/></a><br/>
<b>Case 09</b>: Coupled Reaction-Diffusion
</td>
<td align="center">
<a href="quickstart-runs/case10-adaptive-mesh-refinement"><img src="quickstart-runs/case10-adaptive-mesh-refinement/case10_amr_solution.png" width="100%"/></a><br/>
<b>Case 10</b>: Adaptive Mesh Refinement
</td>
<td align="center">
<a href="quickstart-runs/case11-adaptive-timestepping"><img src="quickstart-runs/case11-adaptive-timestepping/case11_temperature_final.png" width="100%"/></a><br/>
<b>Case 11</b>: Adaptive Timestepping
</td>
<td align="center">
<a href="quickstart-runs/case12-multiapp-coupling"><img src="quickstart-runs/case12-multiapp-coupling/case12_parent_temperature.png" width="100%"/></a><br/>
<b>Case 12</b>: MultiApp Coupling
</td>
</tr>
<tr>
<td align="center">
<a href="quickstart-runs/case13-custom-kernel"><img src="quickstart-runs/case13-custom-kernel/case13_postprocessors.png" width="100%"/></a><br/>
<b>Case 13</b>: Postprocessor Analysis
</td>
<td colspan="3"></td>
</tr>
</table>

### Cases 14-21: Advanced Multi-Physics (Module-Based)

These cases use MOOSE physics modules (`heat_transfer`, `solid_mechanics`, `navier_stokes`, `phase_field`, `porous_flow`) and require `combined-opt` via Docker.

<table>
<tr>
<td align="center" width="25%">
<a href="quickstart-runs/case14-thermoelasticity"><img src="quickstart-runs/case14-thermoelasticity/case14_thermoelasticity.png" width="100%"/></a><br/>
<b>Case 14</b>: Thermoelasticity<br/>
<sub>Heat + Solid Mechanics</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case15-lid-driven-cavity"><img src="quickstart-runs/case15-lid-driven-cavity/case15_velocity_magnitude.png" width="100%"/></a><br/>
<b>Case 15</b>: Lid-Driven Cavity<br/>
<sub>Navier-Stokes FV (Re=100)</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case16-natural-convection"><img src="quickstart-runs/case16-natural-convection/case16_temperature.png" width="100%"/></a><br/>
<b>Case 16</b>: Natural Convection<br/>
<sub>Fluid + Heat (Ra=10⁴)</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case17-joule-heating"><img src="quickstart-runs/case17-joule-heating/case17_joule_heating.png" width="100%"/></a><br/>
<b>Case 17</b>: Joule Heating<br/>
<sub>Electromagnetics + Heat</sub>
</td>
</tr>
<tr>
<td align="center">
<a href="quickstart-runs/case18-cahn-hilliard"><img src="quickstart-runs/case18-cahn-hilliard/case18_phase_separation.png" width="100%"/></a><br/>
<b>Case 18</b>: Cahn-Hilliard<br/>
<sub>Phase Field Decomposition</sub>
</td>
<td align="center">
<a href="quickstart-runs/case19-porous-flow"><img src="quickstart-runs/case19-porous-flow/case19_thermal_plume.png" width="100%"/></a><br/>
<b>Case 19</b>: Porous Flow<br/>
<sub>Darcy Flow + Heat Transport</sub>
</td>
<td align="center">
<a href="quickstart-runs/case20-elastic-wave"><img src="quickstart-runs/case20-elastic-wave/case20_wave_snapshots.png" width="100%"/></a><br/>
<b>Case 20</b>: Elastic Wave<br/>
<sub>Dynamic Solid Mechanics</sub>
</td>
<td align="center">
<a href="quickstart-runs/case21-bimetallic-strip"><img src="quickstart-runs/case21-bimetallic-strip/case21_bimetallic_strip.png" width="100%"/></a><br/>
<b>Case 21</b>: Bimetallic Strip<br/>
<sub>Multi-Material Thermo-Mechanics</sub>
</td>
</tr>
</table>

### Cases 22-29: Continuum Electromechanics

> Inspired by **Professor James R. Melcher**'s landmark textbook
> [*Continuum Electromechanics*](https://ocw.mit.edu/courses/6-641-electromagnetic-fields-forces-and-motion-spring-2005/pages/textbook-contents/) (MIT Press, 1981) —
> the definitive treatment of electrohydrodynamics, magnetohydrodynamics,
> and electromechanical wave interactions. Melcher taught at MIT for over
> 25 years and his work laid the foundations for modern electrokinetic and
> EHD research.

These cases cover charge transport, magnetic diffusion, induction heating, electrohydrodynamics, and magnetohydrodynamics. Each case references the specific chapter and section of Melcher's text. They require `combined-opt` via Docker.

<table>
<tr>
<td align="center" width="25%">
<a href="quickstart-runs/case22-charge-relaxation"><img src="quickstart-runs/case22-charge-relaxation/case22_charge_relaxation.png" width="100%"/></a><br/>
<b>Case 22</b>: Charge Relaxation<br/>
<sub>Exponential Decay (tau=eps/sigma)</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case23-magnetic-diffusion"><img src="quickstart-runs/case23-magnetic-diffusion/case23_magnetic_diffusion.png" width="100%"/></a><br/>
<b>Case 23</b>: Magnetic Diffusion<br/>
<sub>erfc Profile Verification</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case24-drift-diffusion"><img src="quickstart-runs/case24-drift-diffusion/case24_drift_diffusion.png" width="100%"/></a><br/>
<b>Case 24</b>: Drift-Diffusion<br/>
<sub>Charge Transport + Poisson</sub>
</td>
<td align="center" width="25%">
<a href="quickstart-runs/case25-induction-heating"><img src="quickstart-runs/case25-induction-heating/case25_induction_heating.png" width="100%"/></a><br/>
<b>Case 25</b>: Induction Heating<br/>
<sub>Eddy Currents + Joule Heat</sub>
</td>
</tr>
<tr>
<td align="center">
<a href="quickstart-runs/case26-ehd-pumping"><img src="quickstart-runs/case26-ehd-pumping/case26_ehd_pumping.png" width="100%"/></a><br/>
<b>Case 26</b>: EHD Pumping<br/>
<sub>Coulomb-Force-Driven Flow</sub>
</td>
<td align="center">
<a href="quickstart-runs/case27-hartmann-flow"><img src="quickstart-runs/case27-hartmann-flow/case27_hartmann_flow.png" width="100%"/></a><br/>
<b>Case 27</b>: Hartmann Flow<br/>
<sub>MHD Channel (Ha=5)</sub>
</td>
<td align="center">
<a href="quickstart-runs/case28-twoway-joule-heating"><img src="quickstart-runs/case28-twoway-joule-heating/case28_twoway_joule_heating.png" width="100%"/></a><br/>
<b>Case 28</b>: Two-Way Joule Heating<br/>
<sub>T-Dependent Conductivity</sub>
</td>
<td align="center">
<a href="quickstart-runs/case29-electroconvection"><img src="quickstart-runs/case29-electroconvection/case29_electroconvection.png" width="100%"/></a><br/>
<b>Case 29</b>: Electroconvection<br/>
<sub>EHD-Enhanced Buoyancy</sub>
</td>
</tr>
</table>

### Cases 30-36: Electromagnetic Noise and Quantum Optical Measurements

> Inspired by **Professor Herman A. Haus**'s masterful textbook
> [*Electromagnetic Noise and Quantum Optical Measurements*](https://doi.org/10.1007/978-3-642-57250-0) (Springer, 2000) —
> a unified treatment of electromagnetic theory from Maxwell's equations
> through waveguides, resonators, and optical fibers to noise, solitons,
> and quantum measurement. Haus was Institute Professor at MIT and a
> pioneer of laser physics, fiber soliton communication, and coupled
> mode theory.

Haus's book spans 13 chapters, from classical Maxwell theory (Chs 1-5)
through quantum noise and photon statistics (Chs 6-9) to solitons and
squeezing (Chs 10-13). These cases