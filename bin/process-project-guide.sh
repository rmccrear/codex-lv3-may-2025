#!/bin/bash

# Project Guide Processing Script
# ==============================
# 
# This script orchestrates the complete transformation of any concatenated project guide
# into individual level files with navigation and collapsible Show Me sections.
#
# Usage:
#   ./process-project-guide.sh [input_file] [output_dir] [project_name]
#
# Arguments:
#   input_file    - Path to the concatenated guide file
#   output_dir    - Directory to write individual level files  
#   project_name  - Project name (e.g., 'capstone', 'mad-libs') for file naming
#
# Examples:
#   # Capstone project
#   ./process-project-guide.sh capstone/capstone-guide-all-todo.md capstone/capstone-levels capstone
#
#   # Mad Libs project
#   ./process-project-guide.sh mad-libs-guide-all.md mad-libs/mad-libs-levels mad-libs
#
#   # Use defaults (capstone)
#   ./process-project-guide.sh

set -e  # Exit on any error

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# Default paths for capstone project
DEFAULT_INPUT="capstone/capstone-guide-all-todo.md"
DEFAULT_OUTPUT="capstone/capstone-levels"
DEFAULT_PROJECT="capstone"

# Get command line arguments
INPUT_FILE="${1:-$DEFAULT_INPUT}"
OUTPUT_DIR="${2:-$DEFAULT_OUTPUT}"
PROJECT_NAME="${3:-$DEFAULT_PROJECT}"

echo -e "${BLUE}🎯 Project Guide Processing Pipeline${NC}"
echo -e "${BLUE}====================================${NC}"
echo ""
echo -e "📖 Input file: ${YELLOW}$INPUT_FILE${NC}"
echo -e "📁 Output directory: ${YELLOW}$OUTPUT_DIR${NC}"
echo -e "🏷️  Project name: ${YELLOW}$PROJECT_NAME${NC}"
echo ""

# Check if input file exists
if [ ! -f "$INPUT_FILE" ]; then
    echo -e "${RED}❌ Error: Input file '$INPUT_FILE' not found${NC}"
    exit 1
fi

# Create output directory if it doesn't exist
mkdir -p "$OUTPUT_DIR"

echo -e "${BLUE}Step 1: Splitting levels from concatenated guide...${NC}"
python3 bin/split-project-levels.py "$INPUT_FILE" "$OUTPUT_DIR" "$PROJECT_NAME"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to split levels${NC}"
    exit 1
fi
echo ""

echo -e "${BLUE}Step 2: Adding navigation between levels...${NC}"
python3 bin/add-project-navigation.py "$OUTPUT_DIR" "$PROJECT_NAME"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to add navigation${NC}"
    exit 1
fi
echo ""

echo -e "${BLUE}Step 3: Converting Show Me sections to collapsible details...${NC}"
python3 bin/convert-show-me.py "$OUTPUT_DIR"
if [ $? -ne 0 ]; then
    echo -e "${RED}❌ Error: Failed to convert Show Me sections${NC}"
    exit 1
fi
echo ""

# Count the number of level files created
LEVEL_COUNT=$(find "$OUTPUT_DIR" -name "${PROJECT_NAME}-lv-*.md" | wc -l)

echo -e "${GREEN}🎉 Processing Complete!${NC}"
echo -e "${GREEN}======================${NC}"
echo ""
echo -e "✅ Created ${YELLOW}$LEVEL_COUNT${NC} individual level files for ${YELLOW}$PROJECT_NAME${NC}"
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
    find "$OUTPUT_DIR" -name "${PROJECT_NAME}-lv-*.md" | sort -V | while read file; do
        echo -e "  • $(basename "$file")"
    done
else
    echo -e "${BLUE}Created $LEVEL_COUNT level files (too many to list individually)${NC}"
fi
