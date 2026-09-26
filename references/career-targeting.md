# Career Targeting and Mixed-Role Screening

Use this reference when ranking mixed frontend/backend/AI roles or producing career coaching.

## Main Targeting Thesis

The strongest current positioning is:

Product-minded Frontend Engineer with strong React/TypeScript product ownership and project-level backend implementation, backend/data integration, experimentation, production debugging, and AI workflow integration evidence.

Use this targeting order unless the user requests a different lane:

1. Frontend Engineer / Senior Frontend Engineer with substantial product ownership.
2. Frontend Platform, Web Platform UI, Search, Marketplace, CMS, or product-infrastructure frontend roles.
3. Product Engineer and frontend-heavy Full-stack Engineer roles.
4. AI Product Engineer or LLM Application Engineer roles where user-facing frontend/product work remains central.
5. Developer Productivity, Forward Deployed, or Solutions roles with meaningful hands-on frontend/product implementation.

Target frontend-heavy and product-oriented full-stack roles now, but use them as the preferred growth lane rather than replacing the frontend-first strategy. Calibrate every role to evidence that exists on the application date.

Do not rank roles by title alone. Screen by actual work content and transferable skills.

## Backend Depth Scale

Use this scale when estimating fit:

1. API consumer: consumes documented APIs from frontend.
2. API integrator: integrates frontend with APIs, auth, data fetching, and product state.
3. API designer: defines request/response contracts, validation, error handling, and async behavior.
4. Backend feature owner: owns schema changes, API boundary, authz/RLS, transactions, idempotency, observability, and release behavior for a product feature.
5. Service/system owner: owns backend service reliability, deployment, scaling, incident response, and service-level architecture.
6. Platform/infrastructure owner: owns cloud, containers, networking, observability platform, distributed systems, IaC, or internal platform foundations.

Default Joseph assessment: project-level backend feature owner with assessed API/system-design practice and operator-verified personal-service deployment/release rehearsal. Current evidence covers strict/versioned contracts, structured-output validation, server-verified identity, owner-scoped authorization, deterministic APIs, PostgreSQL constraints and migrations, transactional/idempotent review writes, controlled legacy-data import and reconciliation, typed frontend cutover, containerization, staged candidate/promotion/rollback procedures, health checks, operational exercises, and owner-safe semantic retrieval. The deployment evidence is from a personal project and partly operator-reported; it does not establish professional service ownership, production scale, sustained observability, incident response, or on-call experience.

Recent practice also covers PostgreSQL schema tradeoffs, RLS reasoning, idempotency, durable async jobs, lease/fencing concepts, transactional concurrency, ambiguous timeouts, and outbox tradeoffs. Apply the evidence levels in `candidate-profile.md`: mixed or incomplete session results support calibrated readiness notes, not blanket claims of mastery.

## Full-stack Targeting Now

Promote a full-stack role to `Target` or `Strong Fit` when most of the following are true:

- React/TypeScript or comparable product-web ownership is a major part of the job.
- Backend work is tied to user-facing features, API contracts, integrations, authentication, authorization, relational data, or workflow reliability.
- The expected backend depth is API designer or backend feature owner, with room to grow into broader service ownership.
- Node.js, Python, REST, GraphQL, PostgreSQL, Supabase, Firebase, serverless functions, or third-party integrations overlap with current professional or project evidence.
- The role values product judgment, experimentation, debugging, release quality, and cross-functional delivery rather than backend specialization alone.

For comparable opportunities, rank a strong frontend role above a full-stack role unless the full-stack role preserves substantial frontend ownership and offers clearly better product scope or career upside. Do not use the `Full Stack` title itself as an upside signal.

Use `Practice` when the role is moderately backend-heavy but remains product-facing, provides a credible frontend bridge, and does not make prior large-scale service ownership a hard screen. Use `Skip` when the role primarily requires deep distributed systems, backend platform ownership, infrastructure, networking, Kubernetes, or years of professional backend on-call responsibility.

When an `english-learning` milestone is completed, update the evidence level from the repository ledger rather than assuming the whole roadmap is finished:

