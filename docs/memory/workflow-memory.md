# Workflow Memory

This file records repeatable maintenance workflows for this repo.

## Link Skills

Preview symlink changes:

```bash
python3 scripts/symlink_skills.py --dry-run
```

Link skills into the default Codex skill directory:

```bash
python3 scripts/symlink_skills.py
```

Link skills into an alternate agent skill directory:

```bash
python3 scripts/symlink_skills.py --target ~/.agents/skills
```

If a non-symlink path already exists at the destination, use:

```bash
python3 scripts/symlink_skills.py --backup-existing
```

## Add Or Update A Skill

1. Edit the relevant top-level `SKILL.md`, or create a new top-level skill directory with `SKILL.md`.
2. Put reusable source material in `references/` rather than duplicating it in the skill.
3. If the skill needs shared references through a local `references` path, update `SHARED_REFERENCE_SKILLS` in `scripts/symlink_skills.py`.
4. Update [Skill Memory](skill-memory.md) and any relevant reference notes.
5. Run:

```bash
python3 scripts/symlink_skills.py --dry-run
git diff --check
```

## Documentation-Only Changes

For docs and memory-only updates:

```bash
git diff --check
```

Also check links manually when moving or renaming docs.
