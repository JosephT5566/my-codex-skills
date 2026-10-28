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

## Daily coaching rotation

Updated 2026-10-27 from the user's request. For recurring daily or periodic quizzes, rotate topics rather
than drilling the same category on consecutive days, and avoid repeated deep dives on one category within a
week unless the user asks. The rotation supplements the priority table; it does not change which
capabilities are most valuable to prove.

- Categories: frontend architecture and performance; product-oriented system design; full-stack API,
  database, and authorization; AI infrastructure and current AI engineering trends; AI/LLM application
  engineering; AI-assisted development judgment; behavioral; resume or self-introduction; career reflection.
- The user explicitly wants system design and AI infrastructure questions included. Schedule each about
  once or twice a week, with a mix of product-level whiteboard design and tradeoff or failure scenarios.
- AI infrastructure topics: LLM gateway and model routing, retrieval and embedding pipelines, evaluation
  and observability, cost and latency control, caching, agent and tool-calling boundaries (including MCP),
  permissions and safety, and streaming inference serving. Frame these at the level of a product engineer
  growing toward full-stack and AI roles, and require workload-based reasons for added components.
- Trend claims must come from a current source or be labeled uncertain; do not present a trend as
  established fact without support.
- Keep professional and project evidence separate in questions and feedback. Treat answers as assessed
  practice, not production evidence.

### Assessed practice log

Record dated, compact results here when the user completes quiz answers. These are assessments of an
answer, not proof of capability.

- 2026-10-27, frontend architecture and performance (scenario: INP 450 ms and LCP 3.4 s on a list or
  search results page). Strengths: layered diagnosis, correct mapping of INP to main-thread and DOM cost
  and of LCP to server rendering and streaming, named the cost of virtualization, and referred to A/B
  testing experience. Gaps: relied on Lighthouse (lab data) rather than field data (RUM) and INP
  attribution to find the slow interaction; verification lacked p75 comparison by variant and guardrail
  metrics such as conversion. The optional STAR case was not answered. The user is considering Sentry or
  the web-vitals library for RUM; he has not used web-vitals monitoring himself. Next practice: field data
  and attribution, experiment design, and an observability-introduction design question.
- 2026-10-28, AI infrastructure (scenario: expense-app semantic entry at 10x traffic with high p95
  latency, rising model cost, and provider 429/5xx errors; answers mixed design ideas, not claims of
  implemented behavior). The user said the topic was unfamiliar. Strengths: proposed a model router that
  sends requests to a small or frontier model, idempotency with state checks and a retry cap of two,
  semantic caching, and tracing with prompt logs, an evaluation suite, and a release gate; on the bonus
  question, proposed showing failure state, a retry button, and distinct handling for rate limiting and
  retry exhaustion. Gaps: retry detail (backoff with jitter, Retry-After, provider fallback, circuit
  breaker); the router's own latency and cost (rules first, then small model, then escalation); semantic
  cache isolation per user and near-miss risk for numeric inputs; missing latency, cost, error-rate,
  cache-hit, and escalation-rate metrics. Next practice: short learning pass on gateways, retries,
  caching, and LLM evals, then a narrower question on one of these. This is design-level assessed practice
  only; the project does not evidence a production gateway.

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
