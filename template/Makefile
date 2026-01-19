# Makefile for Competitive Programming Notebook PDF

MAIN = main
TEX = $(MAIN).tex
PDF = $(MAIN).pdf

# Default target
all: $(PDF)

# Generate sections from codes folder
sections.tex: generate_sections.py
	@echo "Generating sections from codes folder..."
	@python3 generate_sections.py

# Build PDF
$(PDF): $(TEX) sections.tex
	@echo "Building PDF..."
	@pdflatex -shell-escape -interaction=nonstopmode $(MAIN).tex > /dev/null 2>&1 || true
	@pdflatex -shell-escape -interaction=nonstopmode $(MAIN).tex > /dev/null 2>&1 || true
	@if [ -f "$(PDF)" ]; then \
		echo "✓ PDF built successfully: $(PDF)"; \
	else \
		echo "✗ Error: PDF was not created. Check $(MAIN).log for details."; \
		exit 1; \
	fi

# Clean auxiliary files
clean:
	@echo "Cleaning auxiliary files..."
	@rm -f $(MAIN).aux $(MAIN).log $(MAIN).out $(MAIN).toc sections.tex
	@echo "✓ Cleaned auxiliary files"

# Clean everything including minted cache
cleanall: clean
	@echo "Cleaning minted cache..."
	@rm -rf _minted
	@echo "✓ Cleaned minted cache"

# Rebuild from scratch
rebuild: cleanall $(PDF)

.PHONY: all clean cleanall rebuild
