#!/usr/bin/env python3
"""
Deep Link Validator for Markdown Files

This script validates that all deep links (anchors) in markdown files
actually exist in their target files. It checks:
1. Internal links to other markdown files
2. Anchor links within the same file
3. External links (skips validation)

Usage: python3 bin/validate-deep-links.py [file_or_directory]
"""

import os
import re
import sys
from pathlib import Path
from urllib.parse import urlparse

def extract_anchors_from_markdown(content):
    """Extract all anchor IDs from markdown content."""
    anchors = set()
    
    # Headers create anchors (GitHub Pages style)
    header_pattern = r'^#{1,6}\s+(.+)$'
    for line in content.split('\n'):
        match = re.match(header_pattern, line)
        if match:
            header_text = match.group(1).strip()
            # Convert to GitHub Pages anchor format
            anchor = re.sub(r'[^\w\s-]', '', header_text.lower())
            anchor = re.sub(r'[-\s]+', '-', anchor)
            anchors.add(anchor)
    
    # Manual anchor definitions
    manual_pattern = r'<a\s+id="([^"]+)"'
    for match in re.finditer(manual_pattern, content):
        anchors.add(match.group(1))
    
    return anchors

def extract_links_from_markdown(content, file_path):
    """Extract all links from markdown content."""
    links = []
    
    # Markdown link pattern: [text](url)
    link_pattern = r'\[([^\]]+)\]\(([^)]+)\)'
    for match in re.finditer(link_pattern, content):
        text = match.group(1)
        url = match.group(2)
        
        # Skip external links
        if url.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
            
        # Handle relative paths
        if url.startswith('./'):
            url = url[2:]
        elif not url.startswith('/'):
            # Relative to current file
            current_dir = os.path.dirname(file_path)
            url = os.path.join(current_dir, url)
        
        # Normalize path
        url = os.path.normpath(url)
        
        links.append({
            'text': text,
            'url': url,
            'line': content[:match.start()].count('\n') + 1
        })
    
    return links

def validate_file(file_path):
    """Validate deep links in a single markdown file."""
    print(f"\n🔍 Validating: {file_path}")
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
    except Exception as e:
        print(f"❌ Error reading file: {e}")
        return False
    
    links = extract_links_from_markdown(content, file_path)
    
    if not links:
        print("✅ No internal links found")
        return True
    
    all_valid = True
    
    for link in links:
        url = link['url']
        line = link['line']
        
        # Check if target file exists
        if '#' in url:
            file_part, anchor_part = url.split('#', 1)
        else:
            file_part = url
            anchor_part = None
        
        # Add .md extension if not present
        if not file_part.endswith('.md') and not file_part.endswith('.html'):
            file_part += '.md'
        
        # Check if file exists
        if not os.path.exists(file_part):
            print(f"❌ Line {line}: File not found: {file_part}")
            all_valid = False
            continue
        
        # If there's an anchor, check if it exists
        if anchor_part:
            try:
                with open(file_part, 'r', encoding='utf-8') as f:
                    target_content = f.read()
                
                anchors = extract_anchors_from_markdown(target_content)
                
                if anchor_part not in anchors:
                    print(f"❌ Line {line}: Anchor '#{anchor_part}' not found in {file_part}")
                    print(f"   Available anchors: {', '.join(sorted(anchors))}")
                    all_valid = False
                else:
                    print(f"✅ Line {line}: {url}")
            except Exception as e:
                print(f"❌ Line {line}: Error reading target file {file_part}: {e}")
                all_valid = False
        else:
            print(f"✅ Line {line}: {url}")
    
    return all_valid

def validate_directory(directory):
    """Validate deep links in all markdown files in a directory."""
    print(f"🔍 Validating directory: {directory}")
    
    all_valid = True
    md_files = []
    
    # Find all markdown files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file.endswith('.md'):
                md_files.append(os.path.join(root, file))
    
    if not md_files:
        print("❌ No markdown files found")
        return False
    
    print(f"📁 Found {len(md_files)} markdown files")
    
    for file_path in md_files:
        if not validate_file(file_path):
            all_valid = False
    
    return all_valid

def main():
    """Main function."""
    if len(sys.argv) != 2:
        print("Usage: python3 bin/validate-deep-links.py <file_or_directory>")
        print("\nExamples:")
        print("  python3 bin/validate-deep-links.py README.md")
        print("  python3 bin/validate-deep-links.py week5/")
        print("  python3 bin/validate-deep-links.py .")
        sys.exit(1)
    
    target = sys.argv[1]
    
    if not os.path.exists(target):
        print(f"❌ Path not found: {target}")
        sys.exit(1)
    
    print("🔗 Deep Link Validator")
    print("=" * 50)
    
    if os.path.isfile(target):
        success = validate_file(target)
    elif os.path.isdir(target):
        success = validate_directory(target)
    else:
        print(f"❌ Invalid path type: {target}")
        sys.exit(1)
    
    print("\n" + "=" * 50)
    if success:
        print("🎉 All deep links are valid!")
        sys.exit(0)
    else:
        print("❌ Some deep links are invalid!")
        sys.exit(1)

if __name__ == "__main__":
    main()
