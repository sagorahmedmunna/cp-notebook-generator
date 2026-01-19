# Competitive Programming Notebook

A LaTeX-based notebook containing competitive programming templates and algorithms.

## Quick Start (Easiest Method)

After installing LaTeX and Python (see Step-by-Step Setup Guide below), simply run:

```bash
python3 main.py
```

This single command will:
- ✅ Check all requirements automatically
- ✅ Generate sections from the `codes/` folder
- ✅ Compile the LaTeX document
- ✅ Organize all output files in the `build_output/` folder
- ✅ Create the final PDF

The PDF will be available at `build_output/main.pdf`






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

### Step 3: Project Structure

The project has the following structure:

```
.
├── main.py              # Main build script (run this!)
├── README.md            # This file
└── notebook/            # All LaTeX and source files
    ├── main.tex         # Main LaTeX document
    ├── math_formulas.tex # Mathematical formulas and notes
    ├── generate_sections.py # Script to generate sections
    ├── codes/           # Folder containing all .cpp template files
    ├── sections.tex      # Generated file (created automatically)
    ├── Makefile         # For building with make (optional)
    ├── build.sh         # Alternative build script (optional)
    └── ...              # Other LaTeX-related files
```

**Note**: All files except `main.py` and `README.md` are in the `notebook/` folder. The `main.py` script handles everything automatically.

### Step 4: Build the PDF

**Option A: Automated Build (Recommended)**

Simply run the main build script:

```bash
python3 main.py
```

This will automatically:
- Generate sections from the `codes/` folder
- Compile the LaTeX document
- Organize all output files in `build_output/` folder
- Create the final PDF at `build_output/main.pdf`

**Option B: Manual Build**

If you prefer to build manually, navigate to the `notebook/` folder first:

1. Change to the notebook directory:
   ```bash
   cd notebook
   ```

2. Generate sections from code files:
   ```bash
   python3 generate_sections.py
   ```
   This script will:
   - Scan the `codes/` folder for all `.cpp` files
   - Generate section names by converting filenames (removing underscores, capitalizing words)
   - Create `sections.tex` with all the sections

3. Build the PDF with LaTeX:
   ```bash
   pdflatex -shell-escape main.tex
   pdflatex -shell-escape main.tex  # Run twice for cross-references
   ```
   The PDF will be generated as `main.pdf` in the `notebook/` folder.

**Note**: Always use the `-shell-escape` flag. Without it, you will get errors because `minted` cannot process the code files.








## Building the PDF

⚠️ **IMPORTANT**: This document uses the `minted` package which **REQUIRES** the `-shell-escape` flag. You **cannot** build it with just `pdflatex main.tex`. You must use one of the methods below:

### Method 1: Using main.py (Recommended - Automated)

The easiest way to build everything automatically:

```bash
python3 main.py
```

This script handles everything automatically and organizes output files in the `build_output/` folder.

### Method 2: Using Make

Navigate to the `notebook/` folder first:
```bash
cd notebook
make
```
or
```bash
cd notebook
make pdf
```

### Method 3: Using the Build Script

Navigate to the `notebook/` folder first:
```bash
cd notebook
chmod +x build.sh
./build.sh
```

### Method 4: Using latexmk

Navigate to the `notebook/` folder first:
```bash
cd notebook
latexmk main.tex
```

### Method 5: Manual Compilation

Navigate to the `notebook/` folder first:
```bash
cd notebook
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
cd notebook
python3 generate_sections.py
```

## Project Structure

**Root Directory:**
- `main.py` - Main automated build script (run this!)
- `README.md` - Documentation

**notebook/ Directory:**
- `main.tex` - Main LaTeX document
- `math_formulas.tex` - Mathematical formulas and notes
- `generate_sections.py` - Script to auto-generate sections from codes folder
- `codes/` - Folder containing all `.cpp` template files
- `sections.tex` - Generated file (created automatically by the build process)
- `Makefile` - For building with `make` (optional)
- `build.sh` - Alternative build script (optional)
- Other LaTeX-related files and build artifacts

## Cleaning

Navigate to the `notebook/` folder first, then:

To remove auxiliary files:
```bash
cd notebook
make clean
```

To remove everything including minted cache:
```bash
cd notebook
make cleanall
```

To rebuild from scratch:
```bash
cd notebook
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
