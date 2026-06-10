---
name: linkedin-fresh-job-search
description: LinkedIn-first fresh job-search workflow with optional CakeResume coverage for Taiwan roles. Use when the user asks to identify newly posted high-probability roles, filter out old postings, rank jobs by interview likelihood, create a job-search sheet, or run a daily job-search workflow using LinkedIn, CakeResume, and Chrome.
---

# LinkedIn Fresh Job Search

Use this skill to prioritize jobs where the user can apply before applicant volume builds up. Optimize for interview probability, not just raw job count. LinkedIn is the primary source; CakeResume is a supplemental Taiwan-focused source.

## Run Modes

Choose the lightest mode that satisfies the request.

### Daily Light Run

Use this by default when the user asks for today's jobs or does not specify depth.

- Search LinkedIn first with 3-5 focused queries.
- Target 10 screened roles, with at least 5 credible `Apply Today` or `Maybe` leads when the market permits.
- Stop after 10 qualified roles are verified or 15 direct postings are screened, whichever comes first.
- Search CakeResume only when LinkedIn yields fewer than 8 qualified roles.
- Do not run every adjacent query. Rotate one high-signal adjacent family per day based on recent tracker coverage.
- Update one dated tracker tab. If today's tab already exists, update it rather than creating a duplicate.

### Deep Search Run

Use when the user explicitly requests a comprehensive search, comparison across sources, or a weekly refresh.

- Search LinkedIn across primary, adjacent, and APAC-remote families.
- Expand from past 24 hours to past 3 days.
- Search CakeResume even when the LinkedIn pool is sufficient.
- Target 15-25 screened roles and refresh stale role-priority assumptions.
- Run this at most once or twice per week unless the user explicitly requests otherwise.

## Core Policy

- Treat **Past 24 hours** as the first-pass search window.
- Use **Past 3 days** as the fallback expansion window.
- Ignore postings older than 3 days unless the user explicitly asks, the fit is exceptional, or there is a referral/recruiter path.
- Explain that LinkedIn result counts are noisy search-volume indicators, not counts of perfect-fit jobs.
- Complete the LinkedIn first pass before searching CakeResume.
- Use CakeResume to supplement a thin LinkedIn pool, discover Taiwan-local employers, or find roles not present on LinkedIn. Do not let CakeResume displace stronger fresh LinkedIn matches.
- Treat CakeResume listings without a verifiable posted or updated date as `Freshness unknown`. They may be `Maybe`, but not `Apply Today` based on freshness alone.

## Workflow

1. Establish candidate profile signal.
   - Prefer the user's resume, LinkedIn profile, or stated background.
   - If available, read `references/candidate-profile.md` for a compact maintained profile snapshot.
   - If available, read `references/job-search-sources.md` for the canonical tracking sheet or source links.
   - If available, read `references/github-project-signals.md` for side-project evidence that can strengthen fit notes and resume targeting.
   - Use the Chrome skill/plugin for live LinkedIn and CakeResume searching and for updates to the existing `2026 interview` Google Sheet because these workflows may depend on the user's logged-in browser account.
   - Keep this workflow browser-only. If Chrome cannot access the tracker, stop and report the Chrome blocker instead of creating or updating a replacement through another account.
   - Do not inspect cookies, local storage, passwords, or private session stores.

