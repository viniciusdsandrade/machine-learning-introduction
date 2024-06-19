from typing import Tuple
import math


def brute_force_tsp_complexity(n: int) -> Tuple[int, int]:
    """
    Calcula as complexidades espacial e temporal do algoritmo de Força Bruta para o problema TSP.

    Args:
        n (int): Número de cidades no problema TSP.

    Returns:
        Tuple[int, int]: Uma tupla contendo a complexidade espacial (O(n)) e temporal (O(n!)), respectivamente.
    """
    space_complexity = n  # Complexidade espacial: O(n)
    time_complexity = math.factorial(n)  # Complexidade temporal: O(n!)

    return space_complexity, time_complexity


def held_karp_tsp_complexity(n: int) -> Tuple[int, int]:
    """
    Calcula as complexidades espacial e temporal do algoritmo de Held-Karp (Programação Dinâmica) para o problema TSP.

    Args:
        n (int): Número de cidades no problema TSP.

    Returns:
        Tuple[int, int]: Uma tupla contendo a complexidade espacial (O(n * 2^n)) e temporal (O(n² * 2^n)), respectivamente.
    """
    space_complexity = n * (2 ** n)  # Complexidade espacial: O(n * 2^n)
    time_complexity = (2 ** n) * (n ** 2)  # Complexidade temporal: O(n² * 2^n)

    return space_complexity, time_complexity


# -------------------------------------------------------------------------------------
def brute_force_n_tsp_complexity(cidades: int, viajantes: int) -> Tuple[int, int]:
    """
    Calcula as complexidades espacial e temporal do algoritmo de Força Bruta para o problema nTSP.

    Args:
        cidades   (int): Número de cidades em cada problema TSP individual.
        viajantes (int): Número de viajantes (ou TSPs) no problema nTSP.

    Returns:
        Tuple[int, int]: Uma tupla contendo a complexidade espacial (O(m * n²)) e temporal (O((n!)^m)), respectivamente.
    """
    space_complexity = viajantes * (cidades ** 2)  # Complexidade espacial: O(m * n²)
    time_complexity = (math.factorial(cidades)) ** viajantes  # Complexidade temporal: O((n!)^m)

    return space_complexity, time_complexity


def held_karp_n_tsp_complexity(cidades: int, viajantes: int) -> Tuple[int, int]:
    """
    Calcula as complexidades espacial e temporal de uma solução nTSP que usa o algoritmo de Held-Karp para cada TSP individual.
    Note que esta função não representa a complexidade de um algoritmo único para o nTSP, mas sim a complexidade de aplicar
    o Held-Karp 'm' vezes.

    Args:
        cidades   (int): Número de cidades em cada problema TSP individual.
        viajantes (int): Número de viajantes (ou TSPs) no problema nTSP.

    Returns:
        Tuple[int, int]: Uma tupla contendo a complexidade espacial (O(m * n * 2^n)) e temporal (O(m * n² * 2^n)), respectivamente.
    """
    space_complexity = viajantes * (cidades ** 2) * (2 ** cidades)  # Complexidade espacial: O(m * n * 2^n)
    time_complexity = viajantes * (2 ** cidades) * (cidades ** 2)  # Complexidade temporal: O(m * n² * 2^n)

    return space_complexity, time_complexity


def test_tsp():
    # Loop de 1 a 20 para n (número de cidades)
    for n in range(1, 21):
        print("---------------------------------------------")
        print(f"Cidades = {n:2}   | Espacial  | Temporal       |")
        print("-------------- |-----------|-----------------")
        print(f"Força Bruta    | {brute_force_tsp_complexity(n)[0]:>7}   | {brute_force_tsp_complexity(n)[1]:>7}")
        print(f"Held-Karp      | {held_karp_tsp_complexity(n)[0]:>7}   | {held_karp_tsp_complexity(n)[1]:>7}")
        print("\n")


def test_n_tsp():
    for n in range(1, 21):
        for m in range(1, 21):
            print(f"n = {n}, m = {m}")
            print("Complexidade Espacial | Complexidade Temporal")
            print("Força Bruta: ", brute_force_tsp_complexity(n))
            print("Held-Karp:   ", held_karp_tsp_complexity(n))
            print("\n")


if __name__ == "__main__":
    test_tsp()
    # test_n_tsp()
