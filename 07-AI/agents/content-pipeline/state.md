---
agent: content-pipeline
display_name: "Content Pipeline"
emoji: "📹"
role: "Content Automation · The Plug AI"
status: idle
last_run: "2026-08-12T23:20:00Z"
current_task: "Generated LinkedIn post #179 -- the AI-literacy-itself ministry, deliberately the THIRD and FINAL word of The Plug AI tagline ('Get into AI'), CLOSING the full arc built across #177 ('Get Connected' / digital access) and #178 ('Get Skilled' / workforce training): 'Get Connected. Get Skilled. Get into AI.' The one post where The Plug AI's own core mission -- AI literacy -- IS the subject, not the quiet helper behind a benefits-navigation story; every prior post used AI as the patient someone who helps a family reach a resource, while this is about our people learning to use the tool itself so they aren't locked out of the economy it's rebuilding. NEW persona to rotate off the recent run (SNAP mother #173, homeownership woman #174, college father #175, caterer #176, teen boy #177, warehouse man #178): an OLDER woman, a church mother in her late 60s/70s -- keeper of the prayer list and the benevolence shoebox, ran households/budgets/ministries on a legal pad for 40 years -- the demographic the series had not yet centered and the person most quietly convinced 'AI is not for people like us.' Framed with full dignity as WISDOM meeting a missing translator, never a deficit (PULSE guard against 'old people can't learn tech'): one of the wisest, most discerning people the church produced; learned the phone/internet/smartphone before this; the problem was never her mind, it's that every time the world changed its language someone sat patiently with the family across town and never with her. Doors, fact-checked current/durable 2026, every one HEDGED + ROUTED, none oversold: (1) free tiers of the major AI assistants -- framed GENERALLY, no product ranked, hedged HARD with the two elder cautions (they can be confidently wrong -> verify; never feed them SSN/passwords/bank/full medical); (2) the local PUBLIC LIBRARY -- free computer/digital-literacy help + basic AI classes + a patient librarian, routed to 'your local public library' with Matteson Area Public Library / South Holland Public Library as examples; (3) free intro AI/digital courses -- online + community-college continuing-ed (Prairie State / South Suburban as examples); (4) The Plug AI ITSELF named directly, because 'Get into AI' IS the org's core offering; (5) 211/211.org; (6) scam/safety warnings weighted heavily for the elder persona -- 'get rich with AI in a weekend' + 'pay up front for AI certification' mills, and critically the AI VOICE-CLONING / deepfake grandparent scam (fake grandchild's voice begging for money), with concrete defense (hang up, call the child back on a known number) and the FTC-aligned truth that a real free class never charges a fee. Augment-not-replace held HARD, sharpened ('Not to replace her wisdom. Not to think for her, not to pray for her, not to discern for her... Her wisdom is hers... It is only a translator for a world moving fast'). Core reframe: the gap is not that our elder is less capable -- one family was handed the tools, a house where someone already used them, and a grandchild who sat down and turned on the light; the other was handed a smartphone and a soft lie that the future was a room she wasn't invited into. Compliance stated TWICE in-body -- general navigation, NOT an endorsement of any AI product/company, NOT tech/legal/financial advice; tools can be wrong + must never get private info; voice-cloning + 'AI riches' scams hunt the people who love and try hardest. DELIBERATELY did NOT rank one AI assistant/library/course over another or promise any outcome. Ties directly to the tagline's THIRD word and closes the #177-#179 arc; ties to Community Intake's routing. The plug is in. --- PRIOR (#178): the free-workforce-training / apprenticeship ministry -- the warehouse man whose body was quitting, told at 17 the classroom was for other kids, the tagline's SECOND word 'Get Skilled.' PRIOR (#177): the digital-access / homework-gap ministry -- the honor-roll teen doing homework on a taped-up phone in the church parking lot, the FIRST word 'Get Connected.'"
runs_completed: 179
items_processed: 304
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
