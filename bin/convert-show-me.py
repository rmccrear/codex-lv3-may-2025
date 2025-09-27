#!/usr/bin/env python3
"""
Convert Show Me Sections Script
===============================

This script converts "Show Me" sections in markdown files to collapsible HTML details.
It can be used for any project with "Show Me" sections.

Usage:
    python3 convert-show-me.py [target]

Arguments:
    target    - File or directory to process

Examples:
    # Process all files in directory
    python3 convert-show-me.py mad-libs/mad-libs-levels
    
    # Process specific file
    python3 convert-show-me.py mad-libs/mad-libs-levels/mad-libs-lv-1.md
"""

import os
import re
import sys
import html
from pathlib import Path

def convert_show_me_sections(content):
    """
    Convert "Show Me" sections to collapsible HTML details.
    
    Args:
        content (str): Markdown content
    
    Returns:
        str: Converted content
    """
    
    # Pattern to match "Show Me" sections
    # Matches: "Show Me: description" followed by code block OR existing HTML details
    pattern = r'Show Me: ([^\n]+)\n\n(```(\w+)?\n(.*?)\n```)'
    
    # Also handle existing HTML details that need escaping fixes
    html_pattern = r'(<pre><code class="language-(\w+)">)(.*?)(</code></pre>)'
    
    def replace_show_me(match):
        description = match.group(1).strip()
        code_block = match.group(2)
        language = match.group(3) or ''
        code_content = match.group(4)
        
        # Escape HTML characters in code content for proper display
        # Only escape raw < and > characters, not already escaped ones
        escaped_code = code_content.replace('<', '&lt;').replace('>', '&gt;')
        
        # Create collapsible details
        details_html = f'''<details>
<summary>Show Me: {description}</summary>

<pre><code class="language-{language}">{escaped_code}</code></pre>
</details>'''
        
        return details_html
    
    def fix_html_escaping(match):
        open_tag = match.group(1)
        language = match.group(2)
        code_content = match.group(3)
        close_tag = match.group(4)
        
        # Escape HTML characters in code content for proper display
        # Only escape raw < and > characters, not already escaped ones
        escaped_code = code_content.replace('<', '&lt;').replace('>', '&gt;')
        
        return f"{open_tag}{escaped_code}{close_tag}"
    
    # Replace all "Show Me" sections
    converted_content = re.sub(pattern, replace_show_me, content, flags=re.DOTALL)
    
    # Fix HTML escaping in existing code blocks
    converted_content = re.sub(html_pattern, fix_html_escaping, converted_content, flags=re.DOTALL)
    
    return converted_content

def process_file(file_path):
    """
    Process a single markdown file.
    
    Args:
        file_path (str): Path to the markdown file
    
    Returns:
        bool: True if file was modified, False if no changes
    """
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has "Show Me" sections or HTML code blocks that need escaping
    if 'Show Me:' not in content and '<pre><code class=' not in content:
        return False
    
    # Convert the content
    converted_content = convert_show_me_sections(content)
    
    # Check if content actually changed
    if converted_content == content:
        return False
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(converted_content)
    
    return True

def process_directory(directory_path):
    """
    Process all markdown files in a directory.
    
    Args:
        directory_path (str): Path to the directory
    
    Returns:
        tuple: (files_processed, files_modified)
    """
    
    files_processed = 0
    files_modified = 0
    
    # Find all markdown files
    for file_path in Path(directory_path).glob('*.md'):
        files_processed += 1
        
        if process_file(str(file_path)):
            files_modified += 1
            print(f"✅ Converted: {file_path.name}")
        else:
            print(f"⏭️  Skipped: {file_path.name} (no Show Me sections)")
    
    return files_processed, files_modified

def main():
    # Get command line arguments
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a target file or directory")
        print("Usage: python3 convert-show-me.py [target]")
        sys.exit(1)
    
    target = sys.argv[1]
    
    # Validate target exists
    if not os.path.exists(target):
        print(f"❌ Error: Target '{target}' not found")
        sys.exit(1)
    
    print(f"📁 Processing: {target}")
    print()
    
    try:
        if os.path.isfile(target):
            # Process single file
            if process_file(target):
                print(f"✅ Converted: {os.path.basename(target)}")
            else:
                print(f"⏭️  Skipped: {os.path.basename(target)} (no Show Me sections)")
            
            files_processed = 1
            files_modified = 1 if 'Show Me:' in open(target, 'r').read() else 0
            
        elif os.path.isdir(target):
            # Process directory
            files_processed, files_modified = process_directory(target)
            
        else:
            print(f"❌ Error: '{target}' is neither a file nor a directory")
            sys.exit(1)
        
        print(f"\n🎉 Conversion Complete!")
        print(f"📊 Processed {files_processed} files, modified {files_modified} files")
        
    except Exception as e:
        print(f"❌ Error processing target: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
