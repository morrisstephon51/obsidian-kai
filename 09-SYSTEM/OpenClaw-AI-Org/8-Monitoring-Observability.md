# Monitoring & Observability
## OpenClaw AI Organization — Metrics, Alerts, and Operational Visibility

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Instrumentation) + Aexis (Audit)  
**Target Launch:** 2026-09-08 (Phase 2)  
**Status:** ACTIVE

---

## 1. Observability Strategy

### 1.1 The Three Pillars

**OpenClaw observability rests on three pillars:**

| Pillar | Purpose | Tools | Frequency |
|---|---|---|---|
| **Metrics** | Track quantitative system state (costs, latency, errors) | Message bus + logs | Real-time + daily summary |
| **Logs** | Record every action for audit + debugging | Message bus (SQLite) + files | Real-time (async) |
| **Traces** | Map request flow through supervisors + agents | Message bus correlation IDs | Per-workflow |

### 1.2 Observability Goals

1. **Visibility:** Every action in the system is logged + queryable
2. **Alerting:** Anomalies are surfaced to Kairo + Stef within 15 min
3. **Debugging:** Any failure can be traced end-to-end via logs + traces
4. **Cost Control:** Token spend tracked + alerted before budget overrun
5. **Performance:** Latency + error rates monitored; SLOs enforced

---

## 2. Core Metrics

### 2.1 System-Level Metrics

**Measured daily; aggregated weekly:**

| Metric | Target | Alert Threshold | Owner |
|---|---|---|---|
| **API Cost (daily)** | <$0.01 | >$0.015 (1.5x budget) | Kairo |
| **API Cost (weekly)** | <$0.05 | >$0.08 (1.6x budget) | Kairo |
| **Supervisor Heartbeats (hourly)** | ≥95% responsive | <90% → escalate | Aexis |
| **Message Bus Latency (p95)** | <500 ms | >1000 ms → escalate | Kairo |
| **Task Completion Rate** | >95% | <90% → investigate | Orchestrator |
| **Error Rate** | <5% | >10% → escalate | Aexis |
| **Average Task Latency** | <5 min | >10 min → review | Architect |

### 2.2 Agent-Specific Metrics

**Per supervisor; logged to message bus:**

```json
{
  "agent": "aeos-agent",
  "period": "2026-07-26T00:00:00Z",
  "metrics": {
    "invocations": 12,
    "successful_tasks": 11,
    "failed_tasks": 1,
    "total_tokens_used": 4200,
    "cost": "$0.0084",
    "avg_latency_ms": 3200,
    "p95_latency_ms": 7100,
    "errors": [
      {
        "timestamp": "2026-07-26T14:32:15Z",
        "error": "Timeout (max 5 min exceeded)",
        "task": "research_competitors"
      }
    ]
  }
}
```

### 2.3 Cost Tracking

**Token budget allocation (weekly):**

| Supervisor | Allocation | Used (example) | Remaining | Status |
|---|---|---|---|---|
| Kairo (routing) | $0.02 | $0.012 | $0.008 | ✓ OK |
| Orchestrator | $0.01 | $0.009 | $0.001 | ⚠️ TIGHT |
| Architect | $0.015 | $0.008 | $0.007 | ✓ OK |
| Aexis (audit) | $0.005 | $0.003 | $0.002 | ✓ OK |
| Aeos (research) | $0.02 | $0.018 | $0.002 | ⚠️ TIGHT |
| **Total** | **$0.07** | **$0.05** | **$0.02** | ✓ OK |

**Budget overage alerts:**
- 50% used → informational log
- 80% used → escalate to Kairo (ask Stef to approve more work or defer tasks)
- 100% used → halt all supervisors (require manual approval)

---

## 3. Logging Architecture

### 3.1 Log Levels & Destinations

| Level | Threshold | Destination | Retention |
|---|---|---|---|
| **DEBUG** | Development only | Local file (/.logs/debug.log) | 7 days |
| **INFO** | All operations | Message bus + local file | Forever (bus) / 30 days (file) |
| **WARNING** | Anomalies detected | Message bus + Telegram (to Kairo) | Forever (bus) |
| **ERROR** | Task/supervisor failure | Message bus + Telegram + file | Forever (bus) / 90 days (file) |
| **CRITICAL** | Security/data incident | Message bus + Telegram (to Stef) | Forever (bus) |

### 3.2 Message Bus Schema (SQLite)

**Audit log table (auto-created at startup):**

