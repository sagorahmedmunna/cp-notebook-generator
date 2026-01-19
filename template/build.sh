#!/bin/bash

# Build script for Competitive Programming Notebook PDF
# This script compiles the LaTeX document with the required -shell-escape flag

echo "Generating sections from codes folder..."
python3 generate_sections.py

echo "Building PDF..."
echo "Running pdflatex (first pass)..."
pdflatex -shell-escape -interaction=nonstopmode main.tex > /dev/null 2>&1

echo "Running pdflatex (second pass for cross-references)..."
pdflatex -shell-escape -interaction=nonstopmode main.tex > /dev/null 2>&1

if [ -f "main.pdf" ]; then
    echo "✓ PDF built successfully: main.pdf"
    echo "  Pages: $(pdfinfo main.pdf 2>/dev/null | grep Pages | awk '{print $2}' || echo 'unknown')"
else
    echo "✗ Error: PDF was not created. Check main.log for details."
    exit 1
fi
