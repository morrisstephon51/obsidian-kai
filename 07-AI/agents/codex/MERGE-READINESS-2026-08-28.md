# Merge-Readiness Audit — codex Run 239 (2026-08-28)

**Purpose:** the account-wide open-PR frontier is 100% founder-authority-blocked (18 open PRs, 0 code-actionable open issues). Rather than add a 19th speculative PR to the pile, this run *empirically de-risks the merge queue itself* so Stef can clear it fast and safely. All results below come from real local merges (`git clone` + `git fetch pull/N/head` + `git merge`), not GitHub's per-PR `mergeable` flag — which only checks each PR against the base **in isolation** and does not know how PRs interact once earlier ones land.

Method: clone each repo, fetch all open PR heads, replay the merges in the intended order onto a scratch branch, record conflicts, then build the fully-merged tree and run the test suite on it.

---

## 1. job_opportunity_scanner — 10-PR scorer/reporter stack ✅ VERIFIED GREEN

Independent re-confirmation of codex Run 236 (queue still cites the older 9-file figure).

- **Base:** `claude/clever-cannon-IDh3G` (repo default). All 10 PRs (#7–#16) branch from the same base commit `df09de9`.
- **File clustering:** `scorer.py` × 6 (#7,#8,#9,#11,#12,#13) · `reporter.py` × 3 (#14,#15,#16) · `config.py` × 1 (#10). Each PR adds a uniquely-named `tests/test_*.py` (no test-file collisions).
- **Sequential merge sim (numeric order 7→16):** **10/10 CLEAN, 0 conflicts.** The `is_recent`-recency worry (#11/#12/#13 edit the same function) is a non-issue — the hunks are line-disjoint and 3-way-merge cleanly in any order.
- **Correctness on the combined tree:** built the full 10-PR merge, created a venv, installed pytest 9.1.1, ran the suite → **58 tests pass in 0.06s** (9 test files, 58 test functions). Clean-merge *and* semantically correct together — not just pairwise-mergeable.

**Verdict:** Stef can batch-merge #7–#16 → `clever-cannon` → `main` in any order, **no rebases, zero conflicts, suite green.** ~41 days cold, zero landed.

---

## 2. psychic-bassoon — 5 open PRs ⚠️ NEW HAZARD FOUND (not in the founder queue)

The canonical FOUNDER-ACTION-QUEUE.md lists #1 as `MERGEABLE/CLEAN` with only an `.env.example` add/add hazard vs draft #11. That is true **against base** — but a real edit/delete collision appears once #22 lands.

- **Base:** `main` (`a515639`).
- **File overlaps:** `lib/utils.ts` → **#22 and #1** · `.env.example` → #1 and #11(draft) · `next.config.js` → #19 only · `package.json`/lock → #20 only.
- **Sequential merge sim in fleet-priority order 20→19→22→1→11:**
  - #20 (CVE bump) ✅ CLEAN
  - #19 (security headers) ✅ CLEAN
  - #22 (date-only local-time fix, closes #21) ✅ CLEAN
  - **#1 (content/forms) ❌ CONFLICT on `lib/utils.ts`**
  - #11 (grants, draft) ✅ CLEAN

### Root cause of the #1 ↔ #22 conflict
- **#22** rewrites `formatShortDate` to route through a new `toLocalDate()` helper (the actual issue-#21 off-by-one fix) **and** applies the same fix to `formatDate`.
- **#1** *deletes* `formatShortDate` entirely (as dead code) and leaves `formatDate` untouched.
- Result: an **edit/delete collision on `formatShortDate`** — git cannot auto-resolve this, so #1 stops being one-click mergeable the moment #22 is in.

### Why it's SAFE to resolve (verified)
- `formatShortDate` has **zero callers** — on `main` the only reference is its own definition; in #1's tree there are no references at all (`grep` across `*.ts`/`*.tsx`). It is genuinely dead code.
- **Resolution: keep #1's deletion.** No build break (nothing calls it). The substantive part of the #21 fix lives on `formatDate` (real callers), which #1 never touches, so **#22's correctness fix survives regardless.** Only the moot fix-to-dead-code is dropped.

**Verdict / recommended order:**
1. **#20** (published-CVE Next.js 14.2.5→14.2.35) — highest-value single click on the whole queue.
2. **#22** (closes issue #21) — clean on base.
3. **#19** (security headers) — disjoint.
   *(the trio is clean in any order among themselves.)*
4. **#1** last, and it now requires **one manual edit/delete resolution** on `lib/utils.ts`: keep the `formatShortDate` deletion; keep #22's `toLocalDate`/`formatDate` changes. Then also concatenate the non-overlapping `.env.example` blocks vs draft #11. #1's forms still need the Formspree env on Vercel before they submit.

*(Alternative: merge #1 before #22 — then #22 conflicts instead. #22 is small/tested/higher-priority and #1 is a 34-file PR, so landing #22 first and resolving the one hunk inside #1 is the lower-risk path.)*

---

## Bottom line
- **jobscout batch:** provably safe, one action, no thought required.
- **psychic-bassoon:** the trio (#20→#22→#19) is one-click; **#1 is NOT the clean click the queue implies** — budget one manual (safe) conflict resolution for it. Warning comment left on PR #1.
- Everything remains founder-authority-blocked; no code blockers were introduced or remain. avrg #25 and the Week-1 gate unchanged.

_Evidence: real `git merge` replays in `/tmp/jos-merge-audit` and `/tmp/pb-merge-audit`; pytest 9.1.1 run on the 10-PR merged tree. codex Run 239._
