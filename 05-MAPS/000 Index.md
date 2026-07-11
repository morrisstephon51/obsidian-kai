---
type: index
created: 2026-06-23
updated: 2026-07-05
---

# 000 Index — Vault Reference

This file is the authoritative map of the vault. Any AI assistant or human managing this vault should read this first. Update it whenever folders or tags are added.

**Vault owner:** Stefan (Abdoulaye Mundow), goes by Stef.
**Vault path:** `~/Desktop/kai/`
**Methodology:** Numbered PARA (00–09) + Zettelkasten
**Agent authority:** As of 2026-07-05, Kai (clawd/OpenClaw) has full read/write autonomy across the entire vault — every folder below, not just The Plug AI. No standing approval required, same grant The Plug AI repos already had. See [[07-AI/context/world|world.md]] and [[world#Agent World — Shared Context]]

[[00 Home#🗂 Vault Map]]

---

## Folder Structure (matches disk as of 2026-07-05 — previous version of this file was stale and described a folder layout that no longer exists)

```
kai/ (vault root)
│
├── 00-INBOX/                 ← Raw captures, unsorted drops (canvases, bases, quick notes)
├── 01-DAILY/                 ← Daily notes, weekly review template, Progress Dashboard
├── 02-PROJECTS/              ← Active, time-bounded projects
│   ├── Career/
│   ├── Development/
│   ├── Education/
│   ├── Finance/
│   ├── Forming Paws/         ← Track 2 — Steph's dog-breeding matchmaking platform
│   ├── Learning/
│   ├── Personal Growth/
│   ├── The Plug AI/          ← Track 1 — primary mission
│   └── _project-template/
├── 03-NOTES/                 ← Permanent notes (Zettelkasten) + Personal Knowledge Base
│   ├── Assets/                   (skills, knowledge areas, work experience)
│   ├── Behavioral Patterns/      (habits, communication style, recurring themes)
│   ├── Challenges/               (fears, frustrations, limiting beliefs, risks)
│   ├── Identity/                 (who I am, executive summary, personal evolution)
│   ├── Life Direction/           (long-term goals, vision, success definition)
│   ├── Opportunities/            (business, career, growth, leverage points)
│   ├── Psychology/               (values, motivations, mental models, decision style)
│   └── Personal Knowledge Base.md  (PKB entry point)
├── 04-RESOURCES/             ← Source material, reference, assets
│   ├── Brand Assets/         (The Plug AI logo variants)
│   ├── Documents/
│   ├── Images/
│   ├── Originals/            ← Raw source drops land here before becoming atomic notes
│   └── Prompts/
├── 05-MAPS/                  ← Topic maps and hubs
│   ├── 000 Index.md          ← THIS FILE
│   ├── 00 Home.md            ← Daily dashboard, quick links
│   └── Core Relationships Map.md
├── 06-OUTPUTS/               ← Finished work
├── 07-AI/                    ← AI agent state tracking (do not edit manually except state.md loop updates)
│   ├── agents/                   Per-agent state files: clawd, codex, antigravity, content-pipeline,
│   │                             gemini-agent, perplexity-agent, plus archived (tools, job-scanner,
│   │                             community-intake, enrollment-funnel)
│   ├── chatroom/feed.md          Agent bus feed log
│   ├── context/world.md          Shared world context — read every agent loop
│   ├── copilot-custom-prompts/
│   ├── morning-briefs/
│   ├── weekly-reviews/
│   ├── agency-agents.md          Roster of 233 specialized subagents
│   └── Subagent Registry.md      Full categorized inventory of the 233
├── 08-ARCHIVE/               ← Inactive material
│   └── Web Dev Notes/
├── 09-SYSTEM/                ← Templates, prompts, instructions
│   ├── CLAUDE.md                 Obsidian Vault Instructions — read this + this file first
│   ├── Command Center.md         Single hub for every live site/repo/agent
│   ├── templates/                8 note templates (daily, meeting, book, decision, research, etc.)
│   └── domains-and-email.md, workflows.md, etc.
└── _ops/                     ← Operational tracking
    ├── master-tracker.md         Active projects and today's focus
    ├── important-links.md        Registry of critical external links
    ├── grant-research-log.md     Funding opportunity tracker
    ├── daily-template.md
    └── link-health-checker.md
```

---

## Tag Taxonomy

Tags are applied in YAML frontmatter using `tags: [tag1, tag2]`. Max 3 tags per note.

### Source Tags
| Tag | Use for |
|-----|---------|
| `source` | Original/archival copies in `04-RESOURCES/Originals/` |
| `article` | Web articles and blog posts |
| `transcript` | Video/audio transcripts |
| `voice-dump` | Raw voice memos or brain dumps |
| `research` | Research papers, reports |
| `resource` | Generic reference material |

### Domain Tags
| Tag | Use for |
|-----|---------|
| `career` | Career strategy, jobs, professional development |
| `education` | Learning, courses, certifications |
| `finance` | Money, income, budgeting, financial independence |
| `health` | Physical and mental health |
| `technology` | Software, tools, engineering concepts |
| `ai` | Artificial intelligence, LLMs, agents |
| `community` | Community work, outreach, partnerships |
| `business` | Entrepreneurship, startup, strategy |
| `design` | UX, visual design, branding |
| `writing` | Writing, content, communication |

### Concept Tags
| Tag | Use for |
|-----|---------|
| `identity` | Self-concept, personal narrative |
| `psychology` | Mental models, cognition, behavior |
| `values` | Core values, ethics, principles |
| `goals` | Goals and intentions |
| `strategy` | Plans, approaches, frameworks |
| `insight` | Key realizations or lessons |
| `decision` | Decision points, tradeoffs |
| `independence` | Autonomy, freedom, self-determination |
| `growth` | Personal or professional growth |
| `opportunity` | Potential paths or leverage points |

### Project Tags
| Tag | Use for |
|-----|---------|
| `the-plug-ai` | The Plug AI platform |
| `bigheart` | BigHeart Health work |
| `forming-paws` | Forming Paws / Puppy Power |
| `llm-council` | LLM Council framework (RAZOR, VAULT, PULSE, FORGE) |
| `clawd` | Clawd agent system |
| `agent-world` | Agent world / MUNDI dashboard |

### Status Tags
| Tag | Use for |
|-----|---------|
| `active` | Currently in progress |
| `archived` | No longer active |
| `draft` | Incomplete, needs more work |
| `seedling` | New idea, not yet developed |

---

## Note Type Field

Every note should include `type:` in frontmatter. Standard values:

| Type | Description |
|------|-------------|
| `atomic-note` | Single-concept Zettelkasten note |
| `project-progress` | Active project tracker |
| `daily-note` | Daily journal entry |
| `operations` | Ops/tracking file |
| `original` | Raw source archive (in `04-RESOURCES/Originals/`) |
| `template` | Note template |
| `index` | Index or hub file |
| `reference` | Reference material |

---

## Key Wikilinks

Frequently referenced hub notes:
- `[[05-MAPS/00 Home|00 Home]]` — Daily dashboard
- `[[09-SYSTEM/Command Center|Command Center]]` — full live-systems hub
- `[[_ops/master-tracker]]` — Active work tracker
- `[[03-NOTES/Personal Knowledge Base|Personal Knowledge Base]]` — PKB entry point
- `[[02-PROJECTS/The Plug AI Progress|The Plug AI Progress]]` — The Plug AI tracker
- `[[07-AI/MUNDI System Reference|MUNDI System Reference]]` — full agent fleet / websites / commands
- `[[07-AI/context/world|world.md]]` — shared agent world context (now vault-wide, not Plug-AI-only)

---

## Notes on Structure

- **`04-RESOURCES/Originals/`** is where raw source material lands before being broken into atomic notes.
- **`03-NOTES/`** (PKB folders: Identity, Psychology, Behavioral Patterns, Challenges, Life Direction, Opportunities, Assets) is a deep self-model — reference notes, not living documents, edited deliberately rather than casually.
- **`07-AI/`** is managed by AI agents and synced automatically — edit `state.md` files only via the loop-update convention documented in each, not by hand otherwise.
- **`.obsidian/copilot`-style plugin config folders are not personal notes** — skip when scanning for content.
- **Track discipline still applies for prioritization, not for exclusion:** The Plug AI is Track 1 and gets first call on ambiguous effort tradeoffs, but every other folder above is now in-scope for Kai to read, organize, and act on — see `07-AI/context/world.md`.

---

*Last updated: 2026-07-05 — corrected to match actual on-disk structure and recorded the full-vault authority grant; previous version (2026-06-23) described a stale pre-restructure folder layout.*
