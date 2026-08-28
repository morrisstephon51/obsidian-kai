---
type: resource
category: tools-registry
created: 2026-08-28
tags: [tools, repos, ai-agents]
---

# External Repos & Tools

Third-party open-source repos worth reaching for on relevant builds. Not Stefan's own projects — see [[../_ops/important-links|Important Links Registry]] for those. Added 2026-08-28; extend this list as new tools get flagged.

| Repo | What it is | Reach for it when |
|---|---|---|
| [heygen-com/hyperframes](https://github.com/heygen-com/hyperframes) | Node.js (≥22) library for programmatic video frame/timeline composition, from HeyGen | Building or extending video-generation tooling (content automation pipeline, Track 2 content tools) |
| [jo-inc/camofox-browser](https://github.com/jo-inc/camofox-browser) | Anti-detection browser server for AI agents, built on Camoufox (a Firefox fork with C++-level fingerprint spoofing) | An agent needs headless/browser automation that shouldn't get fingerprinted or blocked — scraping, form-filling, research agents (Perplexity/Aeos-style tasks) |
| [Open-LLM-VTuber/Open-LLM-VTuber](https://github.com/Open-LLM-VTuber/Open-LLM-VTuber) | Open-source LLM-powered VTuber/live-avatar stack (voice + LLM + animated character) | Any avatar/persona-driven content or livestream experiment for The Plug AI or content automation |
| [Anil-matcha/Open-Generative-AI](https://github.com/Anil-matcha/Open-Generative-AI) | Open-source AI image/video generation front end — 400+ models across 14 studios via MuAPI, no content filters | Need an alternative/self-hosted image or video generation path outside the current content-machine stack |
| [Fincept-Corporation/FinceptTerminal](https://github.com/Fincept-Corporation/FinceptTerminal) | Bloomberg-terminal-style financial data/analysis app (C++20, Qt6, Python); this repo is the free AGPL-3.0 edition | Finance-adjacent research or tooling comes up (Track 2 Finance goals, market/data analysis) |

## Access note
These are public repos, cloned read-only as needed — not attached with push credentials. If a task grows into an actual fork/contribution, attach with push access at that point rather than by default.
