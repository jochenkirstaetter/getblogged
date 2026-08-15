#!/usr/bin/env python3
"""
Post-processing script to generate clean, frontmatter-free Markdown files in posts/_site/raw/.
Reads markdown source files from posts/published/ and posts/pages/, strips YAML frontmatter,
and outputs clean .md files to posts/_site/raw/ for Copy/View Markdown features.
"""

import os
import re
import sys
from pathlib import Path

def strip_frontmatter(content: str) -> str:
    """Removes YAML frontmatter (between opening and closing --- markers)."""
    pattern = r'^---\s*\n.*?\n---\s*\n'
    return re.sub(pattern, '', content, flags=re.DOTALL)

def process_and_copy_markdown(source_dirs, output_dir: Path):
    output_dir.mkdir(parents=True, exist_ok=True)
    count = 0

    for src_dir in source_dirs:
        if not src_dir.exists():
            print(f"Warning: Source directory {src_dir} does not exist.", file=sys.stderr)
            continue

        for md_file in src_dir.glob('**/*.md'):
            # Skip toc.yml or non-article files
            if md_file.name == 'toc.yml' or md_file.name.startswith('.'):
                continue

            try:
                content = md_file.read_text(encoding='utf-8')
                cleaned = strip_frontmatter(content).strip() + '\n'
                
                # Destination in raw/
                dest_file = output_dir / md_file.name
                dest_file.write_text(cleaned, encoding='utf-8')
                count += 1
            except Exception as ex:
                print(f"Error processing {md_file}: {ex}", file=sys.stderr)

    print(f"Successfully generated {count} clean raw markdown files in {output_dir}.")
    return count

def main():
    repo_root = Path(__file__).resolve().parent.parent
    published_dir = repo_root / 'posts' / 'published'
    pages_dir = repo_root / 'posts' / 'pages'
    output_raw_dir = repo_root / 'posts' / '_site' / 'raw'

    process_and_copy_markdown([published_dir, pages_dir], output_raw_dir)

if __name__ == '__main__':
    main()
