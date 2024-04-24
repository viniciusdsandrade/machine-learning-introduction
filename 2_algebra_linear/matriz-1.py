import numpy as np


def printar_matriz(matriz):
    # Encontra o elemento com o maior número de dígitos
    max_len = max(len(str(e)) for row in matriz for e in row)

    for i in range(len(matriz)):
        print('[', end='')
        for j in range(len(matriz[i])):
            # Usa str.format() para garantir que todos os elementos ocupem o mesmo espaço
            # Alinha os números à direita removendo espaços extras à esquerda
            print("{:>{}}".format(matriz[i][j], max_len), end='')
            # Adiciona um espaço após cada número, exceto o último da linha
            if j != len(matriz[i]) - 1:
                print(' ', end='')
        print(']')
    print()


def is_matriz_simetrica(matriz):
    if len(matriz) != len(matriz[0]):
        return False

    # Verifica se a matriz é simétrica
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            if matriz[i][j] != matriz[j][i]:
                return False

    return True


def determinante_matriz(matriz):
    """Calcula o determinante de uma matriz quadrada."""

    if len(matriz) != len(matriz[0]):
        raise ValueError("A matriz não é quadrada")

    if len(matriz) == 1:
        return matriz[0][0]

    if len(matriz) == 2:
        return (matriz[0][0] * matriz[1][1] -
                matriz[0][1] * matriz[1][0])

    if len(matriz) == 3:
        return (matriz[0][0] * matriz[1][1] * matriz[2][2] +
                matriz[0][1] * matriz[1][2] * matriz[2][0] +
                matriz[0][2] * matriz[1][0] * matriz[2][1] -
                matriz[0][2] * matriz[1][1] * matriz[2][0] -
                matriz[0][1] * matriz[1][0] * matriz[2][2] -
                matriz[0][0] * matriz[1][2] * matriz[2][1])

    # Caso geral: usa a expansão de Laplace ao longo da primeira linha
    det = 0
    for j in range(len(matriz)):
        det += matriz[0][j] * cofator_matriz(matriz)[0][j]  # Usa a função cofator_matriz
    return det


def cofator_matriz(matriz):
    """Calcula a matriz de cofatores de uma matriz quadrada."""

    cofator = []
    for i in range(len(matriz)):
        linha = []
        for j in range(len(matriz[i])):
            # Cria a submatriz menor excluindo a linha i e a coluna j
            cofator_menor = [linha[:j] + linha[j + 1:] for linha in matriz[:i] + matriz[i + 1:]]
            linha.append(determinante_matriz(cofator_menor) * (-1) ** (i + j))
        cofator.append(linha)
    return cofator


def is_matriz_inversivel(matriz):
    if len(matriz) != len(matriz[0]):
        return False

    try:
        inversa = np.linalg.inv(matriz)
        return True
    except np.linalg.LinAlgError:
        return False


def soma_matriz(matriz_1, matriz_2):
    matriz_soma = []
    for i in range(len(matriz_1)):
        linha = []
        for j in range(len(matriz_1[i])):
            linha.append(matriz_1[i][j] + matriz_2[i][j])
        matriz_soma.append(linha)
    return matriz_soma


def subtracao_matriz(matriz_1, matriz_2):
    matriz_subtracao = []
    for i in range(len(matriz_1)):
        linha = []
        for j in range(len(matriz_1[i])):
            linha.append(matriz_1[i][j] - matriz_2[i][j])
        matriz_subtracao.append(linha)
    return matriz_subtracao


def multiplicacao_matriz(matriz_1, matriz_2):
    # Verifica se as matrizes são compatíveis para multiplicação
    if len(matriz_1[0]) != len(matriz_2):
        raise ValueError("As matrizes não são compatíveis para multiplicação")

    matriz_multiplicacao = []
    for i in range(len(matriz_1)):
        linha = []
        for j in range(len(matriz_2[0])):
            soma = 0
            for k in range(len(matriz_2)):
                soma += matriz_1[i][k] * matriz_2[k][j]
            linha.append(soma)
        matriz_multiplicacao.append(linha)
    return matriz_multiplicacao


def transposta_matriz(matriz):
    matriz_transposta = []
    for j in range(len(matriz[0])):
        linha = []
        for i in range(len(matriz)):
            linha.append(matriz[i][j])
        matriz_transposta.append(linha)
    return matriz_transposta


def matriz_inversa(matriz):
    """
    Calcula e retorna a matriz inversa de uma matriz dada.

    Args:
      matriz: Uma matriz NumPy bidimensional quadrada.

    Returns:
      A matriz inversa da matriz de entrada, se ela existir. Caso contrário,
      retorna None.
    """
    try:
        inversa = np.linalg.inv(matriz)
        return inversa
    except np.linalg.LinAlgError:
        print("A matriz não é invertível (singular).")
        return None


def matriz_identidade(n):
    """
    Retorna uma matriz identidade de ordem n.

    Args:
      n: A ordem da matriz identidade.

    Returns:
      Uma matriz identidade de ordem n.
    """
    return [[1 if i == j else 0 for j in range(n)] for i in range(n)]


