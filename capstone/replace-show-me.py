#!/usr/bin/env python3
import os
import re
import html
import sys
from pathlib import Path

def process_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match "Show Me:" or "Show me:" or "Show me..." (with optional colon or ellipsis) followed by any text, then ```html or ```bash block
    pattern = r'[Ss]how [Mm]e[:.]*(.*?)\n+```(html|bash|javascript)\n(.*?)\n```'
    
    def replacement(match):
        show_me_text = match.group(1).strip()
        code_type = match.group(2)  # 'html', 'bash', or 'javascript'
        code_content = match.group(3)
        
        if code_type == 'html':
            escaped_content = html.escape(code_content)
            return f'''<details>
<summary>Show me:{show_me_text}</summary>

<pre><code>{escaped_content}</code></pre>
</details>'''
        else:  # bash or javascript
            escaped_content = html.escape(code_content)
            return f'''<details>
<summary>Show me:{show_me_text}</summary>

<pre><code class="language-{code_type}">{escaped_content}</code></pre>
</details>'''
    
    # Process code blocks first
    new_content, code_count = re.subn(pattern, replacement, content, flags=re.DOTALL)
    
    # Pattern to match "Show Me:" or "Show me:" or "Show me..." followed by any text, then Markdown image
    image_pattern = r'[Ss]how [Mm]e[:.]*(.*?)\n+!\[([^\]]*)\]\(([^)]+)\)'
    
    def image_replacement(match):
        show_me_text = match.group(1).strip()
        alt_text = match.group(2)
        image_url = match.group(3)
        
        return f'''<details>
<summary>Show me:{show_me_text}</summary>

<img src="{image_url}" alt="{alt_text}">
</details>'''
    
    # Process images
    final_content, image_count = re.subn(image_pattern, image_replacement, new_content, flags=re.DOTALL)
    
    total_count = code_count + image_count
    
    if total_count > 0:
        # Create backup
        backup_path = f"{file_path}.bak"
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        # Write modified content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(final_content)
        
        print(f"Modified {file_path} ({total_count} replacements: {code_count} code blocks, {image_count} images, backup at {backup_path})")
        return total_count
    return 0

def main():
    target = sys.argv[1] if len(sys.argv) > 1 else '.'
    total_replacements = 0
    
    if os.path.isfile(target):
        # If it's a specific file, process it directly
        total_replacements = process_file(target)
    else:
        # If it's a directory, recursively find .md files
        for md_file in Path(target).rglob('*.md'):
            total_replacements += process_file(md_file)
    
    print(f"Total replacements: {total_replacements}")

if __name__ == "__main__":
    main()