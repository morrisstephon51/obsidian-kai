---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-19T07:15:00Z"
current_task: "Generated LinkedIn post #214 -- NEW lane: the special-education / IEP + Section 504 parent-rights ministry. A WORKING MOTHER, 36, of a struggling 8-year-old (2nd grade) reads every note home ('behind in reading,' 'not applying himself,' 'a behavior problem') as a verdict on her child and on her own parenting, and quietly carries the shame of a kid who 'can't keep up' -- not knowing that under federal law her child may have the right to a FREE school evaluation for a learning/developmental difference, that an IEP or a 504 plan is a legal right built for exactly this, that she can request the evaluation IN WRITING at no cost, and that a free, federally funded Parent Training and Information Center (PTI) exists in every state to walk a parent like her through it -- while upfront-fee 'guaranteed IEP / special-needs advocate for $X' cons, cash-only 'diagnosis mill' outfits promising a guaranteed diagnosis to force services, and learning-center / tutoring cons promising to 'fix' or 'cure' the child for money (some falsely implying they speak for the school) and info-harvesters hunt a scared, tired parent. Doors (hedged, none ranked): name it and know help exists (free evaluation + IEP/504, confirm specifics with the school / district special-ed office / parent center -- governed by IDEA + Section 504); ask IN WRITING through the school (keep a dated copy; the school's special-ed contact + district office, never a stranger who calls/advertises); free help (the federally funded PTI, legal aid, disability-rights groups -- no upfront fee for what they do free); gather what helps (report cards, teacher notes/emails, prior testing, her own written record -- a step today); the weight (faith, mentor, family, church, parent center, legal aid, 211, 988). Flat rule: a school evaluation is FREE to request, the school cannot charge a family to evaluate a child, and no legitimate advocate guarantees a diagnosis, an IEP, or any outcome for an upfront fee -- anyone charging up front for a 'guaranteed' result, selling a cash diagnosis, or harvesting the child's info is the scam, not the help. Held a SEPARATE caution: a real evaluation timeline, a real IEP/504 meeting notice, and real district paperwork (consent forms, meeting dates) are NOT scams -- do not ignore a genuine notice; responding in writing and showing up to the meeting is exactly right; and a legitimate private evaluation or a real, reputable paid advocate can be a valid choice -- the caution is about guarantees, pressure, upfront fees for free services, and info-harvesting, not all paid help. AI in quiet-helper + augment-not-replace mode (explains the words -- 'evaluation,' 'IEP,' '504,' 'eligibility,' 'accommodation'; helps her understand what a written request and a school meeting involve; helps her find the school contact / district office / free parent center / legal aid to reach herself; names the scam -- does NOT write the request as her, speak to the school as her, or promise a diagnosis/IEP/outcome; never fed her child's full records / SSN / her bank login). Compliance stated twice in-body (general navigation, NOT legal/medical/educational advice, NOT a determination of eligibility; governed by IDEA + Section 504, decided by the district's team and due process, not a machine); dignity, never deficit (a mother whose child learns differently is not a bad parent and a struggling child is not lazy -- a difference is not a verdict; not knowing the free evaluation and IEP/504 exist is help nobody walked her through). Rotated gender back to a WOMAN off the man 71 (#213); centers a WORKING PARENT of a SCHOOL-AGE CHILD (mother 36 / child 8). Timely for back-to-school (August) -- the notes and conferences start now. Deliberately distinct from childcare assistance (#210 -- a school-age child's education RIGHTS, not paying for daycare so a parent can work) and from every benefit/bill/wage/tax lane in the recent run (utility #212, property tax #213). Saved to output/linkedin-2026-08-19-special-education-iep-504-parent-rights-scam-ministry.md. NOTE / RECONCILIATION: this counter had lagged one behind reality -- post #213 (property-tax / senior-homeowner-exemption + tax-sale rescue scam, man 71) had already shipped to output/ and the feed but the counter still read 212; rolled forward to account for both #213 and this #214 (runs 212->214, items 337->339). PRIOR (#213): property tax / senior-homeowner exemption + tax-sale rescue scam -- a man bracing to lose his paid-off home over a delinquent tax bill, man 71. PRIOR (#212): utility shutoff / energy assistance (LIHEAP) -- a woman on a fixed income rationing to keep the power on in the August heat, woman 58. PRIOR (#211): wage theft / unpaid wages -- a working man quietly eating a short check for fear of losing the job, man 47. The plug is in."
runs_completed: 214
items_processed: 339
last_error: null
color: "#9B59B6"
house: "studio"
---

# Loop Rules

## Loop Start
1. Read `~/Desktop/Context/context.md`
2. Read `~/Desktop/Context/me.md`
3. Check bus for unread messages: `node ~/clawd/.bus/busctl.js unread --agent content-pipeline`
4. Read `~/Desktop/kai/07-AI/context/world.md`
5. Read this `state.md`
6. Execute task

## Loop End
1. Update `status`, `last_run`, `current_task`, `items_processed` in this file
2. Post to bus if meaningful work done: `node ~/clawd/.bus/busctl.js post --from content-pipeline --topic content --msg "<summary>"`
3. Acknowledge bus: `node ~/clawd/.bus/busctl.js ack --agent content-pipeline`
4. Write summary message to `~/Desktop/kai/07-AI/chatroom/feed.md`

## Notes
- Handles video, flyers, social content, training materials for The Plug AI and BigHeart.
- Stack: Next.js, Supabase, Remotion, FAL, Pexels, Vercel, Composio.
- Live at: content-machine-wine.vercel.app
