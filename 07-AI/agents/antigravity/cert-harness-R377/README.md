# R377 cert harness — counter integrity + the ungated RETARGET→MERGE prerequisite

Certifies `codex/merge-fleet.sh` (LIVE, md5 `f2ed3284639b7e6c341ab449f28e9700`, the R389
version) on a **fourth axis**: what the script *reports* vs what it *did*, and which
dependent steps still fire after a prerequisite command errors.

R389's `require_merged` closed the destructive axis (a keystone that does not land no
longer triggers its 39 supersession-closes). Two things it did not cover:

## Finding 1 — ALL FOUR action counters increment past a FAILED command

`run()` returns `eval`'s status in `--execute` mode, but every caller increments its
counter on the *next* statement, so nothing observes a failure:

| site | line | shape |
|------|------|-------|
| `merge_ready`  | 75  | `run "gh pr merge …"; [ $DRY -eq 0 ] && MERGED=… \|\| MERGED=…` |
| `close_pr`     | 86  | `run "gh pr close …"; CLOSED=$((CLOSED+1))` |
| `retarget`     | 95  | `run "gh pr edit …"; RETARGETED=$((RETARGETED+1))` |
| `close_issues` | 103 | `run "gh issue close …"; ISSUES_CLOSED=$((ISSUES_CLOSED+1))` |

My own R376b patch fixed **one of the four** (`merge_ready`) — an incomplete fix of its
own bug class. It is retired as `merged-counter-R376b.SUPERSEDED-BY-R377.patch`.

Why each one matters (they are NOT equally bad):

- `MERGED` overcount is the worst: "PRs merged: 6" alongside a `[HOLD]` is the number the
  owner reads to decide whether the fleet drained.
- `ISSUES_CLOSED` overcount defeats the *reason* the hand-closes exist. Keystones ship
  with `closingIssuesReferences=[]` (re-certified live this run: #61 and #38 both `[]`),
  so the hand-close is the ONLY thing that closes those 27 issues. A summary that says
  "Issues closed: 27" when N silently 502'd means nobody re-runs the section.
- `CLOSED` / `RETARGETED` overcounts fail in the *safe* direction (the PR stays open) but
  still report cleanup as complete.

## Finding 2 — a FAILED `gh pr edit --base` does not stop the dependent merge

```
retarget    agent_I_content 4 "claude/eloquent-edison-aF7yG"
merge_ready agent_I_content 4 "…"          # <- fires regardless
```

`retarget` always returned 0. Live-certified this run: **#4's base is
`fix/enforce-caption-char-limits`, which is #2's head branch.** So if the retarget errors
("Base branch was modified"), #4 merges into a NON-DEFAULT branch — a silent no-op vs
default — while #4 reads `MERGED` and drops out of the open-PR sweep.

**Corrected before publishing:** I first wrote that this also false-closes issue #3 via
#4's "(closes #3)" text. Live `gh` says `closingIssuesReferences=[]`, so issue #3
survives and the loss is recoverable. That is codex R389's own "keyword in the prose is
not the API field" fact, and it narrows this from *false all-clear* to *silent no-op plus
a lost PR record*. It is not a property to rely on.

This is the same rule as `require_merged`, applied to the **retarget→merge** dependency
instead of a merge→close one.

## Reproduce (touches NOTHING on GitHub — `gh` is faked, no network, no git remote)

    mkdir -p /tmp/mf377/bin && cp fake-gh /tmp/mf377/bin/gh && cp probe.sh /tmp/mf377/
    cp ../../codex/merge-fleet.sh /tmp/mf377/mf389.sh
    cp /tmp/mf377/mf389.sh /tmp/mf377/mf377fix.sh
    patch -p0 /tmp/mf377/mf377fix.sh < ../counter-and-retarget-R377.patch
    chmod +x /tmp/mf377/*.sh /tmp/mf377/bin/gh
    cd /tmp/mf377 && ./probe.sh /tmp/mf377/mf389.sh "unpatched" FAKE_CLOSE_ISSUE_FAIL=30

`probe.sh` runs `--execute` against the fake and prints **actual/reported** per counter,
flagging any mismatch `<-LIE`. `fake-gh` v2 adds a failure knob per mutating verb:
`FAKE_MERGE_FAIL`, `FAKE_CLOSE_PR_FAIL`, `FAKE_CLOSE_ISSUE_FAIL`, `FAKE_EDIT_FAIL`
(v1's `FAKE_CONFLICT_PR` kept, plus `FAKE_DRAFT_PR`).

## Result matrix — actual/reported per counter

| scenario | unpatched | patched |
|----------|-----------|---------|
| A control, all succeed          | 21/21 · 11/11 · 1/1 · 27/27 | identical |
| B `gh issue close` 502          | … · … · … · **25/27 LIE**   | 25/25 + 2×`[FAILED]` |
| C `gh pr close` 403             | **10/11 LIE** · …          | 10/10 + `[FAILED]` |
| D `gh pr edit --base` fails     | **0/1 LIE**, and **#4 merges anyway** | 0/0 + `[FAILED]` + `[HOLD]`, #4 NOT merged |
| E `gh pr merge #61` fails       | **20/21 LIE** (beside a `[HOLD]`) | 20/20 + `[FAILED]` |
| F #38 CONFLICTING               | (codex's gate) 1 closePR    | identical — `require_merged` undisturbed |

B shows 2 failures for one knob because issue #30 is in *both* keystone close-lists
(JobScout #30-#59 and Community #14-#36) and the fake keys on number, not repo.

## Regression guards (all green)

- **Happy path `--execute`: BYTE-IDENTICAL** stdout, and the action logs are identical —
  same real mutations in the same order. Not an over-conservative gate.
- **Dry run: BYTE-IDENTICAL.** Correct *here*, unlike R376: `run()` evals nothing in dry
  mode, so there is no failure to predict, and counting "what happens if each command
  succeeds" is the only honest prediction. Contrast `require_merged`, where the dry run
  CAN observe live mergeability and therefore MUST predict rather than assume.
- **Mutation-tested:** re-injecting the unconditional increment at the `close_issues`
  site alone makes scenario B go red again (25/27 `<-LIE`), so the harness genuinely
  detects this class rather than passing vacuously. (The crude mutant also fires `failed`
  unconditionally, which pollutes its message lines but not its counter columns.)
- `bash -n` clean; `patch --dry-run -p0` applies to the live script with zero fuzz.

## Limits of this harness — stated, not papered over

- The absolute tuple (21/11/1/27) is **harness-shaped**, not the live plan tuple
  (23/14/1/27/4): this fake reports every PR `OPEN`+`MERGEABLE` and seeds no real fleet
  state. Every claim above rests on the **actual-vs-reported delta inside a single run**,
  which is invariant to that. Do not quote these absolutes as the plan.
- It cannot test idempotency: the fake does not persist close-state, so a 2nd pass
  re-closes. codex R389 already certified idempotency with its own stateful fake.
- Operational caution learned the hard way this run: I ran `patch --dry-run` against
  codex's **live** file and its mtime moved (content byte-identical, md5 unchanged both
  before and after). Run `patch --dry-run` on a copy — a peer watching mtimes cannot tell
  your no-op read from their own write.
