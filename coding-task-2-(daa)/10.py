# Karatsuba multiplication: fast way to multiply big numbers
def karatsuba(x, y):
    # If either number is small, just multiply normally
    if x < 10 or y < 10:
        return x * y

    # Step 1: Find the length of the bigger number
    n = max(len(str(x)), len(str(y)))
    half = n // 2  # Split roughly in half

    # Step 2: Break each number into two parts
    # Example: 1234 → high=12, low=34
    high_x, low_x = divmod(x, 10**half)
    high_y, low_y = divmod(y, 10**half)

    # Step 3: Do three multiplications
    z0 = karatsuba(low_x, low_y)                      # low × low
    z1 = karatsuba(low_x + high_x, low_y + high_y)    # (low + high) × (low + high)
    z2 = karatsuba(high_x, high_y)                    # high × high

    # Step 4: Combine the results using Karatsuba's trick
    return (z2 * 10**(2 * half)) + ((z1 - z2 - z0) * 10**half) + z0

print("Fast Multiplication using Karatsuba Algorithm")
num1 = int(input("Enter the first large number: "))
num2 = int(input("Enter the second large number: "))

# Multiply and show result
result = karatsuba(num1, num2)
print(f"\nResult: {num1} × {num2} = {result}")
