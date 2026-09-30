# Production Operations and Observability

Use this reference when a reviewed role or interview asks about production ownership, observability, monitoring, alerts, SRE concepts, incident response, debugging, reliability, backup/restore, scaling, or on-call. Keep professional production debugging, project deployment rehearsal, and sustained service ownership as separate evidence levels.

## Core Mental Model

Monitoring tells the team that a known condition occurred. Observability helps the team explain system behavior, including failures it did not predict in advance. Production ownership combines both with explicit reliability targets, response procedures, and repair.

Start with user-visible behavior:

```text
User journey and reliability target
  -> signals and correlation
  -> dashboards and actionable alerts
  -> triage and mitigation
  -> recovery verification
  -> root cause and follow-up
```

## Reliability Model

### Define service behavior

- Identify critical user journeys, dependencies, data boundaries, and failure modes.
- Choose service-level indicators such as successful request rate, correct job completion, latency, freshness, or durable-write success.
- Set an SLO only when it can guide a release, prioritization, or response decision.

### Instrument for questions

- **Logs:** structured events with severity, safe context, and correlation identifiers. Avoid secrets and unnecessary personal data.
- **Metrics:** rates, errors, duration, saturation, queue age, conflicts, retry outcomes, and business-critical counts.
- **Traces:** cross-boundary latency and causality when a request spans services or providers.
- **Audit events:** who performed a sensitive action and what authoritative state changed.

The goal is not to collect everything. Retain the smallest useful signals with appropriate privacy and cost controls.

### Build actionable alerting

- Page on symptoms requiring timely human action, not every internal anomaly.
- Include ownership, impact, useful context, and a next diagnostic step.
- Use dashboards and tickets for trends that do not require immediate action.
- Review false positives, missed incidents, and alert delivery itself.

### Respond to incidents

1. Confirm impact and establish ownership.
2. Stabilize the system with the safest bounded mitigation.
3. Communicate current impact, uncertainty, and next update.
4. Verify recovery from the user's perspective.
5. Preserve evidence and develop a causal timeline.
6. Prioritize follow-ups that reduce recurrence, blast radius, or recovery time.

Do not delay mitigation to find a perfect root cause. Do not call a restart a root cause.

### Plan data and disaster recovery

- Separate high availability from backup and restoration.
- Define RPO and RTO according to product need.
- Test restore into an isolated environment and reconcile data, permissions, indexes, and application compatibility.
- Document what rollback cannot repair, including external side effects or destructive data changes.

### Plan capacity and degradation

- Measure utilization, latency distribution, dependency limits, hot rows, queue age, and cost.
- Define backpressure, timeouts, bounded retry with jitter, circuit breaking, concurrency limits, or graceful degradation only when they address a named failure mode.
- Scale after identifying the bottleneck; do not equate autoscaling with unlimited capacity.

## Joseph Evidence Map

### Demonstrated professionally

- Used Coralogix, Amplitude, and Redash for release monitoring, dashboards, product analysis, and production debugging.
- Traced issues across frontend flows, API integrations, feature switches, logs, and analytics in a large production codebase.
- Coordinated release quality and cross-functional diagnosis.

### Implemented or rehearsed in projects

- `english-learning` includes health checks, candidate verification, authenticated smoke tests, promotion, rollback, operational exercises, and owner-safe data boundaries.
- Backend drills and implementations cover correlation IDs, stable errors, retry bounds, idempotency, ambiguous outcomes, stuck jobs, conflict metrics, and recovery reasoning.
- `google-ai-gcf` has sanitized error domains and extensive negative-path tests.

### Current evidence boundary

- Complete alert delivery, sustained observability, real traffic scaling, capacity planning, on-call rotations, and repeated incident response are not established.
- Initial restored-data reconciliation and independent IAM/database-role artifacts remain incomplete or partly operator-reported.
- A health check or dashboard alone does not prove service reliability.

## Reusable Interview Answer

Use this structure:

1. Define the user journey and reliability target.
2. Name signals that distinguish symptoms, causes, and product impact.
3. Explain correlation, privacy, dashboard, and alert design.
4. Walk through incident stabilization and recovery verification.
5. Cover backup/restore or capacity only where relevant.
6. State evidence level and current gaps.

Example outline:

> I start observability from the user journey rather than from available tools. I define the success and latency signals, then add structured logs and correlation IDs for diagnosis, metrics for rate/error/duration/saturation, and traces when the path crosses enough boundaries to need causal visibility. Alerts should be symptom-based and actionable, with an owner and a tested delivery path. During an incident I first confirm impact, stabilize with a bounded mitigation, communicate, and verify recovery before completing causal analysis and follow-up work. Professionally I have used Coralogix, Amplitude, and Redash for release monitoring and production debugging. My full release, health-check, rollback, and incident exercises are project-level evidence; sustained on-call and production-scale reliability remain areas to deepen.

## Learning and Proof Backlog

### High priority

- Complete response-ID correlation across ingress, application logs, database-relevant operations, and client-visible errors in `english-learning`.
- Verify alert delivery end to end and document who receives it, what action is expected, and how delivery failure is detected.
- Complete an isolated restore and reconciliation exercise, including authorization, counts, constraints, indexes, and application smoke tests.
- Run one incident exercise with a timeline, mitigation, recovery verification, and prioritized follow-up.

### Medium priority

- Define one availability/correctness SLI and one latency SLI with an SLO and explain the decision it drives.
- Add RED-style request signals and a small set of application-specific metrics such as review-write conflicts, oldest async age, or provider failure classification.
- Run a measured load/concurrency test and identify whether the limit is application, database, provider, or platform capacity.
- Learn RPO/RTO, graceful degradation, backpressure, circuit breakers, and retry storms through project-grounded scenarios.

### Lower priority unless role-driven

- Multi-region failover, distributed tracing platforms at scale, formal error-budget policy, fleet capacity planning, and production on-call program design.

### Evidence to capture

- Dashboard or query definitions with rationale.
- Alert notification and response evidence.
- Sanitized incident timeline and recovery verification.
- Restore/reconciliation record and documented RPO/RTO limitations.
- Before/after latency or error evidence from one targeted improvement.

## Readiness Standard

Use `Good` for product-engineering operational literacy because professional debugging and release monitoring are real strengths. Do not use `Strong` for service/system ownership until alerting, restore, incident, scaling, and sustained ownership evidence becomes materially deeper.
