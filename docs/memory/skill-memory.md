# Skill Memory

This file records the repo's active skill inventory and how the skills relate to each other.

## Active Skills

| Skill | Primary purpose | Key dependencies |
| --- | --- | --- |
| `engineering-interview-coach` | Adaptive backend, full-stack, and system-design interview coaching. | Reads candidate profile, resume, GitHub project signals, and drill references. |
| `jd-resume-fit-scorer` | Recruiter-style JD/resume scoring with evidence mapping and ATS gaps. | Reads resume/profile/project references when available. |
| `linkedin-fresh-job-search` | Fresh LinkedIn-first job discovery and application prioritization. | Reads candidate profile, career targeting, source links, query strategy, and project signals. Uses live browser context for LinkedIn/Sheets workflows. |
| `markdown-resume-exporter` | Converts Markdown resumes or similar documents into PDF, DOCX, HTML, or text. | Uses bundled export script and CSS. Does not rewrite content. |
| `tailored-resume-generator` | Tailors resumes to specific job descriptions. | Reads shared resume, candidate profile, and project signals when available. |

## Cross-Skill Boundaries

- Resume writing belongs in `tailored-resume-generator`.
- Resume export mechanics belong in `markdown-resume-exporter`.
- Job fit scoring belongs in `jd-resume-fit-scorer`.
- Job discovery and prioritization belong in `linkedin-fresh-job-search`.
- Interview practice and answer evaluation belong in `engineering-interview-coach`.

## Update Guidance

- When adding a new skill, add it to this inventory and decide whether it should use `references/`.
- If a skill needs shared references symlinked into its directory, update `SHARED_REFERENCE_SKILLS` in `scripts/symlink_skills.py`.
- Keep each `SKILL.md` reusable. Store personal facts in references and operational behavior in the skill file.
