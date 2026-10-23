# Interview Readiness Priorities

Use this as the canonical source for Joseph's preparation priorities. His professional frontend and
product experience remains the starting point for Frontend, Product, Full-stack Product, and
product-facing AI roles. Select one primary practice focus and at most one proof-building exercise.

## Choose the immediate priority

Updated 2026-10-23 after reviewing current roles and the user's coaching request. The default next
investment is a measured frontend architecture/performance case study. Connect that work to
product-oriented system design and the ability to review, explain, and verify AI-assisted changes.

Treat interview preparation and capability evidence as separate decisions:

- When an upcoming interview includes algorithms, the user requests DSA, or the user is actively
  preparing for companies with an expected algorithm screen, make timed DSA a primary practice track.
  Confirm a specific interview's format and allowed languages when supplied material does not establish them.
- When no algorithm interview or DSA goal is identified, start with frontend architecture/performance
  and a product-system deep dive. Offer DSA as a separate interview-preparation track without making it
  an unconditional prerequisite to applying or improving the portfolio.
- An explicit target interview, user-selected topic, time constraint, or language choice overrides defaults.

The 2026-10-23 reviewed postings included frontend-anchor entry, allocation by existing strengths, and
heavy use of coding agents. These observations support practicing transferable product judgment.
They do not prove that all employers relax requirements or that AI replaces service ownership.

## Capability and proof-building priorities

| Priority | Expertise | Proof to build |
| --- | --- | --- |
| 1 | Frontend architecture and performance | Measure one critical flow. Explain state and component boundaries, cache behavior, bundle or rendering costs, accessibility, and loading/error/recovery UX. Show a justified change with comparable before/after evidence. |
| 2 | Product-oriented system design | Explain the same flow across user needs, frontend, API, data, authorization, failure handling, observability, and rollout. Compare alternatives under an explicit workload. |
| 3 | AI-assisted engineering judgment | Define requirements and acceptance criteria, bound agent tasks, review generated code, test behavior, and explain rejected alternatives. For AI product features, add structured-output validation, permissions, human review, and measured quality/latency/cost where relevant. |
| 4 | Behavioral and leadership communication | Prepare reusable stories about product impact, ambiguity, tradeoffs, collaboration, debugging, conflict, and influence. Mark professional versus project evidence. |
| 5 | Selective backend feature ownership | Use existing services to defend API contracts, relational data, authorization, transactions, idempotency, and recovery. Deepen only where a target role or observed failure justifies it. |
| 6 | Cloud and operational fundamentals | Defend the current deployment, CI/CD, secrets, health checks, observability, backup/restore limits, rollout, and rollback. Infrastructure specialization follows a role requirement. |

### DSA when an algorithm screen is a preparation goal

DSA means data structures and algorithms. TypeScript is Joseph's default because of existing fluency.
Python or another language is valid when he prefers it or a supplied interview constraint requires it.
Language choice supports clear implementation and explanation; it does not determine reasoning quality.

Use a curated pattern set: arrays/strings, hash maps, two pointers, sliding windows, stacks/queues,
binary search, linked lists, trees, heaps, graphs, intervals, backtracking, and dynamic programming.
Count a problem as retained after a timed independent re-solve and a spoken explanation of correctness
and time/space complexity. Track hints, error patterns, and re-solve dates rather than raw problem count.
Scale the plan to the interview date and diagnostic results. Do not impose a fixed quota before applying.

## One reusable proof-building exercise

Use one existing English Learning or expense-app flow rather than starting another application.
Budget about 3-4 hours for a first pass and narrow the scope if the baseline reveals substantial work.

1. Select a user-critical frontend flow and record a reproducible baseline before optimizing.
2. Identify the actual bottleneck and compare one credible alternative.
3. Make one bounded change. Verify comparable measurements and relevant loading, error, authorization,
   and recovery behavior.
4. Explain the frontend/API/data boundaries and why the change fits the product's requirements.
5. Produce a one-page case study and rehearse a five-minute explanation without generated notes.

AI can assist with implementation and investigation. Joseph owns the problem definition, acceptance
criteria, review, and interpretation of the results. A proposed improvement or one synthetic run is
not a measured production outcome.

For a deeper backend or AI interview, use the matching drill and extend the existing service only when
the requirement warrants it. Finish the frozen retrieval evaluation before claiming general retrieval
quality. Add durable async processing only after observed latency or failure behavior justifies it.

## Suggested cadence

- General product/frontend preparation: one project deep dive or proof-building session, followed by
  one short system-design or behavioral rehearsal using the same evidence.
- Algorithm-screen preparation: three DSA sessions per week, about 45 minutes each, covering a new
  pattern, a timed attempt, and a spaced re-solve. Keep at most one small portfolio exercise alongside it.
- For a specific interview, prioritize its confirmed format, expected depth, and nearest deadline.
- Review priorities after interview feedback or recurring JD requirements. A missing skill is not
  automatically the next investment with the greatest value.

## Evidence gates

- **Practiced:** completed under interview conditions and explainable without notes.
- **Implemented in a project:** code and relevant tests exist.
- **Verified in CI:** the linked revision passed the relevant automated checks.
- **Deployed and verified:** the behavior was exercised in the deployed personal application.
- **Demonstrated professionally:** supported by shipped professional work and defensible impact.

Do not upgrade evidence because a plan, rubric, dependency, architecture diagram, or generated solution
exists. Personal-project traffic, latency, reliability, and operator reports remain project evidence.

## Current project mapping

- Frontend architecture/performance has strong professional product experience behind it, but the
  shared references do not yet contain a focused measured case study. Build that proof first.
- `english-learning` already supports project-level FastAPI/PostgreSQL boundaries, transactions,
  idempotency, containerization, Cloud Run/Neon releases, rollback, health checks, and operational drills.
  Independently captured IAM/role evidence, restored-data reconciliation, and full alert-delivery
  evidence remain incomplete or partly operator-reported. These gaps matter most for roles expecting
  independent service ownership.
- AI projects support structured output, streaming, authorization, and failure-boundary discussion.
  Retrieval and model-quality claims remain bounded by their recorded evaluations. Planned AI
  authoring/tutor work is not implementation evidence.
- Repository depth does not prove timed DSA ability. Use assessed performance when planning an
  algorithm-screen track, without inferring that every frontend/product interview has that screen.
