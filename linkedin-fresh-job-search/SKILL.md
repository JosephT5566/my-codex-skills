---
name: linkedin-fresh-job-search
description: LinkedIn-first fresh job-search and application-prioritization workflow with optional CakeResume coverage for Taiwan roles. Use when the user asks to identify newly posted high-probability roles, decide which jobs deserve limited application time, rank jobs by interview likelihood and career upside, identify market skill signals, create a job-search sheet, or run a daily job-search workflow using LinkedIn, CakeResume, and Chrome.
---

# LinkedIn Fresh Job Search

Use this skill as a lightweight personal recruiter and career coach. Prioritize jobs where the user can apply before applicant volume builds up, then identify the five roles most deserving of limited application time. Optimize for interview probability, career growth, and market awareness, not raw job count. LinkedIn is the primary source; CakeResume is a supplemental Taiwan-focused source.

Do not add searches, open extra job pages, browse company websites, or introduce research steps for scoring or coaching. Derive all recommendations from information already collected during the normal search workflow and, when available, existing historical tracker outputs.

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
   - If available, read `references/career-targeting.md` for maintained role-family priorities, backend-depth expectations, and mixed-role screening rules.
   - If available, read `references/job-search-sources.md` for the canonical tracking sheet or source links.
   - If available, read `references/github-project-signals.md` for side-project evidence that can strengthen fit notes and resume targeting.
   - Use the Chrome skill/plugin for live LinkedIn and CakeResume searching and for updates to the existing `2026 interview` Google Sheet because these workflows may depend on the user's logged-in browser account.
   - Keep this workflow browser-only. If Chrome cannot access the tracker, stop and report the Chrome blocker instead of creating or updating a replacement through another account.
   - Do not inspect cookies, local storage, passwords, or private session stores.
   - Unless the user's current materials indicate otherwise, evaluate Joseph Tseng as a product-minded frontend-heavy software engineer extending toward Product Engineer, Full-stack Product Engineer, and AI Product Engineer roles. Treat React/TypeScript/frontend architecture as the foundation, and product ownership, backend/data integration, AI workflow integration, production debugging, experimentation, and release quality as the differentiators.
   - Treat international companies, Europe opportunities, remote-first culture, product-focused organizations, and an L4/L5 growth trajectory as career-upside signals.
   - Do not infer fit from title alone. Map the actual work to transferable skills: product ownership, system integration, backend boundary design, authorization/data access, observability, evaluation, AI tool safety, and cross-functional delivery.

