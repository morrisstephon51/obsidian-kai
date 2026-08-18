---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-18T17:25:00Z"
current_task: "Generated LinkedIn post #209 -- NEW lane: the reentry / criminal-record expungement + sealing ministry. A MAN, 34, a father of two who did his time on an early-twenties mistake and has worked and stayed clean for years, but keeps losing job callbacks and apartments the moment the background check comes back -- certain the record is a permanent, unliftable life sentence -- not knowing that many records can be sealed or expunged, that free legal aid clinics and expungement help days will check his record and help him file at no cost, that background-check errors and dismissed charges can sometimes be corrected, and that a record does not automatically bar every job or apartment -- while 'we'll erase your record for $500 upfront' scams, phishing/data-harvest cons that steal his SSN and DOB, and fake 'guaranteed background-clearance' job schemes hunt a proud man who thinks the system is permanently closed to him. Doors (hedged, none ranked): check if it can be lifted (many records sealable/expungeable, get it reviewed, confirm with legal aid or court self-help, don't assume permanent); get the record right (background checks carry errors/dismissed charges that can be corrected); free help to file (legal aid, public defender expungement desks, court self-help, community clinics, no upfront fee); the job + housing side (a record doesn't auto-bar every job/apartment, know your background-check rights); the weight (faith, mentor, reentry ministry, 211, 988). Flat rule: record review runs through the court and free legal help exists, no one honest charges a big upfront fee to erase a record or guarantees a clean slate, and no legitimate service needs your full SSN + DOB handed to a stranger to 'run' it -- anyone charging upfront to wipe it, guaranteeing it, or harvesting your info is the scam, not the second chance. Held a SEPARATE caution: a real court date, filing deadline, or document request in an actual expungement case is NOT a scam -- don't ignore genuine legal paperwork with a real clock. AI in quiet-helper mode (explains the words, finds the legal aid org / expungement clinic / public defender help desk / court self-help to reach himself, helps him understand documents + what a notice asks, names the scam -- does NOT decide whether the record can be cleared, act as his lawyer, or promise an outcome; never fed full SSN / DOB / driver's license / private case details). Compliance stated twice in-body; dignity, never deficit. Rotated gender back to a MAN off the #208 woman 64; centers a YOUNGER FATHER REBUILDING AFTER INCARCERATION (34). Deliberately distinct from unemployment/job-search itself (#201), the eviction (#202), and immigration paperwork (#200 notario) -- this is the OLD RECORD between a changed man and the job/apartment/future and the free legal help to lift it. Saved to output/linkedin-2026-08-18-reentry-criminal-record-expungement-sealing-scam-ministry.md. PRIOR (#208): food assistance / SNAP + EBT benefit-theft -- grandmother skipping meals so her grandkids eat, woman 64. PRIOR (#207): workers' compensation / workplace injury -- mid-life manual laborer hurt on the job and afraid to report, man 51. PRIOR (#206): health coverage / Medicaid / ACA-marketplace enrollment -- working mother uninsured after a job loss, woman 39. The plug is in."
runs_completed: 209
items_processed: 334
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
