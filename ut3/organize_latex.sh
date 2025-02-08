#!/bin/bash

# Input and output files
input_file="combined.tex"
output_file="compiled_articles.tex"

# Temporary files for processing
temp_file=$(mktemp)
preamble_file=$(mktemp)

# Define the standard title and author
standard_title="Combined Articles on Deep Learning"
standard_author="Lucas Eduardo Jaguzewski da Silva (UFPR, Parana, Brazil) and Deep SeekerAI (Hangzhou, China)"

# Step 1: Extract all \usepackage commands and remove duplicates
grep -E '^\\usepackage' "$input_file" | awk '!seen[$0]++' > "$preamble_file"

# Step 2: Process the content to clean up unnecessary commands
awk -v std_title="$standard_title" -v std_author="$standard_author" '
BEGIN {
    # Flags to track if we have processed the title, author, begin document, and preamble
    title_processed = 0
    author_processed = 0
    begin_document_processed = 0
    in_preamble = 1
}
{
    # Remove \textsuperscript everywhere
    gsub(/\\textsuperscript\{[^}]*\}/, "")

    # Handle \title
    if ($0 ~ /^\\title/) {
        if (!title_processed) {
            print "\\title{" std_title "}"
            title_processed = 1
        }
        next
    }

    # Handle \author
    if ($0 ~ /^\\author/) {
        if (!author_processed) {
            print "\\author{" std_author "}"
            author_processed = 1
        }
        next
    }

    # Handle \begin{document}
    if ($0 ~ /^\\begin\{document\}/) {
        if (!begin_document_processed) {
            print "\\begin{document}"
            begin_document_processed = 1
        }
        next
    }

    # Detect the end of the preamble (first non-preamble line)
    if (in_preamble && !/^\\(documentclass|usepackage|RequirePackage|newcommand|renewcommand|DeclareMathOperator)/) {
        in_preamble = 0
    }

    # Remove all \usepackage commands
    if ($0 ~ /^\\usepackage/) {
        next
    }

    # Remove all \end{document} commands
    if ($0 ~ /^\\end\{document\}/) {
        next
    }

    # Print all other lines
    print $0
}' "$input_file" > "$temp_file"

# Step 3: Insert the deduplicated \usepackage commands into the preamble
awk '
BEGIN {
    # Flag to track if we have inserted the usepackage commands
    usepackage_inserted = 0
}
{
    # Insert the \usepackage commands after the \documentclass line
    if (!usepackage_inserted && $0 ~ /^\\documentclass/) {
        print $0
        while ((getline line < "'"$preamble_file"'") > 0) {
            print line
        }
        close("'"$preamble_file"'")
        usepackage_inserted = 1
        next
    }

    # Print all other lines
    print $0
}' "$temp_file" > "$output_file"

# Step 4: Ensure there is exactly one \end{document} at the end of the file
awk '
BEGIN {
    # Flag to track if we have seen \end{document}
    end_document_seen = 0
}
{
    # Remove any existing \end{document} commands
    if ($0 ~ /^\\end\{document\}/) {
        end_document_seen = 1
        next
    }

    # Print all other lines
    print $0
}
END {
    # Add \end{document} at the end if it hasn'"'"'t been added yet
    if (!end_document_seen) {
        print "\\end{document}"
    }
}' "$output_file" > "$temp_file"

# Move the final result back to the output file
mv "$temp_file" "$output_file"

# Clean up temporary files
rm -f "$preamble_file"

echo "Organized article saved as $output_file"
