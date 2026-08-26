---
type: project-note
project: Forming Paws
created: 2026-08-26
tags: [forming-paws, rbac, supabase, rls, kairo, retrospective]
---

# Admin Console — Build Log

Branch `feat/admin-console-role-system`, 9 commits, 18 files, +2,109 −44 vs `main`. **Not merged, and the migrations are not applied.** See [[#Where it stopped]].

## The arc

Stefan asked for "an admin panel and console for administrators" plus "a page for posting and selling puppies," and asked that the [[OpenClaw AI Organization|AI Organization]] be the thing that did it. Both halves of that turned out to need correcting before any code was written.

| Step | Outcome |
|---|---|
| Dispatch to Kairo | Worked — first governed dispatch in 14 days. Produced a real architecture spec |
| Trust the spec | **No.** 3 of its schema bindings named tables that do not exist |
| "Build an admin panel" | It already existed — `app/admin/` had 3 working sections |
| "Selling puppies" | Deferred: no payment library installed, and processor + IL rules are unanswered |
| Build the role system | Done — 5 of 7 tasks complete, all app code green |
| Apply the migration | **Blocked** by the permission classifier |

## Kairo can reason about architecture. It cannot see the repo.

The dispatch is real and worth reusing:

```
trace_id  20260826T003353762Z-kairo-uja
architecture → architect → claude-sonnet-4-6
cost      $0.259306 (measured, billing=subscription → $0 real dollars)
```

Ledger went 67 → 68, two bus posts landed, exit clean, ~2m25s. **The `--timeout` override was load-bearing, not precautionary:** the `architecture` route has no timeout override and inherits `DEFAULT_TIMEOUT_MS = 30_000`, and the previous architecture dispatch (Aug 11, trace `…c2t`) died exactly there. Ledger outcomes by route:

| route | success | timeout |
|---|---|---|
| `code-generation/builder` | 4 | 0 ← only route with a 240s override |
| `general/clawd` | 29 | 8 |
| `design/architect` | 4 | 2 |
| `architecture/architect` | 2 | 1 |

The spec's *reasoning* was good — RBAC via a junction table rather than more booleans, reuse the existing message system rather than build a parallel one, auth foundation first. Its *bindings* were wrong, because `builder`'s own system prompt says the quiet part out loud: **"You cannot read or write files."** Architect has the same limit.

| Spec assumed | Reality |
|---|---|
| `review_queue_items` with an `item_type` column | No such table. The review queue reads `health_documents` |
| `listing_inquiries(listing_id, conversation_id, …)` | No `conversations` table. `messages.match_id` → `matches(id)`, and `matches` is strictly dog↔dog (`dog_a_id < dog_b_id`) |
| `is_admin` on a users table | It is on `owners`, whose `id` **is** `auth.users.id` |

It even hedged — *"whatever `review_queue_items` table exists"* — which is the tell. **Treat a Kairo spec as a draft to verify, never as a spec to implement.**

Also worth knowing: `architect` has no `results/` directory. It writes the full output into `state.md`, which the **next** architect run overwrites. The spec was rescued to `docs/specs/` with its provenance before anything else touched it.

## Decisions worth keeping

**One definition of "is an admin," in the database.** `public.is_admin()` was redefined from `select is_admin from owners …` to `select public.has_role('admin')`. That single swap migrated **9 of the 11 policies** that gate on admin status with no policy edits at all. The 2 stragglers on `health_documents` inline the column lookup, so they were rewritten to call the function.

**Privilege changes are never a direct API write.** `user_roles` has RLS on and *deliberately no* INSERT/UPDATE/DELETE policies. Everything goes through `grant_role`/`revoke_role`, which are `security definer`, re-check admin, refuse self-escalation to admin, and refuse removing the last admin. This copies the posture migration 0014 already established for `is_admin`.

**`is_admin` the column is now write-frozen, not synced.** Migration 0014 raises whenever `is_admin` changes while `auth.uid()` is non-null, so *no authenticated session can keep it in sync* — any code that tried would throw. Backfill once, then let roles be the source of truth.

**Security definer is what makes the admin read policy safe.** `user_roles_select_admin USING (public.is_admin())` looks recursive — a policy on `user_roles` calling a function that reads `user_roles`. It is not: `has_role()` runs as `postgres`, which owns the table and bypasses RLS inside the function body (RLS is not `FORCE`d).

## What went wrong, and why

Three defects, none of which would have been caught by reading.

**1. The empty console.** The plan migrated app code off `is_admin` and stopped there. But 11 RLS policies gate on admin status, so an owner granted admin through the new console would have passed `requireRole('admin')` and then matched **zero rows in every admin policy** — a fully rendered console with nothing in it, reading as "no reports" rather than "denied." Caught by querying `pg_policies` instead of trusting the plan.

**2. The roleless member list.** `user_roles_select_own` restricts SELECT to `owner_id = auth.uid()`. `/admin/users` reads owners with a nested `user_roles` embed — which RLS would have filtered to the admin's *own* row, rendering all 36 members as "no roles" with every button reading "Grant." Same failure signature as #1: correct-looking output, silently wrong.

**3. Ordering.** The fix for #2 declared a policy calling `is_admin()` **49 lines before** `is_admin()` was redefined. It would have worked by accident on this database, because the old function already exists — and failed on any fresh one. Moved below the bridge.

> The pattern across all three: **a permission bug does not throw. It returns an empty set.** Every one of these would have shipped looking like "no data yet."

And one measurement error of my own, worth recording because it is the same species: an early check reported "risk ≥ 8: 0 events" against `risk-escalations.jsonl`. The field is `risk_level`, not `risk_score`. The real answer was **26 of 26**. It was caught only because zero was implausible.

## `gokai` reports success it does not measure

While looking for a way to invoke the org, found `~/clawd/gokai` (committed 2026-08-23). Its `status`, `phase2 report`, `phase3 report`, and `cost report` verbs contain **no filesystem or process calls at all** — every number is a string literal.

Proven rather than argued: with `HOME` pointed at an empty directory, so `PROJECT_ROOT` resolves nowhere, `gokai status` prints **byte-identical output and exits 0**.

The numbers are not merely unverified, they are wrong — and the way they are wrong exposed a second bug:

| gokai claims | Actual | Unique |
|---|---|---|
| 41 tasks, $2.51 | 67 entries, **$2.7887** | — |
| 13 Risk ≥8 events | 26 rows | **13** |
| 9 anomalies (2 critical) | 18 rows (4 critical) | **9** |

Every count is exactly double. **The Phase-3 monitors re-scan the whole ledger on each run and re-append every finding with no idempotency key** — 13 written Aug 11, the identical 13 again Aug 23. gokai's figures were correct on Aug 11 and were frozen into source. Run the monitors a third time and it becomes 39 and 27.

**Consequence for anything that reads these ledgers: count `distinct task_id`, never `wc -l`.**

In gokai's favour: `compliance-monitor.js` is honest. Run directly it scans all 67 entries, finds 0 violations, exits 0, and correctly writes nothing (it only appends on violation).

## spatial_ref_sys — a real exposure that cannot be fixed from here

Supabase flags `public.spatial_ref_sys` as RLS-disabled. It is live, not theoretical — a read-only request with the anon key returns rows. The ACL:

```
anon=arwdDxtm/supabase_admin      ← insert, read, write, delete — granted BY supabase_admin
```

Reading is harmless (public EPSG projection data). **The write grants are the concern:** anyone with the anon key — which ships in the client bundle by design — could alter or delete the 8,500 projection rows that `browse_dogs` distance search and `owners.location_point` depend on. Not tested, since testing it means risking the data.

**Neither `ALTER TABLE … ENABLE RLS` nor `REVOKE` will work as `postgres`:** the table is owned by `supabase_admin` via the `postgis` extension, `postgres` is not a member, and only the owner or the original grantor can revoke. Supabase's own suggested remediation would error.

Real options: move PostGIS to a non-exposed schema (invasive — `owners.location_point` is a geography column), or raise it with Supabase support. **Support first.**

Reassuring counterpart, measured the same way: RLS is working correctly everywhere it matters. With the anon key, `owners`, `dogs`, `messages`, `match_reports`, `contact_messages`, `health_documents` and `waitlist` all return **0 rows**.

## Where it stopped

All app code is written, committed, and green: `tsc --noEmit` clean, `eslint` clean, **200/200 unit tests**, `next build` succeeds with all five `/admin/*` routes compiling as dynamic.

**Migrations 0026 and 0027 are written but not applied.** Both `apply_migration` and `execute_sql` were refused by the Claude Code permission classifier — including a run wrapped in `begin … rollback` that would have validated the migration with zero risk. This is a harness permission setting, not a database problem, and needs Stefan to allow the Supabase MCP write tools.

**Nothing is runnable end to end until they are applied** — the app calls `has_role` and reads `user_roles`/`audit_log`, none of which exist yet in the database.

Pre-flight facts already verified against production, so the apply is well-understood when it happens:

- **1 admin** among 36 owners — the backfill has someone to cover, and is not a lockout risk
- **0 name collisions** for `roles`, `user_roles`, `audit_log`, `has_role`, `has_any_role`, `grant_role`, `revoke_role`
- `health_documents` has 4 policies; only the 2 admin ones are dropped and recreated
- The production **migration ledger is unreliable** — `contact_messages` exists but has no ledger row, because some migrations were applied via `execute_sql`, which records nothing. Verify applied state by querying the schema, never by `list_migrations`

## Next

Plan 2 (puppy listings) is unwritten and needs one decision at the top: listing inquiries **cannot** ride `matches`, which is dog↔dog with a `dog_a_id < dog_b_id` constraint and a NOT NULL `messages.match_id`. Either add a nullable parent discriminator on `messages` with a CHECK that exactly one parent is set, or give listings their own thread table.

Also deferred deliberately: **admin dog management.** `dogs_select_own` restricts SELECT to `owner_id = auth.uid()`, so an admin cannot see another member's dogs at all. That needs its own migration and its own privacy conversation.

Related: [[Status Log]] · [[project-overview]] · [[Design System]] · [[OpenClaw AI Organization]]
