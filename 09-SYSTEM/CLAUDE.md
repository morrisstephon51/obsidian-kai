# CLAUDE.md — Obsidian Vault Instructions & Stefan's Full Context

*Single source of truth. Consolidates vault instructions, operating context, and identity layer. Last updated: 2026-08-06.*

**Vault sync:** `~/Desktop/kai` is a git repo whose remote is **[obsidian-kai](https://github.com/morrisstephon51/obsidian-kai)** (private), auto-committing every few minutes via `git-obsi-sync`. The older `kai-obsidian-vault` repo is **superseded** — last push 2026-07-05. Both `obsidian-git` and `git-obsi-sync` plugins are enabled on purpose; if duplicate or conflicting commits ever appear, that overlap is the first thing to check.

---

## 1. Vault Purpose & Structure

This vault is Stefan's second brain. Goal: connection, synthesis, and better output — not storage.

| Folder | Purpose |
|--------|---------|
| 00-INBOX | Raw captures — thoughts, links, voice transcripts, dumps |
| 01-DAILY | Daily command center — one note per day |
| 02-PROJECTS | Active work — articles, business ideas, research, client work |
| 03-NOTES | Permanent notes — one idea per note, written in your own words |
| 04-RESOURCES | Source material — articles, books, PDFs, videos, course notes |
| 05-MAPS | Maps of Content — topic pages linking related notes |
| 06-OUTPUTS | Finished work — essays, scripts, reports, frameworks |
| 07-AI | AI-generated briefs, audits, summaries, connection reports |
| 08-ARCHIVE | Completed or inactive material |
| 09-SYSTEM | Templates, prompts, CLAUDE.md, setup files |

**Note rules:**
- Markdown only. Clear titles. Frontmatter properties at the top.
- Link related notes with `[[wikilinks]]`.
- Permanent notes: one main idea, connects to at least two other notes.
- Use templates from `09-SYSTEM/templates/` when creating new notes.

**AI rules:**
1. Search relevant vault notes before answering.
2. Prefer Stefan's own notes over general internet answers.
3. If the vault doesn't answer something, name what's missing.
4. When creating a new note, follow existing folder and naming rules.
5. Save useful AI outputs into `07-AI/`.

**Agent authority:** Kai (clawd/OpenClaw) has full read/write autonomy across the entire vault — every folder, including the personal PKB folders under `03-NOTES`. No standing approval required. The Plug AI stays Track 1 for *prioritization* when work is ambiguous — that's about what gets done first, not what Kai is allowed to touch.

---

## 2. Who Stefan Is — Current Reality

*This section is ground truth. Don't re-litigate what's already been decided.*

**Name:** Stefan. Goes by Stef.
**Location:** Chicago area (south suburban Cook County)
**Day job:** BigHeart Health — Training Development & Design. The funding bridge, not the destination.
**Primary mission:** Founder of **The Plug AI** — AI literacy for faith communities, community health workers, and first-gen students in south suburban Cook County.
**Education:** Pursuing B.S. Computer Science (expected 2028). Certifications: Google IT Support, IBM IT Support, Google UX Design, Python (Syracuse).

**Active tracks:**
- **Track 1 — The Plug AI:** Brand, PRD, entity-path analysis, and Kresge Foundation LOI are done. Kresge Fluxx portal live (username: The_Plug_AI). Site live at [theplugai.info](https://theplugai.info); content-hardening pass complete 2026-07-13. Blocked on fiscal sponsor / 501(c)(3) partner for the Illinois "Eliminate the Digital Divide" grant (up to $75K). Kenneth Vasser's church is the live option — need legal name, address, pastor confirmation, workshop date before applying. Full detail: [[02-PROJECTS/The Plug AI/project-overview|project overview]].
- **Track 2 — Everything else:** BigHeart (funds Track 1), **Forming Paws** (dog breeding matchmaking — **the full Next.js app is live at [theplugai.xyz](https://theplugai.xyz)** as of 2026-08-11: accounts, health-doc verification, browse, matching, owner chat. GitHub Pages retired; the old "local-only by design" rule is dead. Repo public. "Puppy Power" is the crowdfunding name for the same product), content automation tooling. Real and managed — don't expand Track 2 without naming the tradeoff.
- **Track 3 — AI Implementation Consulting (for-profit):** Dual-niche — law-firm intake automation + small-business apps/sites. Built out at `~/ai-consulting-business/` on 2026-07-17, not yet launched. **Is** backed up to a private GitHub repo ([ai-consulting-business](https://github.com/morrisstephon51/ai-consulting-business), last push 2026-08-06) — the older "not committed to git" note is obsolete. Separate from Plug AI and BigHeart; don't conflate funding, branding, or docs. Full detail: [[02-PROJECTS/AI Consulting Business/project-overview|project overview]].

**Governance layer:** The **OpenClaw AI Organization** plan (owner: Kairo) sits above the agent fleet — 30+ docs at `~/clawd/AI-Organization/`. Phase 2 live and launch-ready on the Claude path (ADR-008); one blocker reopened 2026-08-09 — the OpenAI/ChatGPT leg is `credit_balance_exhausted` (NON-BLOCKING: code-gen defaults to Claude/OAuth, OpenAI activates via `--override gpt-4o-mini` once funded). **Formal Track 1 execution is gated on Oct 13**, after Phases 2–4 complete.

**What's settled — don't relitigate:**
- The security-vs-freedom conflict is over. Plug AI is the priority. BigHeart is instrumental.
- Workstream sprawl (6–7 simultaneous initiatives) is the diagnosed bottleneck. Two-track system exists to fix it.
- He doesn't need more opportunities found. He needs execution on chosen ones.
- All Track 2 items get named explicitly here when discovered — don't let a project stay invisible.

---

## 3. What He's Building

### The Plug AI
- **Mission:** Close the AI literacy gap for people the tech world forgot.
- **Tagline:** "Get Connected. Get Skilled. Get into AI."
- **Brand:** Deep Space (#0B0B1A), Amber Gold (#F4B942), Electric Indigo (#5B4FE8).
- **Voice:** Short declarative sentences. No corporate language. No dashes/hyphens. Recurring phrases: "the gap," "people like me," "people the tech world forgot," "The plug is in."
- **Funding reality:** Illinois Digital Equity Capacity Kickstarter Grant — terminated. Open Collective Foundation — shut down. Open Source Collective — rejected. Live option: Illinois "Eliminate the Digital Divide" program, up to $75K. Kenneth Vasser's church is the current fiscal sponsor path.
- **Content:** Faith-community angle is best-performing LinkedIn content by a wide margin.
- **Known risk:** Church access (MOFEC, All Nations, Faith Mission, Holy City) was built through BigHeart relationships. Approaching those churches about Plug AI without disclosing BigHeart is professional exposure. Two paths: (1) fold Plug AI into BigHeart as a formal internal initiative, or (2) build proof-of-concept with churches that have zero BigHeart overlap.

### BigHeart Health
- "My Health My Power" initiative — AI-assisted outreach across four church partnerships.
- Stefan built and pitched a content automation machine (videos, flyers, social, training materials) to leadership — seeking title change to "Digital Content and AI Systems Specialist" plus comp adjustment.

### Forming Paws (Track 2)
Health-first nonprofit platform for documented, responsible dog breeding. Chicago, IL, built on $0 capital.
- **Public site:** [theplugai.xyz](https://theplugai.xyz) — GitHub Pages static site + `/join.html` signup. This is the shareable link.
- **Repo:** [morrisstephon51/forming-paws](https://github.com/morrisstephon51/forming-paws) — public. Static site on `gh-pages`, Next.js app on `main`.
- **The real app is local-only** at `~/forming-paws` — Next.js 15 + Supabase (`wyzcnkdonbdykidmcxvx`). Owner accounts, dog profiles, health-doc verification with admin review, geolocation `/browse`, mutual-match `/matches`. Migrations at 0018. Slice 1 complete. Unhosted deliberately per the 2026-07-22 decision — **don't propose deploys unless Stefan reopens it.**
- **Recurring bug pattern:** PostgREST embedded-selects get silently RLS-filtered by an unrelated table. Has bitten three times. Any new query joining through `dogs` for a non-owner viewer must go through `dogs_browsable`, not the base table.

### Tools Built
- Content automation pipeline (Next.js, Supabase, Remotion, FAL, Pexels, Vercel, Composio) — live at content-machine-wine.vercel.app (legacy; repo archived, agents ported to `psychic-bassoon/content-engine`)
- Training Asset Studio — done-for-you training packages for nonprofits ($350–$750/package)
- MUNDI — task router (`~/clawd/router/`), outputs to `07-AI/chatroom/feed.md`
- MUNDI Agent Dashboard — live at [theplugai.live](https://theplugai.live), status-only Edge Config sync from this Mac every 5 min

### Agent System — 8 Supervisors (roster 2026-07-09, statuses corrected 2026-08-03)

⚠️ **Orchestrator, Architect, Aexis, and Aeos were listed "active" for six weeks while completely broken** — all four called the raw Anthropic API and failed instantly with `ANTHROPIC_API_KEY not set`. This system has **OAuth only** via the `claude` CLI; there is no API key. Fixed 2026-08-03 by rewiring each to shell out to `claude -p`. Verified live. Treat "active" as meaning *someone ran it and saw output*, nothing less.

**Archived:** `gemini-agent` (moved to `~/clawd/agents/_archived/` — key worked but the Google Cloud project had zero free-tier quota, HTTP 429 `limit: 0` on every call; needed a billing decision, not a code fix).

| Agent | Role | Bus name |
|-------|------|----------|
| **Kai / clawd** | Coordinating hub — always-on, Telegram-connected | `clawd` |
| **Orchestrator** | Pipeline management — decomposes goals, sequences tasks across supervisors | `orchestrator` |
| **Architect** | System design — Full mode (Plug AI) / Lite mode (BigHeart) | `architect` |
| **Codex** | Code generation, PRs, bug fixes — builds what Architect designs | `codex` |
| **Antigravity** | Content, LinkedIn posts, strategy drafts | `antigravity` |
| **Perplexity** | Real-time research, citations, current events | `perplexity-agent` |
| **Aexis** | Execution accountability — open loops, stalled work, overdue follow-ups | `aexis` |
| **Aeos** | Strategic intelligence — synthesizes research into briefs, monitors grant landscape | `aeos` |

Standard build pipeline: `Orchestrator → Architect → Codex`
Scripts: `~/clawd/agents/<name>-agent/run.js` | State: `07-AI/agents/<name>/state.md` | Feed: `07-AI/chatroom/feed.md`

---

## 4. How to Work With Stefan

**Response shape:** Direct answer first → reasoning → alternatives → action plan. Encouraging tone, no hedge-speak, no filler.

**Operating rules:**
1. **Plan before building.** For anything non-trivial (3+ steps or an architectural call), lay out the plan first. If something goes sideways mid-build, stop and re-plan.
2. **Find root causes. No band-aids.** Senior-level standard: minimal-impact fixes, no side effects.
3. **Don't ask for hand-holding on bugs.** Given a bug report, logs, or a failing test — just fix it.
4. **Prove it works before calling it done.** Run it, check output, diff behavior.
5. **Full autonomy on repos.** No standing approval gate. Stefan will course-correct if needed.
6. **Two-track discipline.** If a task doesn't serve Plug AI or the BigHeart bridge, flag it as Track 2 before going deep.
7. **Four-voice council lens:** Weigh ideas through — RAZOR (harsh critic, exposes flaws), VAULT (cautious strategist, risk-first), PULSE (cuts through Stefan's own bias, advocates for what he actually needs), FORGE (builder — ships working solutions). Take positions, don't hedge.

---

## 5. Identity & Psychology (Deeper Layer)

### Core Identity Themes
- **Truth Seeker** — challenges assumptions, looks for root causes, questions frequently
- **Builder** — focused on creating options and leverage, not consuming info
- **Helper** — core value is helping others navigate complex systems
- **Escaping Dependence** — reducing reliance on employers, institutions, debt, bureaucracy

### Core Values
Freedom · Competence · Truth · Self-reliance · Impact · Continuous learning

### Primary Strengths
Persistent curiosity · Systems thinking · Resourcefulness · Empathy · Pattern recognition · Cross-domain learning

### Primary Obstacles
Over-analysis paralysis · Isolation · Attraction to too many opportunities · Information-seeking instead of acting · Periodic pessimism

### Blind Spots
- Searching for the perfect path instead of committing
- Underestimating the value of consistency and incremental progress
- Seeking certainty before taking action

### Internal Conflicts

| Conflict | Status |
|----------|--------|
| Security vs Freedom | **Resolved** — BigHeart funds The Plug AI; choice is made |
| Helping vs Wealth | Active — The Plug AI attempts to hold both |
| Learning vs Executing | Active — main bottleneck; two-track system is the fix |
| Focus vs Sprawl | Active — critical pattern to watch |

### Decision-Making Style
Research-heavy · Evidence-seeking before commitment · Risk-aware but strategic · Seeks leverage and optionality

---

## 6. Background (Context, Not Identity)

Healthcare ops (Mount Sinai Hospital), education tech (Apollo After Schools), client success, hospitality management, residential treatment specialist. History of using structured mentorship frameworks with AI to build skills and ship portfolios. Interest in blockchain at a foundational level. Loves classical piano and boogie-woogie — connects through musical frequency, not notation.

**Trajectory:** Survival → Stability → Leverage → Independence

**Success definition:** Having enough freedom, capability, and resources to choose your path while helping others.

---

*Updated: 2026-08-06. Consolidated from CLAUDE.md + context.md + me.md. Canonical copy lives at `~/Desktop/kai/09-SYSTEM/CLAUDE.md`. The separate context.md at `~/Desktop/Context/` remains authoritative for the multi-agent system — this file is the Obsidian vault copy.*

**2026-08-06 refresh:** added Track 3 (AI consulting), the OpenClaw governance gate, the corrected Forming Paws status (site live, app local-only), the 2026-08-03 broken-supervisor correction, gemini-agent's archival, and the vault's remote change. Live-verified against `gh`, Vercel, DNS, and HTTP — see [[_ops/important-links|Important Links]] and [[09-SYSTEM/Command Center|Command Center]].
