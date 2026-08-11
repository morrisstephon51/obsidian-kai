---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-11T14:27:03.231Z"
current_task: null
active_spec: null
runs_completed: 11
last_error: null
---

# Architect — General-Purpose System Design Supervisor

Designs systems before Codex builds them. Produces specs, ADRs, and architectural plans for **any project**.
Token-lean: no context.md injection, max_tokens 1024, concise prompts.

Two modes:
- **Full** — Sonnet, structured spec (What/Key Decisions/Spec/Risks/Done When/Handoff)
- **Lite** — Haiku, numbered steps + done-when bullets only

Invocation:
```
node run.js "<design task>" [--mode lite] [--project "name"]
```

Core question: **"What exactly are we building and why, before a single line of code is written?"**

> v1 (Plug AI / BigHeart scoped, max_tokens 2048, context.md injection) archived to `agents/_archived/architect-agent-v1/`

## Active Spec
<!-- Architect writes the current design here -->

## Last Architecture Decision
*2026-08-11 (full)*

## What We're Building

An Orca-native orchestration pipeline that ingests a Phase 2 Week 2 work package, decomposes it into typed subtasks with explicit dependency edges, assigns each subtask to a supervisor terminal (coordinator or worker role), and tracks the full DAG to completion — using `task-create`, `dispatch --inject`, and `check --wait` lifecycle primitives so every subtask has auditable provenance, heartbeat coverage, and a single `worker_done` authority.

---

## Key Decisions

**1. DAG-first decomposition, not linear sequencing.**
Phase 2 Week 2 work typically has parallel-safe leaf tasks (implementation) blocked only by a small set of gate tasks (schema migration, infra provisioning). Encoding deps via `--deps` at `task-create` time lets `task-list --ready` surface the parallel frontier automatically, maximizing concurrency without coordinator logic.

**2. Supervisor = tracked coordinator terminal, not a human role.**
Each supervisor is an Orca agent terminal that owns a sub-DAG (a cluster of sibling tasks). It runs a `check --wait` loop, relays `worker_done` up to the root coordinator, and owns `gate-create` decisions within its cluster. This avoids a single-coordinator bottleneck while keeping lifecycle provenance chain unbroken.

**3. `orchestration run` for leaf tasks, manual loop for gates and supervisors.**
Leaf tasks with no decision dependency use `orca orchestration run` for simplicity. Supervisor-level tasks that require `gate-create`/`gate-resolve` or `ask`/`reply` cycles stay in a manual coordinator loop so the coordinator retains authority over blocking decisions.

---

## Spec

### Data Models / Schema

```
Task {
  id:         string          // orca-assigned
  spec:       string          // ≤ 160-char brief + full detail
  status:     pending | ready | dispatched | completed | failed | blocked
  deps:       string[]        // task ids that must complete first
  parent:     string?         // supervisor task id
  result:     json?           // populated on worker_done
  role:       "leaf" | "supervisor" | "gate"
}

Dispatch {
  taskId:     string
  dispatchId: string
  workerHandle: string        // concrete terminal handle
  coordinatorHandle: string
  injected:   boolean
}

Gate {
  id:         string
  taskId:     string
  question:   string
  options:    string[]?
  resolution: string?
  status:     open | resolved
}
```

### API Contracts (Orca CLI surface)

| Operation | Command |
|---|---|
| Create subtask | `orca orchestration task-create --spec <text> --deps <json> --parent <id>` |
| Assign to supervisor terminal | `orca orchestration dispatch --task <id> --to <handle> --inject` |
| Supervisor polls for completions | `orca orchestration check --wait --types worker_done,escalation,decision_gate --timeout-ms 900000` |
| Worker reports done | `orca orchestration send --to <coord> --type worker_done --payload {taskId,dispatchId,filesModified}` |
| Block on decision | `orca orchestration gate-create --task <id> --question <text> --options <json>` |
| Unblock | `orca orchestration gate-resolve --id <gate_id> --resolution <text>` |
| Heartbeat (long tasks) | `orca orchestration send --to <coord> --type heartbeat --payload {taskId,dispatchId,phase}` |

