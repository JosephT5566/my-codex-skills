# Decision Log

Record durable repo decisions here. Use reverse chronological order.

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
