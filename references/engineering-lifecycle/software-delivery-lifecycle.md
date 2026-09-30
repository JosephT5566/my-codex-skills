# Software Delivery Lifecycle

Use this reference when a reviewed role or interview asks about SDLC, end-to-end delivery, feature ownership, engineering process, release quality, or how a product idea reaches production. Keep the discussion product-oriented and evidence-calibrated. Do not reduce SDLC to a fixed waterfall checklist.

## Core Mental Model

Treat software delivery as a feedback loop:

```text
Problem and outcome
  -> requirements and risks
  -> design and delivery plan
  -> implementation and review
  -> automated and exploratory verification
  -> controlled release
  -> production observation
  -> learning, repair, and iteration
```

The exact ceremonies and artifacts depend on risk. A small reversible UI change does not need the same process as an authorization change, destructive migration, payment flow, or cross-team platform dependency.

## Lifecycle Decisions

### 1. Problem and outcome

- Identify the user or business problem before selecting technology.
- Define success signals and guardrails. Separate product outcomes from delivery outputs.
- Clarify ownership, dependencies, constraints, and what is deliberately out of scope.

### 2. Requirements and risks

- Cover normal behavior plus loading, empty, error, authorization, concurrency, migration, and recovery paths as relevant.
- Identify privacy, security, accessibility, performance, data-integrity, and operational risks early.
- Prefer small, reversible milestones when requirements are uncertain.

### 3. Design and delivery plan

- Define component and service boundaries, API and data contracts, state transitions, and failure semantics.
- Record important tradeoffs in a design document or ADR when future maintainers need the reasoning.
- Plan compatibility, feature switches, migration order, validation, ownership, and rollback before implementation.

### 4. Implementation and review

- Divide work into changes that are independently reviewable and, where possible, independently releasable.
- Use code review to examine correctness, maintainability, security, testing, operational behavior, and not only style.
- Keep server-side identity, authorization, validation, and durable invariants outside editable client state.

### 5. Verification

- Choose tests according to the risk and the layer that owns the guarantee.
- Combine automated checks with exploratory QA for ambiguous product behavior and integration risk.
- Test rollback or recovery behavior when a change affects persistent data, authentication, or external providers.

### 6. Controlled release

- Build a reproducible artifact and promote it through appropriate checks.
- Use feature switches, staged rollout, candidate verification, smoke tests, or progressive delivery when the blast radius justifies them.
- Distinguish application rollback from data rollback. A schema change may require expand-and-contract compatibility rather than reversing production data.

### 7. Production observation and learning

- Define logs, metrics, traces, dashboards, alerts, product analytics, and correlation identifiers according to the failure modes.
- Check technical health and intended product outcomes after release.
- Feed incidents, support findings, experiment results, and user behavior back into prioritization and design.

## Joseph Evidence Map

### Demonstrated professionally

- Clarified ambiguous requirements with PM, design, backend, platform, personalization, and data partners.
- Wrote design documentation, divided work into Jira tasks, reviewed code, coordinated QA and releases, and delivered cross-team product changes.
- Used feature switches, QA guides, bug bashes, A/B tests, and release monitoring.
- Used Coralogix, Amplitude, and Redash for production debugging, product analysis, dashboards, and post-release validation.
- Delivered marketplace search/browse, CMS-driven product infrastructure, campaign experiences, GraphQL integration, and measurable experiments.

### Implemented or rehearsed in projects

- Built typed frontend/API/data flows with authentication, authorization, PostgreSQL constraints, migrations, transactions, and idempotency.
- Implemented controlled import and reconciliation, containerization, health checks, candidate verification, promotion, and schema-compatible rollback in `english-learning`.
- Used GitHub Actions for automated validation, deployment, scheduled workflows, and artifact handling.
- Implemented security-focused negative tests and structured-output validation in `google-ai-gcf`.

### Assessed in practice

- Practiced API contracts, async failure recovery, transactional concurrency, RLS, structured AI output, and PostgreSQL schema tradeoffs.
- Treat mixed drill results as readiness evidence, not shipped-system evidence.

### Current evidence boundary

- Do not claim professional ownership of a production backend service, sustained on-call rotation, large-scale incident response, or infrastructure platform.
- Project deployment and release rehearsal support product-level operational judgment, not production-scale reliability claims.
- Kubernetes exposure supports collaboration and conceptual comparison, not cluster administration ownership.

## Reusable Interview Answer

Use this structure for a 90-second answer:

1. Start with the product outcome and risk, not a process label.
2. Walk through requirements, design, implementation, verification, release, and production feedback.
3. Name one or two safety mechanisms appropriate to the example.
4. Explain how success and failure were observed after release.
5. State the evidence level and one tradeoff or improvement.

Example outline:

> I treat SDLC as a feedback loop rather than a handoff sequence. I first align on the user outcome, success metric, dependencies, and highest-risk failure modes. I then define the UI, API, data, and rollout boundaries, split the work into reviewable changes, and choose tests based on which layer owns each guarantee. Before release I plan compatibility, feature switches, verification, and recovery. After release I use technical and product signals to confirm health and feed what we learn into the next iteration. At Houzz I used this approach across cross-functional product delivery, QA coordination, feature switches, experiments, and release monitoring; my deeper backend deployment and rollback examples come from verified personal projects rather than professional service ownership.

## Learning and Proof Backlog

### High priority

- Produce one concise professional case study covering problem, requirements, design choices, test strategy, rollout, monitoring, outcome, and retrospective.
- Practice explaining how process changes with risk: ordinary UI iteration versus auth, migration, external provider, or high-traffic release.
- Add an explicit incident or release-retrospective example showing detection, mitigation, root cause, follow-up action, and learning.

### Medium priority

- Learn lightweight ADR structure and when a decision needs one.
- Practice expand-and-contract migration reasoning and the distinction between rollback and roll-forward repair.
- Learn how SLOs, error budgets, change-failure rate, lead time, and recovery time influence delivery decisions.

### Evidence to capture

- A design or architecture note written before implementation.
- Test and rollout plans tied to named risks.
- Deployment verification output and rollback or recovery evidence.
- A short retrospective that changes a later engineering decision.

## Readiness Standard

Mark this area `Strong` only when Joseph can tell a coherent professional story across most of the lifecycle and defend why each control existed. Mark it `Good` when the model is sound but operations or incident ownership relies mainly on project evidence. Do not upgrade readiness because this reference exists.
