# Vault Workflows

12 repeatable prompts and processes. Copy the prompt, adjust the context, run it.

---

## 1. Inbox Sweep
*Run at end of day. Keeps 00-INBOX clear.*

```
Process my 00-INBOX folder.

For each note:
- decide if it is a task, idea, resource, project note, or archive item
- suggest the right folder
- add 2 useful tags
- suggest 2 related notes to link
- tell me if anything should become a permanent note
```

---

## 2. Daily Command Center
*One outcome. Everything else is secondary.*

Open today's daily note (`01-DAILY/YYYY-MM-DD.md`).
Write your One Thing. Work from that note all day.
Tasks, links, thoughts, meeting notes, decisions — all land there first.

Template: `09-SYSTEM/templates/daily-note.md`

---

## 3. Meeting Processor
*Paste raw notes. Get action.*

```
Turn this meeting note into:
- key decisions
- action items with owners
- deadlines
- open questions
- links to related projects
- a short summary for the project file
```

Template: `09-SYSTEM/templates/meeting-notes.md`
Save to: `02-PROJECTS/[project-name]/`

---

## 4. Research Ingestion
*Every article, video, or PDF gets a note.*

```
Convert this source into an Obsidian research note.

Include:
- source title
- URL
- date accessed
- 5 key ideas
- what this changes in my understanding
- related notes in my vault
- questions I should explore next
```

Template: `09-SYSTEM/templates/research-note.md`
Save to: `04-RESOURCES/`
If one idea is important enough → permanent note in `03-NOTES/`

---

## 5. Book Notes
*Extract what you can use. Skip the school-report summary.*

Template: `09-SYSTEM/templates/book-notes.md`
Save to: `04-RESOURCES/`

Focus: Main Idea, Ideas I Can Use, Strong Quotes, Connections, What I'll Do Differently.

---

## 6. Project Kickoff
*Every serious project gets its own home.*

Folder structure to create under `02-PROJECTS/project-name/`:
- `project-overview.md`
- `tasks.md`
- `research.md`
- `decisions.md`
- `weekly-updates.md`

Copy from: `02-PROJECTS/_project-template/`

```
Create a project structure for this goal: [GOAL]

Include:
- project overview
- milestones
- first 10 tasks
- likely risks
- resources I should gather
- existing vault notes that may help
```

---

## 7. Decision Journal
*Log decisions before and after. See how you actually decide.*

```
type: decision
date: YYYY-MM-DD
status: open
review_date: YYYY-MM-DD (90 days out)
```

Template: `09-SYSTEM/templates/decision-journal.md`
Save to: `02-PROJECTS/[relevant-project]/decisions.md` or `03-NOTES/`

---

## 8. Writing Activator
*Start from what your brain already collected.*

```
I am writing about: [TOPIC]

Search my vault.

Tell me:
- strongest claim my notes support
- best evidence I already have
- counterarguments inside my notes
- missing research
- 5 possible angles
- notes I should link together
```

Output goes to: `06-OUTPUTS/`

---

## 9. Weekly Review
*Where the system starts feeling calm.*

```
Read my daily notes from this week.

Create a weekly review with:
- what got done
- what stayed open
- decisions made
- ideas worth saving
- projects that need attention
- 3 priorities for next week
```

Template: `09-SYSTEM/templates/weekly-review.md`
Save to: `07-AI/weekly-reviews/YYYY-MM-DD-weekly-review.md`
Link from this week's daily notes.

---

## 10. Vault Audit
*Monthly maintenance as a conversation.*

```
Audit my vault.

Find:
- notes with no links
- projects with no recent updates
- repeated tags
- notes that should become Maps of Content
- old notes that may be outdated
- topics I keep returning to
```

Run once a month. Save output to `07-AI/`.

---

## 11. Morning Brief
*Every morning starts with context.*

```
Read:
- yesterday's daily note
- open loops
- active project files
- tasks due this week
- recent notes from the last 3 days

Create a morning brief with:
- one recommended focus for today
- overdue items
- project pulse
- anything I should not forget
```

Template: `09-SYSTEM/templates/morning-brief.md`
Save to: `07-AI/morning-briefs/YYYY-MM-DD-morning-brief.md`
Link from today's daily note.

---

## 12. Connection Finder
*The heart of the second brain.*

```
Read this note: [[NOTE NAME]]

Search my vault for strong connections.

A strong connection means reading both notes together reveals something new.
Skip obvious same-topic links.

Give me:
- 5 strongest connections
- why each one matters
- what new idea appears when they are read together
- whether I should create a Map of Content
```

Output: add connections directly to the note, or create a new MOC in `05-MAPS/`.

---

## Bases (Dashboard Views)
Use Obsidian Bases to create database views from your notes.

Good uses:
- Active projects dashboard
- Reading list
- Article pipeline
- Decision log
- Content calendar

Create `.base` files in the relevant folder. Filter by `type:` property from note frontmatter.
The `Untitled.base` files in your vault are starting points — rename and configure them.
