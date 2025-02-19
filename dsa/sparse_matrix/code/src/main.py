#!/usr/bin/env python3
"""
Sparse Matrix Operations Script

This script allows users to load two sparse matrices from files and perform 
basic operations (addition, subtraction, and multiplication) on them.

Usage:
    Run the script and enter the file paths for two matrices when prompted. 
    Then, select an operation (add, subtract, multiply).

Requirements:
    - The `SparseMatrix` class must be implemented in `SparseMatrix.py`.

Author: AMAN KASA
Date: FEB 2025
"""
from SparseMatrix import SparseMatrix

def main():
    """
    The main entry point of the program.

    Prompts the user for two matrix file paths, loads the matrices, and performs
    an operation on them based on user input.

    Args:
        None

    Returns:
        None
    """    
    # Prompt for file paths
    matrix_file1 = input("Enter the path for the first matrix: ")
    matrix_file2 = input("Enter the path for the second matrix: ")

    # Create SparseMatrix objects
    try:
        matrix1 = SparseMatrix(matrixFilePath=matrix_file1)
        matrix2 = SparseMatrix(matrixFilePath=matrix_file2)
    except FileNotFoundError as e:
        print(f"Error loading matrices: file not found ({e})")
        return
    except ValueError as e:
        print(f"Error loading matrices: invalid file format ({e})")
        return
    except Exception as e:
        print(f"Error loading matrices: unexpected error ({e})")
        return    
  
    # Ask user for operation choice
    operation = input("Enter the operation (add, subtract, multiply): ").lower()

    if operation == "add":
        result = matrix1.add(matrix2)
        print("Result of addition:")
    elif operation == "subtract":
        result = matrix1.subtract(matrix2)
        print("Result of subtraction:")
    elif operation == "multiply":
        result = matrix1.multiply(matrix2)
        print("Result of multiplication:")
    else:
        print("Invalid operation.")
        return

    # Optionally, print result (or save to file)
    # Print non-zero elements
    for (row, col), value in result.matrix.items():
        print(f"({row}, {col}, {value})")

if __name__ == "__main__":
    main()
