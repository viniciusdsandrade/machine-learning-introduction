import matplotlib.pyplot as plt
import math
import random
import time


# Função para calcular a distância euclidiana entre dois pontos
def distance_between_two_points(p1, p2):
    return math.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


# Função para calcular a distância euclidiana entre dois pontos
def distance_between_two_points_2(p1, p2):
    return math.dist(p1, p2)


def n_tsp(coords, num_viajantes):
    """
    Held–Karp algorithm: https://en.wikipedia.org/wiki/Held%E2%80%93Karp_algorithm
    Algoritmo baseado em Programação Dinâmica com Memoização para resolver o Problema do Caixeiro Viajante (TSP).

    Params:
        coords (list): Lista de coordenadas das cidades a serem visitadas.
        num_viajantes (int): Número de viajantes ou agentes que devem visitar todas as cidades.

    Returns:
        list: Lista de rotas para os viajantes, cada rota representada como uma lista de índices de cidades.
              Cada rota inclui a cidade de partida no final para completar o ciclo.
    """

    n = len(coords)
    # Calcula as distâncias entre todas as coordenadas
    distancias = [[distance_between_two_points(coords[i], coords[j]) for j in range(n)] for i in range(n)]

    memo = {}  # Dicionário para memoização dos resultados

    # Função recursiva que retorna o custo mínimo de visitar todas as cidades e o caminho percorrido
    def tsp(mascara, atual):
        # Caso base: todas as cidades foram visitadas
        if mascara == (1 << n) - 1:
            return distancias[atual][0], [0]  # Retorna ao ponto de partida (0,0)
        # Verifica se este estado já foi calculado antes
        if (mascara, atual) in memo:
            return memo[(mascara, atual)]

        custo_minimo = float('inf')  # Inicializa o custo mínimo como infinito
        caminho_minimo = []  # Inicializa o caminho mínimo como uma lista vazia
        # Percorre todas as cidades
        for cidade in range(n):
            # Se a cidade ainda não foi visitada
            if mascara & (1 << cidade) == 0:
                # Atualiza a máscara indicando que a cidade atual foi visitada
                nova_mascara = mascara | (1 << cidade)
                # Chama recursivamente a função tsp para a próxima cidade
                custo, caminho = tsp(nova_mascara, cidade)
                # Calcula o custo total incluindo a distância entre as cidades
                custo += distancias[atual][cidade]
                # Verifica se este caminho é o mais barato até agora
                if custo < custo_minimo:
                    custo_minimo = custo
                    caminho_minimo = caminho + [cidade]

        memo[(mascara, atual)] = custo_minimo, caminho_minimo  # Armazena o resultado no dicionário memo
        return custo_minimo, caminho_minimo

    # Encontra a rota ótima para um viajante chamando a função tsp com as cidades a partir do ponto de partida (0)
    custo, caminho = tsp(1, 0)

    # Distribui as cidades igualmente entre os viajantes
    num_cidades_por_viajante = n // num_viajantes
    rotas = []
    for i in range(num_viajantes):
        indice_inicio = i * num_cidades_por_viajante  # Indice de inicio da rota
        indice_fim = indice_inicio + num_cidades_por_viajante  # Indice de fim da rota
        rota = caminho[indice_inicio:indice_fim] + [0]  # Rota do viajante com retorno ao ponto de partida
        rotas.append(rota)  # Adiciona a rota à lista de rotas

    return rotas


# Função para gerar coordenadas aleatórias dentro de um intervalo definido
def generate_random_coordinates(min, max, n_cities):
    # Verificar se o número de cidades é pelo menos 2
    if n_cities < 2:
        raise ValueError("The number of cities must be at least 2")

    # Verificar se o valor mínimo é maior que o valor máximo
    if min >= max:
        raise ValueError("The minimum value must be less than the maximum value")

    # Verifica se o numero de cidades é maior que o o quadrado da diferença entre o valor máximo e mínimo
    if n_cities > (max - min) ** 2:
        raise ValueError("The number of cities is too large for the given interval")

    coordinates = [(0, 0)]  # A primeira coordenada é (0,0)
    for i in range(n_cities - 1):  # Gera n_cities - 1 coordenadas aleatórias
        x = random.randint(min, max)
        y = random.randint(min, max)
        coordinates.append((x, y))
    return coordinates


# Função para calcular a distância de uma lista de coordenadas que representam as  localizações das cidades
# (tour) em ordem. Não considera a distancia da ultima cidade para o inicio pois o tsp já faz isso
def calculate_total_distance(coords):
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += distance_between_two_points_2(coords[i], coords[i + 1])
    return total_distance


# Função que retorna as coordenadas das cidades a partir de uma lista de índices de cidades de um tour
def get_coords_from_tour(tour, coords):
    return [coords[i] for i in tour]


# Função para plotar as rotas dos caixeiros viajantes em um gráfico 2D
def plot_tsp(coords, routes):
    plt.figure(figsize=(8, 6))
    for i, route in enumerate(routes):
        route_coords = [coords[idx] for idx in route]
        route_coords.append(route_coords[0])  # Para fechar o ciclo
        x_coords = [coord[0] for coord in route_coords]
        y_coords = [coord[1] for coord in route_coords]
        plt.plot(x_coords, y_coords, marker='o', label=f'Rota {i + 1}')

    plt.scatter([coord[0] for coord in coords], [coord[1] for coord in coords], color='red', label='Pontos de parada')
    plt.xlabel('Coordenada X')
    plt.ylabel('Coordenada Y')
    plt.title('Rotas dos Caixeiros Viajantes')
    plt.legend()
    plt.grid(True)
    plt.show()


# Execução de um teste para o algoritmo n-tsp
def run_tests():
    min = 0
    max = 100
    num_cities = 10
    total = 0

    # Gerar coordenadas aleatórias dentro do intervalo definido
    coordinates = generate_random_coordinates(min, max, num_cities)
    # coordinates = [(0, 0), (0, 2), (2, 0), (2, 2), (1, 1), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8), (9, 9)]

    # Número de viajantes
    num_travelers = 1

    # Executar o algoritmo n-tsp
    start_time = time.time()
    tour = n_tsp(coordinates, num_travelers)
    end_time = time.time()
    interval = end_time - start_time

    print(f"Número de viajantes: {num_travelers}")
    print(f"Número de cidades:   {num_cities}")
    print(f"Coordenadas:         {coordinates}")
    print(f"Indices das rotas    {tour}")
    print(f"Tempo de execução:   {interval:.6f} segundos")

    # Exibir as rotas e as distâncias totais para cada viajante
    for i, route in enumerate(tour):
        tour_coordinates = get_coords_from_tour(tour[i], coordinates)
        print(f"Rota para viajante {i + 1}: {route}")
        distance = calculate_total_distance([coordinates[i] for i in route])
        print(f"Coordenadas da rota: {tour_coordinates}")
        rounded_distance = round(distance, 3)  # Arredonda para 3 casas decimais
        print(f"Distância total: {rounded_distance}")
        total += rounded_distance

    total = round(total, 3)  # Arredonda o total para 3 casas decimais
    print(f"Distância total de todos os viajantes: {total}")

    # Plotar as rotas encontradas
    # plot_tsp(coordinates, tour)


def main():
    run_tests()


if __name__ == "__main__":
    main()