| Verified milestone | Full-stack evidence it can add |
| --- | --- |
| Backend foundation and data model — verified locally in `english-learning` | FastAPI, SQLAlchemy, Alembic, PostgreSQL constraints, reversible migrations, integration tests, and seven query-driven indexes exercised on representative data |
| Authentication and review writes — verified locally | Server-verified identity, per-user authorization, deterministic reads, transactions, idempotency, rollback, and concurrent-conflict behavior |
| Import and frontend cutover — verified locally, with private import operator results | Reconciled migration, typed API integration, end-to-end failure handling, bilingual management, and PostgreSQL source-of-truth transition |
| Deployment and operations — locally verified release contract plus operator-reported production rehearsal | Non-root containerization, TLS/secrets boundaries, health checks, staged candidate verification, authenticated smoke tests, promotion, schema-compatible rollback, and WIF workflows |
| AI authoring and hardening | Safe AI draft lifecycle, evaluation, retries/failures, measured performance, security review |

These milestones strengthen project-level backend feature ownership. They do not become professional production ownership merely because the implementation is deployed.

## Backend Capability Checks

Use these checks to distinguish a keyword match from interview-ready ownership:

| Capability | Look for in the JD | Evidence needed to upgrade readiness |
| --- | --- | --- |
| API contract design | API ownership, async processing, integrations, reliability | A concrete design or implementation covering resource states, validation, idempotency, failure semantics, retries, and observability |
| PostgreSQL data modeling | PostgreSQL, schema design, migrations, transactional workflows | Locally implemented in `english-learning`: shared multilingual schema, named constraints, composite ownership keys, reversible migrations, query-plan checks, locked writes, rollback, and concurrency tests; deployment and operational behavior remain gaps |
| Authorization / RLS | Supabase, PostgreSQL RLS, multi-tenancy, permissions | Locally implemented at the application/database boundary in `english-learning`: server-verified identity, owner-derived writes, horizontal denial tests, foreign-parent denial, and optimistic version conflicts; RLS and live Google verification remain separate gaps |

Apply the evidence levels in `candidate-profile.md`. Project implementation can support a fit note; assessed practice can support an interview-readiness note. Preparation material alone supports only a homework recommendation.

## Role-Family Backend Expectations

- Senior Frontend Engineer: medium-low backend depth. Needs API/data/auth literacy and production debugging, not full service ownership.
- Frontend Platform Engineer: medium depth. Needs architecture, build/test/tooling, contracts, reliability, and sometimes internal APIs.
- Product Engineer: medium-high depth. Needs end-to-end feature ownership across frontend, API, data, authz, edge cases, and product metrics.
- Full-stack Engineer: high depth. Needs credible backend feature ownership and often deployment/testing/observability.
- AI Product Engineer: medium-high depth. Needs backend/data/authz because AI tools access user data and may propose mutations.
- Applied AI Engineer: medium to high depth. Product-facing roles fit better; ML/model-serving/platform roles require deeper Python, ML, and infra.
- AI Agent Engineer: high depth. Needs tool calling, permissions, state, retries, fallbacks, evaluation, tracing, and safe execution boundaries.
- Developer Productivity Engineer: medium-high depth. Needs CI/CD, internal tooling, permissions, logs, reliability, and workflow automation; product DB depth may be less central.
- Forward Deployed Engineer: medium-high depth. Needs fast API/data/auth/deployment/debugging across customer contexts.
- Platform Engineer: very high depth. Backend basics are insufficient; requires deeper cloud, containers, infra, networking, and observability.

## Favor These JD Signals

- End-to-end product ownership.
- React/TypeScript plus backend/data/API ownership.
- PostgreSQL, Supabase, GraphQL, REST, API design, auth, authorization, RLS, data modeling, or analytics.
- Product metrics, A/B testing, experimentation, release monitoring, feature flags, logs, dashboards, production debugging.
- AI product workflows, LLM integration, structured output, tool calling, RAG, human-in-the-loop approval, evaluation, tracing, retry/fallback, token/latency/cost control, permission-aware data access.
- Developer productivity, internal tools, coding-agent workflows, CI/CD integration, workflow automation.
- International product teams, remote-friendly culture, Europe/APAC eligibility, or product-led SaaS companies.

