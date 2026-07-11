# Vault Smart Linking Strategy — Implementation Plan

> **For agentic workers:** RECOMMENDED: Use `superpowers:subagent-driven-development` to implement this plan task-by-task. Each task is self-contained with clear file modifications and testing steps.

**Goal:** Transform the vault into a fully interconnected knowledge graph where every note is discoverable through semantic relationships, enabling both top-down navigation (values→goals→projects→daily) and bottom-up synthesis (daily→weekly→insights→vision refinement).

**Architecture:** Three-phase approach:
1. **Create missing hub files** — Index files for Areas, Projects, Opportunities, Weekly Reviews
2. **Establish bidirectional linking** — Add wikilinks from files to hubs and hubs back to files
3. **Cross-cutting connections** — Link skills to goals, daily work to projects, opportunities to values/goals

**Tech Stack:** Obsidian wiki-links (`[[path/to/file]]`), YAML frontmatter for metadata, backlink generation via edit

## Global Constraints

- **Link format:** Use relative wiki-links only (`[[path/to/file]]` or `[[file-name]]`), never absolute paths
- **Frontmatter:** Maintain existing YAML headers; add `related_to` or `linked_from` metadata where needed
- **Naming:** Follow vault convention (kebab-case, descriptive titles)
- **Backlinks:** Every link must go both directions (A→B means B references A)
- **No broken links:** Test each link after creation; use link checker
- **Current date:** 2026-07-11 for all new files

---

## Phase 1: Create Missing Hub & Index Files

### Task 1: Create Areas Index Files

**Files:**
- Create: `Areas/Career/index.md`
- Create: `Areas/Finance/index.md`
- Create: `Areas/Education/index.md`
- Create: `Areas/Development/index.md`
- Create: `Areas/Personal Growth/index.md`
- Create: `Areas/Learning/index.md`

**Interfaces:**
- Consumes: Existing goal and skill files in each folder
- Produces: Hub files that list all notes in that area with brief descriptions

**Steps:**

- [ ] **Step 1: Create Career Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 🎯 Career

Central hub for all career-related notes, goals, and projects.

## Core Goals
- [[Career Goals]] — Long-term career direction
- [[Competitive Advantages]] — What sets you apart

## Related Areas
- [[../Education/index|Education]] — Unlocks opportunities
- [[../Finance/index|Finance]] — Career drives income
- [[../Development/index|Development]] — Skills enable advancement
- [[../Personal Growth/index|Personal Growth]] — Values guide career choices

## Key Projects
- [[../../02-PROJECTS/The Plug AI Progress|The Plug AI]]

## How This Fits
Career goals are enabled by education, financial goals are enabled by career growth, and all choices flow from values.

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

- [ ] **Step 2: Create Finance Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 💰 Finance

Financial independence and wealth-building goals.

## Core Goals
- [[Financial Goals]] — Path to independence

## Key Milestones
- [Independence number] ← To be filled in

## Related Areas
- [[../Career/index|Career]] — Primary income driver
- [[../Education/index|Education]] — Invests in future earning power
- [[../Personal Growth/index|Personal Growth]] — Values guide financial decisions

## Cross-Links
- See [[../../01-DAILY/Progress Dashboard|Progress Dashboard]] for current status
- See [[../../_ops/master-tracker|Master Tracker]] for today's focus

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

- [ ] **Step 3: Create Education Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 🎓 Education

Educational goals and learning milestones.

## Core Goals
- [[Education Goals]] — Degree timeline and milestones

## Degree Progress
- Program: B.S. Computer Science
- Status: [In progress]
- Timeline: Expected 2028

## Certifications
- Google IT Support
- IBM IT Support
- Google UX Design
- Python (Syracuse)

## Related Areas
- [[../Career/index|Career]] — Degree unlocks opportunities
- [[../Finance/index|Finance]] — Investing in future earning potential
- [[../Development/index|Development]] — Skills development complements formal education
- [[../Personal Growth/index|Personal Growth]] — Continuous learning value

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

- [ ] **Step 4: Create Development Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 🛠️ Development

Skill development, technical mastery, and continuous learning.

## Core Skills
- [[Skills]] — Active skill stack
- [[Competitive Advantages]] — How skills differentiate you

## Related Areas
- [[../Career/index|Career]] — Skills enable career advancement
- [[../Education/index|Education]] — Formal learning complements skill-building
- [[../Personal Growth/index|Personal Growth]] — Learning aligns with values

## Active Projects (Skill Practice)
- [[../../02-PROJECTS/The Plug AI Progress|The Plug AI]] — Full-stack development practice

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

- [ ] **Step 5: Create Personal Growth Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 🌱 Personal Growth

Self-knowledge, values, vision, and psychological understanding.

## Foundation
- [[Core Values]] — Everything flows from here
- [[Life Vision]] — North star for all decisions

## Self-Understanding
- [[../../03-NOTES/Identity/Who I Am|Who I Am]] — Current identity and context
- [[../../03-NOTES/Psychology/Strengths|Strengths]] — Your assets
- [[../../03-NOTES/Psychology/Weaknesses|Weaknesses]] — Areas to develop
- [[../../03-NOTES/Psychology/Motivations|Motivations]] — What drives you
- [[../../03-NOTES/Behavioral Patterns/Communication Style|Communication Style]]
- [[../../03-NOTES/Behavioral Patterns/Decision-Making Style|Decision-Making Style]]

## Challenges & Opportunities
- [[../../03-NOTES/Challenges/Limiting Beliefs|Limiting Beliefs]]
- [[../../03-NOTES/Opportunities/Growth Opportunities|Growth Opportunities]]

