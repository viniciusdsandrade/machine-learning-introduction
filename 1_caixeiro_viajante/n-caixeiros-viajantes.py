import math
import random


def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def distance_between_two_points_2(p1, p2):
    return math.dist(p1, p2)


def held_karp_tsp_multi(coords, num_travelers):
    n = len(coords)
    distances = [[distance_between_two_points(coords[i], coords[j]) for j in range(n)] for i in range(n)]

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

    # Find the optimal route for one traveler
    cost, path = tsp(1, 0)

    # Distribute the cities equally among the travelers
    num_cities_per_traveler = n // num_travelers
    routes = []
    for i in range(num_travelers):
        start_idx = i * num_cities_per_traveler
        end_idx = start_idx + num_cities_per_traveler
        route = path[start_idx:end_idx]
        route.append(0)  # Return to the starting point
        routes.append(route)

    return routes


def generate_random_coordinates_within_defined_interval(min, max, n_cities):
    if n_cities < 2:
        raise ValueError("The number of cities must be at least 2")

    if min >= max:
        raise ValueError("The minimum value must be less than the maximum value")

    if n_cities > (max - min) ** 2:
        raise ValueError("The number of cities is too large for the given interval")

    coordinates = []
    for i in range(n_cities):
        x = random.randint(min, max)
        y = random.randint(min, max)
        coordinates.append((x, y))
    return coordinates


# Essa formula não considera a distancia da ultima cidade para o inicio pois o tsp já faz isso
def calculate_total_distance(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += distance_between_two_points(coords[i], coords[i + 1])
    return total_distance


# Example usage:
def run_tests():
    min_interval = 0
    max_interval = 10
    num_cities = 15
    total = 0

    # Gerar coordenadas aleatórias dentro do intervalo definido
    coords = generate_random_coordinates_within_defined_interval(min_interval, max_interval, num_cities)

    # Número de viajantes
    num_travelers = 2

    # Executar o algoritmo TSP multi caixeiro-viajante
    routes = held_karp_tsp_multi(coords, num_travelers)
    print(f"Número de viajantes: {num_travelers}")
    print(f"Número de cidades: {num_cities}")
    print(f"Coordenadas: {coords}")
    print(f"routes", routes)

    # Exibir as rotas e as distâncias totais para cada viajante
    for i, route in enumerate(routes):
        print(f"Rota para viajante {i + 1}: {route}")
        distance = calculate_total_distance([coords[i] for i in route])
        rounded_distance = round(distance, 3)  # Arredonda para 3 casas decimais
        print(f"Distância total: {rounded_distance}")
        total += rounded_distance

    total = round(total, 3)  # Arredonda o total para 3 casas decimais
    print(f"Distância total de todos os viajantes: {total}")


def main():
    run_tests()


if __name__ == "__main__":
    main()
