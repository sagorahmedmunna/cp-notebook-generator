#!/usr/bin/env python3
"""
Main build script for Competitive Programming Notebook
Automatically generates sections, compiles LaTeX, and organizes output files
"""

import os
import sys
import subprocess
import shutil
from pathlib import Path

# Configuration
NOTEBOOK_DIR = "template"
MAIN_TEX = "main.tex"
FINAL_PDF_NAME = "notebook.pdf"
GENERATE_SCRIPT = "generate_sections.py"
REQUIRED_FILES = ["main.tex", "math_formulas.tex", "codes"]
AUXILIARY_FILES = [
    "main.aux", "main.log", "main.out", "main.toc",
    "sections.tex", "_minted"
]

def print_step(message):
    """Print a formatted step message"""
    print(f"\n{'='*60}")
    print(f"  {message}")
    print(f"{'='*60}")

def check_requirements():
    """Check if all required files and tools are available"""
    print_step("Checking Requirements")

    # Check if template directory exists
    if not os.path.exists(NOTEBOOK_DIR):
        print(f"✗ Error: '{NOTEBOOK_DIR}' folder not found!")
        return False

    # Check required files
    missing_files = []
    for file in REQUIRED_FILES:
        # codes folder should be in root directory, others in template directory
        if file == "codes":
            file_path = file  # Check in root directory
        else:
            file_path = os.path.join(NOTEBOOK_DIR, file)
        if not os.path.exists(file_path):
            missing_files.append(file)

    if missing_files:
        print(f"✗ Error: Missing required files/folders: {', '.join(missing_files)}")
        return False

    # Check Python
    try:
        subprocess.run(["python3", "--version"], capture_output=True, check=True)
        print("✓ Python3 found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Error: Python3 not found")
        return False

    # Check LaTeX
    try:
        result = subprocess.run(["pdflatex", "--version"], capture_output=True, check=True)
        print("✓ pdflatex found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Error: pdflatex not found. Please install LaTeX distribution.")
        print("  macOS: brew install --cask mactex")
        print("  Linux: sudo apt-get install texlive-full")
        print("  Windows: Install MiKTeX from https://miktex.org/")
        return False

    # Check Pygments
    try:
        subprocess.run(["python3", "-c", "import pygments"], capture_output=True, check=True)
        print("✓ Pygments found")
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("✗ Warning: Pygments not found. Installing...")
        try:
            subprocess.run([sys.executable, "-m", "pip", "install", "pygments"], check=True)
            print("✓ Pygments installed")
        except subprocess.CalledProcessError:
            print("✗ Error: Failed to install Pygments")
            return False

    print("✓ All requirements satisfied")
    return True

def generate_sections():
    """Run generate_sections.py to create sections.tex"""
    print_step("Generating Sections from Codes Folder")

    generate_script_path = os.path.join(NOTEBOOK_DIR, GENERATE_SCRIPT)
    if not os.path.exists(generate_script_path):
        print(f"✗ Error: {generate_script_path} not found!")
        return False

    try:
        # Change to template directory and run the script (use just filename since cwd is set)
        result = subprocess.run(
            ["python3", GENERATE_SCRIPT],
            cwd=NOTEBOOK_DIR,
            capture_output=True,
            text=True,
            check=True
        )
        print(result.stdout)
        print("✓ Sections generated successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Error generating sections:")
        print(e.stderr)
        return False

