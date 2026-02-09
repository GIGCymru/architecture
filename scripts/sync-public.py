#!/usr/bin/env python3
"""Synchronize selected files to the public architecture repository."""

from __future__ import annotations

import argparse
import shutil
import sys
from dataclasses import dataclass
from pathlib import Path

try:
    import tomllib  # Python 3.11+
except ModuleNotFoundError:  # pragma: no cover
    import tomli as tomllib  # type: ignore[import-not-found]


@dataclass(frozen=True)
class PublishEntry:
    source: Path
    destination: Path


def parse_manifest(manifest_path: Path) -> list[PublishEntry]:
    """Parse the TOML manifest file."""
    data = tomllib.loads(manifest_path.read_text(encoding="utf-8"))
    entries = data.get("files")
    if not isinstance(entries, list):
        raise ValueError(f"{manifest_path} must define a 'files' list")

    parsed: list[PublishEntry] = []
    for item in entries:
        source_str: str
        dest_str: str

        if isinstance(item, str):
            source_str = item
            dest_str = item
        elif isinstance(item, dict):
            source_val = item.get("source")
            if not isinstance(source_val, str):
                raise ValueError("Each file entry must include a string 'source'")
            source_str = source_val
            dest_str = item.get("dest", source_str)
            if not isinstance(dest_str, str):
                raise ValueError("'dest' must be a string when provided")
        else:
            raise ValueError("Each entry in 'files' must be a string or table")

        source = Path(source_str)
        destination = Path(dest_str)

        if source.is_absolute() or destination.is_absolute():
            raise ValueError(f"Entries must use relative paths: {source_str} -> {dest_str}")

        parsed.append(PublishEntry(source=source, destination=destination))

    return parsed


def ensure_inside_repo(repo_root: Path, target: Path) -> None:
    """Ensure that the target path is within the repository root."""
    resolved_root = repo_root.resolve()
    resolved_target = target.resolve(strict=False)
    if resolved_root not in resolved_target.parents and resolved_root != resolved_target:
        raise ValueError(f"Path {target} is outside repository root {repo_root}")


def normalize_destination(target_root: Path, destination: Path) -> Path:
    """Normalize the destination path relative to the target root."""
    resolved_root = target_root.resolve()
    resolved_destination = (target_root / destination).resolve(strict=False)
    try:
        return resolved_destination.relative_to(resolved_root)
    except ValueError as exc:  # pragma: no cover - defensive
        raise ValueError(
            f"Destination {destination} is outside target root {target_root}"
        ) from exc


def load_entries(repo_root: Path, manifest_path: Path) -> list[PublishEntry]:
    """Load and validate manifest entries."""
    entries = parse_manifest(manifest_path)
    for entry in entries:
        ensure_inside_repo(repo_root, repo_root / entry.source)
    return entries


def copy_entry(repo_root: Path, target_root: Path, entry: PublishEntry, dry_run: bool) -> Path:
    """Copy a single entry from source to destination."""
    source_path = (repo_root / entry.source).resolve()
    
    if not source_path.exists():
        raise FileNotFoundError(f"Source not found: {entry.source}")

    if source_path.is_dir():
        raise ValueError(
            f"Directory copying is prohibited: {entry.source}. "
            "List every file explicitly in the manifest."
        )

    dest_relative = normalize_destination(target_root, entry.destination)
    target_path = target_root / dest_relative
    
    print(f"Copying {entry.source} -> {dest_relative}")
    if not dry_run:
        target_path.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(source_path, target_path)

    return dest_relative


def delete_unlisted(target_root: Path, keep_paths: set[Path], dry_run: bool) -> list[Path]:
    """Delete files in target that are not in the keep list."""
    removed: list[Path] = []
    
    # First pass: delete files
    for path in sorted(target_root.rglob("*")):
        if ".git" in path.parts or path.is_dir():
            continue
            
        relative = path.relative_to(target_root)
        if relative not in keep_paths:
            removed.append(relative)
            print(f"Deleting {relative}")
            if not dry_run:
                path.unlink()

    # Second pass: remove empty directories (bottom-up)
    if not dry_run:
        for path in sorted(target_root.rglob("*"), reverse=True):
            if ".git" in path.parts or not path.is_dir():
                continue
                
            if not any(path.iterdir()):
                path.rmdir()

    return removed


def sync_files(repo_root: Path, target_root: Path, manifest_path: Path, dry_run: bool) -> None:
    """Load manifest and synchronize files."""
    entries = load_entries(repo_root, manifest_path)
    print(f"Loaded {len(entries)} entries from manifest.")
    keep_paths: set[Path] = set()

    for entry in entries:
        dest_path = copy_entry(repo_root, target_root, entry, dry_run)
        keep_paths.add(dest_path)

    removed = delete_unlisted(target_root, keep_paths, dry_run)

    if removed:
        print("Removed unlisted files:")
        for path in sorted(removed):
            print(f"  - {path}")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Synchronize files to the public architecture repo")
    parser.add_argument(
        "target",
        type=Path,
        help="Path to local clone of https://github.com/GIGCymru/architecture.git",
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("sync-public.toml"),
        help="Path to the .toml manifest file (default: sync-public.toml)",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path.cwd(),
        help="Path to this repository (default: current working directory)",
    )
    parser.add_argument(
        "--apply",
        action="store_true",
        help="Apply changes to the target repository (default: dry run)",
    )
    return parser.parse_args()


def main() -> int:
    """Main execution function."""
    args = parse_args()
    repo_root = args.repo_root.resolve()
    
    # Resolve manifest path relative to repo_root if it's not absolute
    manifest_path = args.manifest
    if not manifest_path.is_absolute():
        manifest_path = (repo_root / manifest_path).resolve()
    else:
        manifest_path = manifest_path.resolve()

    target_root = args.target.resolve()

    if not manifest_path.exists():
        print(f"Manifest not found: {manifest_path}", file=sys.stderr)
        return 1
    if not repo_root.exists():
        print(f"Repository root not found: {repo_root}", file=sys.stderr)
        return 1
    if not target_root.exists():
        print(f"Target repo not found: {target_root}", file=sys.stderr)
        return 1

    dry_run = not args.apply
    sync_files(repo_root, target_root, manifest_path, dry_run)

    if dry_run:
        print("Dry run complete: no files were changed.")
    else:
        print("Sync complete: files were updated.")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
