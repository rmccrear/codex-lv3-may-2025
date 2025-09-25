#!/bin/bash

# Perl one-liner to renumber all levels sequentially
# Usage: ./renumber-levels-perl.sh

FILE="guides/week8-capstone/capstone-guide-all.md"

# Create backup
cp "$FILE" "${FILE}.backup"

# Perl one-liner to renumber levels
perl -e '
my $counter = 1;
while (<>) {
    if (/^# .*Level \d+: (.+)$/) {
        print "# 🎯 Level $counter: $1\n";
        $counter++;
    } else {
        print;
    }
}
' "$FILE" > "${FILE}.tmp" && mv "${FILE}.tmp" "$FILE"

echo "Renumbered levels sequentially using perl"
echo "Backup saved as ${FILE}.backup"

# =============================================================================
# HOW THE PERL ONE-LINER WORKS
# =============================================================================
#
# The perl command processes the file line by line and renumbers level headers.
# Here's what each part does:
#
# perl -e '...'                    # Run perl with the code in quotes
# my $counter = 1;                 # Create a variable called $counter, start at 1
# while (<>) {                     # Loop through each line of input
#     if (/^# .*Level \d+: (.+)$/) # Check if line matches the pattern:
#                                   #   ^# = starts with "# "
#                                   #   .* = any characters (like emoji)
#                                   #   Level = literal word "Level"
#                                   #   \d+ = one or more digits
#                                   #   : = literal colon
#                                   #   (.+) = capture everything after colon
#         print "# 🎯 Level $counter: $1\n";  # Print new level header with:
#                                            #   - Fixed emoji 🎯
#                                            #   - Sequential number ($counter)
#                                            #   - Original title ($1)
#         $counter++;              # Increment counter for next level
#     } else {
#         print;                   # Print the line unchanged if not a level header
#     }
# }
#
# The result: All level headers get renumbered 1, 2, 3, 4... in order
# while all other lines (content, code, etc.) remain exactly the same.
