# Decision-Making Framework
## OpenClaw AI Organization — How Decisions Get Made, Logged, and Reviewed

**Version:** 1.0  
**Date:** 2026-07-26  
**Owner:** Kairo (Coordination) + Aexis (Audit)  
**Target Launch:** 2026-09-14 (Phase 2)  
**Status:** ACTIVE

---

## 1. Decision Framework Overview

### 1.1 Why a Decision Framework?

Without explicit decision processes, the system would suffer from:
- **Ambiguous authority:** Who decides what? No clear answer → wasted time
- **Silent failures:** Decisions made in isolation, no one knows why → hard to audit
- **Repeated mistakes:** No learning mechanism → same errors recur
- **Mistrust:** If decisions appear arbitrary, humans lose confidence in the system

This framework makes decision-making **explicit, traceable, and improvable**.

### 1.2 Core Principles

1. **Decisions are logged:** Every decision is recorded to message bus + audit trail
2. **Authority is clear:** Constitution + decision authority matrix tell you who decides
3. **Rationale is documented:** Why was this decision made? (What else was considered?)
4. **Escalation is non-discretionary:** High-risk decisions go to Stef automatically
5. **Learning is systematic:** Post-mortems identify why decisions worked or failed

---

## 2. Decision Taxonomy

### 2.1 Four Decision Types

**Decisions in OpenClaw fall into four categories:**

| Type | Authority | Approval | Logging | Deadline |
|---|---|---|---|---|
| **Strategic** | Stef | N/A | context.md + message bus | No deadline |
| **Operational** | Kairo | Weekly review by Stef | message bus | Daily |
| **Tactical** | Supervisor | Kairo if ambiguous | message bus | Per-task |
| **Escalation** | Kairo (automatic) | N/A | message bus + Telegram | <5 min |

### 2.2 Strategic Decisions

**Definition:** Decisions that change overall direction, priorities, or funding.

**Examples:**
- "Plug AI is Track 1; BigHeart is Track 2"
- "Phase 1-4 roadmap approved; Phase 5 pending"
- "Add compliance audit to Phase 3"
- "Budget allocation to supervisors: Architect $0.015/week, Aeos $0.02/week"

**Process:**
1. Stef identifies need for decision (priority shift, new constraint, opportunity)
2. Kairo + relevant supervisors provide input (what are the tradeoffs?)
3. Stef decides (usually via email + context.md update)
4. Kairo communicates to all (message bus post, context.md update)
5. Supervisors adjust their work (reallocate time/budget)

**Documentation:**
```
# Example: Strategic Decision Log (in context.md)

## 2026-07-26 — Phase 1-4 Roadmap Approved
**Decision:** Phase 1-4 implementation timeline confirmed (12 weeks).
**Authority:** Stef Mundow
**Rationale:** Comprehensive system foundation needed before scaling to multi-team.
**Alternatives Rejected:**
  - Faster timeline (8 weeks): Too risky, would sacrifice quality
  - Slower timeline (16 weeks): Overkill, we have time pressure
**Impact:** All supervisors align on Phase 1-4 deliverables; adjust roadmaps.
**Audit Trail:** Message bus post 2026-07-26 20:00 CT, context.md update 2026-07-26 21:00 CT
```

### 2.3 Operational Decisions

**Definition:** Day-to-day decisions about task routing, resource allocation, priority sequencing.

**Examples:**
- "Route this research task to Aeos (expert in forecasting)"
- "Allocate extra $0.005 budget to Architect this week (ahead of Phase 2 specs)"
- "Escalate Risk #4.1 to Stef (context.md drift detected)"
- "Reorder supervisor tasks: Orchestrator first, then Architect"

**Process:**
1. Kairo (or supervisor) identifies decision (new task, conflict, bottleneck)
2. Kairo routes / allocates (using authority matrix)
3. Decision logged to message bus (automatic)
4. Weekly review with Stef (Thursday 10 AM) — exceptions discussed
5. If decision is questioned, escalate (use conflict resolution protocol)

**Documentation:** Automatic (message bus logs all routing decisions)

### 2.4 Tactical Decisions

**Definition:** Supervisor-level decisions about how to execute assigned work.

**Examples:**
- "Use Sonnet for this spec (higher quality than Haiku, worth extra cost)"
- "Break this workflow into 3 phases (manage latency)"
- "Request clarification from Kairo (ambiguous requirements)"
- "Revert last commit (introduced regression)"

**Process:**
1. Supervisor makes decision (based on domain expertise)
2. Logs decision to message bus (with rationale)
3. Kairo reviews (did it align with task? any conflicts?)
4. If conflict or concern, Kairo escalates (or requests justification)
5. Supervisor executes (decision is final unless challenged)

**Documentation:** Message bus log + commit message (git)

### 2.5 Escalation Decisions

**Definition:** Automatic escalation when criteria are met (not discretionary).

**Triggers:**
- Risk Register score ≥8 (critical risk)
- SENSITIVE data exposure or mishandling
- Supervisor failure (2+ restarts in 1 hour)
- Token budget overrun (>80% weekly spend)
- External communication request
- Ambiguous task (Kairo posts to bus, waits 1 hour)

