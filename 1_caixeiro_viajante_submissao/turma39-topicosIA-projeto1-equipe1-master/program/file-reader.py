import os


def read_coordinates(file_path):
    coordinates = []
    with open(file_path, 'r') as file:
        lines = file.readlines()
        for line in lines:
            index, x, y = map(int, line.split())
            coordinates.append((x, y))
    return coordinates


def choose_file(directory):
    files = os.listdir(directory)
    for i, filename in enumerate(files):
        print(f'{i}: {filename}')
    file_index = int(input('Escolha o número do arquivo que você deseja ler: '))
    return os.path.join(directory, files[file_index])


def test_read_coordinates():
    directory = ('C:\\Users\\vinic\\OneDrive\\Área de '
                 'Trabalho\\machine-learning-introduction\\1_caixeiro_viajante_submissao\\turma39-topicosIA-projeto1'
                 '-equipe1-master\\instances')
    file_path = choose_file(directory)
    coordinates = read_coordinates(file_path)
    print(coordinates)


def main():
    test_read_coordinates()


if __name__ == "__main__":
    main()
