---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-14T10:10:00Z"
current_task: "Generated LinkedIn post #187 -- the special-education / IEP-504 / school-rights-advocacy ministry, a NEW lane: the door a PARENT walks through to get a struggling child what the law already says the child is owed. Distinct from the disability/special-needs ministry (#08-09, the church VOLUNTEER carrying a whole benefits maze where IEP was one line) and from adult education/GED (#08-13, an adult earning his own credential) -- #187 lives at the kitchen table with the parent whose ONLY barrier is the school-rights door, and it centers a CHILD (an 8-year-old), which the adult-barrier run #173-#186 kept offscreen. QUIET-HELPER mode: AI explains evaluation / IEP / 504 / eligibility / accommodation / due process / prior-written-notice in plain words, never the evaluator, never the school, never the advocate of record, never the one who diagnoses the child. NEW persona rotated off the recent run (young man first-gen grad 28 #186 ... housekeeping woman 52 #185): a YOUNG MOTHER MID-THIRTIES (34) -- works, shows up, loves her boy fiercely, left school herself feeling small and carries it into every meeting, has a bright-at-home 8-year-old son being called a behavior problem and quietly written off at school, assumes she has no standing to push. Rotates gender back to a woman but YOUNGER than the recent women (41, 50s, 52) and centers a child for the first time in the adult run. Dignity, never deficit (PULSE guard vs. she should advocate harder / the boy just needs discipline): she was raised to trust the school and believe people like her cannot question it; the child is not a problem, he has a need the law requires the school to meet. Doors, durable/hedged/routed, none ranked: (1) the right to request a full FREE evaluation IN WRITING + the school's legal duty to respond in a set timeline (hedged; procedures/timelines set by law and district). (2) the IEP and 504 plan -- legally binding services/accommodations at NO cost once a child qualifies (hedged; eligibility decided by the evaluation team/school). (3) the FREE federally funded Parent Training and Information center -- every state has one, helps parents understand/exercise rights and come to the meeting (routed/hedged). (4) FREE legal aid + disability-rights orgs for a denied evaluation, a shorted/ignored plan, or a dispute; her right to disagree, bring someone, use mediation/due process (routed/hedged). (5) her own facts to line up (report cards, notes home, pediatrician observations) WITHOUT handing the child's records to a machine. (6) 211/211.org for free tutoring and parent support. (7) Scam/caution weighted for THIS barrier: paid advocates and get-your-kid-an-IEP-for-a-fee outfits, private diagnosis mills, predatory tutoring/therapy -- the truth that the evaluation and the plan are FREE, a real free parent center exists, and no honest person guarantees a diagnosis or outcome for an upfront fee. AI in quiet-helper + augment-not-replace: explains terms as many times as needed, helps her see she has the right to ask, drafts the written evaluation-request letter in her words, helps her read a confusing evaluation report / draft IEP and see what is missing, helps her write and rehearse her meeting questions, helps her find the real free parent center -- but does NOT diagnose the child, does NOT decide eligibility (evaluation team/school do), does NOT give legal advice, does NOT attend or speak for her, does NOT replace the parent center/advocate/teachers/evaluators/attorney, and must NEVER be fed the child's full name, school ID, medical records, or identifying details. Core reframe: the mother across town had a sister who said put it in writing, they have to answer, the plan is free once he qualifies, and a free parent center will sit next to you -- her son got evaluated, got a plan, started to believe he was smart again; this mother's son keeps getting sent to the hallway and hearing at eight that he is the problem -- not less loving, just never told the door was hers to open. Compliance TWICE in-body -- general navigation, NOT an endorsement of any advocate/attorney/org/program, NOT legal advice; AI can be confidently wrong and special-ed procedures/timelines vary by state and district, so verify every right/timeline/step with the school, a free Parent Training and Information center, or a disability-rights/legal-aid org; never put a child's private information (full name, school ID, medical or evaluation records) into a public AI tool. DELIBERATELY did NOT rank any advocate/attorney/org, did NOT promise the child will qualify or get any service, and did NOT assert any specific timeline/procedure/program detail as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intake routing and the Enrollment Funnel. PRIOR (#186): student-loan repayment/forgiveness -- young man first-gen grad 28. PRIOR (#185): unemployment insurance -- housekeeping woman 52. PRIOR (#184): property-tax relief -- elder deacon widower 68. The plug is in."
runs_completed: 187
items_processed: 312
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
