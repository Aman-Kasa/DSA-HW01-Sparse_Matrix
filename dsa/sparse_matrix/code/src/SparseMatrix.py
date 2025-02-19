class SparseMatrix:
    def __init__(self, matrixFilePath=None, numRows=0, numCols=0):
        self.matrix = {}
        if matrixFilePath:
            self.read_matrix_from_file(matrixFilePath)
        elif numRows > 0 and numCols > 0:
            self.numRows = numRows
            self.numCols = numCols

    def read_matrix_from_file(self, matrixFilePath):
        try:
            with open(matrixFilePath, 'r') as file:
                lines = file.readlines()

            # Debugging print to check file content
            print("Lines read from file:", lines)

            # Check for correct file format (at least two lines for rows and cols)
            if len(lines) < 2:
                raise ValueError("File format is incorrect. Missing rows or cols information.")

            # Read the number of rows and columns from the first two lines
            row_line = lines[0].strip()
            col_line = lines[1].strip()

            # Debugging to check the first two lines
            print(f"Row line: {row_line}, Col line: {col_line}")

            # Make sure the lines are in the expected format
            if not row_line.startswith("rows=") or not col_line.startswith("cols="):
                raise ValueError("File format is incorrect. Expected 'rows=<number>' and 'cols=<number>' in the first two lines.")
            
            self.numRows = int(row_line.split('=')[1].strip())
            self.numCols = int(col_line.split('=')[1].strip())

            # Now process the matrix values (from line 3 onwards)
            for line in lines[2:]:
                # Remove any extra spaces and ensure it's a valid line
                line = line.strip()
                if line and line.startswith("(") and line.endswith(")"):
                    try:
                        # Extract the row, column, and value from the string
                        row_col_val = line[1:-1].split(",")  # Remove the parentheses and split by comma
                        row = int(row_col_val[0].strip())
                        col = int(row_col_val[1].strip())
                        value = int(row_col_val[2].strip())

                        # Store in matrix
                        self.setElement(row, col, value)

                    except ValueError as e:
                        print(f"Error parsing line '{line}': {e}")
                        raise ValueError("Matrix entry is not in the correct format.")
                else:
                    if line:  # Only print ignored if the line is not empty
                        print(f"Ignored invalid line: {line}")

        except Exception as e:
            print(f"Error reading matrix from file: {e}")
            raise

    def getElement(self, row, col):
        """ Returns the value at (row, col), or 0 if not present """
        return self.matrix.get((row, col), 0)

    def setElement(self, row, col, value):
        """ Sets the value at (row, col) """
        self.matrix[(row, col)] = value

    def add(self, other):
        """ Adds two sparse matrices """
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for addition")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        
        # Add corresponding elements from both matrices
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value + other.getElement(row, col))
        return result

    def subtract(self, other):
        """ Subtracts two sparse matrices """
        if self.numRows != other.numRows or self.numCols != other.numCols:
            raise ValueError("Matrix dimensions must match for subtraction")
        result = SparseMatrix(numRows=self.numRows, numCols=self.numCols)
        
        # Subtract corresponding elements from both matrices
        for (row, col), value in self.matrix.items():
            result.setElement(row, col, value - other.getElement(row, col))
        return result

    def multiply(self, other):
        """ Multiplies two sparse matrices """
        if self.numCols != other.numRows:
            raise ValueError("Matrix dimensions must match for multiplication")
        
        result = SparseMatrix(numRows=self.numRows, numCols=other.numCols)
        
        # Matrix multiplication logic: multiply corresponding elements and sum
        for (row, col), value in self.matrix.items():
            for k in range(other.numCols):
                result.setElement(row, k, result.getElement(row, k) + value * other.getElement(col, k))
        return result