def matriz_nula(n):
    """
    Retorna uma matriz nula de ordem n.

    Args:
      n: A ordem da matriz nula.

    Returns:
      Uma matriz nula de ordem n.
    """
    return [[0 for j in range(n)] for i in range(n)]


def matriz_por_escalar(matriz, escalar):
    """
    Multiplica uma matriz por um escalar.

    Args:
      matriz: Uma matriz NumPy bidimensional.
      escalar: O escalar pelo qual a matriz será multiplicada.

    Returns:
      A matriz resultante da multiplicação da matriz de entrada pelo escalar.
    """
    return [[elemento * escalar for elemento in linha] for linha in matriz]


def test_determinante_matriz():
    matriz = [[1, 2], [3, 4]]
    matriz_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_3 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
    print("Matriz:")
    printar_matriz(matriz)
    print("Determinante:", determinante_matriz(matriz))

    print("Matriz 2:")
    printar_matriz(matriz_2)
    print("Determinante 2:", determinante_matriz(matriz_2))

    print("Matriz 3:")
    printar_matriz(matriz_3)
    print("Determinante 3:", determinante_matriz(matriz_3))


def test_is_matriz_inversivel():
    matriz_inversivel = [[1, 2], [3, 4]]
    matriz_singular = [[1, 2], [2, 4]]

    print("Matriz inversível:")
    printar_matriz(matriz_inversivel)
    print("É inversível?", is_matriz_inversivel(matriz_inversivel))

    print("Matriz singular:")
    printar_matriz(matriz_singular)
    print("É inversível?", is_matriz_inversivel(matriz_singular))


def test_is_matriz_simetrica():
    matriz_simetrica = [[1, 2, 3], [2, 4, 5], [3, 5, 6]]
    matriz_nao_simetrica = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    print("Matriz simétrica:")
    printar_matriz(matriz_simetrica)
    print("É simétrica?", is_matriz_simetrica(matriz_simetrica))

    transposta_1 = transposta_matriz(matriz_simetrica)
    print("Transposta da matriz simétrica:")
    printar_matriz(transposta_1)

    print("Matriz não simétrica:")
    printar_matriz(matriz_nao_simetrica)
    print("É simétrica?", is_matriz_simetrica(matriz_nao_simetrica))

    transposta_2 = transposta_matriz(matriz_nao_simetrica)
    print("Transposta da matriz não simétrica:")
    printar_matriz(transposta_2)


def test_matriz_nula():
    for n in range(2, 30):
        matriz = matriz_nula(n)
        print("Matriz Nula de ordem", n)
        printar_matriz(matriz)


def test_matriz_identidade():
    for n in range(2, 30):
        matriz = matriz_identidade(n)
        print("Matriz Identidade de ordem", n)
        printar_matriz(matriz)


def test_matriz_por_escalar():
    for escalar in range(2, 10):
        matriz = [[1, 2], [3, 4]]
        matriz_por_escalar_resultante = matriz_por_escalar(matriz, escalar)
        print("Matriz original:")
        printar_matriz(matriz)
        print("Matriz multiplicada por", escalar)
        printar_matriz(matriz_por_escalar_resultante)


def test_matriz_inversa():
    matriz_exemplo = [[1, 2], [3, 4]]
    inversa = matriz_inversa(matriz_exemplo)
    print("Matriz original:")
    print(np.array(matriz_exemplo))
    print("Matriz inversa:")
    print(inversa)

    multiply = np.dot(matriz_exemplo, inversa)
    print("Multiplicação da matriz pela sua inversa:")
    print(multiply)


def test_transposta_matriz():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Matriz original:")
    printar_matriz(matriz)
    matriz_transposta = transposta_matriz(matriz)
    print("Matriz Transposta:")
    printar_matriz(matriz_transposta)


def test_multiplicacao_matriz():
    # faça um exemplo com matrizes de dimensões distintas
    matriz_1 = [[1, 2, 3], [4, 5, 6]]
    matriz_2 = [[7, 8], [9, 10], [11, 12]]

    matriz_multiplicacao = multiplicacao_matriz(matriz_1, matriz_2)
    printar_matriz(matriz_multiplicacao)


def test_printar_matriz():
    matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    printar_matriz(matriz)

    matriz_2 = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]
    printar_matriz(matriz_2)


def test_somar_matriz():
    matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_soma = soma_matriz(matriz_1, matriz_2)
    printar_matriz(matriz_soma)


def test_subtracao_matriz():
    matriz_1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_2 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    matriz_subtracao = subtracao_matriz(matriz_1, matriz_2)
    printar_matriz(matriz_subtracao)


def main():
    test_determinante_matriz()
    test_is_matriz_inversivel()
    test_is_matriz_simetrica()
    test_matriz_nula()
    test_matriz_identidade()
    test_matriz_por_escalar()
    test_matriz_inversa()
    test_transposta_matriz()
    test_printar_matriz()
    test_somar_matriz()
    test_subtracao_matriz()
    test_multiplicacao_matriz()


if __name__ == '__main__':
    main()
