#!/usr/bin/env python3
"""
Split Capstone Guide Script
==========================

This script splits the capstone-guide-all-todo.md file into individual level files.
Each level is extracted based on LEVEL_START markers (no LEVEL_END needed).

Usage:
    python3 split-capstone-levels.py [input_file] [output_dir]

If no arguments provided, uses:
    - Input: capstone/capstone-guide-all-todo.md
    - Output: capstone/capstone-levels/
"""

import os
import re
import sys
from pathlib import Path

def extract_levels_from_file(input_file, output_dir):
    """
    Extract individual levels from the concatenated capstone guide.
    
    Args:
        input_file (str): Path to the input file
        output_dir (str): Path to the output directory
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
        level_match = re.search(r'# Level (\d+):', level_content)
        if not level_match:
            print(f"⚠️  Skipping block - no level number found")
            continue
            
        level_num = level_match.group(1)
        filename = f"capstone-lv-{level_num}.md"
        
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
    # Default paths
    default_input = "capstone/capstone-guide-all-todo.md"
    default_output = "capstone/capstone-levels"
    
    # Get command line arguments
    input_file = sys.argv[1] if len(sys.argv) > 1 else default_input
    output_dir = sys.argv[2] if len(sys.argv) > 2 else default_output
    
    # Validate input file exists
    if not os.path.exists(input_file):
        print(f"❌ Error: Input file '{input_file}' not found")
        sys.exit(1)
    
    print(f"📖 Reading from: {input_file}")
    print(f"📁 Writing to: {output_dir}")
    print()
    
    try:
        levels_count = extract_levels_from_file(input_file, output_dir)
        
        if levels_count == 0:
            print("⚠️  No levels found. Check that the input file contains LEVEL_START markers.")
            sys.exit(1)
            
    except Exception as e:
        print(f"❌ Error processing file: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()
