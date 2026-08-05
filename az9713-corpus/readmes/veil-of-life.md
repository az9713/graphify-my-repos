# The Veil of Life

*If you were drawn at random from every living thing that has ever existed on Earth — what would you be?*

https://github.com/user-attachments/assets/18495d78-31ec-4639-bcc5-628e6aaf45ec

This project extends Ethan Mollick's [**Veil of History**](https://veil-of-history.netlify.app) outward from human history to the full 3.8-billion-year history of life on Earth. The Veil of History asks: *given you are human, which human would you be?* The Veil of Life asks the prior question: *how improbable is it that you are human at all?*

The answer, at every level, is the same: almost certainly something smaller, shorter-lived, and more anonymous than the example that first comes to mind.

---

## The relationship to Mollick's project

**Hard architectural constraint:** The Homo sapiens leaf node in this project IS Mollick's model — referenced directly, never re-estimated. `life_tree.js` loads `model.js` (Mollick's file, untouched) and delegates all human-level statistics — the 81% born before 1650, the 39% Neolithic, the 50% child mortality, the 16% modern life — to `window.VEIL_MODEL`.

*The Veil of Life* is the prologue. *The Veil of History* is the final chapter. The two projects compose: clicking to Homo sapiens hands off to Mollick's data and links to his site.

---

## What's inside

**The Tree Navigator** — A zoomable tree of life with 10 levels from All Life → Bacteria → … → Homo sapiens. At each level, the most probable life is shown as a vignette card. Click any branch to navigate down.

**The Jackpot Meter** — A fixed display showing the cumulative odds of being at your current level. Starts at "1 in 1 — you exist" at the root. Reaches "1 in 10²²" or deeper at Homo sapiens. Updates live as you navigate. The analogy updates with it: *"rarer than a specific star in 1,000 observable universes."*

