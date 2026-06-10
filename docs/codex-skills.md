# Codex Skills Registry

Use this page as a portable reference for installed skills and the prompt shape that tends to activate each one well.

## Installed Skills

| Skill | Best for | Suggested prompt |
|---|---|---|
| `to-prd` | Turning current context into a PRD and publishing it to the issue tracker | `Use the to-prd skill. Turn our current context into a PRD for this feature, using the repo glossary and existing ADRs. Do not interview me; synthesize from what you already know, then publish it to the project issue tracker with the ready-for-agent label.` |
| `frontend-design` | Designing distinctive UI with a deliberate visual identity | `Use the frontend-design skill. Design this UI with a strong point of view, not a generic template. Start by naming the subject, audience, and the page's single job, then propose a compact palette, type system, layout concept, and one signature visual element.` |
| `shadcn-ui` | Adding or refining accessible React UI with shadcn/ui, Tailwind, Radix, React Hook Form, and Zod | `Use the shadcn-ui skill. Implement this interface with shadcn/ui patterns, keeping accessibility, Tailwind theming, and form validation in mind. Prefer the repo's existing patterns and use the appropriate shadcn components for the job.` |

## Prompt Notes

- `to-prd` works best when the current conversation already contains the feature context. It should not be used as an interview prompt.
- `frontend-design` works best when you give it a real product subject, audience, and page goal.
- `shadcn-ui` works best when you specify the UI job clearly, such as a form, dialog, table, dashboard, or component refresh.

## Reuse Pattern

When switching devices, keep this repo cloned and start from this page. The installed skills themselves live in your Codex skill directories, but this registry preserves the prompt shape and usage notes in one place.
