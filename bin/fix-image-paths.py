#!/usr/bin/env python3
"""
Fix image paths in level files
=============================

This script fixes image paths in level files that are in subdirectories.
Changes './docs/' to '../docs/' to properly reference images from subdirectories.
"""

import os
import sys
import re

def fix_image_paths(directory):
    """Fix image paths in all markdown files in the given directory."""
    
    if not os.path.exists(directory):
        print(f"❌ Directory '{directory}' not found")
        return False
    
    files_processed = 0
    files_modified = 0
    
    # Process all .md files in the directory
    for filename in os.listdir(directory):
        if filename.endswith('.md'):
            filepath = os.path.join(directory, filename)
            files_processed += 1
            
            # Read the file
            with open(filepath, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Fix image paths: './docs/' -> '../docs/'
            original_content = content
            content = re.sub(r'src="\./docs/', 'src="../docs/', content)
            
            # Check if content changed
            if content != original_content:
                # Write the modified content back
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                files_modified += 1
                print(f"✅ Fixed: {filename}")
            else:
                print(f"⏭️  Skipped: {filename} (no image paths to fix)")
    
    print(f"\n🎉 Image path fixing complete!")
    print(f"📊 Processed {files_processed} files, modified {files_modified} files")
    return True

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fix-image-paths.py <directory>")
        print("Example: python3 fix-image-paths.py db-levels")
        sys.exit(1)
    
    directory = sys.argv[1]
    fix_image_paths(directory)

if __name__ == "__main__":
    main()