2. Build target role searches.
   - Start from role labels that match the user's strongest evidence.
   - Add broader aliases for volume and narrower aliases for precision.
   - For a Daily Light Run, start with these four core LinkedIn queries:
     - `Frontend Engineer React TypeScript`
     - `Software Engineer Frontend React`
     - `Product Engineer React`
     - `Full Stack Product Engineer React`
   - Add one rotating adjacent query only when useful:
     - QA/quality day: `QA Automation Engineer SQL`
     - ATE/test day: `ATE Software Engineer C++ C#`
     - AI application day: `AI Application Engineer Workflow`
     - Tools/integration day: `Developer Tools Engineer TypeScript` or `Solutions Engineer JavaScript`
   - Check the most recent dated tracker tab before choosing the rotating query. Prefer a family that was not searched in the previous run.
   - For Joseph Tseng, default strong role families are:
     - Frontend Engineer / Frontend Developer
     - Software Engineer, Frontend / Web Engineer
     - Senior Frontend Engineer
     - React / TypeScript Engineer
     - Frontend-heavy Full Stack Engineer
     - Search / Marketplace Frontend Engineer
     - AI Product / AI-Native Web Engineer
     - CMS / Campaign Frontend Engineer
     - Product Engineer with React/TypeScript product-web scope
     - Developer Experience / Internal Tools Engineer with frontend tooling scope
     - Solutions Engineer / Implementation Engineer for web, SaaS, CMS, e-commerce, or workflow automation products
   - For Joseph Tseng, default adjacent role families are:
     - Product Engineer / Full Stack Product Engineer
     - Web Platform UI Engineer
     - Developer Tools / Developer Experience Engineer
     - Internal Tools Engineer
     - Solutions Engineer
     - Implementation Engineer / Forward Deployed Engineer
     - Technical Product Manager only when the posting values hands-on engineering/product delivery evidence
     - Software QA Engineer / QA Engineer only when the role emphasizes test planning, release quality, debugging, automation, or engineering coordination
     - Validation Engineer / System Validation Engineer with software, firmware, application, or product-quality scope
     - Application Engineer / Field Application Engineer for semiconductor, hardware, SaaS, CMS, e-commerce, or technical product roles
     - Technical Project Engineer / Technical Program Engineer when engineering coordination and quality ownership are central
   - For Joseph Tseng, default LinkedIn query set:
     - `Frontend Engineer React TypeScript`
     - `Frontend Developer React TypeScript`
     - `Software Engineer Frontend React`
     - `Web Engineer TypeScript`
     - `Product Engineer React`
     - `Full Stack Product Engineer React`
     - `Frontend-heavy Full Stack Engineer`
     - `React TypeScript Engineer`
     - `Marketplace Frontend Engineer`
     - `Search Frontend Engineer`
     - `E-commerce Frontend Engineer`
     - `CMS Frontend Engineer`
     - `Campaign Frontend Engineer`
     - `AI Product Engineer React`
     - `AI Native Web Engineer`
     - `Developer Experience Engineer Frontend`
     - `Developer Tools Engineer TypeScript`
     - `Internal Tools Engineer React`
     - `Solutions Engineer JavaScript`
     - `Implementation Engineer React`
     - `Forward Deployed Engineer TypeScript`
     - `Technical Product Manager Web Platform`
     - `QA Engineer Software`
     - `Software QA Engineer`
     - `Validation Engineer Software`
     - `System Validation Engineer`
     - `Application Engineer Semiconductor`
     - `Field Application Engineer Software`
     - `Technical Project Engineer`
     - `Technical Program Engineer`
     - `Customer Quality Engineer Software`
     - `Product Quality Engineer Software`
   - For Joseph Tseng, prioritize these high-signal adjacent queries before broad semiconductor/QA searches:
     - `ATE Testing Software Engineer C#`
     - `ATE Software Engineer C++ C#`
     - `Software Engineer ATE Testing`
     - `QA Automation Engineer SQL`
     - `Software Quality Engineer Automation SQL`
     - `AI Application Architect`
     - `AI Application Engineer Workflow`
     - `Digital Transformation AI Application`
     - `Application Engineer Test Equipment`
     - `Application Engineer Power Supply C++`
   - Treat broad queries such as `Application Engineer Semiconductor`, `Validation Engineer Software`, and `Technical Project Engineer` as discovery pools only. Screen individual jobs carefully before ranking them.

3. Search sources, freshness windows, and geographies.
   - First run LinkedIn searches with `f_TPR=r86400` for past 24 hours.
   - Expand to `f_TPR=r259200` only when fewer than 8 qualified roles remain after deduplication and basic screening.
   - In a Daily Light Run, search CakeResume only when LinkedIn still yields fewer than 8 qualified roles after the 3-day expansion.
   - In a Deep Search Run, search CakeResume after LinkedIn regardless of count.
   - On CakeResume, reuse the highest-signal role queries rather than running the entire broad query set. Start with frontend, React/TypeScript, product engineer, QA automation, ATE software, and AI application searches.
   - In a Daily Light Run, use at most two CakeResume queries and stop when the combined qualified pool reaches 10 roles.
   - Prefer CakeResume listings with an explicit posted or updated time within 3 days. Record the displayed wording exactly.
   - If CakeResume exposes no reliable date, record `Freshness unknown` and rank conservatively.
   - Open and screen the direct CakeResume job page. Do not use a generic search-results URL for a selected lead.
   - Deduplicate by normalized company name plus role title. When the same opening appears on LinkedIn and CakeResume, keep one row and prefer the source with clearer freshness, applicant-volume, recruiter, or application-path signals. LinkedIn remains the default canonical source when signals are otherwise equal.
   - For Joseph Tseng, default the location focus to Taiwan/Taipei first, especially `Taipei City, Taiwan`, unless the user asks for another geography.
   - Expand beyond Taiwan for remote roles when the posting is plausibly open to Taiwan-based candidates. Prioritize APAC remote, Asia remote, Taiwan remote, global/worldwide remote, and Singapore or Hong Kong remote-friendly roles.
   - Treat United States-only remote searches as a selective stretch pool, not the default. Include US remote roles only when the posting is an unusually strong React/TypeScript/product-frontend match and does not require US work authorization, US payroll, or strict US-only location.
   - Keep location, remote, hybrid, and onsite preferences aligned with the user's profile or request.

