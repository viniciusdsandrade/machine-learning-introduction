import random
import math

n_cities = 17

distances = [
    [0, 548, 776, 696, 582, 274, 502, 194, 308, 194, 536, 502, 388, 354, 468, 776, 662],
    [548, 0, 684, 308, 194, 502, 730, 354, 696, 742, 1084, 594, 480, 674, 1016, 868, 1210],
    [776, 684, 0, 992, 878, 502, 274, 810, 468, 742, 400, 1278, 1164, 1130, 788, 1552, 754],
    [696, 308, 992, 0, 114, 650, 878, 502, 844, 890, 1232, 514, 628, 822, 1164, 560, 1358],
    [582, 194, 878, 114, 0, 536, 764, 388, 730, 776, 1118, 400, 514, 708, 1050, 674, 1244],
    [274, 502, 502, 650, 536, 0, 228, 308, 194, 240, 582, 776, 662, 628, 514, 1050, 708],
    [502, 730, 274, 878, 764, 228, 0, 536, 194, 468, 354, 1004, 890, 856, 514, 1278, 480],
    [194, 354, 810, 502, 388, 308, 536, 0, 342, 388, 730, 468, 354, 320, 662, 742, 856],
    [308, 696, 468, 844, 730, 194, 194, 342, 0, 274, 388, 810, 696, 662, 320, 1084, 514],
    [194, 742, 742, 890, 776, 240, 468, 388, 274, 0, 342, 536, 422, 388, 274, 810, 468],
    [536, 1084, 400, 1232, 1118, 582, 354, 730, 388, 342, 0, 878, 764, 730, 388, 1152, 354],
    [502, 594, 1278, 514, 400, 776, 1004, 468, 810, 536, 878, 0, 114, 308, 650, 274, 844],
    [388, 480, 1164, 628, 514, 662, 890, 354, 696, 422, 764, 114, 0, 194, 536, 388, 730],
    [354, 674, 1130, 822, 708, 628, 856, 320, 662, 388, 730, 308, 194, 0, 342, 422, 536],
    [468, 1016, 788, 1164, 1050, 514, 514, 662, 320, 274, 388, 650, 536, 342, 0, 764, 194],
    [776, 868, 1552, 560, 674, 1050, 1278, 742, 1084, 810, 1152, 274, 388, 422, 764, 0, 798],
    [662, 1210, 754, 1358, 1244, 708, 480, 856, 514, 468, 354, 844, 730, 536, 194, 798, 0],
]


# Como faço para adicionar a distância em formato de circulo?
def get_total_distance(tour: list):
    total_distance = 0
    for i in range(1, len(tour)):
        total_distance += distances[tour[i - 1]][tour[i]]
    return total_distance + distances[tour[-1]][tour[0]]


def nearest_neighbor_algorithm(distances, n_cities):
    tour = [0]
    unvisited_cities = list(range(1, n_cities))  # Lista com 17 elementos

    while unvisited_cities:
        next = min(unvisited_cities, key=lambda candidate: distances[tour[-1]][candidate])
        tour.append(next)
        unvisited_cities.remove(next)

    return tour


def nearest_neighbor_algorithm_estocastic(distances, n_cities):
    first_city = random.choice(range(n_cities))
    tour = [first_city]
    unvisited_cities = list(range(n_cities))
    unvisited_cities.remove(first_city)

    while unvisited_cities:
        next = min(unvisited_cities, key=lambda candidate: distances[tour[-1]][candidate])
        tour.append(next)
        unvisited_cities.remove(next)

    return tour


def main():
    n_cities = len(distances)
    tour = nearest_neighbor_algorithm(distances, n_cities)
    print()
    total_distance = get_total_distance(tour)
    print(f"The tour is: {tour}")
    print(f"The total distance of the tour is: {total_distance}")

    tour = nearest_neighbor_algorithm_estocastic(distances, n_cities)
    total_distance = get_total_distance(tour)
    print()
    print(f"The tour is: {tour}")
    print(f"The total distance of the tour is: {total_distance}")

    # quero fazer um algoritmo que rode 100 vezes e me retorne o menor valor de distância
    n_cities = len(distances)
    distance_set = set()
    tour_dict = {}

    for i in range(1000):
        tour = nearest_neighbor_algorithm_estocastic(distances, n_cities)
        total_distance = get_total_distance(tour)
        distance_set.add(total_distance)
        tour_dict[total_distance] = tour

    min_distance = min(distance_set)
    best_tour = tour_dict[min_distance]
    print()
    print(f"The best tour is: {best_tour}")
    print(f"The total distance of the best tour is: {min_distance}")

    n_cities = len(distances)
    n = 50  # n% do tour será composto por escolhas aleatórias de cidade

    tour = nearest_neighbor_algorithm_2(distances, n_cities, n)
    total_distance = get_total_distance(tour)
    print()
    print(f"The tour is: {tour}")
    print(f"The total distance of the tour is: {total_distance}")

    # quero fazer um algoritmo que rode 100 vezes e me retorne o menor valor de distância
    distance_set = set()
    tour_dict = {}

    for i in range(1000):
        tour = nearest_neighbor_algorithm_2(distances, n_cities, n)
        total_distance = get_total_distance(tour)
        distance_set.add(total_distance)
        tour_dict[total_distance] = tour

    min_distance = min(distance_set)
    best_tour = tour_dict[min_distance]

    print()
    print(f"The best tour is: {best_tour}")
    print(f"The total distance of the best tour is: {min_distance}")


# Quero fazer uma função n% (que vai de 0 a 100% no maximo e o usuario vai passar numeros de 0 a 100)
# parte do tour a partir do inicio seja composto por escolhas aleatórias
# e partir de n% + 1 o qual o usuario vai passar, seja feito pelo algoritmo do vizinho mais próximo
def nearest_neighbor_algorithm_2(distances, n_cities, n):
    if n < 0 or n > 100:
        raise ValueError("n must be between 0 and 100")

    n_random_cities = math.floor(n_cities * n / 100)  # Calcula o número de cidades a serem selecionadas aleatoriamente

    tour = random.sample(range(n_cities), n_random_cities)  # Seleciona aleatoriamente n_random_cities cidades
    unvisited_cities = [city for city in range(n_cities) if city not in tour]  # Lista de cidades não visitadas

    while unvisited_cities:
        next = min(unvisited_cities, key=lambda candidate: distances[tour[-1]][candidate])
        tour.append(next)
        unvisited_cities.remove(next)

    return tour


if __name__ == "__main__":
    main()
