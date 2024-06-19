from itertools import permutations
import matplotlib.pyplot as plt
import random
import math


# Até n = 10 cidades (10! = 3.628.800 Três milhões Seiscentos e vinte e oito mil e oitocentos) o algoritmo de força
# bruta é viável Quero fazer uma funcao que descubra a menor distância entre as cidades pelo metodo de força bruta
def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


def generate_random_coordinates(min, max, n_cities):
    # Verificar se o número de cidades é pelo menos 2
    if n_cities < 2:
        raise ValueError("The number of cities must be at least 2")

    # Verificar se o valor mínimo é maior que o valor máximo
    if min >= max:
        raise ValueError("The minimum value must be less than the maximum value")

    # Verifica se o número de cidades é maior que o o quadrado da diferença entre o valor máximo e mínimo
    if n_cities > (max - min) ** 2:
        raise ValueError("The number of cities is too large for the given interval")

    coordinates = [(0, 0)]  # A primeira coordenada é (0,0)
    for i in range(n_cities - 1):  # Gera n_cities - 1 coordenadas aleatórias
        x = random.randint(min, max)
        y = random.randint(min, max)
        coordinates.append((x, y))
    return coordinates


def brute_force_traveling_salesman(coordinates):
    n_cities = len(coordinates)
    shortest_tour = None
    shortest_distance = float('inf')
    for tour in permutations(range(n_cities)):
        total_distance = sum(
            distance_between_two_points(coordinates[tour[i]], coordinates[tour[i + 1]]) for i in range(n_cities - 1))
        total_distance += distance_between_two_points(coordinates[tour[-1]],
                                                      coordinates[tour[0]])  # add distance from last city to first city
        if total_distance < shortest_distance:
            shortest_distance = total_distance
            shortest_tour = tour
    return shortest_tour, shortest_distance


def plot_tsp_solution(coordinates, tour):
    x = [coordinates[i][0] for i in tour]
    y = [coordinates[i][1] for i in tour]
    x.append(x[0])
    y.append(y[0])
    plt.plot(x, y, 'ro-')
    for i, txt in enumerate(tour):
        plt.annotate(txt, (coordinates[txt][0], coordinates[txt][1]))
    plt.title('Solução do Problema do Caixeiro Viajante')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.grid()
    plt.show()


def test_brute_force_traveling_salesman():
    min = 0
    max = 100
    n_cities = 10

    coordenadas = generate_random_coordinates(min, max, n_cities)
    # coordenadas = [(0, 0), (0, 2), (2, 0)]
    print(f"Coordenadas Geradas:       {coordenadas}")
    tour, distance = brute_force_traveling_salesman(coordenadas)
    print(f"Melhor tour:               {list(tour)}")
    print(f"Menor distância:           {distance:.3f}")

    plot_tsp_solution(coordenadas, tour)


def main():
    print("\nTesting nearest neighbor algorithm com coordenadas")
    test_brute_force_traveling_salesman()


if __name__ == "__main__":
    main()
