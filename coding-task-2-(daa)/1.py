def get_permutations(items):
   # If there's only one item, return it as the only permutation
    if len(items)==1:     
        return [items]
    all_per=[] #it will hold all the permuttions

    # loop through each item in list
    for i in range(len(items)):
        #pick one 
        first=items[i]
        # get the rest of the items
        rest = items[:i] + items[i+1:]
        # Get all permutations of the rest
        for per in get_permutations(rest):
            # Add the picked item to the front of each smaller permutation
            all_per.append([first] + per)

    return all_per

#using a list
print("Permutations of [3, 4, 5]:")
for p in get_permutations([3, 4, 5]):
    print(p)

#using a string
print("\nPermutations of 'XYZ':")
for p in get_permutations(list("XYZ")):
    print(''.join(p))