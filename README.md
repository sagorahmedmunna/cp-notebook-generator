# Competitive Programming Notebook

A LaTeX-based notebook containing competitive programming templates and algorithms.

## Step-by-Step Setup Guide

Follow these steps to build the PDF from scratch:

### Step 1: Install LaTeX

Install a LaTeX distribution based on your operating system:

- **macOS**: Install [MacTeX](https://www.tug.org/mactex/) (full distribution) or use Homebrew:
  ```bash
  brew install --cask mactex
  ```

- **Linux**: Install TeX Live:
  ```bash
  sudo apt-get install texlive-full  # Ubuntu/Debian
  # or
  sudo yum install texlive-scheme-full  # CentOS/RHEL
  ```

- **Windows**: Install [MiKTeX](https://miktex.org/download) or [TeX Live](https://www.tug.org/texlive/windows.html)

Verify installation:
```bash
pdflatex --version
```

### Step 2: Install Python and Pygments

Install Python (if not already installed) and the Pygments package required for syntax highlighting:

```bash
pip install pygments
# or
pip3 install pygments
```

### Step 3: Get the Required Files and Folders

Ensure you have the following files and folder structure:

**Required Files:**
- `main.tex` - The main LaTeX document
- `generate_sections.py` - Python script to generate sections from code files
- `sections.tex` - Generated file (will be created by the script)

**Required Folder:**
- `codes/` - Folder containing all `.cpp` template files

**Optional Files (for advanced builds):**
- `Makefile` - For building with `make`
- `build.sh` - Alternative build script
- `build` - Simple wrapper script
- `latexmkrc` - Configuration for latexmk

### Step 4: Generate Sections from Code Files

Run the Python script to automatically generate `sections.tex` from all `.cpp` files in the `codes/` folder:

```bash
python3 generate_sections.py
```

This script will:
- Scan the `codes/` folder for all `.cpp` files
- Generate section names by converting filenames (removing underscores, capitalizing words)
- Create `sections.tex` with all the sections

### Step 5: Build the PDF with LaTeX

Compile the main LaTeX document using `pdflatex` with the `-shell-escape` flag (required for the `minted` package):

```bash
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex  # Run twice for cross-references
```

The PDF will be generated as `main.pdf`.

**Note**: Always use the `-shell-escape` flag. Without it, you will get errors because `minted` cannot process the code files.








## Building the PDF

⚠️ **IMPORTANT**: This document uses the `minted` package which **REQUIRES** the `-shell-escape` flag. You **cannot** build it with just `pdflatex main.tex`. You must use one of the methods below:

### Method 1: Using Make (Recommended)
```bash
make
```
or
```bash
make pdf
```

### Method 2: Using the Build Script
```bash
chmod +x build.sh
./build.sh
```

### Method 3: Using latexmk
```bash
latexmk main.tex
```

### Method 4: Manual Compilation
```bash
pdflatex -shell-escape main.tex
pdflatex -shell-escape main.tex  # Run twice for cross-references
```

**Note**: If you try to run `pdflatex main.tex` without `-shell-escape`, you will get errors because `minted` cannot process the code files. Always use `-shell-escape` or one of the build methods above.

## Requirements

- LaTeX distribution (TeX Live, MiKTeX, or MacTeX)
- Python with Pygments installed:
  ```bash
  pip install pygments
  ```
- For Method 1: `make` (usually pre-installed on Unix systems)
- For Method 3: `latexmk` (usually included with LaTeX distributions)

## Automatic Section Generation

The LaTeX sections are **automatically generated** from the files in the `codes/` folder. When you run `make` or `./build.sh`, it will:

1. Scan the `codes/` folder for all `.cpp` files
2. Generate section names by removing underscores and `.cpp` extension
3. Create `sections.tex` with all the sections
4. Build the PDF

**To manually regenerate sections:**
```bash
python3 generate_sections.py
```

## Files Needed

- `main.tex` - The main LaTeX document
- `codes/` - Folder containing all `.cpp` template files
- `generate_sections.py` - Script to auto-generate sections from codes folder
- `Makefile` - For building with `make`
- `build.sh` - Alternative build script
- `build` - Simple wrapper script
- `latexmkrc` - Configuration for latexmk

## Cleaning

To remove auxiliary files:
```bash
make clean
```

To remove everything including minted cache:
```bash
make cleanall
```

To rebuild from scratch:
```bash
make rebuild
```

## Troubleshooting

If you get errors about `minted` or Pygments:
1. Ensure Python is installed: `python --version` or `python3 --version`
2. Install Pygments: `pip install pygments` or `pip3 install pygments`
3. Ensure your LaTeX distribution supports `-shell-escape`

If the PDF shows only section titles without code:
- Make sure you're using the `-shell-escape` flag
- Check that Pygments is installed correctly
- Try running the compilation twice (minted requires multiple passes)
