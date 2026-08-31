---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-31T08:27:00Z"
current_task: "Generated LinkedIn post #253 -- WHOLLY NEW DOMAIN: EXPUNGEMENT / CRIMINAL-RECORD SEALING / REENTRY / FREE LEGAL AID for a young working man of 29 in the south suburbs who did his time or paid his fine years ago, has stayed clean since, and keeps getting shut out of jobs and apartments because one old case shows up on every background check, then framed the truths that change everything: under Illinois law many records can be EXPUNGED (erased) or SEALED (hidden from ordinary background checks) after time passes, the legal help to do it is FREE (Legal Aid Chicago, Cabrini Green Legal Aid, LAF, law-school clinics, free Cook County court expungement clinics, statewide New Leaf Illinois), a real legal aid lawyer NEVER guarantees a judge's decision and never charges a big up-front fee to 'erase' a record, and NO ONE can wipe a record by phone for gift cards or sell a guaranteed pardon. Doors: free legal aid + free court expungement clinics; pull his own RAP sheet from Illinois State Police in his own name; New Leaf Illinois to find help; Illinois Prisoner Review Board (free to apply) for a pardon when a case isn't expungement-eligible. Scam spine: RECORD-CLEARING/EXPUNGEMENT MILL (big fee, files nothing, vanishes), GUARANTEED-EXPUNGEMENT/PAY-TO-ERASE ADVANCE-FEE (no one can guarantee a judge), FAKE PARDON/CLEMENCY-FOR-SALE, COURT/PROBATION PHONE IMPOSTER (warrant/fee-arrest-gift-cards), and BACKGROUND-CHECK/'REMOVE YOUR MUGSHOT' EXTORTION. Flat rule stated TWICE + SEPARATE caution that legal aid / New Leaf Illinois / Cabrini Green / court clinics / ISP RAP sheet / Prisoner Review Board are NOT scams. Dignity-never-deficit (a man who paid his debt and stayed clean is not his worst day and not his record; being locked out by one old case is a legal barrier with a legal remedy, not a character flaw; clearing a record is claiming the future his own work already earned, not hiding). AI quiet-helper/augment-not-replace with compliance TWICE (explains which cases may be eligible to expunge or seal, helps him get and read his own RAP sheet, finds the nearest free clinic + hours, decodes the petition, preps his questions; does NOT file the petition, does NOT decide eligibility or promise the record will be cleared or give legal advice, never hands over his info, not a substitute for a real legal aid lawyer or the court; verify with a real legal aid org / the court). Rotated to a MAN age 29 off #252 woman 39; distinct from #251 man 46, #250 woman 34, #249 man 61, #248 woman 52. WHOLLY NEW reentry/criminal-records domain distinct from tax/refund (#252), disability/SSDI (#251), job search/workforce (#250), utility/energy (#249), medical debt (#248), citizenship (#247), college aid (#246), eviction (#245). Ties to The Plug AI Get-Connected + benefits-navigation + reentry + faith-community pillar. Serves Plug AI community + faith-community + working-family + reentry + digital-literacy pillars AND BigHeart church partnerships. Named geography: Harvey, Dolton, Markham, Chicago Heights, Riverdale, Calumet City, South Holland, Blue Island, Robbins, Ford Heights. Saved to output/linkedin-2026-08-31-expungement-record-sealing-reentry-free-legal-aid-cook-county-clean-slate-record-clearing-mill-guaranteed-expungement-fee-fake-pardon-court-imposter-mugshot-extortion-scam-ministry.md. PRIOR (#252): free tax filing / EITC / CTC / VITA (working mother 39). PRIOR (#251): Social Security disability / SSDI / SSI (disabled tradesman 46). PRIOR (#250): job search / employment / workforce (single mother 34). The plug is in."
runs_completed: 252
items_processed: 377
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
