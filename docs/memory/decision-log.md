# Decision Log

Record durable repo decisions here. Use reverse chronological order.

## 2026-08-28: Keep Job Search Frontend-First While Expanding Full-stack Coverage

Decision: Keep Frontend Engineer and Senior Frontend Engineer as Joseph's first job-search priority. Treat Product Engineer and frontend-heavy Full-stack Engineer as the preferred growth lane, followed by frontend-centered AI Product roles.

Reasoning:

- Joseph's strongest professional evidence remains React/TypeScript product frontend, experimentation, product infrastructure, production debugging, and cross-functional delivery.
- Existing side projects support searching for feature-level full-stack work now, but do not establish professional backend service or platform ownership.
- The active `english-learning` training should strengthen full-stack ranking incrementally only when implementation and verification are recorded in its evidence ledger.

Implications:

- Daily job searches spend their first coverage on frontend and senior frontend queries.
- A full-stack title does not outrank a comparable frontend role unless substantial frontend ownership and better product or career scope are visible.
- Update shared candidate, targeting, project, and query references after verified training milestones without converting project evidence into professional production claims.

## 2026-08-02: Establish Repo Memory System

Decision: Add a root `AGENTS.md` plus `docs/memory/` files for durable repo memory.

Reasoning:

- Agents need a fast, repo-native orientation file before editing skills or references.
- The repo already uses `docs/` for documentation, so memory docs should live under `docs/memory/` instead of creating a competing top-level `doc/` directory.
- Shared personal context should remain in `references/`; memory docs should describe structure, conventions, and update rules.

Implications:

- Future durable repo knowledge should be captured in the smallest relevant `docs/memory/` file.
- Sensitive candidate facts should stay in `references/`, not `AGENTS.md`.
- Behavior-specific instructions still belong in the relevant `SKILL.md`.
