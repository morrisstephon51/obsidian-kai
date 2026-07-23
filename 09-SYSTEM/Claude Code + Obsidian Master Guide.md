---
type: guide
category: productivity-system
status: living-document
last-updated: 2026-06-12
---

# Claude Code + Obsidian: Master Guide

> How to use Claude Code as your Obsidian AI partner and build an effective second brain.

---

## Part 1: Directing Claude Code to Obsidian

### How Claude Code Works with Your Vault

I (Claude Code) have direct access to your Obsidian vault at `/Users/abdoulayemundow/Desktop/kai`. I can:

- ✅ **Read** any markdown file in your vault
- ✅ **Write** new files to your vault
- ✅ **Edit** existing files with surgical precision
- ✅ **Understand** your vault structure, links, and frontmatter
- ✅ **Create** wikilinks (`[[note]]`) that work in Obsidian
- ✅ **Respect** relative paths (no absolute paths needed)

### The Three Ways to Direct Me

#### Method 1: Direct Vault Commands (What I Prefer)

Tell me exactly what you want done with file paths:

```
Create a note at "02-PROJECTS/Learning/Claude Code Guide.md" with sections on:
- How to work with me
- Best practices
- Common commands
```

**What I'll do:**
- Create the file with proper structure
- Use relative paths automatically
- Add wikilinks where appropriate
- Follow your vault conventions

#### Method 2: Selection Context (Use Obsidian Editor)

**In Obsidian:**
1. Open a note
2. Select text (or position cursor)
3. Send message to Claude Code with context

**What you include in your message:**
```
I selected this text in my note:
[your selected text here]

Can you help me organize this into a decision matrix?
```

**What I'll see:**
- The file path you're working in
- The exact lines you selected
- Your exact request
- I can edit that specific file

#### Method 3: Asking About Your Vault Structure

```
What notes do I have in Areas/Development/?
How many backlinks does me.md have?
Which files mention "financial independence"?
```

**I'll:**
- Search your vault
- Report findings
- Suggest improvements
- Create links between related notes

---

## Part 2: Building an Effective Second Brain

### Core Principle: P.A.R.A.

Your vault already uses this! Here's how it works:

```
📁 Vault Root (00 Home.md)
├── 🎯 Projects/        → Active work with deadlines
├── 📍 Areas/           → Ongoing responsibilities  
├── 📚 Resources/       → Reference material
└── 📦 Archive/         → Completed work
```

**Why this works:**
- Clear separation of concern
- Easy to find things
- Natural workflow (Projects → Archive)
- Scales as vault grows

### The Four Types of Notes

#### 1. **Hub Notes** (Dashboard/Index)

**Purpose:** Navigation and overview

**Your examples:**
- `00 Home.md` — vault entrance
- `me.md` — personal dashboard
- `Areas/Development/` — area index

**How to create:**
```markdown
# Development Hub

## Active Projects
- [[project-name]]

## Key Areas
- [[skill-one]]
- [[skill-two]]

## Recent Work
- [[note-a]]
- [[note-b]]
```

#### 2. **Atomic Notes** (Single Idea)

**Purpose:** One clear concept/decision/insight

**Examples:**
- "Why Financial Independence Matters to Me"
- "Decision: Choose TypeScript for Next Project"
- "Insight: Systems Thinking Applied to Career"

**Structure:**
```markdown
---
type: insight
created: 2026-06-12
related: [[core-value]], [[financial-goals]]
---

# [Clear, Specific Title]

## The Core Idea

[One paragraph explaining the idea]

## Why It Matters

[Personal relevance]

## Related

- [[connected-note-1]]
- [[connected-note-2]]
```

#### 3. **Reference Notes** (Lookup/Evergreen)

**Purpose:** Information you refer back to

**Examples:**
- "Healthcare Program Guide"
- "JavaScript Async Patterns"
- "Chicago Nonprofit Resources"

**Structure:**
```markdown
# [Topic] Reference

## Quick Facts
- Fact 1
- Fact 2

## Detailed Information
[Organized by subtopic]

## Sources
- [Link 1]
- [Link 2]

## Last Verified
2026-06-12
```

#### 4. **Timeline Notes** (Journal/Reflection)

**Purpose:** Capture moments, decisions, reflections

**Examples:**
- Daily notes
- Project retrospectives
- Yearly reviews

**Structure:**
```markdown
---
date: 2026-06-12
type: daily-note
---

# 2026-06-12

## 🎯 Focus
- [main goal today]

## 📝 Notes
[what happened, learned, noticed]

## 🔗 Related
- [[project-name]]
- [[decision-made]]

## 📊 Reflection
[end-of-day thinking]
```

---

## Part 3: Linking Strategy

### The Three Types of Links

#### 1. **Hierarchical Links** (Structure)

Navigate down through your organization:
```markdown
[[Areas/Development/|Development]] 
→ [[Areas/Development/architect-agent|Architect Agent]]
→ [[Areas/Development/architect-agent/performance-notes|Performance]]
```

#### 2. **Semantic Links** (Meaning)

