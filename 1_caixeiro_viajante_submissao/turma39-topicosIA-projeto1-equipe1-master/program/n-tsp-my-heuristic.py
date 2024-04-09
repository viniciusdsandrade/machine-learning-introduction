import time
import math
import re
import os


def distance_between_two_points_1(p1, p2):
    """
    Calcula a distância euclidiana entre dois pontos em um espaço 2D.

    Parâmetros:
    p1 (tupla): Uma tupla representando as coordenadas (x, y) do primeiro ponto.
    p2 (tupla): Uma tupla representando as coordenadas (x, y) do segundo ponto.

    Retorna:
    float: A distância euclidiana entre os dois pontos.
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def distance_between_two_points_2(p1, p2):
    """
    Calcula a distância euclidiana entre dois pontos em um espaço 2D.

    Parâmetros:
    p1 (tupla): Uma tupla representando as coordenadas (x, y) do primeiro ponto.
    p2 (tupla): Uma tupla representando as coordenadas (x, y) do segundo ponto.

    Retorna:
    float: A distância euclidiana entre os dois pontos.
    """
    return math.dist(p1, p2)


def n_tsp_my_heuristic(coords, num_viajantes):
    """
    Implementa uma heurística para o problema do caixeiro viajante.

    Parâmetros:
        coords (lista): Uma lista de coordenadas das cidades. Cada coordenada é uma tupla (x, y).
        num_viajantes (int): O número de viajantes.

    Retorna:
        rotas (lista): Uma lista de rotas para cada viajante. Cada rota é uma lista de índices das cidades.

    Descrição:
    A heurística determinística para o problema n-TSP funciona da seguinte maneira:

    Definição da Cidade de Origem:
        A primeira coordenada lida no arquivo é designada como a cidade de origem. Todos os carteiros
        iniciam e terminam suas rotas nesta cidade.

    Classificação das Cidades: Todas as cidades, exceto a de origem, são classificadas com base em sua distância da
    cidade de origem. A cidade mais próxima recebe o índice 1, a segunda mais próxima recebe o índice 2, e assim por
    diante, até a cidade mais distante, que recebe o índice n-1 onde n é o tamanho do vetor de coordenadas lido
    anteriormente. A cidade de origem é reservada com o índice 0.

    Distribuição das Cidades:
        As cidades são distribuídas igualmente entre  os carteiros. Se o número de cidades não for divisível pelo número
        de carteiros, as cidades restantes são distribuídas de forma circular entre eles.

    Finalização das Rotas: A cidade de origem é adicionada ao final da rota de cada carteiro, indicando que todos os
    carteiros devem retornar à cidade de origem ao concluir suas rotas.

    Exemplo:
        # Número de carteiros e cidades
        carteiros = 3
        cidades = 9

        # Coordenadas das cidades
        coordenadas = [(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6), (7, 7), (8, 8)]

        # A cidade de origem é a cidade 0. As cidades são classificadas e indexadas de acordo com a sua distância da
        cidade de origem. # A cidade 0 recebe o índice 0, a cidade 1 recebe o índice 1, a cidade 2 recebe o índice 2
        e assim sucessivamente.

        # A quantidade de cidades são distribuídas igualmente entre os carteiros.
        # Cada carteiro recebe indices de cidades de acordo com a sua ordem de classificação.
        # Carteiro 1: cidades 1, 2, 3
        # Carteiro 2: cidades 4, 5, 6
        # Carteiro 3: cidades 7, 8

        # O indice da cidade de origem é adicionada ao final de cada rota.
        rotas = [[0, 1, 2, 3, 0], [0, 4, 5, 6, 0], [0, 7, 8, 0]]

        # Rotas finais para cada carteiro (Indices das cidades)
        carteiro_1 = [0, 1, 2, 3, 0]
        carteiro_2 = [0, 4, 5, 6, 0]
        carteiro_3 = [0, 7, 8, 0]

        # Rotas finais para cada carteiro (Coordenadas das cidades)
        coordenadas_carteiro_1 = [(0, 0), (1, 1), (2, 2), (3, 3), (0, 0)]
        coordenadas_carteiro_2 = [(0, 0), (4, 4), (5, 5), (6, 6), (0, 0)]
        coordenadas_carteiro_3 = [(0, 0), (7, 7), (8, 8), (0, 0)]

        # Distância percorrida por cada carteiro
        distancia_carteiro_1 = 8.485
        distancia_carteiro_2 = 16.9706
        distancia_carteiro_3 = 22.6274

        # Distância total percorrida
        distancia_total = 48.0833
    """
    n = len(coords)
    # Calcula a distância entre todas as cidades
    distancias = [[distance_between_two_points_2(coords[i], coords[j]) for j in range(n)] for i in range(n)]

    # Lista de cidades a serem visitadas
    # Começa em 1 porque a cidade 0 é a inicial
    cidades_restantes = list(range(1, n))

    # Ordena as cidades restantes com base na distância até a origem
    cidades_restantes.sort(key=lambda x: distancias[0][x])

    # Inicializa as rotas dos viajantes: Todos os viajantes começam na cidade 0
    rotas = [[0] for _ in range(num_viajantes)]

    # Distribui as cidades igualmente entre os viajantes
    num_cidades_por_viajante = len(cidades_restantes) // num_viajantes
    for i in range(num_viajantes):
        for _ in range(num_cidades_por_viajante):
            rotas[i].append(cidades_restantes.pop(0))

    # Se houver cidades restantes, distribui-as para os viajantes
    i = 0
    while cidades_restantes:
        rotas[i % num_viajantes].append(cidades_restantes.pop(0))
        i += 1

    # Adiciona a cidade inicial ao final de cada rota: Todos os viajantes retornam à cidade 0
    for i in range(num_viajantes):
        rotas[i].append(0)

    return rotas


def get_coords_from_tour(tour, coords):
    """
    Obtém as coordenadas de cada cidade no tour.

    Parâmetros:
    tour (lista): Uma lista de índices de cidades representando o tour.
    coords (lista): Uma lista de tuplas onde cada tupla representa as coordenadas (x, y) de uma cidade.

    Retorna:
    lista: Uma lista de tuplas onde cada tupla representa as coordenadas (x, y) de uma cidade no tour.
    """
    return [coords[i] for i in tour]


def calculate_total_distance(coords):
    """
        Calcula a distância euclidiana total de um percurso.

        Esta função calcula a soma das distâncias euclidianas entre cada par de pontos consecutivos no percurso.

        Parâmetros:
        coords (lista): Uma lista de tuplas onde cada tupla representa as coordenadas (x, y) de um ponto no percurso.

        Retorna:
        float: A distância euclidiana total do percurso.
    """
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += distance_between_two_points_1(coords[i], coords[i + 1])
    return total_distance


def read_coordinates(file_path):
    """
        Lê coordenadas de um arquivo.

        Esta função lê um arquivo onde cada linha contém um índice e as coordenadas x e y de um ponto,
        separados por espaços. Retorna uma lista de tuplas onde cada tupla representa as coordenadas de um ponto.

        Parâmetros:
        caminho_arquivo (str): O caminho para o arquivo.

        Retorna:
        lista: Uma lista de tuplas onde cada tupla representa as coordenadas (x, y) de um ponto.
        """
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            index, x, y = map(int, line.split())
            coordinates.append((x, y))
    return coordinates


def extract_city_count(filename):
    # Função para extrair o número de cidades do nome do arquivo
    match = re.search(r'(\d+)_cidades\.txt$', filename)
    if match:
        return int(match.group(1))
    else:
        return 0


def choose_file(directory):
    """
        Permite ao usuário escolher um arquivo de um diretório.

        Esta função lista todos os arquivos em um diretório e pede ao usuário para escolher um digitando seu índice.
        Continua perguntando até que o usuário digite um índice válido.

        Parâmetros:
        diretorio (str): O caminho para o diretório.

        Retorna:
        str: O caminho para o arquivo escolhido.
        """
    files = os.listdir(directory)
    while True:
        for i, filename in enumerate(files):
            print(f'{i}: {filename}')
        try:
            file_index = int(input('Escolha o número do arquivo que você deseja ler: '))
            if 0 <= file_index < len(files):
                return os.path.join(directory, files[file_index])
            else:
                print("Número inválido. Por favor, tente novamente.")
        except ValueError:
            print("Entrada inválida. Por favor, insira um número.")


def extract_info_from_filename(file_path):
    """
        Extrai informações de um nome de arquivo.

        Esta função extrai o número de cidades e o número de viajantes de um nome de arquivo com o formato
        'mTSP-n<num_cidades>-m<num_viajantes>'. Levanta um ValueError se o nome do arquivo não estiver no formato
        esperado.

        Parâmetros:
        caminho_arquivo (str): O caminho para o arquivo.

        Retorna:
        tupla: Uma tupla contendo o número de cidades e o número de viajantes.
        """
    filename = os.path.basename(file_path)
    match = re.match(r'mTSP-n(\d+)-m(\d+)', filename)
    if match:
        num_cities, num_travelers = map(int, match.groups())
        return num_cities, num_travelers
    else:
        raise ValueError(f"O nome do arquivo '{filename}' não está no formato esperado.")


def run_tests():
    mac_directory = ('/Users/u22333/Desktop/machine-learning-introduction/machine-learning-introduction'
                     '/1_caixeiro_viajante_submissao/turma39-topicosIA-projeto1-equipe1-master/instances')

    windows_directory = ('C:\\Users\\vinic\\OneDrive\\Área de '
                         'Trabalho\\machine-learning-introduction\\1_caixeiro_viajante_submissao\\turma39-topicosIA'
                         '-projeto1'
                         '-equipe1-master\\instances')

    directory = mac_directory
    file_path = choose_file(directory)
    coordinates = read_coordinates(file_path)

    num_cities, num_travelers = extract_info_from_filename(file_path)

    start_time = time.time()
    tour = n_tsp_my_heuristic(coordinates, num_travelers)
    end_time = time.time()
    interval = end_time - start_time

    print(f"Número de viajantes: {num_travelers}")
    print(f"Número de cidades:   {num_cities}")
    print(f"Coordenadas:         {coordinates}")
    print(f"Indices das rotas    {tour}")
    print(f"Tempo de execução:   {interval:.6f} segundos")

    total_distance = 0
    for i, route in enumerate(tour):
        tour_coordinates = get_coords_from_tour(route, coordinates)
        print(f"\nRota viajante {i + 1}: {route}")
        print(f"Coordenadas  rota: {tour_coordinates}")
        distance = calculate_total_distance(tour_coordinates)
        rounded_distance = round(distance, 3)
        print(f"Distância viajante {i + 1}: {rounded_distance}\n")
        total_distance += distance

    total_distance = round(total_distance, 3)
    print(f"Distância total de todos os viajantes: {total_distance}")


def main():
    while True:
        run_tests()
        repeat = input("Você quer testar novamente? (s/n): ")
        if repeat.lower() != 's':
            break
    print("Obrigado por usar o programa. Até a próxima!")


if __name__ == "__main__":
    main()
