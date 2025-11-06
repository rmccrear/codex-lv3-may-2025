#!/usr/bin/env python3
"""
Split Project Levels Script
===========================

This script splits concatenated project guide files into individual level files.
It can be used for any project (capstone, mad-libs, etc.) that uses LEVEL_START markers.

Usage:
    python3 split-project-levels.py [input_file] [output_dir] [project_name]

Arguments:
    input_file    - Path to the concatenated guide file
    output_dir    - Directory to write individual level files
    project_name  - Project name (e.g., 'capstone', 'mad-libs') for file naming

Examples:
    # Capstone project
    python3 split-project-levels.py capstone/capstone-guide-all-todo.md capstone/capstone-levels capstone
    
    # Mad Libs project  
    python3 split-project-levels.py mad-libs-guide-all.md mad-libs/mad-libs-levels mad-libs
    
    # Use defaults (capstone)
    python3 split-project-levels.py
"""

import os
import re
import sys
from pathlib import Path

def extract_levels_from_file(input_file, output_dir, project_name="capstone"):
    """
    Extract individual levels from a concatenated project guide.
    
    Args:
        input_file (str): Path to the input file
        output_dir (str): Path to the output directory
        project_name (str): Project name for file naming
    
    Returns:
        int: Number of levels extracted
    """
    
    # Ensure output directory exists
    Path(output_dir).mkdir(parents=True, exist_ok=True)
    
    # Read the input file
    with open(input_file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Pattern to match level blocks
    # Matches: <!-- LEVEL_START --> ... content ... (until next LEVEL_START or end of file)
    pattern = r'<!-- LEVEL_START -->(.*?)(?=<!-- LEVEL_START -->|$)'
    
    levels_found = 0
    
    for match in re.finditer(pattern, content, re.DOTALL):
        level_content = match.group(1).strip()
        
        # Extract level number from the content
        # Match "Level X:" or "Level X (Challenge):" patterns
        level_match = re.search(r'# Level (\d+)(?:\s*\([^)]+\))?:', level_content)
        if not level_match:
            print(f"⚠️  Skipping block - no level number found")
            continue
            
        level_num = level_match.group(1)
        filename = f"{project_name}-lv-{level_num}.md"
        
        # Clean up the content
        # Remove leading/trailing whitespace and empty lines
        level_content = level_content.strip()
        
        # Remove the initial separator line if present
        if level_content.startswith('---\n'):
            level_content = level_content[4:]
        
        # Write the level file
        output_path = os.path.join(output_dir, filename)
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(level_content)
        
        levels_found += 1
        print(f"Created: {filename}")
    
    print(f"\n✅ Successfully extracted {levels_found} levels to {output_dir}")
    return levels_found

def main():
    # Default paths for capstone project
    default_input = "capstone/capstone-guide-all-todo.md"
    default_output = "capstone/capstone-levels"
    default_project = "capstone"
    
    # Get command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_dir = sys.argv[2] if len(sys.argv) > 2 else default_output
    project_name = sys.argv[3] if len(sys.argv) > 3 else default_project
    
    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    print(f"📖 Reading from: {input_file}")
    print(f"📁 Writing to: {output_dir}")
    print(f"🏷️  Project: {project_name}")
    print()
    
    try:
        levels_count = extract_levels_from_file(input_file, output_dir, project_name)
        
        if levels_count == 0:
            print("⚠️  No levels found. Check that the input file contains LEVEL_START markers.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
