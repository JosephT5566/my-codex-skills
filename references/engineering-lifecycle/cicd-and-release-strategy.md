# CI/CD and Release Strategy

Use this reference when a reviewed role or interview asks about CI/CD, GitHub Actions, build pipelines, deployment automation, release strategies, GitOps, feature flags, database migration safety, rollback, or developer productivity. Keep CI, delivery, deployment, and production verification distinct.

## Core Mental Model

- **Continuous integration:** integrate small changes frequently and obtain fast, trustworthy feedback before they accumulate merge risk.
- **Continuous delivery:** keep a validated, versioned artifact ready to release through a repeatable process.
- **Continuous deployment:** automatically release every change that passes the required controls. This is optional and risk-dependent.

A green pipeline proves only that the configured checks passed. It does not prove that the release is healthy or that the product outcome improved.

## Reference Pipeline

```text
Change
  -> source checks
  -> automated tests
  -> build once
  -> security and artifact checks
  -> publish immutable artifact
  -> deploy candidate
  -> health and smoke verification
  -> promote or progressively expose
  -> observe technical and product signals
  -> continue, roll back, or roll forward
```

## Design Principles

### Fast and trustworthy integration

- Put the fastest high-signal checks early: formatting, lint, types, focused tests, and build validation.
- Keep the main branch releasable; prefer small changes and short-lived branches unless the team has a justified alternative.
- Use required checks and review appropriate to the risk without turning every release into a manual queue.
- Treat flaky pipelines, slow feedback, and unclear failures as developer-productivity defects.

### Build once, promote the same artifact

- Produce a traceable artifact tied to source revision, build metadata, and dependency versions.
- Avoid rebuilding different binaries for staging and production. Move environment-specific configuration and secrets outside the artifact.
- Retain enough provenance to identify what is running and reproduce or investigate it.

### Protect credentials and dependencies

- Prefer short-lived workload identity or federation over long-lived static credentials.
- Scope permissions to the workflow and environment; protect production environments with explicit policy where appropriate.
- Scan dependencies and images according to risk, but define ownership and remediation rather than collecting unactioned findings.
- Consider artifact signing, provenance, SBOMs, and protected runners when supply-chain risk or target roles justify them.

### Separate deploy from release

- A deployment makes code available; a release exposes behavior to users.
- Feature flags, percentage rollout, allowlists, shadow traffic, or canaries can separate these moments.
- Every progressive mechanism needs ownership, cleanup, success criteria, and a stop or rollback rule.

### Treat data changes as compatibility work

- Use expand-and-contract migrations when old and new application versions may overlap.
- Separate schema introduction, backfill, application cutover, enforcement, and cleanup when necessary.
- Validate data before promotion. Do not assume application rollback can safely undo a destructive migration.

### Verify after deployment

- Check startup, health, dependencies, authentication, and one critical user path.
- Compare error rate, latency, saturation, and selected product guardrails against an explicit baseline.
- Decide in advance what triggers continuation, pause, rollback, or roll-forward repair.

## Release Strategies and Tradeoffs

| Strategy | Useful when | Main cost or risk |
| --- | --- | --- |
| Recreate / simple replacement | Small low-risk services with tolerated interruption | Downtime and abrupt failure exposure |
| Rolling update | Ordinary stateless workloads with compatible versions | Mixed-version compatibility and slower rollback |
| Blue/green | Fast environment switch and easy application rollback matter | Duplicate capacity and data compatibility still remain |
| Canary / percentage rollout | Production behavior must be measured before broad exposure | Routing, analysis, and operational complexity |
| Feature flag | Product exposure should be independent from deployment | Stale flags, branching complexity, and incomplete cleanup |
| Candidate then promotion | One managed revision can be verified before traffic | Requires representative smoke tests and clear promotion evidence |

Choose the simplest strategy that meets the blast-radius, recovery-time, and validation needs.

## Joseph Evidence Map

### Demonstrated professionally

- Used GitHub-based CI/CD and GitOps workflows earlier in his career.
- Coordinated releases using feature switches, QA planning, bug bashes, reviews, and post-release monitoring.
- Collaborated with platform engineers and debugged behavior across frontend, API, logs, and analytics.

### Implemented in projects

- Built GitHub Actions workflows for validation, previews, deployment, scheduled automation, resume generation, artifact retention, and Google Drive delivery.
- Operates a self-hosted runner for controlled Codex workflow automation.
- `english-learning` includes non-root containerization, Cloud Run/Neon deployment, workload-identity workflows, zero-traffic candidate verification, authenticated smoke tests, promotion, and schema-compatible rollback.
- The expense application uses GitHub Actions for automated deployment and preview validation.

### Current evidence boundary

- Do not claim ownership of an organization-wide delivery platform, multi-cluster GitOps system, or high-frequency production deployment program.
- Supply-chain controls, artifact signing, SBOM enforcement, sophisticated canary analysis, and sustained DORA measurement are not established evidence.
- Some deployed project results are operator-reported; independent capture of IAM/runtime roles and complete alert delivery remains incomplete.

## Reusable Interview Answer

Use this structure:

1. State the delivery goal and risk profile.
2. Describe pre-merge feedback and required quality gates.
3. Explain build-once artifact provenance and credential boundaries.
4. Explain candidate deployment, migration compatibility, release control, and verification.
5. Define recovery and production signals.
6. Give a concrete example and evidence boundary.

Example outline:

> I see CI/CD as a risk-reduction and feedback system. CI should give fast, deterministic feedback on each small change, and a successful build should create one traceable artifact. Delivery then promotes that artifact through environment-specific configuration and least-privilege credentials. I separate deployment from user exposure, use a release method proportional to blast radius, and verify health plus product guardrails after deployment. Database changes need compatibility planning because rolling application code back does not automatically reverse data. In `english-learning` I implemented container build, candidate verification, authenticated smoke tests, promotion, and schema-compatible rollback on Cloud Run and Neon. That is solid project-level release evidence, but not a claim of owning a large enterprise delivery platform.

## Learning and Proof Backlog

### High priority

- Draw and explain the current `english-learning` pipeline from commit to running revision, including identities, secrets, artifact, migration order, smoke tests, promotion, and recovery.
- Capture independent evidence for runtime identity/IAM boundaries, alert delivery, deployed revision identity, and rollback or roll-forward results.
- Practice an expand-and-contract migration across two simultaneously running application versions.

### Medium priority

- Add pipeline health measurements: duration, failure class, flaky rate, deployment success, recovery time, and change-failure examples.
- Learn trunk-based development, environment promotion, protected environments, and when manual approval adds real risk control.
- Learn canary analysis, blue/green, and feature-flag lifecycle through one scenario rather than tool syntax.
- Add dependency and image scanning with a documented remediation policy if a target role values supply-chain security.

### Lower priority unless role-driven

- Artifact signing, SLSA-style provenance, SBOM enforcement, multi-cluster GitOps, advanced policy-as-code, and organization-wide developer platform design.

### Evidence to capture

- Pipeline diagram plus a real workflow run linked to source and artifact.
- Candidate verification and promotion logs.
- Migration compatibility test with old and new versions.
- A failed-release exercise showing diagnosis and a bounded recovery decision.

## Readiness Standard

Use `Strong` for product-facing CI/CD discussion when Joseph can defend the current pipeline, compatibility, verification, and recovery. Use `Good` for developer-platform roles until he can show broader pipeline ownership, supply-chain controls, and measured organization-level outcomes.
