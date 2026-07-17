# PostgreSQL Schema Tradeoff Drills

Use these drills for backend-ownership interviews about PostgreSQL data modeling. Select one prompt at a time and adapt names or scale to the candidate's project. Do not reveal strong-answer signals or risky signals before the candidate answers.

## 1. Historical Category Names

**Prompt**

A shared-expense system links each expense to a category. Users may rename categories, but historical reports must show the category name as it was when the expense occurred. Design the PostgreSQL schema and defend the tradeoff between normalization, a snapshot column, and JSONB.

**Strong-answer signals**

- Keep `category_id` as a foreign key and store an explicit `category_name_snapshot` at the correct relationship level.
- Distinguish an expense's own name from the category-name snapshot.
- Explain that full normalization reflects the current category name, while a snapshot preserves historical meaning at the cost of duplication.
- Prefer typed columns for stable, queryable fields; justify JSONB only when the structure or access pattern warrants it.
- Write the expense and snapshot atomically, and state which value historical reports read.

**Risky signals**

- Claim that `expense_name` preserves a renamed category without storing the category name.
- Keep only `category_id` while promising immutable historical labels.
- Choose JSONB solely to avoid another table without discussing integrity or query costs.

**Possible follow-up**

If one expense can be allocated across several categories, where should the category snapshot live and why?

## 2. Relational Shares vs JSONB

**Prompt**

An expense can be split among several users, with an amount and payment status per participant. Compare an `expense_shares` table with an `expenses.expense_shares JSONB` column and choose one for the initial production design.

**Strong-answer signals**

- Base the choice on access patterns, integrity requirements, update granularity, concurrency, and expected schema evolution.
- Prefer a relational table when participants reference users or require individual queries and updates.
- Identify useful constraints such as foreign keys, typed amounts, `UNIQUE (expense_id, user_id)`, and allowed statuses.
- Recognize JSONB as reasonable for an early prototype or opaque, variable data read and written as a whole.
- Explain what database guarantees JSONB gives up and how any accepted risks are mitigated.

**Risky signals**

- Treat JSONB as equivalent to relational rows for foreign keys.
- Ignore cross-expense queries such as finding all unpaid shares for one user.
- Assume application validation alone protects every database write path.

**Possible follow-up**

Which concrete product requirement would make you migrate from JSONB to an `expense_shares` table?

## 3. Enforcing JSONB Invariants

**Prompt**

Assume the team keeps shares in JSONB. Every embedded `user_id` must identify a real user, every amount must be non-negative, no user may appear twice, and the share total must equal the expense amount. Decide which rules belong in middleware and which must be enforced by PostgreSQL.

**Strong-answer signals**

- Use middleware for request-shape validation and friendly errors, not as the only integrity boundary.
- Use PostgreSQL JSONB functions to expand and calculate array elements when database enforcement is required.
- State that ordinary foreign keys cannot target identifiers embedded inside a JSONB array.
- Consider a trigger or controlled database function for cross-element and cross-table checks, while acknowledging complexity, permissions, and performance.
- Prefer normalization if substantial trigger code is recreating relational constraints.

**Risky signals**

- Claim that PostgreSQL automatically validates JSONB member types or references.
- Put all checks in middleware without addressing SQL consoles, jobs, migrations, or other writers.
- Add a trigger without discussing failure behavior, transaction scope, or operational cost.

**Possible follow-up**

If middleware already verifies the share total, why might the database still reject an invalid total?

## 4. Concurrent JSONB Updates

**Prompt**

Two requests read the same expense and concurrently update different participants inside its shares JSONB array. Describe the failure mode and design a safe update strategy.

**Strong-answer signals**

- Identify read-modify-write and lost-update risk at the expense-row level.
- Propose a transaction with `SELECT ... FOR UPDATE`, optimistic version checking, or a single atomic SQL update with clear conflict behavior.
- Explain how the API reports or retries a conflict without silently overwriting data.
- Contrast row-level JSONB contention with independently updateable rows in a normalized table.
- Avoid automatic retries that can duplicate side effects or overwrite newer user intent.

**Risky signals**

- Assume updates to different JSON paths cannot conflict.
- Retry blindly without re-reading state or checking a version.
- Discuss locks without stating transaction boundaries.

**Possible follow-up**

How would your choice change if payment-status updates became frequent while expense metadata remained mostly static?

## 5. Migrating JSONB to Relational Rows

**Prompt**

The prototype stores shares in JSONB, but production now needs user-level queries, foreign keys, and frequent status updates. Plan a safe migration to an `expense_shares` table without stopping writes.

**Strong-answer signals**

- Add the relational table and constraints in a backward-compatible phase.
- Backfill in batches with validation, observability, and a resumable process.
- Use controlled dual writes or database-side synchronization temporarily, with an explicit source of truth.
- Compare old and new representations before switching reads.
- Plan rollout, rollback, cleanup, and handling of malformed legacy JSONB.

**Risky signals**

- Perform a single unbounded rewrite and immediate cutover.
- Dual-write indefinitely without reconciliation or ownership.
- Add strict constraints before inspecting or repairing legacy data.

**Possible follow-up**

During dual write, how would you detect and recover from the JSONB update succeeding while the relational insert fails?

## Evaluation Thread

Use the drills as a connected thread rather than asking all prompts as a checklist:

1. Start with historical category names to test requirement-to-schema mapping.
2. Move to relational shares versus JSONB only after the candidate defends the snapshot boundary.
3. Use invariant enforcement to test production ownership.
4. Introduce concurrency if the candidate keeps JSONB or claims updates are simple.
5. Use migration only when the candidate has articulated why requirements can outgrow the original model.

Reward an explicitly scoped prototype choice when it satisfies the stated workload. Increase pressure by changing access patterns, write concurrency, or integrity requirements rather than demanding fashionable architecture.
