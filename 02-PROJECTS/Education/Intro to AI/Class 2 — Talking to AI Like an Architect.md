---
type: study-notes
course: Intro to AI (Generations College AI Program)
class: 2
instructor: Caio Anderson Almeida
topic: Talking to AI Like an Architect / Building the Madison Grind Brand
created: 2026-09-26
tags: [school, intro-to-ai, study-notes, prompting, madison-grind]
---

# Class 2: Talking to AI Like an Architect

> [!summary] The class in one line
> **Stop asking questions. Start giving jobs.** A short, vague request gets you the average of everything the AI has ever seen. A complete request with a job, context, format, limits, and an example pulls it away from average. Then **inspect** the answer against those same five pieces before you accept it.

**My assignment:** [[Madison Grind Brand Kit]]

---

## 1. Why the lazy request fails

- Type three words ("make a coffee logo") and you get the **average of every coffee shop ever**: brown circle, a bean, a curl of steam.
- The AI did what it was asked. It was asked for **almost nothing**.
- Your job as the **architect** is to tell it what makes *your* thing specific.
- **The quality of the answer is mostly decided before you click Send.**

---

## 2. The five pieces of a good request

| Piece | The plain question | Technical name | Madison Grind example |
|---|---|---|---|
| **Job** | What do you want done? Name the thing you'll hold in your hand. | The task | Design a simple logo that reads at one inch on a cup |
| **Context** | What does the AI need to know to do it well? | Context (context engineering) | The business brief, then the brand brief |
| **Format** | What shape should the answer be? | Output format | A table with four named columns. One flat logo on white. |
| **Limits** | What should it avoid? Where are the edges? | Constraints | No beans, no steam, no brown, three colors only, name spelled exactly |
| **Example** | Show it what good looks like. | Few-shot example | The logo concept in the brand brief. The approved logo file. |

> [!tip] Memory hook: **J C F L E**
> "**J**ust **C**ontext **F**irst, **L**imits **E**ventually." Or think of it as a work order: *what* to do, *what to know*, *what it should look like*, *what not to do*, *what good looks like*.

> [!important] Complete, not long
> A good request is **complete, not long**. If it takes more than a short paragraph after the brief, it's probably **two jobs**. Split it.

> [!important] The five pieces become your five checks
> When the answer comes back, ask:
> 1. Did it do the **job**?
> 2. Did it use the **context**?
> 3. Did it take the right **shape**?
> 4. Did it respect the **limits**?
> 5. Does it match the **example**?

---

## 3. The five parts of a brand identity

A **brand identity** is what lets someone recognize a business **before they read a word**: a color, a shape, a logo on a cup.

| Part | What it is | Madison Grind (class version) |
|---|---|---|
| **Name** | The name on everything | Madison Grind Coffee Company |
| **Personality** | 3–4 words for how the business feels | Warm, quick, a little witty, not corporate |
| **Colors** | 2–3 colors, each with a **hex code** so it stays exact | From your brand brief |
| **Type** | A *feeling* for the lettering, **not a font name** | From your brand brief |
| **Logo** | Simple enough to read at **one inch**, distinctive, honest | MADISON GRIND lettering plus one small shape |

**Brand brief** = those five parts written as a short paragraph. It's the document a real business hands a designer.

> [!example] The chain (this was the whole class)
> **Brief in → logo out.**
> **Brief + logo in → mockup out.**

---

## 4. Habits from class

| Habit | Why |
|---|---|
| **Paste the briefs first**, business brief then brand brief, at the start of every new chat | The AI starts every new chat knowing nothing |
| **Shift + Enter** for a new line; **Enter alone sends** | So you can stack the briefs and the job in one message |
| **Refine in the same conversation.** Say what to keep and what to fix. | A new chat throws away all the context |
| **Attach the image as context** (paperclip, or drag the file into the message) | Without the file, the AI redraws the logo from words and it **drifts** |
| **Inspect before you react**: spelling, element count, colors, background, limits, one inch squint test | "A beautiful wrong answer is still wrong. It's just wearing a nicer jacket." |
| **Catch invented facts**: founding year, owner, organic beans | If it isn't in the brief, it isn't a fact about the shop. Refine it out. |
| **Match thinking effort to the job**: making = normal, judging = **extended thinking on** | A critique is slow work. Turn it back off when you're done. |
| **Copy with the Copy button** (under a response) | Clean text into your file |

