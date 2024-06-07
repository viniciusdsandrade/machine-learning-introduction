from scipy.optimize import linprog
from math import sin, cos
import numpy as np


def problema_1():
    """Resolve o Problema 1."""
    c = [5, 1]
    A = [[-2, -1], [-1, -1], [-1, -5]]
    b = [-6, -4, -10]
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x∗) = {res.fun:.0f}.')  #
    # Formatação da saída


def problema_2():
    """Resolve o Problema 2."""
    c = [-2, 3]  # Invertido para maximização
    A = [[1, 2], [2, -1]]
    b = [6, 8]
    x0_bounds = (0, None)
    x1_bounds = (0, None)
    res = linprog(c, A_ub=A, b_ub=b, bounds=[x0_bounds, x1_bounds], method='highs')
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x∗) = {-res.fun:.0f}.')  #
    # Formatação da saída e inversão do sinal


def problema_3():
    """Resolve o Problema 3."""
    c = [-15, -41, 11]
    A = [[-2, -1, -1]]
    b = [-3]
    x_bounds = [(0, 1), (0, 1), (0, 1)]
    res = linprog(c, A_ub=A, b_ub=b, bounds=x_bounds, method='highs')
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x∗) = {-res.fun:.0f}.')


def problema_4():
    """Resolve o Problema 4."""
    c = [0, 0, 10, 10]
    A_ub = [
        [-1, 2, 0, 0],
        [0, -1, 2, 0],
        [0, 0, -1, 2]
    ]
    b_ub = [0, 0, 0]
    A_eq = [[1, 1, 1, 1]]
    b_eq = [400]
    bounds = [(0, None), (0, None), (0, None), (0, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}, {res.x[3]:.0f}) com f(x∗) = {res.fun:.0f}.')


def problema_5():
    """Resolve o Problema 5."""
    c = [2, 0, -3]  # Invertido para maximização
    A_ub = [[1, -1, 0], [0, 1, -1]]
    b_ub = [-1, -1]
    A_eq = [[1, 1, 1]]
    b_eq = [12]
    bounds = [(0, None), (0, None), (0, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, A_eq=A_eq, b_eq=b_eq, bounds=bounds)
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x∗) = {-res.fun:.0f}.')  # Inverte o sinal de res.fun


def problema_6():
    print("Não existe o enunciado do Problema 6 =(")


def problema_7():
    """Resolve o Problema 7."""
    c = [-9, -5, 0]
    A_ub = np.array([[sin(k / 13), cos(k / 13), 0] for k in range(1, 14)])
    b_ub = np.array([7] * 13)
    bounds = [(0, None), (0, None), (0, None)]
    res = linprog(c, A_ub=A_ub, b_ub=b_ub, bounds=bounds, method="highs")

    if res.success:
        print(
            f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x∗) = {-res.fun:.0f}.')  # Inverte o sinal de res.fun
    else:
        print("Otimização falhou. Status:", res.status)
        print("Mensagem:", res.message)

    # Exibe os resultados
    if res.success:
        print("Solução ótima encontrada:")
        print("x1 =", res.x[0])
        print("x2 =", res.x[1])
        print("x3 =", res.x[2])
        print("Valor ótimo =", -res.fun)
    else:
        print("Otimização falhou. Status:", res.status)
        print("Mensagem:", res.message)


# Função principal para o menu
def linear_optimization():
    problemas = {
        '1': problema_1,
        '2': problema_2,
        '3': problema_3,
        '4': problema_4,
        '5': problema_5,
        '6': problema_6,
        '7': problema_7,
    }

    while True:
        print("\nMenu de Problemas de Otimização:")
        for i in range(1, 8):
            print(f"{i}. Problema {i}")
        print("8. Sair")

        opcao = input("Digite o número do problema que deseja resolver: ")

        if opcao == '8':
            break

        funcao = problemas.get(opcao)
        if funcao:
            funcao()
        else:
            print("Opção inválida. Tente novamente.")


if __name__ == "__main__":
    linear_optimization()

# https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html 13](1,2) Huangfu, Q., Galabova, I.,
# Feldmeier, M., and Hall, J. A. J. “HiGHS - high performance software for linear optimization.” https://highs.dev/ [
# 14] Huangfu, Q. and Hall, J. A. J. “Parallelizing the dual revised simplex method.” Mathematical Programming
# Computation, 10 (1), 119-142, 2018. DOI: 10.1007/s12532-017-0130-5 [15] Harris, Paula MJ. “Pivot selection methods
# of the Devex LP code.” Mathematical programming 5.1 (1973): 1-28. [16] Goldfarb, Donald, and John Ker Reid. “A
# practicable steepest-edge simplex algorithm.” Mathematical Programming 12.1 (1977): 361-371.
