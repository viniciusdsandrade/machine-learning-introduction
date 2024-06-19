import math
import random
import numpy as np


coordinates = [(0, 0), (2, 0), (1, 0), (3, 0)]


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


def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def distance_between_two_points_2(p1, p2):
    return math.dist(p1, p2)


def distance_between_two_points_np(p1, p2):
    return np.linalg.norm(np.array(p1) - np.array(p2))


def nearest_neighbor_tour_with_coordinate_and_indices(coordenadas):
    n_cities = len(coordenadas)
    tour_indices = [0]
    tour_coordinates = [coordenadas[0]]  # Inicia na cidade inicial
    unvisited_cities = list(range(1, n_cities))

    while unvisited_cities:
        next_city = min(unvisited_cities,
                        key=lambda candidate: distance_between_two_points(coordenadas[tour_indices[-1]],
                                                                          coordenadas[candidate]))
        tour_indices.append(next_city)
        tour_coordinates.append(coordenadas[next_city])
        unvisited_cities.remove(next_city)

    return tour_indices, tour_coordinates


def total_distance_of_coordinate_tour(coordenadas):
    tour_indices, _ = nearest_neighbor_tour_with_coordinate_and_indices(coordenadas)
    total_distance = 0
    for i in range(len(tour_indices) - 1):
        total_distance += distance_between_two_points(coordenadas[tour_indices[i]], coordenadas[tour_indices[i + 1]])
    total_distance += distance_between_two_points(coordenadas[tour_indices[-1]],
                                                  coordenadas[
                                                      tour_indices[0]])  # add distance from last city to first city
    return round(total_distance, 3)


def test_nearest_neighbor_algorithm_com_coordenadas():
    min = 0
    max = 100

    coordenadas = generate_random_coordinates_within_defined_interval(min, max, 10)
    # coordenadas = [(0, 0), (2, 0), (1, 0), (3, 0)]
    tour_indices, tour_coordinate = nearest_neighbor_tour_with_coordinate_and_indices(coordenadas)

    print("Coordenadas Geradas:       ", coordenadas)
    print("Tour indices:              ", tour_indices)
    print("Tour das coordenadas:      ", tour_coordinate)
    print("Distância total:           ", total_distance_of_coordinate_tour(coordenadas))


def main():
    print("\nTesting nearest neighbor algorithm com coordenadas")
    test_nearest_neighbor_algorithm_com_coordenadas()


if __name__ == "__main__":
    main()
