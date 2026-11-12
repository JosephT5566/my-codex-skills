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
- 2026-10-29, product-oriented system design (scenario: shared expense ledger for 3-6 people with
  concurrent edits, offline resubmission, and budget-overrun notifications). Strengths: proposed
  request IDs with idempotency for offline resubmission, named last-write-wins and operational transform
  as conflict options, and clearly separated implemented evidence from design ideas. Project evidence:
  the expense-app AI agent write path uses request IDs with idempotency because processing is
  asynchronous; everything else in the answer was a design idea. Gaps: jumped to operational transform
  for a small group instead of version numbers with optimistic locking and field-level merge; did not
  compare sync options (SSE or hosted realtime versus WebSocket); no uniqueness constraint on
  (ledger, client request ID) was described; notification design (event fan-out and flood control) was
  unfamiliar; for the high-write bonus, named load balancing, autoscaling, caching, and rate limiting but
  not database write bottlenecks (partitioning, hot ledgers, batching, queue buffering). Next practice:
  conflict handling with optimistic locking, then a notification and event-driven design question. This
  is design-level assessed practice only.
- 2026-10-30, full-stack API, database, and authorization (scenario: shared ledger expense edited
  concurrently, with a duplicate offline add, on Supabase PostgreSQL with RLS). The user said the topic
  was unfamiliar and researched before answering. Strengths: described a version column for optimistic
  locking, a request ID with a uniqueness constraint against duplicate adds, 409 Conflict returning the
  latest version and data, field-level merge with its complexity cost, RLS plus an API-layer check, and
  a frontend flow that auto-merges non-conflicting edits and asks the user on real conflicts. Project
  evidence: expense-app implements an idempotency key and a transaction to prevent duplicate writes and
  keep them atomic; everything else was a design idea. Gaps: a replayed create should return the original
  result without changing the version; the uniqueness constraint should include the ledger, not only the
  user; the conditional update (UPDATE ... WHERE version = ?) and affected-row check were not described;
  RLS should check ledger membership rather than only matching the row's user ID; PATCH should send
  changed fields plus a base version so overlap can be detected. Next practice: a short SQL exercise
  on the conditional update and a membership-based RLS policy. This is design-level assessed practice only.
- 2026-10-31, AI-assisted development judgment (scenario: a coding agent's PR adds a CSV export of one
  ledger's monthly expenses; CI is green, tests mock the database; the endpoint takes ledger_id and month
  with no membership check, uses start + 30 days with BETWEEN, SELECT *, and writes note values straight
  into CSV). The user said the issues were not obvious at a glance and discussed them with an agent.
  Strengths: named missing authorization on ledger_id (IDOR) as the top risk, CSV formula injection, and
  unbounded result size; explained that CI only checks the logic and requirements someone thought of, so
  a missed security requirement passes; proposed an authorization test (user A cannot read user B) and a
  CSV injection test; wrote a structured follow-up instruction that prioritizes risks, asks for negative
  and real-database integration tests, forbids weakening existing assertions, and asks for findings,
  changes, results, and remaining risks. Gaps: missed the silent data-correctness bug (30-day month
  range loses the 31st and spills into the next month; BETWEEN includes the next month's first instant;
  time zone not handled), invalid month returning 500 instead of 400, and SELECT * over-fetching; the
  tests did not name boundary-date cases (1/31, 2/28, 12/31) or explain that a mocked database cannot
  verify SQL, RLS, or date boundaries; the follow-up instruction was generic, not scoped to the export
  endpoint, had no checkable acceptance criteria, and "do not unnecessarily change production code"
  would discourage the fix. Evidence: the user said this kind of AI-generated-code review only comes up
  in personal projects, not at Houzz; the STAR bonus was answered only at that level. Next practice:
  write acceptance criteria and a scoped agent instruction for a small change, and a short exercise on
  date-range boundaries and real-database tests. This is design-level assessed practice only.
