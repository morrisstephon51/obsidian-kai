---
type: guide
category: claude-code-workflow
created: 2026-06-13
related: [[../Personal Growth/index|Personal Growth]], [[../Development/index|Development]]
---

# 📚 Claude Code Guide

**How to work effectively with me (Claude Code) in your vault.**

---

## 🎯 Part 1: How to Work With Me

### The Three Ways to Communicate

#### **Method 1: Direct Vault Commands (Most Efficient)**

Tell me exactly what you want, with clear file paths and content:

```
Create a new file at "Areas/Career/Project Ideas.md" with:
- Title: [X]
- Sections: [X], [X], [X]
- Links to: [[Career Goals]], [[me]]
```

**What I'll do:**
- Create file in exact location
- Use proper Markdown formatting
- Add wikilinks automatically
- Match your vault style
- Return confirmation

**Why it works:** Explicit = faster execution

---

#### **Method 2: Selection Context (When You're in Obsidian)**

Select text in your vault and send it to me with context:

```
I selected this text in my [[Career Goals]] note:

[your selected text]

Can you reorganize this into a decision matrix?
```

**What I'll see:**
- The file you're in
- The exact lines selected
- Your full request
- I can edit that specific file

**Why it works:** I understand context, can make surgical edits

---

#### **Method 3: Open-Ended Questions (For Research/Thinking)**

Ask questions about your system or request analysis:

```
"Show me all connections between [[Core Values]] and [[Career Goals]]"

"Create a decision framework for [choice]"

"What's missing from my [[Progress Dashboard]]?"
```

**What I'll do:**
- Search your vault
- Analyze patterns
- Make recommendations
- Create new structure if needed

**Why it works:** I can think across your whole system

---

### Communication Formula for Clarity

When you ask me to do something, structure it as:

```
[Action]: Create/Edit/Analyze/Connect/Find
[What]: [Specific file or concept]
[Where]: [Folder location or reference]
[Why]: [What's the purpose?]
[Details]: [Any special requirements?]
```

**Example:**
```
Create an atomic note called "Decision: Bootcamp vs Degree"
in Areas/Education/
because I need to document this major decision
and it should link to [[Career Goals]], [[Financial Goals]], [[Core Values]]
with sections for: Pros, Cons, Alignment, Timeline, Next Steps
```

---

### What I Can Do

✅ **File Operations**
- Create new files with structure
- Edit existing files surgically
- Reorganize files and folders
- Update links across files
- Archive completed work

✅ **Content Operations**
- Write structured content
- Add metadata/frontmatter
- Create templates
- Integrate information
- Format complex structures

✅ **Analysis & Design**
- Map connections in your vault
- Identify gaps or orphaned notes
- Suggest improvements
- Design new structures
- Audit organization

✅ **Automation**
- Generate repetitive content
- Create templates for patterns
- Batch create related files
- Update multiple files

---

### What I Can't Do

❌ **Real-time sync** — I work with snapshots of your vault, not live updates
❌ **Access external data** — Unless you give me the information
❌ **Guarantee current info** — Always verify links/references after changes
❌ **Make decisions for you** — I provide frameworks, you decide

---

## 🏆 Part 2: Best Practices

### 1. Be Specific, Not Vague

❌ **Bad:** "Improve my vault"
✅ **Good:** "Create an index for Projects/ folder with status of each project"

❌ **Bad:** "Add some notes about my goals"
✅ **Good:** "Create atomic notes for each Career Goal with: definition, timeline, blockers, next steps"

---

### 2. Provide Context

**Include:**
- What you're trying to accomplish (not just what you want created)
- Relevant existing notes to link to
- Your naming conventions/style
- Any constraints or preferences

**Example with context:**
```
I want to track my Plug AI project progress weekly.
Create a note at Projects/The Plug AI/Weekly Updates/2026-W25.md
that links to [[../The Plug AI Progress]] 
and uses this template: [paste template]
```

---

### 3. Use the Vault Structure I Built

**Leverage existing folders:**
- `Areas/` — Ongoing responsibilities
- `Projects/` — Active work
- `Daily Notes/` — Reflections
- `Weekly Reviews/` — Pattern aggregation
- `_ops/` — Operations & tracking
- `Opportunities/` — Ideas to evaluate

**Don't create new top-level folders without asking why.**

---

### 4. Keep Links Relative

When I create files, I use relative links:

✅ Correct: `[[../Career/Career Goals]]`
✅ Correct: `[[Core Values]]` (same folder)

❌ Wrong: `/Areas/Career/Career Goals`
❌ Wrong: `/Users/abdoulayemundow/Desktop/kai/...`

---

### 5. Use Frontmatter Consistently

Every note should start with:

```yaml
---
type: [atomic-note/project/guide/etc]
created: 2026-06-13
related: [[link1]], [[link2]]
---
```

This helps:
- Obsidian organize notes
- Track what's connected
- Filter by type

---

### 6. Think in Atomic Notes

One idea = one file

❌ **Bad:** "Create a Career Guide" (too big)
✅ **Good:** "Create notes for: Career Vision, Career Blockers, Career Timeline" (specific)

Why? Smaller notes are:
- Easier to link
- Better for reflection
- More reusable

---

### 7. Link Bidirectionally

When I create connections:

```
Note A → links to → Note B
Note B → links back to → Note A
```

This creates a web, not a hierarchy. Makes discovery easier.

---

### 8. Don't Fear Iteration

