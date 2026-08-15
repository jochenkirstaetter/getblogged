#!/usr/bin/env python3
"""
Comprehensive scanner and cleaner for HTML entities in code blocks:
- Fenced code blocks (``` ... ``` or ~~~ ... ~~~)
- HTML <pre><code>...</code></pre> tags in markdown
- Inline code (`...`)
"""

import re
import html
from pathlib import Path

def decode_entities_in_text(text: str) -> str:
    # Decode HTML entities
    def replace_entity(m):
        ent = m.group(0)
        if ent.lower() == '&nbsp;':
            return ' '
        return html.unescape(ent)
    
    return re.sub(r'&(?:nbsp|amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+|[a-zA-Z]+);', replace_entity, text)

def process_markdown(content: str) -> tuple[str, int]:
    changes = 0

    # 1. Fenced blocks
    fenced_pattern = r'(```[\s\S]*?```|~~~[\s\S]*?~~~)'
    def replace_fenced(match):
        nonlocal changes
        block = match.group(0)
        lines = block.split('\n')
        if len(lines) >= 2:
            header = lines[0]
            footer = lines[-1]
            body = '\n'.join(lines[1:-1])
            new_body = decode_entities_in_text(body)
            if new_body != body:
                changes += 1
                return header + '\n' + new_body + '\n' + footer
        return block

    content = re.sub(fenced_pattern, replace_fenced, content)

    # 2. HTML pre/code tags
    html_pre_pattern = r'(<pre[^>]*><code[^>]*>[\s\S]*?</code></pre>|<pre[^>]*>[\s\S]*?</pre>)'
    def replace_html_pre(match):
        nonlocal changes
        block = match.group(0)
        new_block = decode_entities_in_text(block)
        if new_block != block:
            changes += 1
            return new_block
        return block

    content = re.sub(html_pre_pattern, replace_html_pre, content)

    # 3. Inline code spans (`...`)
    inline_pattern = r'(`[^`\n]+`)'
    def replace_inline(match):
        nonlocal changes
        code = match.group(0)
        inner = code[1:-1]
        new_inner = decode_entities_in_text(inner)
        if new_inner != inner:
            changes += 1
            return f"`{new_inner}`"
        return code

    content = re.sub(inline_pattern, replace_inline, content)

    return content, changes

def main():
    repo_root = Path(__file__).resolve().parent.parent
    posts_dir = repo_root / 'posts'

    total_files = 0
    total_changes = 0

    for md_file in sorted(posts_dir.glob('**/*.md')):
        if '_site' in md_file.parts or '.docfx' in md_file.parts:
            continue
        try:
            content = md_file.read_text(encoding='utf-8')
            new_content, count = process_markdown(content)
            if count > 0 and new_content != content:
                md_file.write_text(new_content, encoding='utf-8')
                total_files += 1
                total_changes += count
                print(f"Fixed {count} item(s) in {md_file.relative_to(repo_root)}")
        except Exception as e:
            print(f"Error reading {md_file}: {e}")

    print(f"\nFinished! Made {total_changes} fix(es) across {total_files} file(s).")

if __name__ == '__main__':
    main()
