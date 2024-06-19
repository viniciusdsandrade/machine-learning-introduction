import math
import random


def generate_distances(coordinates):
    n = len(coordinates)
    distances = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            distances[i][j] = distance_between_two_points(coordinates[i], coordinates[j])
    return distances


def generate_random_coordinates_within_defined_interval(min, max, n_cities):
    if n_cities < 2 or n_cities > 10000:
        raise ValueError("O número de cidades deve ser entre 2 e 50.")

    coordinates = []
    for i in range(n_cities):
        x = random.randint(min, max)
        y = random.randint(min, max)
        coordinates.append((x, y))
    return coordinates


def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def held_karp_tsp(distances):
    n = len(distances)
    memo = {}

    # Recursive function that returns the minimum cost of visiting all cities and the path taken
    def tsp(mask, current):
        if mask == (1 << n) - 1:  # All cities have been visited
            return distances[current][0], [current]  # Return to the starting point
        if (mask, current) in memo:  # Check if this state has been calculated before
            return memo[(mask, current)]

        min_cost = float('inf')
        min_path = []
        for city in range(n):
            if mask & (1 << city) == 0:  # If the city has not been visited yet
                new_mask = mask | (1 << city)  # Update the mask
                cost, path = tsp(new_mask, city)
                cost += distances[current][city]
                if cost < min_cost:
                    min_cost = cost
                    min_path = path + [current]

        memo[(mask, current)] = min_cost, min_path
        return min_cost, min_path

    return tsp(1, 0)  # Start at the starting point


def test_held_karp_tsp():
    min_coordinate = 0
    max_coordinate = 100
    n_cities = 5

    # max 996! = 4.0481167966e+2555

    # 15! = 1.307674368e+12
    # 16! = 2.0922789888e+13
    # 17! = 3.55687428096e+14
    # 18! = 6.402373705728e+15
    # 19! = 1.21645100408832e+17
    # 20! = 2.43290200817664e+18
    # ...
    # 1558! = 2.4248584012e+4299

    coordinates = generate_random_coordinates_within_defined_interval(min_coordinate, max_coordinate,
                                                                      n_cities)  # Generate the coordinates of the cities
    distances = generate_distances(coordinates)  # Calculate the distances between the cities
    optimal_distance, optimal_path = held_karp_tsp(distances)  # Find the optimal distance using the Held-Karp algorithm

    print("City coordinates:", coordinates)  # Print the coordinates of the cities in list format
    print(f"Minimum total distance: {optimal_distance:.3f}")  # Print the minimum distance found

    # Print the coordinates of the cities in the order they are visited
    optimal_coordinates = [coordinates[i] for i in optimal_path]
    print("Coordinates in  order they are visited:", optimal_coordinates)


if __name__ == "__main__":
    test_held_karp_tsp()
