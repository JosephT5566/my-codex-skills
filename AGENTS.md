# Agent Instructions

This repository stores Joseph Tseng's personal Codex skills, shared reference material, and setup helpers. Treat it as a reusable knowledge/workflow repo, not an application codebase.

## Repository Map

- `*/SKILL.md`: top-level Codex skills. Each skill directory is intended to be symlinked into an agent skill directory.
- `*/agents/openai.yaml`: agent-specific metadata for skills that support OpenAI-style agents.
- `references/`: shared source-of-truth material used by several skills at runtime. This may include private career, resume, project, and search context.
- `docs/`: human-readable repo documentation and durable repo memory.
- `scripts/symlink_skills.py`: helper for linking skills into `~/.codex/skills` or another target directory.

## Working Rules

- Read the relevant `SKILL.md` before editing any skill behavior.
- Keep private candidate details out of `SKILL.md` files unless the detail is intentionally reusable instruction. Put source material in `references/` instead.
- Prefer updating shared references over duplicating the same context inside multiple skills.
- Keep skill instructions direct, operational, and testable. Avoid vague coaching language that does not change agent behavior.
- Preserve existing symlink assumptions: shared references are linked into selected skill folders by `scripts/symlink_skills.py`.
- Do not rewrite unrelated skills while changing one workflow.
- Use ASCII in new files unless an existing file clearly uses another character set.

## Memory System

Use `docs/memory/` for durable repo memory:

- [Repository Memory](docs/memory/repository-memory.md): stable facts about the repo structure, conventions, and maintenance model.
- [Skill Memory](docs/memory/skill-memory.md): current skill inventory, purpose, and cross-skill relationships.
- [Reference Memory](docs/memory/reference-memory.md): what belongs in shared references and how to handle private source material.
- [Workflow Memory](docs/memory/workflow-memory.md): repeatable maintenance, install, and verification workflows.
- [Decision Log](docs/memory/decision-log.md): dated decisions that should influence future edits.

When a change creates knowledge that future agents should rely on, update the smallest relevant memory file in the same commit. Do not put transient task notes, scratch analysis, or one-off conversation state into repo memory.

## Verification

For documentation-only edits, verify with:

```bash
git diff --check
```

For symlink or script changes, also run:

```bash
python3 scripts/symlink_skills.py --dry-run
```
