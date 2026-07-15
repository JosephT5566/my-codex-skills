# Career Targeting and Mixed-Role Screening

Use this reference when ranking mixed frontend/backend/AI roles or producing career coaching.

## Main Targeting Thesis

The strongest current positioning is:

Product-minded Full-stack / AI Product Engineer with strong frontend, product ownership, backend/data integration, experimentation, production debugging, and AI workflow integration experience.

Do not rank roles by title alone. Screen by actual work content and transferable skills.

## Backend Depth Scale

Use this scale when estimating fit:

1. API consumer: consumes documented APIs from frontend.
2. API integrator: integrates frontend with APIs, auth, data fetching, and product state.
3. API designer: defines request/response contracts, validation, error handling, and async behavior.
4. Backend feature owner: owns schema changes, API boundary, authz/RLS, transactions, idempotency, observability, and release behavior for a product feature.
5. Service/system owner: owns backend service reliability, deployment, scaling, incident response, and service-level architecture.
6. Platform/infrastructure owner: owns cloud, containers, networking, observability platform, distributed systems, IaC, or internal platform foundations.

Default Joseph assessment: API integrator moving toward API designer/backend feature owner. Upgrade this only when project evidence shows schema tradeoffs, RLS policy reasoning, API contracts, idempotency, async jobs, observability, or production-like backend ownership.

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

- Backend ownership evidence: schema tradeoffs, indexes, transactions, idempotency, migrations, RLS policies, service-role safety, API contracts, async workflow, and observability.
- AI product evidence: structured output, tool calling, permission-aware data access, human approval, evaluation dataset, tracing, retry/fallback, and cost/latency controls.
- System design communication: explain product feature boundaries, data flow, failure modes, security/privacy, and monitoring in interview-ready language.

Prefer exercises that extend the expense app rather than generic toy projects.
