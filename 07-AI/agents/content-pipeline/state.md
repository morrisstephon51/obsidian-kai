---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-17T10:30:00Z"
current_task: "Generated LinkedIn post #202 -- the HOUSING / EVICTION / RENTAL-ASSISTANCE-SCAM ministry: the week a working single mother of two, rent current for years until her hours were cut, falls one month behind and finds a notice taped to her door -- too ashamed to tell the pew, sure the only move is to pack -- not knowing emergency rental assistance, free legal aid, eviction mediation, and HUD-approved housing counselors exist a phone call away, that ignoring a court summons is the one move that actually loses the case, and that no real program charges a fee to release help -- while rental-listing scams, fake rent-relief sites, and eviction-rescue con artists hunt her the moment she starts searching. Doors: DO NOT IGNORE THE NOTICE (answer the summons; tenant rights; free legal aid; deadline-sensitive); EMERGENCY RENTAL ASSISTANCE (back rent + utilities; eligibility decided by programs); UNDERSTAND THE OPTIONS (legal aid, eviction mediation, payment plan, HUD-approved housing counselor, tenant-rights help); HELP SHE MAY QUALIFY FOR (SNAP/utility bridge, childcare assistance, other benefits); SUPPORT FOR THE SHAME (faith, trusted friend, 211, 988); CHURCH BENEVOLENCE + 211. Scam weighted for THIS barrier: RENTAL-LISTING scams (too-good listing, wire a deposit before touring, keys by mail, copied real listing); RENT-RELIEF / ASSISTANCE-IMPOSTER phishing (fake rental-assistance texts/sites demanding an application fee or SSN/bank/login to release funds); EVICTION-RESCUE / FAKE-LANDLORD fraud (cash to stop the eviction and files nothing, or pay rent to them instead of the real landlord). Flat rule: a legitimate rental-assistance program never charges to apply or unlock help; never wire a deposit for a place you have not toured or a landlord you cannot verify; answering the court and free legal aid cost nothing. QUIET-HELPER + augment-not-replace: AI explains eviction notice / court summons / rental assistance / legal aid / eviction mediation / housing counselor / tenant rights in plain words, reads the notice and finds the deadline, drafts a hardship letter / payment-plan request, and names the scam -- but does NOT give legal advice, does NOT represent her in court, does NOT decide eligibility, is NOT a lawyer / the housing agency / the court, and must NEVER be fed her full SSN, bank/direct-deposit details, or logins. NEW system (housing/eviction), distinct from the recent benefits/debt/immigration/workforce run (SNAP #193 ... immigration #200, job-loss #201). NEW persona rotated off the run (man 58 #201): a WOMAN, 31, working single mother of two, one month behind after cut hours, staring at a notice, sure she must pack, unaware assistance and free legal aid are hers -- rotates gender back to a WOMAN and centers a YOUNGER WORKING SINGLE MOTHER in a different system and barrier (landlord clock + court deadline + children + shame + predatory housing scams). Dignity, never deficit (PULSE guard vs she-should-have-budgeted / shouldnt-have-signed-that-lease / just-move-somewhere-cheaper / should-already-know-her-rights). Core reframe: the woman across town was one month behind too, same notice, same shame, but a friend at church said do not ignore the summons, the assistance is real, the legal help is free, let me help you find it, so she answered the notice, applied, sat with legal aid, worked out a plan through mediation, and kept her kids home -- while the woman in the pew almost wired a deposit to a fake landlord and almost let the court date pass. Compliance TWICE in-body -- general navigation, NOT legal/financial/housing-guarantee advice, NOT a determination of eligibility or how the case ends; eligibility/timelines/outcomes decided by the programs, the court, and the law, not a machine or a guess; verify with free legal aid, a HUD-approved housing counselor, the court, and 211; never put a full SSN, bank login, or direct-deposit info into a rental listing or public AI tool. Did NOT rank any door, did NOT promise assistance/delay/win, did NOT assert any rule/amount/timeline/eligibility as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Ties to JobScout routing and the Enrollment Funnel. Saved to output/linkedin-2026-08-17-housing-eviction-rental-assistance-scam-ministry.md. PRIOR (#201): job loss / unemployment / reemployment scams -- older displaced worker man 58. PRIOR (#200): immigration / citizenship / notario fraud -- young first-gen home health aide woman 29. The plug is in."
runs_completed: 202
items_processed: 327
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
