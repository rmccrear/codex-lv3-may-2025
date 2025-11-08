# Project Guide Processing Scripts

This directory contains general-purpose scripts to convert concatenated project guide files into individual level files with enhanced features. These scripts can be used for any project (capstone, mad-libs, etc.) that uses `LEVEL_START` markers.

## 🚀 Quick Start

To process any project guide in one command:

```bash
./bin/process-project-guide.sh [input_file] [output_dir] [project_name]
```

**Examples:**
```bash
# Capstone project
./bin/process-project-guide.sh capstone/capstone-guide-all-todo.md capstone/capstone-levels capstone

# Mad Libs project
./bin/process-project-guide.sh mad-libs-guide-all.md mad-libs/mad-libs-levels mad-libs

# Use defaults (capstone)
./bin/process-project-guide.sh
```

## 📁 Script Overview

### Main Orchestration Script
- **`process-project-guide.sh`** - Main script that runs the entire pipeline for any project

### Individual Processing Scripts
- **`bin/split-project-levels.py`** - Splits concatenated guide into individual level files
- **`bin/add-project-navigation.py`** - Adds navigation links between levels
- **`bin/convert-show-me.py`** - Converts "Show Me" sections (markers or `<details>` blocks) into HTML-friendly collapsible details

### Legacy Scripts (Project-Specific)
- **`capstone/split-capstone-levels.py`** - Capstone-specific version (legacy)
- **`capstone/add-navigation.py`** - Capstone-specific version (legacy)
- **`capstone/process-capstone-guide.sh`** - Capstone-specific version (legacy)

## 🔧 Individual Script Usage

### 1. Split Levels
```bash
python3 bin/split-project-levels.py [input_file] [output_dir] [project_name]
```

**Examples:**
```bash
# Capstone project
python3 bin/split-project-levels.py capstone/capstone-guide-all-todo.md capstone/capstone-levels capstone

# Mad Libs project
python3 bin/split-project-levels.py mad-libs-guide-all.md mad-libs/mad-libs-levels mad-libs

# Use defaults
python3 bin/split-project-levels.py
```

### 2. Add Navigation
```bash
python3 bin/add-project-navigation.py [levels_dir] [project_name]
```

**Examples:**
```bash
# Capstone project
python3 bin/add-project-navigation.py capstone/capstone-levels capstone

# Mad Libs project
python3 bin/add-project-navigation.py mad-libs/mad-libs-levels mad-libs

# Use defaults
python3 bin/add-project-navigation.py
```

### 3. Convert Show Me Sections
```bash
python3 bin/convert-show-me.py [target]
```

**Examples:**
```bash
# Process all files in directory
python3 bin/convert-show-me.py mad-libs/mad-libs-levels

# Process specific file
python3 bin/convert-show-me.py mad-libs/mad-libs-levels/mad-libs-lv-1.md
```

## 📋 Input Format Requirements

The input file must contain levels marked with:

```markdown
<!-- LEVEL_START -->

# Level 1: Project Planning & Setup
[Level content here...]

<!-- LEVEL_START -->

# Level 2: Basic Input Handling
[Level content here...]
```

**Key Points:**
- Only `LEVEL_START` markers are needed (no `LEVEL_END`)
- Each level must have a header like `# Level X: Title`
- Levels are automatically separated by the next `LEVEL_START` marker

## 🎯 Output Features

### Individual Level Files
- Each level becomes a separate `.md` file
- Files are named `{project_name}-lv-X.md` (e.g., `capstone-lv-1.md`, `mad-libs-lv-3.md`)
- Content is cleaned and formatted

### Navigation
Each level file gets a navigation bar at the top:
```markdown
Level Navigation: **1** | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | ...
```

### Collapsible Show Me Sections
"Show Me" sections are converted to HTML details (supports both the original `Show Me:` markers and pre-existing `<details><summary>Show Me</summary>` blocks):

**Before:**
```markdown
Show Me: the HTML code

```html
<div>Hello World</div>
```
```

**After:**
```html
<details>
<summary>Show Me: the HTML code</summary>

<pre><code class="language-html">&lt;div&gt;Hello World&lt;/div&gt;</code></pre>
</details>
```

## 🛠️ Technical Details

### Dependencies
- Python 3.6+
- Bash shell
- No external Python packages required (uses only standard library)

### File Naming Convention
- **Capstone:** `capstone-lv-1.md`, `capstone-lv-2.md`, etc.
- **Mad Libs:** `mad-libs-lv-1.md`, `mad-libs-lv-2.md`, etc.
- **Any Project:** `{project_name}-lv-{number}.md`

### Project Structure Examples
```
# Capstone Project
capstone/
├── capstone-guide-all-todo.md     # Input file
├── capstone-levels/               # Output directory
│   ├── capstone-lv-1.md
│   ├── capstone-lv-2.md
│   └── ...

# Mad Libs Project
mad-libs/
├── mad-libs-guide-all.md          # Input file
├── mad-libs-levels/               # Output directory
│   ├── mad-libs-lv-1.md
│   ├── mad-libs-lv-2.md
│   └── ...
```

## 🔍 Troubleshooting

### Common Issues

1. **"No levels found"**
   - Check that input file contains `LEVEL_START` markers
   - Verify the markers follow the exact format: `<!-- LEVEL_START -->`

2. **"No {project_name} level files found"**
   - Ensure the output directory contains files matching `{project_name}-lv-*.md`
   - Check that the split script ran successfully first
   - Verify the project name parameter is correct

3. **"Navigation already exists"**
   - This is normal - the script skips files that already have navigation
   - To force regeneration, manually remove navigation lines from files

### Debug Mode
Add `set -x` to the beginning of `process-project-guide.sh` to see detailed execution:

```bash
#!/bin/bash
set -x  # Add this line for debug output
# ... rest of script
```

## 📝 Usage Examples

### Creating a New Project Guide

1. **Create your concatenated guide:**
   ```markdown
   # My Project Guide
   
   <!-- LEVEL_START -->
   
   # Level 1: Getting Started
   [Content here...]
   
   <!-- LEVEL_START -->
   
   # Level 2: Basic Features
   [Content here...]
   ```

2. **Process it:**
   ```bash
   ./process-project-guide.sh my-project-guide.md my-project/levels my-project
   ```

3. **Result:**
   ```
   my-project/levels/
   ├── my-project-lv-1.md
   ├── my-project-lv-2.md
   └── ...
   ```

### Batch Processing Multiple Projects

```bash
# Process all projects
./process-project-guide.sh capstone/capstone-guide-all-todo.md capstone/capstone-levels capstone
./process-project-guide.sh mad-libs/mad-libs-guide-all.md mad-libs/mad-libs-levels mad-libs
./process-project-guide.sh my-project/my-project-guide.md my-project/my-project-levels my-project
```

## 🤝 Contributing

When modifying these scripts:

1. Test with different project types
2. Create backups before running on full datasets
3. Update this README if adding new features
4. Maintain backward compatibility where possible
5. Consider both capstone and mad-libs use cases

## 🎯 Benefits of General Scripts

- **Reusable** across different project types
- **Consistent** file naming and navigation
- **Maintainable** single codebase for all projects
- **Flexible** parameter-driven configuration
- **Scalable** easy to add new project types
