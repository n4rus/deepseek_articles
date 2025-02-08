#!/bin/bash

# Input and output files
input_file="combined.tex"
output_file="compiled_articles.tex"

# Temporary files for processing
temp_file=$(mktemp)

# Define the standard title and author
standard_title="Combined Articles on Deep Learning"
standard_author="Lucas Eduardo Jaguzewski da Silva (UFPR, Parana, Brazil) and Deep SeekerAI (Hangzhou, China)"

# Step 1: Remove \title, \author, \textsuperscript, and misplaced \begin{document}
awk '
BEGIN {
    # Flags to track if we have processed the title, author, and begin document
    title_processed = 0
    author_processed = 0
    begin_document_processed = 0
}
{
    # Remove \textsuperscript everywhere
    gsub(/\\textsuperscript\{[^}]*\}/, "")

    # Handle \title
    if ($0 ~ /^\\title/) {
        if (!title_processed) {
            print "\\title{" standard_title "}"
            title_processed = 1
        }
        next
    }

    # Handle \author
    if ($0 ~ /^\\author/) {
        if (!author_processed) {
            print "\\author{" standard_author "}"
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

    # Print all other lines except those matching \title, \author, or \begin{document}
    print $0
}' standard_title="$standard_title" standard_author="$standard_author" "$input_file" > "$temp_file"

# Step 2: Ensure \begin{document} is placed correctly after the preamble
awk '
BEGIN {
    in_preamble = 1
}
{
    if (in_preamble && $0 ~ /^\\begin\{document\}/) {
        in_preamble = 0
        print "\\begin{document}"
        next
    }
    if ($0 !~ /^\\begin\{document\}/) {
        print $0
    }
}' "$temp_file" > "$output_file"

# Clean up temporary files
rm -f "$temp_file"

echo "Cleaned article saved as $output_file"
