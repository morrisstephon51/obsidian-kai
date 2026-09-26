# Fleet Merge Runbook — 2026-09-24 (codex R376, amended R377, extended R378, re-verified R379, auto-close-audited R380, Section-6 draft-state corrected R382 2026-09-25)

**Supersedes:** MERGE-RUNBOOK-2026-09-15.md (9 days stale; predates JobScout #62-#67, Community #39/#40, content #8/#9).

> **R377 AMENDMENT (2026-09-24):** A full-fleet per-repo issue sweep found a **5th active agent
> repo** the R376 runbook missed — `ai-video-reel-generator` (the trends->avatar-video->clip->
> schedule->post automation loop). It is in the *same* owner-merge-blocked state with **2 MERGEABLE
> fix PRs** (one of them fixes the app's primary output being dead in every config). Added as
> **Section 5** below. Root cause of the miss: account-wide `gh search` drops whole repos; only a
> per-repo `gh issue list` sweep is authoritative. The fleet is **5 repos, not 4.**

> **R378 EXTENSION (2026-09-25):** Re-ran the full per-repo sweep across **all 24 non-archived
> repos** (not just the agent fleet). Agent fleet re-verified LIVE: still **0 merges since ~Sep
> 11-12** (last merges JobScout #24@09-11, Community #13@09-12, EFA #23@09-11, avrg #25@09-10), all
> 33 agent PRs still MERGEABLE, Sections 1-5 unchanged. NEW FINDING: the merge backlog **extends
> beyond the agent fleet** — 3 personal/business/vault repos hold 7 more stranded PRs the R376/R377
> runbook never listed (one open since **Jun 13**, older than any agent PR). Added as **Section 6**.
> Same root cause as the R377 miss: account-wide search hides whole repos. One of the 7 (Link-inbio
> #6) is a stale empty-diff PR flagged to **CLOSE**, not merge.

> **R379 LIVE RE-VERIFICATION (2026-09-25 ~13:15 UTC):** Re-ran the authoritative per-repo sweep
> across all 24 non-archived repos. **Nothing has changed since R378 this morning — this runbook is
> still 100% accurate; execute it as written.** Confirmed live:
> - **Still 0 merges/closes fleet-wide.** No PR merged or closed in the last 2 days; last-merged SHAs
>   unchanged (JobScout #24 @09-11, Community #13 @09-12, EFA #23 @09-11, avrg #25 @09-10). Owner-merge
>   remains the sole bottleneck.
> - **All open PRs still MERGEABLE:** 32 agent PRs (JobScout 6, Community 14, EFA 5, content 5, avrg 2)
>   + 7 non-agent PRs = 39, every one `MERGEABLE`. Stacked-base map holds exactly — Community's 10
>   `fix/*` non-default bases (#17/#19/#21/#25/#27/#29/#31/#33/#35/#37) and content #4/#8 confirmed.
> - **Section 6 currency holds:** psychic #1 (+7800/-53) / #25 / Link-inbio #5 / #15 / kai-vault #3 all
>   `behind_by:0`; Link-inbio **#6 still +0/-0, behind 13 -> CLOSE** (stale, confirmed); kai-vault #2
>   behind 7 but CLEAN (still "confirm current" before merge).
> - **Fix queue still 100% covered:** spot-proved on JobScout (the deepest, 19 open issues) - every
>   issue maps to a covering PR (#66->#67, #64->#65, #62->#63, cadence tower #30-#59 -> keystone #61,
>   #26->#27). No new uncovered issue has appeared anywhere; **nothing new to build.**
> - **Correction to the R378 count:** there are **32** open agent PRs, not 33 (R378 off-by-one; no PR
>   closed - recount 6+14+5+5+2=32).
>
> **R380 AUTO-CLOSE AUDIT (2026-09-25 ~17:20 UTC):** Nothing changed since R379 — sweep of all
> non-archived repos still shows 0 merges/closes, every open issue covered, 4 recently-touched
> non-agent repos (obsidian-kai, ecc-staffing-preview, ai-consulting-business, command-center-redirect)
> hold 0 issues/0 PRs (no 6th agent repo, no new backlog). This run verified the 3 consequential
> auto-close claims via the **authoritative `closingIssuesReferences` GraphQL field** (not body-text
> grep, which misreads bold/mid-sentence keywords): **avrg PR#27 auto-closes BOTH #26 AND #28** (the
> "Also closes #28" prose IS parsed — so avrg needs NO hand-close, #28 is not an uncovered sibling);
> **JobScout #61 and Community #38 both have EMPTY closingIssuesReferences** -> the hand-close loops in
> Sections 1-2 are confirmed REQUIRED (merging those keystones closes nothing automatically).

**Situation (live-verified 2026-09-24):** 0 merges across all **5** agent repos since ~Sep 11-12.
Fix queue is 100% complete — every open issue has a covering, MERGEABLE PR. Both large
keystones are independently superset-certified in fresh clones (JobScout #61 via Python 3.14;
Community #38 via 94/94 unit tests today, incl. newest siblings #34/#36). **Owner-merge is the
sole bottleneck.** This runbook is copy-paste executable; every PR below is MERGEABLE right now.

> Trap that has silently no-op'd past sweeps: many Community sibling PRs sit on **non-default
> stacked bases** — clicking "Merge" lands them on an intermediate branch, NOT production.
> The plan below CLOSES those (their fix is already in the keystone) instead of merging them.

---

## 1. JobScout — `morrisstephon51/job_opportunity_scanner` (default `claude/clever-cannon-IDh3G`)
6 open PRs, all on default, all MERGEABLE. #61 is the scorer keystone (closes cadence issue
cluster #30-#59). #61 and #63 both edit `scorer.py` — merge #61 first; if #63 then flips to
CONFLICTING, author rebases #63 on new default before merging.

```
R=morrisstephon51/job_opportunity_scanner
gh pr merge 61 --repo $R --merge   # keystone: salary-cadence regex families. NB: #61 has NO closing keywords (closingRefs=[]) -> FIXES the code but will NOT auto-close its issues; hand-close them below.
gh pr merge 63 --repo $R --merge   # whole-word SEARCH_KEYWORDS match (closes #62)  [re-check MERGEABLE after #61]
gh pr merge 25 --repo $R --merge   # salary-range placeholder-0 / shared-k fix
gh pr merge 27 --repo $R --merge   # recency: "X years ago" past MAX_DAYS_OLD (closes #26)
gh pr merge 65 --repo $R --merge   # AGENCY_BLOCKLIST "TEKsystems" one-word match (closes #64)
gh pr merge 67 --repo $R --merge   # sync /scan prompt to scorer/config, restore `trainer` (closes #66)
# #61 carries no "Closes #NN" refs, so hand-close the 15 cadence/salary issues it supersedes:
for n in 30 32 34 36 38 41 43 45 47 49 51 53 55 57 59; do \
  gh issue close $n --repo $R --comment "Fixed by #61 (anchored salary/cadence regex families; superset-proven in a fresh Python 3.14 clone). #61 lacked a closing keyword, closing manually."; done
```
scorer.py is fully farmed — do NOT open more per-token cadence PRs.

## 2. Community Intake — `morrisstephon51/-Community_intake_Routing` (default `claude/quirky-galileo-UGnfz`)
Collapses 14 open PRs -> 2 merges. #38 keystone is a proven behavioral superset of the entire
#14-#36 classify tower (verified today, both `intake.js` + `api/intake.js` copies).

```
R=morrisstephon51/-Community_intake_Routing
gh pr merge 38 --repo $R --merge   # keystone intent-based classifier. NB: #38 has NO closing keywords -> will NOT auto-close #14-#36; hand-close them below.
# Close the 12 superseded classify siblings — code already in #38, no loss.
# (10 of these are on NON-DEFAULT stacked bases; merging them = silent no-op vs production.)
for n in 15 17 19 21 23 25 27 29 31 33 35 37; do \
  gh pr close $n --repo $R --comment "Superseded by #38 (proven behavioral superset of the #14-#36 tower, verified 2026-09-24). Closing to avoid a non-default-base no-op."; done
# #38 carries no "Closes #NN" refs, so hand-close the 12 classify issues it supersedes:
for n in 14 16 18 20 22 24 26 28 30 32 34 36; do \
  gh issue close $n --repo $R --comment "Fixed by #38 (intent-based classifier; proven behavioral superset of the #14-#36 tower, 94/94 tests 2026-09-24). #38 lacked a closing keyword, closing manually."; done
gh pr merge 40 --repo $R --merge   # web /api/intake email-routing parity (closes #39) — independent of classify, still needed
```

## 3. Enrollment Funnel — `morrisstephon51/Enrollment_Funnel_Agent` (default `claude/keen-noether-VED1j`)
5 open PRs, all on default, all MERGEABLE. Merge #25 FIRST (adds the `test/*.test.ts` glob
runner). #29 and #31 both touch `scorer.ts` — merge #29 then re-check #31 mergeable.

```
R=morrisstephon51/Enrollment_Funnel_Agent
gh pr merge 25 --repo $R --merge   # GA4 "Sessions" thousand-separators + test-glob runner (merge first)
gh pr merge 26 --repo $R --merge   # trim GA4 UTM CSV so hand-edits don't zero sessions
gh pr merge 27 --repo $R --merge   # Meta alias whole-filename-token match
gh pr merge 29 --repo $R --merge   # unify weekly engagement weights, one formula (closes #28)
gh pr merge 31 --repo $R --merge   # surface empty engagement baseline vs false all-clear (refs #30) [re-check after #29]
```
OWNER-ONLY (no PR possible): issue #30 upsertPerformance persistence root cause (needs live
Supabase schema map); issue #24 retire stale `main` (branch admin — do NOT merge main->default).

## 4. Content Pipeline — `morrisstephon51/agent_I_content` (default `claude/eloquent-edison-aF7yG`)
#4 is stacked on #2's branch (`fix/enforce-caption-char-limits`); #8 is stacked on #6's branch.

```
R=morrisstephon51/agent_I_content
gh pr merge 2 --repo $R --merge          # enforce CAPTION_LIMITS in code
gh pr edit  4 --repo $R --base claude/eloquent-edison-aF7yG   # retarget off #2's branch to default
gh pr merge 4 --repo $R --merge          # enforce topic-derived hashtags + hashtag-filter.test.ts (closes #3) — DO NOT close, unique code
gh pr merge 6 --repo $R --merge          # validate post.platform before insert (closes #5) — brings platform-validation.test.ts
gh pr merge 9 --repo $R --merge          # glob test runner scripts/run-tests.ts (auto-discovers all *.test.ts)
gh pr close 8 --repo $R --comment "Superseded by #9: the glob runner auto-discovers platform-validation.test.ts (added by #6). #8 only hand-wired package.json, now redundant."
```
VERIFY after: `gh pr checkout 9` won't apply post-merge; instead confirm `scripts/run-tests.ts`
lists `platform-validation.test.ts` in its run output once #6+#9 are on default. If #9's glob
does NOT pick it up, re-open #8 and merge it (retarget base->default first).

## 5. AI Video Reel Generator — `morrisstephon51/ai-video-reel-generator` (default `main`)
The 5th agent repo (R376 runbook omitted it). Default branch is a normal `main` (NOT a `claude/*`
branch like the others). 2 open PRs, both **MERGEABLE**, disjoint files -> order-independent.
Unlike the JobScout/Community keystones, **both PRs carry proper closing keywords** (verified via
`closingIssuesReferences`) -> they auto-close their issues on merge; **no hand-close loop needed.**

```
R=morrisstephon51/ai-video-reel-generator
gh pr merge 27 --repo $R --merge   # remove unsatisfiable ADMIN_SECRET guard on the 2 browser-only routes (auto-closes #26 AND #28)
gh pr merge 31 --repo $R --merge   # anchor best-post-times to America/New_York, not server UTC (auto-closes #30)
```
- **#27 is the critical one:** the fail-closed `ADMIN_SECRET` guard made the app's PRIMARY output
  ("Schedule for Publishing") return 401 in *every* config, and silently no-op'd "Remove persona."
  It closes both #26 and #28 (PR #29, the #28-only fix, was correctly closed as redundant).
  **Owner judgment flagged by the author:** #27 reverses prior deliberate hardening PRs (#20, #14),
  so it is intentionally a your-call merge — that is exactly why it belongs in this runbook, not auto-merged.
- **#31** is the serverless-UTC schedule-skew fix (every auto-post fired 4-5h before the researched
  peak; also made dev vs prod diverge for identical input). DST-correct, dependency-free.
- OWNER-ONLY: issue #5 (provision a live Supabase project) — infra/setup, no PR possible; blocks only
  end-to-end runtime verification, not the by-inspection correctness of #27/#31.

## 6. Non-agent repos — also owner-merge-blocked (R378 add)
These are Stef's own **personal / business / vault** repos (default branch `main`), so what goes
live is entirely the owner's editorial call — even more than the agent fixes. 7 stranded PRs, all
MERGEABLE/CLEAN. Currency verified by `compare base...head` behind_by (per the "CLEAN ≠ current"
rule): behind=0 means the branch still fits `main` today.

**6a. psychic-bassoon** (AI-consulting / services website) — default `main`
```
R=morrisstephon51/psychic-bassoon
gh pr merge 1  --repo $R --merge   # real content + working forms + resource detail pages (34 files, +7800; open since Jun 13, ahead 17 / behind 0) — NON-draft, merge-ready
# gh pr merge 25 --repo $R --merge # BLOCKED (R382): #25 is a DRAFT (isDraft:true) -> `gh pr merge` fails "Pull request is in draft state". OWNER-ONLY: "Mark ready for review" first, then merge. (add /websites services page, +297; behind 0)
```

**6b. Link-inbio** (link-in-bio site) — default `main`
```
R=morrisstephon51/Link-inbio
gh pr merge 15 --repo $R --merge   # rebuild Command Center as live scroll dashboard (+2288/-541; behind 0) — NON-draft, merge-ready
# gh pr merge 5 --repo $R --merge  # BLOCKED (R382): #5 is a DRAFT (isDraft:true) -> merge fails. OWNER-ONLY: "Mark ready for review" first. (Obsidian ops vault: domain registry / tracker / grant log; behind 0)
gh pr close 6  --repo $R --comment "Empty diff (+0/-0), 13 commits behind a diverged main -> the condensed-resume PDF is already on main or was abandoned, and the fellowship deadline it targeted has passed. Closing as stale."   # #6 is also a DRAFT; closing a draft is fine
```

**6c. kai-obsidian-vault** (vault docs) — default `main`
```
R=morrisstephon51/kai-obsidian-vault
# BLOCKED (R382): BOTH PRs are DRAFTS (isDraft:true) -> neither can be merged with `gh pr merge` (fails "Pull request is in draft state"). OWNER-ONLY: "Mark ready for review" first.
# gh pr merge 3 --repo $R --merge  # DRAFT: record theplugai.info scroll-homepage deployment in vault docs (+3/-3; behind 0)
# gh pr merge 2 --repo $R --merge  # DRAFT: CHA Resident Business Owner Program business plan (+129; behind 7 — also confirm current before marking ready)
```

**Also owner-action, NOT a merge:** `forming-paws` **#8** is a founder-action tracking issue — the
IL Secretary-of-State not-for-profit filing steps (name check, [CITY]/[PLACEHOLDER] fill-in, $50
online filing, board bylaw adoption) are all **[YOU]** steps for Stef. No code/PR is pending against
it (the old Issue #6 / PR #7 Supabase blocker was already cleared 2026-08-11). It stays open until
Stef files; nothing here is a merge.

---

---

## Net effect
- **JobScout:** 6 merges + hand-close 15 cadence issues (#61 has no closing keyword) -> all 19 open issues resolved.
- **Community:** 2 merges + 12 PR-closes + hand-close 12 issues (#38 has no closing keyword) -> all 13 open issues resolved (10 no-op traps sidestepped).
- **EFA:** 5 merges -> #28 + GA4/CSV fixes; #30/#24 remain owner-only.
- **Content:** 4 merges + 1 close -> all 3 open issues resolved.
- **AI Video Reel Gen (R377 add):** 2 merges -> auto-closes #26/#28/#30 (proper closing keywords, no hand-close); #5 (Supabase provisioning) remains owner-only.
- **Non-agent repos (R378 add; R382 draft-state correction):** psychic-bassoon **1 merge (#1)** — #25 is a DRAFT (owner-only); Link-inbio **1 merge (#15)** + 1 stale-close (#6, itself a draft) — #5 is a DRAFT (owner-only); kai-obsidian-vault **0 merges** — BOTH #2 and #3 are DRAFTS (owner-only). Executable Section-6 total is **2 merges + 1 close**, NOT 6+1: the other 4 draft PRs need the owner to "Mark ready for review" first. `forming-paws #8` is founder-action (IL-SOS filing), not a merge.

After this sweep (agent fleet + Section 6) the only remaining items are genuinely owner/founder-scoped:
EFA #30 schema-persistence, EFA #24 branch retirement, AI-Video-Reel #5 Supabase provisioning,
`forming-paws #8` (Stef's IL-SOS not-for-profit filing), and the **4 Section-6 DRAFT PRs** (psychic #25,
Link-inbio #5, kai-vault #2 + #3) which stay owner-only until Stef marks each "Ready for review."
Nothing left to build — the entire fleet-wide queue is now either a MERGEABLE non-draft PR awaiting the
owner's merge, an owner-only draft, or an explicit owner/founder action.

*Prepared by codex R376; Section 5 + 5th-repo reconciliation added R377 (2026-09-24); Section 6 (non-agent repos) + fleet-wide re-verification added R378 (2026-09-25); live re-verified unchanged + count corrected (32 agent PRs) R379 (2026-09-25 ~13:15 UTC). Doc only — no code changed, no merges executed (reserved for owner per governance).*


### R381 completeness note (2026-09-25 ~21:40 UTC) — two Section-6 repos were missing; both NON-actionable
Full per-repo sweep of **all 25 non-archived repos** re-run. All 5 agent repos + the 4 Section-6 non-agent
repos are **unchanged vs R380** (JobScout 19i/6pr, Community 13i/14pr, EFA 3i/5pr, avrg 4i/2pr, content
3i/5pr; psychic-bassoon 0i/2pr, Link-inbio 0i/3pr, kai-obsidian-vault 0i/2pr, forming-paws 1i/0pr).
Still **0 merges fleet-wide**. The sweep also surfaced **two repos with open items that Section 6 had
never listed** — both are NON-actionable, so **no runbook action / no PR / no merge**:
- **`skills-introduction-to-git` #1 "Exercise: Introduction to Git"** — repo is templated from
  `skills/introduction-to-git`; the issue is the GitHub-Skills **course exercise tracker** auto-opened by
  `app/github-actions`, not a code defect. Ignore (or close the course when done). NOT an uncovered bug.
- **`----Workspace-notes-2025-01-07_notes.md` PR #1** — owner-authored **DRAFT** (isDraft:true) Obsidian
  master-vault build (+2677/-0, 24 files). Draft = unmergeable until Stef marks it ready. **Owner-only.**

Net: every non-archived repo is now accounted for. No new agent-fleet code issue lacks a covering PR;
the only bottleneck remains owner-merge. — codex R381


### R382 Section-6 draft-state correction (2026-09-25 ~22:10 UTC) — 4 merge commands would have failed
Ran a **live merge-readiness audit** of every runbook-target PR (`mergeable` + `mergeStateStatus` + `isDraft`),
something prior runs skipped — R378/R379 verified `behind_by` currency but never `isDraft`. Findings:

- **Agent fleet (Sections 1-5) all clear:** all 32 agent PRs (JobScout 6, Community 14, EFA 5, content 5,
  avrg 2) are `MERGEABLE`/`CLEAN`, `isDraft:false`, no conflict drift after ~2 weeks. Sections 1-5 execute
  as written. JobScout issue->PR coverage re-proven 100% live (#66->#67, #64->#65, #62->#63, #26->#27,
  cadence tower #30-#59 -> keystone #61). Community non-default stacked bases hold exactly (10 on `fix/*`:
  #17/#19/#21/#25/#27/#29/#31/#33/#35/#37; only #40/#38/#23/#15 on default). content #4/#8 stacked as noted.
- **Section 6 defect fixed:** 5 of Section 6's 6 `gh pr merge` commands targeted **DRAFT** PRs and would have
  died on `"Pull request is in draft state"`:
  - psychic-bassoon **#25 = DRAFT** (only #1 is merge-ready)
  - Link-inbio **#5 = DRAFT** and **#6 = DRAFT** (only #15 is merge-ready; #6 still the stale-close target)
  - kai-obsidian-vault **#2 = DRAFT** and **#3 = DRAFT** (NEITHER merge-ready)
  All four content-drafts are the owner's own editorial WIP (business plan, resume PDF, ops vault, deployment
  record) -> correctly **owner-only** per the classify-by-draft-state lesson. Command blocks 6a/6b/6c now
  comment out the draft merges with an OWNER-ONLY "Mark ready for review first" note; Net effect corrected
  from "6 merges + 1 close" to **2 executable merges (#1, #15) + 1 close (#6)**.

Still **0 merges fleet-wide**; owner-merge remains the sole bottleneck. Doc only — no code changed, no merges
executed (reserved for owner per governance). — codex R382


### R383 executable script + live re-audit (2026-09-26T06:17:47Z) — runbook is now one command
Re-ran the authoritative per-repo sweep (all 21 non-archived repos) and the LIVE merge-readiness
audit (isDraft + mergeable + mergeStateStatus + baseRefName) of every target PR. **Zero drift vs
R382:** all agent-fleet PRs still `MERGEABLE`/`CLEAN`/non-draft; Community's 10 `fix/*` non-default
stacked bases + content #4/#8 stacking hold exactly; the 5 Section-6 drafts (psychic #25, Link-inbio
#5/#6, kai-vault #2/#3) unchanged. Still **0 merges fleet-wide**; owner-merge remains the sole bottleneck.

New this run: this prose runbook is now also a single guarded executable —
**`merge-fleet.sh`** (same folder). It is **dry-run by default** (prints the plan, touches nothing);
`./merge-fleet.sh --execute` performs the whole sweep in dependency order. Before EVERY action it
re-checks the PR live and **auto-skips any draft or non-MERGEABLE PR** (so it can't die mid-run, can't
merge a draft, and can't no-op a stacked base). It runs the keystone hand-close loops (#61, #38) and
retargets content #4 off #2's branch automatically. Verified dry-run net effect matches this runbook
exactly: **21 merges + 14 PR-closes + 1 retarget + 27 issue-closes + 4 draft-skips**. Per-repo scope
flags too (`--only jobscout|community|efa|content|avrg|psychic|linkinbio|kaivault`). Doc/script only —
nothing executed (reserved for owner per governance). — codex R383


### R384 live drift re-check (2026-09-26) — still 100% accurate, still 0 merges
Re-ran the authoritative per-repo sweep across **all 24 non-archived repos** + the live
merge-readiness audit (`merge-fleet.sh` dry-run live-checks state/isDraft/mergeable on every
target before it prints a merge vs skip line). **ZERO drift vs R383:**
- **Counts identical on every repo** — JobScout 19i/6pr, Community 13i/14pr, EFA 3i/5pr, avrg
  4i/2pr, content 3i/5pr; psychic 0i/2pr, Link-inbio 0i/3pr, kai-vault 0i/2pr, forming-paws 1i/0pr;
  + non-actionable skills-introduction-to-git (course-bot issue) and ----Workspace-notes (owner
  draft PR). No new repo, no new uncovered issue, no 6th agent repo.
- **Still 0 merges fleet-wide** — last-merged SHAs unchanged from R379/R383: JobScout #24 @09-11,
  Community #13 @09-12, EFA #23 @09-11, avrg #25 @09-10 (content's recent tower #2-#9 has never
  merged; its last merge is #1 @Jun). The stall is now **~15 days**. Owner-merge is the sole bottleneck.
- **Dry-run net effect still exactly 21 merges + 14 PR-closes + 1 retarget + 27 issue-closes +
  4 draft-skips.** All 21 agent-fleet targets live-verified OPEN + MERGEABLE + non-draft (none went
  GONE/CONFLICTING); the 4 Section-6 drafts (psychic #25, Link-inbio #5, kai-vault #2/#3) correctly
  auto-skipped. Community's 10 `fix/*` non-default stacked bases + content #4/#8 stacking still hold.

Nothing to build — the entire queue is a MERGEABLE non-draft PR awaiting owner-merge, an owner-only
draft, or an explicit owner/founder action. `merge-fleet.sh --execute` still clears it in one shot.
Doc only — no code changed, no merges executed (reserved for owner per governance). — codex R384


### R385 coverage claim verified by CODE INSPECTION, not just counts (2026-09-26)
Prior runs re-confirmed the stall by matching issue/PR **counts**. This run upgraded the confidence
level: cloned JobScout's default branch (`claude/clever-cannon-IDh3G`) and **read the actual code +
every open-PR diff** to prove the "every code issue has a covering MERGEABLE PR" claim, not just assume it.
- **All 19 open JobScout issues map 1:1 to the 6 open MERGEABLE PRs:** #26->#27 (recency "X years ago");
  the 15-issue salary-cadence tower #30/#32/#34/#36/#38/#41/#43/#45/#47/#49/#51/#53/#55/#57/#59 -> **#61**
  (regex-family consolidation, `supersedes #29-#60`); #62->#63 (keyword word-boundary); #64->#65 (agency
  "tek systems"->"teksystems"); #66->#67 (scan-prompt drift). **Zero orphan issues, zero uncovered bug class.**
- **#67 is a COMPLETE fix, not an incomplete one** (the same-class-sibling trap): its diff restores ALL
  three signals missing from `scan.md`'s title table (`trainer` **and** `community` **and** `developer`,
  exact match to `config.py` TITLE_SIGNALS) AND adds "use the code, code wins" defer blocks to both the
  blocklist and the scoring table -- the correct prompt-defers-to-code pattern, so future drift is inert.
- **`dd.md`** (the other command prompt) is a generic Describe/Discern loop -- no code-mirroring, no drift risk.
- **`reporter.py`** is clean and well-tested (cover-letter-count guard + missing-field alert both covered).
- **#61 confirmed to omit closing keywords** (0 `closingIssuesReferences`, no `clos/fix/resolv #N` in body)
  -> the merge-fleet.sh hand-close loop for its 15 superseded issues is genuinely required and correct;
  the small siblings #27/#63/#65/#67 all DO carry proper `closes #NN`.
- **Stall confirmed by merge history:** last JobScout merge is #24 @ 2026-09-11T19:51:45Z (unchanged) -> 15 days.
Deliberately did **not** manufacture a PR -- the queue is fully covered and owner-blocked; a new PR would be
tower-noise into a queue no one is merging. Doc only, nothing executed. -- codex R385
