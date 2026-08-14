#!/usr/bin/env python3
"""
scripts/indent-vfp-code.py

Automatically detects Visual FoxPro (VFP) code blocks across all markdown files
in the repository, adds standard structured indentation (procedures, with-blocks,
if/else branches, do-case/case constructs, loops, try/catch), and tags untagged
code fences with '```foxpro'.
"""

import os
import re
import sys
import glob

def is_vfp_code(code_text):
    lower = code_text.lower()
    
    # Exclude obvious non-VFP code blocks
    if re.search(r'\b(using\s+System|namespace\s+\w+|public\s+class\s+\w+|private\s+void\s+\w+)\b', code_text):
        return False
    if re.search(r'\b(function\s*\([^\)]*\)\s*\{|const\s+\w+\s*=|let\s+\w+\s*=|var\s+\w+\s*=.*;)\b', code_text) and not 'thisform' in lower:
        return False
    if re.search(r'<\?php|\b(\$this->|\$db->|\$_GET|\$_POST)\b', code_text):
        return False
    if re.search(r'^\s*<(\?xml|html|div|pre|table|script)\b', code_text, re.MULTILINE):
        return False
    if re.search(r'^\s*\{\s*\"', code_text):
        return False
    if re.search(r'\b(import\s+\w+|def\s+\w+\s*\(.*?\):|from\s+\w+\s+import)\b', code_text):
        return False

    vfp_strong_patterns = [
        r'\bprocedure\s+this\b', r'\bprocedure\s+\w+', r'\bendproc\b',
        r'\bfunction\s+\w+.*?\bendfunc\b', r'\blparameters\b',
        r'\bwith\s+this\b', r'\bendwith\b',
        r'\bdo\s+case\b', r'\bendcase\b',
        r'\bdeclare\s+\w+\s+in\s+win32api\b',
        r'\bthisform\b', r'\b_screen\b', r'\bthisformset\b',
        r'\bnewobject\s*\(', r'\bcreateobject\s*\(',
        r'\bobjtoclient\s*\(', r'\bbittest\s*\(',
        r'\baddbs\s*\(', r'\bgetenv\s*\(',
        r'\bscan\b.*?\bendscan\b', r'\bdo\s+while\b.*?\benddo\b',
        r'\bdefine\s+class\b', r'\benddefine\b',
        r'\bset\s+(deleted|exact|near|safety|exclusive|talk|multilocks)\s+on\b',
        r'\bset\s+(deleted|exact|near|safety|exclusive|talk|multilocks)\s+off\b',
        r'\bscatter\s+name\b', r'\bgather\s+name\b',
        r'^\s*\*================================',
        r'^\s*\*---+\s+\w+'
    ]

    strong_matches = sum(1 for p in vfp_strong_patterns if re.search(p, code_text, re.IGNORECASE | re.MULTILINE))
    if strong_matches >= 1:
        return True

    vfp_secondary_patterns = [
        r'\bthis\.\w+', r'\bm\.\w+', r'\blocal\s+\w+', r'#define\s+\w+',
        r'&&', r'\.t\.', r'\.f\.', r'\bendif\b', r'\belse\b', r'\bendif\b'
    ]
    secondary_matches = sum(1 for p in vfp_secondary_patterns if re.search(p, code_text, re.IGNORECASE))
    return secondary_matches >= 3

def indent_vfp(code_lines, indent_str="  "):
    indented = []
    level = 0
    in_continuation = False
    case_depth = 0
    case_body = []
    
    for raw_line in code_lines:
        line = raw_line.strip()
        if not line:
            indented.append("")
            in_continuation = False
            continue
            
        lower = line.lower()
        is_comment = line.startswith("*") or lower.startswith("note ")
        
        # Check dedent before line
        if not is_comment:
            if re.match(r"^endcase\b", lower):
                if case_body and case_body[-1]:
                    level = max(0, level - 1)
                if case_depth > 0:
                    case_depth -= 1
                    case_body.pop()
                    level = max(0, level - 1)
            elif re.match(r"^(case|otherwise)\b", lower):
                if case_body and case_body[-1]:
                    level = max(0, level - 1)
                    case_body[-1] = False
            elif re.match(r"^(endproc|endfunc|enddefine|endwith|endif|enddo|endfor|next|endscan|endtry)\b", lower):
                level = max(0, level - 1)
            elif re.match(r"^(else|catch|finally)\b", lower):
                level = max(0, level - 1)
                
        curr_indent = (level + (1 if in_continuation else 0)) * indent_str
        indented.append(f"{curr_indent}{line}")
        
        # Check continuation line with semicolon
        if not is_comment and line.endswith(";"):
            in_continuation = True
        else:
            in_continuation = False
            
        # Check indent after line
        if not is_comment:
            if re.match(r"^do\s+case\b", lower):
                level += 1
                case_depth += 1
                case_body.append(False)
            elif re.match(r"^(case|otherwise)\b", lower):
                level += 1
                if case_body:
                    case_body[-1] = True
            elif re.match(r"^(procedure|function|define\s+class|with|if|else|do\s+while|for|scan|try|catch|finally)\b", lower):
                level += 1
                
    return indented

def process_markdown_file(file_path, dry_run=False):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        content = f.read()

    parts = content.split('---', 2)
    if len(parts) < 3:
        return False, []
        
    fm = parts[1]
    body = parts[2]
    
    modified = False
    blocks_formatted = 0

    def repl_block(m):
        nonlocal modified, blocks_formatted
        lang = m.group(1).strip()
        code = m.group(2)
        
        # Check if already tagged as another language
        if lang in ['csharp', 'cs', 'javascript', 'js', 'json', 'html', 'xml', 'css', 'sql', 'bash', 'sh', 'powershell', 'ps1', 'php', 'python', 'py', 'mermaid', 'yaml', 'yml']:
            return m.group(0)
            
        if lang in ['foxpro', 'vfp', 'visualfoxpro'] or is_vfp_code(code):
            indented_lines = indent_vfp(code.splitlines())
            new_code = '\n'.join(indented_lines) + '\n'
            new_lang = 'foxpro' if not lang else lang
            if new_code != code or new_lang != lang:
                modified = True
                blocks_formatted += 1
                return f"```{new_lang}\n{new_code}```"
                
        return m.group(0)

    new_body = re.sub(r'```([a-zA-Z0-9_-]*)\n(.*?)```', repl_block, body, flags=re.DOTALL)

    if modified and not dry_run:
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(f"---{fm}---{new_body}")

    return modified, blocks_formatted

def main():
    dry_run = '--dry-run' in sys.argv
    posts_dir = 'posts'
    md_files = sorted(glob.glob(os.path.join(posts_dir, '**', '*.md'), recursive=True))

    total_files = 0
    total_blocks = 0

    print(f"Scanning {len(md_files)} markdown files in {posts_dir}...")
    for f in md_files:
        changed, count = process_markdown_file(f, dry_run=dry_run)
        if changed:
            total_files += 1
            total_blocks += count
            print(f"  [{count} block(s)] {f}")

    print(f"\nFormatting complete! Formatted {total_blocks} VFP code blocks across {total_files} files.")

if __name__ == '__main__':
    main()
