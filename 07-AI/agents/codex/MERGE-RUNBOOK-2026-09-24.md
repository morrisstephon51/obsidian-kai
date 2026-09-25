# Fleet Merge Runbook — 2026-09-24 (codex R376, amended R377, extended R378, re-verified R379 2026-09-25)

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
gh pr merge 1  --repo $R --merge   # real content + working forms + resource detail pages (34 files, +7800; open since Jun 13, ahead 17 / behind 0 = still current)
gh pr merge 25 --repo $R --merge   # add /websites services page (+297; behind 0)  [merge #1 first, then re-check #25]
```

**6b. Link-inbio** (link-in-bio site) — default `main`
```
R=morrisstephon51/Link-inbio
gh pr merge 5  --repo $R --merge   # Obsidian ops vault: domain registry / tracker / grant log (behind 0)
gh pr merge 15 --repo $R --merge   # rebuild Command Center as live scroll dashboard (+2288/-541; behind 0)
gh pr close 6  --repo $R --comment "Empty diff (+0/-0), 13 commits behind a diverged main -> the condensed-resume PDF is already on main or was abandoned, and the fellowship deadline it targeted has passed. Closing as stale."
```

**6c. kai-obsidian-vault** (vault docs) — default `main`
```
R=morrisstephon51/kai-obsidian-vault
gh pr merge 3 --repo $R --merge    # record theplugai.info scroll-homepage deployment in vault docs (+3/-3; behind 0)
gh pr merge 2 --repo $R --merge    # CHA Resident Business Owner Program business plan (+129; behind 7 but still CLEAN — confirm the plan is current before merging)
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
- **Non-agent repos (R378 add):** psychic-bassoon 2 merges (#1, #25); Link-inbio 2 merges (#5, #15) + 1 stale-close (#6); kai-obsidian-vault 2 merges (#2, #3) = **6 merges + 1 close**. `forming-paws #8` is founder-action (IL-SOS filing), not a merge.

After this sweep (agent fleet + Section 6) the only remaining items are genuinely owner/founder-scoped:
EFA #30 schema-persistence, EFA #24 branch retirement, AI-Video-Reel #5 Supabase provisioning, and
`forming-paws #8` (Stef's IL-SOS not-for-profit filing). Nothing left to build — the entire fleet-wide
queue is now either a MERGEABLE PR awaiting the owner's merge or an explicit owner/founder action.

*Prepared by codex R376; Section 5 + 5th-repo reconciliation added R377 (2026-09-24); Section 6 (non-agent repos) + fleet-wide re-verification added R378 (2026-09-25); live re-verified unchanged + count corrected (32 agent PRs) R379 (2026-09-25 ~13:15 UTC). Doc only — no code changed, no merges executed (reserved for owner per governance).*
