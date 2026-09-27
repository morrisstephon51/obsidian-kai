# R376 cascade cert harness — ungated keystone supersession-closes

Certifies `codex/merge-fleet.sh` against the rule codex itself stated in R388:
**"gate every 'X supersedes Y' step on X actually reaching MERGED."**

codex applied that rule to ONE site (`#9` -> `#8`, content section, script lines 242-247).
The two KEYSTONE sections had no such gate, where the blast radius is 39 closes, not 1.

## Reproduce (touches NOTHING on GitHub — `gh` is faked)

    mkdir -p /tmp/mfcert/bin && cp fake-gh /tmp/mfcert/bin/gh && chmod +x /tmp/mfcert/bin/gh
    cp ../../codex/merge-fleet.sh /tmp/mfcert/mf.sh && chmod +x /tmp/mfcert/mf.sh
    cd /tmp/mfcert
    : > actions.log; : > state.db
    FAKE_LOG=$PWD/actions.log FAKE_STATE=$PWD/state.db FAKE_CONFLICT_PR=38 \
      PATH=$PWD/bin:$PATH ./mf.sh --execute --only community
    grep -c '^CLOSE-PR ' actions.log      # UNPATCHED: 12  (should be 0 — #38 never merged)
    grep -c '^CLOSE-ISSUE ' actions.log   # UNPATCHED: 12  (should be 0)

The fake `gh` models the real state transition (a PR that merges reports `state=MERGED`
afterwards), which is what makes the happy-path control meaningful. Knobs:
`FAKE_CONFLICT_PR=<n>` makes #n report `mergeable=CONFLICTING`;
`FAKE_MERGE_FAIL=<n>` makes `gh pr merge #n` exit 1 (branch protection / required checks).

## Result matrix (`closePR` / `closeISSUE` / reported `merged`)

| section   | scenario              | unpatched      | with keystone-gate-R376.patch |
|-----------|-----------------------|----------------|-------------------------------|
| community | keystone merges       | 12 / 12 / 2    | 12 / 12 / 2   (identical)     |
| community | #38 CONFLICTING       | 12 / 12 / 1    | 0 / 0 / 1  [HOLD]             |
| community | `gh pr merge 38` -> 1 | 12 / 12 / **2**| 0 / 0 / 1  [HOLD]             |
| jobscout  | keystone merges       | 0 / 15 / 6     | 0 / 15 / 6    (identical)     |
| jobscout  | #61 CONFLICTING       | 0 / 15 / 5     | 0 / 0 / 5  [HOLD]             |
| jobscout  | `gh pr merge 61` -> 1 | 0 / 15 / **6** | 0 / 0 / 5  [HOLD]             |
| content   | codex's #9->#8 gate   | 1 / 0 / 5      | 1 / 0 / 5     (undisturbed)   |

Bold `merged` = the summary counts a FAILED merge as a success: `run()` propagates
`eval`'s status fine, but `merge_ready` line 75 increments `MERGED` on both branches of
`[ "$DRY" -eq 0 ] && MERGED=... || MERGED=...`, so nothing ever observes the failure.
The hard-fail path is worse than the skip path: skip prints a red `[skip]` and bumps
`Skipped`, while a failed merge prints a green `[run]` and reports "PRs merged: 2 / Skipped: 0".

Dry-run tuple is BYTE-IDENTICAL patched vs unpatched (gate passes through when `DRY=1`,
exactly as codex's `#8` gate does), so the certified 23/14/1/27/4 plan is unchanged.
