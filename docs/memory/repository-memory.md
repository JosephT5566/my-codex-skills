# Repository Memory

This repo is a personal Codex skills registry and source-of-truth workspace. It is organized around portable skills plus shared references that can be symlinked into multiple agent environments.

## Stable Structure

- Root-level directories that contain `SKILL.md` are installable skill directories.
- `references/` holds shared context used by multiple skills. Several skill instructions intentionally read these files at runtime instead of embedding personal details directly.
- `docs/` holds durable documentation for humans and future agents.
- `scripts/symlink_skills.py` discovers top-level skill directories and links them into a target skill folder.

## Maintenance Conventions

- Add new personal skills as top-level directories with a `SKILL.md`.
- Keep shared, reusable candidate/job-search/project context in `references/`.
- Keep broad repo memory in `docs/memory/`.
- Keep installation and setup instructions in `readme.md` or `docs/`.
- Use narrowly scoped edits. A skill behavior change should usually touch only that skill, its relevant references, and possibly the memory docs.

## Current Shared Reference Model

The repo currently uses a single shared `references/` directory for career and job-search context. `scripts/symlink_skills.py` links that directory into selected skill folders so skills can use local relative paths during execution.

Current shared-reference skills:

- `engineering-interview-coach`
- `linkedin-fresh-job-search`
- `tailored-resume-generator`

`jd-resume-fit-scorer` also reads shared references when available, but it is not currently listed in `SHARED_REFERENCE_SKILLS` in the symlink script.
