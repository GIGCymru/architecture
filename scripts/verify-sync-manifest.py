#!/usr/bin/env python3
"""Verify that all files listed in sync-public.toml exist in the repository."""

import argparse
import re
import sys
from pathlib import Path

# tomllib is standard library in Python 3.11+, fall back to tomli for older versions
try:
    import tomllib
except ImportError:
    import tomli as tomllib

from _utils import emit_github_error, to_repo_relative


def load_manifest_line_map(manifest_path: Path) -> dict[str, int]:
    """Map manifest entries to line numbers for annotations."""
    line_map: dict[str, int] = {}
    try:
        lines = manifest_path.read_text(encoding="utf-8").splitlines()
    except Exception:
        return line_map

    for line_no, line in enumerate(lines, start=1):
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue

        # Match TOML dict entries with source field:
        #   { source = "path", ... } or { source = 'path', ... }
        # Uses named group 'source_double' for double-quoted and 'source_single' for single-quoted values.
        source_match = re.search(
            r'source\s*=\s*'           # Match 'source =' with optional whitespace
            r'(?:'                      # Non-capturing group for alternatives
            r'"(?P<source_double>[^"]+)"'  # Double-quoted string in named group
            r"|"                        # OR
            r"'(?P<source_single>[^']+)'"  # Single-quoted string in named group
            r')',
            stripped,
        )
        if source_match:
            value = source_match.group('source_double') or source_match.group('source_single')
            line_map.setdefault(value, line_no)
            continue

        # Match bare string entries in TOML array:
        #   "path", or 'path',  # with optional trailing comma and comment
        # Uses named group 'bare_double' for double-quoted and 'bare_single' for single-quoted values.
        string_match = re.match(
            r'(?:'                      # Non-capturing group for alternatives
            r'"(?P<bare_double>[^"]+)"'    # Double-quoted string in named group
            r"|"                        # OR
            r"'(?P<bare_single>[^']+)'"    # Single-quoted string in named group
            r')'
            r'\s*,?\s*'                 # Optional whitespace, comma, and whitespace
            r'(?:#.*)?$',               # Optional trailing comment until end of line
            stripped,
        )
        if string_match:
            value = string_match.group('bare_double') or string_match.group('bare_single')
            line_map.setdefault(value, line_no)

    return line_map


def verify_manifest(
    manifest_path: Path,
    repo_root: Path,
    verbose: bool = False,
    output_format: str = "summary",
) -> int:
    """
    Verify that all source files in the sync manifest exist.
    
    Args:
        manifest_path: Path to the sync-public.toml manifest file.
        repo_root: Root directory of the repository.
        verbose: Whether to output details about every file checked.
        
    Returns:
        int: 0 if all files exist, 1 if any files are missing.
    """
    if not manifest_path.exists():
        message = f"Manifest file not found: {manifest_path}"
        print(f"❌ {message}", file=sys.stderr)
        if output_format == "github":
            emit_github_error(to_repo_relative(manifest_path, repo_root), message)
        return 1
    
    try:
        with open(manifest_path, 'rb') as f:
            config = tomllib.load(f)
    except Exception as e:
        message = f"Error reading manifest file: {e}"
        print(f"❌ {message}", file=sys.stderr)
        if output_format == "github":
            emit_github_error(to_repo_relative(manifest_path, repo_root), message)
        return 1
    
    files = config.get('files', [])
    if not files:
        print("⚠️  No files found in manifest", file=sys.stderr)
        return 0
    
    print(f"🔍 Verifying {len(files)} file(s) in sync manifest...")
    
    missing_files = []
    line_map = load_manifest_line_map(manifest_path) if output_format == "github" else {}
    checked_files = 0
    
    for entry in files:
        # Handle both string paths and dict entries with 'source' and 'dest'
        if isinstance(entry, dict):
            source_path = entry.get('source')
            if not source_path:
                print(f"⚠️  Skipping entry with no 'source': {entry}", file=sys.stderr)
                continue
        else:
            source_path = entry
        
        full_path = repo_root / source_path
        checked_files += 1
        
        if full_path.exists():
            if verbose:
                print(f"✅ {source_path}")
        else:
            if output_format == "summary":
                print(f"❌ Missing: {source_path}", file=sys.stderr)
            missing_files.append(source_path)
    
    if missing_files:
        if output_format == "github":
            manifest_file = to_repo_relative(manifest_path, repo_root)
            for missing in missing_files:
                emit_github_error(
                    manifest_file,
                    f"Missing file in sync-public.toml: {missing}",
                    line_map.get(missing),
                )

        print(f"\n❌ {len(missing_files)} file(s) missing from repository:", file=sys.stderr)
        for missing in missing_files:
            print(f"   - {missing}", file=sys.stderr)
        return 1
    
    print(f"✅ All {checked_files} file(s) in manifest exist in repository")
    return 0


def main():
    """Main entry point for the script."""
    parser = argparse.ArgumentParser(
        description="Verify that all files in sync-public.toml exist in the repository."
    )
    parser.add_argument(
        '--manifest',
        type=Path,
        default=Path('sync-public.toml'),
        help='Path to sync-public.toml manifest file (default: sync-public.toml)'
    )
    parser.add_argument(
        '--repo-root',
        type=Path,
        default=Path('.'),
        help='Root directory of the repository (default: current directory)'
    )
    parser.add_argument(
        '-v', '--verbose',
        action='store_true',
        help='Show details for every file checked'
    )
    parser.add_argument(
        '--format',
        choices=['summary', 'github'],
        default='summary',
        help='Output format (default: summary)'
    )
    
    args = parser.parse_args()
    repo_root = args.repo_root.resolve()

    return verify_manifest(args.manifest, repo_root, args.verbose, args.format)


if __name__ == '__main__':
    sys.exit(main())
