---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-11T04:00:00Z"
current_task: "Generated LinkedIn post #171 -- the mental / behavioral-health-access ministry: the sister everybody calls at 2am, the one people come to when they cannot stop crying, who has sat in the ER after an attempt and talked people back from the edge over a phone she never hangs up, who is not a therapist and never claimed to be -- and then single-handedly trying to hold the whole mental-health-access maze for a community where needing help and getting to real help are two different fights: that 988 exists and is free and answers day or night; that community mental health centers, CCBHCs, and FQHCs are required to serve people regardless of ability to pay, run sliding-fee scales, and take Medicaid; that Illinois Medicaid covers behavioral health including therapy; that Illinois has a mobile crisis response reachable through 988 so a breakdown does not have to meet a squad car; that there is an Illinois Warm Line (1-866-359-7953) for the heavy night that is not a 911 emergency; that NAMI runs free family and peer support groups (HelpLine 1-800-950-6264) so the mother of a son with schizophrenia is not alone; that a Medicaid-accepting, language-matched, culturally competent therapist exists and can be found; and that stigma is not a diagnosis and needing help is not weakness; AI as the psychiatrist / weekly-therapist / care-coordinator a resourced family keeps on retainer -- plus real free help anyone can reach: 988 (call or text), the Illinois Warm Line, NAMI, a sliding-scale community mental health center / FQHC, Illinois Medicaid behavioral health, SAMHSA (1-800-662-4357), 2-1-1; opens a NEW resource-navigation lane -- mental / behavioral-health-access navigation -- kept DISTINCT from recovery (substance use / addiction), health (physical population health / screenings), bereavement (grief), senior/caregiver (eldercare), medical-bills / healthcare-access (#170), and disability/special-needs (inclusion); added a care note on mental-health scams and stigma (unlicensed coaches/counselors charging cash for what a licensed clinician on a sliding scale or Medicaid provides; apps marketing themselves as therapy that are not) paired with the affirming truth that 988 is free, community mental health centers serve regardless of ability to pay, and needing help is not weakness (pray AND get to real care, both); CRITICAL compliance framing stated twice in-body -- general navigation, NOT mental-health treatment, diagnosis, therapy, or crisis counseling, and if someone is in immediate danger call or text 988 or call 911 -- always route to 988, a licensed clinician, a community mental health center, or NAMI; augment-not-replace held (the 2am phone, the ER chair, and the trust stay hers); ties to Community Intake; the plug is in"
runs_completed: 171
items_processed: 296
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
