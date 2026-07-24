# Durable Async Workflow Recovery Drills

Use this reference when the candidate should design the execution and recovery of an already-accepted asynchronous job. Keep API contract discussion secondary unless it changes the worker guarantees. Ask exactly one question at a time, skip concerns the candidate has already defended, and stop once the important failure windows are covered.

## Starting Drill: Recoverable AI Processing

> A receipt-parsing job has already been persisted as `queued`. Workers call an external AI provider that may take seconds, time out, or finish after a worker loses connectivity. Workers may crash before the provider call, during it, or after it completes but before the result is saved. Design the job state machine, worker ownership, retry, and recovery behavior.

Do not ask for the complete solution immediately after this prompt. Let the candidate choose a starting point, then deepen one unresolved failure window at a time.

## Alternative Starting Drill: Durable Export Generation

> A background service generates large account exports. Jobs may run for minutes, deployments may terminate workers, and two workers must not publish conflicting results. Design how workers claim, extend, complete, retry, and recover these jobs.

Use this non-AI version when provider idempotency would distract from the core ownership problem.

## Topic Boundary

Use `api-contract-design.md` when the main question is how clients create, retry, and observe an operation. Use this drill when the operation has already been accepted and the main question is how backend workers execute it safely.

## Adaptive Follow-up Ladder

Choose only the next unresolved issue.

1. **State model:** Ask which states are durable and which transitions are legal.
2. **Atomic claim:** Ask how concurrent workers ensure that only one owns a queued job.
3. **Pre-call crash:** Ask what happens when a worker claims a job and dies before contacting the provider.
4. **Lost versus slow:** Ask how recovery distinguishes a dead worker from a legitimately long-running job.
5. **Lease renewal:** Ask how lease duration and heartbeat frequency relate to expected processing time.
6. **Stale worker:** Ask what prevents an original worker from writing after its lease expires and another worker takes ownership.
7. **Provider completion gap:** Ask what happens when the provider completes but the worker dies before saving the result.
8. **Provider reconciliation:** Ask how recovery handles provider states of absent, in progress, completed, and permanently failed.
9. **Retry policy:** Ask which failures are retryable and how attempts, timeouts, backoff, jitter, and limits are represented.
10. **Terminal recovery:** Ask what happens after automated retries are exhausted.
11. **Safe shutdown:** Ask how deployments drain workers or allow leases to expire without corrupting state.
12. **Backpressure:** Ask how the system behaves when queued work grows faster than workers can process it.
13. **Operations:** Ask how the team detects and repairs jobs that stop progressing.

## Strong Signals

Look for workload-appropriate decisions rather than a mandatory technology list.

- Define a small durable state machine such as `queued`, `processing`, `succeeded`, and `failed`, with explicit transition ownership.
- Atomically claim work with a conditional update, row lock, compare-and-set, or queue visibility mechanism; do not use check-then-update.
- Store claim ownership separately from business output, commonly with `worker_id`, `lease_expires_at`, `attempt_count`, and a claim token or lease version.
- Use an explicit lease expiry and heartbeat instead of treating an old `updated_at` value as proof that a worker is dead.
- Keep the external provider call outside the database transaction.
- Reclaim expired work with an atomic transition and increment the claim or lease version.
- Fence completion writes by verifying the current claim token or lease version so a stale worker cannot overwrite a newer owner.
- Reuse a stable provider idempotency key or provider request identifier across recovery attempts.
- Distinguish undispatched local work from an uncertain external execution.
- Reconcile provider outcomes explicitly: persist completed output, reschedule in-progress work, safely retry an absent request, and record permanent failure.
- State that the cross-system guarantee is normally at-least-once processing with controlled duplicate effects, not exactly-once execution.
- Bound retries with per-attempt timeouts, exponential backoff with jitter, `next_retry_at`, and a terminal path.
- Make terminal failure recoverable through manual review, replay, or a product fallback without silently dropping the original request.
- Monitor oldest queued age, expired leases, processing duration, retry rate, terminal failures, provider latency, and recovery success.

## Weak or Risky Signals

Probe further when the answer:

- Uses in-memory worker state as the only record of progress.
- Selects a queued row and updates it later without atomic ownership enforcement.
- Uses `updated_at` alone to decide that a worker is dead.
- Sets `processing` with no lease expiry or recovery mechanism.
- Lets any worker complete a job without verifying current ownership.
- Holds a database transaction open while waiting for the provider.
- Treats every queued job as though the provider may already have executed it.
- Retries a provider call with a fresh key after an ambiguous timeout.
- Retries indefinitely or gives every failure the same policy.
- Claims exactly-once behavior without closing the provider-completion and stale-worker windows.
- Adds a workflow engine, queue, or outbox without a workload or reliability reason.
- Has no alert or repair path for accepted jobs that never reach a terminal state.

## Model Answer Outline

Use this only after evaluating the candidate's answer. Produce the stronger answer in first person and label workload-dependent choices as assumptions.

1. Define durable job states, legal transitions, and the owner of each transition.
2. Explain atomic claim and the fields that represent execution ownership.
3. Define lease expiry, heartbeat, takeover, and fenced completion writes.
4. Walk through crashes before the provider call, during the call, and after provider completion.
5. Define the stable provider key and outcome-based reconciliation behavior.
6. Classify retryable and permanent failures with bounded scheduling policy.
7. State the achievable processing guarantee and remaining duplicate risks.
8. Explain safe deployment, backpressure, observability, and manual repair.

## Calibration

For a small project, accept a database-backed job table plus periodic workers when atomic claim, lease recovery, bounded retries, and monitoring meet the reliability target. For higher throughput or isolation requirements, ask the candidate to compare database polling, a managed queue, and a workflow engine, then justify the added operational cost.
