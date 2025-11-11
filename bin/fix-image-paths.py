#!/usr/bin/env python3
"""
Adjust relative URLs in generated level files
=============================================

When level files are generated in a deeper directory, any relative URLs
need an additional "../" prefix to continue pointing at the same targets.
This script scans markdown files for relative links or sources and adds
one extra parent-directory segment while preserving fragments and queries.
"""

import os
import re
import sys
import posixpath
from urllib.parse import urlparse, urlunparse

RELATIVE_SCHEMES_SKIP = {"http", "https", "mailto", "tel", "data", "javascript"}


def is_relative_url(url: str) -> bool:
    """Return True if the URL is a relative reference that should be adjusted."""
    if not url:
        return False
    if url.startswith("#") or url.startswith("//") or url.startswith("/"):
        return False

    parsed = urlparse(url)
    if parsed.scheme and parsed.scheme.lower() in RELATIVE_SCHEMES_SKIP:
        return False

    # Treat anything without a network location as relative (e.g. ../foo, docs/bar)
    return parsed.netloc == ""


def add_parent_directory(url: str) -> str:
    """Prefix the URL path with one additional '../', preserving fragments and queries."""
    parsed = urlparse(url)
    path = parsed.path or ""

    if not path:
        return url

    # Join with '..' and normalise to collapse any ./ segments
    new_path = posixpath.normpath(posixpath.join("..", path))

    # Restore trailing slash if original path ended with '/'
    if path.endswith("/") and not new_path.endswith("/"):
        new_path += "/"

    updated = parsed._replace(path=new_path)
    return urlunparse(updated)


MARKDOWN_LINK_RE = re.compile(r"(!?\[[^\]]+\])\(([^)\s]+)\)")
HTML_ATTR_RE = re.compile(r'(href|src)="([^"]+)"')


def adjust_relative_urls(directory: str) -> bool:
    """Adjust relative URLs in all markdown files within the given directory."""
    if not os.path.exists(directory):
        print(f"❌ Directory '{directory}' not found")
        return False

    files_processed = 0
    files_modified = 0

    for filename in os.listdir(directory):
        if not filename.endswith(".md"):
            continue

        filepath = os.path.join(directory, filename)
        files_processed += 1

        with open(filepath, "r", encoding="utf-8") as f:
            content = f.read()

        original_content = content

        def replace_markdown(match):
            label = match.group(1)
            url = match.group(2).strip()
            if not is_relative_url(url):
                return match.group(0)
            return f"{label}({add_parent_directory(url)})"

        def replace_html(match):
            attr = match.group(1)
            url = match.group(2).strip()
            if not is_relative_url(url):
                return match.group(0)
            return f'{attr}="{add_parent_directory(url)}"'

        content = MARKDOWN_LINK_RE.sub(replace_markdown, content)
        content = HTML_ATTR_RE.sub(replace_html, content)

        if content != original_content:
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(content)
            files_modified += 1
            print(f"✅ Updated: {filename}")
        else:
            print(f"⏭️  Skipped: {filename} (no relative URLs to adjust)")

    print("\n🎉 Relative URL adjustment complete!")
    print(f"📊 Processed {files_processed} files, modified {files_modified} files")
    return True


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 fix-image-paths.py <directory>")
        print("Example: python3 fix-image-paths.py vitest-levels")
        sys.exit(1)

    directory = sys.argv[1]
    adjust_relative_urls(directory)


if __name__ == "__main__":
    main()
