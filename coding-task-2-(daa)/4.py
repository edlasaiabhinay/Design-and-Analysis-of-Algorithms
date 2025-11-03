def ts_bruteforce(dis_matrix):
    # Total number of cities
    num_cities = len(dis_matrix)

    # Create a list of city numbers: [0, 1, 2, ..., n-1]
    cities = list(range(num_cities))

    # Function to get all possible orders (permutations)
    def get_permutations(items):
        if len(items) == 1:
            return [items]
        all_orders = []
        for i in range(len(items)):
            first = items[i]
            rest = items[:i] + items[i+1:]
            for order in get_permutations(rest):
                all_orders.append([first] + order)
        return all_orders

    # Start from city 0
    start_city = 0
    other_cities = cities[1:]

    shortest_path = []
    shortest_distance = float('inf')

    # Try every possible order of visiting other cities
    for order in get_permutations(other_cities):
        path = [start_city] + order + [start_city]  # round trip
        total = 0
        for i in range(len(path) - 1):
            total += dis_matrix[path[i]][path[i + 1]]
        if total < shortest_distance:
            shortest_distance = total
            shortest_path = path

    return shortest_path, shortest_distance

# Distance between cities (matrix)
dis_matrix = [
    [0, 3, 8, 2, 5],
    [4, 0, 7, 6, 3],
    [6, 5, 0, 4, 2],
    [3, 6, 7, 0, 4],
    [5, 2, 6, 3, 0]

]

# Run the function
best_path, min_distance = ts_bruteforce(dis_matrix)

# Show result
print("Shortest Path:", best_path)
print("Minimum Distance:", min_distance)

#In this program, I solve the TSP by checking every possible 
# route that visits all cities and returns to the starting point.
# I use permutations to generate all possible orders of visiting the cities. 
# For each route, I calculate the total distance using the distance matrix. 
# Then I compare all routes and pick the one with the shortest total distance. 
# It’s a brute force method, so it’s simple but slow when the number of cities increases.

#I fix the starting city as 0, then generate all permutations of the remaining cities.
# I add the starting city at the beginning and end to make it a round trip. 
# Then I loop through each path, calculate the total distance, and keep track of the shortest one.