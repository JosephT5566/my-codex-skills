# GitHub / Side Project Signals

Use Joseph's public GitHub profile as supporting evidence when screening roles, tailoring resumes, and writing fit notes:

```text
https://github.com/JosephT5566
```

Maintained repo signals, with project evidence updated through 2026-08-26:

- `wedding-table-service` - Next.js/React/TypeScript wedding operations app with real-time Firestore data, responsive table visualization, fuzzy guest search, check-in/check-out, guest management, Google authentication, email-allowlisted writes, strict Firestore rules, and dry-run-first data migrations. Use as evidence for end-to-end product ownership, operational UX, Firebase security, real-time state, and schema migration work.
- `my-actions-runner` - GitHub Actions automation on a self-hosted runner for Codex CLI tasks, scheduled LinkedIn job search, JD/resume fit scoring, and tailored resume generation/export/upload to Google Drive. Use as evidence for developer tooling, workflow automation, reusable AI-agent skills, security-conscious prompt boundaries, artifact handling, and cross-tool orchestration.
- `expense-app` - Svelte app, recently active in May 2026. Use as evidence for modern frontend app ownership, product UI, and personal finance/tooling workflows.
- `TravelSplit` + `google-api-gcf` - TypeScript travel/shared-expense product with a companion CommonJS Node.js/Express Google Cloud Function backed by Google Sheets. The service exposes REST-style `GET`, `POST`, and `DELETE` endpoints for health/configuration checks and expense reads, creation, and deletion; verifies Google ID tokens; uses service-account JWT access for Sheets; parses spreadsheet-hosted configuration; preserves a consistent response envelope; and synchronizes additions/deletions across participant tabs. Use as project-level evidence for lightweight full-stack product execution, REST API development, serverless HTTP APIs, OAuth-aware integration, spreadsheet-backed data contracts, and concurrent external-service workflows. Keep the evidence calibrated: the route names are action-oriented rather than fully resource-oriented, multi-tab writes/deletes are not atomic, `/data` verifies that the caller is allowlisted but does not bind the requested email to the verified token email, the legacy test scaffold is not runnable, direct runtime dependencies are incomplete, and deployment/operational ownership is not documented.
- `google-ai-gcf` - Python/Pydantic receipt-extraction backend integrated with Gemini and GCS. PRs #18-#22 add a canonical constrained schema, SDK structured responses, a versioned normalized `receipt-result.v1` contract, JWT-derived object ownership, MIME/size/generation and magic-byte checks, prompt-injection control-plane separation, sanitized errors, and negative-path short-circuit tests; the documented suite reached 97 tests. Use as project-level evidence for API contract design, AI application trust boundaries, authorization, input hardening, provider isolation, and backend testing. Do not present it as production service ownership: metrics/alerts, live smoke tests, retention policy, rollback, and runbook work were still identified as next steps.
- `my-codex-skills` - Codex skill repo with reusable job-search, resume, and adaptive engineering-interview workflows. Its interview drill library covers API contracts, transactional concurrency, async recovery, AI structured output, PostgreSQL schema tradeoffs, and Supabase RLS reasoning with follow-up ladders and evaluation anchors. Use as evidence for AI-assisted workflow design, agent instruction design, structured technical evaluation, and practical Codex/Gemini leverage. Do not treat the drill rubrics themselves as proof of production backend ownership or completed interview mastery.
- `my-oauth` - TypeScript auth/OAuth project. Use as supporting evidence for auth flows, integrations, and web security basics when relevant.
- `musicFest` - TypeScript RWD mobile-first planning tool for music festivals. Use as evidence for responsive UX, mobile workflow design, and consumer-facing scheduling/planning tools.
- `english-learning` - Svelte learning app. Use as evidence for personal productivity, learning workflows, and durable app ownership.

Do not overstate side projects as production-scale work unless the repo itself clearly shows that. Treat them as interview conversation starters and proof of initiative, not as primary work experience.

When a promising role overlaps with a side project, add a short fit note such as:

- Side-project proof: Svelte/TS expense app + Houzz frontend product work.
- Side-project proof: wedding-table-service shows real-time Firebase operations, access control, schema migration, and responsive UX.
- Side-project proof: my-actions-runner shows GitHub Actions, self-hosted automation, Codex skill orchestration, and Google Drive delivery.
- Side-project proof: google-ai-gcf shows Python/Pydantic API boundaries, Gemini structured output, GCS ownership controls, versioned normalization, and security-focused negative tests.
- Side-project proof: TravelSplit + google-api-gcf show a TypeScript product with Node.js/Express REST-style APIs, Google identity verification, and Google Sheets workflow automation.
- Side-project proof: musicFest shows mobile-first RWD planning UX.
- Side-project proof: my-codex-skills shows AI-assisted workflow design and structured technical evaluation across job search, resume, and engineering-interview workflows.

## Project Leverage Plan

Joseph can use Gemini/Codex to polish side projects into stronger application assets. When ranking a role, consider whether one targeted project improvement could make the application materially stronger within 1-2 days.

High-leverage project upgrades:

- Add concise READMEs with problem, user workflow, tech stack, architecture notes, screenshots/GIFs, and deployment links; prioritize `wedding-table-service`, whose current README focuses mostly on setup.
- Add small test coverage or typed validation for the core workflow.
- For `google-api-gcf`, bind `/data` access to the verified caller, add request-schema validation and runnable endpoint tests, declare all direct dependencies, and define idempotency or recovery behavior for partial multi-tab writes/deletes before presenting it as production-ready backend work.
- For `google-ai-gcf`, prioritize production-facing gaps already identified in the project review: metrics/alerts and correlation tracing, a real Gemini/GCS smoke test, retention/privacy policy, rollback, service ownership, and a concise runbook.
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
- AI-assisted product engineering or developer tooling
- Applied AI services with structured output, human-review boundaries, provider isolation, or permission-aware data access
- Python/Pydantic API contracts and security-focused backend validation
- Firebase/Firestore operational tools with authenticated writes
- GitHub Actions and self-hosted workflow automation

Do not boost roles primarily focused on backend infrastructure, hardware, QA/testing-only, pure ML research, or data engineering solely because a side project exists.