Connect ideas by relationship:
```markdown
This relates to [[core-values|my core values]] 
because I value [[truth-seeking]].

This could be a [[business-opportunity]] 
using my [[competitive-advantages]].
```

#### 3. **Backlinks** (Discovery)

Let Obsidian show you what's connected:
- Every file shows "Linked mentions" at bottom
- See what mentions your current note
- Discover unexpected connections

---

## Part 4: The Workflow

### Creating a New Note (Step by Step)

**Step 1: Tell me what you want**
```
I want to capture my thoughts on whether to pursue 
a bootcamp vs completing my degree. I'm torn between 
speed (bootcamp) and credential weight (degree).
```

**Step 2: I'll ask clarifying questions** (if needed)
```
Should this go in:
- Areas/Education/[decision-note]?
- Daily Notes/[dated-reflection]?
- Or link to both?

What's your timeline for this decision?
```

**Step 3: I create the note**
- Proper location in your vault
- Relevant wikilinks
- Connected to existing notes
- Formatted for readability

**Step 4: You review and adjust**
- Open in Obsidian
- Add/remove links
- Refine language
- Mark as complete

### Processing External Information

**When you have information from ChatGPT/web/conversation:**

```
I have information about [topic]. 
Can you help me:
1. Extract the key insights
2. Create atomic notes for each
3. Link them to my existing knowledge
4. Put them in the right folders
```

**What I'll do:**
- Break down into digestible pieces
- Create properly located files
- Add relevant backlinks
- Suggest how it connects to your goals

---

## Part 5: Key Features & Tricks

### Frontmatter (Metadata)

Add to top of notes for searchability and organization:

```yaml
---
type: insight | reference | project | daily-note
status: active | archived | in-progress
created: 2026-06-12
updated: 2026-06-12
tags: #finance #independence #decision
related: [[note1]], [[note2]]
priority: high | medium | low
confidence: high | medium | low
---
```

**Uses:**
- Filter notes by type
- Track status
- Add context for Obsidian plugins
- Help me understand your intent

### Dataview Queries

Create dynamic lists that auto-update:

```dataview
LIST
FROM "Areas" OR "Projects"
WHERE status = "active"
SORT created DESC
```

**I can create these for you** to automatically show:
- Active projects
- Recent decisions
- Learning progress
- Goal status

### Templates

Save time with consistent formats:

```markdown
---
type: atomic-note
created: <% tp.date.now() %>
---

# [Title]

## Core Idea
[explanation]

## Why It Matters
[personal relevance]

## Related
[backlinks]
```

---

## Part 6: Best Practices

### ✅ Do This

- **Atomic notes:** One idea = one file
- **Clear titles:** "Why I Chose TypeScript" not "Note on TypeScript"
- **Link liberally:** Connect related ideas
- **Use frontmatter:** Track metadata
- **Date your work:** Know when you created things
- **Review regularly:** Reflect on notes monthly
- **Archive ruthlessly:** Move completed projects
- **Standardize structure:** Similar notes have similar format

### ❌ Don't Do This

- **Massive files:** Keep individual notes <2000 words
- **Vague titles:** "Stuff" or "Thoughts" — be specific
- **Orphaned notes:** Every note should link to something
- **Mixed purposes:** Don't put a project checklist in a philosophy note
- **Dead links:** Update wikilinks when moving files
- **Neglect:** Review and refactor monthly
- **Over-tagging:** 2-3 tags per note, not 20

---

## Part 7: Common Workflows with Claude Code

### Workflow 1: Capture & Process

**Scenario:** You have raw information (from ChatGPT, conversation, etc.)

**Tell me:**
```
I have raw information about [topic]. 
Process it into my vault:
1. Extract key insights
2. Create atomic notes
3. Link to relevant existing notes
4. Place in appropriate folders
```

**What I'll do:**
- Create properly structured notes
- Add frontmatter
- Create wikilinks
- Organize in correct folders
- Suggest improvements

### Workflow 2: Connect Knowledge

**Scenario:** You want to find relationships between notes

**Tell me:**
```
Show me all connections between:
- [[Financial Goals]]
- [[Career Goals]]  
- [[Education Goals]]

Create a synthesis note showing how they support each other.
```

**What I'll do:**
- Search relevant notes
- Find connections
- Create hub note
- Add cross-references

### Workflow 3: Review & Refactor

**Scenario:** Vault is getting messy

**Tell me:**
```
Review my Areas/ folder. 
Are there:
- Notes that should be archived?
- Notes that could be better organized?
- Missing connections between notes?
- Outdated information?

Give me a report and suggestions.
```

**What I'll do:**
- Audit your vault
- Identify issues
- Suggest reorganization
- Report improvements

### Workflow 4: Create Decision Framework

**Scenario:** You're facing a decision

**Tell me:**
```
I'm deciding between [option A] and [option B].
Create a decision framework note that:
1. Lists criteria
2. Scores each option
3. Links to relevant values/goals
4. Leaves space for reflection
```

**What I'll do:**
- Build decision matrix
- Link to your values
- Add reflection space
- Create actionable next steps

---

## Part 8: Commands to Use with Me

### File Operations