## Related Areas
All areas flow from personal growth — your values inform every decision.

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

- [ ] **Step 6: Create Learning Area Index**

```markdown
---
type: area-hub
created: 2026-07-11
---

# 📚 Learning

Resources, guides, and knowledge about systems that support your work.

## Guides
- [[Claude Code Guide]] — How to work with Claude Code in your vault

## Resources
- [[../../04-RESOURCES/Prompts/index|Prompts Library]] — AI prompts and templates
- [[../../07-AI/index|AI Systems]] — AI tools, agents, and automation

## Related Areas
- [[../Education/index|Education]] — Formal learning
- [[../Development/index|Development]] — Skill-building

See [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] for the full picture.
```

---

### Task 2: Create Projects Index & Opportunities Index

**Files:**
- Create: `02-PROJECTS/index.md`
- Create: `Opportunities/index.md`

**Steps:**

- [ ] **Step 1: Create Projects Index**

```markdown
---
type: hub
created: 2026-07-11
---

# 🚀 Projects

All active and inactive projects. Projects are how you advance goals.

## Track 1: Primary Mission

### [[The Plug AI Progress]]
- **Mission:** AI literacy for underserved communities (faith leaders, community health workers, first-gen students)
- **Target:** South suburban Cook County
- **Status:** 🟡 Seeking fiscal sponsor
- **Supports:** [[../Areas/Career/index|Career]] + [[../Areas/Finance/index|Finance]]
- **Skills Built:** Full-stack development, fundraising, nonprofit strategy

## Track 2: Instrumental & Side Projects

### [[Personal Growth/Strengths|Strengths]]
- Status: 🟢 Active
- Purpose: Self-knowledge foundation

### [[Personal Growth/Weaknesses|Weaknesses]]
- Status: 🟢 Active
- Purpose: Self-awareness

### [[Career/Competitive Advantages|Competitive Advantages]]
- Status: 🟡 Foundation building
- Purpose: Differentiator development

## Archived Projects
[Will add as projects complete]

## How Projects Connect to Everything Else

Values & Vision (foundation)
  ↓
Goals (what to achieve)
  ↓
Projects (how you achieve it)
  ↓
Daily Work (execution)
  ↓
Weekly Reviews (patterns)
  ↓
Back to Vision (refinement)

See [[../05-MAPS/Core Relationships Map|Core Relationships Map]] for full architecture.
```

- [ ] **Step 2: Create Opportunities Index**

```markdown
---
type: hub
created: 2026-07-11
---

# 💡 Opportunities

Ideas, grants, partnerships, and potential paths worth exploring.

## Grant Opportunities (Active)

### Illinois "Eliminate the Digital Divide" Program
- **Status:** 🟢 Active — Live Option
- **Amount:** Up to $75K
- **Fiscal Sponsor Path:** Kenneth Vasser's church (MOFEC area)
- **Tracker:** [[../_ops/grant-research-log|Grant Research Log]]
- **Related:** [[../02-PROJECTS/The Plug AI Progress|The Plug AI]]

## Evaluation Framework

When assessing opportunities:
1. Alignment with [[../02-PROJECTS/Personal Growth/Core Values|Core Values]]?
2. Support for [[../02-PROJECTS/Career/Career Goals|Career Goals]] or [[../02-PROJECTS/Finance/Financial Goals|Finance Goals]]?
3. Leverage of existing [[../02-PROJECTS/Personal Growth/Strengths|Strengths]]?
4. Time commitment vs. Track 1/Track 2 balance?

See [[../05-MAPS/Core Relationships Map|Core Relationships Map]] for how opportunities fit your system.
```

---

### Task 3: Create Weekly Reviews Index & Update Daily Notes Index

**Files:**
- Create: `01-DAILY/Weekly Reviews/index.md`
- Modify: `01-DAILY/index.md`

**Steps:**

- [ ] **Step 1: Create Weekly Reviews Index**

```markdown
---
type: hub
created: 2026-07-11
---

# 📊 Weekly Reviews

Aggregate insights, pattern recognition, and feedback loop hub.

## Template
See [[../../09-SYSTEM/templates/weekly-review|Weekly Review Template]]

## How Weekly Reviews Work

Monday–Friday: Daily Notes
         ↓
Saturday: Weekly Review (aggregate)
         ↓
Identify: Patterns, wins, blockers
         ↓
Adjust: Goals, projects, priorities
         ↓
Inform: Vision refinement
         ↓
Next Week: Updated daily work

## Related Hubs
- [[../Progress Dashboard|Progress Dashboard]] — Bird's-eye status
- [[../../_ops/master-tracker|Master Tracker]] — Daily focus
- [[../../05-MAPS/Core Relationships Map|Core Relationships Map]] — System architecture

## Structure
- Each week gets one review note: `YYYY-WXX-review.md`
- Review feeds insights back to [[../Progress Dashboard|Progress Dashboard]]
```

---

## Phase 2: Establish Bidirectional Linking

### Task 4: Link Career Goals ↔ The Plug AI Project ↔ Daily Work

### Task 5: Link Finance Goals ↔ Projects & Daily

### Task 6: Link Education Goals ↔ Skills Development ↔ Career

## Phase 3: Cross-Cutting Connections

### Task 7: Link Values → All Goals

### Task 8: Link 03-NOTES (Psychology/Identity) to Areas

### Task 9: Link Resources (04-RESOURCES) to Projects & Learning

### Task 10: Create 07-AI Index (Agents, Outputs, Briefs)

### Task 11: Link Daily → Opportunities → Decisions → Vision

## Phase 4: Verification & Cleanup

### Task 12: Audit All Links & Fix Broken References