---

## 5. Getting around Claude

> [!note] The class guide is written for ChatGPT. This is the same workflow in Claude.
> The five pieces, the briefs, and the inspection habits don't change. Only the buttons do.

| Where | What | Used for |
|---|---|---|
| Left sidebar | **New chat** | A fresh chat for each step: brand brief, logo, mockup |
| Left sidebar | **Chat history** | Reopen any chat and keep refining (ChatGPT calls this Recents) |
| Left sidebar | **Projects** | Keep both briefs in a project so every new chat already has them |
| Center | **Message box** | Paste briefs → Shift+Enter → the job |
| Left of composer | **Paperclip / drag and drop** | Attach the approved logo before the mockup |
| Above composer | **Extended thinking** toggle | Turn on for the designer critique, off for making |
| Above composer | **Model picker** | Opus for judgment work, Sonnet for speed |
| Under a response | **Copy button** | Copy the brand brief into your text file |
| In a response | **Artifact panel** | Where the logo opens. Download from the panel. |

> [!warning] The one real difference: there is no Create image button
> ChatGPT makes a raster image from a description. Claude builds the logo as **code** (an SVG artifact) and you download it from the artifact panel.
>
> **Why that's better for a logo:**
> - **Vector, not pixels.** It stays sharp at any size, from a one inch cup to a storefront sign.
> - **Exact hex codes.** The colors are literally the ones from your brand brief, so they can't drift.
> - **The spelling can't break.** The name is real text, not drawn letters, so MADISON GRIND is spelled right every time.
> - **Refinements are surgical.** "Make the sun smaller" changes one number instead of redrawing the whole logo.
>
> **What you give up:** photorealism. A photo-style mockup of a real cup on a real table is something an image generator does better.

## 6. The workflow step by step

> [!note] Business brief (paste first, exactly as written, never "improve" it)
> Madison Grind Coffee Company is a fictional coffee shop on Madison Street in downtown Chicago, in the Loop, steps from Generations College. Our customers are college students, faculty, and nearby office workers. We open at six thirty in the morning on weekdays. We serve espresso drinks, drip coffee, tea, and simple pastries. Our personality is warm, quick, and a little witty, like a friend who works behind the counter. Prices are fair for students. We are not fancy, we are not corporate, and we never use hype.

### Step 1: Three directions → brand brief
**New chat.** Paste the business brief → Shift+Enter → ask for **three brand directions** in a table (Direction Name, Personality in Three Words, Color Palette, Logo Concept). No beans, no steam, nothing like a national chain.

**Inspect:** 3 rows × 4 columns in order? Directions actually different? Any brown? Any beans or steam?
**Choose by asking:** Which would a tired student walk toward at 6:45 am? Which fits on a cup? Which prints small?

**Same chat:** ask for the **brand brief** in the exact 5 part format (personality in 4 words; 3 colors with names and hex codes; typography feeling, not a font; logo concept in 2 sentences; 3 taglines under 6 words, no exclamation points). Add: *do not invent facts*.

**Inspect:** personality matches the brief? Colors drifted to brown? Logo simple enough for a napkin sketch? Taglines sound like hype? Invented founding year, owner, or farm?

**Refine**, then **Copy** the final brief into your text file under the business brief.

### Step 2: Logo → logo family
**New chat.** Paste both briefs → ask for the logo **as an SVG artifact** (lettering plus one shape, three colors only using the exact hex codes, flat, no gradients or shadows, centered on white, spelled exactly, no beans/steam/cups).

> [!check] Logo inspection checklist
> - [ ] Spelled **MADISON GRIND**, every letter
> - [ ] Lettering **plus one shape**. Count them.
> - [ ] Only the three brand colors. Any brown?
> - [ ] Plain white background
> - [ ] Any bean, steam, or cup?
> - [ ] **Squint:** one inch tall on a paper cup, still readable?
> - [ ] Does the shape *mean* something? Is the **name the star**?

**Refine** (2–3 rounds is normal). Download first and final logo.

**Same chat:**
- **Dark version:** same logo on the primary color; lettering switched to the lightest brand color; change nothing else.
- **Icon:** square, for a social profile picture. Just the shape **or** "MG", whichever reads better tiny.

