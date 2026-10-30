# Candidate Profile Snapshot

Use this as the compact maintained source of truth for Joseph Tseng's job-search targeting.

## Current Positioning

Joseph Tseng is a product-minded frontend engineer with a strong TypeScript/React professional foundation and project-level full-stack/backend evidence. Frontend Engineer and Senior Frontend Engineer are the first priority. Frontend-heavy Product Engineer and Full-stack Engineer roles are the preferred growth path, followed by AI Product Engineer roles where user-facing frontend/product work remains central. His strongest professional evidence is marketplace search and browse, CMS-driven product infrastructure, A/B-tested product improvements, GraphQL/API integration, production debugging, release quality, analytics, and practical AI workflow integration. Project work adds Node.js/Express and FastAPI/Pydantic service boundaries, SQLAlchemy/Alembic and PostgreSQL/Supabase persistence, authentication and authorization, transactional/idempotent writes, controlled data migration, versioned API contracts, containerized Cloud Run/Neon deployment, staged release/rollback practice, owner-safe semantic retrieval, structured AI output validation, and security-focused negative testing.

Do not position him as a pure UI implementer, pure ML researcher, pure backend/platform engineer, or pure manual QA candidate unless the user explicitly requests that lane.

## Strongest Evidence

- Houzz software engineer from May 2022 to May 2026 across Marketplace, Lead Nurture, and 3D teams, as recorded in `resume-2026.md`.
- Built marketplace search, browse, navigation, CMS, event, and campaign experiences across desktop and mobile web.
- Delivered A/B-tested search/browse improvements; one mobile experiment trended positive with +5.8% orders and +2.5% GMV.
- Built Prismic/CMS-driven page infrastructure with content models, GraphQL schemas/resolvers, data transformations, routing, reusable slices, and frontend rendering.
- Shipped a contest/voting experience with about 21,000 unique visitors and 1,700 signed-in voting users.
- Integrated AI/3D-adjacent workflows, GraphQL services, frontend state/data flow, dimension parsing/transformation, and external AI services.
- Uses Amplitude, Redash, and Coralogix for product analysis, release monitoring, dashboards, and production debugging.
- Maintains JoPie (`expense-app`), a SvelteKit/TypeScript/Supabase expense PWA, with a Python/FastAPI/LangGraph semantic-entry service. Project implementation includes deterministic LLM-output validation and bounded clarification, caller-scoped transactional idempotency, versioned Gemini SSE with backpressure/deadlines, uncertain-write status recovery, and Python/TypeScript contract parity. The 2026-10-14 record reports 187 backend tests and 38 browser scenarios at root and subpath; these historical synthetic/local checks were not rerun for the 2026-10-15 reference update and do not establish real-model quality, hosted reliability, or professional backend service ownership. See [project evidence and limits](github-project-signals.md#expense-app-semantic-entry-evidence-reviewed-2026-10-15). Existing OAuth, shared expenses, and monthly caching remain part of the product. As of 2026-10-30 (v3), receipt-image analysis is merged into the semantic-entry service with signed-URL uploads, editable per-line-item drafts, batch persistence, and pending-write recovery; Joseph reports it is deployed for personal use only, and hosted reliability remains unverified.
- Built a companion CommonJS Node.js/Express Google Cloud Function for a travel/shared-expense product, exposing REST-style `GET`, `POST`, and `DELETE` APIs with Google ID-token verification, service-account access to Google Sheets, spreadsheet-defined user/configuration contracts, a consistent response envelope, and concurrent participant-tab writes and deletes. Treat this as project implementation rather than production service ownership; resource-oriented route design, caller-to-request binding, partial-failure recovery, automated tests, dependency completeness, and deployment operations remain improvement areas.
- Implemented a Python/Pydantic receipt-extraction service in `google-ai-gcf` with a canonical schema, Gemini structured responses, a versioned normalized result contract, JWT-derived GCS ownership checks, file and metadata limits, prompt-injection trust boundaries, sanitized failure handling, and 97 tests across the latest documented hardening pass. Joseph reported on 2026-10-30 that this capability is now integrated into JoPie rather than a separate project.
- Maintains `english-learning`, a deployed SvelteKit/Svelte 5 and FastAPI/PostgreSQL multilingual review product. It implements one owner-scoped English/Japanese domain, server-verified Google identity, deterministic reads, transactional/idempotent review writes, controlled CSV validation/import/reconciliation, typed frontend review and bilingual management flows, containerized Cloud Run/Neon releases, and owner-safe semantic retrieval. Operator-reported evidence covers authenticated reads, controlled write/replay, candidate promotion, schema-compatible rollback, and provider-backed retrieval smoke; deterministic tests cover isolation and failure boundaries. Keep the boundary explicit: restored-data reconciliation, independent IAM/role artifacts, complete alert delivery, sustained observability/on-call ownership, retrieval quality, and AI drafts remain incomplete or unverified.
- Earlier experience includes React/Next.js/TypeScript web apps, API integration, PostgreSQL changes, GitHub-based CI/CD/GitOps, firmware, C/C++/C#, validation, and production application tooling.

## Current Full-stack Targeting Boundary

- Keep frontend roles first in search coverage, shortlist tie-breaks, and application priority because they have the strongest professional evidence and interview probability.
- Consider frontend-heavy and product-oriented full-stack roles now when React/TypeScript, user-facing product ownership, API integration, authentication, relational data, testing, and production debugging are central.
- Treat roles as stronger matches when backend work is feature-level and can be supported by the existing Node.js/Express, Python/Pydantic, Supabase/PostgreSQL, Google identity, and API-contract projects.
- Treat backend-heavy roles as `Practice` or `Skip` when they require established professional ownership of distributed services, high-scale backend architecture, on-call operations, Kubernetes, networking, or infrastructure platforms.
- Never count a planned `english-learning` milestone as evidence. Promote it only after the repository evidence ledger records implementation and relevant local, CI, or deployed verification.

## Recent Assessed Practice

Use these completed sessions as interview-readiness evidence, not as professional experience:

- PostgreSQL schema tradeoffs (2026-07-16): the initial answer was `Weak / risky`; Joseph understood normalization, foreign keys, snapshots, and JSONB flexibility but needed more precise entity mapping, database invariants, concurrency, and explicit tradeoffs.
- API contract and full-stack error handling (2026-07-17): `Strong` on database-arbitrated idempotency and the external-provider failure window; `Acceptable but incomplete` on initial contract semantics, continuous job recovery, retry policy, state machines, and observability.
- RLS, AI structured output, and async recovery (week of 2026-07-26): demonstrated sound trust-boundary instincts, human review, tenant-sensitive authorization, durable job state, and provider idempotency. Remaining practice areas were old/new row precision, lease fencing, partial-failure recovery, bounded retry, and operational signals.
- Transactional concurrency (week of 2026-08-02): correctly combined idempotency, business uniqueness, database arbitration, and a short transaction for limited inventory. Remaining practice areas were lock granularity, invariant-first explanation, ambiguous commit recovery, and avoiding unnecessary async architecture.

Current calibration: project-level backend feature owner with assessed API/system-design practice and an operator-verified personal-service deployment/release rehearsal. This is sufficient to pursue frontend-heavy and product-oriented full-stack roles when backend ownership is feature-level. It also supports selective product-facing roles that expect containerization, migration, and staged-release judgment. Do not present Joseph as a professional production service/system owner; production observability, incident response, scaling, database-role verification, and sustained on-call ownership remain less evidenced.

## Interview Readiness Focus

Use `interview-readiness-priorities.md` as the canonical source for preparation priorities. The default
next investment is a measured frontend architecture/performance case study, connected to product-oriented
system design and the ability to explain and verify AI-assisted changes. Prioritize timed DSA when an
algorithm screen is a current preparation goal. TypeScript is a familiarity default; Joseph's language
choice or a supplied interview constraint takes precedence. Backend, cloud, and AI work should deepen
existing projects where a measured requirement or target role justifies it.

## Evidence Calibration

Use these levels when scoring jobs, writing fit notes, assessing readiness, or tailoring application materials:

1. **Demonstrated professionally:** Supported by shipped work, production ownership, measurable outcomes, or direct collaboration described in the resume.
2. **Implemented in a project:** Supported by repository code, project documentation, or a working artifact, but do not present it as production-scale professional ownership.
3. **Assessed in practice:** Supported by a completed interview drill or coaching session with a recorded evaluation of Joseph's own answer. Use it as readiness evidence, not work-experience evidence.
4. **Preparation material only:** Covered by a rubric, model answer, or uncompleted drill. Use it to recommend practice; do not increase fit or readiness because the material exists.

The files under `references/engineering-interview-drills/` are preparation material unless a session result records Joseph's performance. Do not infer that Joseph can defend every strong-answer signal merely because the repository contains the rubric.

## Preferred Market Position

Primary:
- Senior Frontend Engineer for complex product frontend, architecture, experimentation, performance, accessibility, design systems, realtime workflows, data visualization, or AI interfaces
- Frontend Platform Engineer / Web Platform UI Engineer
- Product Engineer when React/TypeScript and user-facing product-web ownership remain central

Secondary:
- Full-stack Product Engineer / Frontend-heavy Full-stack Engineer
- AI Product Engineer / LLM Application Engineer when user-facing frontend and product workflows remain central
- Developer Productivity Engineer / Developer Experience Engineer when frontend tooling, automation, internal workflows, or coding-agent workflows are central
- Forward Deployed Engineer / Solutions Engineer when hands-on implementation, integration, and product engineering are central

Lower priority:
- Pure backend/platform/infra unless product-facing and realistic for backend feature ownership.
- Pure ML research, model training, or deep ML infrastructure roles.
- Pure manual QA or repetitive validation roles.
- Semiconductor or hardware-adjacent roles without a meaningful software/application/product bridge.
