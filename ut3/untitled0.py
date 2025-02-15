#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  9 18:34:11 2025

@author: narus
"""
import re

# Read the local LaTeX file
with open("compiled.tex", "r", encoding="utf-8") as file:
    latex_content = file.read()

# Remove duplicate package imports
package_pattern = re.compile(r"\\usepackage\{.*?\}")
unique_packages = sorted(set(package_pattern.findall(latex_content)), key=lambda x: latex_content.index(x))
latex_content = package_pattern.sub("", latex_content)
latex_content = "\n".join(unique_packages) + "\n" + latex_content

# Remove duplicate sections
section_pattern = re.compile(r"(\\section\{.*?\})")
unique_sections = sorted(set(section_pattern.findall(latex_content)), key=lambda x: latex_content.index(x))
latex_content = section_pattern.sub("", latex_content)
latex_content = "\n".join(unique_sections) + "\n" + latex_content

# Save cleaned content to a new .tex file
with open("cleaned_article.tex", "w", encoding="utf-8") as file:
    file.write(latex_content)

print("Processing complete. The cleaned LaTeX file is saved as cleaned_article.tex")
