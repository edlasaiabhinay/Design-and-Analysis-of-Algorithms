try:
    n = int(input("Enter matrix size (n): "))
    matrix = [[i * n + j + 1 for j in range(n)] for i in range(n)]

    print("Generated matrix:")
    for row in matrix:
        print(row)

    i = int(input(f"Enter row index (0-{n-1}): "))
    j = int(input(f"Enter column index (0-{n-1}): "))

    if 0 <= i < n and 0 <= j < n:
        print(f"Value at ({i},{j}): {matrix[i][j]}")
    else:
        print("Invalid indices!")
except ValueError:
    print("Please enter valid numbers")