2. Build target role searches.
   - Start from role labels that match the user's strongest evidence.
   - Add broader aliases for volume and narrower aliases for precision.
   - For a Daily Light Run, start with these four core LinkedIn queries:
     - `Product Engineer React TypeScript`
     - `Full Stack Product Engineer React`
     - `AI Product Engineer TypeScript`
     - `Frontend Engineer React TypeScript`
   - Add one rotating adjacent query only when useful:
     - QA/quality day: `QA Automation Engineer SQL`
     - ATE/test day: `ATE Software Engineer C++ C#`
     - AI application day: `AI Product Engineer TypeScript` or `Applied AI Engineer Product`
     - Agent/workflow day: `AI Agent Engineer Tool Calling` or `LLM Application Engineer`
     - Tools/integration day: `Developer Tools Engineer TypeScript`, `Developer Productivity Engineer`, or `Solutions Engineer JavaScript`
   - Check the most recent dated tracker tab before choosing the rotating query. Prefer a family that was not searched in the previous run.
   - For Joseph Tseng, default strong role families are:
     - Product Engineer with React/TypeScript product-web scope
     - Full-stack Product Engineer / Frontend-heavy Full Stack Engineer
     - AI Product Engineer / AI-Native Web Engineer / LLM Application Engineer
     - Senior Frontend Engineer when the role involves complex product frontend, architecture, experimentation, performance, accessibility, design systems, realtime workflows, data visualization, or AI interfaces
     - Frontend Platform Engineer / Web Platform UI Engineer
     - Search / Marketplace Frontend Engineer
     - CMS / Campaign Frontend Engineer
     - Developer Experience / Developer Productivity / Internal Tools Engineer with frontend tooling, workflow automation, or coding-agent scope
     - Solutions Engineer / Implementation Engineer / Forward Deployed Engineer for web, SaaS, CMS, e-commerce, AI workflow, or developer-tool products
   - For Joseph Tseng, default adjacent role families are:
     - Applied AI Engineer when product-facing and focused on LLM application integration rather than ML research
     - AI Agent Engineer / Agent Infrastructure Engineer when tool calling, human approval, evaluation, tracing, permissions, or developer workflows are central
     - Developer Productivity Engineer / AI Workflow Engineer / Coding Agent Workflow Engineer
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
     - `Product Engineer React TypeScript`
     - `Full Stack Product Engineer React`
     - `AI Product Engineer TypeScript`
     - `Applied AI Engineer Product`
     - `LLM Application Engineer`
     - `AI Agent Engineer Tool Calling`
     - `Software Engineer Agent Infrastructure`
     - `Developer Productivity Engineer`
     - `Developer Experience Engineer Frontend`
     - `Developer Tools Engineer TypeScript`
     - `Frontend Platform Engineer`
     - `Frontend Engineer React TypeScript`
     - `Frontend Developer React TypeScript`
     - `Software Engineer Frontend React`
     - `Web Engineer TypeScript`
     - `Frontend-heavy Full Stack Engineer`
     - `React TypeScript Engineer`
     - `Marketplace Frontend Engineer`
     - `Search Frontend Engineer`
     - `E-commerce Frontend Engineer`
     - `CMS Frontend Engineer`
     - `Campaign Frontend Engineer`
     - `AI Product Engineer React`
     - `AI Native Web Engineer`
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
     - `AI Product Engineer TypeScript`
     - `Applied AI Engineer Product`
     - `LLM Application Engineer`
     - `AI Agent Engineer Tool Calling`
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
     - product engineering, full-stack product ownership, AI-product, LLM application, agent workflow, or developer-productivity scope
     - marketplace, e-commerce, search, CMS, experimentation, GraphQL, PostgreSQL/data modeling, authorization/RLS, observability, or AI-product overlap
     - product engineering, developer tooling, internal tooling, implementation, or solutions-engineering roles where React/TypeScript/web integration remains central
     - backend basics as role-appropriate evidence: API design, PostgreSQL/schema tradeoffs, authz/RLS, idempotency, async workflow, observability, security boundary, or production debugging
     - AI workflow evidence: structured output, tool calling, RAG, human-in-the-loop approval, evaluation datasets, tracing, retry/fallback, token/latency/cost control, or permission-aware data access
     - QA, validation, application engineering, field application, customer quality, or technical project roles where test planning, root-cause debugging, release quality, production issue investigation, external/customer communication, or cross-functional engineering coordination are central
     - ATE/software-test roles using C/C++/C#, .NET, REST/WebSockets, data acquisition, device communication, debugging, documentation, and cross-functional hardware/test/system collaboration
     - AI application or digital transformation roles focused on workflow design, AI use-case definition, enterprise application patterns, stakeholder communication, delivery quality, and practical product outcomes
     - mixed frontend/backend/AI roles where the backend depth is feature-level rather than deep platform ownership, especially when the work involves data access, auth boundaries, API contracts, evaluations, and user-facing AI workflows
     - posted within 24 hours
     - low applicant count
     - explicit recent posted or updated time on CakeResume
     - remote eligibility for Taiwan/APAC/global candidates when outside Taiwan
     - active recruiter, alumni, shared connections, or direct hiring-manager signal
   - Penalize:
     - pure ML/data/AI research roles when the user's proof is frontend/product
     - backend/platform/infra roles unless clearly product-facing, frontend-heavy, developer-tooling-oriented, or realistic for backend feature ownership rather than service/platform ownership
     - AI Agent Engineer postings that are actually ML research, model training, GPU/model-serving infrastructure, or deep distributed systems roles rather than product-agent, tool-calling, evaluation, or workflow roles
     - generic `Harness Engineer` or `Loop Engineer` matches unless the posting clearly means AI agent harnesses, evaluation loops, coding-agent workflows, or developer tools. Reject wire harness, hardware-in-the-loop, and software-in-the-loop noise by default.
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
   - After screening, rank every reviewed role using only captured evidence across four dimensions:
     - `Skill Match`: React, TypeScript, GraphQL, frontend architecture, product engineering, web platform development, marketplaces, experimentation, production-scale systems, backend feature ownership, and applied AI workflow integration.
     - `Career Growth Match`: ownership, leadership, technical scope, seniority trajectory, product influence, backend/data judgment, AI-product capability, and cross-functional collaboration.
     - `Location Match`: Europe eligibility, international hiring, remote-first or remote-friendly culture, and plausible Taiwan/APAC eligibility.
     - `Company Quality Signals`: visible evidence in the posting or search results that the employer is product-led, SaaS-oriented, engineering-driven, or operating at meaningful scale. Do not research the company separately.
   - Use qualitative evidence rather than fabricated precision. Do not show a numeric score unless the user explicitly requests one.
   - Assign one opportunity tier:
     - `Target`: high career upside with strong engineering/product signals plus international, Europe-friendly, or remote-friendly exposure. Action: apply immediately, customize the resume, and seek a referral when a visible path exists.
     - `Strong Fit`: strong skill alignment, credible interview probability, good compensation potential, or relevant technical scope. Action: apply normally.
     - `Practice`: moderate alignment that is useful for interview practice or market calibration. Action: apply only if bandwidth allows.
     - `Skip`: weak fit, limited growth, location friction, or low interview probability. Action: do not apply.
   - Keep freshness labels separate from opportunity tiers:
     - `Apply Today`, `Maybe`, and `Skip` describe urgency and plausibility.
     - `Target`, `Strong Fit`, `Practice`, and `Skip` describe career priority.
   - Select a maximum of five daily application priorities from `Target` and `Strong Fit` roles. Rank them by:
     1. plausible interview probability
     2. career upside
     3. freshness and applicant timing
     4. application effort required
   - Prefer five strong choices over filling the quota. If fewer than five roles deserve an application, say so explicitly.

