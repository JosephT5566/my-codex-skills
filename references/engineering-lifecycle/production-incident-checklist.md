# Production Incident Checklist

Coaching guidance for incident-response practice and interview answers. This is learning material, not
evidence of Joseph's experience; use `references/candidate-profile.md` and the evidence map in
`production-operations-and-observability.md` for calibration. Added 2026-11-03 from quiz question 7.

## 1. Discovery and triage (first 5 minutes)

- Quantify impact: which feature, which users, start time, and how much error rate or latency changed.
- Correlate with the timeline: recent deploys, feature flags, config, data changes, or third-party
  services.
- Compare traffic splits: new versus old version, region, browser, or device.

## 2. Stop the bleeding (before root cause)

- Use the fastest reversible action: turn off the feature flag, roll back, degrade, or rate limit.
- Confirm metrics return to baseline before continuing the investigation.
- Notify stakeholders: current status, impact, and next update time.

## 3. Root cause

- Work outside-in: error message, page, component, API, database.
- Use data over guesses: error and latency charts, traces, slow query logs, version diff.
- Test one hypothesis at a time and reproduce with the smallest possible steps.
- Common backend and database clues: missing index, heavier query, connection pool exhaustion, cache
  invalidation, slow external service.

## 4. Fix and reopen

- Ship the fix with tests that cover this failure.
- Roll out gradually (1, 10, 50, 100 percent), check metrics at each step, and keep rollback available.
- Keep monitoring the same error and the key metrics for a while after full rollout.

## 5. Blameless postmortem

- Ask why it was not detected earlier: missing integration tests, performance tests, latency or
  error-rate alerts, or too little data volume in pre-production.
- Improve detection, not only the bug.
- Record the timeline, root cause, impact, and action items with owners.

## Interview one-liner

> I first quantify impact and compare it with recent changes, then stop the bleeding with a feature flag
> or rollback. I compare old and new version metrics and trace through the API and database to find the
> root cause. After the fix I roll out gradually and add alerts and tests so the next one is caught
> earlier.