## Penalize These JD Signals

- Pure UI implementation with little ownership beyond component coding.
- Pure ML research, model training, fine-tuning, PyTorch-heavy model development, GPU infrastructure, or model-serving ownership.
- Deep backend/platform ownership with no frontend/product bridge.
- Deep data engineering with pipeline/warehouse ownership and no product-web scope.
- Security specialist roles requiring penetration testing, compliance ownership, or security certifications as primary proof.
- Harness Engineer roles that mean wire harness.
- Loop Engineer roles that mean hardware-in-the-loop or software-in-the-loop rather than AI agent loops/evaluation workflows.
- Solutions or FDE roles that are mostly account management, support, project coordination, or pre-sales with little hands-on product implementation.

## Coaching Gap Defaults

When relevant requirements recur in reviewed roles, surface these as practical homework:

- Interview filter risk: follow `interview-readiness-priorities.md`; timed TypeScript DSA is the highest-priority gap and should run continuously alongside portfolio work.
- Frontend seniority evidence: build one measured architecture/performance case study with budgets, bundle and Core Web Vitals evidence, accessibility, failure states, and Playwright coverage.
- Backend ownership evidence: close remaining operational proof gaps—restored-data reconciliation, independently captured runtime-role/IAM boundaries, alert delivery, and response-ID correlation. Add async infrastructure only for a measured requirement.
- AI product evidence: finish the frozen semantic-retrieval evaluation before claiming general quality; later prove structured output, permission-aware tool calling, human approval, tracing, retry/fallback, and latency/cost controls without allowing AI to confirm durable cards directly.
- System design communication: practice product-facing systems such as search, CMS, experimentation, realtime dashboards, notifications, and AI-assisted workflows, covering data flow, failure modes, security/privacy, observability, and evolution under load.

Prefer exercises that deepen a measured `english-learning` or professional frontend gap, or extend the expense app when Supabase/RLS is specifically relevant, rather than generic toy projects.

## Conditional Drill Routing

Recommend a drill only after the corresponding requirement recurs in the reviewed jobs or appears in a shortlisted role. Choose the smallest relevant exercise rather than assigning the full drill library.

| Observed requirement or gap | Practice reference | Desired outcome |
| --- | --- | --- |
| API design, async jobs, idempotency, partial failure, retry, or operational recovery | `engineering-interview-drills/api-contract-design.md` | Defend an end-to-end contract and its failure semantics at the role's expected scale |
| PostgreSQL schema design, normalization, JSONB, constraints, concurrency, or migrations | `engineering-interview-drills/postgresql-schema-tradeoffs.md` | Tie a schema choice to access patterns, integrity, write behavior, and migration safety |
| Supabase/PostgreSQL RLS, multi-tenancy, ownership, admin roles, or service credentials | `engineering-interview-drills/supabase-rls-reasoning.md` | Model authorization boundaries and concrete exploit prevention without relying on syntax recall |
| Synchronous concurrent writes, limited inventory, one-per-user rules, counters, balances, or ambiguous commits | `engineering-interview-drills/transactional-concurrency.md` | State invariants first, assign each guarantee to the database or API layer, and defend contention and recovery behavior |
| Durable jobs, worker ownership, leases, fencing, stuck work, or provider reconciliation | `engineering-interview-drills/async-workflow-recovery.md` | Defend at-least-once execution, atomic claim, bounded retry, stale-worker rejection, and operational recovery |
| Structured AI output, prompt injection, human review, draft confirmation, or late model results | `engineering-interview-drills/ai-structured-output.md` | Separate model guidance from enforceable boundaries and safely move probabilistic output into application state |

Do not mark a gap resolved merely because a drill exists. Use the completed-session calibration in `candidate-profile.md`; repeat or deepen a drill when its recorded gaps match a shortlisted role.