**Process:**
1. Condition detected (Kairo or Aexis monitor)
2. Automatic escalation (post to message bus + Telegram to Stef)
3. Kairo awaits response (1 hour max for urgent)
4. Stef decides (approve action, request more info, override)
5. Decision logged + executed

**Documentation:** Escalation request + Stef response logged to message bus

---

## 3. Decision Log Template

**Every decision must include:**

```json
{
  "decision_id": "2026-07-26-001",  // Unique ID (date + sequence)
  "timestamp": "2026-07-26T20:15:00Z",
  "decision_type": "operational",  // strategic | operational | tactical | escalation
  "title": "Route Phase 1-4 artifact workflow to Orchestrator + Architect",
  "authority": "kairo",  // Who decided? (stef | kairo | supervisor-name)
  "description": "Phase 1-4 buildout requires two supervisors: Orchestrator (decompose work) + Architect (generate specs). Workflow sequenced as: 1. Orchestrator routes, 2. Architect specs, 3. parallel execution.",
  "rationale": "Orchestrator is optimal for decomposition (domain expertise). Architect for spec quality (prevents rework).",
  "alternatives": [
    {
      "option": "Use Architect for both routing + specs",
      "rejected_because": "Architect would bottleneck; Orchestrator pipeline experience is wasted"
    },
    {
      "option": "Use Claude Base for routing (cost savings)",
      "rejected_because": "Routing is domain-specific; needs Orchestrator expertise"
    }
  ],
  "stakeholders": ["orchestrator-agent", "architect-agent"],
  "impact": "Phase 1-4 delivery timeline, supervisor allocation, cost forecast",
  "risks": [
    {
      "risk": "Orchestrator timeout on complex decomposition",
      "mitigation": "Risk Register #4.2 (workflow timeouts) has mitigation"
    }
  ],
  "logged_to": ["message_bus", "context.md"],
  "reviewed_by": ["kairo"],
  "approval_status": "approved",
  "escalation": false
}
```

---

## 4. Decision Review Process

### 4.1 Daily Review (Kairo, Ongoing)

**Kairo reviews tactical decisions in real-time:**
- Did the decision align with task assignment?
- Any conflicts with other decisions?
- Any escalation triggers?

**Action:** If conflict detected, post to message bus + request clarification

### 4.2 Weekly Review (Stef + Kairo, Thursday 10 AM)

**Kairo presents operational decisions from past week:**
- Which supervisors were routed to? Why?
- Any budget reallocations? Justified?
- Any escalations? How were they resolved?
- Any decisions that went unexpectedly?

**Discussion:** Stef can challenge decisions (why did you route to Aeos instead of Architect?), and Kairo explains rationale.

**Action:** Document exceptions + learnings (feedback loop)

### 4.3 Monthly Review (Aexis Audit, 1st Friday)

**Aexis audits decision logs:**
- Are all decisions documented (no silent decisions)?
- Are escalation triggers being honored?
- Are decision patterns consistent (or drifting)?
- Any decisions that caused rework / errors?

**Action:** Post audit report to message bus, recommendations to Stef

### 4.4 Quarterly Review (Stef + Kairo, Q starts + 4 weeks)

**Comprehensive decision audit:**
- Strategic decisions: Are we still aligned on priorities?
- Operational patterns: Is Kairo routing decisions appropriately?
- Tactical quality: Are supervisor decisions producing good outcomes?
- Decision velocity: How long are decisions taking? (Too slow? Too fast?)

**Action:** Update Constitution + governance policies (if needed)

---

## 5. Post-Decision Review (Learning Loop)

### 5.1 Did It Work?

**30 days after a significant decision, review:**

1. **Outcome:** Did it produce the expected result?
   - ✓ Better than expected
   - ✓ As expected
   - ✗ Worse than expected
   - ✗ Unresolved

2. **Cost:** What was the actual cost vs. forecast?
   - Token spend
   - Calendar time
   - Supervisor attention

3. **Risks:** Did any of the anticipated risks occur?
   - Which ones materialized?
   - Were mitigations effective?

4. **Alternatives:** Would a different decision have been better?
   - Hindsight perspective
   - What would we do differently?

**Documentation:**
```json
{
  "original_decision_id": "2026-07-26-001",
  "review_date": "2026-08-25",
  "outcome_vs_expected": "as_expected",
  "cost_actual_vs_forecast": {
    "tokens_forecast": 45000,
    "tokens_actual": 43200,
    "delta_pct": -4
  },
  "risks_materialized": ["workflow_timeout_once"],
  "risk_mitigation_effectiveness": "high (mitigation worked, task completed after restart)",
  "alternative_analysis": "Routing to Architect instead would have been slower but no timeout risk. Decision was correct.",
  "lessons": "Workflow timeout risk is real but manageable with restart protocol.",
  "action_items": [
    "Update Risk Register #4.2 (workflow timeout) — increase timeout to 60 min for Phase 2"
  ]
}
```

