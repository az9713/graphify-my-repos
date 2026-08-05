---
repo: neuronal-wiring
description: Interactive explainer of the first complete neuronal wiring diagram of an adult brain (Dorkenwald et al., Nature 2024)
language: HTML
stars: 0
forks: 0
created: 2026-08-01
updated: 2026-08-01
topics: 
is_fork: False
kb: 20
---

# neuronal-wiring
# Every Neuron in a Fly's Brain

An interactive explainer of the first complete neuronal wiring diagram of an adult brain,
written for readers with no neuroscience background.

**Live page → https://az9713.github.io/neuronal-wiring/**

## The paper

> Dorkenwald, S., Matsliah, A., Sterling, A. R., Schlegel, P., Yu, S., McKellar, C. E., *et al.*
> and The FlyWire Consortium.
> **"Neuronal wiring diagram of an adult brain."**
> *Nature* **634**, 124–138 (3 October 2024).
> [doi:10.1038/s41586-024-07558-y](https://doi.org/10.1038/s41586-024-07558-y) · open access

The paper reports a connectome — a complete list of every neuron and every connection between
them — for an adult female *Drosophila melanogaster*: **139,255 neurons** and **54.5 million
synapses**, reconstructed from electron microscope images over roughly **33 person-years** of
human proofreading by more than 50 labs and a community of volunteers.

The companion paper the authors ask be cited alongside it is Schlegel *et al.*, which supplies
the 8,400+ cell-type annotations. The underlying data is public and browsable at
[codex.flywire.ai](https://codex.flywire.ai/).

## What this page does

The paper's own figures assume you already work in the field. This page rebuilds the argument
for someone who doesn't, without dropping the numbers or the caveats. It covers what a
connectome actually is and how it differs from a brain scan, how the map was built, four
structural findings, one complete sensory-to-motor circuit, and — at equal length — what the
map cannot tell you.

Four figures are interactive:

| Figure | What you can do |
| --- | --- |
| Scale field | Compare every previously completed wiring diagram against this one, drawn to a single scale |
| Micrograph wipe | Drag between raw electron-microscope grey and the machine's cell segmentation |
| Degree burst | Switch between a typical neuron's 13 partners and CT1's 6,399 |
| Ocellar circuit | Move a light across the sky and watch the crossed wiring roll the fly level |

## Running it

`index.html` is fully self-contained — no build step, no dependencies, no network requests.
Open it directly, or serve the folder:

```bash
python -m http.server 8000
```

It follows the visitor's light or dark system theme, and the toggle in the top-right corner
overrides that choice and remembers it.

## Credits and scope

Every quantity on the page is taken from the Nature paper. The illustrations are schematic
reconstructions built to explain those numbers — they are **not** reproductions of the paper's
figures, and the micrograph panel is a stylised simulation rather than real image data.
Behavioural claims about the ocellar circuit are the authors' hypotheses drawn from the wiring,
not filmed experiments, and the page says so where it makes them.

This is an independent explainer. It is not affiliated with, reviewed by, or endorsed by the
authors, the FlyWire Consortium, or *Nature*.

The paper is open access under CC BY 4.0; it is not redistributed here — follow the DOI above.
