---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-15T18:20:00Z"
current_task: "Generated LinkedIn post #194 -- the FUNERAL / BURIAL-COSTS ministry (the financial crisis three days after a death: the FTC FUNERAL RULE + the legal right to an itemized General Price List / decline the package / bring your own casket / prices by phone / no forced embalming; FUNERAL + BURIAL ASSISTANCE via state/county/township + indigent-burial funds; CHURCH BENEVOLENCE + burial funds + repast; VETERANS BURIAL BENEFITS -- VA allowance, national-cemetery grave, headstone, flag if he served; SOCIAL SECURITY lump-sum death payment + survivor benefits; LOWER-COST DIGNIFIED OPTIONS -- direct cremation, graveside, comparing 2-3 written price lists, a family-controlled memorial fund; 211 + legal aid; the truth that love is not the price of the casket and a dignified homegoing does not require crippling debt; the grief-exploitation UPSELL + FAKE-CROWDFUNDING (obituary photo lifted) + phantom-balance calls + burial-insurance cold-calls + obituary-harvesting identity theft; and the flat rule do-not-sign-a-five-figure-contract-in-the-first-48-hours, get-every-price-in-writing, nobody-honest-pressures-a-grieving-widow-to-decide-today, never-wire-money-or-pay-a-balance-to-anyone-who-called-you). A NEW lane, distinct from estate-planning/wills/legacy (PLANNING before death) and the older bereavement HELPER angle (the deaconess + the paperwork avalanche) -- #194 is the FINANCIAL squeeze of the funeral bill itself + the scams that hunt a family the moment somebody dies. QUIET-HELPER + augment-not-replace: AI explains the General Price List / Funeral Rule / direct cremation / SS death payment / VA burial allowance / survivor benefits and lays 2-3 itemized price lists side by side -- but does NOT plan the funeral, does NOT say what her husband deserves, does NOT decide eligibility or what any benefit pays, is NOT a funeral director/lawyer/SSA, and must NEVER be fed her SSN, her husband SSN, death-certificate details, or bank/insurance/account numbers. NEW persona rotated off the recent run (working man 57 #189 ... woman 63 #190 ... working man 64 #191 ... woman 44 #192 ... working man 49 #193): a WOMAN, 56, a school lunchroom aide, suddenly widowed after 33 years by her husband heart attack, a tiny life policy that will not cover it, three days into grief being walked toward the biggest package and about to sign it onto a card + a high-interest funeral loan, held there by the belief that a simpler homegoing would mean she loved him less. Rotates gender back to a WOMAN off the man (#193), centering a suddenly-WIDOWED WORKING WOMAN (56) in the acute financial shock of a death. Dignity, never deficit (PULSE guard vs she-should-have-planned / she-is-foolish / too-proud / just-pick-the-cheap-one). Core reframe: the widow across town lost him the same sudden way but a friend said love-is-not-the-price-of-the-casket, you-have-the-right-to-an-itemized-list-and-to-say-no, there is the VA benefit + the Social Security payment + the church burial fund, and that GoFundMe with his photo is not yours -- so she gave him a dignified homegoing without a $12,000 debt, while the woman in the pew signed the biggest package in 48 hours and got a second grief in the mail. Compliance TWICE in-body -- general navigation, NOT financial/legal advice, NOT an endorsement, NOT a benefit determination; verify with VA/SSA/the written price list/211; never put an SSN or bank/insurance/account numbers into a public AI tool; a reputable funeral home must give an itemized price list free and no honest party pressures a grieving family to sign in the first days. Did NOT rank any option, did NOT promise she qualifies, did NOT assert any benefit amount/rule as fact. Named geography: Harvey, Dolton, Robbins, Chicago Heights, Matteson, South Holland. Saved to output/linkedin-2026-08-15-funeral-burial-costs-ministry.md. PRIOR (#193): SNAP -- working man 49. PRIOR (#192): eviction -- working woman 44. The plug is in."
runs_completed: 194
items_processed: 319
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
