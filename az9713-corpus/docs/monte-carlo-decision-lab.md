---
repo: monte-carlo-decision-lab
description: Explore 'what if' scenarios for tough decisions using Monte Carlo simulation
language: Python
stars: 0
forks: 0
created: 2026-01-05
updated: 2026-01-05
topics: 
is_fork: False
kb: 521
---

# monte-carlo-decision-lab
# Monte Carlo Decision Analyzer

A Python framework for exploring decision outcomes using Monte Carlo simulation.

**What does this do?** It helps you understand the range of possible outcomes for any decision by simulating thousands of "what if" scenarios.

---

## ⚠️ IMPORTANT: Read Before Running

**The included scenarios are EXAMPLES ONLY.** They contain placeholder values and should NOT be used for real decisions without customization.

### Files You Must Create/Edit

| Step | File | Action |
|------|------|--------|
| 1 | `scenarios/my_scenario.py` | **COPY** `scenarios/_TEMPLATE.py` and edit values |
| 2 | `scenarios/__init__.py` | **EDIT** - Add 2 lines (import + __all__ entry) |
| 3 | `run_simulation.py` | **EDIT** - Add 2 lines (import + SCENARIOS entry) |

### What You Must Specify

For each factor affecting your decision:
- `min_value`, `max_value`: Possible range (from data/research)
- `mu_min`, `mu_max`: Typical value range (narrower than above)
- `sigma_max`: Variation (≈30% of range)
- `is_positive`: True if higher is better, False if worse

👉 **See [SETUP_YOUR_ANALYSIS.md](docs/SETUP_YOUR_ANALYSIS.md) for step-by-step instructions with copy-paste templates.**

The example scenarios demonstrate the framework's capabilities but their parameter values are arbitrary. Running them without customization produces meaningless results.

---

## Why Use This?

When making important decisions, you face uncertainty. This tool helps by:

- **Exploring many futures**: Instead of guessing one outcome, see thousands
- **Identifying what matters**: Find out which factors most influence success
- **Testing assumptions**: See how results change when assumptions change
- **Quantifying uncertainty**: Get probabilities, not just gut feelings

---

## Quick Start

### 1. Install

```bash
pip install numpy pandas matplotlib seaborn
```

### 2. Create Your Scenario

```bash
# Copy the template
cp scenarios/_TEMPLATE.py scenarios/my_scenario.py

# Edit with YOUR values (this is required!)
# See docs/SETUP_YOUR_ANALYSIS.md for guidance
```

### 3. Register and Run

```bash
# After editing scenarios/__init__.py and run_simulation.py:
python run_simulation.py --scenario my_scenario
```

### Note: Example Scenarios Are Blocked

Running `python run_simulation.py` without creating your own scenario will show:

```
STOP: You are trying to run an EXAMPLE scenario
The 'foreign_policy' scenario contains PLACEHOLDER values.
Running it will produce MEANINGLESS results.
```

This is intentional. You MUST create your own scenario with real data.

---

## Example Output

```
======================================================================
SIMULATION RESULTS
Scenario: Foreign Policy Action Analysis
======================================================================

Total assumption sets explored: 500
Simulated futures per assumption set: 1,000
Total simulations: 500,000

----------------------------------------------------------------------
OUTCOME DISTRIBUTION
----------------------------------------------------------------------

SUCCESS (things go well):
  Median:          30.3%
  10th percentile: 20.9%  (pessimistic assumptions)
  90th percentile: 39.2%  (optimistic assumptions)

UNCLEAR (mixed results):
  Median:          37.8%

BACKFIRE (things go badly):
  Median:          31.2%

----------------------------------------------------------------------
WHAT THIS MEANS (Plain English)
----------------------------------------------------------------------

Under the assumptions explored, the most common outcome is UNCLEAR
occurring in about 38% of simulated futures.

  • Success is POSSIBLE but not dominant (~30% of the time)
  • Backfire is a MODERATE RISK (~31% of the time)
  • Results are SENSITIVE to assumptions (success varies by 18 percentage points)
```

---

## Included Scenarios

### 1. Foreign Policy Action

Analyze a hypothetical government decision with factors like:
- Popularity boost
- Public judgment (right vs. wrong decision)
- Ally support
- Legal challenges
- Blame attribution

```bash
python run_simulation.py --scenario foreign_policy
```

### 2. Product Launch

Analyze a business product launch with factors like:
- Customer demand
- Product quality
- Competition strength
- Production cost
- Technical risk

```bash
python run_simulation.py --scenario product_launch
```

---

## Command Line Options

