# Function to take matrix input from user
def get_matrix(rows, cols, name):
    print(f"\nEnter values for {name} matrix ({rows} x {cols}):")
    matrix = []
    for i in range(rows):
        while True:
            row = input(f"Row {i+1}: ").split()
            if len(row) == cols:
                matrix.append([int(x) for x in row])
                break
            else:
                print(f"Please enter exactly {cols} numbers.")
    return matrix

# Function to multiply two matrices
def multiply(A, B):
    rows_A, cols_A = len(A), len(A[0])
    rows_B, cols_B = len(B), len(B[0])

    if cols_A != rows_B:
        print("\nMultiplication not possible: columns of A ≠ rows of B")
        return None

    # Create result matrix with zeros
    result = [[0] * cols_B for _ in range(rows_A)]

    # Multiply
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result

# Main program
print(" Matrix Multiplication Program")

# Get matrix sizes
r1 = int(input("Enter rows for Matrix A: "))
c1 = int(input("Enter columns for Matrix A: "))
r2 = int(input("Enter rows for Matrix B: "))
c2 = int(input("Enter columns for Matrix B: "))

# Get matrix values
A = get_matrix(r1, c1, "A")
B = get_matrix(r2, c2, "B")

# Multiply and show result
result = multiply(A, B)
if result:
    print("\nResult of A × B:")
    for row in result:
        print(row)