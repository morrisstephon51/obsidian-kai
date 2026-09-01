---
type: reference
category: skills
created: 2026-08-30
source: ~/.claude/skills (12 personal skills)
last-verified: 2026-08-30
---

# Claude Code Skills Inventory

Personal skills installed at `~/.claude/skills/`. These are **on-demand instruction packs**, not agents — nothing here runs on its own. Claude loads one when the task matches its description, or when it is invoked directly as `/<name>`.

Distinct from the [[07-AI/Subagent Registry|233 subagent definitions]] at `~/.claude/agents/`, which are dispatched personas rather than loaded instructions.

← Back to [[09-SYSTEM/Command Center|Command Center]]

---

## ⭐ ultimate — premium scroll-driven landing pages

**Invoke:** `/ultimate`

The headline skill in this inventory, and the reason this page exists. Vendored 2026-08-30 from [nateherkai/scroll-craft](https://github.com/nateherkai/scroll-craft) (MIT, v0.2.0, commit `e957985`).

**Upstream name is `scrollcraft`.** The only local change is the frontmatter `name:` field, so it answers to `/ultimate`. The skill body still calls itself scrollcraft throughout — that is correct, not drift. Full detail in `~/.claude/skills/ultimate/PROVENANCE.md`.

### What it builds

A scroll-driven landing page where scroll is the timeline: video scrubs frame by frame under the wheel, sections pin while their argument advances, rails pan sideways, headlines assemble line by line, the page ground shifts colour, and the pointer moves things that are not scrolling.

It is explicitly built to avoid the two ways AI website output usually fails — forgettable-but-well-behaved, or flashy-with-2.1:1-body-text.

### How it protects against sameness

| Mechanism | What it does |
|---|---|
| **Interview first** | Eight questions, asked and answered, before anything is generated. Refuses to build from an inferred brief |
| **Eight page grammars** | Filmic one-shot, chaptered editorial, live surface, continuous world, typographic poster, gallery, split stage, rhythmic cutlist. Each forbids what the others require |
| **Fingerprint gate** | A new build must differ from every previous build on ≥4 of 6 dimensions: grammar, nav, hero, act shape, close, signature move |
| **Required signature move** | One bespoke interaction per site. A recoloured spotlight does not count |
| **Feeling curve + one peak** | Peak-end rule applied literally. Two adjacent acts with the same feeling means one is filler |
| **Refuse list** | Bans identical feature-card grids, `01 / 06` counters, "scroll to explore" cues, gradient text, em dashes, invented statistics, fake dashboards, AI-purple gradients, and the cream-and-brass artisan palette |

### It verifies its own output

A headless browser walks the finished page at every scroll position, waits for the video playhead to settle, and reports dead scroll, cues that never reach full opacity, per-line contrast measured on the composited page at the brightest frame passing under it, and legs stuck on a poster (a clip that silently never decoded).

### Preflight status on this Mac — verified 2026-08-30

`node ~/.claude/skills/ultimate/scripts/doctor.mjs`

| Check | Status |
|---|---|
| node v25.6.1 | 🟢 ok |
| ffmpeg (487 filters) | 🟢 ok |
| Chrome | 🟢 ok |
| libwebp encoder | 🟡 missing — posters fall back to JPEG, heavier but not fatal |
| playwright-core | 🟡 not installed — `npm i playwright-core` inside the build folder, only needed for the verification pass |
| `KIE_AI_API_KEY` | 🟡 not set — **only** needed to generate imagery. Building from own photos and footage needs no key and no spend |

**Verdict: ready to build today**, bring-your-own-assets. Generated imagery needs a [kie.ai](https://kie.ai) key. Published rates are 28 credits per still, 160 per 5s clip; a six-act page is roughly 520 credits.

### ⚠️ Workspace is per-project, and that weakens the fingerprint gate

Builds land in `<git root>/scrollcraft/`, and `FINGERPRINTS.md` — the record that enforces "no two builds alike" — lives inside that workspace. **A build in `psychic-bassoon` is therefore invisible to a build in `forming-paws`**, so the uniqueness gate only works within one repo.

To make it global across every Plug AI property, set `SCROLLCRAFT_HOME` to one shared path, or drop a `.scrollcraft.json` with a `workspace` key pointing at it. Not done yet — flagged as a decision, not an oversight.

### Builds so far

| Build | Grammar | Shipped as | Status |
|---|---|---|---|
| Command Center | Live surface (real fetch reachability checks) | [Link-inbio#15](https://github.com/morrisstephon51/Link-inbio/pull/15) | Open — needs a real-device check |
| Forming Paws homepage | Worldflight opening → act-mode body hybrid | [forming-paws#63](https://github.com/morrisstephon51/forming-paws/pull/63) | Open — needs Stefan's visual review + e2e |

Both builds live in different repos, so per the per-project workspace note above, neither was ever actually checked against the other by the fingerprint gate — confirmed in practice, not just in theory. Real engine/harness bugs found and worked around while building these (a `position:sticky` cascade break, worldflight's fixed stage never releasing once real content follows it, the verification harness skipping half a hybrid page) are recorded in Claude's own memory system (not this vault) for reuse next time — ask Claude directly rather than looking for a note here.

---

## Full inventory — 12 personal skills

| Skill | Purpose |
|---|---|
| **ultimate** | ⭐ Scroll-driven landing pages (above) |
| **auditing-agents** | Repeatable 4-layer sweep for auditing what's real vs stale across the agent fleet. See [[07-AI/MUNDI System Reference\|MUNDI System Reference]] |
| **refero-design** | Default research-first UI/product design skill. See [[09-SYSTEM/Command Center\|Command Center]] |
| **agent-browser** | Browser automation CLI — navigate, fill forms, screenshot, scrape, QA |
| **computer-use** | Inspect and operate local desktop app windows via accessibility trees |
| **remote-browser** | Drive a local browser from a sandboxed remote machine |
| **cloud** | Browser Use Cloud — hosted API and SDK reference |
| **open-source** | Browser Use open-source Python library reference |
| **orca-cli** | Orca worktrees, terminals, repos, artifacts, embedded browser |
| **orchestration** | Multi-agent coordination — threaded messages, task DAGs, decision gates |
| **find-skills** | Discover and install new skills |
| **self-improving-agent** | Multi-memory architecture that learns from skill runs |

Plugin-provided skills (vercel, figma, supabase, chrome-devtools, superpowers, coderabbit, and others) are **not** listed here — they live under `~/.claude/plugins/` and are managed with `/plugin`, not by editing this inventory.

---

## Adding a skill under a custom slash name

Installing a plugin from a marketplace gives you `/<plugin>:<skill>`, which you cannot rename. To control the slash name, vendor the skill directory into `~/.claude/skills/<yourname>/` and set `name: <yourname>` in the SKILL.md frontmatter.

The tradeoff: `/plugin update` will not maintain a vendored copy. Record the upstream commit in a `PROVENANCE.md` next to it so the next update is a diff rather than a guess — `ultimate` does this.

---

## 🔗 Related
- [[07-AI/Subagent Registry|Subagent Registry — all 233]]
- [[07-AI/Agent Registry - Master Status|Agent Registry — Master Status]]
- [[07-AI/MUNDI System Reference|MUNDI System Reference]]
- [[09-SYSTEM/Command Center|Command Center]]

*Last updated: 2026-08-30*
