#!/usr/bin/env python3
"""
Generate LaTeX sections automatically from codes folder
This script reads all .cpp files and generates the LaTeX code
"""

import os
import re

def filename_to_section_name(filename):
    """Convert filename to section name format"""
    # Remove .cpp extension
    name = filename.replace('.cpp', '')

    # Handle special cases
    if name == '0custom':
        return 'Custom Codes'

    # Replace underscores with spaces
    name = name.replace('_', ' ')

    # Handle special characters
    name = name.replace('&', '\\&')  # Escape & for LaTeX

    # Capitalize first letter of each word
    words = name.split()
    capitalized_words = []
    for word in words:
        # Capitalize first letter, keep rest lowercase
        if word:
            capitalized_words.append(word[0].upper() + word[1:].lower())

    return ' '.join(capitalized_words)

def generate_sections():
    """Generate LaTeX sections from codes folder"""
    # codes folder is in parent directory (root, same as main.py)
    codes_folder = "../codes"

    if not os.path.exists(codes_folder):
        print(f"Error: '{codes_folder}' folder not found!")
        return

    # Get all .cpp files
    files = [f for f in os.listdir(codes_folder) if f.endswith('.cpp')]
    files.sort()  # Sort alphabetically

    # Generate LaTeX code
    latex_code = []
    for filename in files:
        section_name = filename_to_section_name(filename)
        latex_code.append(f"\t\t\\section{{{section_name}}}")
        latex_code.append(f"\t\t\\inputminted{{cpp}}{{../codes/{filename}}}")
        latex_code.append("")

    return '\n'.join(latex_code)

if __name__ == "__main__":
    sections = generate_sections()

    # Write to sections.tex file
    with open('sections.tex', 'w') as f:
        f.write(sections)

    print(f"✓ Generated sections.tex with {len([f for f in os.listdir('../codes') if f.endswith('.cpp')])} sections")
    print("  Now run: pdflatex -shell-escape main.tex")
