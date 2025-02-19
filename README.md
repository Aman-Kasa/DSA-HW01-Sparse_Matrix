![Sparse Matrix](https://cdn.educba.com/academy/wp-content/uploads/2021/05/Sparse-Matrix-in-Python.jpg)
# Sparse Matrix Operations

This project provides a Python implementation for performing operations on sparse matrices. The main operations supported are addition, subtraction, and multiplication of sparse matrices.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Examples](#examples)
- [Contributing](#contributing)
- [License](#license)

## Introduction

Sparse matrices are matrices in which most of the elements are zero. This project provides a way to efficiently store and perform operations on such matrices.

## Features

- Load sparse matrices from files.
- Perform addition, subtraction, and multiplication of sparse matrices.
- Output the result of operations to the console.

## Installation

To clone and run this project, you'll need [Git](https://git-scm.com) and [Python](https://www.python.org/downloads/) installed on your computer. From your command line:

```bash
# Clone this repository
$ git clone https://github.com/Aman-Kasa/DSA-HW01-Sparse_Matrix.git

# Go into the repository
$ cd DSA-HW01-Sparse_Matrix

# Install dependencies (if any)
$ pip install -r requirements.txt


                            Usage
To use this project, you need to provide two sparse matrix files. The files should contain the number of rows and columns, followed by the non-zero elements in the format (row_index, column_index, value).

Run the main script:
$ python dsa/sparse_matrix/code/src/main.py

You will be prompted to enter the paths for the two matrix files and the operation (add, subtract, multiply) you want to perform.



#Examples
Example of a sparse matrix file format (matrix1.txt):

rows=4035
cols=3018
(0, 324, 593)
(0, 934, 273)
...

Example of running the script:

$ python dsa/sparse_matrix/code/src/main.py
Enter the path for the first matrix: dsa/sparse_matrix/sample_inputs/matrix1.txt
Enter the path for the second matrix: dsa/sparse_matrix/sample_inputs/matrix2.txt
Enter the operation (add, subtract, multiply): add

Result of addition:
(0, 324, 1186)
(0, 934, 546)
...

Contributing
Contributions are welcome! Please feel free to submit a Pull Request   // ✌🏿✌🏿 //

Acknowledgments
I would like to thank:

---->>>Mr. Waka for his guidance and support throughout this project.
---->>>ChatGPT for assistance with code suggestions and documentation.
