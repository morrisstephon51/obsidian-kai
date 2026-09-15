---
type: plan
tags:
  - finance
  - income
  - forming-paws
  - plug-ai
created: 2026-09-13
updated: 2026-09-13
---

# Income Plan — 2026-09-13

Stefan is unemployed, has **no transportation**, and is full time on this. Every step works by phone, email, video, or online. See [[Financial Goals]], [[Forming Paws/project-overview|Forming Paws]], [[The Plug AI/project-overview|The Plug AI]].

**Revised the same day** after four updates: Misericordia is closed (they moved on to another candidate on Sep 11), in-person visits are out, both businesses go for-profit, and the plan must stay free of paid tools.

## Where things actually stand (verified 2026-09-13)

| Channel | Reality |
|---|---|
| Indiegogo "Puppy Power" | Still a campaign preview; it never launched. 124 followers. Indiegogo is all or nothing now (flexible funding was retired Oct 2025). |
| Open Collective "The Plug AI" | No fiscal host, inactive, $0. Irrelevant now that both businesses are going for-profit. |
| Forming Paws | 13 real members (9 joined in the last 30 days, 8 active), 10 dogs, 2 verified. No payments yet. |
| Website outreach | At least 20 emails in August, 0 replies. Diagnosis in `~/ai-consulting-business/docs/08-remote-outreach-plan.md`. |
| CHA WORC | Advisor Niquenya Fulbright, meeting **Wednesday Sep 16**. Section 3 Business Concern eligible through the voucher. |
| Stripe | Account exists. |

## Decision: for-profit

- **Forming Paws** goes for-profit. Animal welfare funders fund 501(c)(3) shelters and adoption, not breeding platforms, and verification is a paid service anyway.
- **The Plug AI** earns through paid services: websites and AI help.
- **Structure:** decide with Niquenya on Wednesday. Option A is one LLC with "Forming Paws" as an assumed name, about $270 in state fees. Option B is two LLCs, about $300 plus two annual reports.
- **Follow-on work:** the Forming Paws site says "nonprofit" or "501(c)(3)" in 22 places across 10 files (/about, /donate, home, privacy, footer, FAQ, journey, and others). Update the copy once the entity type is settled, so the site stays honest.

## Daily prep agent (cloud routine)

Every day at 6:00am Chicago time (11:00 UTC; after Nov 1 it runs at 5:00am), a cloud agent emails you a **"Daily outreach brief"** by about 7am. **Reply to that email with what happened**, one line per business, for example "Niko's: no answer" or "Lady's: deposit paid". The next morning's run reads your reply.

- **What it does:**
  - finds 20 barbers, salons, and braiders with no website
  - builds 3 site previews and publishes them as public links search engines are told not to index
  - fills in the call list, texts, and follow-ups
  - saves a dated "Website Outreach Tracker" sheet in Drive
  - opens a pull request (PR) for theplugai.info/websites
  - after Sep 16, once you reply with the business structure, opens a PR removing the nonprofit copy from Forming Paws
- **What it never does:** contact a business, send anything to anyone but you, or merge a PR.
- **When it stops:** at 3 paying clients, it sends a final report. Then pause it at https://claude.ai/code/routines/trig_01Fwen5EKwNu1HRUUMPZbH6J
- **Where things live:**
  - instructions: `docs/08-remote-outreach-plan.md` in the private ai-consulting-business repo
  - previews: Vercel project `site-previews`

## This week

- [ ] **Mon:** send the Forming Paws member survey (below).
- [ ] **Mon to Tue:** build the foundation from the outreach plan: services page at theplugai.info/websites, one sender identity, free Cal.com booking link, $175 Stripe deposit link, free Google Voice number.
- [ ] **Mon to Tue:** text 30 people the referral ask.
- [ ] **Tue:** review the CHA brief (Google Doc "Business Readiness Update — Stephon Morris — CHA WORC — Sept 16, 2026", vault copy [[CHA Meeting Brief — 2026-09-16]]).
- [ ] **Wed:** CHA meeting. Leave with an answer on the structure, the license, Section 3 timing, and how income affects the voucher.
- [ ] **Wed to Fri:** start preview-first calls, 20 a day.

## Forming Paws member survey (draft, send from founder@theplugai.info)

Subject: 4 quick questions about Forming Paws

> Hi [first name],
>
> You're one of the first 13 members of Forming Paws, so your answers shape what comes next. Reply with a number or a few words.
>
> 1. Would you pay $29 once to get a dog health-verified, which unlocks matching? (yes / maybe / no)
> 2. Would you pay $49 a year for membership with verification, priority matching, and the education guides? (yes / maybe / no)
> 3. What is the one thing that would make Forming Paws worth paying for?
> 4. What almost made you stop using it?
>
> Founding members keep free verification, as promised.
>
> Thank you,
> Stephon Morris

## Next 30 days

- 3 paying website clients (outreach plan scoreboard)
- LLC, EIN, and City license in place, following Niquenya's advice
- Survey results in; turn on the $29 verification fee only if members say they would pay
- Indiegogo: revisit only after the first paying customers. Use a small goal and honest copy.

## Stop doing

- Bulk email with fake "re:" subjects
- "Free website" offers
- Building Forming Paws features before anyone has paid
- Paid tools when a free one works

---
*Backlinks: [[01-DAILY/To-Do-List|To-Do-List]] · [[02-PROJECTS/Finance/CHA Meeting Brief — 2026-09-16|CHA Meeting Brief (Sep 16)]] · [[02-PROJECTS/Finance/index|Finance Hub]]*
