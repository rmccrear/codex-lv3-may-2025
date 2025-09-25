#!/usr/bin/env python3
"""
Add Project Navigation Script
==============================

This script adds navigation links between project level files.
It can be used for any project (capstone, mad-libs, etc.) with level files.

Usage:
    python3 add-project-navigation.py [levels_dir] [project_name]

Arguments:
    levels_dir    - Directory containing level files
    project_name  - Project name (e.g., 'capstone', 'mad-libs') for file pattern matching

Examples:
    # Capstone project
    python3 add-project-navigation.py capstone/capstone-levels capstone
    
    # Mad Libs project
    python3 add-project-navigation.py mad-libs/mad-libs-levels mad-libs
    
    # Use defaults (capstone)
    python3 add-project-navigation.py
"""

import os
import re
import sys
from pathlib import Path

def extract_level_number(filename, project_name="capstone"):
    """Extract level number from filename like 'capstone-lv-5.md' or 'mad-libs-lv-3.md'"""
    pattern = f'{project_name}-lv-(\\d+)\\.md'
    match = re.search(pattern, filename)
    return int(match.group(1)) if match else 0

def create_navigation_html(total_levels, current_level, project_name="capstone", challenge_levels=None):
    """
    Create navigation HTML for the current level.
    
    Args:
        total_levels (int): Total number of levels
        current_level (int): Current level number (1-based)
        project_name (str): Project name for file naming
        challenge_levels (set): Set of level numbers that are challenge levels
    
    Returns:
        str: Navigation HTML
    """
    
    if challenge_levels is None:
        challenge_levels = set()
    
    nav_parts = []
    
    for level_num in range(1, total_levels + 1):
        filename = f"{project_name}-lv-{level_num}.md"
        
        # Check if this is a challenge level
        is_challenge = level_num in challenge_levels
        challenge_icon = "⚡" if is_challenge else ""
        
        if level_num == current_level:
            # Current level - bold and highlighted
            nav_parts.append(f"**{level_num}{challenge_icon}**")
        else:
            # Other levels - linked
            nav_parts.append(f"[{level_num}{challenge_icon}](./{filename})")
    
    nav_line = "Level Navigation: " + " | ".join(nav_parts)
    return nav_line

def detect_challenge_levels(level_files, project_name="capstone"):
    """
    Detect which levels are challenge levels by reading their titles.
    
    Args:
        level_files (list): List of level file paths
        project_name (str): Project name for file pattern matching
    
    Returns:
        set: Set of level numbers that are challenge levels
    """
    challenge_levels = set()
    
    for file_path in level_files:
        level_num = extract_level_number(os.path.basename(file_path), project_name)
        if level_num == 0:
            continue
            
        # Read the file to check for challenge level indicators
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Check if the title contains "CHALLENGE LEVEL"
        if "CHALLENGE LEVEL" in content:
            challenge_levels.add(level_num)
    
    return challenge_levels

def add_navigation_to_file(file_path, total_levels, project_name="capstone", challenge_levels=None):
    """
    Add navigation to a single level file.
    
    Args:
        file_path (str): Path to the level file
        total_levels (int): Total number of levels
        project_name (str): Project name for file pattern matching
        challenge_levels (set): Set of level numbers that are challenge levels
    
    Returns:
        bool: True if file was modified, False if skipped
    """
    
    if challenge_levels is None:
        challenge_levels = set()
    
    current_level = extract_level_number(os.path.basename(file_path), project_name)
    if current_level == 0:
        return False
    
    # Read the file
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Check if navigation already exists
    if "Level Navigation:" in content:
        return False
    
    # Create navigation
    navigation = create_navigation_html(total_levels, current_level, project_name, challenge_levels)
    
    # Add navigation at the beginning of the file
    new_content = navigation + "\n\n" + content
    
    # Write back to file
    with open(file_path, 'w', encoding='utf-8') as f:
        f.write(new_content)
    
    return True

def main():
    # Default paths for capstone project
    default_levels_dir = "capstone/capstone-levels"
    default_project = "capstone"
    
    # Get command line arguments
    levels_dir = sys.argv[1] if len(sys.argv) > 1 else default_levels_dir
    project_name = sys.argv[2] if len(sys.argv) > 2 else default_project
    
    # Validate directory exists
    if not os.path.exists(levels_dir):
        print(f"❌ Error: Levels directory '{levels_dir}' not found")
        sys.exit(1)
    
    # Find all project level files
    level_files = []
    for file in os.listdir(levels_dir):
        if file.startswith(f'{project_name}-lv-') and file.endswith('.md'):
            level_files.append(os.path.join(levels_dir, file))
    
    if not level_files:
        print(f"❌ Error: No {project_name} level files found in '{levels_dir}'")
        print(f"   Looking for files matching pattern: {project_name}-lv-*.md")
        sys.exit(1)
    
    # Sort files by level number
    level_files.sort(key=lambda x: extract_level_number(os.path.basename(x), project_name))
    
    total_levels = len(level_files)
    print(f"📁 Processing {total_levels} {project_name} level files in {levels_dir}")
    
    # Detect challenge levels
    challenge_levels = detect_challenge_levels(level_files, project_name)
    if challenge_levels:
        challenge_list = sorted(list(challenge_levels))
        print(f"⚡ Detected challenge levels: {', '.join(map(str, challenge_list))}")
    else:
        print("📝 No challenge levels detected")
    print()
    
    modified_count = 0
    
    for file_path in level_files:
        filename = os.path.basename(file_path)
        current_level = extract_level_number(filename, project_name)
        
        if add_navigation_to_file(file_path, total_levels, project_name, challenge_levels):
            print(f"✅ Added navigation to: {filename}")
            modified_count += 1
        else:
            print(f"⏭️  Skipped {filename} (navigation already exists)")
    
    print(f"\n🎉 Successfully added navigation to {modified_count} files")

if __name__ == "__main__":
    main()
