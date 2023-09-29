# LaTeX_auto_tooltip

## Description

`LaTeX_auto_tooltip` is a project that allows equations and citation references to appear as pop-ups in Adobe Reader. When the reader hovers over an equation or citation reference in a PDF generated from LaTeX, a contextual pop-up window displays additional information.

![demo](https://github.com/Samuel-Treton/LaTeX_auto_tooltip/blob/main/auto_tooltip_demo.gif)

## Features

- Pop-up display for LaTeX equations
- Pop-up display for citation references

## Prerequisites

- Make sure you have Python installed on your computer. If not, you can download it from [Python's official website](https://www.python.org/downloads/).
- Ensure that your MiKTeX distribution is up-to-date. You can update it through the MiKTeX Console.

## How It Works

### Step 1: Prepare Your LaTeX File

Create your LaTeX file as usual.

#### Important Notes:

- Avoid special characters in labels, such as `.`, `-`, and `_`. Instead, use case sensitivity to distinguish your labels, for example, `MySuperFirstEquation`.
- The formatting of equations should be as follows:
  ```latex
  \begin{equation}\label{MySuperFirstEquation}
    E = mc^2
  \end{equation}
  ```
  Note that `\begin{equation}\label{XXX}` must be on the same line.
- Include the `mytooltip.sty` and `biblio.sty` packages in your LaTeX file.
  ```latex
  \usepackage{biblio}
  \usepackage{mytooltip}
  ```
- With the package `biblio.sty`, use
  ```latex
  \addbibresource{YOUR_BIB_FILE_NAME.bib}
  ```
  in the preambule, and
  ```latex
  \printbibliography
  ```
  where you want the bibliography to be printed.

### Step 2: Run main.py

Before compiling your LaTeX file, run `main.py`. This script scans all `.tex` files in the current directory to retrieve equations and the first `.bib` file found in the directory. It then extracts the content of the equations and citations and stores them in `equations.txt` and `citations.txt`, respectively.

```batch
python main.py
```

#### Important Notes:

- Re-run `main.py` each time you want to refresh `equations.txt` and `citations.txt`.
- The `main.py` file is easily editable to target a specific `.tex` or `.bib` file (see....).

### Step 3: Compile Your LaTeX File

Compile your LaTeX file as usual. The commands affected by `mytooltip.sty` are `\eqref` and `\cite`.

Examples in images:

- The following code:
  ```latex
  \begin{equation}\label{EqFacile}
  1+1=2
  \end{equation}
  The ref \eqref{EqFacile}.
  ```
  gives
  <br>
  ![demo](https://github.com/Samuel-Treton/LaTeX_auto_tooltip/blob/main/eqref_demo.png)