# Fleet Merge Runbook — 2026-09-24 (codex R376)

**Supersedes:** MERGE-RUNBOOK-2026-09-15.md (9 days stale; predates JobScout #62-#67, Community #39/#40, content #8/#9).

**Situation (live-verified 2026-09-24):** 0 merges across all 4 agent repos since ~Sep 11-12.
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

---

## Net effect
- **JobScout:** 6 merges + hand-close 15 cadence issues (#61 has no closing keyword) -> all 19 open issues resolved.
- **Community:** 2 merges + 12 PR-closes + hand-close 12 issues (#38 has no closing keyword) -> all 13 open issues resolved (10 no-op traps sidestepped).
- **EFA:** 5 merges -> #28 + GA4/CSV fixes; #30/#24 remain owner-only.
- **Content:** 4 merges + 1 close -> all 3 open issues resolved.

After this sweep the only remaining items are the 3 genuinely owner-scoped ones
(EFA #30 schema-persistence, EFA #24 branch retirement). Nothing left to build.

*Prepared by codex R376. Doc only — no code changed, no merges executed (reserved for owner per governance).*
