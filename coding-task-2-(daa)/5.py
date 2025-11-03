# 0/1 Knapsack Problem using Brute Force
# Using binary representation for item selection
# Author: Karthik Mateti 🙂

def knapsack_bruteforce(weights, values, capacity):
    n = len(weights)
    max_value = 0
    best_combination = []

    # There are 2^n possible combinations of items
    for i in range(2 ** n):
        # Convert number to binary representation with n bits
        binary = bin(i)[2:].zfill(n)

        total_weight = 0
        total_value = 0
        combination = []

        # Calculate total weight and value for this combination
        for j in range(n):
            if binary[j] == '1':  # item is included
                total_weight += weights[j]
                total_value += values[j]
                combination.append(j + 1)  # item index (1-based)
        
        # Check if this combination fits within capacity
        if total_weight <= capacity and total_value > max_value:
            max_value = total_value
            best_combination = combination[:]

    return best_combination, max_value


# Example: 6 items
weights = [2, 3, 4, 5, 9, 7]   # weight of each item
values = [3, 4, 8, 8, 10, 6]   # value of each item
capacity = 15                   # maximum weight knapsack can hold

best_items, max_value = knapsack_bruteforce(weights, values, capacity)

print("Best combination of items:", best_items)
print("Maximum value:", max_value)