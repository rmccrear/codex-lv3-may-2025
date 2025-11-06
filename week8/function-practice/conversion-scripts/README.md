# Conversion Scripts

Scripts to convert Vitest guide files into a project guide format.

## Usage

Run the main conversion script:

```bash
node conversion-scripts/convert-to-project-guide.js
```

Or from the `function-practice` directory:

```bash
node ./conversion-scripts/convert-to-project-guide.js
```

## What It Does

1. **Automatically discovers** source files matching pattern `##-vitest-*-guide.md`:
   - Files are sorted by numeric prefix (e.g., `01-vitest-intro-guide.md`, `02-vitest-add-tests-guide.md`)
   - Currently includes:
     - `01-vitest-intro-guide.md`
     - `02-vitest-add-tests-guide.md`
     - `03-vitest-red-green-guide.md`
     - `04-vitest-challenges-guide.md`

2. **Adds markers** to each file:
   - `<!-- LEVEL_START -->` at the beginning
   - `<!-- LEVEL_START -->` before each `##` header (replacing `---`)
   - `<!-- INFORMATIVE_ONLY -->` for headers that don't contain "Step"

3. **Creates intermediary files** (temporarily, for debugging):
   - `01-vitest-intro-guide-marked.md`
   - `02-vitest-add-tests-guide-marked.md`
   - `03-vitest-red-green-guide-marked.md`
   - `04-vitest-challenges-guide-marked.md`
   - These are automatically cleaned up after conversion

4. **Extracts levels** from each file

5. **Renumbers levels** sequentially across all files:
   - Converts "Step X" to "Level X"
   - Maintains sequential numbering

6. **Concatenates** all levels into:
   - `vitest-project-guide.md`

## Output Files

- **vitest-project-guide.md** - Final concatenated project guide

## Options

- **`--keep-intermediary` or `-k`** - Keep the intermediary `*-marked.md` files for debugging
  ```bash
  node conversion-scripts/convert-to-project-guide.js --keep-intermediary
  ```

By default, intermediary files are automatically cleaned up after conversion.

## File Naming Convention

Source files must follow the pattern: `##-vitest-*-guide.md` where `##` is a two-digit number indicating the order.

Examples:
- `01-vitest-intro-guide.md` - First file
- `02-vitest-add-tests-guide.md` - Second file
- `03-vitest-red-green-guide.md` - Third file
- `04-vitest-challenges-guide.md` - Fourth file

The script automatically discovers and sorts files by their numeric prefix.

## Requirements

- Node.js (no external dependencies needed)

