import os
import re


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


def test_read_coordinates():
    directory = ('C:\\Users\\vinic\\OneDrive\\Área de '
                 'Trabalho\\machine-learning-introduction\\1_caixeiro_viajante_submissao\\turma39-topicosIA-projeto1'
                 '-equipe1-master\\instances')
    file_path = choose_file(directory)
    coordinates = read_coordinates(file_path)

    num_cities, num_travelers = extract_info_from_filename(file_path)

    print(f"Número de viajantes: {num_travelers}")
    print(f"Número de cidades:   {num_cities}")
    print(f"Coordenadas:         {coordinates}")


def main():
    test_read_coordinates()


if __name__ == "__main__":
    main()