```sql
CREATE TABLE IF NOT EXISTS audit_log (
  id INTEGER PRIMARY KEY,
  timestamp DATETIME DEFAULT CURRENT_TIMESTAMP,
  agent_name TEXT NOT NULL,
  action TEXT NOT NULL,  -- "invocation", "completion", "error", etc.
  task_description TEXT,
  outcome TEXT,  -- "success", "failure", "timeout", etc.
  tokens_used INTEGER,
  cost_usd DECIMAL(10, 4),
  latency_ms INTEGER,
  data_classification TEXT,  -- "SENSITIVE", "INTERNAL", "PUBLIC"
  error_message TEXT,
  trace_id TEXT,  -- Correlation ID for multi-step workflows
  metadata JSON
);

CREATE INDEX idx_agent_time ON audit_log(agent_name, timestamp);
CREATE INDEX idx_trace_id ON audit_log(trace_id);
```

### 3.3 Logging Best Practices

**Every agent must:**

1. **Generate a trace_id** at workflow start
   ```python
   trace_id = uuid.uuid4()  # Generate once per workflow
   # Pass to all subagents in the chain
   ```

2. **Log start + completion**
   ```python
   # At start
   log_event("invocation", task_description, trace_id=trace_id)
   
   # At completion
   log_event("completion", outcome="success", tokens_used=1200, latency_ms=3500, trace_id=trace_id)
   ```

3. **Classify data before logging**
   ```python
   if contains_sensitive_data(data):
       log_event(..., data_classification="SENSITIVE", redacted=True)
   else:
       log_event(..., data_classification="INTERNAL")
   ```

4. **Include metadata**
   ```python
   log_event(..., metadata={
       "supervisor": "architect-agent",
       "input_tokens": 450,
       "output_tokens": 750,
       "model": "claude-haiku-4-5"
   })
   ```

---

## 4. Alerts & Escalation

### 4.1 Alert Rules (Automated, Starting 2026-09-08)

**Aexis runs these checks hourly:**

| Alert | Condition | Action |
|---|---|---|
| **Supervisor Down** | No heartbeat for 10 min | Restart supervisor + notify Kairo |
| **Latency Spike** | p95 latency >10 min | Log warning + investigate (disk I/O?) |
| **Error Rate High** | >15% errors in last hour | Alert Kairo + review error logs |
| **Budget Overrun** | Weekly spend >$0.06 | Escalate to Stef + request approval |
| **API Failure** | Claude/Perplexity down | Retry with exponential backoff + alert |
| **Message Bus Slow** | Write latency >1 sec | Cleanup old logs + optimize |
| **SENSITIVE Data Leak** | SENSITIVE data in external API call | CRITICAL alert to Stef immediately |
| **Unauthorized Access** | Agent accessing data outside domain | Log incident + escalate |

### 4.2 Alert Delivery

| Severity | Channel | Recipient | SLA |
|---|---|---|---|
| INFO | Message bus only | Kairo (can read async) | 1 hour |
| WARNING | Message bus + log file | Kairo | 15 min |
| ERROR | Message bus + log + Telegram | Kairo | 5 min |
| CRITICAL | Message bus + log + Telegram + Stef SMS | Both | <2 min |

---

## 5. Dashboards & Reporting

### 5.1 Daily Digest (Automated, 9 AM CT)

**Email to Stef (starting 2026-09-15):**

```
OpenClaw Daily Health Report — 2026-07-27

=== SYSTEM STATUS ===
✓ All supervisors healthy (8/8 responsive)
✓ Message bus: HEALTHY (0.3 sec avg latency)
✓ Token budget: $0.048 used / $0.05 allocated (96% — TIGHT)

=== YESTERDAY'S WORK ===
- Orchestrator: 5 workflows completed (avg latency 3.2 min)
- Architect: 3 specs generated (avg tokens 850)
- Aeos: 2 research tasks completed
- Aexis: Audit pass (0 violations)

=== ALERTS & ISSUES ===
⚠️  WARNING: Budget tight (96%). Recommend: defer non-critical work or request increase.
⚠️  WARNING: Orchestrator hit 5-min timeout once (Task: "phase-2-artifacts"). Resumed successfully.

=== NEXT ACTIONS ===
- Approval needed: Request $0.02 budget increase for Phase 2 work
- Review: Why did one Orchestrator task timeout?

--- End Report ---
```

### 5.2 Weekly Report (Manual, Stef + Kairo, Thursdays 10 AM)

**Review metrics + flags + plan next week:**

1. **Cost summary:** Actual spend vs. forecast
2. **Reliability:** Error rate, supervisor downtime
3. **Performance:** Avg latency, SLO attainment
4. **Incidents:** Any issues reported + root cause
5. **Forecast:** Expected spend next week
6. **Action items:** What needs attention?

### 5.3 Monthly Report (Aexis + Stef, 1st Friday)

**Comprehensive audit + compliance review:**

