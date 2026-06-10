## Skill Registry

Portable notes for installed skills and suggested prompt patterns:

- [docs/codex-skills.md](docs/codex-skills.md)

## Symlink the skills
Link the skills in this repo to Codex:

```
python3 scripts/symlink_skills.py
```

Preview changes first:

```
python3 scripts/symlink_skills.py --dry-run
```

If a non-symlink skill already exists at the destination, back it up and replace it with a symlink:

```
python3 scripts/symlink_skills.py --backup-existing
```

The script also maintains shared `references/` links for skills that use the common candidate/job-search reference files.

To link skills for agents that read `~/.agents/skills`:

```
python3 scripts/symlink_skills.py --target ~/.agents/skills
```

## Install the skill
Or we can install the skill through `npx skills`

[vercel-lab/skill](https://github.com/vercel-labs/skills)

### find skill
Take `find-skill` installation for example

By default
```
npx skills add https://github.com/vercel-labs/skills
```
In the install, it asks about the **Installation scope**
- Project: It installs the skill to the *current* path.
- Global: It installs the skill to the `~/.agents/skills` and the agent is able to read it automatically.
