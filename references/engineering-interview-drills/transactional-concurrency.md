# Transactional Concurrency and Limited-Inventory Drills

Use this reference to run an adaptive backend interview about concurrent writes to bounded resources. Focus on business invariants, database arbitration, transaction boundaries, retry semantics, and contention. Ask exactly one question at a time, choose only the next unresolved issue, and do not expose the rubric before the candidate answers.

## Contents

- [Topic Boundary](#topic-boundary)
- [Starting Drill](#starting-drill)
- [Alternative Scenarios](#alternative-scenarios)
- [Adaptive Follow-up Ladder](#adaptive-follow-up-ladder)
- [Strong Signals](#strong-signals)
- [Weak or Risky Signals](#weak-or-risky-signals)
- [Model Answer Outline](#model-answer-outline)
- [Calibration](#calibration)
- [Session-Summary Priorities](#session-summary-priorities)

## Topic Boundary

Use this drill when the primary problem is synchronous arbitration among concurrent database writes: limited inventory, one-per-user eligibility, reservations, quotas, balances, counters, or mutually exclusive state transitions.

Use `api-contract-design.md` when the primary problem is request and response semantics, especially partial success or long-running job resources. Use `async-workflow-recovery.md` when ownership, leases, workers, queues, or provider reconciliation are central. Idempotency may appear in all three, but do not turn a short transactional command into a job without a workload or external-latency reason.

## Starting Drill

> An e-commerce platform releases 10,000 limited coupons. Each authenticated user may claim at most one. Traffic spikes when the campaign opens, clients may submit concurrently from multiple tabs, and a request may be retried after an ambiguous timeout. Design the claim path so the system does not oversubscribe inventory, does not issue two coupons to one user, and returns an authoritative result.

Do not assume a queue, cache, or globally distributed database. Let the candidate state the workload and reliability assumptions that would justify additional components.

## Alternative Scenarios

Use one of these when the candidate has already practiced coupons or when another domain better tests transfer:

- **Seat hold:** Two users try to reserve the last seat. A hold expires after several minutes, and payment may finish near the expiration boundary.
- **Inventory checkout:** Several orders compete for the final units of one SKU, while duplicate checkout submissions may use different request identifiers.
- **Usage quota:** Concurrent API calls consume the final units of a tenant's monthly quota, and rejected requests must not be charged.
- **Single-winner transition:** Two operators attempt incompatible transitions on the same order, such as cancel and ship.

Preserve the core properties: at least one bounded or exclusive invariant, concurrent actors, a durable database decision, and a client that may not know whether a commit succeeded.

## Adaptive Follow-up Ladder

Choose only the next unresolved issue. Skip concerns the candidate already defended.

1. **Invariants:** Ask the candidate to state the exact rules the database must preserve before naming mechanisms.
2. **Data model:** Ask which rows and constraints represent capacity, claims, ownership, and operation replay.
3. **Last-unit race:** Let two different users request the final unit simultaneously and ask where arbitration occurs.
4. **Lock scope:** If the candidate uses `SELECT ... FOR UPDATE`, ask what is locked, when the condition is rechecked, and how long the lock is held.
5. **Conditional update:** Ask the candidate to compare a locked read with `UPDATE ... WHERE remaining > 0 RETURNING`.
6. **Business duplicate:** Let the same user submit concurrently with two different idempotency keys and ask how the one-per-user rule survives.
7. **Key reuse:** Reuse one idempotency key with a different payload and ask whether the old result may be returned.
8. **Transaction ordering:** Ask what happens if inventory changes but the claim insert fails, or the claim is inserted before capacity is secured.
9. **Ambiguous commit:** Let the transaction commit but the HTTP response disappear and ask how the client learns the authoritative result.
10. **Isolation behavior:** Ask which anomalies the chosen statements prevent under the selected isolation level without accepting “use serializable” as an unexplained answer.
11. **Deadlock:** Introduce an operation that locks two resources in opposite order and ask for prevention, bounded retry, and observability.
12. **Contention:** Make one campaign or SKU a hot row and ask when serialization is acceptable and when the design must evolve.
13. **Derived counters:** Ask whether a stored claimed counter or an aggregate over claim rows is authoritative and how drift is detected or repaired.
14. **Cancellation or expiry:** Add a release path and ask how returned capacity avoids double release or resurrection of stale holds.
15. **Operations:** Ask how the team detects oversubscription attempts, lock waits, deadlocks, idempotency conflicts, counter drift, or abnormal latency.

## Strong Signals

Look for decisions that assign each guarantee to the correct layer.

- State invariants first, such as total successful claims not exceeding capacity and at most one claim per campaign and user.
- Derive authenticated identity on the server rather than trusting a client-supplied user identifier.
- Use a database constraint such as `UNIQUE (campaign_id, user_id)` as the final one-per-user arbiter.
- Scope idempotency by authenticated principal and operation, compare a canonical request hash, and reject key reuse with a different request.
- Distinguish transport replay using the same key from a business duplicate using different keys.
- Keep the stock decision and claim write in one short database transaction, with rollback closing partial-write windows.
- Understand that `SELECT ... FOR UPDATE` normally locks selected rows, not the whole table, and recheck mutable conditions after acquiring the lock.
- Use a conditional atomic statement such as `UPDATE ... WHERE claimed_count < capacity RETURNING ...` when it expresses the invariant clearly.
- Let affected-row count or `RETURNING` distinguish success from exhausted capacity; do not rely on a stale application read.
- Translate expected uniqueness or capacity conflicts into stable business outcomes rather than exposing raw database errors.
- Recover an ambiguous HTTP timeout by replaying the same idempotency key or querying authoritative claim state.
- Avoid holding a transaction open across payment, provider calls, user think time, or other slow external work.
- Use a stable lock order for multi-row operations and retry deadlock victims only when the command is safe to replay.
- Recognize a hot campaign row as a serialization point and justify whether its measured throughput is sufficient before adding complexity.
- Separate reservation, confirmation, expiry, and release transitions when resources are held before final consumption.
- Define metrics for conflict rate, sold-out rate, lock-wait duration, deadlocks, transaction latency, and invariant-repair events.

## Weak or Risky Signals

Probe further when the answer:

- Checks remaining inventory in application code and inserts later without a transaction or database predicate.
- Claims that two requests cannot race because the frontend disables the button.
- Uses only an idempotency key to enforce one-per-user eligibility.
- Returns an old result for a reused key without comparing the request payload.
- Says `SELECT ... FOR UPDATE` locks the entire table when only a campaign row was selected.
- Reads capacity before acquiring the lock and does not recheck it afterward.
- Updates a counter and inserts a claim in separate transactions.
- Catches a uniqueness error but forgets that the current PostgreSQL transaction is aborted until rollback.
- Automatically retries with a new idempotency key after an ambiguous timeout.
- Recommends a queue, distributed lock, or serializable isolation without explaining which invariant requires it.
- Holds row locks while waiting for payment or another external system.
- Ignores deadlocks, hot-row throughput, cancellation, expiry, or operational repair when those properties are part of the scenario.
- Claims exactly-once client behavior instead of stating the database invariant and replay behavior.

## Model Answer Outline

Use this only after evaluating the candidate. Produce the stronger answer in first person and label workload-dependent choices as assumptions.

1. State the capacity, eligibility, and replay invariants.
2. Define campaign, claim, and idempotency records plus their database constraints.
3. Derive user and tenant identity from authentication and validate campaign eligibility.
4. Explain the short transaction and choose a locked read or conditional update.
5. Walk through two users competing for the final unit.
6. Walk through one user submitting with the same key and with different keys.
7. Explain rollback behavior for counter, claim, and idempotency-result writes.
8. Define stable success, already-claimed, exhausted, key-conflict, and retryable responses.
9. Explain recovery when commit outcome is ambiguous to the client.
10. Discuss isolation assumptions, deadlock handling, hot-row limits, metrics, and the threshold for redesign.

## Calibration

For a moderate single-region workload, accept one campaign row as the serialization point when a short transaction, proper indexing, and measured throughput satisfy the requirement. Do not require sharded counters, pre-generated token rows, Redis locks, or a queue by default.

Increase difficulty when the candidate has defended the simple design by adding a measured hot-row bottleneck, multiple inventory dimensions, expiring holds, payment, regional writes, or strict fairness. Require each added component to preserve a named invariant and justify its operational cost.

## Session-Summary Priorities

When the drill ends, summarize:

1. Whether the candidate states business invariants before selecting concurrency mechanisms.
2. Whether the candidate assigns replay, uniqueness, capacity, and atomicity to the correct layers.
3. Whether the candidate can explain lock scope, rollback, ambiguous commit recovery, and contention without unnecessary infrastructure.
