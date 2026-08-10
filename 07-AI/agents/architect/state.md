---
agent: architect
role: System Design Supervisor
mode: "full"
status: "idle"
last_run: "2026-08-10T23:33:48.281Z"
current_task: null
active_spec: null
runs_completed: 9
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
*2026-08-10 (full)*

## What We're Building
A centralized, append-only, tamper-evident audit logging service that captures every meaningful system action — who did what, to which resource, when, and from where — to satisfy SOC 2, HIPAA, GDPR, and PCI-DSS requirements. The system ingests events asynchronously from any internal service, writes them to immutable storage with cryptographic hash chaining, and exposes a read-only query and reporting layer for auditors and compliance teams.

---

## Key Decisions

1. **Async queue-backed ingestion over synchronous writes.** Services should not fail or slow down because the audit system is under load. A durable message queue (Kafka or SQS) decouples producers from the writer, guarantees at-least-once delivery, and lets the writer batch-flush for throughput — accepting a brief lag in exchange for zero producer impact.

2. **Hash-chained WORM storage over a mutable database.** Each event stores a SHA-256 of its own fields plus the previous event's hash (like a blockchain). Paired with S3 Object Lock (Compliance mode) or a TimescaleDB append-only hypertable, this makes retroactive alteration detectable and legally defensible without an external notary service.

3. **Strict schema at write time, PII masking before persistence.** Data classification happens at the ingestion boundary — before anything hits the queue. Fields tagged as PII are hashed or redacted to prevent GDPR/HIPAA violations in the log store itself, avoiding costly retroactive purges.

---

## Spec

### Data Models

**`AuditEvent`** (write-once)
```
event_id       UUID            PK, generated server-side
timestamp      TIMESTAMPTZ     UTC, set by ingestion layer (not caller)
actor          JSONB           { id, type: user|service|system, ip, user_agent }
action         VARCHAR(128)    verb.noun pattern — e.g. "record.delete", "user.login"
resource       JSONB           { type, id, name }
outcome        ENUM            success | failure | error
context        JSONB           { request_id, session_id, tenant_id, env }
before_state   JSONB           nullable; PII-masked snapshot before change
after_state    JSONB           nullable; PII-masked snapshot after change
metadata       JSONB           extensible free-form fields
prev_hash      CHAR(64)        SHA-256 of previous event; null for genesis record
event_hash     CHAR(64)        SHA-256 of all above fields concatenated
```

**`RetentionPolicy`**
```
policy_id      UUID
tenant_id      UUID
action_prefix  VARCHAR         e.g. "user.*" or "*"
retain_days    INT             e.g. 2555 (7 years for HIPAA)
archive_tier   ENUM            hot | warm | glacier
```

---

### API Contracts

All write endpoints are **internal-only** (mTLS, no public exposure).

| Method | Path | Auth | Purpose |
|---|---|---|---|
| `POST` | `/internal/audit/events` | mTLS service identity | Enqueue one or batch of events |
| `GET` | `/audit/events` | RBAC: auditor role | Query events (filters: actor, resource, action, outcome, time range, tenant) |
| `GET` | `/audit/events/{id}` | RBAC: auditor role | Retrieve single event with hash verification status |
| `GET` | `/audit/verify` | RBAC: auditor role | Verify chain integrity over a time window; returns first broken link if any |
| `POST` | `/audit/reports` | RBAC: compliance role | Generate async compliance report (SOC2/HIPAA/PCI scope) |
| `GET` | `/audit/reports/{id}` | RBAC: compliance role | Fetch generated report |

---

### Components

| Component | Responsibility | Interface |
|---|---|---|
| **Ingestion API** | Validate schema, classify/mask PII, stamp server-side timestamp, publish to queue | REST `POST /internal/audit/events`; rejects malformed events with 422 |
| **Log Writer** | Consume from queue, compute hash chain, flush to WORM store in ordered batches | Queue consumer; writes to immutable store; exposes health metric |
| **Query Service** | Read-only search over audit store with filtering, pagination, and field projection | REST `GET /audit/events*`; backed by a read replica or search index |
| **Integrity Verifier** | Scheduled job recomputes hash chain over sliding window; alerts on mismatch | Cron + alerting webhook; writes verification run records |
| **Retention Manager** | Enforces per-tenant `RetentionPolicy`; archives to cold tier; hard-deletes past legal hold | Scheduled job; reads policy table; never deletes within hold period |
| **Report Generator** | Produces structured compliance reports (PDF + JSON) for defined audit scopes | Async job triggered via `POST /audit/reports`; polls completable |

---

### Integration Points

- **Message queue** (Kafka / AWS SQS FIFO) — between Ingestion API and Log Writer; SQS FIFO preserves ordering per tenant
- **Immutable store** — S3 with Object Lock in Compliance mode + ClickHouse or TimescaleDB for queryable hot tier
- **Identity Provider** — Ingestion API resolves `actor.id` to canonical identity at write time; no runtime lookups from query layer
- **SIEM / observability** (Splunk, Datadog, OpenSearch) — Log Writer publishes a parallel stream for real-time alerting; audit store is source of truth
- **Alerting** — Integrity Verifier and anomaly thresholds (e.g. >N deletes/min by one actor) push to PagerDuty/Slack webhook

---

## Risks

| Risk | Mitigation |
|---|---|
| **Privileged insider tampers with logs** | WORM storage (Object Lock Compliance mode) + off-site hash anchoring to a separate AWS account the audit team controls; writer service has no delete permission |
| **High write burst overwhelms ingestion** | Queue absorbs spikes; auto-scale Log Writer consumers; Ingestion API sheds load gracefully with 429 rather than dropping events |
| **PII leaks into log payloads violate GDPR/HIPAA** | Field-level PII classifier runs in Ingestion API before enqueue; sensitive fields hashed (SHA-256 + pepper) or redacted; schema enforced at queue boundary — no raw PII ever hits the store |

---

## Done When

1. **Ingestion throughput:** Sustained 10,000 events/sec at p99 write latency ≤ 150 ms, verified by load test with no events dropped.
2. **Tamper evidence:** Integrity Verifier runs against 1 million chained events and reports zero hash mismatches; manually flipping one byte in one event causes verifier to identify the exact broken link.
3. **Compliance query:** An auditor can retrieve all `record.delete` actions by a given actor over any 90-day window in ≤ 5 seconds, and a full SOC 2 report for that window generates completely in ≤ 60 seconds.

---

## Handoff

**Build the `AuditEvent` schema and the Ingestion API (`POST /internal/audit/events`) first.**

This is the single write path everything depends on. Nail schema validation, PII masking logic, server-side timestamping, and queue publishing before any other component exists. All downstream components (writer, query, verifier) are read-from-queue or read-from-store — none can be meaningfully built or tested until the event structure and ingestion contract are locked.


<!-- KAIRO-LEDGER -->
## Cost Ledger (appended by Kairo — supervisors must not rewrite below this line)

[2026-08-10T23:32:41.534Z] design via claude-sonnet-4-6: SUCCESS cost_usd=0.175340 billing=subscription measured=true trace=20260810T233241534Z-kairo-s31