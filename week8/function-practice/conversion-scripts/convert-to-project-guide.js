#!/usr/bin/env node

const fs = require('fs');
const path = require('path');

/**
 * Add markers to markdown content
 * - Add LEVEL_START at the beginning
 * - Replace --- before ## headers with LEVEL_START
 * - Add INFORMATIVE_ONLY for headers without "Step"
 */
function addMarkers(content) {
  let result = content;
  
  // Add LEVEL_START at the very beginning
  if (!result.startsWith('<!-- LEVEL_START -->')) {
    result = '<!-- LEVEL_START -->\n' + result;
  }
  
  // Replace --- before ## headers with LEVEL_START
  // Pattern: --- followed by newline(s) and ##
  result = result.replace(/^---\s*\n+/gm, '<!-- LEVEL_START -->\n');
  
  // Add LEVEL_START before ## headers that don't already have it
  // Split by lines and process
  const lines = result.split('\n');
  const processedLines = [];
  
  for (let i = 0; i < lines.length; i++) {
    const line = lines[i];
    
    // Check if this is a ## header
    if (line.match(/^## /)) {
      // Check if previous line is not already a marker
      const prevLine = i > 0 ? lines[i - 1].trim() : '';
      const hasMarker = prevLine === '<!-- LEVEL_START -->' || 
                       prevLine === '<!-- INFORMATIVE_ONLY -->';
      
      if (!hasMarker) {
        // Check if header contains "Step" or "Steps" (case insensitive)
        // But exclude "Setup Steps" and similar - those are informational
        if (line.match(/Step\s*\d+/i)) {
          // This is a numbered step like "Step 1:", "Step 2", etc.
          processedLines.push('<!-- LEVEL_START -->');
        } else {
          // All other headers are informational
          processedLines.push('<!-- LEVEL_START -->');
          processedLines.push('<!-- INFORMATIVE_ONLY -->');
        }
      }
    }
    
    // Also check for # headers (h1) - these should be the first level
    if (line.match(/^# /) && !line.match(/^# Quick|^# Adding|^# Red-Green/)) {
      // This is handled by the beginning marker, but we can add INFORMATIVE_ONLY if needed
    }
    
    processedLines.push(line);
  }
  
  result = processedLines.join('\n');
  
  return result;
}

/**
 * Extract levels from marked content
 */
function extractLevels(content) {
  const levels = [];
  const parts = content.split(/<!-- LEVEL_START -->/);
  
  for (let i = 1; i < parts.length; i++) {
    const part = parts[i].trim();
    if (part) {
      const isInformative = part.startsWith('<!-- INFORMATIVE_ONLY -->');
      const levelContent = isInformative 
        ? part.replace(/^<!-- INFORMATIVE_ONLY -->\n?/, '')
        : part;
      
      levels.push({
        content: levelContent,
        isInformative: isInformative
      });
    }
  }
  
  return levels;
}

/**
 * Renumber levels sequentially
 */
function renumberLevels(levels, startNumber = 1) {
  return levels.map((level, index) => {
    const levelNumber = startNumber + index;
    let renumbered = level.content;
    
    // Replace "Step X" with "Level X" in headers
    renumbered = renumbered.replace(
      /^## Step (\d+):/gm,
      (match, stepNum) => `## Level ${levelNumber}:`
    );
    // Also handle headers that are just "Step X" without colon
    renumbered = renumbered.replace(
      /^## Step (\d+)\s/gm,
      (match, stepNum) => `## Level ${levelNumber} `
    );
    
    // If first header is h1 (#), convert it to h2 with Level number
    renumbered = renumbered.replace(
      /^(# )([^#\n]+)$/m,
      (match, prefix, title) => {
        // Skip if it's one of the main titles
        if (title.match(/^(Quick Intro to Vitest|Adding More Tests|Red-Green-Refactor)/)) {
          return `## Level ${levelNumber}: ${title.trim()}`;
        }
        return `## Level ${levelNumber}: ${title.trim()}`;
      }
    );
    
    // If first header is h2 (##) and doesn't have "Step" or "Level", add "Level X: " prefix
    const firstH2Match = renumbered.match(/^## ([^#\n]+)$/m);
    if (firstH2Match && !firstH2Match[1].includes('Level') && !firstH2Match[1].match(/Step\s*\d+/i)) {
      renumbered = renumbered.replace(
        /^(## )([^#\n]+)$/m,
        (match, prefix, title) => `${prefix}Level ${levelNumber}: ${title.trim()}`
      );
    }
    
    return {
      ...level,
      number: levelNumber,
      content: renumbered
    };
  });
}

/**
 * Format a single level for output
 */
function formatLevel(level) {
  let output = '<!-- LEVEL_START -->\n';
  
  // Add INFORMATIVE_ONLY marker if this level is informational
  if (level.isInformative) {
    output += '<!-- INFORMATIVE_ONLY -->\n';
  }
  
  output += '\n';
  output += level.content;
  output += '\n\n---\n\n';
  return output;
}

/**
 * Clean up intermediary files
 */
function cleanupIntermediaryFiles(practiceDir, inputFiles) {
  console.log('\nCleaning up intermediary files...');
  
  for (const filename of inputFiles) {
    const markedFilePath = path.join(practiceDir, filename.replace('.md', '-marked.md'));
    
    if (fs.existsSync(markedFilePath)) {
      fs.unlinkSync(markedFilePath);
      console.log(`  → Removed: ${path.basename(markedFilePath)}`);
    }
  }
  
  console.log('✅ Cleanup complete');
}

/**
 * Discover and sort source files by numeric prefix
 */
function discoverSourceFiles(practiceDir) {
  const files = fs.readdirSync(practiceDir);
  
  // Find files matching pattern: ##-vitest-*-guide.md
  const sourceFiles = files
    .filter(file => /^\d{2}-vitest-.*-guide\.md$/.test(file))
    .sort((a, b) => {
      // Extract numeric prefix and compare
      const numA = parseInt(a.match(/^(\d{2})-/)[1]);
      const numB = parseInt(b.match(/^(\d{2})-/)[1]);
      return numA - numB;
    });
  
  return sourceFiles;
}

/**
 * Main conversion function
 */
function convertToProjectGuide() {
  const scriptDir = __dirname;
  const practiceDir = path.dirname(scriptDir);
  
  // Automatically discover source files sorted by numeric prefix
  const inputFiles = discoverSourceFiles(practiceDir);
  
  if (inputFiles.length === 0) {
    console.error('Error: No source files found matching pattern ##-vitest-*-guide.md');
    console.error('Expected files like: 01-vitest-intro-guide.md, 02-vitest-add-tests-guide.md, etc.');
    process.exit(1);
  }
  
  let allLevels = [];
  let currentLevelNumber = 1;
  
  console.log('Converting Vitest guides to project guide format...\n');
  console.log(`Found ${inputFiles.length} source files:`);
  inputFiles.forEach(file => console.log(`  - ${file}`));
  console.log('');
  
  // Process each file
  for (const filename of inputFiles) {
    const filePath = path.join(practiceDir, filename);
    
    if (!fs.existsSync(filePath)) {
      console.error(`Error: File not found: ${filePath}`);
      process.exit(1);
    }
    
    console.log(`Processing ${filename}...`);
    
    // Read file
    let content = fs.readFileSync(filePath, 'utf8');
    
    // Add markers
    const markedContent = addMarkers(content);
    
    // Save intermediary file (optional, for debugging)
    const markedFilePath = path.join(practiceDir, filename.replace('.md', '-marked.md'));
    fs.writeFileSync(markedFilePath, markedContent);
    console.log(`  → Created intermediary file: ${path.basename(markedFilePath)}`);
    
    // Extract levels
    const levels = extractLevels(markedContent);
    console.log(`  → Extracted ${levels.length} levels`);
    
    // Renumber levels
    const renumberedLevels = renumberLevels(levels, currentLevelNumber);
    allLevels = allLevels.concat(renumberedLevels);
    
    currentLevelNumber += levels.length;
    
    console.log(`  → Renumbered to levels ${renumberedLevels[0]?.number || 'N/A'} - ${renumberedLevels[renumberedLevels.length - 1]?.number || 'N/A'}\n`);
  }
  
  // Format all levels
  console.log('Formatting project guide...');
  let projectGuide = '';
  
  for (const level of allLevels) {
    projectGuide += formatLevel(level);
  }
  
  // Write output file
  const outputPath = path.join(practiceDir, 'vitest-project-guide.md');
  fs.writeFileSync(outputPath, projectGuide);
  
  console.log(`\n✅ Successfully created: vitest-project-guide.md`);
  console.log(`   Total levels: ${allLevels.length}`);
  
  // Clean up intermediary files
  const keepIntermediary = process.argv.includes('--keep-intermediary') || process.argv.includes('-k');
  if (!keepIntermediary) {
    cleanupIntermediaryFiles(practiceDir, inputFiles);
  } else {
    console.log(`\n⚠️  Keeping intermediary files (use without --keep-intermediary to auto-cleanup)`);
  }
}

// Run the conversion
if (require.main === module) {
  convertToProjectGuide();
}

module.exports = { addMarkers, extractLevels, renumberLevels, formatLevel };