**Vignette Cards** — At every node, a Mollick-style card:
- Most probable species (specific, not generic)
- Location, duration with human comparison
- What you do — honest, unglamorous
- What you never experience (available to the next level up)
- Greatest threat, with probability where known
- Conditions table adapted per level (Mollick's poverty/mortality/literacy metrics at the human leaf)
- Philosophical note — one sentence
- Jackpot odds to reach the next level

**Draw a Life** — Weighted random draw from any level. Draw from All Life: almost certainly a bacterium. Draw from Animalia: almost certainly a nematode. Draw from Homo sapiens: Mollick's draw — era, region, station, conditions — calling `window.VEIL_MODEL` directly.

**The Emergence Timeline** — Logarithmic geological timescale from 3.8 Bya to today, showing when each group first appeared. Reinforces how many microbial lives accumulated before complex life existed.

**Conditions Table** — Level-adapted metrics analogous to Mollick's:

| Level | Metric 1 | Metric 2 | Metric 3 |
|-------|----------|----------|----------|
| Bacteria | % lysed by phage/day | Genome size | Lifespan |
| Archaea | Habitat | Metabolism | Lifespan |
| Nematode | % dying in first week | Neuron count | Sensory modalities |
| Insect | % sterile workers | Colony rank | Neuron count |
| Fish | Depth (proxy for isolation) | Body length | Lifespan |
| Mammal | Predation mortality | Litter size | Heart rate |
| Primate | Dominance rank | Troop size | Theory of mind |
| **Human** | **Mollick's metrics verbatim** — poverty, child mortality, literacy, life expectancy |

---

## The ten-level vignette series

| Level | Most probable life | Jackpot odds to next |
|-------|-------------------|----------------------|
| All Life | *Pelagibacter ubique*, open ocean, 2–7 days | 1 in 100 |
| Archaea | Marine Group I Thaumarchaeota, 200–2,000m depth | 1 in 10,000 |
| Chromista | A diatom — 20% of Earth's oxygen, 1–4 days | 1 in 10,000,000 |
| Nematoda | Bacterivorous soil nematode, 302 neurons, 2–3 weeks | 1 in 1,000 |
| Insecta | Worker ant — sterile, 1 year, anonymous | 1 in 10,000,000 |
| Marine invertebrate | Copepod — vertical migration, eaten by herring | 1 in 1,000 |
| Fish | Bristlemouth (*Cyclothone*) — never seen by humans | 1 in 10,000 |
| Mammalia | Field vole — 500 bpm heart, eaten within the year | 1 in 10,000 |
| Primate | Rhesus macaque — politics, grief, birth-rank lottery | 1 in 1,000 |
| **Homo sapiens** | **→ Mollick's Veil of History** | — |

The cumulative odds of drawing a comfortable modern human from the full pool: approximately **1 in 10³¹**.

---

## The model

```
P(group) = totalLives(group) / totalLives(all life) ≈ totalLives(group) / 10⁴¹
```

Life-count estimates by level:

| Kingdom | Total lives ever | Source |
|---------|-----------------|--------|
| Bacteria | ~10⁴¹ | Whitman et al. 1998; Bar-On et al. 2018 |
| Archaea | ~10³⁸ | Karner et al. 2001 |
| Chromista (diatoms) | ~10³⁷ | Smetacek 1999; Tréguer et al. 2018 |
| Protozoa | ~10³⁶ | Bar-On et al. 2018 |
| Animalia | ~10³⁰ | Bar-On et al. 2018; van den Hoogen et al. 2019 |
| Plantae | ~10²⁴ | Bar-On et al. 2018 |
| Homo sapiens | ~117 billion | **Mollick's model — PRB 2022, Maddison, HYDE, UN WPP** |

All microbial counts carry 1–3 orders of magnitude uncertainty. The jackpot meter shows ranges for microbial nodes. Even with a 1,000× error in the bacterial count, the conclusion does not change.

**The unit problem for bacteria:** one life = cell division (birth) to next division, lysis, or starvation (death). Consistent and measurable.

**The unit problem for fungi:** a mycelium network is one organism; the "life" unit is incoherent. Fungi appear in the tree as a noted exception, excluded from cumulative probability.

---

## Sources

- Bar-On, Phillips & Milo (2018). "The Biomass Distribution on Earth." *PNAS* — authoritative global biomass census
- Whitman, Coleman & Wiebe (1998). "Prokaryotes: the unseen majority." *PNAS*
- van den Hoogen et al. (2019). "Soil nematode abundance and functional group composition." *Nature* — 4.4 × 10²⁰ nematodes globally
- Irigoien et al. (2014). "Large mesopelagic fishes biomass and trophic efficiency in the open ocean." *Nature Communications* — bristlemouths as most abundant vertebrate
- Karner et al. (2001). "Archaeal dominance in the mesopelagic zone of the Pacific Ocean." *Nature*
- Smetacek (1999). "Diatoms and the Ocean Carbon Cycle." *Protist*
- **Mollick, E. (2024). *The Veil of History*** — Population Reference Bureau (2022), Maddison Project, McEvedy & Jones (1978), HYDE 3.x, UN WPP. All human-level statistics.

---

## Tech

Plain HTML/CSS/JS — no build step, no bundler, no framework. [D3](https://d3js.org) is vendored under `vendor/`. No runtime CDN dependency.

```
index.html      — single page, all sections
model.js        — Mollick's model, verbatim and untouched
life_tree.js    — LIFE_TREE data and computation (loads after model.js)
app.js          — all rendering and interaction logic
styles.css      — Mollick's design system extended
netlify.toml    — static deployment, no build command
vendor/
  d3.min.js     — D3 v7
```

`life_tree.js` follows Mollick's IIFE + `window.X` export pattern exactly. It expects `window.VEIL_MODEL` to be loaded first via script tag order. The Homo sapiens node delegates its draw function, conditions table, and era distribution entirely to `window.VEIL_MODEL`.

---

## Local preview

```bash
python -m http.server 4322
# then open http://localhost:4322
```

Or with Node:

```bash
npx serve .
```

---

## License

Code is MIT. Mollick's `model.js` is included verbatim under its original MIT license (see [veil-of-history](https://github.com/emollick/veil-of-history)). The underlying demographic figures belong to their respective sources, cited above and on the site.