It's okay to say:

```
"This structure isn't working. 
Can you reorganize [folder] differently?"

"Can you add [section] to [note]?"

"Let me try [different format]"
```

The vault improves with use.

---

## 🎬 Part 3: Common Commands

### File Creation

**Simple file:**
```
Create "Areas/Learning/Topic.md" with:
- Brief explanation
- Key concepts
- Related files
```

**With template:**
```
Create a daily note at Daily Notes/2026-06-14.md
using the [[_ops/daily-template|daily template]]
```

**Batch create:**
```
Create atomic notes for each of:
- [[Strength 1]]
- [[Strength 2]]  
- [[Strength 3]]

All in Areas/Personal Growth/
```

---

### File Editing

**Add section:**
```
Add a "Next Steps" section to [[02-PROJECTS/Career/Career Goals]]
with: [content]
```

**Replace content:**
```
Update [[Progress Dashboard|Progress Dashboard]]
Career status from [old] to [new]
```

**Add links:**
```
Link [[02-PROJECTS/The Plug AI Progress|Plug AI project]]
to: [[Career Goals]], [[Financial Goals]], [[Strengths]]
```

---

### Analysis & Design

**Find connections:**
```
Show me all files that link to [[Core Values]]
and suggest any missing connections
```

**Audit structure:**
```
Review Areas/ folder:
- Any orphaned notes?
- Any notes that should be linked?
- Any missing indices?
```

**Create framework:**
```
Create a decision framework for [decision]
that links to [[Core Values]] and [[Life Vision]]
and shows: Pros, Cons, Alignment, Timeline
```

---

### Integration Commands

**Process external info:**
```
I have [description of information].
Create atomic notes in [folder]
breaking it into: [topic 1], [topic 2], [topic 3]
and link to [[existing note]]
```

**Template creation:**
```
Create a template at Templates/[name].md
for: [use case]
with sections: [X], [Y], [Z]
```

**Bulk update:**
```
Update all goal notes with:
- Current status
- Progress metric
- Next milestone
```

---

## 🔄 Real-World Examples

### Example 1: Research & Capture

**You:** "I just learned about [topic]. Help me capture it."

**Command structure:**
```
Create atomic notes from this [topic] information:
[paste information]

Break it into:
- Definition
- How it applies to my goals
- Next actions

Put in Areas/Learning/[topic].md
Link to: [[Career Goals]], [[Skills]]
```

---

### Example 2: Project Tracking

**You:** "Update The Plug AI progress for this week"

**Command structure:**
```
Edit [[02-PROJECTS/The Plug AI Progress]]
- Update status to: [current]
- Add this week's progress: [details]
- Update next steps: [actions]
- Link to this week's daily notes: [dates]
```

---

### Example 3: System Improvement

**You:** "The vault feels disorganized. Fix it."

**Better structure:**
```
Review my vault and:
1. List any orphaned notes (no links)
2. Suggest missing connections
3. Propose folder reorganization if needed
4. Recommend new index pages

Report findings and ask for approval before changing anything
```

---

### Example 4: Decision Framework

**You:** "I'm choosing between X and Y"

**Command structure:**
```
Create a decision framework note at Areas/[Area]/[Decision].md

Structure:
- The decision
- My values (link to [[Core Values]])
- My goals (link to relevant goals)
- Option A: pros/cons/alignment
- Option B: pros/cons/alignment  
- Decision: (leave for me to fill)
- Timeline: (when do I decide?)

Link to: [[Life Vision]], [[Core Values]], [[Career Goals]]
```

---

## 💡 Pro Tips

1. **State the "why"** — Tell me the purpose, not just the action
   - Better: "I'm tracking this because..."
   - Worse: "Just make this file"

2. **Give me constraints** — Any limitations I should know?
   - "This needs to fit in 200 words"
   - "Keep it simple for daily review"

3. **Reference patterns** — If I've done something before
   - "Like you did for [[Finance Goals]]..."
   - Saves back-and-forth

4. **Ask for templates** — When you'll repeat an action
   - "Create a template I can use weekly"
   - Better than manual copying

5. **Request review** — After I create something
   - "Does this connect properly?"
   - "Did I miss anything?"

6. **Use version control** — Before major changes
   - "Archive the old version before restructuring"
   - Gives you a fallback

---

## 🚀 Workflow Summary

**Ideal interaction flow:**

1. **You describe** what you want (clear, specific)
2. **I ask clarifying questions** if needed
3. **I create/edit** exactly what you asked
4. **You review** in Obsidian
5. **You give feedback** if adjustments needed
6. **I iterate** until it's right

**The better your initial brief, the fewer iterations needed.**

---

## 🎯 Quick Reference

| Need | Command |
|---|---|
| Create a file | "Create [file] at [path] with: [content]" |
| Edit existing file | "Edit [[note]] — add/change/remove [X]" |
| Link files | "Link [[note A]] to [[note B]]" |
| Find patterns | "Show me all connections to [[topic]]" |
| Design structure | "Create a [framework] for [purpose]" |
| Process info | "Create notes from [info] in [folder]" |
| Improve organization | "Audit [folder] and suggest improvements" |
| Create template | "Make a reusable template for [use case]" |

---

## 📞 Questions?

If something isn't clear:
- Ask me directly
- Show me an example of what you want
- Reference a note that's similar

I'm here to make your vault work for you. 🎯

---

*Created: 2026-06-13*
*Updated as new patterns emerge*
