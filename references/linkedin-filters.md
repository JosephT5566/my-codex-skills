# LinkedIn Filters

Use these details when constructing LinkedIn search URLs or explaining freshness filters.

## Freshness

- Past 24 hours: `f_TPR=r86400`
- Past 3 days: `f_TPR=r259200`
- Use Past 24 hours first. Expand to Past 3 days only when the qualified pool is thin or the user explicitly asks for broader coverage.

LinkedIn result counts are noisy search-volume indicators. Do not treat them as exact counts of qualified jobs.

## Screening Notes

- Verify direct job pages before recommending a role.
- Deduplicate by normalized company name plus role title.
- Prefer direct job URLs over search-result URLs for selected leads.
- Reject US-only remote roles unless the posting is unusually strong and does not require US work authorization, US payroll, or strict US-only location.
