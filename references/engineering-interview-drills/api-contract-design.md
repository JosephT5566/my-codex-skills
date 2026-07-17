# API Contract Design Drills

Use this reference to run an adaptive API contract interview. Do not expose the rubric or follow-up ladder before the candidate answers. Ask exactly one question at a time, skip concerns the candidate already addressed, and stop deepening once they have defended the important tradeoffs.

## Starting Drill: AI Receipt Parsing

Use this scenario for expense-tracking or AI workflow practice:

> Your expense app exposes an API that uploads a receipt and uses AI to produce an expense draft. Parsing can take several seconds, some fields may be unrecognized, and a client may retry after a timeout. Design the API contract and define the semantics of success, partial success, and failure.

Accept another project-grounded async operation when it better matches the candidate's experience. Preserve the same failure properties rather than forcing the receipt domain.

## Adaptive Follow-up Ladder

Choose only the next unresolved issue. Do not mechanically ask every question.

1. **Representation:** Probe how the response represents an unrecognized field and whether partial extraction is request failure.
2. **Retry semantics:** Ask what happens when a client retries with the same idempotency key before the first request completes.
3. **Key reuse:** Ask how the API handles the same key with a different request payload.
4. **Concurrent requests:** Ask how multiple server instances ensure that simultaneous requests create only one job.
5. **Dispatch failure:** Ask what happens when the database transaction commits but the service crashes before a worker receives the job.
6. **Worker recovery:** Ask how the system distinguishes a lost worker from a job that is still legitimately processing.
7. **Provider boundary:** Ask what happens when the provider completes the call but the worker crashes before saving the result.
8. **Permanent failure:** Ask how the status endpoint tells a client whether retry is appropriate without leaking provider internals.

## Strong Signals

Look for decisions appropriate to the stated workload, not a mandatory component list.

- Model long-running parsing as a job resource, commonly returning `202 Accepted` and a stable job identifier.
- Represent unknown JSON values with an omitted field or `null`, optionally paired with field status or confidence; do not use `undefined` in JSON.
- Treat usable partial extraction as a completed job with field-level uncertainty when product semantics allow it.
- Separate HTTP status from stable application error codes and safe client-facing messages.
- Keep server-side prompts controlled and versioned; accept structured hints instead of an unrestricted raw prompt unless customization is a stated requirement.
- Scope idempotency by authenticated principal and operation, compare a canonical request hash, define retention, and return the same job while it is pending.
- Reject reuse of the same key for a different payload, commonly as `409 Conflict`.
- Use a database unique constraint as the concurrency arbiter. Create the idempotency record and job atomically, then perform slow external work after commit.
- Use durable job state, atomic claim, leases, retry limits, backoff, and a periodic sweeper or equivalent recovery mechanism.
- State that cross-system execution is normally at-least-once. Prefer provider idempotency or request lookup; otherwise bound duplicate cost and provide reconciliation or manual review.
- Protect the final expense-creation side effect separately so duplicate parsing cannot create duplicate expenses.

## Weak or Risky Signals

Probe further when the answer:

- Names REST and JSON without defining resources, state transitions, or response semantics.
- Uses `undefined` as a JSON value or treats every missing field as an HTTP failure.
- Maps every timeout to `408 Request Timeout` without identifying which party timed out.
- Performs a check-then-insert without a unique constraint.
- Returns a previous result for the same key without verifying that the payload matches.
- Holds a database transaction open during the external AI call.
- Recovers jobs only when the service restarts, with no handling for stuck work during normal operation.
- Claims exactly-once behavior across the database and provider without explaining the failure window.
- Retries indefinitely or ignores duplicate provider cost.
- Exposes provider stack traces, model details, credentials, or raw internal errors to clients.

## Model Answer Outline

Use this only after evaluating the candidate's answer. Produce the model answer in first person and label workload-dependent choices as assumptions.

1. Define a create-job endpoint and status endpoint, including request, response, and state transitions.
2. Explain field-level partial success and JSON nullability.
3. Define safe validation, authorization, conflict, and job-failure semantics.
4. Define idempotency scope, request fingerprint, replay behavior, and expiration.
5. Explain the transaction boundary and database concurrency mechanism.
6. Explain durable dispatch, worker claim, lease expiry, retry, and terminal failure.
7. Explain the provider failure window, achievable guarantee, reconciliation, and cost controls.

## Calibration

For a small side project, accept a database-backed job table and periodic worker when it meets the stated reliability target. Do not require a queue, outbox, or distributed workflow engine without a workload-based reason. For higher reliability, ask the candidate to compare database polling, transactional outbox delivery, and a managed queue, then defend one choice.
