#!/usr/bin/env python3
"""Check for navigation entries excluded from sync-public.toml."""

import argparse
import sys
from pathlib import Path

# tomllib is standard library in Python 3.11+, fall back to tomli for older versions
try:
    import tomllib
except ImportError:
    import tomli as tomllib

from _utils import get_excluded_files, to_repo_relative


def iter_nav_entries(value):
    """Yield nav entries that are file paths."""
    if isinstance(value, str):
        yield value
    elif isinstance(value, list):
        for item in value:
            yield from iter_nav_entries(item)
    elif isinstance(value, dict):
        for item in value.values():
            yield from iter_nav_entries(item)


def normalize_nav_path(path: str, docs_dir: str) -> str | None:
    """Normalize nav paths to repository-relative paths."""
    if "://" in path or path.startswith("mailto:"):
        print(f"WARNING: Skipping non-file nav entry: {path}", file=sys.stderr)
        return None

    clean = path.lstrip("/")
    if clean.startswith("./"):
        clean = clean[2:]

    if clean.startswith(f"{docs_dir}/") or clean == docs_dir:
        return clean

    return Path(docs_dir, clean).as_posix()


def load_nav_files(config_path: Path) -> tuple[set[str], str] | None:
    """Load file paths from the zensical navigation config."""
    if not config_path.exists():
        print(f"ERROR: Config file not found: {config_path}", file=sys.stderr)
        return None

    try:
        with open(config_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as exc:
        print(f"ERROR: Error reading config file: {exc}", file=sys.stderr)
        return None

    project_config = config.get("project", {})
    nav = config.get("nav") or project_config.get("nav")
    if nav is None:
        print(
            "WARNING: No nav section found in zensical.toml (expected nav or project.nav)",
            file=sys.stderr,
        )
        return set(), "doc"

    docs_dir = project_config.get("docs_dir", "doc")
    nav_files: set[str] = set()
    for entry in iter_nav_entries(nav):
        normalized = normalize_nav_path(entry, docs_dir)
        if normalized:
            nav_files.add(normalized)

    return nav_files, docs_dir


def nav_path_value(nav_path: str, docs_dir: str) -> str:
    """Return the nav entry value as written in zensical.toml."""
    if nav_path.startswith(f"{docs_dir}/"):
        return nav_path[len(docs_dir) + 1 :]
    return nav_path


def find_nav_line_numbers(
    config_path: Path,
    nav_paths: list[str],
    docs_dir: str,
) -> dict[str, int]:
    """Find line numbers for nav entries in zensical.toml."""
    line_map: dict[str, int] = {}
    try:
        lines = config_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return line_map

    nav_values = {path: nav_path_value(path, docs_dir) for path in nav_paths}

    for line_no, line in enumerate(lines, start=1):
        for nav_path, nav_value in nav_values.items():
            if nav_path in line_map:
                continue
            if f'"{nav_value}"' in line or f"'{nav_value}'" in line:
                line_map[nav_path] = line_no

    return line_map


def report_mismatches(
    nav_files: set[str],
    excluded_files: set[str],
    config_path: Path,
    repo_root: Path,
    docs_dir: str,
    output_format: str,
) -> int:
    """Report navigation entries excluded from sync-public.toml."""
    mismatches = sorted(nav_files & excluded_files)

    print(f"Navigation files: {len(nav_files)}")
    print(f"Excluded files: {len(excluded_files)}")
    print(f"Excluded navigation files: {len(mismatches)}")

    if mismatches:
        if output_format == "github":
            line_map = find_nav_line_numbers(config_path, mismatches, docs_dir)
            config_file = to_repo_relative(config_path, repo_root)
            for path in mismatches:
                line_no = line_map.get(path)
                if line_no:
                    print(
                        f"::error file={config_file},line={line_no}::"
                        f"Navigation entry excluded from sync-public.toml: {path}"
                    )
                else:
                    print(
                        f"::error file={config_file}::"
                        f"Navigation entry excluded from sync-public.toml: {path}"
                    )

        print("\nNavigation entries excluded from sync-public.toml:")
        for path in mismatches:
            print(f"- {path}")
        return 1
    else:
        print("\nNo navigation entries are excluded from sync-public.toml.")

    return 0


def main() -> int:
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Check for navigation entries excluded from sync-public.toml."
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
        "--config",
        type=Path,
        default=Path("zensical.toml"),
        help="Path to zensical.toml config file (default: zensical.toml)",
    )
    parser.add_argument(
        "--format",
        choices=["summary", "github"],
        default="summary",
        help="Output format (default: summary)",
    )

    args = parser.parse_args()

    nav_result = load_nav_files(args.config)
    if nav_result is None:
        return 1
    nav_files, docs_dir = nav_result

    repo_root = args.repo_root.resolve()
    excluded_files = get_excluded_files(args.manifest, repo_root)
    if excluded_files is None:
        return 1

    return report_mismatches(
        nav_files,
        excluded_files,
        args.config,
        repo_root,
        docs_dir,
        args.format,
    )


if __name__ == "__main__":
    sys.exit(main())
