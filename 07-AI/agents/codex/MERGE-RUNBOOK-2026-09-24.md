# Fleet Merge Runbook — 2026-09-24 (codex R376, amended R377, extended R378, re-verified R379, auto-close-audited R380, Section-6 draft-state corrected R382 2026-09-25, JobScout #69 added R390 2026-09-27, agent-II section 5b added R392 2026-09-27)

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
**7** open PRs (R390 added #69), all on default, all MERGEABLE. #61 is the scorer keystone (closes cadence issue
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
gh pr merge 69 --repo $R --merge   # /scan issues one query per config.SEARCH_KEYWORDS (closes #68)  [R390; scan.md hunks disjoint from #67 — test-merged both orders, 16/16 test files exit 0]
# #61 carries no "Closes #NN" refs, so hand-close the 15 cadence/salary issues it supersedes:
for n in 30 32 34 36 38 41 43 45 47 49 51 53 55 57 59; do \
  gh issue close $n --repo $R --comment "Fixed by #61 (anchored salary/cadence regex families; superset-proven in a fresh Python 3.14 clone). #61 lacked a closing keyword, closing manually."; done
```
scorer.py is fully farmed — do NOT open more per-token cadence PRs.

## 2. Community Intake — `morrisstephon51/-Community_intake_Routing` (default `claude/quirky-galileo-UGnfz`)
Collapses 14 open PRs -> 2 merges. #38 keystone is a proven behavioral superset of the entire
> **R386 precision note:** the "superset" proof is 11/12, not 12/12 -- and the 12th is a keystone WIN.
> Running sibling **#23**'s own suite against #38 reports **50/52**. Do NOT read that as a keystone
> regression: the failing line is the already-merged `#3` assertion (`'I want to teach and mentor
> students'` -> volunteer) that **#23 inverted in place** to `learner` because its token-deletion fix
> couldn't satisfy it. #38 keeps `#3` AND fixes #22 via seek-vs-offer direction logic. #25/#27/#29/#31/
> #33/#37 are stacked on #23 and inherit the inverted line. Merging #23 would silently route genuine
> volunteers ("I want to mentor first-gen students") to the learner default. **Close #23, never merge it.**
> Evidence posted as comments on PR #38 and PR #23 (2026-09-26).
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
# --- #9 CONFLICTS HERE. Resolve first (R388, verified by test-merge). ---
git clone --branch fix/test-runner-glob-union https://github.com/$R.git /tmp/glob && cd /tmp/glob
git merge origin/claude/eloquent-edison-aF7yG     # conflicts on package.json "test"
#   keep OURS: "test": "ts-node scripts/run-tests.ts"
git add package.json && git commit && git push
gh pr merge 9 --repo $R --merge          # glob test runner scripts/run-tests.ts (auto-discovers all *.test.ts)
gh pr close 8 --repo $R --comment "Superseded by #9: the glob runner auto-discovers platform-validation.test.ts (added by #6). #8 only hand-wired package.json, now redundant."
gh pr merge 10 --repo $R --merge         # pipeline-wiring.test.ts — MERGE LAST, asserts #2+#4+#6 are all wired
```

### R388 — the section did not merge as written, and the failure was silent

`#2 -> #4 -> #6` merge clean; **`#9` then hits `CONFLICT (content): package.json`.**
Default has no `"test"` key and #2/#4/#8/#9 each ADD it with a DIVERGENT value, so the
**set** conflicts even though every PR reads MERGEABLE against its own base. (#4 absorbs
#2's line cleanly only because it is stacked on #2's branch.) Contrast EFA #25/#27, which
add *byte-identical* lines and merge silently — same class, opposite outcome.

**The cascade was the real hazard.** `merge_ready` would have skipped a conflicting #9,
but the next line closed #8 unconditionally: #9 skipped -> package.json keeps #4's
enumerated line -> #8 closed as "superseded" -> `platform-validation.test.ts` lands on
default **with no runner at all**, suite still green on the two files it knows about. The
exact bug class the section exists to fix, caused by the runbook.

`merge-fleet.sh` now (a) auto-resolves via `resolve_test_line_conflict` (aborts unless
`package.json` is the only conflict; asserts the resolved value is the glob line) and
(b) gates #8's closure on #9 reaching `MERGED`, else `[HOLD]`.

> Resolver gotcha: merging the base **into** the PR branch inverts which side is "ours"
> versus the obvious local test. The first cut kept the enumerated line. Only the
> post-resolve assertion caught it — keep that assert.

VERIFIED after resolution: `npm install && npm test` -> **4/4 files, 30/30 assertions.**
The glob DOES discover `platform-validation.test.ts`, so #8 is genuinely redundant.

### R388 — NEW PR #10: the guards are real, but none of them checks the wiring

Mutation-tested all three guards per the R387 rule. All pass: each goes red when its bug
is re-injected AND red against the default branch. **No tautology here** — every suite
imports the real module under fix.

But all three test the exported helper *in isolation*. Replacing the three call sites with
arity/type-identical no-ops — helpers left defined, exported, byte-identical — gives a
clean `tsc --noEmit` and:

| suite | wired | **call sites unhooked** |
|---|---|---|
| caption-limit | 7/7 OK | 7/7 OK **blind** |
| hashtag-filter | 9/9 OK | 9/9 OK **blind** |
| platform-validation | 8/8 OK | 8/8 OK **blind** |
| **pipeline-wiring (#10)** | 6/6 OK | **6/6 FAIL — catches it** |

Every symptom returns (over-limit captions persisted, `#fyp` in `text_outputs`,
`durationInFrames` dropped) and the suite reports green. Not hypothetical: **issue #3 was
itself a wiring bug** — `topicWords` was computed in `generateContent` and never used.

PR #10 drives the real entrypoints through injected fakes (stub Anthropic client;
monkeypatched `createClient`) and asserts on output. No `package.json` change -> no
add/add conflict; #9's glob auto-wires it. **Merge LAST.**

**Generalized rule (extends R387):** mutation-testing the HELPER is necessary but not
sufficient. Also unhook the CALL SITE — if the suite stays green, the fix is only as
durable as the next refactor.

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

## 5b. Grant Agent — `morrisstephon51/agent-II` (default `claude/nifty-bohr-AhrsA`) (R391/R392 add)
The **6th** agent repo. It was missed for 390 runs because it showed `PRs=0, ISSUES=0` and that read as
"clean" — it actually meant "never audited". Same fleet architecture as the others
(config/scraper/scorer/report/alerts/models + a `main.py` CLI with a `--cron` installer), no tests and
no CI until these PRs. Both PRs are based on the **default** branch and both carry a body closing
keyword (`closingIssuesReferences` verified `[2]` and `[4]`) -> they auto-close on merge;
**no hand-close loop needed.**

```
R=morrisstephon51/agent-II
gh pr merge 3 --repo $R --merge   # HTML scraper: 403/404 error page is not content (auto-closes #2)
gh pr merge 5 --repo $R --merge   # scorer: validate Claude's response shape (auto-closes #4)
```
- **#3 (R391)** — `_html_scrape` returned `r.text` without checking `r.status_code`. Servers answer
  403/404 with a *full HTML error page*, so the caller's `if not html:` guard could never fire on an
  HTTP error. Measured live: `fallback_url` fired for **0 of 4** HTML targets (inert config), and every
  dead source **fabricated a grant out of the error page's own text** — observed
  `"Error 404 — Woods Fund Chicago … Page not found"` — which then reached the *billed* Claude scorer,
  the report table with a dead link, and potentially a deadline-alert email. Also a **discovery win**:
  once the guard made `fallback_url` reachable, Woods Fund Chicago `/grantmaking/` returned real content.
- **#5 (R392)** — `score_grants` wraps the API call in `try/except` with a `_placeholder_scores`
  fallback, but consumed the parsed JSON *outside* that block. Measured against the real scorer:
  a wrapped array, a missing `"index"`, and a non-numeric `fit_score` each **crash the run after the
  API is billed and before the report is written** (so a cron run produces no report and no alert,
  with only a traceback in `grant_agent.log`); `"index": "0"` instead of `0` produces **no error at all**
  and silently discards every score, rendering a complete-looking report where all grants are 5/10.
- Order is preference, not a dependency: disjoint files (`scraper.py` vs `scorer.py`), and the shared
  test scaffolding is **byte-identical** in both PRs so it add/add-merges cleanly. Test-merged in both
  orders — no conflict, scorer suite green in the merged tree either way.
- **NOT fixed, stated as a known limitation in #2:** `google.org` and the `grants.gov` URL return
  HTTP 200 but are a philanthropy landing page and a JS-rendered search shell. A status check cannot
  detect those and content validation would risk dropping genuine grants — owner call on the targets.

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
- **JobScout:** **7** merges + hand-close 15 cadence issues (#61 has no closing keyword) -> all **20** open issues resolved. (R390: #69 added, auto-closes #68 via a body keyword — no extra hand-close.)
- **Community:** 2 merges + 12 PR-closes + hand-close 12 issues (#38 has no closing keyword) -> all 13 open issues resolved (10 no-op traps sidestepped).
- **EFA:** 5 merges -> #28 + GA4/CSV fixes; #30/#24 remain owner-only.
- **Content:** 4 merges + 1 close -> all 3 open issues resolved.
- **AI Video Reel Gen (R377 add):** 2 merges -> auto-closes #26/#28/#30 (proper closing keywords, no hand-close); #5 (Supabase provisioning) remains owner-only.
- **Grant Agent / agent-II (R391/R392 add):** 2 merges -> auto-closes #2 and #4 (proper closing keywords, no hand-close). Takes `merge-fleet.sh` from 24 to **26** merges; the issue-close counter stays at **27** because neither PR needs a hand-close.
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

### R386 keystone superset PROVEN BY EXECUTION of the tower's own tests (2026-09-26)
R385 upgraded JobScout from count-parity to code-inspection parity. This run did the same for the
**largest un-inspected queue (Community Intake, 13i/14pr)** -- and went one step further than inspection:
checked out **all 12 superseded sibling branches' own test files** and *ran* them against keystone #38's
`intake.js` + `api/intake.js` in a fresh clone. This matters because Section 2 **closes** 12 PRs, which is
lossy if #38 is not really a superset.
- **Result: #15 48/48, #17 56/56, #19 62/62, #21 70/70, #35 78/78 -- clean passes.** #25/#27/#29/#31/#33/#37
  pass everything except one inherited case. **#23: 50/52.**
- **The single divergence is #38 being correct.** #23 could not satisfy the merged `#3` assertion
  (`test/classify.test.mjs:28-29` on default: `'I want to teach and mentor students'` -> `volunteer`), so it
  **flipped that line to `learner`** and relabeled it an intentional `#22` false-negative. Measured:
  | input (intent) | default (live) | PR #23 | keystone #38 |
  |---|---|---|---|
  | `I want to teach and mentor students` (offer) | volunteer OK | **learner WRONG** | volunteer OK |
  | `I want to mentor first-gen students on AI tools` (offer) | volunteer OK | **learner WRONG** | volunteer OK |
  | `I need a mentor to help me learn AI` (seek) | volunteer WRONG (#22) | learner OK | learner OK |
  | `Teach me how to use AI for my church` (seek) | volunteer WRONG (#22) | learner OK | learner OK |
- **So the tower is worse than useless, it is harmful:** merging #23 (or the six stacked on it) drops genuine
  volunteers who offer to teach/mentor -- the exact population The Plug AI wants in the volunteer inbox.
  Section 2's "close 12, merge #38" plan is **confirmed correct and now execution-proven.**
- **#38's own suite: 94/94 unit + 3/3 smoke.** CLI `intake.js` and serverless `api/intake.js` agreed on every
  probe -> **no twin drift** (the duplicated-logic hazard) in the keystone.
- **Hand-close set audited fleetwide.** Wrote a closing-keyword coverage audit over every open issue x every
  open PR **body** (titles do NOT auto-close): JobScout 4 auto / 15 keyword-less; Community 4 auto / 9
  keyword-less; EFA 1 auto; avrg 3 auto; content 3 auto / 0 keyword-less. `merge-fleet.sh`'s Community loop
  correctly closes **14 16 18** 20..36 -- `#14/#16/#18` DO have body keywords but in PRs **#15/#17/#19 that get
  CLOSED, not merged**, so their keywords never fire and the hand-close is required. Verified present.
- **avrg "#27+#31 auto-close" claim re-verified true:** #27's body carries `Fixes #26` *and* an appended
  `Also closes #28`, and its diff really does drop the `ADMIN_SECRET` guard from `persona` DELETE -- so #28 is a
  covered duplicate, not an orphan. Only avrg #5 (owner Supabase setup) stays open. No new PR warranted.
- Fleet sweep re-run across all 23 non-archived repos: **ZERO drift vs R385** (JobScout 19i/6pr, Community
  13i/14pr, EFA 3i/5pr, avrg 4i/2pr, content 3i/5pr; psychic 0i/2pr, Link-inbio 0i/3pr, kai-vault 0i/2pr,
  forming-paws 1i/0pr). Owner-merge remains the sole bottleneck. -- codex R386

---

## R387 addendum (2026-09-26) — EFA queue execution-verified; a NEW failure class: the tautological guard

R386 execution-proved the Community Intake keystone. R387 did the same for the **last large
un-executed queue, Enrollment_Funnel_Agent** (3 issues / 5 PRs), in a fresh clone with a real
`npm install`.

**Merge safety — clean.**
- Order `#25 → #26 → #27 → #29 → #31` **and the exact reverse**: every merge clean, no conflicts.
- `git diff` between the two resulting trees is **empty** — order does not matter.
- `#25` and `#27` both add the *identical* `test/*.test.ts` glob line to `package.json`; git
  resolves identical additions without an add/add conflict. This is the **fixed** form of the
  testless-repo conflict class — contrast `agent_I_content`, where siblings hand-wired
  divergent `test` lines.
- Full suite on the merged tree: **6/6 files, exit 0** — `baseline-visibility` ✓,
  `detect-platform` 13/13, `engagement-parity` ✓, `engagement-weight-drift` ✓,
  `enrollment-csv` 6/6, `sessions` 10/10.

**NEW FAILURE CLASS — a guard that is wired, runs, is green, and can never fail.**

Prior classes were *test added but not wired to the runner* (invisible) and *open-PR tests
codify a gap* (contested). This one is worse because it is invisible in the opposite
direction: it reports success.

`test/engagement-parity.test.ts`, shipped by **PR #29** as the regression guard for issue #28:

```ts
const baselineTotal    = week.reduce((s, p) => s + computeEngagementScore(p), 0)
const currentWeekTotal = week.reduce((s, p) => s + computeEngagementScore(p), 0)
assert.equal(baselineTotal, currentWeekTotal, 'baseline and current-week must share one formula')
```

Both sides call `computeEngagementScore` — it is `x === x`. The file **never imports
`supabase.ts`**, the module that actually held the duplicated weights. Measured:

| tree | `engagement-parity` | `engagement-weight-drift` (#32) |
|---|---|---|
| default branch, pre-fix (`supabase.ts:174` duplicates the weights) | **PASSES** | FAILS — names both sites |
| #29 head (fixed) | passes | passes |
| #29 head + drift re-injected (`1/99/99/99` in `fetchRollingEngagement`) | **PASSES** | FAILS |

**The #29 code fix is correct and still merges.** Only its guard is unenforceable.

**Detection method — mutation testing, and it must be the default from here.**
Counting passing assertions cannot distinguish a real guard from a tautology. Two cheap checks:
1. **Run the PR's test file against the DEFAULT branch.** A regression guard for a bug that
   still exists there MUST fail. If it passes, it is a no-op. (Watch for a false negative:
   copying `node_modules` between trees broke `tsx` and made all five files "fail" for the
   wrong reason — always re-`npm install` in the baseline tree and sanity-check the runner.)
2. **Re-inject the bug into the fixed tree** and confirm the guard goes red.

**Shipped:** PR **#32** (`test/engagement-weight-drift.test.ts`), based on
`fix/unify-engagement-weights` so it hardens #29 in place. Because #28 is a *duplication* bug,
the guard asserts the structural invariant — the weight arithmetic must exist at exactly one
site, that site must be `scorer.ts`, and `supabase.ts` + `agent.ts` must both route through
`computeEngagementScore`. No `package.json` change, so no add/add conflict; the glob runner
picks it up. Plus an evidence comment on #29.

**Merge-order consequence — `merge-fleet.sh` updated:** `#32` now merges immediately **before**
`#29` (it merges *into* #29's branch). Dry-run is now **22 merges** / 14 PR-closes / 1 retarget
/ 27 issue-closes / 4 draft-skips.

**Also flagged:** `#26`, `#29` and `#31` add test files but **no runner wiring** — `#25` or
`#27` must land or no EFA test executes at all.


---

## R389 addendum (2026-09-27) — the unconditional-follow-up audit R388 asked for

R388 patched ONE gate by hand (`agent_I_content` #8, held unless #9 reaches MERGED) and left a
carryover: *"Audit the script for other unconditional close_pr calls that assume a prior merge
landed."* Done. **The same bug class was present at 39x the scale**, on the two biggest keystones.

### What was wrong

`merge_ready` downgrades an unmergeable PR to a `[skip]` and keeps going. Three follow-up blocks
then executed **unconditionally**, each asserting in its GitHub comment that a keystone had landed:

| Block | Actions | Comment it posts | Gated before R389? |
|---|---|---|---|
| JobScout hand-closes | 15 issues (#30–#59) | "Fixed by #61" | **no** |
| Community sibling closes | 12 PRs (#15–#37) | "Superseded by #38" | **no** |
| Community hand-closes | 12 issues (#14–#36) | "Fixed by #38" | **no** |

The Community pair is the worst of the three: those 12 PRs are the *only other* fixes for those 12
issues, so closing them as superseded while #38 is absent **erases the entire fix surface for that
repo** and leaves 12 issues marked fixed. And it is silent — the summary still prints
`Issues closed: 27`.

### Proven, not asserted

Built a stateful fake-`gh` harness (`/tmp/ghsim`) that reproduces the live dry run exactly
(23/14/1/27/4), then forced each keystone UNMERGEABLE and diffed the unpatched vs patched script:

| Scenario | UNPATCHED (merges/prClose/issClose) | PATCHED |
|---|---|---|
| A — all keystones merge | 23 / 14 / 27 | **23 / 14 / 27** (identical: no-op on the happy path) |
| B — #61 + #38 unmergeable | 21 / **14 / 27** ← fired anyway | 21 / **2 / 0** + 2 `[HOLD]` |
| C — #9 unresolvable | 22 / 13 / 27, 1 hold | 22 / 13 / 27, 1 hold (R388 gate preserved) |
| D — #32 unmergeable | 22 / 14 / 27 | 22 / 14 / 27 + `[WARN]` (does not block a real fix) |

Also verified **idempotent**: a second `--execute` pass issues 0 mutating actions and does not
spuriously HOLD. Behaviour changes in scenario B only.

### The fix

- **`require_merged <repo> <pr> <what>`** — shared gate. In `--execute` it demands `state == MERGED`.
  In dry-run there is no merge to observe, so it **predicts from live mergeability** rather than
  assuming success; otherwise the dry run would promise 27 issue-closes that `--execute` would
  correctly refuse. Now wraps all three blocks above *and* R388's #8 case (one helper, four sites).
- **`warn_unless_merged`** — for a dependency where holding would be worse than proceeding. EFA #29
  carries the real code fix for #28 and auto-closes it, so blocking #29 because its guard #32
  skipped would withhold a correct fix. Warns loudly instead, telling the owner #28 will close with
  only the tautological `engagement-parity.test.ts` behind it.
- **`retarget`** now checks state first (no longer fires or counts against a non-OPEN PR).

### Net effect on the owner's plan: UNCHANGED — still 23 merges / 14 PR-closes / 1 retarget /
### 27 issue-closes / 4 draft-skips. The gates only engage when something has already gone wrong.

### Two surface facts confirmed this run

- **A closing keyword in the TITLE does not auto-close.** `agent_I_content` #8 is titled
  "…(closes #7)" but its `closingIssuesReferences` is **empty**; #9 carries the real `closes=[7]`.
  Harmless here because the plan merges #9 and closes #8 — but the inverse ordering would have
  orphaned issue #7. Verify closing refs via the API field, never by reading a title.
- **Every open issue fleetwide still has a covering MERGEABLE PR or is owner-only** (JobScout #26←#27
  and content #7←#9 were the two that looked unaccounted for; both are covered). Zero new fix PRs
  warranted. Live sweep: 41 open PRs across the 9 active repos, 0 unmergeable, 5 drafts — of which
  only 4 are draft-*skips*, because Link-inbio #6 is a draft being **closed** as stale, not merged.
  **SUPERSEDED R390:** "zero new fix PRs warranted" was true only of *filed issues*. It did not
  survive an audit of the still-unhardened **sites** inside an already-fixed file — see the R390
  addendum. 42 open PRs / 20 JobScout issues now.


---

## R390 addendum (2026-09-27) — "issue-covered" is not "class-covered"

R389 closed with *"every open issue fleetwide has a covering MERGEABLE PR → zero new fix PRs
warranted."* That was a correct statement about the **issue list** and a wrong one about the
**code**. Applying R389's own rule (*audit the bug class, not the site where you found it*) to a
file a merged-and-pending PR had already "fixed" produced a new, real bug.

### The finding — JobScout issue #68 / PR #69

`config.SEARCH_KEYWORDS` has two consumers, and only one of them reads it:

| consumer | reads the tuple? | what it does |
|---|---|---|
| `scorer._keyword_score()` | yes (unit-tested) | credits all 8 terms on the 30%-weighted keyword dimension |
| `.claude/commands/scan.md` | **no — hardcoded its own lists** | the **only** thing that actually issues searches |

There is no Python search driver in the repo (`config.py`, `scorer.py`, `reporter.py` only);
discovery happens entirely through the ZipRecruiter/Indeed MCP calls the `/scan` prompt makes.
So **a keyword added to `config.py` began contributing to a job's *score* while never causing that
job to be *found*** — and `CLAUDE.md` advertises `SEARCH_KEYWORDS` as the knob for "job keywords to
search," making the documented knob inert on the documented run path.

Measured on the default branch: Step 1 listed 6 queries, Step 2 listed 3 mashed combinations.

| configured keyword | issued verbatim by the prompt? |
|---|---|
| `EdTech coordinator` | **no — absent from the prompt entirely** |
| `learning experience designer` | **no — absent from the prompt entirely** |
| `training specialist` | no — sent as `"training specialist EdTech"` (AND-narrowed) |
| `digital learning` | no — sent as `"digital learning coordinator"` (AND-narrowed) |
| other 4 | yes |

**4 of 8.** "Learning Experience Designer" is a standard industry title — a whole role family was
invisible to the scanner. Step 2's `search: "AI educator instructional designer"` ANDs two terms
and loses every posting matching only one.

### Why #67 did not already cover it

#66/#67 are the same *class* ("the `/scan` prompt re-implements pipeline logic and has drifted").
#67 reconciled the two **scoring** surfaces — the Step 3 filter summary and the Step 4 criteria
table, where it correctly restored *all* of `trainer`/`community`/`developer` — and added
"the code wins" notes to both. It never touched the Step 1 / Step 2 **query** surface.

That was the worse of the two sites: **a scoring drift mis-ranks a posting that was fetched; a
query drift means the posting is never fetched, and no correct scoring downstream can recover it.**

### Verification — mutation-tested, not asserted

`tests/test_scan_prompt_keyword_parity.py` parses `scan.md` and asserts the structural invariant,
not the one instance (every configured keyword is a standalone Step 1 query; no Step 1 query is an
unconfigured mutation; no query line concatenates two keywords; Step 2 names the config tuple).

| scenario | result |
|---|---|
| default-branch `scan.md` + the new guard | **0/5 pass** — all five assertions red |
| PR #69 branch | 5/5 pass |
| add a keyword to `config.py` only (the real drift direction) | **2 assertions red** |
| delete one keyword from `scan.md` only | **2 assertions red** |
| full existing suite on #69 (11 files) | all green |

Guard fails on shipped code and catches a future edit to **either** side — not tautological in
either direction. No CI in this repo; pytest auto-discovers `tests/`, and the file also runs
standalone (`python tests/test_scan_prompt_keyword_parity.py`), so there is no runner to wire.

### Merge safety — test-merged live, both orders

`scan.md` is edited by both #67 (Steps 3–4) and #69 (Steps 1–2). Against `origin` heads of all six
other open JobScout PRs (#25, #27, #61, #63, #65, #67):

- siblings → #69: 7/7 merges clean, `scan.md` **auto-merged**, **16/16 test files exit 0**
- #69 → siblings: 7/7 merges clean, `scan.md` **auto-merged**, **16/16 test files exit 0**
- #67 + #69 alone: merged `scan.md` keeps **both** fixes — #67's completed title row and both
  "code wins" notes, plus all 8 standalone queries and no leftover mutation

**#69 is order-independent — no ordering change to this runbook or `merge-fleet.sh`.**

### Known residual, deliberately NOT shipped

`scan.md:49` still lists the agency token `tek systems` (spaced). **#65 corrects `config.py` to the
real one-word brand `teksystems`, so once #65 lands the prompt's inline copy is stale again.**
#67's "the code wins" note above that line mitigates it in prose, but the wrong literal is still
shown to the model. The fix sits *inside #67's hunk*, so shipping it would have manufactured a
conflict with a pending PR. **Post-merge apply-me** (one line, after #65 and #67 are both in):

```
# in .claude/commands/scan.md Step 3, change the blocklist token:  tek systems -> teksystems
# then extend tests/test_scan_prompt_keyword_parity.py's _LISTS to cover
# AGENCY_BLOCKLIST and TITLE_SIGNALS too (both are order-dependent until #65/#67 land)
```

### Rules this run adds

1. **"Every issue has a covering PR" is not "every bug is fixed."** The issue list only contains
   bugs someone already noticed. A file that a pending PR has "fixed" can still hold un-hardened
   sites of the very class that PR was opened for — audit the *file*, not the issue.
2. **When a PR hardens N of M copies of a duplicated list, enumerate M.** #67 did the two scoring
   copies perfectly and the query copy not at all. Count the copies before calling the class closed.
3. **Prefer the un-hardened site that kills discovery over the one that kills ranking.** Ranking
   errors are recoverable downstream; a query never sent has no downstream.
4. **Scope a new drift guard to the lists no pending PR is touching.** Asserting `TITLE_SIGNALS`
   parity today would have made #69's result depend on whether #67 merged first. Order-dependent
   guards turn a green suite red on the default branch for reasons unrelated to the change.
5. **`zsh` does not word-split unquoted `$VAR`.** A `for b in $SIBS` test-merge loop silently
   merged *nothing* (one branch named by all six concatenated) and still printed "ALL GREEN" —
   a false all-clear from the harness, not the code. Same family as R383's capital-`True` guard:
   verify a merge loop by **exit code and merge count**, and write multi-item loops in `bash`
   with a real array.
6. **`git checkout <path>` mid-mutation-test destroys the fix you are testing.** Restoring one
   mutated file also reverted the uncommitted change under test, and the next full-suite run
   reported the new guard 0/5 — looking like a broken guard rather than a lost edit. **Commit
   before mutation-testing**, then restore with `git checkout` freely.

### Net effect on the owner's plan: **24 merges** (was 23) / 14 PR-closes / 1 retarget /
### 27 issue-closes / 4 draft-skips — dry-run verified after the edit (`bash -n` clean).
Only JobScout's merge count changes (6 → 7). Issue-closes stay 27 because #69 auto-closes #68 via
a body keyword. Nothing else in this runbook moves.

*R390 by codex, 2026-09-27. One new issue (#68) + one new PR (#69), both live. No merges executed.*
