#!/usr/bin/env python3
"""
BBCode to Markdown and Bold-to-Heading Migration Tool for GhostFx.

Features:
1. BBCode Syntax Migration:
   - [code]...[/code] -> ```\n...\n``` (multiline) or `...` (inline)
   - [quote]...[/quote] -> > ...
   - [quote=Author]...[/quote] -> > **Author:** ...
   - [url=TARGET]TEXT[/url] -> [TEXT](TARGET)
   - [url]TARGET[/url] -> [TARGET](TARGET)
   - Malformed links like [url][URL\[/url\]](URL) -> [URL](URL)
   - [img]TARGET[/img] -> ![](TARGET)
   - [b]...[/b] -> **...**
   - [i]...[/i] -> *...*
   - [u]...[/u] -> <u>...</u>
   - [s]...[/s] -> ~~...~~
   - [color], [size], [align], [center], [font] tags stripped
   - Frontmatter metaDescription/description cleaned of residual BBCode
2. Bold to Markdown Heading Detection & Conversion:
   - Identifies standalone bold lines (\*\*Title\*\*, **Title**, __Title__)
   - Checks semantic context (not full sentence, length <= 75 chars, section title)
   - Converts to markdown heading: ## Title
   - Unescapes inline \\*\\*word\\*\\* to **word**
"""

import os
import re
import glob
import sys

