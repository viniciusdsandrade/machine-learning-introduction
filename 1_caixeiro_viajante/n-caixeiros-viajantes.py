import math
import random


# Relatório do projeto
# 1 - Introdução ao problema
# 2 - Qual heuristica estou criando?
# 3 - Resultados


# Entrega - 03/05/2023 23:59 - githubClassRoom (Até 3 dias após o prazo)

# O objetivo da atividade é realizar uma solução genérica do problema do caixeiro viajante: No primeiro momento
# estudamos algumas heuristicas da resolução do problema com um apenas caixeiro viajante.

# Entretanto, nessa solução, devemos implementar uma solução para n caixeiros viajantes
# que o usuário irá informar.

# O desafio bonus é implementar uma heuristica diferente das estudadas em aula.

# O numero de caixeiros viajantes deverá ser necessariamente menor ou igual ao numero de cidades.
# Todos os caixeiros viajantes vão sair da mesma cidade

# Heuristica: Centróide, Vizinho mais próximo, Vizinho mais distânte


###############################################################
# Pensar em uma função

def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def distance_between_two_points_2(p1, p2):
    return math.dist(p1, p2)


def total_distance_of_coordinate_tour(coordenadas):
    tour_indices, _ = n_traveling_salesman_algorithm(1, coordenadas)
    total_distance = 0
    for i in range(len(tour_indices) - 1):
        total_distance += distance_between_two_points(coordenadas[tour_indices[i]], coordenadas[tour_indices[i + 1]])
    total_distance += distance_between_two_points(coordenadas[tour_indices[-1]],
                                                  coordenadas[
                                                      tour_indices[0]])  # add distance from last city to first city
    return round(total_distance, 3)


# Escrever um algoritmo que sorteie a quantidade de cidade entre a quantidade de caixeiros viajantes de maneira aleatória
# por exemplo: Tenho 4 caixeiros e 20 cidades, o primeiro pega 5, o segundo pega 4, o terceiro pega 6 e o quarto pega 5
def n_cities_per_salesman(n_caixeiros, n_cities):
    if n_caixeiros > n_cities:
        raise ValueError("The number of cities must be greater than or equal to the number of salesmen")

    cities_per_salesman = [0] * n_caixeiros
    remaining_cities = n_cities

    for i in range(n_caixeiros):
        if i == n_caixeiros - 1:
            cities_per_salesman[i] = remaining_cities
        else:
            # Distribuir aleatoriamente as cidades entre os caixeiros
            cities_per_salesman[i] = random.randint(1, remaining_cities - (n_caixeiros - i - 1))
            remaining_cities -= cities_per_salesman[i]

    return cities_per_salesman

def n_traveling_salesman_algorithm(n_caixeiros, coordenadas):
    n_cities = len(coordenadas)
    cities_per_salesman = n_cities_per_salesman(n_caixeiros, n_cities)

    tours_indices = []
    tours_coordinates = []

    for i in range(n_caixeiros):
        tour_indices = [0]
        tour_coordinates = [coordenadas[0]]  # Inicia na cidade inicial
        unvisited_cities = list(range(1, n_cities))

        while len(tour_indices) < cities_per_salesman[i]:
            next_city = min(unvisited_cities,
                            key=lambda candidate: distance_between_two_points(coordenadas[tour_indices[-1]],
                                                                              coordenadas[candidate]))
            tour_indices.append(next_city)
            tour_coordinates.append(coordenadas[next_city])
            unvisited_cities.remove(next_city)

        tours_indices.append(tour_indices)
        tours_coordinates.append(tour_coordinates)

    return tours_indices, tours_coordinates


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


def test_nearest_neighbor_algorithm_com_coordenadas():
    min = 0
    max = 100

    coordenadas = generate_random_coordinates_within_defined_interval(min, max, 10)
    tour_indices, tour_coordinate = n_traveling_salesman_algorithm(1, coordenadas)

    print("Coordenadas Geradas:       ", coordenadas)
    print("Tour indices:              ", tour_indices)
    print("Tour das coordenadas:      ", tour_coordinate)
    print("Distância total:           ", total_distance_of_coordinate_tour(coordenadas))


def main():
    n_caixeiros = 3
    coordenadas = [(0, 0), (1, 2), (3, 1), (2, 3), (4, 4)]
    tours_indices, tours_coordinates = n_traveling_salesman_algorithm(n_caixeiros, coordenadas)
    print("Indices dos caixeiros:", tours_indices)
    print("Coordenadas dos caixeiros:", tours_coordinates)


if __name__ == "__main__":
    main()
