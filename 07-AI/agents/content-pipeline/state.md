---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-13T07:41:00Z"
current_task: "Generated LinkedIn post #181 -- the adult-education / GED / high-school-equivalency ministry, a NEW lane opened deliberately as the door BENEATH Get Skilled (#178 workforce training assumed a diploma the way #180 transportation assumed a car). The barrier is a credential ceiling: a plainly intelligent, reliable adult who never finished high school hits the same locked line on every application -- high school diploma or GED required -- so training, the promotion, and the better job stay one door out of reach. Real, durable, deeply local: south suburban Cook County has genuine FREE adult-ed / HSE programs at its community colleges; the true barrier is not ability but shame, time, money-myths, and the belief that the ship sailed. Series QUIET-HELPER mode -- AI is the patient tutor who never makes a grown man feel dumb, not the subject. NEW persona rotated off the recent run (SNAP mother #173, homeownership woman #174, college father #175, caterer woman #176, teen boy #177, warehouse man #178, elder church mother #179, home-health aide woman #180): a MAN IN HIS LATE THIRTIES, a building-maintenance / facilities lead who keeps a whole SCHOOL running (the irony: he keeps up the building where children learn and never graduated from one himself), left in 11th grade because his family needed his paycheck NOW, has hidden it for 20 years, does math in his head faster than the register, trains the younger diploma-holders who get promoted over him then come ask him how to do the job. Distinct from #178 (whose barrier was a failing body) -- his is a credential ceiling + private shame, sharpened by the newer wound that his daughter now brings home homework he cannot help with, and that he tells his kids stay in school without ever finishing the sentence. Dignity, never a deficit (PULSE guard against he just needs to go back to school). Doors, durable/hedged/routed, none ranked: (1) Illinois community-college adult education -- free/low-cost HSE prep, routed to your local community college adult-ed office, Prairie State College (Chicago Heights) + South Suburban College (South Holland) as examples only, hedged; (2) the HSE credential itself -- the GED or another state-approved test, recognized like a diploma, routed via the adult-ed program + the ICCB, hedged HARD on current test details; (3) public library adult-literacy + tutoring, quiet space, computers; (4) money/time myth-buster -- many programs are FREE and run evenings/weekends/online with childcare or a ride so you neednt quit your job; (5) the workforce bridge -- Illinois bridge / Integrated Education and Training letting you earn the HSE WHILE training for a trade, tying back to #178; (6) 211/211.org for free classes nearby; (7) scam warning weighted for THIS barrier -- online diploma mills / instant-GED-for-a-fee-no-test sites that sell worthless paper no employer or college accepts, with the FTC-aligned truth that a real HSE needs real study + a real test and legit prep is usually free. AI held in quiet-helper + augment-not-replace: patient 11pm study partner, quizzes, breaks subjects into small pieces, finds the free class, drafts the questions to ask -- but does NOT take the test for him (cannot, must not; an unearned credential IS the diploma-mill lie), does NOT replace the teacher/tutor, does NOT do the learning for him, does NOT replace the intelligence he always had. Core reframe: the gap is not that he is less smart -- one 16-year-old had a household that could absorb a crisis and a parent to call the counselor; the other WAS his household crisis-absorber and left in 11th grade, no one to handle the forms. One got a diploma and a helper; the other got a job and a ceiling. Compliance TWICE in-body -- general navigation, NOT an endorsement of any school/program/company, NOT legal/financial/educational advice; AI can be wrong so verify every program, cost, schedule, and test detail with the actual college/program/library; never feed private info (SSN, ID numbers) to a public AI tool; instant-diploma-for-a-fee sites are diploma-mill scams hunting the people carrying the most shame. DELIBERATELY did NOT rank one school/program/test or promise a credential or outcome. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intakes routing and to #178. The plug is in. --- PRIOR (#180): the transportation-access / transit-desert ministry -- the home-health-aide woman in her 50s whose car dies. PRIOR (#179): the AI-literacy-itself ministry, Get into AI -- the elder church mother. PRIOR (#178): the workforce-training / Get Skilled ministry -- the warehouse man whose body was quitting."
runs_completed: 181
items_processed: 306
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
