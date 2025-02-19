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
    matrixFile1 = input("Enter the path for the first matrix: ")
    matrixFile2 = input("Enter the path for the second matrix: ")

    # Create SparseMatrix objects
    try:
        matrix1 = SparseMatrix(matrixFilePath=matrixFile1)
        matrix2 = SparseMatrix(matrixFilePath=matrixFile2)
    except Exception as e:
        print(f"Error loading matrices: {e}")
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