5. Produce the output.
   - Lead with `Today's Application Shortlist`, containing at most five roles in priority order.
   - For each recommended role, report:
     - `Company`
     - `Role`
     - `Tier`: `Target`, `Strong Fit`, or `Practice`
     - `Why It Matches`: 2-4 concise evidence bullets
     - `Suggested Action`: one or more of `Apply today`, `Customize resume first`, `Find referral`, or `Practice interview opportunity`
     - source, freshness, location, and direct job URL
   - State which shortlisted roles deserve resume customization. Reserve customization for `Target` roles or roles where a specific JD requirement can be addressed with existing candidate evidence.
   - List remaining reviewed roles compactly by tier so the user can see what was deprioritized without receiving another long job list.
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
   - Preserve an existing daily-tab schema instead of adding columns solely for the new analysis. Put the top-five shortlist and coaching analysis in the written completion report or an existing summary area when one is available.
   - Keep daily-tab notes short and scannable. Put stable role-family context in `Role Priorities` or `Job Leads Summary`, not as an extra column in dated result tabs unless the sheet already has that column.
   - In screened job rows, paste the direct LinkedIn or CakeResume job-description URL, not the generic search-result URL. Search-result URLs are acceptable only for unscreened search-pool rows where no specific job has been selected yet.
   - Keep the existing `LinkedIn URL` column name for workbook compatibility even when a CakeResume URL is stored there. Prefix CakeResume search-query values with `CakeResume:` so the source remains unambiguous without changing the 12-column schema.
   - When using Chrome to update the sheet, claim an existing open tab titled `2026 interview` when available. Add or rename today's `<YYYY-MM-DD> Results` tab, and use the previous dated tab as the visual/template reference.
   - If Chrome paste shortcuts do not work in Google Sheets, use the Chrome-accessible sheet UI plus the system clipboard as needed, then verify visually that the data landed in the grid.

