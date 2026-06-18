# Chun Lin Tseng

josephtseng-tw.com | LinkedIn: linkedin.com/in/joseph-tseng-50ba36136 | GitHub: github.com/JosephT5566  
chunlinjoseph@gmail.com | 0928-746-335

## Summary

Software Engineer focused on frontend and full-stack product development, with experience building marketplace search, CMS-driven page platforms, experimentation workflows, real-time operational tools, and developer automation. Strong in TypeScript, React, Next.js, SvelteKit, GraphQL, Firebase, Supabase, and frontend architecture.

At Houzz, delivered search and browse improvements, Prismic-powered landing and event pages, GraphQL schema/resolver work, A/B-tested product changes, and frontend integrations across Marketplace, Lead Nurture, and 3D teams. Comfortable working through ambiguous product requirements with PM, design, backend, platform, personalization, and data stakeholders. Also experienced in large production codebases, tracing issues across frontend flows, API integrations, feature switches, logs, and analytics tools.

## Technical Skills

- **Languages:** TypeScript, JavaScript, HTML, CSS, SQL, C, C#
- **Frontend:** React, Next.js, SvelteKit, Tailwind CSS, responsive web development, PWA development, frontend state management, frontend architecture
- **Backend / Data:** GraphQL schema and resolvers, Firebase Authentication, Firestore, Supabase, PostgreSQL, API integration, row-level security, serverless function integration
- **Product / Platform:** Prismic CMS, Amplitude, Redash, Coralogix, Jira, feature switches, A/B testing, QA planning, bug bash coordination
- **Cloud / Tooling:** GitHub Actions, self-hosted runners, GitHub Pages, Firebase Hosting, GCP, Cloudflare Workers, CI/CD, Kubernetes collaboration, Codex CLI, AI API integration

## Professional Experience

### Software Engineer

**Houzz** | May 2022 - May 2026  
Teams: Marketplace, Lead Nurture, 3D

- Owned CMS-driven page platform work using Prismic, including content and data modeling, GraphQL schema and resolver implementation, and frontend rendering for reusable landing page and event page patterns.
- Delivered marketplace search and browse UX improvements across desktop and mobile web, including search dropdown recommendation pills, filter/navigation updates, and mobile search layout improvements; one experiment trended positive with +5.8% orders and +2.5% GMV. (We should not mention the detail value directly unless it's necessary)
- Implemented campaign and CMS-driven experiences, including an event/contest page that reached around 21,000 unique visitors and drove around 1,700 signed-in voting users. (We should not mention the detail value directly unless it's necessary)
- Planned frontend architecture for new product features by researching existing code paths, integrating with frontend stores, creating reusable methods, and reducing impact on legacy behavior.
- Investigated issues in a large production codebase by tracing frontend flows, API dependencies, feature switches, logs, and product metrics to identify root causes and ship safe fixes.
- Collaborated with PMs, designers, backend/platform engineers, personalization engineers, and data stakeholders to clarify requirements, write design docs, break work into Jira tickets, coordinate releases, and deliver projects on schedule.
- Supported 3D workflow feature development from the frontend side by integrating new feature behavior into the existing codebase, managing required frontend data flow, and coordinating with engineers responsible for Three.js rendering.
- Improved delivery quality through feature switches, QA guides, bug bash organization, code reviews, debugging, and release monitoring with tools such as Coralogix, Amplitude, and Redash.

### Frontend Engineer

**Chung Yung Consultant Company, Taipei** | Aug 2020 - May 2022

- Built responsive web applications using React, Next.js, TypeScript, HTML, and CSS, while also supporting UI design collaboration and backend/API integration.
- Implemented membership website features including login/logout flows, data fetching, form-driven interfaces, and responsive layouts.
- Used XState to structure authentication flow and frontend state transitions, improving maintainability for user-facing membership features.
- Supported backend maintenance and database changes, including API integration and PostgreSQL table updates.
- Launched CI/CD and GitOps-based deployment workflows using GitHub and cloud infrastructure.

### Additional Engineering Experience

**Firmware Engineer, Foxconn, Hsinchu** | Sep 2018 - Mar 2020  
**Application Engineer, Mega Design Tech / Memoright Tech, Hsinchu** | Oct 2016 - Sep 2018

- Developed and maintained embedded firmware, memory controller testing patterns, and production application tooling using C, C++, and C#.
- Established unit tests for driver development using Ceedling, improving test coverage and development reliability.

## Selected Projects

### Wedding Guest Seating and Check-In Service

**Tech:** Next.js, React, TypeScript, Firebase Authentication, Firestore, Tailwind CSS, Firebase Hosting

- Built a responsive, real-time wedding operations app for guest lookup, table visualization, check-in/check-out tracking, and guest-list updates across mobile and desktop.
- Implemented Google Sign-In plus email-allowlisted write access, backed by Firestore security rules that allow public seat lookup while restricting check-in and guest-management changes.
- Designed fuzzy guest search, transactional guest creation, capacity validation, and dry-run-first migration scripts to move existing Firestore records to a guest-keyed data model without losing check-in state.

### Codex Workflow Automation Runner

**Tech:** GitHub Actions, self-hosted runner, Codex CLI, Bash, Chrome integration, Google Drive

- Built four manually triggered or scheduled GitHub Actions workflows for repository tasks, weekday LinkedIn job searches, job-description fit scoring, and tailored resume generation.
- Automated a multi-step resume pipeline that validates job URLs, invokes reusable Codex skills, exports ATS-friendly Markdown to PDF, uploads verified output to dated Google Drive folders, and retains workflow artifacts for diagnosis.
- Added runner prerequisite checks, timeouts, concurrency controls, least-privilege repository permissions, prompt-boundary guidance for untrusted job pages, and patch/result artifacts without automatically pushing generated changes.

### Personal Expense Tracking PWA

**Tech:** SvelteKit, TypeScript, Supabase, Tailwind CSS, IndexedDB, GitHub Actions, GitHub Pages

- Built a mobile-first expense tracking PWA supporting personal expenses and household shared expenses.
- Designed a static-first architecture using SvelteKit and GitHub Pages, with Supabase as the backend service.
- Implemented Google OAuth authentication and row-level secured Supabase data access.
- Added IndexedDB-based monthly caching to reduce redundant API requests and improve navigation performance.
- Designed normalized expense-sharing data models and monthly balance aggregation flows.
- Built a CI/CD pipeline with GitHub Actions for automated deployment and preview validation.
- Integrated an AI-powered receipt parsing flow through serverless cloud function endpoints.

## Education

**National Chung Hsing University**  
Master, Electrical Engineering | 2014 - 2016

**National Chiayi University**  
Bachelor, Electrical Engineering | 2010 - 2014
