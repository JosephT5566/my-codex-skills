# Supabase RLS Reasoning Drills

Use these drills to test authorization reasoning in Supabase/PostgreSQL systems. Prioritize trust boundaries, tenant isolation, old-row versus new-row state, and production-safe enforcement. Do not turn the session into a syntax quiz unless the user explicitly requests SQL-writing practice.

## Contents

- [Interviewer Guidance](#interviewer-guidance)
- [Shared Scenario](#shared-scenario)
- [Drill Progression](#drill-progression)
- [Evaluation Anchors](#evaluation-anchors)
- [Session-Summary Priorities](#session-summary-priorities)

## Interviewer Guidance

- Ask exactly one question at a time and adapt the next question to the answer.
- Let the candidate describe a policy conceptually before asking for exact SQL.
- Do not penalize failure to recall syntax when the authorization model is sound.
- Require the candidate to name the actor, action, tenant boundary, old-row condition, and new-row condition when relevant.
- Distinguish row authorization from column privileges, data constraints, request validation, and business logic.
- Ask for a concrete exploit outcome: data disclosure, modification of an existing foreign row, cross-tenant injection, ownership transfer, or privilege escalation.
- Treat `service_role`, security-definer functions, RPCs, and backend credentials as separate trust boundaries rather than assuming RLS protects every path.

## Shared Scenario

Use this schema when the user has no project-grounded schema:

```sql
organizations (
  id uuid primary key
);

organization_members (
  organization_id uuid,
  user_id uuid,
  role text,
  primary key (organization_id, user_id)
);

expenses (
  id uuid primary key,
  organization_id uuid,
  created_by uuid,
  amount numeric,
  title text
);
```

Assume `role` is organization-scoped and can be `member` or `admin`. Do not assume scale, traffic, or actual implementation details that the user has not provided.

## Drill Progression

### 1. Authorization Matrix

**Question**

Members may read every expense in their organization, edit only expenses they created, and never change `organization_id` or `created_by`. Organization admins may edit every expense in their organization. Describe the authorization rules for `SELECT`, `INSERT`, `UPDATE`, and `DELETE`.

**Listen for**

- Separate rules by action instead of relying on one broad `FOR ALL` policy.
- Check organization membership for tenant isolation.
- Scope admin status to the expense's organization.
- Separate ownership from membership.
- State an explicit product decision for delete permissions rather than inventing one silently.

**Useful follow-up**

Ask the candidate to identify which rules inspect existing rows and which inspect proposed new rows.

### 2. Old Row Versus New Row

**Question**

A member may update an expense when its current `organization_id` belongs to one of their organizations. What can go wrong if the database never validates the row produced by the update?

**Listen for**

- `USING` authorizes access to the old row.
- `WITH CHECK` validates the resulting row.
- The concrete exploit is moving or injecting an authorized row into another tenant, not automatically gaining access to an existing row in that tenant.
- The candidate considers both `organization_id` and `created_by` as authorization-sensitive fields.

**Useful follow-up**

Ask how the answer changes when the user is a member of both the source and destination organizations but cross-organization moves are forbidden.

### 3. Final-State Validation Versus Immutability

**Question**

A user belongs to organizations A and B. A `WITH CHECK` policy allows any resulting expense whose organization is one of the user's organizations. The product says an expense can never move between organizations. Is the policy sufficient?

**Listen for**

- Final-state authorization does not prove that a field remained unchanged.
- RLS policy expressions cannot directly compare `OLD` and `NEW`.
- Credible controls include column privileges, a narrow RPC or update allowlist, and a trigger using `IS DISTINCT FROM`.
- Defense in depth may use more than one control, but each control should have a clear responsibility.

**Useful follow-up**

Ask where the candidate would enforce immutability if admins are allowed to perform an explicit transfer workflow.

### 4. Tenant-Scoped Admin

**Question**

The same user is an admin in organization A and a regular member in organization B. How should an admin update rule avoid granting admin powers over B?

**Listen for**

- Join role membership to the row's `organization_id`; do not use a global `is_admin` boolean.
- Validate the target organization after an update as well as the source organization before it.
- Avoid trusting user-editable metadata for authoritative roles.
- Consider membership removal and stale JWT claims when authorization is derived from tokens.

**Useful follow-up**

Ask what should happen to in-flight requests or cached claims when an admin is demoted.

### 5. Ownership Is Not Tenant Isolation

**Question**

A policy checks only `created_by = auth.uid()`. Explain what this protects and what it does not protect in a multi-tenant expense system.

**Listen for**

- It provides an ownership condition but does not prove organization membership.
- A malicious or buggy write path could attach an owned row to an unauthorized organization unless tenant membership is also checked.
- Whether other organization members may read or edit the row is a separate product rule.
- Ownership, membership, and role are independent authorization dimensions.

### 6. Column-Reference Ambiguity

**Question**

Review this condition and explain whether it reliably ties the membership to the expense:

```sql
exists (
  select 1
  from organization_members m
  where m.organization_id = organization_id
    and m.user_id = auth.uid()
)
```

**Listen for**

- The unqualified `organization_id` can resolve to the inner relation and turn the comparison into a tautology.
- Fully qualify the outer column as `expenses.organization_id` or use an unambiguous table alias.
- A user with membership in any organization could otherwise satisfy the subquery for unrelated expenses.

Do not use this syntax-focused drill before the candidate has demonstrated the conceptual authorization model.

### 7. `USING` and Omitted `WITH CHECK`

**Question**

An `UPDATE` policy defines `USING (created_by = auth.uid())` and omits an explicit `WITH CHECK`. Can Alice necessarily change `created_by` to Bob? Explain how you would verify the actual behavior before calling it a vulnerability.

**Listen for**

- For PostgreSQL `UPDATE` and `ALL` policies that can have both expressions, an omitted `WITH CHECK` reuses the `USING` expression for new rows.
- Alice-to-Bob should therefore fail under that policy alone.
- The candidate checks command type and all applicable policies instead of reasoning from one fragment.
- Explicit `WITH CHECK` may still be preferable for clarity and when old/new rules differ.

### 8. Multiple Policies

**Question**

The owner policy looks correct in isolation, but another broad policy also applies to authenticated users. What must you inspect before concluding that access is denied?

**Listen for**

- Inspect every policy applicable to the command and database role.
- PostgreSQL policies are permissive by default and permissive policies can combine with `OR`; restrictive policies have different composition behavior.
- Broad `FOR ALL`, `USING (true)`, or incorrectly scoped admin policies may defeat a narrower policy.
- Include grants and roles in the review; RLS does not replace ordinary privileges.

### 9. API Mass Assignment

**Question**

An API calls `.update(request.body)` on `expenses`. RLS verifies that the resulting row remains within an organization the user can access. What risks remain?

**Listen for**

- Mass assignment may expose authorization-sensitive or server-managed columns.
- A final row may still satisfy RLS while violating immutability or business rules.
- Use request schemas and explicit allowlists; consider narrow RPCs or column privileges.
- Keep RLS as the final row-authorization boundary rather than treating API validation as a replacement.

### 10. Trigger Failure Semantics

**Question**

A `BEFORE UPDATE` trigger raises an exception when `organization_id` changes. Does the database update the row and then restore it?

**Listen for**

- The statement fails; the prohibited row change is not committed.
- In an explicit transaction, an uncaught error normally leaves the transaction failed until rollback.
- Avoid overclaiming when savepoints or caught PL/pgSQL exceptions change the rollback boundary.

### 11. Membership Lifecycle

**Question**

A user is removed from an organization while they still have an active session. What determines whether their next request can read expenses?

**Listen for**

- A policy querying the authoritative membership table observes removal differently from a policy relying on stale JWT claims.
- JWT refresh timing matters when membership or role is embedded in claims.
- The candidate considers transaction timing and revocation expectations without claiming impossible instant revocation guarantees.
- Audit logging and tests should cover removal and demotion.

### 12. Bypass and Trust Boundaries

**Question**

The frontend is protected by RLS, but a backend endpoint uses a Supabase service credential. What authorization responsibility moves to that endpoint?

**Listen for**

- Do not assume RLS protects a path that bypasses it.
- The backend must authenticate the caller and re-establish tenant, ownership, and role checks.
- Keep elevated credentials server-side and narrow the endpoint's inputs and effects.
- Prefer least-privilege paths rather than using elevated credentials by default.

### 13. Test Strategy

**Question**

How would you prove that the expense policies prevent cross-tenant access before deployment?

**Listen for**

- Build an actor-by-action test matrix across owner, same-tenant member, tenant admin, other-tenant user, anonymous user, and elevated backend paths.
- Test `SELECT`, `INSERT`, `UPDATE`, and `DELETE`, including attempts to mutate authorization-sensitive columns.
- Include users with multiple memberships and different roles across organizations.
- Test both allowed behavior and denial behavior, including empty-result versus error semantics.
- Run tests using the same database roles and claims as production clients.

### 14. Performance Without Weakening Authorization

**Question**

A membership subquery runs for every expense row and the query becomes slow. How would you improve it without weakening tenant isolation?

**Listen for**

- Index membership lookup keys such as `(user_id, organization_id)` or the access-pattern-appropriate order.
- Index row columns used by policies and application filters.
- Inspect the query plan and measure before redesigning authorization.
- Consider stable helper functions carefully, including security-definer ownership, schema exposure, and search path.
- Preserve the same authorization invariant while optimizing its implementation.

## Evaluation Anchors

Rate an answer **Strong** when it:

- States a clear authorization decision before discussing implementation.
- Separates actor, action, tenant membership, ownership, and role.
- Distinguishes old-row access from new-row validity for updates.
- Names the concrete failure mode and assigns each mitigation to the right layer.
- Covers relevant trust boundaries without adding unjustified complexity.

Rate it **Acceptable but incomplete** when the direction is safe but it misses one important dimension, such as tenant scoping, new-row validation, immutable columns, or the exact exploit outcome.

Rate it **Weak / risky** when it relies only on frontend checks, treats a global admin flag as tenant authorization, confuses ownership with membership, assumes RLS restricts update columns, or proposes a policy that enables cross-tenant access.

## Session-Summary Priorities

When this drill ends, summarize:

1. Whether the user can model authorization separately from syntax.
2. Whether the user consistently distinguishes old and new row state.
3. Whether the user scopes ownership and roles to the correct tenant.
4. Whether the user assigns row authorization, column restrictions, validation, and business logic to appropriate layers.
5. The next three practice priorities, without asking another question unless the user requests continued practice.
