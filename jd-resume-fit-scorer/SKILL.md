---
name: jd-resume-fit-scorer
description: Evaluate how well a candidate's resume matches a specific job description using a recruiter-style 100-point score, evidence mapping, ATS keyword gaps, ten-second hiring-manager red flags, hard-screen risks, and application priority. Use when a user shares a job URL or JD and asks whether they are a fit, requests a resume score, wants missing keywords or red flags, compares several jobs, or asks which role is most worth applying to.
---

# JD Resume Fit Scorer

Assess the resume as a senior recruiter screening for the specific company and role. Be direct, evidence-based, and truthful.

## Gather Sources

1. Obtain the complete job description.
   - When given a URL, browse it and verify the current posting.
   - If the primary page is inaccessible, use indexed copies or reputable mirrors and clearly state that limitation.
   - Prefer the employer's official page when available.
2. Obtain the candidate source of truth in this order:
   - Resume or background supplied in the current request.
   - Candidate files in the current working folder, especially `resume-2026.md`, `candidate-profile.md`, and `project-signals.md`.
   - Shared sibling references:
     - `../tailored-resume-generator/references/resume-2026.md`
     - `../tailored-resume-generator/references/candidate-profile.md`
     - `../tailored-resume-generator/references/github-project-signals.md`
   - If the relative paths cannot be resolved, look under the common skill root for `tailored-resume-generator/references/`.
3. Ask for a resume only when no usable candidate source exists.
4. Treat the resume as authoritative. Use profile and project references only as supporting evidence.

Do not copy private candidate details into this skill. Read the shared references at run time so both skills use the same current data.

## Analyze the JD

Extract and classify:

- Minimum qualifications and explicit year thresholds
- Preferred qualifications
- Role family and expected seniority
- Required technologies, languages, platforms, and methodologies
- Customer, partner, leadership, or cross-functional expectations
- Domain requirements such as advertising, manufacturing, cloud, or AI
- Ownership expectations from discovery through launch, maintenance, and retirement
- Repeated and ATS-significant phrases

Separate actual hard requirements from examples. For example, a language listed after "such as" is not automatically mandatory.

## Map Candidate Evidence

For every important requirement, label the match:

- **Direct:** Explicitly demonstrated in the resume
- **Transferable:** Closely related evidence that can be credibly reframed
- **Wording gap:** Evidence exists but the JD terminology is absent
- **Experience gap:** No substantiated evidence
- **Hard-screen risk:** A minimum qualification appears unmet or ambiguous

Never invent experience or recommend inserting an unsupported keyword.

## Score Out of 100

Use this weighted rubric:

| Category | Points |
| --- | ---: |
| Minimum qualifications and seniority | 30 |
| Core technical skills and architecture | 20 |
| Role and industry/domain relevance | 20 |
| Scope, ownership, and measurable impact | 15 |
| Customer, partner, and cross-functional evidence | 10 |
| Resume positioning and ATS clarity | 5 |

Apply these principles:

- Award full credit only for explicit, substantiated evidence.
- Give partial credit for strong transferable evidence.
- Deduct meaningfully for each ambiguous or unmet minimum qualification.
- Do not let keyword overlap hide a seniority, customer-facing, or domain gap.
- Treat exact year thresholds using the dates shown in the resume and the current date.
- Explain the two or three factors that most affect the score.

Interpret the result:

- **90-100:** Excellent fit; high application priority
- **80-89:** Strong fit; tailor and apply
- **70-79:** Plausible fit; meaningful gaps or screening risk
- **60-69:** Stretch; apply selectively
- **Below 60:** Low-probability without new evidence

Also estimate a **tailored score ceiling**: the realistic score after truthful reordering and rewriting, without acquiring new experience.

## Identify Missing Keywords

List exactly five when the JD provides enough signal. Rank them by screening impact, not frequency alone.

For each keyword or phrase:

- Use the employer's terminology.
- State whether it is a wording gap or an experience gap.
- Point to transferable evidence when available.
- Avoid low-value generic words such as "teamwork" when a more specific technical or domain phrase matters.

## Identify Ten-Second Red Flags

List exactly three issues a recruiter or hiring manager is likely to notice immediately. Prioritize:

1. Unmet or borderline minimum qualifications
2. Resume identity that conflicts with the target role
3. Missing customer/domain/seniority evidence
4. Critical experience buried too low in the document
5. Unsupported senior title or insufficient scope

Describe observable resume signals, not personality judgments.

## Produce the Response

Reply in the user's language. Use this compact structure:

1. Role title and **overall score: X/100**
2. One short paragraph explaining the fit
3. JD source links and any source limitation
4. **Top five missing keywords**, numbered, with gap type and concise explanation
5. **Three ten-second red flags**, numbered
6. **Recruiter conclusion** with application priority
7. **Tailored score ceiling** and the highest-impact positioning changes

When the user has evaluated multiple roles, compare the new role against prior roles and update the application ranking when useful.

Do not generate a full rewritten resume unless requested. Keep scoring distinct from resume tailoring.
