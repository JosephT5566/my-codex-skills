---
name: markdown-resume-exporter
description: Export Markdown resumes and resume-like documents to PDF, DOCX, HTML, or plain text using Pandoc and available local PDF engines, with fallback handling and output verification.
---

# Markdown Resume Exporter

Use this skill when the user wants to convert a Markdown resume, cover letter, or similar Markdown application document into PDF, DOCX, HTML, or plain text.

Keep this skill separate from resume-writing skills. This skill handles file export mechanics only; it should not rewrite resume content unless the user asks.

## Workflow

1. Identify the source Markdown file and desired output format.
2. Prefer the local helper script:

   ```bash
   python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py SOURCE.md --format pdf
   ```

3. If a workspace CSS file is available, especially `resume-pandoc.css`, pass it explicitly:

   ```bash
   python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py SOURCE.md --format pdf --css resume-pandoc.css
   ```

4. Verify that the output file exists and report the exact path.
5. If PDF export fails because no PDF engine is installed, generate HTML and/or DOCX as a fallback and explain which dependency is missing.
6. In sandboxed sessions, headless Chrome may need an escalated rerun because it launches a macOS app.

## Export Behavior

The helper script:

- Uses `pandoc` when available.
- For PDF, tries available engines in this order: `pdflatex`, `xelatex`, `lualatex`, `tectonic`.
- If no LaTeX-style engine is available, tries HTML-to-PDF paths with `weasyprint`, then headless Chrome.
- If PDF is unavailable, can still produce `html`, `docx`, or `txt` outputs through Pandoc.
- Uses `resume-pandoc.css` from the source file directory by default when present.

## Common Commands

Export PDF:

```bash
python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py resume.md --format pdf
```

Export DOCX:

```bash
python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py resume.md --format docx
```

Export HTML:

```bash
python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py resume.md --format html
```

Export plain text:

```bash
python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py resume.md --format txt
```

Choose an explicit output path:

```bash
python3 /Users/joseph/.agents/skills/markdown-resume-exporter/scripts/export_resume.py resume.md --format pdf --output resume-final.pdf
```

## Notes

- Do not recommend installing full MacTeX unless the user wants a complete LaTeX environment. For resume export only, lighter options such as BasicTeX, Tectonic, WeasyPrint, or headless Chrome export are usually enough.
- If the user asks whether exact PDF styling is important, prefer HTML/PDF export with CSS over LaTeX PDF export.
- Do not overwrite source Markdown content.
