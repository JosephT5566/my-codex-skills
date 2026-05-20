# Job Search Sources

## Canonical Tracking Sheet

Use this Google Sheet as the maintained table for role priorities, LinkedIn search queries, and application tracking. It is named `2026 interview` and usually lives in the Google Drive folder `Interview 2026`.

```text
https://docs.google.com/spreadsheets/d/18w0eNHKBtIf0DwmvO2h73SydQHQG7NXI6PBzTKWtInA/edit?gid=0#gid=0
```

Access note:

- Prefer Chrome for updating this tracker. The browser is usually logged into the account that owns `2026 interview`, while the Google Drive/Sheets connector account may differ.
- Use the Google Drive/Sheets connector only when the user explicitly asks for API-based edits, Chrome is unavailable, or the sheet is not accessible in Chrome.
- If the connector gets `403`, `404`, or cannot find the sheet by search, stop using the connector for that run and use Chrome to claim the open `2026 interview` tab when available.
- Do not create a replacement tracker unless the user explicitly approves it.

## Maintenance Notes

- Keep these tabs:
  - `Job Leads Summary`: manually curated lead tracker.
  - `Role Priorities`: stable reference table for target role families and search queries.
  - `<YYYY-MM-DD> Results`: one new search-result tab per search day.
- `Job Leads Summary` columns:
  - Company Name
  - Role Title
  - Role Location
  - Post Date / Age
  - Ranking Label
  - Role Family
  - Fit Notes
  - LinkedIn URL
  - Status
  - Next Action
- Daily result tabs should include search metadata and screened job leads:
  - Search Date
  - Search Query
  - Freshness Filter
  - Result Count
  - Company Name
  - Role Title
  - Role Location (on site, hybrid, remote)
  - Post Date / Age
  - Ranking Label
  - Fit Notes
  - LinkedIn URL
  - Decision
- Do not add `Role Family` to dated daily results tabs unless the existing workbook has that column. The current `2026 interview` daily-tab format mirrors `2026-05-19 Results` and uses the 12 columns above.
- When adding a new dated tab, inspect the previous dated results tab first and mirror its column order, width, concise notes style, and decisions such as `Search pool` / `Fallback pool`.
- Keep `Fit Notes` short enough to scan in-sheet. Long reasoning can go in chat or a separate summary, not in every row.
- Keep role-priority rows stable unless the user's positioning changes.
- Refresh LinkedIn search counts when running a new job-search session.
- Add individual job leads to the sheet only when they pass the freshness screen:
  - posted in the past 24 hours, or
  - posted in the past 3 days with strong fit.
- Ignore jobs older than 3 days by default.
