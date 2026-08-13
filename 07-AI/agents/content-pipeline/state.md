---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-13T12:00:00Z"
current_task: "Generated LinkedIn post #182 -- the health-coverage / insurance-enrollment ministry, a NEW lane opened deliberately as the UPSTREAM door BENEATH the medical-bills / healthcare-access lane (#08-10): that post met the person AFTER the bill arrived, this one meets them BEFORE it. The barrier is being uninsured and believing coverage is a thing for people with a boss, so a self-employed, responsible adult goes years with no card, rationing his own health and googling symptoms at 2am, one diagnosis away from losing what he built. Real, durable, deeply local: south suburban Cook County has FREE enrollment help (Get Covered Illinois / navigators), real ACA-marketplace premium subsidies that self-employed people routinely qualify for and never check, Illinois Medicaid, and community health centers (FQHCs) that treat you now on a sliding scale regardless of insurance -- the true barrier is not irresponsibility but the assumption that coverage needs a W-2, plus fear of cost and fear of what a doctor might find. Series QUIET-HELPER mode -- AI explains premium/deductible/subsidy/network without making a grown man feel dumb, never the subject and never the enroller. NEW persona rotated off the recent run (SNAP mother #173, homeownership woman #174, college father #175, caterer woman #176, teen boy #177, warehouse man mid-40s #178, elder church mother 60s/70s #179, home-health-aide woman 50s #180, facilities-lead man late-30s #181): a MAN IN HIS LATE FIFTIES (58), a self-employed barber with his own chair for 30 years cutting three generations of the same families, the steady corner of the block, who has NEVER once had health insurance because it always felt like an HR/boss/badge thing for other people -- now with blood pressure the drugstore machine keeps flagging, knees going, still a few years short of Medicare at 65, terrified one diagnosis wipes out the shop and his savings. Distinct from #178 (employed, failing body, workforce-training barrier) and #180 (transportation TO the doctor): his barrier is having NO coverage at all and assuming he cant and shouldnt have it -- a pre-Medicare gap plus a lifetime of insurance is for people with a boss. Dignity, never a deficit (PULSE guard against he should have just bought insurance): he built something real with his hands for 30 years and got no card because the whole system is wired for a W-2 he never had -- not less responsible, differently situated. Doors, durable/hedged/routed, none ranked: (1) Get Covered Illinois + FREE in-person navigators who enroll you at no charge, hedged (windows/eligibility vary); (2) the ACA marketplace with premium subsidies a self-employed modest-income person very often qualifies for and never checks, hedged HARD on amounts/plans/windows; (3) Illinois Medicaid depending on income, routed via navigator, hedged on eligibility; (4) community health centers / FQHCs that see you NOW on a sliding scale regardless of insurance, Aunt Marthas named as ONE example only, hedged; (5) cost-and-fear myth-buster -- the help is free, you likely qualify for more than you think, and timing matters (enrollment windows / special-enrollment triggers), so the door may not be closed, hedged; (6) 211/211.org for free enrollment help and low-cost care; (7) scam warning weighted for THIS barrier -- junk short-term plans that look like insurance but arent, and robocall/cold-call health-plan pitches that demand payment + your SSN on the spot, with the FTC-aligned truth that a real navigator is always FREE, nobody legit cold-calls to sell a plan, and a real plan is one you can look up through the official marketplace. AI held in quiet-helper + augment-not-replace: explains the words, ballparks eligibility, finds the nearest free navigator and community health center, drafts the 3 questions to ask -- but does NOT enroll him (a human navigator / the official marketplace does that), does NOT diagnose or give medical advice, does NOT replace the doctor or navigator, must NEVER be given his SSN or income documents. Core reframe: the salaried man across town has had a coverage card since 24 because a job handed it to him and an HR portal renews it every autumn while he clicks keep my plan, a spouse plan behind it -- coverage found him on day one; the barber built a business and got a blank space where the card should be. One never had to look; the other was never shown where to look. Compliance TWICE in-body -- general navigation, NOT an endorsement of any plan/insurer/program/health center, NOT legal/financial/medical/insurance advice; AI can be confidently wrong so verify every plan, cost, subsidy, eligibility rule, and enrollment deadline with the actual navigator/official marketplace/health center; never feed private info (SSN, income docs, member/Medicaid ID) to a public AI tool; cold-call health-plan offers demanding payment + SSN are scams and an unverifiable plan isnt real coverage. DELIBERATELY did NOT rank a plan/insurer/program/health center or promise coverage, a subsidy amount, or an outcome. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to Community Intake routing, sits UPSTREAM of the medical-bills lane (#08-10) the way #181 sat beneath #178, connects loosely to #180. The plug is in. --- PRIOR (#181): adult-education / GED / HSE ministry -- the facilities-lead man late-30s credential-locked out of every promotion. PRIOR (#180): transportation / transit-desert ministry -- the home-health-aide woman whose car dies. PRIOR (#179): AI-literacy Get into AI ministry -- the elder church mother."
runs_completed: 182
items_processed: 307
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
