#!/usr/bin/env python3
"""Check for broken internal markdown links in the documentation."""

import argparse
import os
import re
import sys
from pathlib import Path

from _utils import get_excluded_files, to_repo_relative


def check_links(
    search_path: Path,
    excluded_files: set[str],
    repo_root: Path,
    verbose: bool = False,
    output_format: str = "summary",
) -> int:
    """
    Scan for broken internal markdown links.
    
    Args:
        search_path: The directory or file to search for markdown files.
        verbose: Whether to output details about every link checked.
        
    Returns:
        int: 0 if all links are valid, 1 if broken links are found.
    """
    md_files = []
    
    if search_path.is_file():
        if search_path.suffix == '.md':
            md_files.append(search_path)
    else:
        for root, dirs, files in os.walk(search_path):
            # Ignore hidden directories like .git or .venv
            dirs[:] = [d for d in dirs if not d.startswith('.')]
            for file in files:
                if file.endswith('.md'):
                    md_files.append(Path(root) / file)

    if not md_files:
        print(f"ℹ️ No markdown files found in {search_path}")
        return 0

    link_pattern = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    errors: list[dict[str, object]] = []

    print(f"🔍 Checking internal links in {len(md_files)} file(s) under {search_path}...")

    for md_file in md_files:
        try:
            content = md_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"❌ Error reading {md_file}: {e}", file=sys.stderr)
            continue
        
        in_code_block = False
        md_file_relative = to_repo_relative(md_file, repo_root)

        for line_no, line in enumerate(content.splitlines(), start=1):
            stripped_line = line.strip()
            if stripped_line.startswith("```"):
                in_code_block = not in_code_block
                continue

            if in_code_block:
                continue

            for match in link_pattern.finditer(line):
                text, link = match.group(1), match.group(2)
                column = match.start(0) + 1
                # Skip external links
                if any(link.startswith(s) for s in ['http://', 'https://', 'mailto:', 'tel:']):
                    if verbose:
                        print(f"⏭️  Ignored external link in {md_file}: {link}")
                    continue

                # Remove anchors (e.g., #section-name)
                link_path = link.split('#')[0]
                if not link_path:
                    if verbose:
                        print(f"⏭️  Ignored anchor-only link in {md_file}: {link}")
                    continue

                # Resolve relative path
                # target_path is relative to the directory containing the markdown file
                target_path = (md_file.parent / link_path).resolve()

                # Check if target exists
                target_exists = target_path.exists()

                if not target_exists and link_path.startswith('/'):
                    # If it looks like an absolute path from the repo root
                    target_path = (repo_root / link_path.lstrip('/')).resolve()
                    target_exists = target_path.exists()

                relative_path = None
                try:
                    relative_path = target_path.relative_to(repo_root).as_posix()
                except ValueError:
                    relative_path = None

                if target_exists and relative_path in excluded_files:
                    errors.append(
                        {
                            "file": md_file_relative,
                            "line": line_no,
                            "col": column,
                            "message": f"Excluded link '[{text}]({link})' -> {relative_path}",
                        }
                    )
                elif target_exists:
                    if verbose:
                        print(f"✅ Found valid link in {md_file}: '{text}' -> {target_path}")
                else:
                    errors.append(
                        {
                            "file": md_file_relative,
                            "line": line_no,
                            "col": column,
                            "message": f"Broken link '[{text}]({link})'",
                        }
                    )

    if errors:
        if output_format == "github":
            for error in errors:
                print(
                    "::error file={file},line={line},col={col}::{message}".format(
                        file=error["file"],
                        line=error["line"],
                        col=error["col"],
                        message=error["message"],
                    )
                )

        print(f"❌ Found {len(errors)} link issue(s):")
        for error in errors:
            print(f"  - {error['file']}:{error['line']}: {error['message']}")
        return 1

    print("✅ All internal links resolved successfully!")
    return 0

def main():
    parser = argparse.ArgumentParser(description="Check for broken internal links in markdown files.")
    parser.add_argument(
        "path", 
        type=Path, 
        nargs='?', 
        default=Path("doc"), 
        help="The directory or file to check (default: doc)"
    )
    parser.add_argument(
        "-v", "--verbose",
        action="store_true",
        help="Enable verbose output showing all checked links"
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
        choices=["summary", "github"],
        default="summary",
        help="Output format (default: summary)",
    )
    args = parser.parse_args()

    if not args.path.exists():
        print(f"❌ Error: Path '{args.path}' does not exist.", file=sys.stderr)
        return 1

    repo_root = args.repo_root.resolve()
    excluded_files = get_excluded_files(args.manifest, repo_root)
    if excluded_files is None:
        return 1

    return check_links(
        args.path,
        excluded_files,
        repo_root,
        verbose=args.verbose,
        output_format=args.format,
    )

if __name__ == "__main__":
    sys.exit(main())
