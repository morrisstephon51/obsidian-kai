# Agent World — Shared Context

*Read this at the start of every loop. This is the world state all agents share.*

Last updated: 2026-06-21

---

## Mission

**The Plug AI** — closing the AI literacy gap for faith communities, community health workers, and first-gen students in south suburban Cook County, Chicago.

**Tagline:** "Get Connected. Get Skilled. Get into AI."

**Priority order:** Track 1 = The Plug AI. Track 2 = BigHeart, Puppy Power, side projects.

---

## Active Agents

| Agent | Role | Status |
|-------|------|--------|
| clawd / OpenClaw | Always-on gateway · Telegram coordinator | running |
| MUNDI | Dashboard governor · Claude Code | active |
| Codex | Coding agent (per-task) | idle |
| Antigravity | General agent (per-task) | idle |
| Content Pipeline | Video, social, training content | idle |
| Enrollment Funnel | BigHeart health enrollment | idle |
| JobScout | Job opportunity scanning | idle |
| Community Intake | Community routing & resources | idle |

---

## Current Priorities

1. The Plug AI — brand, funding, launch
2. BigHeart — content automation + title/comp ask
3. Puppy Power — execution phase (Track 2, managed in clawd)

---

## Governance

- **MUNDI** governs the dashboard world
- **clawd/OpenClaw** coordinates agents via the bus (SQLite)
- **Bus location:** `~/clawd/.bus/busctl.js`
- **LLM Council:** RAZOR · VAULT · PULSE · FORGE (weigh all major decisions through these four voices)

---

## Rules All Agents Follow

1. Read this file + context.md + me.md at loop start
2. Check bus for unread messages at loop start
3. Post meaningful work to bus at loop end
4. Acknowledge bus at loop end
5. Update own state.md with status, last_run, current_task, items_processed
6. Write to chatroom/feed.md when socializing or reporting
