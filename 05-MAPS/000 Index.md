---
type: index
created: 2026-06-23
---

# 000 Index — Vault Reference

This file is the authoritative map of the vault. Any AI assistant or human managing this vault should read this first. Update it whenever folders or tags are added.

**Vault owner:** Stefan (Abdoulaye Mundow)
**Vault path:** `~/Desktop/kai/`
**Methodology:** PARA + Zettelkasten + Personal Knowledge Base

---

## Folder Structure

```
kai/ (vault root)
│
├── 000 Index.md              ← THIS FILE — always read first
├── 00 Home.md                ← Daily dashboard, quick links
├── me.md                     ← Personal profile shortcut
│
├── Areas/                    ← Ongoing life domains (PARA: Areas)
│   ├── Career/               ← Career strategy, goals, competitive edge
│   ├── Development/          ← Technical skills, coding, learning
│   ├── Education/            ← Formal education, certifications
│   ├── Finance/              ← Financial goals, independence path
│   └── Personal Growth/      ← Values, vision, strengths, weaknesses
│
├── Projects/                 ← Active, time-bounded projects (PARA: Projects)
│   └── The Plug AI/          ← The Plug AI platform project
│
├── Resources/                ← Reference material, assets (PARA: Resources)
│   ├── Brand Assets/         ← Logos, visual identity for The Plug AI
│   ├── Originals/            ← Raw, unedited source material (articles, transcripts, dumps)
│   └── Prompts/              ← Saved AI prompts and workflows
│
├── Archive/                  ← Completed or inactive material (PARA: Archive)
│   └── Web Dev Notes/        ← Old HTML/CSS learning notes
│
├── Daily Notes/              ← Daily journals and check-ins
├── Templates/                ← Note templates
│
├── _ops/                     ← Operational tracking files
│   ├── master-tracker.md     ← Active projects and today's focus
│   ├── daily-template.md     ← Daily note template
│   ├── grant-research-log.md ← Funding opportunity tracker
│   ├── important-links.md    ← Registry of critical external links
│   └── link-health-checker.md ← Weekly link verification
│
├── pkb/                      ← Personal Knowledge Base (deep self-model)
│   ├── Identity/             ← Who I am, executive summary, personal evolution
│   ├── Psychology/           ← Values, motivations, mental models, decision style
│   ├── Behavioral Patterns/  ← Habits, communication style, recurring themes
│   ├── Assets/               ← Skills, knowledge areas, work experience
│   ├── Challenges/           ← Fears, frustrations, limiting beliefs, risks
│   ├── Life Direction/       ← Long-term goals, life vision, success definition
│   └── Opportunities/        ← Business, career, growth, leverage points
│
├── 07-AI/                    ← AI agent state tracking (do not edit manually) — corrected 2026-07-03, this folder was previously (and incorrectly) documented as "agent-world/", a path that never actually existed on disk
│   ├── agents/               ← Per-agent state files (clawd, codex, antigravity, etc.) — see [[07-AI/MUNDI System Reference]]
│   ├── chatroom/             ← Agent bus feed log
│   ├── context/              ← Shared world context for agents
│   └── agency-agents.md      ← Roster of 233 specialized subagents
│
├── copilot/                  ← Obsidian Copilot plugin custom prompts
├── Attachments/              ← Embedded files (images, PDFs, documents)
└── Apple Notes/              ← Imported Apple Notes (archive)
```

---

## Tag Taxonomy

Tags are applied in YAML frontmatter using `tags: [tag1, tag2]`. Max 3 tags per note.

### Source Tags
| Tag | Use for |
|-----|---------|
| `source` | Original/archival copies in Resources/Originals/ |
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
| `original` | Raw source archive (in Resources/Originals/) |
| `template` | Note template |
| `index` | Index or hub file |
| `reference` | Reference material |

---

## Key Wikilinks

Frequently referenced hub notes:
- `[[me]]` — Personal profile
- `[[00 Home]]` — Daily dashboard
- `[[_ops/master-tracker]]` — Active work tracker
- `[[Areas/Career/index]]` — Career hub
- `[[Areas/Finance/index]]` — Finance hub
- `[[Areas/Development/index]]` — Development hub
- `[[pkb/Personal Knowledge Base]]` — PKB entry point
- `[[Projects/The Plug AI Progress]]` — The Plug AI tracker
- `[[07-AI/MUNDI System Reference]]` — full agent fleet / websites / commands reference (added 2026-07-03)

---

## Notes on Structure

- **`Resources/Originals/`** is where raw source material lands before being broken into atomic notes. If it doesn't exist yet, create it before saving originals.
- **`pkb/`** is a deep self-model — notes here describe Stefan's psychology, patterns, and identity. They are reference notes, not living documents.
- **`agent-world/`** is managed by AI agents and synced automatically — do not edit by hand.
- **`copilot/`** holds Obsidian Copilot plugin prompts — not personal notes.

---

*Last updated: 2026-06-23 — Initial creation via vault scan.*
