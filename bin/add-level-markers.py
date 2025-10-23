#!/usr/bin/env python3
"""
Add Level Start Markers Script
==============================

This script automatically adds <!-- LEVEL_START --> markers before # Level X patterns
in markdown files, but only if they're not already present.

Usage:
    python3 add-level-markers.py [target]

Arguments:
    target    - File or directory to process

Examples:
    # Process all files in directory
    python3 add-level-markers.py week5/db-mini-project/
    
    # Process specific file
    python3 add-level-markers.py week5/db-mini-project/project-guide-show-me.md
"""

import os
import re
import sys
from pathlib import Path

def add_level_markers(content):
    """
    Add <!-- LEVEL_START --> markers before # Level X patterns if not already present.
    
    Args:
        content (str): Markdown content
    
    Returns:
        str: Content with level markers added
    """
    
    # Pattern to match # Level X (where X is a number)
    level_pattern = r'^# Level (\d+)'
    
    lines = content.split('\n')
    modified_lines = []
    changes_made = 0
    
    for i, line in enumerate(lines):
        # Check if this line matches # Level X pattern
        level_match = re.match(level_pattern, line)
        
        if level_match:
            # Check if there's already a LEVEL_START marker in the previous few lines
            has_marker = False
            for j in range(max(0, i-3), i):
                if lines[j].strip() == '<!-- LEVEL_START -->':
                    has_marker = True
                    break
            
            if has_marker:
                # Marker already exists, just add the line
                modified_lines.append(line)
            else:
                # Check if there's a separator line before this level
                if i > 0 and lines[i-1].strip() == '---':
                    # Add marker after the existing separator
                    modified_lines.append('<!-- LEVEL_START -->')
                    modified_lines.append('')
                    modified_lines.append(line)
                    changes_made += 1
                else:
                    # Add separator and marker before the level
                    modified_lines.append('---')
                    modified_lines.append('')
                    modified_lines.append('<!-- LEVEL_START -->')
                    modified_lines.append('')
                    modified_lines.append(line)
                    changes_made += 1
        else:
            # Not a level header, just add the line
            modified_lines.append(line)
    
    return '\n'.join(modified_lines), changes_made

def process_file(file_path):
    """
    Process a single markdown file.
    
    Args:
        file_path (str): Path to the markdown file
    
    Returns:
        tuple: (file_modified, changes_made)
    """
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if file has Level patterns
    if not re.search(r'^# Level \d+', content, re.MULTILINE):
        return False, 0
    
    # Add level markers
    modified_content, changes_made = add_level_markers(content)
    
    # Check if content actually changed
    if modified_content == content:
        return False, 0
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(modified_content)
    
    return True, changes_made

def process_directory(directory_path):
    """
    Process all markdown files in a directory.
    
    Args:
        directory_path (str): Path to the directory
    
    Returns:
        tuple: (files_processed, files_modified, total_changes)
    """
    
    files_processed = 0
    files_modified = 0
    total_changes = 0
    
    # Find all markdown files
    for file_path in Path(directory_path).glob('*.md'):
        files_processed += 1
        
        modified, changes = process_file(str(file_path))
        if modified:
            files_modified += 1
            total_changes += changes
            print(f"✅ Modified: {file_path.name} ({changes} markers added)")
        else:
            print(f"⏭️  Skipped: {file_path.name} (no Level patterns or already marked)")
    
    return files_processed, files_modified, total_changes

def main():
    # Get command line arguments
    if len(sys.argv) < 2:
        print("❌ Error: Please provide a target file or directory")
        print("Usage: python3 add-level-markers.py [target]")
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
            modified, changes = process_file(target)
            if modified:
                print(f"✅ Modified: {os.path.basename(target)} ({changes} markers added)")
            else:
                print(f"⏭️  Skipped: {os.path.basename(target)} (no Level patterns or already marked)")
            
            files_processed = 1
            files_modified = 1 if modified else 0
            total_changes = changes
            
        elif os.path.isdir(target):
            # Process directory
            files_processed, files_modified, total_changes = process_directory(target)
            
        else:
            print(f"❌ Error: '{target}' is neither a file nor a directory")
            sys.exit(1)
        
        print(f"\n🎉 Processing Complete!")
        print(f"📊 Processed {files_processed} files, modified {files_modified} files")
        print(f"🔢 Total level markers added: {total_changes}")
        
    except Exception as e:
        print(f"❌ Error processing target: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
