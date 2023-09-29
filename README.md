# LaTeX_auto_tooltip

## Description

`LaTeX_auto_tooltip` is a project that allows equations and citation references to appear as pop-ups in Adobe Reader. When the reader hovers over an equation or citation reference in a PDF generated from LaTeX, a contextual pop-up window displays additional information.

![demo](https://github.com/Samuel-Treton/LaTeX_auto_tooltip/blob/main/auto_tooltip_demo.gif)

## Features

- Pop-up display for LaTeX equations
- Pop-up display for citation references

## Prerequisites

Make sure you have Python installed on your computer. If not, you can download it from [Python's official website](https://www.python.org/downloads/).

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
Note that \begin{equation}\label{XXX} must be on the same line.
