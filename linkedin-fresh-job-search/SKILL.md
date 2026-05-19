---
name: linkedin-fresh-job-search
description: Fresh LinkedIn job-search workflow for finding newly posted roles, especially jobs posted in the past 24 hours or past 3 days. Use when the user asks to identify high-probability LinkedIn roles, filter out old postings, rank jobs by interview likelihood, create a job-search sheet, or run a daily fresh-job application workflow using LinkedIn/Chrome.
---

# LinkedIn Fresh Job Search

Use this skill to prioritize jobs where the user can apply before applicant volume builds up. Optimize for interview probability, not just raw job count.

## Core Policy

- Treat **Past 24 hours** as the first-pass search window.
- Use **Past 3 days** as the fallback expansion window.
- Ignore postings older than 3 days unless the user explicitly asks, the fit is exceptional, or there is a referral/recruiter path.
- Explain that LinkedIn result counts are noisy search-volume indicators, not counts of perfect-fit jobs.

## Workflow

1. Establish candidate profile signal.
   - Prefer the user's resume, LinkedIn profile, or stated background.
   - If available, read `references/candidate-profile.md` for a compact maintained profile snapshot.
   - If available, read `references/job-search-sources.md` for the canonical tracking sheet or source links.
   - If using LinkedIn, use the Chrome skill/plugin when logged-in context is needed.
   - Do not inspect cookies, local storage, passwords, or private session stores.

2. Build target role searches.
   - Start from role labels that match the user's strongest evidence.
   - Add broader aliases for volume and narrower aliases for precision.
   - For Joseph Tseng, default strong role families are:
     - Frontend Engineer / Frontend Developer
     - Software Engineer, Frontend / Web Engineer
     - Senior Frontend Engineer
     - React / TypeScript Engineer
     - Frontend-heavy Full Stack Engineer
     - Search / Marketplace Frontend Engineer
     - AI Product / AI-Native Web Engineer
     - CMS / Campaign Frontend Engineer

3. Search freshness windows.
   - First run LinkedIn searches with `f_TPR=r86400` for past 24 hours.
   - Then run `f_TPR=r259200` for past 3 days if the 24-hour pool is too small.
   - Keep location, remote, hybrid, and onsite preferences aligned with the user's profile or request.

4. Screen and rank.
   - Score fit over raw count. A smaller fresh search with high title/skill match can beat a larger noisy search.
   - Favor postings with:
     - exact or near-exact title match
     - React/TypeScript/frontend/product-web requirements
     - marketplace, e-commerce, search, CMS, experimentation, GraphQL, or AI-product overlap
     - posted within 24 hours
     - low applicant count
     - active recruiter, alumni, shared connections, or direct hiring-manager signal
   - Penalize:
     - pure ML/data/AI research roles when the user's proof is frontend/product
     - backend/platform/infra roles unless clearly frontend-heavy
     - hardware/product-engineer roles that are not web product engineering
     - postings older than 3 days

5. Produce the output.
   - For a quick answer, list role targets with freshness window, LinkedIn URL, fit, and action.
   - For a sheet, use the Spreadsheets skill to create an `.xlsx` with:
     - `Job Leads Summary`: company name, role title, role location, post date/age, ranking label, role family, fit notes, URL, status, next action
     - `Role Priorities`: rank, role target, interview probability, freshness rule, best queries, count, why it fits, action
     - one dated daily results tab per run, for example `2026-05-19 Results`
   - In Google Sheets, keep `Role Priorities` as an isolated reference tab and add a new dated search-result tab each day.

## Ranking Labels

- `Apply Today`: fresh, strong title/skill fit, plausible interview path.
- `Maybe`: fresh but noisy, partial fit, or broader role.
- `Skip`: older than 3 days, poor fit, wrong discipline, or high-friction with weak match.

Read `references/linkedin-filters.md` when constructing LinkedIn search URLs or explaining freshness counts.
