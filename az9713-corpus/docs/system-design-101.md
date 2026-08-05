---
repo: system-design-101
description: Beginner-friendly system design notes and interactive lab from a source lecture
language: HTML
stars: 0
forks: 0
created: 2026-06-04
updated: 2026-06-04
topics: 
is_fork: False
kb: 21
---

# system-design-101
# System Design 101

This repository is a beginner-friendly learning package for modern web application system design. It turns one long-form source lecture into practical notes, visual diagrams, and a small interactive study lab for readers who already know traditional OOP programming in Java, Python, C, or C++, but have little or no experience with modern web app development.

The goal is shortest-path onboarding: help an experienced procedural/OOP programmer understand how web systems are built, called, scaled, secured, and reasoned about in production.

## Source

The source lecture is the original YouTube video:

**System Design 101: APIs, Databases, Caching, CDNs, Load Balancing & Production Infra**  
https://www.youtube.com/watch?v=oYxTTirKY8M&t=3026s

The raw local transcript used during generation is intentionally not committed to this repository. The public repo contains the synthesized learning materials, diagrams, and manifest only.

## What This Repo Contains

- [`system_design_lecture_notes.md`](system_design_lecture_notes.md)  
  Transcript-grounded lecture notes rewritten for readers coming from classic OOP training.

- [Open the interactive learning lab](https://az9713.github.io/system-design-101/system_design_learning_lab.html)  
  A standalone browser learning lab with a concept map, request-flow walkthrough, scaling recommender, API chooser, auth drill, quiz, and capstone prompt builder.

- [`assets/request_flow.svg`](assets/request_flow.svg)  
  Visual explanation of a browser-to-server request flow.

- [`assets/scaling_load_balancer.svg`](assets/scaling_load_balancer.svg)  
  Visual explanation of horizontal scaling, load balancers, health checks, and remaining single points of failure.

- [`assets/auth_flow.svg`](assets/auth_flow.svg)  
  Visual explanation of authentication versus authorization.

- [`manifest.md`](manifest.md)  
  Generation notes, source limitations, prompts used, and artifact list.

## Development Journey

This repo started as a local transcript-to-artifact exercise. The initial source was a long system design transcript covering:

- single-server web app setup;
- SQL, NoSQL, graph, and key-value storage;
- vertical and horizontal scaling;
- load balancing algorithms and health checks;
- single points of failure;
- API design, REST, GraphQL, and gRPC;
- HTTP, HTTPS, WebSockets, queues, TCP, and UDP;
- authentication, authorization, and common security risks.

The first pass produced a dense Markdown note set. That was not enough for the learning objective, because onboarding someone new to web app development should not be a wall of text. The package was expanded into:

1. A lecture-note document with OOP-to-web mental model bridges.
2. SVG diagrams for the concepts that benefit from visual explanation.
3. A standalone HTML lab for immediate practice and self-checking.
4. A manifest that documents source scope, generation prompts, and limitations.

The resulting repo is designed to be inspectable without special tooling. Open the Markdown file for reading, or use the GitHub Pages learning-lab link for interactive practice.

## Audience

This is written for readers who understand ideas like classes, methods, interfaces, object state, exceptions, access control, and processes, but are still building intuition for:

- HTTP requests and responses;
- APIs as public contracts between programs;
- JSON as cross-language object exchange;
- databases as persistent state outside the process;
- load balancers as traffic dispatchers;
- auth as identity plus permission checks;
- production infrastructure as failure management.

## How To Use

1. Read [`system_design_lecture_notes.md`](system_design_lecture_notes.md).
2. Open the [interactive learning lab](https://az9713.github.io/system-design-101/system_design_learning_lab.html) as a rendered web page.
3. Work through the quizzes and exercises.
4. Use the capstone builder to design a small app, such as a bookstore, task tracker, photo album, or online course platform.

No build step is required.

## Repository Policy

The raw transcript file is excluded from version control:

```text
transcript.txt
```

This keeps the repository focused on derived educational artifacts and avoids publishing the full transcript.

## Status

Initial artifact package generated locally on June 3, 2026.