def migrate_post(content, filepath, apply_headings=True):
    parts = content.split('---', 2)
    has_fm = len(parts) >= 3
    fm = parts[1] if has_fm else ''
    body = parts[2] if has_fm else content
    
    changes = []
    
    # 1. Clean residual BBCode from frontmatter (description / metaDescription)
    fm_clean = fm
    if re.search(r'\[/?(b|i|u|s|code|quote|url|img|list|\*|color|size|align|center|font)(?:=[^\]]+)?\]', fm_clean, re.IGNORECASE):
        fm_clean = re.sub(r'\[/?(b|i|u|s|code|quote|url|img|list|\*|color|size|align|center|font)(?:=[^\]]+)?\]', '', fm_clean)
        changes.append("Cleaned residual BBCode in frontmatter")
    
    body_clean = body
    original_body = body
    
    # 2. [code]...[/code]
    def repl_code(m):
        code_text = m.group(1)
        if '\n' in code_text.strip():
            # Multiline code block
            lines = code_text.strip('\r\n').splitlines()
            code_body = '\n'.join(lines)
            return f"\n```\n{code_body}\n```\n"
        else:
            return f"`{code_text.strip()}`"
            
    if re.search(r'\[code(?:=[^\]]+)?\]', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\[code(?:=[^\]]+)?\](.*?)\[/code\]', repl_code, body_clean, flags=re.DOTALL | re.IGNORECASE)
        # Handle any stray unclosed [code] or [/code]
        body_clean = re.sub(r'\[/?code\]', '', body_clean, flags=re.IGNORECASE)
        changes.append("Converted [code] tags to markdown code blocks / inline code")
        
    # 3. [quote]...[/quote]
    def repl_quote(m):
        author = m.group(1)
        quote_text = m.group(2).strip()
        quote_lines = quote_text.splitlines()
        res = []
        if author:
            author_clean = author.strip('="\'')
            res.append(f"> **{author_clean}:**")
        for line in quote_lines:
            res.append(f"> {line}")
        return '\n' + '\n'.join(res) + '\n'
        
    if re.search(r'\[quote(?:=[^\]]+)?\]', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\[quote(=[^\]]+)?\](.*?)\[/quote\]', repl_quote, body_clean, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'\[/?quote\]', '', body_clean, flags=re.IGNORECASE)
        changes.append("Converted [quote] tags to blockquotes")
        
    # 4. URLs
    if re.search(r'\[url', body_clean, re.IGNORECASE):
        # [url=TARGET]TEXT[/url]
        body_clean = re.sub(r'\[url=([^\]]+)\](.*?)\[/url\]', r'[\2](\1)', body_clean, flags=re.DOTALL | re.IGNORECASE)
        # Malformed markdown links wrapped in [url]
        body_clean = re.sub(r'\[url\]\s*\[([^\]]+)\\?\[/url\\?\]\]\(([^\)]+)\)', r'[\1](\2)', body_clean, flags=re.IGNORECASE)
        body_clean = re.sub(r'\[url\]\s*\[([^\]]+)\]\(([^\)]+)\)\s*\[/url\]', r'[\1](\2)', body_clean, flags=re.IGNORECASE)
        body_clean = re.sub(r'\[url\]\s*\[([^\]]+)\]\(([^\)]+)\)', r'[\1](\2)', body_clean, flags=re.IGNORECASE)
        # Simple [url]TARGET[/url]
        body_clean = re.sub(r'\[url\](.*?)\[/url\]', r'[\1](\1)', body_clean, flags=re.IGNORECASE)
        # Stray [url] tags
        body_clean = re.sub(r'\[/?url\]', '', body_clean, flags=re.IGNORECASE)
        changes.append("Converted [url] tags to markdown links")
        
    # 5. [img]...[/img]
    if re.search(r'\[img', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\[img(?:=[^\]]+)?\](.*?)\[/img\]', r'![](\1)', body_clean, flags=re.IGNORECASE)
        body_clean = re.sub(r'\[/?img\]', '', body_clean, flags=re.IGNORECASE)
        changes.append("Converted [img] tags to markdown image embeds")
        
    # 6. Inline BBCode formatting
    if re.search(r'\[(b|i|u|s)\]', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\[b\](.*?)\[/b\]', r'**\1**', body_clean, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'\[i\](.*?)\[/i\]', r'*\1*', body_clean, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'\[u\](.*?)\[/u\]', r'<u>\1</u>', body_clean, flags=re.DOTALL | re.IGNORECASE)
        body_clean = re.sub(r'\[s\](.*?)\[/s\]', r'~~\1~~', body_clean, flags=re.DOTALL | re.IGNORECASE)
        changes.append("Converted [b], [i], [u], [s] inline formatting to markdown")
        
    # 7. Strip stylistic BBCode containers & legacy CMS shortcodes
    if re.search(r'\[/?(color|size|align|center|font)', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\[/?(color|size|align|center|font)(?:=[^\]]+)?\]', '', body_clean, flags=re.IGNORECASE)
        changes.append("Stripped stylistic BBCode tags ([color], [size], [align], [center], [font])")

    # 7b. Strip legacy Joomla {loadposition ...} shortcodes and stray empty backticks
    if re.search(r'\{loadposition\s+[^}]+\}', body_clean, re.IGNORECASE):
        body_clean = re.sub(r'\{loadposition\s+[^}]+\}', '', body_clean, flags=re.IGNORECASE)
        changes.append("Stripped legacy CMS shortcodes ({loadposition ...})")

    # 7c. Populate image alt text from immediately following italic caption (*Caption* or \*Caption\*)
    def repl_img_caption(m):
        alt = m.group(1).strip()
        url = m.group(2).strip()
        trailing = m.group(3)
        caption = m.group(4).strip()
        # Clean all backslashes and asterisks from caption to get clean text
        clean_caption = re.sub(r'\\?[\*\[\]]', '', caption).strip()
        if not alt and clean_caption:
            return f"![{clean_caption}]({url}){trailing}*{clean_caption}*"
        return m.group(0)

    body_clean = re.sub(r'!\[([^\]]*)\]\(([^\)]+)\)(\s*\n\s*)\\?\*([^\n]+?)\\?\*(?=\s*(?:\n|$))', repl_img_caption, body_clean)
    # Clean any malformed ![alt\](...)
    body_clean = re.sub(r'!\[([^\]]*)\\\]\(', r'![\1](', body_clean)

    # 8. Bold Heading Detection & Conversion
    lines = body_clean.splitlines()
    new_lines = []
    heading_count = 0
    italic_count = 0
    in_code_block = False
    
    for idx, line in enumerate(lines):
        trimmed = line.strip()
        
        # Track fenced code blocks (``` or ~~~)
        if trimmed.startswith('```') or trimmed.startswith('~~~'):
            in_code_block = not in_code_block
            new_lines.append(line)
            continue
            
        if in_code_block:
            # Unescape backslash-escaped asterisks and underscores in verbatim code blocks (e.g. VFP comments, constants)
            line = line.replace(r'\*', '*').replace(r'\_', '_')
            new_lines.append(line)
            continue
            
        if apply_headings:
            # Check escaped bold: strictly \*\*Heading\*\* or \*\*Heading:\*\*
            m_esc = re.match(r'^\s*\\\*\\\*(.+?)\\\*\\\*:?\s*$', trimmed)
            # Check normal bold on isolated line: strictly **Heading** or **Heading:** or __Heading__
            m_norm = re.match(r'^\s*(\*\*|__)(.+?)\1:?\s*$', trimmed)
            
            m = m_esc or m_norm
            if m:
                heading_raw = m.group(1 if m_esc else 2).strip()
                clean_h = heading_raw.replace('\\*', '*').replace('\\_', '_')
                
                # Check previous and next lines for context
                prev_line = lines[idx-1].strip() if idx > 0 else ''
                next_line = lines[idx+1].strip() if idx < len(lines)-1 else ''
                
                # Adjacent bold check: if prev or next line is also bold, it's a bold paragraph, not a heading!
                is_prev_bold = bool(re.match(r'^(\*\*|__|\\*\\\*).+(\*\*|__|\\*\\\*):?$', prev_line))
                is_next_bold = bool(re.match(r'^(\*\*|__|\\*\\\*).+(\*\*|__|\\*\\\*):?$', next_line))
                
                # Exclude non-headings:
                # - Multi-line bold paragraphs
                # - Lines with single escaped asterisk comments (\*...)
                # - Ends with comma, semicolon, period, or hyphen
                # - Numbers only, URLs, code snippets, quotes, or all-caps long bulletins
                if (not is_prev_bold and not is_next_bold and
                    len(clean_h) <= 75 and 
                    not clean_h.startswith('*') and
                    not clean_h.startswith('#') and
                    not clean_h.endswith('.') and
                    not clean_h.endswith(',') and
                    not clean_h.endswith(';') and
                    not clean_h.endswith('-') and
                    not re.match(r'^\d+$', clean_h) and
                    not clean_h.lower().startswith('http') and
                    not clean_h.startswith('`') and
                    not clean_h.startswith('(') and
                    not clean_h.startswith('\"') and
                    not (clean_h.isupper() and len(clean_h) > 20)):
                    
                    new_heading = f"## {clean_h}"
                    new_lines.append(new_heading)
                    heading_count += 1
                    continue
                    
        # Replace remaining escaped bold \*\*word\*\* with **word** outside code blocks
        if r'\*\*' in line:
            line = line.replace(r'\*\*', '**')

        # Convert escaped bullet points at start of line: \* item -> * item
        if re.match(r'^\s*\\\*\s+', line):
            line = re.sub(r'^(\s*)\\\*\s+', r'\1* ', line)

        # Convert escaped italics (\*text\* or *text\* or \*text*) to clean markdown *text*
        if r'\*' in line:
            line = re.sub(r'\\\*([^\*\n]+?)\\\*', r'*\1*', line)
            line = re.sub(r'\*([^\*\n]+?)\\\*', r'*\1*', line)
            line = re.sub(r'\\\*([^\*\n]+?)\*', r'*\1*', line)

        # Unescape underscores outside code blocks (e.g. \_ -> _)
        if r'\_' in line:
            line = re.sub(r'\\_', '_', line)
            
        new_lines.append(line)
        
    if heading_count > 0:
        changes.append(f"Parsed {heading_count} bold section line(s) to '## Heading'")
    if italic_count > 0:
        changes.append(f"Converted {italic_count} escaped italic instance(s) (\\*...\\*) to markdown *...*")
        
    body_final = '\n'.join(new_lines)
    
    if has_fm:
        final_content = f"---{fm_clean}---{body_final}"
    else:
        final_content = body_final
        
    is_changed = (final_content != content)
    return final_content, is_changed, changes

def main():
    dry_run = '--dry-run' in sys.argv
    posts_dir = 'posts'
    md_files = sorted(glob.glob(os.path.join(posts_dir, '**', '*.md'), recursive=True))
    
    print(f"Scanning {len(md_files)} markdown files in {posts_dir}...")
    
    modified_count = 0
    report = []
    
    for f in md_files:
        with open(f, 'r', encoding='utf-8', errors='ignore') as fp:
            original = fp.read()
            
        final_content, is_changed, changes = migrate_post(original, f, apply_headings=True)
        
        if is_changed:
            modified_count += 1
            report.append({
                'file': f,
                'changes': changes
            })
            if not dry_run:
                with open(f, 'w', encoding='utf-8') as fp:
                    fp.write(final_content)
                    
    print(f"\nMigration completed{' (DRY RUN)' if dry_run else ''}!")
    print(f"Total modified files: {modified_count} / {len(md_files)}")
    print("\n--- Summary by file ---")
    for item in report:
        print(f"\n{item['file']}:")
        for ch in item['changes']:
            print(f"  - {ch}")

if __name__ == '__main__':
    main()
