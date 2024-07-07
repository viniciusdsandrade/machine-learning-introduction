import numpy as np
from scipy import stats


def calcular_media(lista):
    return np.mean(lista)


def calcular_mediana(lista):
    return np.median(lista)


def calcular_moda(numeros):
    moda = stats.mode(numeros)
    if len(set(numeros)) == len(numeros):
        return "não há moda"
    else:
        return moda.mode[0]


def calcular_variancia(lista):
    return np.var(lista)


def calcular_desvio_padrao(lista):
    return np.std(lista)


def pesquisa():
    total_pessoas = 2673

    x = round((12 / 100) * total_pessoas)
    y = round((22 / 100) * total_pessoas)
    z = round((28 / 100) * total_pessoas)
    w = total_pessoas - x - y - z  # Ajusta w para que a soma seja igual ao total

    print("2673 pessoas")
    print("espaço        12%:   ", x)
    print("conforto      22%:   ", y)
    print("tranquilidade 28%:   ", z)
    print("Seguranca:    38%:   ", w)


escola = [23, 25, 28, 31, 32, 35]
conjunto = [1, 2, 3, 6]
numeros = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29, 31, 33, 35, 37, 39, 41, 43, 45, 47, 49]
numeros2 = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36, 38, 40, 42, 44, 46, 48]
numeros3 = [4, 8, 12, 16, 20, 24, 28, 32, 36, 40]
numeros4 = [6, 12, 18, 24, 30, 36, 42, 48, 54, 60]
numeros5 = [8, 16, 24, 32, 40, 48, 56, 64, 72, 80]


def relatorio(numeros):
    print("Média: ", calcular_media(numeros))
    print("Mediana: ", calcular_mediana(numeros))
    print("Moda: ", calcular_moda(numeros))
    print("Variância: ", calcular_variancia(numeros))
    print("Desvio padrão: ", calcular_desvio_padrao(numeros))


def main():
    pesquisa()
    relatorio(escola)
    print("\n")
    relatorio(conjunto)
    print("\n")
    relatorio(numeros)
    print("\n")
    relatorio(numeros2)
    print("\n")
    relatorio(numeros3)
    print("\n")
    relatorio(numeros4)
    print("\n")
    relatorio(numeros5)


if __name__ == "__main__":
    main()
