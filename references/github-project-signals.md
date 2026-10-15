# GitHub / Side Project Signals

Use Joseph's public GitHub profile as supporting evidence when screening roles, tailoring resumes, and writing fit notes:

```text
https://github.com/JosephT5566
```

Maintained repo signals, with `english-learning` evidence updated through 2026-09-26 and `expense-app` semantic-entry evidence reviewed on 2026-10-15:

- `wedding-table-service` - Next.js/React/TypeScript wedding operations app with real-time Firestore data, responsive table visualization, fuzzy guest search, check-in/check-out, guest management, Google authentication, email-allowlisted writes, strict Firestore rules, and dry-run-first data migrations. Use as evidence for end-to-end product ownership, operational UX, Firebase security, real-time state, and schema migration work.
- `my-actions-runner` - GitHub Actions automation on a self-hosted runner for Codex CLI tasks, scheduled LinkedIn job search, JD/resume fit scoring, and tailored resume generation/export/upload to Google Drive. Use as evidence for developer tooling, workflow automation, reusable AI-agent skills, security-conscious prompt boundaries, artifact handling, and cross-tool orchestration.
- `expense-app` (JoPie) - Svelte 5/SvelteKit/TypeScript/Supabase expense PWA with a Python/FastAPI/LangGraph semantic-entry service and Gemini SSE integration. Use as project-level evidence for full-stack feature ownership, deterministic validation around LLM extraction, transactional request idempotency, bounded async streaming, uncertain-write recovery, and cross-language contracts. See [the scoped evidence below](#expense-app-semantic-entry-evidence-reviewed-2026-10-15); local fixtures and recorded tests do not establish hosted reliability, real-model quality, or professional backend operations ownership.
- `TravelSplit` + `google-api-gcf` - TypeScript travel/shared-expense product with a companion CommonJS Node.js/Express Google Cloud Function backed by Google Sheets. The service exposes REST-style `GET`, `POST`, and `DELETE` endpoints for health/configuration checks and expense reads, creation, and deletion; verifies Google ID tokens; uses service-account JWT access for Sheets; parses spreadsheet-hosted configuration; preserves a consistent response envelope; and synchronizes additions/deletions across participant tabs. Use as project-level evidence for lightweight full-stack product execution, REST API development, serverless HTTP APIs, OAuth-aware integration, spreadsheet-backed data contracts, and concurrent external-service workflows. Keep the evidence calibrated: the route names are action-oriented rather than fully resource-oriented, multi-tab writes/deletes are not atomic, `/data` verifies that the caller is allowlisted but does not bind the requested email to the verified token email, the legacy test scaffold is not runnable, direct runtime dependencies are incomplete, and deployment/operational ownership is not documented.
- `google-ai-gcf` - Python/Pydantic receipt-extraction backend integrated with Gemini and GCS. PRs #18-#22 add a canonical constrained schema, SDK structured responses, a versioned normalized `receipt-result.v1` contract, JWT-derived object ownership, MIME/size/generation and magic-byte checks, prompt-injection control-plane separation, sanitized errors, and negative-path short-circuit tests; the documented suite reached 97 tests. Use as project-level evidence for API contract design, AI application trust boundaries, authorization, input hardening, provider isolation, and backend testing. Do not present it as production service ownership: metrics/alerts, live smoke tests, retention policy, rollback, and runbook work were still identified as next steps.
- `my-codex-skills` - Codex skill repo with reusable job-search, resume, and adaptive engineering-interview workflows. Its interview drill library covers API contracts, transactional concurrency, async recovery, AI structured output, PostgreSQL schema tradeoffs, and Supabase RLS reasoning with follow-up ladders and evaluation anchors. Use as evidence for AI-assisted workflow design, agent instruction design, structured technical evaluation, and practical Codex/Gemini leverage. Do not treat the drill rubrics themselves as proof of production backend ownership or completed interview mastery.
- `my-oauth` - TypeScript auth/OAuth project. Use as supporting evidence for auth flows, integrations, and web security basics when relevant.
- `musicFest` - TypeScript RWD mobile-first planning tool for music festivals. Use as evidence for responsive UX, mobile workflow design, and consumer-facing scheduling/planning tools.
- `english-learning` - Deployed SvelteKit and FastAPI/PostgreSQL English/Japanese learning product migrated from Google Sheets. Evidence includes controlled import/reconciliation tooling, reversible Alembic migrations, composite owner constraints, authenticated owner-scoped APIs, keyset pagination, locked/idempotent review transactions, frontend cutover, a numeric non-root container, Cloud Run/Neon deployment workflows, zero-traffic candidate verification, promotion, schema-compatible rollback, health checks, operational exercises, and deployed owner-safe semantic retrieval. Use as project evidence for end-to-end product migration, relational integrity, authorization, transactions, release safety, operational judgment, pgvector retrieval, and evidence-driven engineering. Keep claims bounded: some production results are operator-reported; initial restored-data reconciliation, independent IAM/role artifacts, and complete alert-delivery proof remain incomplete; retrieval quality remains under the frozen Issue #41 evaluation; no professional production-scale reliability claim is supported.

Do not overstate side projects as production-scale work unless the repo itself clearly shows that. Treat them as interview conversation starters and proof of initiative, not as primary work experience.

When a promising role overlaps with a side project, add a short fit note such as:

- Side-project proof: JoPie combines Svelte/TypeScript product UI with Python/FastAPI/LangGraph, caller-scoped transactional writes, bounded Gemini SSE, and failure recovery; supports frontend-heavy full-stack and applied-AI feature roles alongside Houzz frontend experience.
- Side-project proof: wedding-table-service shows real-time Firebase operations, access control, schema migration, and responsive UX.
- Side-project proof: my-actions-runner shows GitHub Actions, self-hosted automation, Codex skill orchestration, and Google Drive delivery.
- Side-project proof: google-ai-gcf shows Python/Pydantic API boundaries, Gemini structured output, GCS ownership controls, versioned normalization, and security-focused negative tests.
- Side-project proof: TravelSplit + google-api-gcf show a TypeScript product with Node.js/Express REST-style APIs, Google identity verification, and Google Sheets workflow automation.
- Side-project proof: musicFest shows mobile-first RWD planning UX.
- Side-project proof: my-codex-skills shows AI-assisted workflow design and structured technical evaluation across job search, resume, and engineering-interview workflows.
- Side-project proof: english-learning shows a deployed multilingual SvelteKit/FastAPI/PostgreSQL product with owner-scoped APIs, transactional idempotent reviews, controlled migration, release/rollback workflows, and owner-safe semantic retrieval.

## Expense-app semantic-entry evidence (reviewed 2026-10-15)

**Evidence level:** implemented in a personal project. Current source and named test definitions were inspected on 2026-10-15 at local HEAD `03c734315e740c0da04cebacde808ed5b0009a4d`; tests were not rerun for this reference update. Counts below are historical repository-recorded verification, not fresh results. Plans contain superseded Node/Starlette/provider/category details; current source and dated verification take precedence. This evidence does not independently establish line-by-line authorship or interview mastery; describe Joseph's actual design, implementation, review, and AI-assisted contributions accurately.

### Skills and concrete implementation

| Skill | Implementation evidence | Source paths in `expense-app` |
| --- | --- | --- |
| Python backend architecture | FastAPI/Uvicorn HTTP service with explicit LangGraph authentication, trusted context, replay, quota, extraction, deterministic validation, clarification, and persistence stages. Completed replay skips model and quota. | `services/semantic-entry/semantic_entry/{server,graph,normalize,clarification,supabase}.py` |
| PostgreSQL transactions and concurrency | Caller-scoped UUID and normalized payload hash; unique request identity, row locking, one transaction for expense plus saved result, conflict rejection, and snapshot replay. Local integration tests cover matching concurrent requests, rollback, user isolation, edits/deletion, grants, and quota. | `supabase/migrations/202610120001_semantic_entry.sql`, `services/semantic-entry/tests/test_db_integration.py` |
| Async streaming and protocol handling | Incremental SSE/JSON-string decoding handles fragmented UTF-8, escapes and surrogate pairs. Frame/model text caps, a bounded 64-event queue, backpressure, total deadlines, and disconnect handling bound the operation. Only a complete validated provider envelope can reach persistence. | `services/semantic-entry/semantic_entry/{provider_stream,provider,handler}.py`, `tests/{test_provider_stream,test_stream_transport}.py` under the service |
| LLM trust boundaries | Gemini produces extraction and a short user-facing summary; deterministic rules decide validity, fixed clarification, and writes. Summary stays outside persisted graph state and cannot override missing fields. One provider call per round, bounded follow-ups, no automatic model retries. | `services/semantic-entry/semantic_entry/{contracts,prompt,graph,normalize,clarification}.py` |
| Full-stack recovery and privacy | Cancels extraction on disconnect before persistence; an accepted write may continue within its deadline. UI retains uncertainty, freezes in-memory retry payloads, stores only an account-scoped pending UUID, and guards stale responses across account/lifecycle changes. Status recovery avoids blindly recreating an expense. | `services/semantic-entry/semantic_entry/handler.py`, `src/lib/data/semantic-entry.fetcher.ts`, `src/lib/components/semantic-entry/SemanticEntryContent.svelte`, `e2e/semantic-entry.test.ts` |
| Contract compatibility and verification | Version-negotiated SSE analysis events preserve legacy behavior; Python/TypeScript parity checks cover request normalization/hashes and real synthetic responses/events. Real localhost socket tests establish incremental arrival and disconnect boundaries beyond whole-response mocks. | `packages/semantic-entry-contract/{src/index.ts,tests/python-parity.mjs}`, `services/semantic-entry/tests/test_stream_transport.py` |

### Recorded verification and limits

- 2026-10-14 streaming record: 187 backend tests passed; 38 Playwright scenarios passed at root and again under `/expense-app`. These are the same browser suite in two deployment-path configurations, not 76 distinct scenarios.
- The same record reports Ruff/mypy, Python/browser parity, Docker build and synthetic container smoke passing; fixture evaluation covered 40 authored cases and 120 observations with zero failures and zero paid calls. Repeated fixture observations are not independent model samples or evidence of extraction accuracy.
- 2026-10-12 Python migration record: 14 SQL integration tests passed against disposable localhost PostgreSQL/PostgREST, covering concurrency, rollback, replay, grants, and quota. This is historical fixture evidence, not production GoTrue/RLS acceptance.
- Review-driven regressions addressed a full-queue persistence/cancellation race and acceptance of trailing events after a terminal result. Use these as concrete debugging and review examples, not as proof of incident/on-call ownership.
- Whole-repository lint remained failed on 122 pre-existing Prettier files; changed-file lint passed. Do not claim all checks passed.
- Hosted Gemini schema support, completion within the token cap, actual token/cost and latency measurements, Cloud Run buffering/instance termination, and end-to-end hosted auth/write/RLS acceptance were not established by the cited streaming tests. Database adoption has a separate dated record; do not generalize the earlier local-only SQL scope into a claim that no later remote database action occurred.
- Cloud Run container and workflow files support implementation/containerization claims. They do not by themselves prove a successful hosted deployment, production-scale reliability, measured performance improvement, or professional backend/platform ownership. No new operator-reported acceptance evidence was supplied for this update.

### Resume wording supported by this evidence

Select only bullets relevant to the target role and consistent with Joseph's actual contribution:

- Built a semantic expense-entry workflow using Python, FastAPI, LangGraph, and Supabase, combining structured LLM extraction with deterministic validation and bounded clarification.
- Implemented transactional request idempotency with caller-scoped UUIDs, payload hashes, and row locking, with local integration coverage for concurrency, rollback, conflicts, and replay.
- Delivered backward-compatible SSE streaming across Python and Svelte/TypeScript, handling incremental Unicode decoding, backpressure, cancellation, and recovery from uncertain writes.

### Source references

Paths are relative to the sibling `expense-app` checkout. They identify local review material; do not assume these revisions are published or that every GitHub link is available.

- [Semantic-entry implementation plan](../../expense-app/docs/superpowers/plans/2026-10-11-semantic-expense-entry.md)
- [Gemini streaming implementation plan](../../expense-app/docs/superpowers/plans/2026-10-14-gemini-streaming-analysis.md)
- [Semantic-entry evidence index and historical SQL verification](../../expense-app/docs/evidence/semantic-entry/README.md)
- [Streaming verification and review fixes](../../expense-app/docs/evidence/semantic-entry/2026-10-14-streaming-analysis.md)
- [Database baseline and adoption scope](../../expense-app/docs/evidence/semantic-entry/2026-10-13-database-baseline.md)
- [Current architecture](../../expense-app/docs/architecture.md) and [service contracts](../../expense-app/docs/database.md#semantic-entry-service)

## Project Leverage Plan

Joseph can use Gemini/Codex to polish side projects into stronger application assets. When ranking a role, consider whether one targeted project improvement could make the application materially stronger within 1-2 days.

High-leverage project upgrades:

- Add concise READMEs with problem, user workflow, tech stack, architecture notes, screenshots/GIFs, and deployment links; prioritize `wedding-table-service`, whose current README focuses mostly on setup.
- Add small test coverage or typed validation for the core workflow.
- For `google-api-gcf`, bind `/data` access to the verified caller, add request-schema validation and runnable endpoint tests, declare all direct dependencies, and define idempotency or recovery behavior for partial multi-tab writes/deletes before presenting it as production-ready backend work.
- For `google-ai-gcf`, prioritize production-facing gaps already identified in the project review: metrics/alerts and correlation tracing, a real Gemini/GCS smoke test, retention/privacy policy, rollback, service ownership, and a concise runbook.
- For `english-learning`, finish the frozen retrieval evaluation and close the remaining operational evidence gaps: restored-data reconciliation, independent runtime-role/IAM capture, response-ID correlation, and alert-delivery verification. Add an AI authoring or durable async path only after requirements, trust boundaries, human approval, and measured latency/failure behavior justify it.
- Add one polished demo path per repo, especially for `expense-app`, `TravelSplit`, `musicFest`, and `english-learning`.
- Add AI/Codex notes only when relevant: describe how AI accelerated implementation, testing, refactoring, or workflow design without implying the project was not personally owned.
- For frontend/product roles, prioritize visible UX polish, responsive screenshots, loading/empty/error states, and one measurable product decision.
- For automation/integration roles, prioritize API/auth/App Script explanations, data flow diagrams, and reliability notes.

Use this project evidence to boost roles involving:

- Frontend product engineering
- React/Svelte/TypeScript web apps
- Workflow/productivity tools
- Consumer mobile-web/RWD UX
- Spreadsheet, Apps Script, or lightweight automation integrations
- Node.js/Express REST API and serverless API roles involving Google identity and Sheets integration
- Frontend-heavy and product-oriented full-stack roles where feature-level API, auth, relational-data, migration, and failure-handling judgment matter
- AI-assisted product engineering or developer tooling
- Applied AI services with structured output, human-review boundaries, provider isolation, or permission-aware data access
- Python/Pydantic API contracts and security-focused backend validation
- FastAPI/PostgreSQL product-backend roles involving relational constraints, migrations, owner isolation, deterministic pagination, transactions, concurrency, or idempotency
- Firebase/Firestore operational tools with authenticated writes
- GitHub Actions and self-hosted workflow automation

Do not boost roles primarily focused on backend infrastructure, hardware, QA/testing-only, pure ML research, or data engineering solely because a side project exists.