4. Screen and rank.
   - Score fit over raw count. A smaller fresh search with high title/skill match can beat a larger noisy search.
   - Apply a two-stage screen:
     - Search-card screen: reject obvious wrong-discipline, wrong-location, old, or seniority-mismatch results without opening them.
     - Direct-posting screen: open only plausible leads to verify freshness, location, role scope, applicant signal, and direct URL.
   - Do not fully read every plausible description during discovery. Capture enough evidence to rank it, then reserve detailed JD analysis for roles marked `Apply Today`.
   - Deduplicate before opening more postings so repeated sponsored or cross-query results do not consume the screening budget.
   - Favor postings with:
     - exact or near-exact title match
     - React/TypeScript/frontend/product-web requirements
     - marketplace, e-commerce, search, CMS, experimentation, GraphQL, or AI-product overlap
     - product engineering, developer tooling, internal tooling, implementation, or solutions-engineering roles where React/TypeScript/web integration remains central
     - QA, validation, application engineering, field application, customer quality, or technical project roles where test planning, root-cause debugging, release quality, production issue investigation, external/customer communication, or cross-functional engineering coordination are central
     - ATE/software-test roles using C/C++/C#, .NET, REST/WebSockets, data acquisition, device communication, debugging, documentation, and cross-functional hardware/test/system collaboration
     - AI application or digital transformation roles focused on workflow design, AI use-case definition, enterprise application patterns, stakeholder communication, delivery quality, and practical product outcomes
     - posted within 24 hours
     - low applicant count
     - explicit recent posted or updated time on CakeResume
     - remote eligibility for Taiwan/APAC/global candidates when outside Taiwan
     - active recruiter, alumni, shared connections, or direct hiring-manager signal
   - Penalize:
     - pure ML/data/AI research roles when the user's proof is frontend/product
     - backend/platform/infra roles unless clearly frontend-heavy
     - solutions, implementation, or TPM roles that are mostly account management, project coordination, or support without meaningful technical/product-building scope
     - manual QA roles focused mainly on repetitive scripted testing without technical debugging, automation, release ownership, or engineering coordination
     - semiconductor validation or customer quality roles requiring deep device physics, wafer process ownership, or hardware lab specialization without a software/application bridge
     - principal/staff application roles requiring 10+ years of deep semiconductor power-electronics expertise, SiC/GaN device mastery, circuit design, PCB layout, or lab-heavy power validation
     - cybersecurity testing roles requiring penetration-testing specialization, IEC 62443/RED/CRA ownership, OSCP/CPENT-style credentials, or security domain depth unless the user explicitly targets cybersecurity
     - technical project roles dominated by industrial automation project delivery, process-industry site management, heavy travel, BOM/pre-sales support, or schedule/budget ownership with limited software/product-building scope
     - hardware/product-engineer roles that are not web product engineering
     - remote roles that are United States-only, require US work authorization, or require US payroll unless the fit is exceptional
     - postings older than 3 days
     - CakeResume listings with no visible freshness signal when enough verified-fresh roles are available

5. Produce the output.
   - For a quick answer, list role targets with source, freshness window, direct job URL, fit, and action.
   - For a local sheet artifact, use the Spreadsheets skill to create an `.xlsx` with:
     - `Job Leads Summary`: company name, role title, role location, post date/age, ranking label, role family, fit notes, URL, status, next action
     - `Role Priorities`: rank, role target, interview probability, freshness rule, best queries, count, why it fits, action
     - one dated daily results tab per run, for example `2026-05-19 Results`
   - In the existing `2026 interview` Google Sheet, use Chrome to keep `Role Priorities` as an isolated reference tab and add a new dated search-result tab each day.
   - Before creating a dated tab, check whether `<YYYY-MM-DD> Results` already exists. Reuse and update it when present.
   - When updating the existing `2026 interview` Google Sheet, mirror the previous dated results tab's columns and formatting instead of imposing a new schema. The daily results tab should normally use:
     - `Search Date`
     - `Search Query`
     - `Freshness Filter`
     - `Result Count`
     - `Company Name`
     - `Role Title`
     - `Role Location`
     - `Post Date / Age`
     - `Ranking Label`
     - `Fit Notes`
     - `LinkedIn URL`
     - `Decision`
   - Keep daily-tab notes short and scannable. Put stable role-family context in `Role Priorities` or `Job Leads Summary`, not as an extra column in dated result tabs unless the sheet already has that column.
   - In screened job rows, paste the direct LinkedIn or CakeResume job-description URL, not the generic search-result URL. Search-result URLs are acceptable only for unscreened search-pool rows where no specific job has been selected yet.
   - Keep the existing `LinkedIn URL` column name for workbook compatibility even when a CakeResume URL is stored there. Prefix CakeResume search-query values with `CakeResume:` so the source remains unambiguous without changing the 12-column schema.
   - When using Chrome to update the sheet, claim an existing open tab titled `2026 interview` when available. Add or rename today's `<YYYY-MM-DD> Results` tab, and use the previous dated tab as the visual/template reference.
   - If Chrome paste shortcuts do not work in Google Sheets, use the Chrome-accessible sheet UI plus the system clipboard as needed, then verify visually that the data landed in the grid.

## Ranking Labels

- `Apply Today`: fresh, strong title/skill fit, plausible interview path.
- `Maybe`: fresh but noisy, partial fit, or broader role.
- `Skip`: older than 3 days, poor fit, wrong discipline, or high-friction with weak match.

## Completion Report

At the end of a run, report:

- run mode used
- sources searched
- queries run
- number of direct postings screened
- number of qualified roles saved
- whether CakeResume fallback was triggered and why
- top 3-5 application priorities

Read `references/linkedin-filters.md` when constructing LinkedIn search URLs or explaining freshness counts.
