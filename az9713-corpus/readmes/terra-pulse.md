# Terra Pulse

A full-screen 3D globe that visualises nine live planetary data layers in real time — satellites, earthquakes, wildfires, lightning, volcanoes, aurora, meteors, tropical storms, and the International Space Station.

No backend. No API keys. Runs entirely in the browser.

https://github.com/user-attachments/assets/932de4eb-0950-4959-be97-21906bfd639f

> Inspired by [WorldMonitor](https://github.com/koala73/worldmonitor) — the globe architecture, discriminated union marker system, and smart poll loop patterns are modelled on that project.

---

## Layers

| Layer | Source | Update frequency |
|-------|--------|-----------------|
| 🛰️ Satellites | tle.ivanstanojevic.me (300 objects) | Position: every 2s live · TLE: 10 min |
| 🌍 Earthquakes | USGS GeoJSON M2.5+ | 5 min |
| 🔥 Wildfires | NASA EONET v3 | 30 min |
| ⚡ Lightning | Open-Meteo thunderstorm grid | 30 s |
| 🌋 Volcanoes | NASA EONET v3 | 60 min |
| 🌌 Aurora | NOAA OVATION forecast | 30 min |
| ☄️ Meteors | NASA JPL CNEOS Fireball API | 60 min |
| 🌀 Storms | NOAA NHC active storms | 10 min |
| 🚀 ISS | tle.ivanstanojevic.me (NORAD 25544) | Position: every 2s live · TLE: 10 min |

---

## Tech stack

| Component | Technology |
|-----------|-----------|
| 3D globe | [globe.gl](https://globe.gl) v2 |
| 3D engine | [THREE.js](https://threejs.org) v0.183 |
| Orbital mechanics | [satellite.js](https://github.com/shashwatak/satellite-js) v5 (SGP4 propagator) |
| Build | [Vite](https://vitejs.dev) v5 + TypeScript v5 |
| Runtime | Browser — no Node.js at runtime |

---

## Running locally

```bash
git clone https://github.com/az9713/terra-pulse.git
cd terra-pulse
npm install
npm run dev
```

Open `http://localhost:5173`. Click any layer button to enable it.

---

## How it works

**Satellites and ISS** use TLE data from `tle.ivanstanojevic.me` and the SGP4 propagator from `satellite.js` to compute orbital positions client-side. TLEs are fetched once every 10 minutes and cached in localStorage. Positions re-propagate every 2 seconds using `new Date()` — no network call needed for live motion.

Satellites are rendered as THREE.js spheres via globe.gl's `objectsData` layer, placed at their actual orbital altitude. ISS shows a 15-minute orbital trail as a fading arc.

**All other layers** poll public APIs on fixed intervals (30 seconds to 60 minutes). Responses are normalised into a typed `GlobeMarker` discriminated union and rendered as WebGL points, rings, or paths via globe.gl.

**Two-tier cache** (in-memory + localStorage) eliminates redundant fetches when layers are toggled or the page is refreshed.

See [`docs/`](docs/index.md) for full architecture documentation including system design, all nine data layer deep-dives, and Architecture Decision Records.

---

## Project structure

```
src/
├── main.ts              ← entry point, layer wiring, animation tick
├── types.ts             ← GlobeMarker union + all interfaces
├── config/layers.ts     ← layer registry (key, icon, color, poll interval)
├── globe/GlobeApp.ts    ← globe.gl renderer, four render layers
├── services/            ← one fetcher per data source
│   ├── satellites.ts    ← TLE fetch + SGP4 propagation
│   ├── iss.ts           ← ISS TLE + 15-min trail computation
│   ├── earthquakes.ts   ← USGS GeoJSON
│   ├── wildfires.ts     ← NASA EONET
│   ├── lightning.ts     ← Open-Meteo thunderstorm grid
│   ├── volcanoes.ts     ← NASA EONET
│   ├── aurora.ts        ← NOAA OVATION
│   ├── meteors.ts       ← NASA JPL Fireball API
│   └── storms.ts        ← NOAA NHC
├── ui/
│   ├── LayerToggle.ts   ← toggle panel
│   └── EventPopup.ts    ← click-to-inspect card
└── utils/
    ├── cache.ts         ← two-tier memory + localStorage cache
    └── poll.ts          ← backoff poll loop with tab-pause
```

---

## Documentation

Full docs in [`docs/`](docs/index.md):

- [What is Terra Pulse?](docs/overview/what-is-this.md)
- [Quickstart](docs/getting-started/quickstart.md)
- [Globe rendering deep dive](docs/concepts/globe-rendering.md)
- [All nine data layers](docs/concepts/data-layers.md)
- [Orbital propagation](docs/concepts/orbital-propagation.md)
- [System design](docs/architecture/system-design.md)
- [Architecture Decision Records](docs/architecture/adr/)
- [Troubleshooting](docs/troubleshooting/common-issues.md)

---

## License

MIT
