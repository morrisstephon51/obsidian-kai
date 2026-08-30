---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-30T19:20:00Z"
current_task: "Generated LinkedIn post #250 -- NEW DOMAIN: JOB SEARCH / EMPLOYMENT / WORKFORCE for a single mother of 34 in the south suburbs whose shift got cut and who is applying to everything on her phone at midnight, then hit the job-scam wave: text-only you-are-hired with no interview, OVERPAYMENT CHECK to buy equipment and wire part back (bounces, bank comes after her), STARTER-KIT/TRAINING/EQUIPMENT pay-to-start fee, TASK/GIG earn-from-your-phone app demanding a deposit to unlock bigger earnings, IMPOSTER RECRUITER over text/WhatsApp/Telegram posing as a known company HR to harvest SSN+bank info on a fake onboarding form, and MLM/PYRAMID pay-and-recruit. Facts that change everything: free workforce help is real -- American Job Center / Illinois workNet (free resume/interview/job help), WIOA-funded free training + short certificates that pay for the class, community college career offices, nonprofit job programs; a real employer PAYS YOU -- never pay to get hired, never deposit a strangers check and wire money back, never hand SSN/bank login before a real interview + verified hire; verify every employer yourself via the companys real website + phone. Flat rule stated TWICE + SEPARATE caution that AJC/workNet/WIOA/community college/real nonprofit job programs are NOT scams. Dignity-never-deficit (a cut shift is arithmetic done to her, not a verdict; job-hunting at midnight while raising kids is honorable, not lazy). AI quiet-helper/augment-not-replace with compliance TWICE (resume/interview/posting-decode/red-flag-spotting/find-the-real-office; does NOT apply for her, does NOT guarantee a job/income, never hands over SSN/bank login, not a substitute for the real workforce office; verify with the real company; never pay to work, never deposit a strangers check). Rotated to a WOMAN age 34 off #249 man 61; distinct from #248 woman 52 and #247 man 57. WHOLLY NEW employment/workforce domain distinct from utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245), long-term care (#244). Ties to The Plug AI Get-Skilled pillar + the JobScout agent world. Serves Plug AI community + faith-community + working-family + single-parent + financial-literacy + digital-literacy + Get-Skilled pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-30-job-search-employment-free-workforce-help-american-job-center-worknet-wioa-training-fake-job-offer-overpayment-check-starter-kit-fee-task-gig-recruiter-imposter-mlm-pyramid-scam-ministry.md. PRIOR (#249): utility shutoff/LIHEAP (man 61). PRIOR (#248): medical debt/charity care (woman 52). PRIOR (#247): citizenship/naturalization (man 57). The plug is in."
runs_completed: 249
items_processed: 374
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