- Full audit log (structured)
- Risk Register review (new risks? resolved risks?)
- Compliance checklist (audit checks passing?)
- Cost trend (is burn rate increasing/decreasing?)
- Supervisor performance (who's excelling? who needs retooling?)
- Scaling readiness (any bottlenecks emerging?)

---

## 6. Instrumentation Runbook

### 6.1 Adding Metrics to a New Supervisor

**When adding a new supervisor (Phase 2+):**

1. **Define success metrics**
   - What does "done well" look like for this supervisor?
   - Examples: Architect → "specs reviewed + no rework"; Aeos → "research complete + high confidence"

2. **Add logging to supervisor code**
   ```python
   # At task start
   log_event("invocation", task_description, trace_id=trace_id, 
             supervisor="new-agent", start_time=time.time())
   
   # At task completion
   elapsed = time.time() - start_time
   log_event("completion", outcome="success", latency_ms=elapsed*1000, 
             tokens_used=response.usage.total_tokens, trace_id=trace_id)
   ```

3. **Update metrics schema** (add to 2.1 if critical)

4. **Create alert rule** (if failure is high-impact)

5. **Test logging** (manual run + verify logs appear in message bus)

---

## 7. SLO (Service Level Objectives)

### 7.1 OpenClaw SLOs

**We commit to:**

| SLO | Target | Measurement | Owner |
|---|---|---|---|
| **Availability** | 99% (1 hr downtime/month) | Kairo heartbeat + supervisor health | Kairo |
| **Latency (p95)** | <5 min per task | Message bus logs | Orchestrator |
| **Error Rate** | <5% tasks failed | Audit log outcome field | Aexis |
| **Budget Adherence** | Actual ≤ Planned | Weekly cost tracking | Kairo |
| **Audit Compliance** | 100% of actions logged | Message bus audit trail | Aexis |

### 7.2 SLO Tracking

**Monthly review:**
- Did we meet all SLOs?
- If not, why? (Outage? Misconfiguration?)
- What's the remediation?
- Update Risk Register with lessons

---

## 8. Debugging Guide

### 8.1 Common Issues & Traces

**Supervisor doesn't respond:**
```bash
# 1. Check heartbeat
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT MAX(timestamp) FROM audit_log WHERE agent_name='aeos-agent' AND action='heartbeat';"

# 2. Check for errors
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT * FROM audit_log WHERE agent_name='aeos-agent' AND outcome='error' ORDER BY timestamp DESC LIMIT 5;"

# 3. Check logs
tail -50 /Users/abdoulayemundow/clawd/.logs/aeos-agent.log
```

**High latency on a task:**
```bash
# 1. Find the trace_id
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT trace_id, latency_ms FROM audit_log WHERE task_description LIKE '%search%' ORDER BY timestamp DESC LIMIT 1;"

# 2. Follow the trace
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT timestamp, agent_name, action, latency_ms FROM audit_log WHERE trace_id='<trace_id>' ORDER BY timestamp;"

# 3. Identify bottleneck (which agent took longest)
```

**Cost spike:**
```bash
# 1. Check daily spend by agent
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT DATE(timestamp), agent_name, SUM(cost_usd) FROM audit_log WHERE timestamp > datetime('now', '-7 days') GROUP BY DATE(timestamp), agent_name ORDER BY cost_usd DESC;"

# 2. Review expensive tasks
sqlite3 /Users/abdoulayemundow/clawd/.bus/bus.sqlite \
  "SELECT timestamp, agent_name, tokens_used, cost_usd FROM audit_log WHERE cost_usd > 0.01 ORDER BY cost_usd DESC LIMIT 10;"
```

---

## 9. Observability Roadmap

| Phase | Deliverable | Target Date |
|---|---|---|
| **Phase 2** | Health checks + alerts + daily digest | 2026-09-08 |
| **Phase 3** | Weekly reports + compliance audit automation | 2026-09-28 |
| **Phase 4** | Full SOC 2 compliance + external audit ready | 2026-10-12 |
| **Phase 5** | Real-time dashboard (Grafana/Datadog) | 2027-01-12 |

---

## Appendix: Observability Checklist

**Phase 2 (2026-09-08 — deploy observability stack):**
- [ ] Message bus schema created + tested
- [ ] Logging code added to all supervisors
- [ ] Alert rules configured (Aexis automation)
- [ ] Daily digest email template ready
- [ ] Cost tracking script deployed
- [ ] Health checks scheduled (cron)
- [ ] Sample 24-hour log review completed

**Phase 3 (2026-09-28 — mature observability):**
- [ ] Weekly reports generated automatically
- [ ] Compliance audit script passing
- [ ] Monthly review meeting established
- [ ] SLO tracking dashboard ready
- [ ] Debugging runbook tested on real incidents

