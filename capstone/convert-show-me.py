#!/usr/bin/env python3
"""
Convert Show Me Script
=====================

This script converts "Show Me:" sections in markdown files to collapsible HTML details.
It handles both code blocks and images that follow "Show Me:" text.

Usage:
    python3 convert-show-me.py [target]

If no argument provided, processes: capstone/capstone-levels/

Examples of conversions:
- "Show Me: the HTML code" followed by ```html block
- "Show me: the terminal output" followed by ```bash block  
- "Show Me: the screenshot" followed by ![alt](image.png)
"""

import os
import re
import html
import sys
from pathlib import Path

def process_file(file_path):
    """
    Process a single markdown file to convert Show Me sections.
    
    Args:
        file_path (str): Path to the markdown file
        
    Returns:
        int: Number of replacements made
    """
    
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    original_content = content
    total_replacements = 0
    
    # Pattern 1: "Show Me:" or "Show me:" followed by text, then code block
    # Matches: Show Me: description\n\n```language\ncode\n```
    code_pattern = r'([Ss]how [Mm]e[:.]*)\s*(.*?)\n+```(html|bash|javascript|css|json|python|sql)\n(.*?)\n```'
    
    def code_replacement(match):
        show_me_text = match.group(1).strip()
        description = match.group(2).strip()
        code_type = match.group(3)
        code_content = match.group(4)
        
        # Escape HTML characters in code content
        escaped_content = html.escape(code_content)
        
        # Create collapsible details
        return f'''<details>
<summary>{show_me_text} {description}</summary>

<pre><code class="language-{code_type}">{escaped_content}</code></pre>
</details>'''
    
    # Process code blocks
    content, code_count = re.subn(code_pattern, code_replacement, content, flags=re.DOTALL)
    total_replacements += code_count
    
    # Pattern 2: "Show Me:" followed by text, then markdown image
    # Matches: Show Me: description\n\n![alt](image.png)
    image_pattern = r'([Ss]how [Mm]e[:.]*)\s*(.*?)\n+!\[([^\]]*)\]\(([^)]+)\)'
    
    def image_replacement(match):
        show_me_text = match.group(1).strip()
        description = match.group(2).strip()
        alt_text = match.group(3)
        image_url = match.group(4)
        
        return f'''<details>
<summary>{show_me_text} {description}</summary>

<img src="{image_url}" alt="{alt_text}">
</details>'''
    
    # Process images
    content, image_count = re.subn(image_pattern, image_replacement, content, flags=re.DOTALL)
    total_replacements += image_count
    
    # Write modified content if changes were made
    if total_replacements > 0:
        # Create backup
        backup_path = f"{file_path}.bak"
        with open(backup_path, 'w', encoding='utf-8') as f:
            f.write(original_content)
        
        # Write modified content
        with open(file_path, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print(f"✅ Modified {os.path.basename(file_path)} ({total_replacements} replacements: {code_count} code blocks, {image_count} images)")
        return total_replacements
    
    return 0

def main():
    # Default target
    default_target = "capstone/capstone-levels"
    
    # Get command line argument
    target = sys.argv[1] if len(sys.argv) > 1 else default_target
    
    total_replacements = 0
    files_processed = 0
    
    if os.path.isfile(target):
        # Process single file
        if target.endswith('.md'):
            replacements = process_file(target)
            total_replacements += replacements
            files_processed = 1
        else:
            print(f"❌ Error: '{target}' is not a markdown file")
            sys.exit(1)
    else:
        # Process directory
        if not os.path.exists(target):
            print(f"❌ Error: Target '{target}' not found")
            sys.exit(1)
        
        # Find all markdown files
        md_files = list(Path(target).glob('*.md'))
        
        if not md_files:
            print(f"❌ Error: No markdown files found in '{target}'")
            sys.exit(1)
        
        print(f"📁 Processing {len(md_files)} markdown files in {target}")
        print()
        
        for md_file in md_files:
            replacements = process_file(str(md_file))
            total_replacements += replacements
            files_processed += 1
    
    print(f"\n🎉 Processed {files_processed} files, made {total_replacements} total replacements")

if __name__ == "__main__":
    main()