### 5.2 Feedback Loop

**Post-decision reviews feed back into:**
- Risk Register (new risks identified? Mitigations working?)
- Decision Framework (should we change how we make decisions?)
- Supervisor performance (did the routed supervisor perform well?)
- Process improvements (what can we do differently next time?)

---

## 6. Decision Anti-Patterns (What NOT to Do)

### 6.1 Silent Decisions

**❌ Bad:** Kairo routes a task without logging it, "we'll document later"
- No one knows why the decision was made
- Can't audit or review
- Kairo loses credibility

**✓ Good:** Decision logged to message bus at routing time (automatic)

### 6.2 Scope Creep via Defaults

**❌ Bad:** "No one objected, so I assumed approval"
- Escalation bypassed
- Stef unaware of commitment
- Builds technical debt

**✓ Good:** Explicit approval (Stef signs off on decision + timeline)

### 6.3 Decision Flip-Flopping

**❌ Bad:** Decision made Monday, reversed Thursday, re-approved Friday
- Undermines confidence in decision process
- Wastes supervisor time
- Signals authority confusion

**✓ Good:** Decisions are made once, with review gates (weekly, monthly) for learning

### 6.4 Undocumented Rationale

**❌ Bad:** "I decided this because I felt it was right"
- Can't audit
- Can't learn (why did it fail?)
- Hard to onboard new supervisors

**✓ Good:** Decision includes explicit rationale + alternatives considered

---

## 7. Scaling Decisions (Future)

### 7.1 Multi-Supervisor Decisions (Phase 2+)

**When a decision affects multiple supervisors:**

1. **Notify all stakeholders** (message bus post + Telegram ping if urgent)
2. **Solicit input** (3-day review window for feedback)
3. **Address conflicts** (if supervisors disagree, post reasoning)
4. **Approve** (Kairo or Stef, depending on type)
5. **Implement** (all supervisors execute in sequence or parallel, as needed)

### 7.2 Cross-Team Decisions (Phase 4+)

**When adding multiple teams (future scalability):**

1. **Decisions by committee** (domain heads + Stef + Kairo)
2. **Formal voting** (majority approval required)
3. **Dissent logged** (who disagreed and why)
4. **Escalation to CEO** (Stef) if tie vote

---

## 8. Decision Framework Checklist

**Phase 2 (2026-09-14 — implement framework):**
- [ ] Decision taxonomy documented + understood by all supervisors
- [ ] Decision log template in use (automatic via message bus)
- [ ] Weekly review meeting scheduled (Stef + Kairo, Thursday 10 AM)
- [ ] Escalation triggers automated (Aexis checks)
- [ ] Post-decision review template ready

**Phase 3 (2026-09-28 — mature framework):**
- [ ] 30-day post-mortems completed on key decisions
- [ ] Feedback loop updates Risk Register + governance
- [ ] Monthly audit identifying anti-patterns
- [ ] Decision velocity measured (are we deciding too fast? too slow?)

**Phase 4 (2026-10-12 — scaling framework):**
- [ ] Multi-supervisor decisions working smoothly
- [ ] Cross-team decision protocol drafted (for future teams)
- [ ] Decision performance metrics tracked (outcome quality, cost accuracy)

---

## Appendix: Example Decision Flow

**Scenario: Phase 2 budget reallocation (Orchestrator budget tight)**

```
TIME: 2026-09-08 10:00 CT — Decision Identified
  └─ Orchestrator alerts Kairo: "Budget 95% used, 6 workflows still pending"

TIME: 2026-09-08 10:15 CT — Decision Proposed
  └─ Kairo posts to message bus: "Proposal: Increase Orchestrator budget from $0.01 to $0.015/week"
  └─ Rationale: Phase 2 critical path, need headroom for unexpected tasks
  └─ Cost: +$0.005/week (total system budget still $0.055, within target)

TIME: 2026-09-08 10:30 — 2026-09-09 08:00 CT — Review Window
  └─ Stef reviews (asks: is this temporary or permanent? review in 2 weeks?)
  └─ Aeos reviews (asks: could we optimize workflows to reduce latency?)
  └─ Architect reviews (no conflict)

TIME: 2026-09-09 09:00 CT — Decision Made
  └─ Stef approves: "Yes, +$0.005/week for Orchestrator. Recheck in 2 weeks (2026-09-22)."
  └─ Kairo logs decision: decision_id=2026-09-09-015, approval_status=approved
  └─ Message bus notified: decision + reasoning

TIME: 2026-09-09 09:15 CT — Implementation
  └─ Kairo updates router config: orchestrator_budget=0.015
  └─ Orchestrator notified (new budget available)
  └─ Context.md updated: budget allocation + review date

TIME: 2026-09-22 10:00 CT — Review
  └─ Kairo posts: "Orchestrator budget review: used $0.012 of $0.015 (80%). Recommend keep at $0.015."
  └─ Stef approves: "Keep it. Good decision."
  └─ Decision logged as successful (post-mortem: cost forecast was accurate)
```

