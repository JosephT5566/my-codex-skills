# Risk-Based Testing Strategy

Use this reference when a reviewed role or interview asks about test strategy, unit/integration/E2E testing, quality engineering, test automation, coverage, flaky tests, release confidence, or shift-left quality. Route database authorization, concurrency, or AI-specific details to the smallest matching engineering drill after establishing the overall strategy.

## Core Mental Model

Testing is a risk-control system, not a contest to maximize test count or coverage. Start with:

1. What failure matters?
2. Which layer owns the guarantee?
3. What is the cheapest reliable test that can detect it?
4. What can only be learned in an integrated, deployed, or production-like environment?

Prefer many fast deterministic checks near the owning logic, fewer integration tests at real boundaries, and a small set of high-value end-to-end paths. The shape may resemble a pyramid or testing trophy, but the architecture and risk decide the final mix.

## Test Layers and Responsibilities

| Layer | Primary responsibility | Common misuse |
| --- | --- | --- |
| Static checks | Types, linting, formatting, dependency and policy checks | Treating compilation as behavioral proof |
| Unit | Pure logic, parsing, validation, calculations, state transitions | Mocking so much that the test proves only the mock setup |
| Component | UI rendering, interaction, accessibility roles, local error states | Repeating implementation details instead of user-observable behavior |
| Integration | Database constraints, migrations, auth, APIs, caches, queues, provider adapters | Replacing real boundary behavior with unrealistic mocks |
| Contract | Request/response schemas, compatibility, provider or consumer assumptions | Checking shape without semantics or versioning behavior |
| End-to-end | A few critical user journeys across deployed components | Using E2E for every branch and accepting slow flaky suites |
| Negative/security | Unauthorized actors, malformed input, privilege boundaries, injection, limits | Testing only expected success paths |
| Performance/reliability | Latency, throughput, resource use, contention, recovery | Running load without a target, representative data, or diagnosis plan |
| Deployment smoke | Artifact starts, dependencies connect, critical path works | Assuming smoke tests prove full correctness |
| Production validation | Real health, business outcome, regressions, unknown failure modes | Treating monitoring as a substitute for pre-release testing |

## Selection Rules

- Put durable invariants in the database and test them through the same transaction and role boundaries used by the application.
- Test authorization with an actor-by-action matrix, including denial cases, multi-membership users, and elevated backend paths.
- Keep external provider tests in layers: deterministic adapter tests, contract or schema tests, a small real-provider smoke, and controlled production observation.
- Test migrations in both directions when reversal is supported; otherwise test compatibility and forward repair.
- Use fixtures or factories that expose important variation without hiding the scenario.
- Use mocks for expensive, unstable, or exceptional dependencies only when the mock preserves the contract being tested.
- Treat accessibility, browser behavior, network failure, loading, empty, stale, and recovery states as product correctness.

## Coverage, Flakiness, and Maintenance

- Coverage shows executed code, not confidence, correctness, or assertion quality.
- Set coverage targets only when they improve behavior; prioritize critical paths, invariants, and regression history.
- A flaky test is a reliability defect in the delivery system. Record it, identify timing/state/environment causes, repair it, and quarantine only with an owner and deadline.
- Do not normalize blind retries. A bounded rerun may collect diagnostic evidence but must not hide the original failure rate.
- Track suite duration, failure classification, flaky rate, escaped defects, and time to diagnose when those measurements change decisions.

## Joseph Evidence Map

### Demonstrated professionally

- Planned QA, wrote QA guides, coordinated bug bashes, performed code review and production debugging, and monitored releases.
- Used feature switches and product experiments to limit risk and validate behavior.
- Established Ceedling unit tests for firmware driver development earlier in his career.

### Implemented in projects

- `google-ai-gcf` documents 97 tests across structured output, ownership, file and metadata limits, invalid provider output, prompt injection, configuration injection, sanitized errors, and negative-path short-circuit behavior.
- `english-learning` includes deterministic tests for owner isolation, PostgreSQL constraints, migrations, transactions, idempotency, concurrency, rollback, and failure boundaries.
- Deployment rehearsal includes authenticated smoke tests and candidate verification.

### Current evidence boundary

- Shared references do not yet contain a polished browser-level Playwright suite or measured accessibility test story.
- There is little evidence for sustained performance/load testing, chaos testing, cross-browser strategy, mutation testing, contract-testing infrastructure, or organization-wide test governance.
- Do not infer testing depth from a raw test count. Be ready to explain which risks the tests protect.

## Reusable Interview Answer

Use this structure:

1. Name the critical failure modes and business risk.
2. Assign each guarantee to an owner: type system, frontend, API, database, provider boundary, deployment, or production monitor.
3. Select the smallest reliable test at each necessary layer.
4. Explain how real boundaries are exercised and where mocks are acceptable.
5. Cover negative paths, test data, CI execution, flakiness, and production validation.
6. Give one concrete example and an evidence boundary.

Example outline:

> I design a test strategy from failure risk rather than a fixed ratio. Pure validation and state transitions get fast unit tests; API, authentication, database constraints, and migrations need integration tests against realistic boundaries; a small number of critical user journeys get browser E2E coverage. I add negative tests for unauthorized actors and malformed inputs, then use deployment smoke tests and production signals for risks that cannot be proven locally. Coverage is a diagnostic, not the goal, and flaky tests are defects because they reduce trust in CI. My strongest recent project example is the receipt-extraction service, where tests cover structured output, ownership, input hardening, injection boundaries, and provider failure, while browser E2E and load-testing proof remain areas I am actively strengthening.

## Learning and Proof Backlog

### High priority

- Add Playwright coverage for one user-critical `english-learning` flow: loading, empty, success, authorization denial, recoverable failure, and stale or concurrent update behavior.
- Produce a one-page test strategy mapping named risks to unit, component, integration, contract, E2E, smoke, and production checks.
- Practice defending why a test belongs at one layer and what duplication is intentionally avoided.

### Medium priority

- Add accessibility checks using semantic queries plus an automated tool, followed by a small manual keyboard and screen-reader checklist.
- Run a measured concurrency or load exercise with a target, representative data, latency/error results, bottleneck analysis, and stopping condition.
- Learn consumer-driven versus provider contract testing and decide whether the current projects justify it.
- Establish a flaky-test policy with classification, ownership, quarantine criteria, and repair deadline.

### Lower priority unless a target role requires it

- Cross-browser matrix design, visual regression infrastructure, mutation testing, chaos experiments, and large-scale performance environments.

### Evidence to capture

- Test plan tied to explicit risks and requirements.
- CI output for each test layer.
- A regression prevented by a specific invariant or negative-path test.
- Before/after evidence for one flaky or slow-test improvement.

## Readiness Standard

Mark this area `Strong` when Joseph can select and defend layers for a realistic product, explain test doubles and flakiness, and anchor the answer in professional plus project evidence. Use `Good` when backend negative testing is strong but frontend E2E, accessibility, or performance proof remains incomplete.
