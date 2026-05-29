#!/usr/bin/env python3
"""Export Markdown resumes using Pandoc with practical PDF fallbacks."""

from __future__ import annotations

import argparse
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path


PDF_ENGINES = ("pdflatex", "xelatex", "lualatex", "tectonic")
CHROME_PATHS = (
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Chromium.app/Contents/MacOS/Chromium",
)


def run(cmd: list[str]) -> subprocess.CompletedProcess[str]:
    return subprocess.run(cmd, text=True, capture_output=True, check=False)


def require_pandoc() -> str:
    pandoc = shutil.which("pandoc")
    if not pandoc:
        raise SystemExit("pandoc is not installed or not on PATH.")
    return pandoc


def default_css(source: Path) -> Path | None:
    candidate = source.parent / "resume-pandoc.css"
    return candidate if candidate.exists() else None


def output_path(source: Path, fmt: str, explicit: str | None) -> Path:
    if explicit:
        return Path(explicit).expanduser().resolve()
    suffix = ".txt" if fmt == "txt" else f".{fmt}"
    return source.with_suffix(suffix)


def pandoc_base(pandoc: str, source: Path, output: Path) -> list[str]:
    return [pandoc, str(source), "-o", str(output)]


def export_non_pdf(pandoc: str, source: Path, output: Path, fmt: str, css: Path | None) -> None:
    cmd = pandoc_base(pandoc, source, output)
    if fmt == "html":
        cmd.extend(["--standalone"])
        if css:
            cmd.extend(["--css", str(css)])
    elif fmt == "txt":
        cmd.extend(["-t", "plain"])

    result = run(cmd)
    if result.returncode != 0:
        raise SystemExit(result.stderr.strip() or f"pandoc failed exporting {fmt}.")


def export_pdf_with_latex(pandoc: str, source: Path, output: Path, engine: str) -> bool:
    result = run([pandoc, str(source), "-o", str(output), "--pdf-engine", engine])
    if result.returncode == 0:
        return True
    sys.stderr.write(f"{engine} failed:\n{result.stderr.strip()}\n")
    return False


def export_pdf_with_weasyprint(pandoc: str, source: Path, output: Path, css: Path | None) -> bool:
    weasyprint = shutil.which("weasyprint")
    if not weasyprint:
        return False

    with tempfile.TemporaryDirectory() as tmp:
        html = Path(tmp) / f"{source.stem}.html"
        cmd = [pandoc, str(source), "-o", str(html), "--standalone"]
        if css:
            cmd.extend(["--css", str(css)])
        html_result = run(cmd)
        if html_result.returncode != 0:
            sys.stderr.write(html_result.stderr.strip() + "\n")
            return False

        pdf_cmd = [weasyprint, str(html), str(output)]
        pdf_result = run(pdf_cmd)
        if pdf_result.returncode == 0:
            return True
        sys.stderr.write(pdf_result.stderr.strip() + "\n")
        return False


def find_chrome() -> str | None:
    for name in ("google-chrome", "chrome", "chromium"):
        path = shutil.which(name)
        if path:
            return path
    for path in CHROME_PATHS:
        if Path(path).exists():
            return path
    return None


def export_pdf_with_chrome(pandoc: str, source: Path, output: Path, css: Path | None) -> bool:
    chrome = find_chrome()
    if not chrome:
        return False

    html = output.with_suffix(".html")
    export_non_pdf(pandoc, source, html, "html", css)
    result = run(
        [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-pdf-header-footer",
            f"--print-to-pdf={output}",
            html.resolve().as_uri(),
        ]
    )
    if result.returncode == 0 and output.exists() and output.stat().st_size > 0:
        return True
    sys.stderr.write(result.stderr.strip() + "\n")
    return False


def export_pdf(pandoc: str, source: Path, output: Path, css: Path | None, engine: str) -> None:
    engines = PDF_ENGINES if engine == "auto" else (engine,)
    for candidate in engines:
        if candidate == "weasyprint":
            continue
        if shutil.which(candidate) and export_pdf_with_latex(pandoc, source, output, candidate):
            return

    if engine in ("auto", "weasyprint") and export_pdf_with_weasyprint(pandoc, source, output, css):
        return

    if engine in ("auto", "chrome") and export_pdf_with_chrome(pandoc, source, output, css):
        return

    html_fallback = output.with_suffix(".html")
    export_non_pdf(pandoc, source, html_fallback, "html", css)
    raise SystemExit(
        "PDF export failed because no working PDF engine was available. "
        f"Generated HTML fallback: {html_fallback}"
    )


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Export a Markdown resume.")
    parser.add_argument("source", help="Source Markdown file.")
    parser.add_argument(
        "--format",
        choices=("pdf", "docx", "html", "txt"),
        default="pdf",
        help="Output format. Default: pdf.",
    )
    parser.add_argument("--output", help="Output file path.")
    parser.add_argument("--css", help="CSS file for HTML or WeasyPrint PDF export.")
    parser.add_argument(
        "--engine",
        default="auto",
        choices=("auto", "pdflatex", "xelatex", "lualatex", "tectonic", "weasyprint", "chrome"),
        help="PDF engine. Default: auto.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    source = Path(args.source).expanduser().resolve()
    if not source.exists():
        raise SystemExit(f"Source file does not exist: {source}")
    if source.suffix.lower() not in {".md", ".markdown"}:
        raise SystemExit(f"Source must be Markdown: {source}")

    pandoc = require_pandoc()
    css = Path(args.css).expanduser().resolve() if args.css else default_css(source)
    output = output_path(source, args.format, args.output)

    if args.format == "pdf":
        export_pdf(pandoc, source, output, css, args.engine)
    else:
        export_non_pdf(pandoc, source, output, args.format, css)

    if not output.exists() or output.stat().st_size == 0:
        raise SystemExit(f"Export did not produce a valid file: {output}")

    print(output)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
