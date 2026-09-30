# Engineering Lifecycle Learning and Evidence Plan

Use this reference when the user asks for an overall learning plan, gap summary, sequencing, or readiness update across SDLC, testing, CI/CD, DevOps, production operations, containers, and Kubernetes. Read individual lifecycle references only when the selected work needs their detail.

## Current Calibration

Joseph already has:

- professional end-to-end product delivery, cross-functional planning, QA coordination, feature-switch, experimentation, release-monitoring, and production-debugging evidence
- project-level API, database, authorization, testing, containerization, CI/CD, Cloud Run deployment, migration, promotion, rollback, and operational-rehearsal evidence
- assessed practice in API contracts, concurrency, async recovery, RLS, structured AI output, and schema tradeoffs

The central gap is not familiarity with engineering vocabulary. It is converting dispersed experience into:

1. a coherent lifecycle story
2. measured frontend and system-quality proof
3. independently verifiable operational evidence
4. calibrated Kubernetes and platform judgment without overstating ownership

## Sequencing Rules

- Keep timed TypeScript DSA as the primary interview-filter track defined in `interview-readiness-priorities.md`.
- Keep only one engineering-lifecycle proof track active at a time.
- Extend `english-learning` or a professional case study before starting a new toy system.
- Choose work because it closes a recurring job or interview gap, not because it adds another tool name.
- Capture evidence as the work is completed. A plan, document, diagram, or unexecuted workflow is preparation material only.

## Priority Outcomes

### Outcome 1: One end-to-end engineering case study

Build a concise case study covering:

- user and business outcome
- requirements, constraints, and highest-risk failure modes
- architecture and data/API boundaries
- implementation and review decisions
- risk-based test strategy
- CI/CD and migration order
- rollout, verification, and recovery
- technical and product signals
- result, limitation, and retrospective

Preferred source: a professional Houzz product story for product delivery, paired with clearly labeled `english-learning` material when deeper backend operations are needed.

**Completion evidence:** a 5-minute spoken version, a 15-minute deep dive, a diagram, and defensible answers to one failure, rollback, security, testing, and observability follow-up.

### Outcome 2: Frontend-to-backend quality strategy

Add one critical browser flow to `english-learning` with:

- loading, empty, success, error, and recovery behavior
- authentication and authorization denial
- component or browser accessibility checks
- API/database integration coverage
- concurrent or stale-write behavior where relevant
- deployment smoke verification

**Completion evidence:** risk-to-test mapping, CI result, failure screenshots or logs, and an explanation of what is deliberately not tested at E2E level.

### Outcome 3: Close the operational proof loop

Complete the currently documented gaps:

- response-ID correlation
- end-to-end alert delivery
- independent runtime identity/IAM evidence
- isolated backup restore and reconciliation
- one incident exercise

**Completion evidence:** sanitized logs/dashboard, delivered alert, role/identity record, restore checklist and reconciliation result, incident timeline, recovery verification, and follow-up actions.

### Outcome 4: Defend the release system

Document the actual pipeline from source change to running revision:

- required source and test checks
- artifact identity and provenance
- workload identity and secrets
- migration compatibility and ordering
- candidate deployment and authenticated smoke
- promotion criteria
- rollback versus roll-forward decision
- post-deployment technical and product checks

**Completion evidence:** pipeline diagram plus one successful and one intentionally failed release exercise.

### Outcome 5: Kubernetes comparison literacy

First demonstrate conceptual judgment:

- Pod, Deployment, Service, Ingress/Gateway
- configuration, identity, probes, resources, autoscaling, and rollout
- ephemeral versus durable state
- Cloud Run versus Kubernetes for the current workload
- operational cost and migration threshold

Complete a bounded lab only if target roles repeatedly require Kubernetes.

**Completion evidence:** architecture comparison and a spoken failure walkthrough. Optional lab evidence may show rollout, failed readiness, rollback, resource settings, and logs, but must remain labeled as lab experience.

## Consolidated Learning Backlog

### High priority now

- Risk-based testing across unit, component, integration, contract, E2E, negative, smoke, and production validation.
- Browser E2E and accessibility proof for one polished product flow.
- CI/CD artifact, identity, migration, candidate verification, promotion, and recovery reasoning.
- Observability correlation, actionable alerting, restore verification, and incident response.
- A coherent SDLC case study that connects product outcome to production learning.

### Medium priority next

- SLI, SLO, error-budget, DORA, toil, and blameless postmortem reasoning.
- Measured load/concurrency testing, capacity limits, backpressure, and graceful degradation.
- Expand-and-contract migration across overlapping application versions.
- Kubernetes probes, requests/limits, autoscaling, RBAC, networking, rollout, and Cloud Run comparison.
- Flaky-test governance and pipeline-health measurement.

### Role-triggered, not default

- Helm or Kustomize, cluster administration, CNI/CSI, service mesh, operators, multi-cluster systems.
- Advanced supply-chain security, artifact signing, SBOM enforcement, and policy as code.
- Chaos engineering, multi-region failover, formal capacity programs, and organization-wide platform design.
- Consumer-driven contract infrastructure or large-scale performance environments.

## Readiness Upgrade Rules

| Area | Current safe calibration | Evidence needed to upgrade |
| --- | --- | --- |
| SDLC / product delivery | Strong professional base; story is dispersed | Coherent case study with risk, rollout, observation, and retrospective |
| Testing strategy | Good backend/negative-test evidence; frontend/system coverage uneven | Browser flow, accessibility, risk map, CI evidence, and measured reliability or performance exercise |
| CI/CD and release | Good project implementation plus professional collaboration | Independently captured pipeline, identity, migration, failed-release, and recovery evidence |
| DevOps | Good product-level collaboration and automation | Measured toil or feedback improvement, SLI/SLO decision, and incident/postmortem evidence |
| Production operations | Good debugging and release-monitoring literacy | Alert delivery, restore, incident, correlation, scaling, and sustained ownership evidence |
| Containers / Cloud Run | Good project-level implementation | Independent runtime/security/operational evidence and measured platform decisions |
| Kubernetes | Conceptual/collaborative familiarity | Role-driven bounded lab for product roles; sustained cluster ownership for platform roles |

Do not upgrade professional experience from project or lab completion. Upgrade interview readiness only after Joseph can explain the work without generated notes and defend realistic follow-ups.

## Recommended Review Loop

After each completed outcome:

1. Record the evidence level and links in the candidate or project ledger.
2. Run one timed interview explanation without notes.
3. Record strengths, unresolved gaps, and follow-up answers.
4. Update `candidate-profile.md` only when the evidence is implemented, verified, or assessed.
5. Re-rank the backlog from actual interview feedback and recurring target-role requirements.
