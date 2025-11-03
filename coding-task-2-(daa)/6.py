def knapsack_brute_force(weights, values, capacity):
    n = len(weights)  # Number of items
    best_value = 0    # Track the highest value found
    best_items = []   # Track the best item combination

    # Try all possible combinations (2^n)
    for i in range(2 ** n):
        # Convert number to binary string (e.g., '010101')
        binary = bin(i)[2:].zfill(n)

        total_weight = 0
        total_value = 0
        selected_items = []

        # Check which items are selected in this combination
        for j in range(n):
            if binary[j] == '1':
                total_weight += weights[j]
                total_value += values[j]
                selected_items.append(j + 1)  # Use 1-based indexing

        # If within capacity and better value, update best
        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_items = selected_items

    return best_items, best_value


# Example with 6 items
weights = [1,4,3,5,2]
values = [10,40,30,50,20] 
capacity = 7

result_items, result_value = knapsack_brute_force(weights, values, capacity)

print("Best items to pick:", result_items)
print("Maximum value:", result_value)