#!/usr/bin/env python3
"""List git-tracked files excluded from sync-public.toml."""

import argparse
import sys
from pathlib import Path

from _utils import get_tracked_files, load_manifest_sources


def list_excluded_files(
    manifest_sources: set[str],
    tracked_files: list[str],
    output_format: str,
) -> int:
    """Print a list of tracked files not present in the manifest."""
    excluded = sorted(set(tracked_files) - manifest_sources)

    if output_format == "lines":
        for path in excluded:
            print(path)
        return 0

    print(f"Tracked files: {len(tracked_files)}")
    print(f"Files in sync manifest: {len(manifest_sources)}")
    print(f"Excluded files: {len(excluded)}")

    if excluded:
        print("\nExcluded file list:")
        for path in excluded:
            print(f"- {path}")
    else:
        print("\nAll git-tracked files are included in sync manifest.")

    return 0


def main() -> int:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="List git-tracked files excluded from sync-public.toml."
    )
    parser.add_argument(
        "--manifest",
        type=Path,
        default=Path("sync-public.toml"),
        help="Path to sync-public.toml manifest file (default: sync-public.toml)",
    )
    parser.add_argument(
        "--repo-root",
        type=Path,
        default=Path("."),
        help="Root directory of the repository (default: current directory)",
    )
    parser.add_argument(
        "--format",
        choices=["summary", "lines"],
        default="summary",
        help="Output format (default: summary)",
    )

    args = parser.parse_args()
    repo_root = args.repo_root.resolve()

    manifest_sources = load_manifest_sources(args.manifest)
    if manifest_sources is None:
        return 1

    tracked_files = get_tracked_files(repo_root)
    if tracked_files is None:
        return 1

    return list_excluded_files(manifest_sources, tracked_files, args.format)


if __name__ == "__main__":
    sys.exit(main())
