#!/bin/bash

# Capstone Guide Processing Script
# ================================
# 
# This script orchestrates the complete transformation of capstone-guide-all-todo.md
# into individual level files with navigation and collapsible Show Me sections.
#
# Usage:
#   ./process-capstone-guide.sh [input_file] [output_dir]
#
# If no arguments provided, uses:
#   - Input: capstone/capstone-guide-all-todo.md
#   - Output: capstone/capstone-levels/

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default paths
DEFAULT_INPUT="capstone/capstone-guide-all-todo.md"
DEFAULT_OUTPUT="capstone/capstone-levels"

# Get command line arguments
INPUT_FILE="${1:-$DEFAULT_INPUT}"
OUTPUT_DIR="${2:-$DEFAULT_OUTPUT}"

echo -e "${BLUE}🎯 Capstone Guide Processing Pipeline${NC}"
echo -e "${BLUE}=====================================${NC}"
echo ""
echo -e "📖 Input file: ${YELLOW}$INPUT_FILE${NC}"
echo -e "📁 Output directory: ${YELLOW}$OUTPUT_DIR${NC}"
echo ""

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${RED}❌ Error: Input file '$INPUT_FILE' not found${NC}"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}Step 1: Splitting levels from concatenated guide...${NC}"
python3 capstone/split-capstone-levels.py "$INPUT_FILE" "$OUTPUT_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to split levels${NC}"
    exit 1
fi
echo ""

echo -e "${BLUE}Step 2: Adding navigation between levels...${NC}"
python3 capstone/add-navigation.py "$OUTPUT_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to add navigation${NC}"
    exit 1
fi
echo ""

echo -e "${BLUE}Step 3: Converting Show Me sections to collapsible details...${NC}"
python3 capstone/convert-show-me.py "$OUTPUT_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to convert Show Me sections${NC}"
    exit 1
fi
echo ""

# Count the number of level files created
LEVEL_COUNT=$(find "$OUTPUT_DIR" -name "capstone-lv-*.md" | wc -l)

echo -e "${GREEN}🎉 Processing Complete!${NC}"
echo -e "${GREEN}=======================${NC}"
echo ""
echo -e "✅ Created ${YELLOW}$LEVEL_COUNT${NC} individual level files"
echo -e "✅ Added navigation between all levels"
echo -e "✅ Converted Show Me sections to collapsible details"
echo ""
echo -e "📁 Level files are now available in: ${YELLOW}$OUTPUT_DIR${NC}"
echo ""
echo -e "${BLUE}Next steps:${NC}"
echo -e "  • Review the generated level files"
echo -e "  • Test navigation between levels"
echo -e "  • Verify Show Me sections work correctly"
echo -e "  • Commit changes to version control"
echo ""

# Optional: List the created files
if [ "$LEVEL_COUNT" -le 10 ]; then
    echo -e "${BLUE}Created files:${NC}"
    find "$OUTPUT_DIR" -name "capstone-lv-*.md" | sort -V | while read file; do
        echo -e "  • $(basename "$file")"
    done
else
    echo -e "${BLUE}Created $LEVEL_COUNT level files (too many to list individually)${NC}"
fi
