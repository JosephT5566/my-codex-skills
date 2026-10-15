---
name: managing-shared-references
description: Use when new facts or learning material belong in a shared references folder, existing references conflict or need reorganization, or skills need to discover and use added, renamed, or moved references.
---

# Managing Shared References

Maintain canonical source material together with the skills that consume it. A reference update is complete when relevant consumers can find it and interpret its evidence correctly.

## Locate and Map

Resolve this skill's installed path through symlinks to its source directory; inspect its parent for the repository's `references/`, `AGENTS.md`, and `scripts/symlink_skills.py`. Otherwise use the user-specified repository or current workspace. If the repository is ambiguous, ask for its location. `/references` means repository-relative here, not the filesystem root.

Read repository instructions and `docs/memory/reference-memory.md` and `skill-memory.md` when present. Inventory filenames before loading content. Search skill instructions, supporting files, reference cross-links, memory, and symlink configuration for affected filenames and topic-routing rules. Read each affected `SKILL.md` before editing its behavior. Include indirect consumers using sibling-skill paths.

## Quick Reference

| Information | Usual canonical home in this repository |
| --- | --- |
| Positioning and calibrated experience | `references/candidate-profile.md` |
| Resume facts | `references/resume-2026.md` |
| Project implementation and verification | `references/github-project-signals.md` |
| Role preferences and screening | `references/career-targeting.md` |
| Training priorities | `references/interview-readiness-priorities.md` |
| Practice or delivery guidance | Matching drill or engineering-lifecycle reference |

Confirm current filenames and authority rules from the files themselves; this table is a starting point.

## Apply the Update

1. Separate supplied facts, verification evidence, learning material, and unresolved claims. Explicit user corrections supersede stale facts; preserve unrelated evidence. If a conflict cannot be resolved from the supplied material, ask the narrow question and continue independent updates. Record available source/date and verification limits beside changed claims. Keep professional, project, assessed-practice, planned, and unverified evidence distinct. A rubric does not establish capability.
2. Update the canonical file, then reconcile affected summaries. Keep private source material in shared references. Change skill instructions only for loading, routing, or interpretation behavior.
3. If promised source text is absent, request it and leave that reference and its new consumer routes pending. Complete supported changes independently. Author new learning material only when requested.
4. For a new reference, add a topic-based loading rule to each relevant consumer; preserve selective loading. For a rename or move, update direct and indirect paths plus cross-links in the same change. Follow each consumer's source precedence.
5. Preserve shared-directory symlinks. Inspect `SHARED_REFERENCE_SKILLS` before adding a consumer that needs skill-local references. An existing shared-directory link already exposes new files. Update the smallest relevant memory entry when inventory, routing, or conventions change.

## Example

"Worker implemented; retries unverified" updates project evidence and any affected profile summary. Keep the resume within supported claims. A supplied queue-recovery drill gets conditional routes in coaching and job search; an absent drill remains pending while fact corrections proceed.

## Verify and Report

Run `git diff --check`. For path or symlink changes, also run `python3 scripts/symlink_skills.py --dry-run`. Search for stale paths and resolve changed consumer paths through symlinks, including sibling-skill references. Read the diff for contradictory or inflated claims.

Report changed canonical files, affected consumers, checks performed, and pending material. Keep private details minimal.

## Common Mistakes

- Copying shared facts into skill instructions creates competing sources.
- Saving a new file without consumer routing leaves it undiscoverable.
- Wiring missing content creates a broken dependency.
- Replacing a reference symlink with a directory breaks sharing.
