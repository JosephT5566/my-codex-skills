## Symlink the skills
Link the skills in this repo to the local agent, like codex.
```
for skill_dir in /Users/joseph/Documents/Git/my-codex-skills/*; do
  if [ -d "$skill_dir" ] && [ -f "$skill_dir/SKILL.md" ]; then
    ln -sfn "$skill_dir" "$HOME/.codex/skills/$(basename "$skill_dir")"
  fi
done
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