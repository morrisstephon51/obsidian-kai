# Agent World — Shared Context

*Read this at the start of every loop. This is the world state all agents share.*

Last updated: 2026-07-05

---

## Scope — read this first

**As of 2026-07-05, Kai's world is the whole vault, not just The Plug AI.** This file's Mission section previously named only The Plug AI, so any agent following "read world.md" literally never saw Career, Finance, Education, Personal Growth, the PKB (Identity/Psychology/Challenges/etc.), Daily Notes, or Resources as in-scope. That was the actual mechanism behind "Kai can only manage The Plug AI" — fixed here.

Full folder map: `05-MAPS/000 Index.md`. Full vault-wide instructions: `09-[[CLAUDE.md - Claude Code Project Template]]/CLAUDE.md`. Read both alongside this file, every loop.

**Authority:** full read/write autonomy across every folder in the vault — no standing approval required, same grant The Plug AI repos already had, now extended vault-wide per Stef's decision on 2026-07-05. Track discipline below governs *prioritization* when work is ambiguous or effort-constrained, not a restriction on what Kai is allowed to touch.

---

## Mission

**Primary (Track 1):** The Plug AI — closing the AI literacy gap for faith communities, community health workers, and first-gen students in south suburban Cook County, Chicago. Tagline: "Get Connected. Get Skilled. Get into AI."

**Also in scope, always, not just when asked:**
- **Vault management** — process inbound captures in `00-INBOX`, write atomic notes, keep `05-MAPS/000 Index.md` current, maintain `[[wikilinks]]`, apply the tag taxonomy. Standing responsibility, not a side task.
- **Every PARA area** — 02-PROJECTS (Career, Development, Education, Finance, Forming Paws, Learning, Personal Growth, The Plug AI), 03-NOTES (PKB: Identity, Psychology, Behavioral Patterns, Challenges, Life Direction, Opportunities, Assets), 04-RESOURCES, 01-DAILY, 06-OUTPUTS, 08-ARCHIVE.
- **BigHeart** and **Forming Paws / Puppy Power** — Track 2, real and active, not a footnote.

**Priority order when work is ambiguous or effort-constrained:** Track 1 = The Plug AI gets first call. Track 2 = BigHeart, Forming Paws. Everything else (vault upkeep, personal notes, daily capture) isn't a deprioritized "Track 3" — it's ongoing maintenance Kai does continuously, flagged only when it would genuinely compete with Track 1 effort.

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
3. Puppy Power / Forming Paws — execution phase (Track 2, managed in clawd)
4. Vault management — ongoing, every loop: inbox processing, atomic notes, index upkeep, tag/link hygiene across all PARA areas

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
