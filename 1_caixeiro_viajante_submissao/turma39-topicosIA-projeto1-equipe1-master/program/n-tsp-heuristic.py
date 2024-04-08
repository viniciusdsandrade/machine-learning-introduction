import time
import math
import re
import os


def distance_between_two_points_1(p1, p2):
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Parameters:
    p1 (tuple): A tuple representing the coordinates (x, y) of the first point.
    p2 (tuple): A tuple representing the coordinates (x, y) of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def distance_between_two_points_2(p1, p2):
    """
    Calculate the Euclidean distance between two points in a 2D space.

    Parameters:
    p1 (tuple): A tuple representing the coordinates (x, y) of the first point.
    p2 (tuple): A tuple representing the coordinates (x, y) of the second point.

    Returns:
    float: The Euclidean distance between the two points.
    """
    return math.dist(p1, p2)


def get_coords_from_tour(tour, coords):
    """
    Get the coordinates for each city in the tour.

    Parameters:
    tour (list): A list of city indices representing the tour.
    coords (list): A list of tuples where each tuple represents the coordinates (x, y) of a city.

    Returns:
    list: A list of tuples where each tuple represents the coordinates (x, y) of a city in the tour.
    """
    return [coords[i] for i in tour]


def n_tsp_my_heuristic(coords, num_viajantes):
    """
    Implementa uma heurística para o problema do caixeiro viajante.

    Parâmetros:
        coords (lista): Uma lista de coordenadas das cidades. Cada coordenada é uma tupla (x, y).
        num_viajantes (int): O número de viajantes.

    Retorna:
        rotas (lista): Uma lista de rotas para cada viajante. Cada rota é uma lista de índices das cidades.

    Descrição: A função primeiro calcula a distância entre todas as cidades e as ordena da mais próxima à mais
    distante da origem. Em seguida, distribui as cidades igualmente entre os viajantes, sempre respeitando a ordem
    das cidades da mais próxima à mais distante da origem. Se houver cidades restantes, elas são distribuídas aos
    viajantes de forma rotativa. Finalmente, cada viajante retorna à cidade de origem.
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


def calculate_total_distance(coords):
    """
        Calculate the total Euclidean distance of a tour.

        This function calculates the sum of the Euclidean distances between each pair of consecutive points in the tour.

        Parameters:
        coords (list): A list of tuples where each tuple represents the coordinates (x, y) of a point in the tour.

        Returns:
        float: The total Euclidean distance of the tour.
        """
    total_distance = 0
    for i in range(len(coords) - 1):
        total_distance += distance_between_two_points_1(coords[i], coords[i + 1])
    return total_distance


def read_coordinates(file_path):
    """
        Read coordinates from a file.

        This function reads a file where each line contains an index and the x and y coordinates of a point,
        separated by spaces. It returns a list of tuples where each tuple represents the coordinates of a point.

        Parameters:
        file_path (str): The path to the file.

        Returns:
        list: A list of tuples where each tuple represents the coordinates (x, y) of a point.
        """
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            index, x, y = map(int, line.split())
            coordinates.append((x, y))
    return coordinates


def choose_file(directory):
    """
        Let the user choose a file from a directory.

        This function lists all files in a directory and asks the user to choose one by typing its index. It keeps
        asking until the user types a valid index.

        Parameters:
        directory (str): The path to the directory.

        Returns:
        str: The path to the chosen file.
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
        Extract information from a filename.

        This function extracts the number of cities and the number of travelers from a filename with the format
        'mTSP-n<num_cities>-m<num_travelers>'. It raises a ValueError if the filename is not in the expected format.

        Parameters:
        file_path (str): The path to the file.

        Returns:
        tuple: A tuple containing the number of cities and the number of travelers.
        """
    filename = os.path.basename(file_path)
    match = re.match(r'mTSP-n(\d+)-m(\d+)', filename)
    if match:
        num_cities, num_travelers = map(int, match.groups())
        return num_cities, num_travelers
    else:
        raise ValueError(f"O nome do arquivo '{filename}' não está no formato esperado.")


def run_tests():
    directory = ('C:\\Users\\vinic\\OneDrive\\Área de '
                 'Trabalho\\machine-learning-introduction\\1_caixeiro_viajante_submissao\\turma39-topicosIA-projeto1'
                 '-equipe1-master\\instances')
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
