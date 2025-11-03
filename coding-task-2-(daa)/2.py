def get_combinations(items, r): #r- how many iteams to choose
    if r == 0: #if ) then there is only one combination
        return [[]]
    if r > len(items): #impossible to choose more items than i have
        return []

    # Include the first item
    with_first = get_combinations(items[1:], r - 1)
    for com in with_first:
        com.insert(0, items[0])

    # Exclude the first item
    without_first = get_combinations(items[1:], r)

    # Combine both
    return with_first + without_first

# Try with numbers
print("Combinations of [1, 2, 3] taking 2:")
for c in get_combinations([1, 2, 3], 2):
    print(c)

# Try with letters
print("\nCombinations of 'XYZ' taking 2:")
for c in get_combinations(list("XYZ"), 2):
    print(''.join(c))
