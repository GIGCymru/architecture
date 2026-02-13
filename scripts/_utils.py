"""Shared utility functions for QA scripts."""

import subprocess
import sys
from pathlib import Path

# tomllib is standard library in Python 3.11+, fall back to tomli for older versions
try:
    import tomllib
except ImportError:
    import tomli as tomllib


def to_repo_relative(path: Path, repo_root: Path) -> str:
    """Return a repository-relative path for display and annotations."""
    full_path = path if path.is_absolute() else (repo_root / path)
    try:
        return full_path.resolve().relative_to(repo_root).as_posix()
    except ValueError:
        return full_path.as_posix()


def emit_github_error(file_path: str, message: str, line_no: int | None = None) -> None:
    """Emit a GitHub Actions annotation error."""
    if line_no:
        print(f"::error file={file_path},line={line_no}::{message}")
    else:
        print(f"::error file={file_path}::{message}")


def load_manifest_sources(manifest_path: Path) -> set[str] | None:
    """Load file sources listed in the sync manifest."""
    if not manifest_path.exists():
        print(f"ERROR: Manifest file not found: {manifest_path}", file=sys.stderr)
        return None

    try:
        with open(manifest_path, "rb") as f:
            config = tomllib.load(f)
    except Exception as exc:
        print(f"ERROR: Error reading manifest file: {exc}", file=sys.stderr)
        return None

    files = config.get("files", [])
    if not files:
        print("WARNING: No files found in manifest", file=sys.stderr)

    sources: set[str] = set()
    for entry in files:
        if isinstance(entry, dict):
            source_path = entry.get("source")
            if not source_path:
                print(f"WARNING: Skipping entry with no 'source': {entry}", file=sys.stderr)
                continue
        else:
            source_path = entry
        sources.add(source_path)

    return sources


def get_tracked_files(repo_root: Path) -> list[str] | None:
    """Return git-tracked files relative to the repository root."""
    result = subprocess.run(
        ["git", "-C", str(repo_root), "ls-files"],
        capture_output=True,
        text=True,
        check=False,
    )

    if result.returncode != 0:
        print("ERROR: Failed to list git-tracked files", file=sys.stderr)
        if result.stderr:
            print(result.stderr.strip(), file=sys.stderr)
        return None

    return [line for line in result.stdout.splitlines() if line.strip()]


def get_excluded_files(manifest_path: Path, repo_root: Path) -> set[str] | None:
    """
    Get files excluded from sync-public.toml.
    
    Returns a set of repository-relative paths that are git-tracked but not
    included in the sync manifest.
    """
    manifest_sources = load_manifest_sources(manifest_path)
    if manifest_sources is None:
        return None

    tracked_files = get_tracked_files(repo_root)
    if tracked_files is None:
        return None

    return set(tracked_files) - manifest_sources
