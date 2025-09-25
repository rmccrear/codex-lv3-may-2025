# Capstone Guide Processing Scripts

This directory contains scripts to convert the concatenated `capstone-guide-all-todo.md` file into individual level files with enhanced features.

## 🚀 Quick Start

To process the entire capstone guide in one command:

```bash
./process-capstone-guide.sh
```

This will:
1. Split the concatenated guide into individual level files
2. Add navigation between levels
3. Convert "Show Me" sections to collapsible details

## 📁 Script Overview

### Main Orchestration Script
- **`process-capstone-guide.sh`** - Main script that runs the entire pipeline

### Individual Processing Scripts
- **`split-capstone-levels.py`** - Splits concatenated guide into individual level files
- **`add-navigation.py`** - Adds navigation links between levels
- **`convert-show-me.py`** - Converts "Show Me" sections to collapsible HTML details

### Legacy Scripts
- **`renumber-levels.sh`** - Renumbers levels sequentially (legacy)
- **`replace-show-me.py`** - Alternative Show Me converter (legacy)

## 🔧 Individual Script Usage

### 1. Split Levels
```bash
python3 split-capstone-levels.py [input_file] [output_dir]
```

**Examples:**
```bash
# Use defaults
python3 split-capstone-levels.py

# Specify custom paths
python3 split-capstone-levels.py capstone/capstone-guide-all-todo.md capstone/capstone-levels/
```

### 2. Add Navigation
```bash
python3 add-navigation.py [levels_dir]
```

**Examples:**
```bash
# Use default directory
python3 add-navigation.py

# Specify custom directory
python3 add-navigation.py capstone/capstone-levels/
```

### 3. Convert Show Me Sections
```bash
python3 convert-show-me.py [target]
```

**Examples:**
```bash
# Process all files in default directory
python3 convert-show-me.py

# Process specific file
python3 convert-show-me.py capstone/capstone-levels/capstone-lv-1.md

# Process custom directory
python3 convert-show-me.py my-levels/
```

## 📋 Input Format Requirements

The input file (`capstone-guide-all-todo.md`) must contain levels marked with:

```markdown
<!-- LEVEL_START: capstone-lv-1.md -->
[Level content here]
<!-- LEVEL_END: capstone-lv-1.md -->
```

## 🎯 Output Features

### Individual Level Files
- Each level becomes a separate `.md` file
- Files are named `capstone-lv-X.md` where X is the level number
- Content is cleaned and formatted

### Navigation
Each level file gets a navigation bar at the top:
```markdown
Level Navigation: **1** | [2](./capstone-lv-2.md) | [3](./capstone-lv-3.md) | ...
```

### Collapsible Show Me Sections
"Show Me" sections are converted to HTML details:

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

### File Structure
```
capstone/
├── capstone-guide-all-todo.md     # Input file
├── capstone-levels/               # Output directory
│   ├── capstone-lv-1.md
│   ├── capstone-lv-2.md
│   └── ...
├── process-capstone-guide.sh      # Main script
├── split-capstone-levels.py       # Level splitter
├── add-navigation.py              # Navigation adder
├── convert-show-me.py             # Show Me converter
└── README-SCRIPTS.md              # This file
```

### Error Handling
- Scripts exit with error codes on failure
- Backup files are created before modifications
- Input validation checks file existence and format

## 🔍 Troubleshooting

### Common Issues

1. **"No levels found"**
   - Check that input file contains `LEVEL_START` and `LEVEL_END` markers
   - Verify the markers follow the exact format: `<!-- LEVEL_START: capstone-lv-X.md -->`

2. **"Navigation already exists"**
   - This is normal - the script skips files that already have navigation
   - To force regeneration, manually remove navigation lines from files

3. **"No markdown files found"**
   - Ensure the output directory contains `.md` files
   - Check that the split script ran successfully first

### Debug Mode
Add `set -x` to the beginning of `process-capstone-guide.sh` to see detailed execution:

```bash
#!/bin/bash
set -x  # Add this line for debug output
# ... rest of script
```

## 📝 Customization

### Adding New Features
Each script is modular and can be extended:

1. **New transformations**: Add new Python scripts following the same pattern
2. **Different output formats**: Modify the individual scripts
3. **Custom navigation**: Edit `add-navigation.py` to change navigation format

### Integration with Other Tools
The scripts can be integrated into:
- CI/CD pipelines
- Git hooks
- Build systems
- Documentation generators

## 🤝 Contributing

When modifying these scripts:

1. Test with a small subset of levels first
2. Create backups before running on full dataset
3. Update this README if adding new features
4. Maintain backward compatibility where possible
