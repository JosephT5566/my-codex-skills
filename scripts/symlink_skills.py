#!/usr/bin/env python3
"""Symlink skills from this repository into an agent skills directory."""

from __future__ import annotations

import argparse
import os
from datetime import datetime
from pathlib import Path


def repo_root() -> Path:
    return Path(__file__).resolve().parents[1]


def find_skills(root: Path) -> list[Path]:
    return sorted(
        path
        for path in root.iterdir()
        if path.is_dir() and (path / "SKILL.md").is_file()
    )


def backup_path(path: Path) -> Path:
    stamp = datetime.now().strftime("%Y%m%d-%H%M%S")
    return path.with_name(f"{path.name}.backup-{stamp}")


def link_skill(skill_dir: Path, target_dir: Path, *, dry_run: bool, backup_existing: bool) -> str:
    destination = target_dir / skill_dir.name
    source = skill_dir.resolve()

    if destination.is_symlink():
        current = destination.resolve()
        if current == source:
            return f"skip  {destination} already points to {source}"
        if dry_run:
            return f"link  {destination} -> {source} (replace symlink to {current})"
        destination.unlink()
        destination.symlink_to(source, target_is_directory=True)
        return f"link  {destination} -> {source} (replaced symlink to {current})"

    if destination.exists():
        if not backup_existing:
            return (
                f"skip  {destination} exists and is not a symlink "
                "(rerun with --backup-existing to move it aside)"
            )
        backup = backup_path(destination)
        if dry_run:
            return f"link  {destination} -> {source} (backup existing to {backup})"
        destination.rename(backup)
        destination.symlink_to(source, target_is_directory=True)
        return f"link  {destination} -> {source} (backed up existing to {backup})"

    if dry_run:
        return f"link  {destination} -> {source}"
    destination.symlink_to(source, target_is_directory=True)
    return f"link  {destination} -> {source}"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Symlink all top-level repo skills into ~/.codex/skills."
    )
    parser.add_argument(
        "--target",
        default="~/.codex/skills",
        help="Directory to receive skill symlinks. Default: ~/.codex/skills",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print actions without changing the filesystem.",
    )
    parser.add_argument(
        "--backup-existing",
        action="store_true",
        help="Move existing non-symlink paths aside before linking.",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    root = repo_root()
    target_dir = Path(os.path.expanduser(args.target)).resolve()
    skills = find_skills(root)

    if not skills:
        print(f"No skills found under {root}")
        return 1

    if not args.dry_run:
        target_dir.mkdir(parents=True, exist_ok=True)

    print(f"Repo:   {root}")
    print(f"Target: {target_dir}")

    for skill_dir in skills:
        print(link_skill(skill_dir, target_dir, dry_run=args.dry_run, backup_existing=args.backup_existing))

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