- 2026-11-02, AI/LLM application engineering (agent tool-calling error handling and evaluation;
  scenario: expense-app semantic entry upgraded to a tool-calling agent with find_ledger, find_member,
  and create_expense, for the input "dinner with Xiaoming yesterday, 1200, split evenly, put it in the
  roommates ledger"; the ledger is hypothetical because expense-app scopes data as household versus
  personal and has no ledger concept). A first version sent on 2026-11-01 (receipt parsing with a JSON
  missing currency or a string amount, item sum 480 versus total 520, a ledger_id the user does not
  belong to, and a duplicate create_expense call in one request) was not answered. The user said he
  could not answer in detail but tried. Strengths: treated prompt and model output as a trust boundary
  that still needs real server-side authentication; proposed a validate function before writing and
  asking the user to fill in or fix data; resolved same-name members by ID and capped retries to avoid
  agent loops; split tests into function-logic unit tests without an agent fixture and model I/O tests
  with an agent fixture (needs the API); separated design ideas from implemented behavior. After
  feedback he highlighted as important that validation and permission errors should not be retried by
  the model, only transient errors (5xx, timeout) get bounded retries with the same idempotency key, and
  that the auth layer keeps an agent from reaching data it should not. Gaps: validation was not layered
  (schema format versus authorization versus business rules such as split shares summing to the
  amount); the create_expense parameters listed table columns, including payer_email, instead of
  having the server inject identity fields from the session; same-name matches should return a
  candidate list (ID, name, email prefix) and ask the user; no error classification for retry versus
  stop; evaluation had no release gate (normal, ambiguous or missing-data, and malicious or
  hallucinated cases such as a foreign ledger_id or prompt injection, with tool-call format accuracy,
  wrong-write rate near zero, clarification rate, and no regression across prompt changes); the
  confirmation-card bonus was not answered. Evidence: expense-app implements a request ID with
  idempotency and a transaction on the AI write path; the tool-calling agent and evaluation set are
  design ideas; RLS (#58) and the Gemini gateway (#62) under roadmap issue #64 are planned, not
  implemented. Next practice: an evaluation set with a release gate, the confirmation-card tradeoff, and
  layered authorization. This is design-level assessed practice only.
- 2026-11-03, behavioral (production incident handling, paired with the skill-gap themes production
  debugging, incident response, and deployment and rollback). The question asked for a STAR story about
  debugging and fixing a production problem. The user said he has little direct incident-troubleshooting
  experience and asked for a scenario and best practices, so the coach gave one: a search results page
  redesign released behind a feature flag to 50 percent of users; p95 latency rose from 400 ms to 3.5 s
  and 5xx from 0.2 percent to 4 percent, only on the new version, with a new sort-field query on the
  backend. Answers: first stop the bleeding by finding the impacted code change or page and trying a
  revert or feature switch; from Houzz experience with Coralogix, start from error messages, check the
  page and failed component, trace back to likely missing response data, then the API logic; notify
  stakeholders to change it or submit the fix himself, complete related tests before reopening, and add
  a feature switch as appropriate; after the root cause, fix plus unit tests and keep monitoring the same
  warning message. Strengths: mitigation before root cause; outside-in troubleshooting grounded in real
  Coralogix use; fix plus test plus continued monitoring. Gaps: quantify impact and timeline and
  correlate with recent deploys before choosing a mitigation; compare new versus old version traffic
  splits; check the backend and database (traces, slow queries, missing index, heavier query); reopen
  with gradual rollout (1, 10, 50, 100 percent) and metrics at each step; the post-incident review should
  ask why it was not detected earlier (integration tests, performance tests, latency and error-rate
  alerts, pre-production data volume) and improve detection, not only the bug; stakeholder communication
  (status, impact, next update time). After feedback he agreed that detection capability and database
  and traffic-split evidence are important. Evidence: professional evidence is monitoring and diagnosing
  frontend errors in Coralogix at Houzz (page, component, missing response data, API logic); he has no
  direct end-to-end incident ownership story yet, and the scenario answers were conceptual. Reference:
  `engineering-lifecycle/production-incident-checklist.md`. Next practice: a 60-90 second STAR from a
  real Houzz case, plus a follow-up question on this scenario planned this week. This is design-level
  assessed practice only.
- 2026-11-04, AI infra (embedding v2 backfill pipeline: retries, resumability, rate limiting, and
  monitoring, paired with the skill-gap themes AI engineering second half and production
  observability). Hypothetical scenario: english-learning upgrades its embedding model to v2; a backfill
  CLI re-embeds all notes and sentences while user-added content still uses background embedding; the
  provider returns many 429s and some 5xx, and the CLI is interrupted midway. Parts: retry strategy,
  resumability and idempotency with the version switch, rate limiting and priority between realtime and
  backfill, and monitoring metrics; bonus: implemented versus design-only. Answers: 429 means too many
  concurrent requests, so use jitter to spread retries and Retry-After when provided, record retry state,
  and stop and update state at the retry limit; keep a state table and rerun only specific states such
  as failed, serving v1 until the backfill is confirmed complete, then switch to v2; use the API service
  rate limiter to reduce request volume; check embedding switch completion rate, correctness of context
  tests under v2, and build an eval. The bonus part was not answered. Strengths: jitter plus
  Retry-After; a state table with rerun of failed only; v1 until complete, then v2; completion rate and
  v2 quality as launch metrics. Gaps: error classification (retry 429, 5xx, and timeouts; do not retry
  400, 401, or 403; pause the whole run on repeated failures); an in_progress state with timeout reclaim
  and an upsert keyed by (content id, model version) for idempotency; an explicit switch threshold
  (coverage plus eval not worse than v1) and a rollback flag; separate priority queues or token-bucket
  quotas for realtime versus backfill, with backfill yielding on 429 (a single rate limiter only slows
  everything); monitoring lacked process health (429 and 5xx rate, retry and failed counts, realtime p95
  latency, backfill speed and ETA, cost). Follow-up: he asked about token buckets and how they differ
  from a rate limiter; the coach explained that a token bucket is one algorithm for implementing a rate
  limiter, controls sending speed, is typically combined with a concurrency cap, and can be split into
  two buckets for realtime and backfill. Evidence: design-level only. english-learning actually has
  versioned vectors, hash-guarded background embedding, a backfill CLI
  (apps/api/app/embedding_backfill.py, with --retry-exhausted), DB-level retry for document
  embeddings (up to 3 attempts at about 1/4/16 minutes with jitter, then marked exhausted; #47,
  commit cb20956), and a retryable 503 on provider failure. His answer "rerun only failed items"
  matches that implemented design. Still planned, not implemented: query-side retry and rate
  limiting (#63; today an 8 s timeout and 429 mapped to provider_rate_limited, no Retry-After
  handling), cost observability (#64), and the realtime/backfill priority split; tracked under
  roadmap #66. Implementation facts verified on 2026-11-04 from public GitHub (code, commits, issue
  states); not verified as running in production. No production
  experience is claimed. Next practice: a short design note or issue in english-learning for a priority
  queue plus token bucket and backfill CLI flags (--max-rps, --concurrency); reading: Amazon Builders'
  Library "Timeouts, retries and backoff with jitter" and Google SRE Book "Handling Overload". This is
  design-level assessed practice only.

- 2026-11-09, product-oriented system design (quiz Q11: shared-ledger budget-overrun notifications;
  3-6 members per ledger, monthly category budgets, in-app plus Web Push at 80 and 100 percent,
  about 20k ledgers, 50 writes/s peak, and offline replay of about 10 expenses). Answers: detect the
  threshold in the transaction and roll back on failure, then hand push to a background worker;
  unsure about deduplication, proposed request IDs, monthly-once behavior with periodic re-validation,
  and re-triggering after spend drops below the threshold; revision traffic splitting and rollback
  to the previous revision, with a failed-state table and bounded retry for push 5xx. Strengths:
  worker decoupling, bounded retry with recorded failures, revision-based rollback, and an honest,
  precise account of implemented idempotency limits. Coach feedback: an expense write must not depend
  on crossing a threshold. In one transaction, write the expense, recompute the monthly category total,
  detect before < threshold <= after, and insert a transactional outbox event so event recording and
  expense commit are atomic; direct push risks phantom notifications on rollback or lost notifications
  after a post-commit crash. Serialize concurrent writes per ledger with SELECT ... FOR UPDATE or
  enforce the relevant invariant with a uniqueness constraint. Request IDs cover request retries,
  not monthly-once delivery; use a notification log with unique (ledger_id, category_id, threshold,
  month) and INSERT ... ON CONFLICT DO NOTHING before sending. Offline replays hit that constraint
  after the first event; optional short-window coalescing reduces floods. A drop below the threshold
  neither retracts nor re-notifies within the month; edits/deletes use the same recompute, and a jump
  from 70 to 110 percent sends only the 100 percent notice. Detect on writes; schedules are for
  reconciliation, not periodic re-validation. Retry 5xx/timeouts with a cap, exponential backoff, and
  jitter, then mark failed; 410 Gone means an expired subscription, so deactivate it without retry
  (missed in the answer). Monitor outbox backlog and oldest-event age, send success rate, 5xx/410 rates,
  crossing-to-delivery latency, and notifications per ledger for duplicates. Add ledger/user feature
  flags at 1/10/50/100 percent and a kill switch that pauses sending while the outbox keeps recording.
  Evidence: expense-app has no similar notification design. Its real AI-entry implementation uses
  (user_id, request_id) plus input_hash: same ID and input returns the saved result; changed input with
  the same ID returns 409; a new ID is a new operation and can duplicate it. Retry content exists only
  in the original page's memory. Outbox, notification deduplication, and push retry/410 handling are
  design-only. Reading given: microservices.io "Transactional outbox", RFC 8030 on subscription expiry,
  `engineering-interview-drills/async-workflow-recovery.md`, and
  `engineering-interview-drills/transactional-concurrency.md`. Next practice: notification/outbox design
  has now been practiced; an optional expense-app budget-notification design issue is deferred until
  the user asks. This is design-level assessed practice only.
- 2026-11-10, AI-assisted development judgment (quiz Q12: review an AI-authored deployment PR
  for `english-learning`, also practicing cloud deploy and checkable acceptance criteria). The
  hypothetical PR claimed CI was green, rebuilt the image at deploy time once each for staging
  and production, wrote the database connection string and a long-lived service account key into
  workflow environment variables, skipped a zero-traffic candidate and sent the new revision to
  100 percent traffic, ran in one job an Alembic migration that made a previously nullable
  column `NOT NULL` then immediately `DROP` an old column, and used a smoke test that only hit
  `/health` against a mocked database. The user said this was closer to SRE work and was
  unfamiliar. Answers: putting the connection string and SA key in env is dangerous; secrets
  should go in Secret Manager; test new behavior at zero traffic after publishing a revision,
  then gradually shift production traffic; keep the old column and change the related backend
  methods rather than immediately `DROP` it; old and new code should coexist behind a feature
  switch, and the new version must run without the old column before evaluating `DROP`; rolling
  back the Cloud Run revision leaves the database migration's schema change; at zero traffic,
  verify with a smoke test and look at tracking before shifting traffic. Strengths: correctly
  rejected long-lived secrets in workflow env; zero-traffic then gradual traffic shift; kept the
  old column and required new code to work without it before `DROP`; clearly stated that
  revision rollback does not undo a breaking migration. Gaps: treated rebuild-at-deploy for
  staging and production as acceptable, missing image drift (build once and promote the same
  digest); did not explain why CI green is still unsafe (mocked `/health` does not exercise the
  real migration, auth, or changed read/write path); missed nullable-to-`NOT NULL` risk
  (existing nulls and old writers still inserting `NULL`); expand-and-contract was incomplete
  (no backfill-then-constrain sequence, and `DROP` must be a later contract migration after old
  revisions are gone); acceptance criteria were too vague (only "smoke test" and "tracking"),
  without 4-6 pass/fail checks for a single image digest, secret injection, authenticated
  real-database smoke on the changed path, pre-shift 5xx/latency versus baseline, and
  backward-compatible schema so traffic rollback still works; did not label what was already
  implemented in `english-learning` versus designed in this answer. Evidence: design-level
  assessed practice only, not professional SRE or production service ownership.
  `english-learning` already has project-level zero-traffic candidate verification,
  authenticated smoke, promotion, schema-compatible rollback, WIF, and secrets boundaries; these
  remain project evidence, not professional SRE experience, formal on-call ownership, or
  production service ownership. The "build once and promote the same digest" rule and timing of
  `DROP`/`NOT NULL` were identified in feedback as today's design. Reading given: Martin Fowler
  "Parallel Change", Google Cloud Run "Rollouts, gradual rollouts, and traffic migration", and
  Secret Manager overview. Next practice: write checkable acceptance criteria and a scoped agent
  follow-up for a small deploy or migration change; a short expand-and-contract exercise on
  nullable-to-`NOT NULL` plus later `DROP`. This is design-level assessed practice only.
- 2026-11-11, frontend architecture and performance plus observability (quiz Q13; follow-up to
  the 2026-10-27 gap on field data and experiment guardrails). Hypothetical scenario (all
  numbers hypothetical): a React/Next.js search results page redesign rolled out behind a
  feature flag to 10% of users; Lighthouse score rose from 72 to 88, but RUM showed mobile INP
  p75 rising from 180 ms to 320 ms, LCP roughly unchanged, and search-to-product-click
  conversion slightly down. Answers: Lighthouse may have improved due to other metrics; worse
  INP possibly came from a larger bundle, long main-thread tasks from new expensive JS, async
  waiting, or longer React render; use DevTools Network or add `web-vitals/attribution`, which
  the user said he has not used yet; reduce synchronous recompute wait by caching after initial
  load and not refetching, re-render only the currently displayed list, and keep monitoring INP
  and continue rollout if it improves. Strengths: identified main-thread blocking, expensive JS,
  and React render time as INP drivers; re-rendering only visible items points toward
  virtualization; tied rollout to monitoring INP. Gaps: did not explain lab versus field
  (Lighthouse measures page load in a simulated environment with no real interactions, so it has
  no INP, only TBT as a proxy; real low-end mobile devices differ); conflated bundle size
  (mainly load, indirect for INP via hydration-time input delay) and async waiting (network
  awaits after handlers are not part of INP, which ends at next paint) with INP causes; missed
  the three INP phases (input delay, processing duration, presentation delay) and hydration-time
  interactions; DevTools is local only and cannot see field data; did not name attribution
  fields (`interactionTarget`, `interactionType`, `inputDelay`, `processingDuration`,
  `presentationDelay`, `loadState`, `longAnimationFrameEntries`) or slicing dimensions (flag
  variant, device class/mobile versus desktop, browser, page type, interaction target) and
  comparing variant-vs-control p75 delta; fix lacked concrete React techniques (immediate
  checkbox state then deferred list update with `useTransition`/`useDeferredValue`, memoized
  filtering, list virtualization, chunking/yielding or Web Worker for heavy recompute), and
  "cache after load" only helps if recompute inputs repeat; rollout lacked pre-written pass/fail
  thresholds (mobile INP p75 not worse than control beyond a small margin, ideally back under
  the 200 ms "good" threshold; conversion not significantly below control; JS error rate and LCP
  not worse; enough samples and 1-2 days per stage; otherwise turn flag off) and ignored the
  already-dropping conversion as the key guardrail signal. Bonus Houzz A/B STAR was not
  answered. Evidence: design-level assessed practice only; `web-vitals` attribution / RUM
  instrumentation is not yet used in practice. A/B testing and product-oriented frontend remain
  Houzz professional experience, but this answer did not add new professional evidence. Reading
  given: web.dev "Interaction to Next Paint (INP)", web.dev "Find slow interactions in the
  field", and React docs useTransition. Next practice: answer the Houzz A/B test 60-second STAR;
  a small exercise adding `web-vitals` attribution INP reporting to a personal project (e.g.
  english-learning or expense-app) and writing rollout thresholds.
- 2026-11-12, AI infra (quiz Q14: LLM gateway retry placement, time budget, rate limiting and
  cost, caching, and observability), based on an english-learning hypothetical. Implemented
  project context: #70 read-only assistant with a maximum 3-step tool loop (`search_cards`,
  `get_due_cards`, `get_review_stats`), SSE streaming, and Gemini Flash-Lite; #91 15-second
  heartbeat, 25-second assistant deadline, and Cloud Run 30-second timeout; #73 request-ID
  structured logs covering success, step limit, timeout, provider failure, and SSE early
  disconnect. Planned only, not implemented: #77 rate limit and cache, #63 query-side retry and
  limit, #64 cost observability. Hypothetical scenario (not an actual production incident; all
  scenario numbers hypothetical): the assistant opens to 50 beta users; evening peak logs show
  provider 429/5xx bursts, about 10% of runs timing out mostly at step 3, and regenerate spam
  tripling daily token cost. The user said the topic was beyond his current understanding but
  attempted an answer. Answers: before any text is sent, treat it as server overload, notify the
  user to wait, or retry on the frontend with jitter / Retry-After; mid-stream, use the recorded
  request ID to auto-retry or ask the user. Asked the purpose of per-user limiting; for regenerate
  spam, use the backend request ID as an idempotency key and disable the frontend submit button.
  Cache key could include the request ID unique constraint; cache embeddings and tool results; do
  not cache final answers because they can vary with questioning time. Bonus metrics question was
  not answered. Strengths: jitter plus Retry-After; frontend submit guarding; embeddings are
  cacheable; final answers generally should not be cached. Gaps: 429 and 5xx are provider-side
  errors, so retries belong in the backend gateway, not the frontend. Before the first token,
  retry transparently with exponential backoff plus jitter, honoring Retry-After, only if the
  remaining deadline allows it; otherwise use a fallback model or return a fast clear error.
  Mid-stream cannot silently retry because it would produce duplicate or inconsistent text; keep
  partial output, mark the answer interrupted, and offer regenerate. The request ID is for tracing
  and cannot resume a stream from the interruption point. Deadline propagation in this
  hypothetical design: each step gets min(remaining time, a step cap of about 8 seconds); reserve
  about 5 seconds for the final answer; at step 3 near the deadline, answer with tool results
  already gathered instead of letting the whole run time out. Per-user limiting provides fairness
  on a shared provider quota (429 means quota is exhausted), cost control, and service protection.
  Enforce at the backend gateway per `user_id`; frontend limits are bypassable and only auxiliary.
  Combine 1 concurrent run per user, requests per minute, and a daily token budget, with a clear
  message when the budget is used up. An idempotency key does not stop regenerate: each regenerate
  is a new intent and should count as a new request. Frontend should disable the button and cancel
  the previous request with `AbortController`. Backend should cancel the same user's previous run
  when a new one starts (latest wins), add a per-message regenerate cap, and count those attempts
  toward the daily token budget. A request ID is useless as a cache key because it is unique every
  time and always misses. Embedding cache key = model, version, and hash of normalized text
  (shareable across users; contains no user data). Tool-result cache key = `user_id`, tool name,
  args hash, and data version, with a short TTL (`get_due_cards` changes after reviews). Final
  answers generally should not be cached; if cached at all, only per user when prompt and data
  version are exactly the same. Isolation depends on `user_id` plus database authorization (RLS),
  not the cache key alone. Bonus (unanswered) reference metrics: provider failure rate
  (hypothetical example: above 5% over 15 minutes), timeout rate sliced by step, and per-user
  daily tokens (hypothetical example: above 5 times the median). Set thresholds from one week of
  baseline data, then use multiples of usual values. Evidence: design-level assessed practice
  only; no professional or production LLM gateway experience, and no professional production
  rate-limiting experience established by this answer. This answer did not add new professional
  evidence; #77, #63, and #64 remain planned. Reading given: AWS Builders' Library "Timeouts,
  retries and backoff with jitter"
  (https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/). Next
  practice: in english-learning, design deadline propagation plus a per-user concurrent-run limit
  (ties to #77 and #63); the Q13 bonus Houzz A/B 60-second STAR is still pending.

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
  Retrieval and model-quality claims remain bounded by their recorded evaluations. The personal
  english-learning project implements the read-only assistant (#70) and structured extraction (#72)
  under epic #78, closed as completed on 2026-11-10. A finished RAG tutor is not built; routing was
  evaluated and is not wired in; alerts are not implemented. See `github-project-signals.md` for
  dated merge evidence and limits.
- Repository depth does not prove timed DSA ability. Use assessed performance when planning an
  algorithm-screen track, without inferring that every frontend/product interview has that screen.