```
"Create a new note at Areas/Learning/[topic].md"
→ I'll create it, properly formatted

"Move notes from Areas/Old to Archive/Old"
→ I'll reorganize and update links

"Delete Daily Notes older than 2026-01-01"
→ I'll clean up safely

"Rename Areas/Dev to Areas/Development"
→ I'll update all links
```

### Content Operations

```
"Add this information to Areas/Finance/[topic].md"
→ I'll integrate it, preserving existing content

"Create a summary of all my goals from Areas/"
→ I'll synthesize a hub note

"Find conflicts between my goals and my fears"
→ I'll search and report findings

"Create a 90-day plan based on [[Long-Term Goals]]"
→ I'll create actionable breakdown
```

### Search & Analysis

```
"What files mention 'independence'?"
→ I'll find and summarize

"Show me my decision history"
→ I'll aggregate decisions made

"What opportunities use my [[Competitive Advantages]]?"
→ I'll connect dots for you

"Which areas need more development?"
→ I'll audit your vault structure
```

### Link Operations

```
"Create reciprocal links between [[me.md]] and [[Areas/]]"
→ I'll build connection map

"Show me orphaned notes (no links)"
→ I'll find unconnected notes

"Create a hub note for [[Career Goals]]"
→ I'll build index of related notes
```

---

## Part 9: Your Vault Right Now

### Current Structure

```
✅ 00 Home.md              — Main dashboard
✅ me.md                   — Personal profile
✅ Projects/               — Active work
✅ Areas/                  — Ongoing areas
✅ Resources/              — Reference material
✅ Archive/                — Completed work
✅ Daily Notes/            — Day-to-day reflections
✅ copilot/                — Custom prompts
```

### Next Steps to Complete

1. **Create Area Hubs** (for each area):
   - Areas/Development/index.md
   - Areas/Finance/index.md
   - etc.

2. **Create Goal Tracking**:
   - Areas/Goals/[specific-goal].md
   - Link to [[me]]

3. **Set Up Daily Practice**:
   - Template for daily notes
   - Weekly review process
   - Monthly synthesis

4. **Build Knowledge Graph**:
   - Atomic notes from [[me]]
   - Connect to projects/areas
   - Create feedback loops

---

## Part 10: The Second Brain Mindset

### What Makes a Second Brain Work

**1. Trust the System**
- Capture everything (no "I'll remember")
- Trust it will be findable
- Review regularly

**2. Link Aggressively**
- Every note connects to something
- Follow your curiosity
- Let serendipity happen

**3. Refactor Regularly**
- Monthly: Read old notes
- Quarterly: Reorganize
- Yearly: Archive and reflect

**4. Make It Habit**
- Daily capture (5 min)
- Weekly review (15 min)
- Monthly synthesis (30 min)

### The Compounding Effect

**Month 1:** "This is interesting but I'm not sure why"
**Month 3:** "Oh! This connects to that goal"
**Month 6:** "I see a pattern across three areas"
**Month 12:** "This vault has become my competitive advantage"

---

## Quick Reference: How to Talk to Me

### ✅ Good Requests

```
"Create a note at Areas/Finance/[topic] with sections on: [a], [b], [c]"
→ Clear, specific, actionable

"I selected some text in [[my-note]]. Can you restructure it as a comparison table?"
→ Uses selection context effectively

"Show me what links to [[me.md]] and suggest improvements"
→ Audit + recommendation

"Process this ChatGPT output into 3 atomic notes in my Areas/ folder"
→ Clear input, clear output location
```

### ❌ Unclear Requests

```
"Make my vault better"
→ Too vague — what specifically?

"Add some notes about my goals"
→ Which goals? Where? What format?

"Fix my organization"
→ What's broken? What's the goal?
```

### 🎯 Clear Request Formula

```
I want to [action: create/edit/organize/analyze/connect]
[what: specific topic/file/section]
[where: specific folder/location]
[why: what's the purpose?]
[details: any special requirements?]
```

**Example:**
```
I want to create an atomic note about my decision to pursue a degree,
place it in Areas/Education/,
because I need to reference this decision when evaluating opportunities,
and it should link to [[me.md]], [[career-goals]], and [[long-term-goals]].
```

---

## Resources

### Internal (in your vault)
- [[00 Home.md]] — Your vault entrance
- [[me]] — Your personal profile
- [[Projects/]] — Active work
- [[Areas/]] — Ongoing responsibilities

### External (to learn more)
- Obsidian Docs: https://help.obsidian.md
- Linking Your Thinking: https://www.linkingyourthinking.com
- PARA Method: https://fortelabs.com/blog/para/
- Atomic Notes: https://www.andymatuschak.org/evergreen-notes/

---

## Your Action Items

- [ ] Review this guide
- [ ] Tell me what type of note you want to create first
- [ ] I'll create it properly
- [ ] You review and adjust
- [ ] We iterate until it's perfect

---

**Ready to build your second brain together?**

Send me a message with:
1. What you want to capture or organize
2. Where it should go in your vault
3. How it connects to your goals

I'll handle the structure, formatting, and linking. You focus on the ideas. 🧠✨

*Last updated: 2026-06-12*
