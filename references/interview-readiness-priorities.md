# Interview Readiness Priorities

Use this reference when choosing training work, interview drills, or portfolio proof. The ordering is
optimized for Joseph's current target: frontend-strong Product Engineer, Full-stack Product Engineer,
and AI Product Engineer roles at large product companies. Do not interpret the list as seven parallel
projects. Keep one primary practice track and at most one proof-building track active at a time.

## Priority Table

| Priority | Expertise | Why it matters | Proof to build |
| --- | --- | --- | --- |
| 1 | Data structures and algorithms | Often the first major Google/Microsoft interview filter, including for frontend roles. Current project depth cannot compensate for failing this screen. | Solve 40-60 curated medium problems in TypeScript; practice explaining complexity, invariants, edge cases, and tradeoffs without generated notes. |
| 2 | Frontend architecture and performance | This is Joseph's strongest route into large product companies and the shortest path from existing professional experience to senior-level evidence. | Establish performance budgets, bundle analysis, Core Web Vitals evidence, virtualization or large-list behavior, caching decisions, accessibility checks, and Playwright coverage on one polished product flow. |
| 3 | Product-oriented system design | Senior frontend, product, and full-stack interviews require scope beyond an individual UI feature. | Practice designing search, CMS, experimentation, realtime dashboards, notifications, and AI-assisted workflows, including requirements, APIs, data, failure behavior, security, observability, and evolution under load. |
| 4 | Production backend ownership | This broadens the role pool without discarding the frontend advantage. The English Learning project now supports a credible deployed-project story, but not professional production-scale ownership. | Extend one service with a measured need for durable async work, then demonstrate idempotency, bounded retries, recovery, observability, deployment, rollback, and an incident exercise. Do not add a queue merely to check a box. |
| 5 | Behavioral and leadership communication | Large companies evaluate influence, ambiguity, collaboration, judgment, and measurable impact as heavily as implementation detail. | Prepare 6-8 reusable STAR/CAR stories covering conflict, failure, leadership without authority, ambiguity, debugging, tradeoffs, delivery, and product impact. Mark which claims are professional versus project evidence. |
| 6 | Cloud and operational fundamentals | End-to-end ownership requires operational literacy, but deep infrastructure specialization is unnecessary for the target roles. | Be able to defend the current Cloud Run/Neon design, Docker image, CI/CD, secrets, health checks, metrics, alerts, backup/restore limits, rollout, and rollback; learn Kubernetes concepts well enough to compare, not administer, a cluster. |
| 7 | Applied AI product engineering | This is a useful differentiator for product-facing AI teams when paired with safe execution and measured quality. | Demonstrate structured output, permission-aware retrieval/tool calling, human approval, evaluation, tracing, failure handling, and latency/cost measurement. Keep generated content as a validated editable draft, never a directly confirmed learning card. |

## How to Execute the Priorities

### Primary weekly track: DSA

- Use TypeScript unless a target interview explicitly requires another language.
- Prefer a curated pattern set over random volume: arrays/strings, hash maps, two pointers, sliding
  window, stacks/queues, binary search, linked lists, trees, heaps, graphs, intervals, backtracking,
  and dynamic programming.
- Count a problem as retained only after a timed re-solve and a spoken explanation of correctness and
  time/space complexity. Forty well-retained mediums are stronger evidence than sixty copied solutions.
- Track first-attempt result, hint level, error pattern, re-solve dates, and explanation quality.

### Proof-building track: frontend first, then selective backend/AI depth

Use one end-to-end English Learning flow as the evidence surface rather than starting another toy
application. A strong sequence is:

1. Measure a user-critical frontend flow and set a budget before optimizing it.
2. Add browser coverage for loading, empty, error, authorization, and recovery states.
3. Produce a short architecture explanation connecting the Svelte UI, authenticated API, PostgreSQL
   invariants, deployment boundary, and monitoring.
4. Finish the frozen semantic-search evaluation before making broad RAG-quality claims.
5. Add durable async processing only when observed AI generation latency or failure behavior justifies
   it; define recovery and human approval before choosing infrastructure.

## Evidence Gates

Use the following labels consistently:

- **Practiced:** completed under interview conditions and explainable without notes.
- **Implemented in a project:** code and relevant tests exist.
- **Verified in CI:** the linked revision passed the relevant automated checks.
- **Deployed and verified:** the behavior was exercised in the deployed personal application.
- **Demonstrated professionally:** supported by actual shipped professional work and defensible impact.

Do not upgrade evidence because a plan, rubric, dependency, or architecture diagram exists. Never turn
personal-project traffic, latency, reliability, or operator reports into professional production claims.

## Suggested Cadence

- Three DSA sessions per week: one new pattern/problem, one timed mixed set, and one spaced re-solve.
- One system-design or project-deep-dive session per week, alternating frontend/product design and
  backend/AI ownership.
- One behavioral story rehearsal per week until the 6-8 story bank is concise and adaptable.
- One monthly portfolio checkpoint: record only new implemented and verified proof, then revise the
  next four weeks based on actual interview feedback and recurring job requirements.

## Current Project Mapping

- Priorities 4 and 6 already have meaningful project evidence in `english-learning`: FastAPI and
  PostgreSQL ownership boundaries, transactions and idempotency, containerization, Cloud Run/Neon
  deployment, candidate promotion, schema-compatible rollback, health checks, and operational drills.
  Remaining limits include independently captured IAM/role evidence, full restored-data
  reconciliation, and complete alert-delivery evidence.
- Priority 7 has implemented and deployed owner-safe semantic retrieval plus a frozen evaluation
  boundary. Treat retrieval quality as unproven until the Issue #41 provider evaluation and sanitized
  production inspection support a go/iterate/stop decision. The later AI authoring/tutor workflow is
  planned, not implemented.
- Priority 2 has strong professional product-frontend evidence, but the shared references do not yet
  contain a focused, measured performance case study. Build one rather than listing tools without
  results.
- Priority 1 remains the highest interview-risk reduction because repository work does not prove
  timed algorithm performance.
