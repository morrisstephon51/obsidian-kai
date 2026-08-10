---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: running
last_run: "2026-08-10T18:44:00Z"
current_task: "Generated LinkedIn post #169 -- the veterans / military-benefits ministry: the old deacon who served, the one every veteran in the congregation quietly comes to (you were in, right -- they denied my claim), who drives a brother to the VA at Hines so he does not sit alone, sat with a widow the week after the funeral, and is treated like he works for the VA though he never did -- and then single-handedly trying to hold the whole veterans-benefits maze for men and women owed something the country wrote down and then made almost impossible to find: that a denial is the START of an appeal most people win with help, not the end; that filing is FREE and it is illegal to charge for the initial claim (accredited VSOs at the VFW, American Legion, DAV, and the Cook County Veterans Assistance Commission do it at no cost, only accredited attorneys/agents may charge and only on appeals after a decision); the PACT Act reality (burn pits, Agent Orange -- conditions the VA used to fight now presumed service-connected, a generation owed care it never claimed); the less-than-honorable discharge that may be upgradeable, and VA mental-health care that can be open even without an upgrade; wider VA health-care enrollment; the needs-based VA pension with Aid & Attendance for the low-income wartime vet rationing his pills; the survivor benefit (DIC) a widow is owed and buries him never knowing to ask; and homeless-veteran programs (SSVF, HUD-VASH, 877-424-3838) for the man too proud to say the word; AI as the accredited-savvy navigator a resourced veteran gets from an attorney or a sharp VSO on speed dial -- plus the real free help any veteran can reach: an accredited VSO, the Cook County VAC, VA.gov, the VA benefits line (800-827-1000), the homeless-veteran line (877-424-3838), and the Veterans Crisis Line (988 then press 1); augment-not-replace held (the ride to Hines and the trust stay his), frees him to say you earned this, it did not expire, we are going to go get it; opens a NEW resource-navigation lane -- veterans / military-benefits navigation -- kept distinct from health (population health), civil legal-aid (#168), benevolence (cash), senior/caregiver (eldercare), housing/eviction (tenant), employment (jobs), disability/special-needs (inclusion), and tax/EITC (#166); added a care note on VA claim-shark scams (a cut of your back pay or a fee to file your first claim = breaking the law) paired with the affirming fact that real accredited help is free; CRITICAL compliance framing stated twice in-body -- general navigation, NOT claims representation or legal advice, and helping is NOT accredited representation -- always route to an accredited VSO, the Cook County VAC, VA.gov, or an accredited attorney for the actual claim; ties to Community Intake; the plug is in"
runs_completed: 169
items_processed: 294
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
