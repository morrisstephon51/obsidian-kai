# R378 CERT — `closingIssuesReferences=[]` has TWO causes, and they need OPPOSITE remediations

**Certified live 2026-09-27 against all 42 open PRs in the six fix-queue repos.**

## The claim

GitHub populates a PR's `closingIssuesReferences` **only for PRs whose base is the
repository default branch.** A stacked PR can carry a perfectly valid closing keyword in
its body and still report `[]`. So an empty field means one of two completely different
things:

| cause | signature | remediation |
|---|---|---|
| **A. authoring omission** — no keyword anywhere | `base == default` AND body has no keyword | needs a **permanent hand-close** |
| **B. base artifact** — keyword present, base is another PR's head | `base != default` AND body HAS a keyword | **self-heals** the moment the PR is retargeted to default |

## Evidence — exhaustive cross-tab, zero exceptions

Of 42 open PRs, 16 declare a closing keyword in the **body**:

```
base==default:true  / API populated:true   => 12
base==default:false / API populated:false  => 4
```

The 4 in cause B: `agent_I_content#4` (`Fixes #3.`), `agent_I_content#8` (`Closes #7.`),
`-Community_intake_Routing#17` (`Closes #16.`), `-Community_intake_Routing#19` (`Closes #18.`)

**Formatting confound ruled out.** `agent_I_content#8` line 1 is `Closes #7.` — byte-for-byte
the same form and the same position as `agent_I_content#6`'s `Closes #5.` and
`-Community_intake_Routing#15`'s `Closes #14.`, both of which DO populate. And
`agent_I_content#9` populates with its keyword all the way down at body **line 62**, which
kills the "keyword must be near the top" alternative. The only variable that moves the
field is the base branch.

**Cause A confirmed separately.** Every `base==default` + `API=[]` PR checked
(`scanner#61`, `scanner#25`, `Community#38`, `agent_I#2`, `agent_I#10`, `Enrollment#31`)
has **no closing keyword in the body at all** — genuine omission. So
``keystone-prs-omit-closing-keywords`` is correct *for the keystones* and must not be
generalized to stacked PRs.

## Why it matters operationally

`agent_I_content #4` is the **only** stacked PR the merge plan MERGES rather than closes,
and merge-fleet.sh retargets it to default first (line 304).

- **Retarget succeeds** → base becomes default → `Fixes #3.` re-arms → **issue #3 auto-closes
  on merge** → the plan's 27 hand-closes is correct.
- **Retarget fails** → `merge_ready agent_I_content 2` on the line *above* has already moved
  #2 to default, so #4 merges into a vacated branch: the fix never reaches default, **and**
  #3 never auto-closes, **and** #3 is absent from the 27-item hand-close loop → the plan
  silently needed **28**.

So the R377/R378 retarget gate is **load-bearing for the issue ledger**, not just for the
code landing. That is a second, independent reason to apply it.

## Correction to my own R377

R377 stated: *"Live gh says #4 closingIssuesReferences=[] -> issue #3 SURVIVES … That is
codex R389's own 'prose keyword is not the API field' fact turned on me."*

**The attribution was wrong.** #4's body carries `Fixes #3.` — a valid keyword, not prose.
The conclusion (*#3 survives*) is true only on the **failure** path; on the success path #3
auto-closes. R377's comment shipped inside `counter-and-retarget-R377.patch`, so the patch
is retired as `counter-and-retarget-R377.SUPERSEDED-BY-R378.patch` and reshipped as
`counter-and-retarget-R378.patch` with the mechanism corrected inline.

## Two false-zero traps hit while proving this

1. `grep -F -i "clos"` on #4's body returned **ZERO** — the keyword is `Fixes`, a different
   member of GitHub's keyword family. A "clos"-only grep would have "confirmed" the wrong
   story. Grep the whole family: `clos(e|es|ed)|fix(es|ed)?|resolv(e|es|ed)`.
2. My own evidence printer truncated body lines at 150 chars, which cut `Fixes #3.` off the
   end of #4's line 2 and briefly made me conclude the body had no keyword at all — a
   louder and wronger finding. Print the **match**, not the line.

## Issue-side partition cert (new — R374 partitioned PRs, never issues)

| repo | open issues | auto-closed by a merging PR | hand-close required |
|---|---|---|---|
| job_opportunity_scanner | 20 | 5 (`68←69, 66←67, 64←65, 62←63, 26←27`) | **15** = 30 32 34 36 38 41 43 45 47 49 51 53 55 57 59 |
| -Community_intake_Routing | 13 | 1 (`39←40`) | **12** = 14 16 18 20 22 24 26 28 30 32 34 36 |
| agent_I_content | 3 | 2 (`7←9, 5←6`) | **0 — conditional**: #3 auto-closes iff #4's retarget lands |
| Enrollment_Funnel_Agent | 3 | 1 (`28←29`) | 0 (#30 owner-only, #24 infra) |
| ai-video-reel-generator | 4 | 3 (`30←31, 26+28←27`) | 0 (#5 infra) |

**27 hand-closes exactly**, matching the dry run — with **#3 as a 28th on the failure path only.**

## Plan re-cert against codex's current revision

- merge-fleet.sh md5 `b0caab63` (mtime 2026-09-27T16:55:04Z — rewritten 13 min into this run).
- `counter-and-retarget-R378.patch` applies with **zero fuzz**; `bash -n` clean; gate wired at
  the **call site** (`if retarget …; then merge_ready … else [HOLD]`), not just in the helper.
- **Both dry runs byte-identical** → the certified plan is unchanged. Tuple reproduced
  independently: **24 merges / 14 PR-closes / 1 retarget / 27 issue-closes / 4 draft-skips.**
- All four unconditional-increment sites (lines 75/86/95/103) are **still live** on
  `b0caab63` — the R377/R378 patch remains unapplied.
- `patch --dry-run` was run against a **copy**; codex's live file mtime and md5 were
  re-checked after and are unchanged (R377's lesson applied).
