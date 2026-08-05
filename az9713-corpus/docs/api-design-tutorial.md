---
repo: api-design-tutorial
description: Interactive teaching package for senior-level API design
language: HTML
stars: 0
forks: 0
created: 2026-06-07
updated: 2026-06-07
topics: 
is_fork: False
kb: 24
---

# api-design-tutorial
# API Design Tutorial

This repository contains a source-grounded teaching package based on the YouTube video **"How to Design APIs Like a Senior Engineer (REST, GraphQL, Auth, Security)"**:

https://www.youtube.com/watch?v=Rrd6xkyjPB8&t=23s

The tutorial turns the video transcript into a graduate-level API design module covering:

- API design fundamentals
- API protocols
- TCP and UDP transport tradeoffs
- RESTful API design
- GraphQL API design
- Authentication
- Authorization
- API security

## Artifacts

- `index.html` - GitHub Pages entrypoint for the interactive tutorial.
- `api_design_grad_tutorial.html` - standalone interactive tutorial with navigation, diagrams, search, progress tracking, protocol/auth/security drills, and quiz questions.
- `api_design_ta_instructor_guide.md` - instructor-facing guide with lecture pacing, learning objectives, discussion prompts, assignments, and grading rubric.
- `api_design_visual_aids.md` - Mermaid diagram packet for slides, recitation, or handouts.
- `manifest.md` - source basis, prompt record, limitations, and generated output index.

## Source Handling

The source video is listed above. A local transcript was used to create the tutorial artifacts, but the raw transcript is not checked into this repository. The generated materials separate transcript-grounded ideas from added instructor expansion where the tutorial fills in deeper technical detail.

## Development Journey

1. Started with the local transcript for the video and preserved the timestamp outline as the teaching structure.
2. Converted the transcript into a standalone interactive HTML tutorial rather than a text-only summary.
3. Added instructor expansion for graduate-level depth: API contracts, idempotency, protocol tradeoffs, GraphQL resolver risks, OAuth/OIDC taxonomy, authorization models, and API threat modeling.
4. Created separate TA materials so the package can support lecture delivery, recitation, assignments, and assessment.
5. Added reusable visual aids for API boundaries, REST request flow, REST vs GraphQL, TCP vs UDP, authentication taxonomy, authorization models, and API security controls.
6. Verified the HTML structure and extracted JavaScript locally. The bundled transcript-artifact verifier was not used as the primary check because this workspace uses a root/source-transcript layout rather than the verifier's expected child-folder layout.

## How to Use

Open the GitHub Pages site:

https://az9713.github.io/api-design-tutorial/

You can also open `api_design_grad_tutorial.html` directly in a browser. No build step or server is required.

For teaching, start with `api_design_ta_instructor_guide.md`, then copy diagrams from `api_design_visual_aids.md` into slides or course notes as needed.
