## CP Notebook Front Page

This project is a LaTeX template for an ICPC-style competitive programming notebook front page.

### 1. Where to edit your information

All team, institute, and supervisor information lives near the top of `main.tex` in the **CONFIG SECTION**:

- **Logo file**: set the filename of your logo (PNG/JPG/PDF) placed in this folder
  - `\newcommand{\universityLogo}{University_logo.png}`
- **Basic info**:
  - `\teamNumber` — your team ID (e.g. `ICPCSLG004`)
  - `\teamName` — your team name
  - `\instituteName` — your university or institute name
  - `\regionName` — contest name/region
  - `\seasonName` — season string (e.g. `ICPC 2025--2026 Season`)
- **Members** (name + email for each member):
  - `\memberOneName`, `\memberOneEmail`
  - `\memberTwoName`, `\memberTwoEmail`
  - `\memberThreeName`, `\memberThreeEmail`
- **Supervisor / Coach**:
  - `\supervisorName`
  - `\supervisorTitle`

Edit only the **right-hand side** of each `\newcommand{...}{...}` line (inside the second pair of curly braces).

### 2. How to compile to PDF

Requirements:

- A working LaTeX distribution (e.g. TeX Live, MiKTeX)
- `pdflatex` available in your terminal/command prompt

Steps:

1. Open a terminal in this folder (where `main.tex` is located).
2. Run:

   ```bash
   pdflatex main.tex
   ```

3. For best results (to update all references), run `pdflatex` **a second time**:

   ```bash
   pdflatex main.tex
   ```

4. After successful compilation, you will get `main.pdf` in the same folder. This is your final front page.

### 2.1. One-command build, clean, and rename

If you want to **delete the extra files** (`.aux`, `.log`, `.out`) and have the final PDF named **`front_page.pdf`**, you can run this single command in the terminal (from this folder):

```bash
pdflatex main.tex && pdflatex main.tex && rm -f main.aux main.log main.out main.out && mv -f main.pdf front_page.pdf
```

After it finishes, you will have:

- Cleaned-up directory (no `main.aux`, `main.log`, `main.out`)
- Final PDF named `front_page.pdf`

### 3. Changing the logo

1. Put your logo file (e.g. `MyUniversityLogo.png`) into this folder.
2. In `main.tex`, set:

   ```tex
   \newcommand{\universityLogo}{MyUniversityLogo.png}
   ```

3. Re-run `pdflatex main.tex` (twice, as above) to update the PDF.

