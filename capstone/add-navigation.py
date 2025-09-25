#!/usr/bin/env python3
"""
Add Navigation Script
====================

This script adds navigation links between capstone levels.
It creates a navigation bar at the top of each level file showing:
- Current level (highlighted)
- Links to all other levels

Usage:
    python3 add-navigation.py [levels_dir]

If no argument provided, uses: capstone/capstone-levels/
"""

import os
import re
import sys
from pathlib import Path

def extract_level_number(filename):
    """Extract level number from filename like 'capstone-lv-5.md'"""
    match = re.search(r'capstone-lv-(\d+)\.md', filename)
    return int(match.group(1)) if match else 0

def create_navigation_html(total_levels, current_level):
    """
    Create navigation HTML for the current level.
    
    Args:
        total_levels (int): Total number of levels
        current_level (int): Current level number (1-based)
    
    Returns:
        str: Navigation HTML
    """
    
    nav_parts = []
    
    for level_num in range(1, total_levels + 1):
        filename = f"capstone-lv-{level_num}.md"
        
        if level_num == current_level:
            # Current level - bold and highlighted
            nav_parts.append(f"**{level_num}**")
        else:
            # Other levels - linked
            nav_parts.append(f"[{level_num}](./{filename})")
    
    nav_line = "Level Navigation: " + " | ".join(nav_parts)
    return nav_line

def add_navigation_to_file(file_path, total_levels):
    """
    Add navigation to a single level file.
    
    Args:
        file_path (str): Path to the level file
        total_levels (int): Total number of levels
    """
    
    current_level = extract_level_number(os.path.basename(file_path))
    if current_level == 0:
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation already exists
    if "Level Navigation:" in content:
        return False
    
    # Create navigation
    navigation = create_navigation_html(total_levels, current_level)
    
    # Add navigation at the beginning of the file
    new_content = navigation + "\n\n" + content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    # Default levels directory
    default_levels_dir = "capstone/capstone-levels"
    
    # Get command line argument
    levels_dir = sys.argv[1] if len(sys.argv) > 1 else default_levels_dir
    
    # Validate directory exists
    if not os.path.exists(levels_dir):
        print(f"❌ Error: Levels directory '{levels_dir}' not found")
        sys.exit(1)
    
    # Find all capstone level files
    level_files = []
    for file in os.listdir(levels_dir):
        if file.startswith('capstone-lv-') and file.endswith('.md'):
            level_files.append(os.path.join(levels_dir, file))
    
    if not level_files:
        print(f"❌ Error: No capstone level files found in '{levels_dir}'")
        sys.exit(1)
    
    # Sort files by level number
    level_files.sort(key=lambda x: extract_level_number(os.path.basename(x)))
    
    total_levels = len(level_files)
    print(f"📁 Processing {total_levels} level files in {levels_dir}")
    print()
    
    modified_count = 0
    
    for file_path in level_files:
        filename = os.path.basename(file_path)
        current_level = extract_level_number(filename)
        
        if add_navigation_to_file(file_path, total_levels):
            print(f"✅ Added navigation to: {filename}")
            modified_count += 1
        else:
            print(f"⏭️  Skipped {filename} (navigation already exists)")
    
    print(f"\n🎉 Successfully added navigation to {modified_count} files")

if __name__ == "__main__":
    main()