6. Produce career coaching from reviewed evidence.
   - Perform this analysis after all jobs in the existing run are reviewed. Do not collect additional jobs or open additional pages.
   - `Market Gap Analysis`:
     - Identify only recurring requirements relevant to the candidate's target frontend/product career path that are less represented in the candidate profile.
     - Show at most three gaps.
     - For each gap report `Gap`, `Why it matters`, `Observed frequency`, and `Potential interview impact`.
     - Calculate observed frequency from the reviewed-job set when the evidence is countable, for example `4 of 10 reviewed jobs (40%)`. Otherwise use a bounded qualitative description such as `Repeated across several reviewed roles`; do not invent percentages.
     - Do not frame gaps as personal weaknesses.
   - `Homework Recommendations`:
     - Provide one practical recommendation per reported gap.
     - Report `Priority` (`High`, `Medium`, or `Low`), `Suggested learning topics`, `Suggested project or exercise`, `Estimated effort`, and `Interview relevance` (`High`, `Medium`, or `Low`).
     - Make exercises interview-oriented and reusable, such as a focused system-design walkthrough, architecture extension to an existing project, or concise implementation exercise. Avoid generic course lists.
   - `Interview Readiness`:
     - Assess `Frontend Engineering`, `Product Engineering`, `Backend Ownership`, `System Design`, `Cloud Infrastructure`, `AI / LLM Knowledge`, and `Leadership & Collaboration`.
     - For `Backend Ownership`, distinguish API consumer, API integrator, API designer, backend feature owner, service/system owner, and platform/infrastructure owner. Treat Joseph's current default as API integrator moving toward API designer/backend feature owner unless newer project evidence proves more.
     - For each category report `Current Assessment` (`Strong`, `Good`, or `Needs Improvement`), `Reasoning`, and `Suggested Next Step`.
     - Base reasoning on the candidate profile plus requirements observed in this run. Use `Good` rather than overclaiming when evidence is incomplete.
   - `Career Signal Watch`:
     - Use only historical outputs already available in the tracker or supplied by the user.
     - Report a trend only when the same directional signal appears across at least three distinct runs. Examples include increasing AI requirements, Python frequency, system-design expectations, Europe opportunities, or decreasing remote availability.
     - State the runs or dates supporting each trend when available.
     - If fewer than three comparable runs exist or no trend is consistent, say `Insufficient history for a reliable trend` and omit speculation.

## Ranking Labels

- `Apply Today`: fresh, strong title/skill fit, plausible interview path.
- `Maybe`: fresh but noisy, partial fit, or broader role.
- `Skip`: older than 3 days, poor fit, wrong discipline, or high-friction with weak match.

## Opportunity Tiers

- `Target`: highest priority for career upside and fit; customize the resume and pursue a referral when practical.
- `Strong Fit`: credible interview opportunity with strong alignment; apply normally.
- `Practice`: useful for interview practice or market calibration; apply only with spare bandwidth.
- `Skip`: do not invest application time.

## Completion Report

At the end of a run, report:

- run mode used
- sources searched
- queries run
- number of direct postings screened
- number of qualified roles saved
- whether CakeResume fallback was triggered and why
- ranked application shortlist of up to five roles
- roles requiring resume customization
- top three market gaps and practical homework
- backend-depth fit note for shortlisted mixed roles when backend ownership expectations are visible
- interview-readiness assessment
- career signal watch, or an explicit insufficient-history note

Read `references/linkedin-filters.md` when constructing LinkedIn search URLs or explaining freshness counts.