def compile_latex():
    """Compile LaTeX document with -shell-escape flag"""
    print_step("Compiling LaTeX Document")

    main_tex_path = os.path.join(NOTEBOOK_DIR, MAIN_TEX)
    if not os.path.exists(main_tex_path):
        print(f"✗ Error: {main_tex_path} not found!")
        return False

    # First compilation
    print("Running first pdflatex pass...")
    try:
        result = subprocess.run(
            ["pdflatex", "-shell-escape", "-interaction=nonstopmode", MAIN_TEX],
            cwd=NOTEBOOK_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("⚠ Warning: First compilation had errors (this may be normal)")
            # Print errors for debugging
            if result.stderr:
                print(result.stderr[:500])  # Print first 500 chars of errors
    except Exception as e:
        print(f"✗ Error running pdflatex: {e}")
        return False

    # Second compilation (for cross-references)
    print("Running second pdflatex pass...")
    try:
        result = subprocess.run(
            ["pdflatex", "-shell-escape", "-interaction=nonstopmode", MAIN_TEX],
            cwd=NOTEBOOK_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("⚠ Warning: Second compilation had errors")
            if result.stderr:
                print(result.stderr[:500])
    except Exception as e:
        print(f"✗ Error running pdflatex: {e}")
        return False

    # Third compilation (for lastpage reference to resolve correctly)
    print("Running third pdflatex pass (for page count)...")
    try:
        result = subprocess.run(
            ["pdflatex", "-shell-escape", "-interaction=nonstopmode", MAIN_TEX],
            cwd=NOTEBOOK_DIR,
            capture_output=True,
            text=True
        )
        if result.returncode != 0:
            print("⚠ Warning: Third compilation had errors")
            if result.stderr:
                print(result.stderr[:500])
    except Exception as e:
        print(f"✗ Error running pdflatex: {e}")
        return False

    # Check if PDF was created
    pdf_file = MAIN_TEX.replace(".tex", ".pdf")
    pdf_path = os.path.join(NOTEBOOK_DIR, pdf_file)
    if os.path.exists(pdf_path):
        print(f"✓ PDF compiled successfully: {pdf_file}")
        return True
    else:
        log_file = os.path.join(NOTEBOOK_DIR, MAIN_TEX.replace(".tex", ".log"))
        print(f"✗ Error: PDF was not created. Check {log_file} for details.")
        return False

def organize_output():
    """Rename PDF to notebook.pdf, move to root, and clean up auxiliary files"""
    print_step("Organizing Output Files")

    # First, check if PDF exists in build_output directory
    build_output_pdf = os.path.join("build_output", "main.pdf")
    pdf_source = None

    if os.path.exists(build_output_pdf):
        pdf_source = build_output_pdf
        print(f"✓ Found PDF in build_output directory")
    else:
        # Fallback: check template directory (for backward compatibility)
        pdf_file = MAIN_TEX.replace(".tex", ".pdf")
        pdf_source = os.path.join(NOTEBOOK_DIR, pdf_file)
        if os.path.exists(pdf_source):
            print(f"✓ Found PDF in template directory")
        else:
            print(f"⚠ Warning: PDF not found in build_output or template directory")
            return

    # Remove existing notebook.pdf in root if it exists
    final_pdf_path = FINAL_PDF_NAME
    if os.path.exists(final_pdf_path):
        os.remove(final_pdf_path)
        print(f"✓ Removed existing {FINAL_PDF_NAME}")

    # Move and rename PDF to root directory
    shutil.move(pdf_source, final_pdf_path)
    print(f"✓ Renamed and moved PDF to {FINAL_PDF_NAME}")

    # Clean up build_output directory - remove all files except the PDF (which we already moved)
    if os.path.exists("build_output"):
        try:
            build_output_files = os.listdir("build_output")
            removed_count = 0
            for item in build_output_files:
                item_path = os.path.join("build_output", item)
                try:
                    if os.path.isdir(item_path):
                        shutil.rmtree(item_path)
                    else:
                        os.remove(item_path)
                    removed_count += 1
                except Exception as e:
                    print(f"⚠ Warning: Could not remove {item}: {e}")

            # Remove the build_output directory itself
            os.rmdir("build_output")
            print(f"✓ Removed {removed_count} file(s) from build_output and deleted directory")
        except Exception as e:
            print(f"⚠ Warning: Could not clean build_output: {e}")

    # Remove all auxiliary files from template directory
    removed_count = 0
    for aux_file in AUXILIARY_FILES:
        aux_source = os.path.join(NOTEBOOK_DIR, aux_file)
        if os.path.exists(aux_source):
            try:
                if os.path.isdir(aux_source):
                    shutil.rmtree(aux_source)
                else:
                    os.remove(aux_source)
                removed_count += 1
            except Exception as e:
                print(f"⚠ Warning: Could not remove {aux_file}: {e}")

    if removed_count > 0:
        print(f"✓ Removed {removed_count} auxiliary file(s) from template directory")

    if os.path.exists(final_pdf_path):
        abs_path = os.path.abspath(final_pdf_path)
        print(f"\n✓ Build complete! PDF is available at: {abs_path}")
    else:
        print(f"\n⚠ Warning: PDF not found at expected location")

def main():
    """Main build process"""
    print("\n" + "="*60)
    print("  Competitive Programming Notebook - Build Script")
    print("="*60)

    # Step 1: Check requirements
    if not check_requirements():
        print("\n✗ Build failed: Requirements not met")
        sys.exit(1)

    # Step 2: Generate sections
    if not generate_sections():
        print("\n✗ Build failed: Could not generate sections")
        sys.exit(1)

    # Step 3: Compile LaTeX
    if not compile_latex():
        print("\n✗ Build failed: LaTeX compilation failed")
        sys.exit(1)

    # Step 4: Organize output
    organize_output()

    print("\n" + "="*60)
    print("  ✓ Build completed successfully!")
    print("="*60 + "\n")

if __name__ == "__main__":
    main()
