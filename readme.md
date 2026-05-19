```
for skill_dir in /Users/joseph/Documents/Git/my-codex-skills/*; do
  if [ -d "$skill_dir" ] && [ -f "$skill_dir/SKILL.md" ]; then
    ln -sfn "$skill_dir" "$HOME/.codex/skills/$(basename "$skill_dir")"
  fi
done
```