```bash
# Quick test (faster, less accurate)
python run_simulation.py --quick

# Thorough analysis (slower, more accurate)
python run_simulation.py --thorough

# Choose scenario
python run_simulation.py --scenario product_launch

# Custom settings
python run_simulation.py --outer 200 --inner 500 --seed 123

# Just see scenario description
python run_simulation.py --describe
```

---

## How It Works

### The Two-Layer Approach

This isn't just a simple Monte Carlo. It uses **two layers**:

1. **Outer Loop**: Tries different sets of assumptions
   - "What if demand is typically high vs. low?"
   - "What if success scenarios are more vs. less likely?"

2. **Inner Loop**: For each assumption set, simulates many outcomes
   - Samples factor values randomly
   - Computes outcome scores
   - Classifies as Success / Unclear / Backfire

This reveals not just "what might happen" but "how sensitive conclusions are to assumptions."

### Outcome Classification

Each simulated future gets a score based on:
```
Score = (Positive Factors) - (Negative Factors)
```

Scores are standardized, then classified:
- **Success**: Above average (Z > 0.5)
- **Unclear**: Near average (-0.5 ≤ Z ≤ 0.5)
- **Backfire**: Below average (Z < -0.5)

---

## Create Your Own Scenario

```python
from simulator import Scenario, Factor, run_simulation

# Define factors
factors = [
    Factor(
        name="revenue",
        display_name="Revenue Potential",
        description="Expected revenue from the project",
        min_value=0,
        max_value=1000000,
        is_positive=True,  # Higher is better
        weight=1.0
    ),
    Factor(
        name="cost",
        display_name="Total Cost",
        description="All costs including development and marketing",
        min_value=0,
        max_value=500000,
        is_positive=False,  # Higher is worse
        weight=1.0
    ),
]

# Create scenario
my_scenario = Scenario(
    name="my_project",
    display_name="My Project Decision",
    description="Should we proceed with this project?",
    factors=factors
)

# Run simulation
results = run_simulation(my_scenario)
```

---

## Project Structure

```
monte-carlo-decision-analyzer/
├── run_simulation.py       # Main entry point
├── requirements.txt        # Python dependencies
├── README.md               # This file
│
├── simulator/              # Core simulation engine
│   ├── __init__.py
│   ├── scenario.py         # Scenario and Factor classes
│   ├── engine.py           # Monte Carlo engine
│   └── visualize.py        # Charts and reports
│
├── scenarios/              # Example scenarios
│   ├── __init__.py         # ← EDIT THIS (Step 2)
│   ├── _TEMPLATE.py        # ← COPY THIS to create your scenario (Step 1)
│   ├── foreign_policy.py   # Example only - don't use as-is
│   └── product_launch.py   # Example only - don't use as-is
│
├── docs/                   # Documentation
│   ├── SETUP_YOUR_ANALYSIS.md  # ⚠️ READ THIS FIRST
│   ├── methodology.md      # Mathematical details
│   ├── QUICK_START.md      # Getting started guide
│   ├── USER_GUIDE.md       # Full user documentation
│   └── DEVELOPER_GUIDE.md  # For contributors
│
└── results/                # Output directory (created on run)
    ├── simulation_results.csv
    ├── summary_report.txt
    └── *.png               # Visualization charts
```

---

## Documentation

| Document | Purpose | Read First? |
|----------|---------|-------------|
| [SETUP_YOUR_ANALYSIS.md](docs/SETUP_YOUR_ANALYSIS.md) | **How to set up YOUR decision** | **YES - START HERE** |
| [QUICK_START.md](docs/QUICK_START.md) | 5-minute setup and first run | After setup guide |
| [USER_GUIDE.md](docs/USER_GUIDE.md) | Complete user documentation | Reference |
| [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) | For contributors and developers | If modifying code |
| [methodology.md](docs/methodology.md) | Mathematical methodology | If curious about math |
| [CLAUDE.md](CLAUDE.md) | Context for AI assistants | For AI tools |

---

## Requirements

- Python 3.8+
- numpy
- pandas
- matplotlib
- seaborn

---

## FAQ

**Q: Is this a prediction tool?**
A: No. It explores "what if" scenarios based on your assumptions. Different assumptions lead to different results.

**Q: How accurate are the probabilities?**
A: They're as accurate as your assumptions. The tool helps you understand the *range* of outcomes, not predict a specific one.

**Q: Why two layers?**
A: To show how sensitive results are to assumptions. If results are similar across many assumption sets, you can be more confident.

**Q: Can I add my own scenarios?**
A: Yes! See [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for instructions.

---

## License

This project is provided for educational and research purposes.

---

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes with tests
4. Submit a pull request

See [DEVELOPER_GUIDE.md](docs/DEVELOPER_GUIDE.md) for coding guidelines.