**Check:** dark = same logo, only recolored. Icon = recognizable from across the room.

**Optional critique:** turn on **extended thinking**, ask it to act as an experienced brand designer: three specific risks (small size readability, confusion with existing brands, personality match) plus one recommendation. "Be honest. Do not flatter." Then turn it back off.

### Step 3: Mockup
**New chat.** Paste both briefs → **attach your final logo file** → ask for the mockup **as an HTML artifact that places the attached logo file**, not a redrawing of it → mockup prompt (cup, small storefront sign, phone with social profile; soft morning light; don't alter the logo; no text except MADISON GRIND).

**Inspect:** is it *your* logo, or did it drift? Spelled right everywhere? Extra text? Neighborhood campus shop, or luxury lobby?

---

## 7. Assignment rules and grading

**Graded on:**
- **The request:** pasted briefs, named the job, asked for a shape, set limits
- **The inspection:** your refinement fixed something *real* you found by checking against your request
- **Not** on whether your logo is prettier than anyone else's

**Rules:**
- Use the business brief **exactly as written**
- **No invented facts.** Refine them out.
- **MADISON GRIND** spelled exactly on every image. "If it is wrong, it is not done."
- Refine in the **same** chat. **Attach** the logo file before the mockup.
- Extended thinking back **off** after the critique

**Submit, in this order:** final brand brief (text) → first and final logo side by side + one sentence on what changed and why → dark version and icon → final mockup.

---

## 8. Mistakes to avoid

> [!warning] The five classic mistakes
> 1. **Lazy request:** three words and hope
> 2. **Overstuffed request:** a page of rules that buries the job
> 3. **Forgetting to attach the logo** for the mockup, so it drifts
> 4. **Refining in a new chat**, so the AI forgets everything
> 5. **Skipping inspection** because it looked nice

---

## Before Class 3

- [ ] Submit the Brand Kit
- [ ] Keep **both briefs** in your text file (you paste them one last time in Class 3). In Claude, a **Project** does the same job: drop the briefs in once and every chat in it starts with them.
- [ ] Look at logos on cups, signs, and your phone. Ask the **one inch question**: would I still recognize it small?
- **Next class:** the **Remember** pillar, Personalization and Memory. A new chat will already know Madison Grind without you explaining it. Claude's version of this is **Projects** (shared context for every chat inside it) and **memory**.

---

## Self-Quiz

> [!question]- 1. Why does a lazy request produce an average result?
> The AI has almost no direction, so it falls back on the most common version of the thing, which is the average of everything it has seen.

> [!question]- 2. Name the five pieces of a good request and their technical names.
> Job (the task), Context (context engineering), Format (output format), Limits (constraints), Example (few-shot example).

> [!question]- 3. What's the difference between a complete request and a long one?
> Complete means it covers all five pieces. If it runs longer than a short paragraph after the brief, it's probably two jobs and should be split.

> [!question]- 4. What are the five parts of a brand identity?
> Name, personality, colors (with hex codes), type (a feeling, not a font name), and logo.

> [!question]- 5. Why should you refine in the same conversation instead of starting a new chat?
> A new chat throws away the context: the briefs and everything you already approved.

> [!question]- 6. Why attach the logo file before making the mockup?
> Without it, the AI redraws the logo from words and it drifts (changes spelling, shape, or colors).

> [!question]- 7. What is the one inch squint test?
> Imagine the logo one inch tall on a paper cup and squint. If you can still read the name, it works.

> [!question]- 8. The AI's brand brief says "Founded in 1998 by a local family." What do you do?
> It's an invented fact that isn't in the business brief. Refine it out.

> [!question]- 9. When should you turn extended thinking on?
> For judging tasks like the designer critique. Making is fast, judging is slow. Turn it back off afterward.

> [!question]- 10. What is the assignment actually graded on?
> The quality of your request and whether your refinement fixed a real problem you found by inspecting. Not how pretty the logo is.

> [!question]- 11. Why describe typography as a feeling instead of naming a font?
> The feeling guides the look without locking you into a specific font the image tool may not be able to reproduce.

> [!question]- 12. What's the chain the whole class was built on?
> Brief in, logo out. Brief and logo in, mockup out.
