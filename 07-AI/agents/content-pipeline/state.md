---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-17T19:35:00Z"
current_task: "Generated LinkedIn post #206 -- NEW lane: the health-coverage / Medicaid / ACA-marketplace enrollment ministry. A WOMAN, 39, a working mother uninsured after losing the job her health insurance came with -- rationing a prescription, skipping her own checkups to keep the kids seen, certain coverage is unaffordable or 'not for people like her' -- not knowing she and especially her kids may qualify for free/low-cost Medicaid, that a subsidized marketplace plan could cost a fraction of what she fears, that losing job-based coverage usually opens a special enrollment window (with a clock), and that the help to enroll is free -- while sham 'limited-benefit' fake-health-plan scams, 'enrollment/processing/activation fee' con artists, and health-insurance robocalls hunt a frightened uninsured woman who thinks coverage is out of reach. Doors (hedged, none ranked): Medicaid/children's coverage (free/low-cost by income + household, check free); the Marketplace + subsidy (healthcare.gov or state site, premium tax credits may cut cost sharply); special enrollment (job-loss window with time limits, check now); free help to enroll (navigators/certified assisters, community health centers, official call line -- no fee); care in the meantime (FQHC/sliding-scale clinics on income-based fees); the shame + fear (faith, mentor, 211, 988). Flat rule: legit enrollment help is free, no one charges a fee to sign you up, and no honest plan is sold by a high-pressure robocall demanding a card number or your full SSN. Held a SEPARATE caution: a real official notice (state Medicaid agency / marketplace asking to verify income or renew) is NOT a scam call -- don't ignore genuine paperwork with a real deadline. AI in quiet-helper mode (explains the words, finds the official sites + a navigator to reach herself, helps her gather what she needs to apply, reads a plan letter/notice, names the scam -- does NOT enroll her, decide what she/kids qualify for, or pick her plan, is NOT a doctor/insurance agent/navigator, never fed full SSN/bank login/account numbers). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a WOMAN off the #205 man 63; centers a MID-LIFE WORKING MOTHER IN THE COVERAGE GAP (39). Saved to output/linkedin-2026-08-17-health-coverage-medicaid-aca-marketplace-enrollment-scam-ministry.md. PRIOR (#205): debt collection/collector harassment/know-your-rights -- older near-retirement man 63. PRIOR (#204): student loans/IDR/forgiveness -- first-gen college graduate woman 26. PRIOR (#203): disability/SSDI/SSI -- skilled-labor man 45. The plug is in."
runs_completed: 206
items_processed: 331
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