### Components

| Component | Responsibility | Interface |
|---|---|---|
| **Root Coordinator** | Owns the full Phase 2 W2 DAG; creates all tasks; dispatches supervisor tasks; waits on supervisor `worker_done`; resolves root-level gates | Runs in active worktree terminal; enters `check --wait` loop after fan-out |
| **Supervisor Agent (×N)** | Owns a sub-DAG cluster; dispatches leaf tasks to workers; runs inner `check --wait` loop; escalates unresolvable gates up to root; sends `worker_done` to root coordinator when all cluster tasks complete | Orca agent terminal created with `--agent claude` in current worktree; receives dispatch preamble via `--inject` |
| **Leaf Worker (×M)** | Executes a single atomic task (code change, test run, doc update); sends exactly one `worker_done`; uses `ask` for blocking questions | Fresh claude/codex terminal per task; created by supervisor via `orca terminal create --worktree active` |
| **Gate Resolver** | Surfaces blocking decisions to human or root coordinator; created by supervisor via `gate-create`; unblocked by root via `gate-resolve` | Orca gate primitive; no additional component needed |
| **Task Registry** | Persists DAG state, dispatch provenance, gate records | Orca runtime-global orchestration state; inspected via `task-list`, `dispatch-show`, `gate-list` |

### Integration Points

- **Orca runtime** (`orca status --json`) must be running before any task creation.
- **Git worktrees**: leaf workers that modify files stay in the active worktree (`--worktree active`); isolated checkout workers use `--no-parent` top-level worktrees only when they require independent state.
- **CI/external systems**: after leaf `worker_done`, root coordinator or supervisor posts merge-readiness signal via `--type merge_ready` to `@all` or a named review terminal.
- **Human escalation**: unresolved gates surface via `orca orchestration gate-list --status open --json`; human resolves via `gate-resolve` or direct coordinator `reply`.

---

## Risks

| Risk | Mitigation |
|---|---|
| Supervisor terminal goes stale mid-DAG (handle rotation after restart) | Re-resolve with `orca terminal list --worktree active --json` before each dispatch; never cache handles across turns |
| `worker_done` lost due to wrong target handle (group fanout or stale coordinator) | Validate that each worker's preamble carries concrete `coordinatorHandle`; reject `worker_done` sent to `@all` or group addresses |
| Gate deadlock — supervisor creates gate, root coordinator never polls it | Root coordinator loop must include `decision_gate` in `--types`; gate-list check as a fallback every N timeout cycles |

---

## Done When

1. `orca orchestration task-list --status completed --json` shows all Phase 2 W2 leaf tasks with non-null `result` payloads and no tasks in `failed` or `blocked`.
2. Root coordinator terminal receives `worker_done` from every supervisor terminal with `filesModified` arrays that account for all expected output artifacts.
3. `orca orchestration gate-list --status open --json` returns an empty array (no unresolved blocking decisions remain).

---

## Handoff

**First thing to build:** the root coordinator decomposition script — run `orca status --json` to confirm runtime is live, then call `orca orchestration task-create` in a loop for every Phase 2 W2 subtask with explicit `--deps` encoding, verify the DAG is correct with `task-list --brief --json`, and only then begin supervisor dispatch. Do not dispatch until the full DAG is committed to runtime state.

<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-10T23:32:41.534Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.175340 billing=subscription measured=true trace=20260810T233241534Z-kairo-s31
[2026-08-11T14:25:33.437Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.116302 billing=subscription measured=true trace=20260811T142533437Z-kairo-59k
[2026-08-11T14:25:33.435Z] architecture via claude-sonnet-4-6: SUCCESS cost_usd=0.142285 billing=subscription measured=true trace=20260811T142533435Z-kairo-59w