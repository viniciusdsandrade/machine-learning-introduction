from scipy.optimize import linprog
import math

from graphic_representation import (
    plot_2d_problema_1,
    plot_3d_problema_1,
    plot_2d_problema_2,
    plot_3d_problema_2,
    plot_2d_problema_3,
    plot_3d_problema_3,
    plot_2d_problema_4,
    plot_3d_problema_4,
    plot_2d_problema_5,
    plot_3d_problema_5,
    plot_2d_problema_7,
    plot_3d_problema_7,
)


def problema_1():
    """
    Resolve o Problema 1 de otimização linear, minimizando a função objetivo 5x1 + x2 sujeita a restrições lineares.

        Min f(x1, x2) = 5x1 + x2

    sujeita às seguintes restrições:

        2x1 + x2 ≥ 6
        x1 + x2  ≥ 4
        x1 + 5x2 ≥ 10
        x1, x2   ≥ 0

    A solução ótima deste problema é x∗ = (0, 6) com f(x∗) = 6.

    A função formula o problema no formato padrão de programação linear e utiliza o solver 'linprog' da biblioteca
    SciPy para encontrar a solução ótima. Em seguida, plota gráficos 2D e 3D para visualizar a solução.

    Returns:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - 'x': array com os valores ótimos das variáveis de decisão (x1, x2)
            - 'fun': valor ótimo da função objetivo
    """
    # Coeficientes da função objetivo (a serem minimizados)
    c = [5, 1]

    # Matriz de coeficientes das restrições de desigualdade
    # Cada linha representa uma restrição, cada coluna uma variável
    A = [
        [-2, -1],  # -2x1 - x2 ≤ -6  (equivalente a 2x1 + x2 ≥ 6)
        [-1, -1],  # -x1 - x2 ≤ -4   (equivalente a x1 + x2 ≥ 4)
        [-1, -5]  # -x1 - 5x2 ≤ -10  (equivalente a x1 + 5x2 ≥ 10)
    ]

    # Vetor de termos independentes das restrições de desigualdade
    b = [-6, -4, -10]

    # Limites inferiores e superiores das variáveis (ambas não negativas)
    x0_bounds = (0, None)  # x1 ≥ 0
    x1_bounds = (0, None)  # x2 ≥ 0

    # Resolve o problema de PL usando o solver de alto desempenho 'highs'
    res = linprog(
        c,  # Coeficientes da função objetivo
        A_ub=A,  # Matriz de restrições
        b_ub=b,  # Lados direitos das restrições
        bounds=[x0_bounds, x1_bounds],  # Limites das variáveis
        method='highs',  # Método de otimização (highs)
    )

    # Exibe a solução ótima encontrada (convertendo o valor da função objetivo de volta para a maximização)
    print(f'A solução ótima deste problema é x* = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x*) = {res.fun:.0f}.')

    # Chama funções para plotar gráficos 2D e 3D da solução
    plot_2d_problema_1(res)
    plot_3d_problema_1(res)

    # Retorna o objeto com os resultados da otimização (incluindo a solução ótima e o valor da função objetivo)
    return res


def problema_2():
    """
    Resolve o Problema 2 de otimização linear, maximizando a função objetivo 2x1 - 3x2.

        Max f(x1, x2) = 2x1 - 3x2

    sujeita às seguintes restrições:

        x1 + 2x2 ≤ 6
        2x1 - x2 ≤ 8
        x1, x2   ≥ 0

    A solução ótima deste problema é x∗ = (4, 0) com f(x∗) = 8.

    A função formula o problema no formato padrão de programação linear, convertendo o problema de maximização em um
    de minimização invertendo os coeficientes da função objetivo. Em seguida, utiliza o solver 'linprog' da
    biblioteca SciPy para encontrar a solução ótima.

    Por fim, plota gráficos 2D e 3D para visualizar a solução.

    Returns:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - 'x': array com os valores ótimos das variáveis de decisão (x1, x2)
            - 'fun': valor ótimo da função objetivo (multiplicado por -1 para obter o valor original da maximização)
    """
    # Coeficientes da função objetivo (invertidos para transformar o problema de maximização em minimização)
    c = [-2, 3]

    # Matriz de coeficientes das restrições de desigualdade
    # Cada linha representa uma restrição, cada coluna uma variável
    A = [
        [1, 2],  # x1 + 2x2 ≤ 6
        [2, -1]  # 2x1 - x2 ≤ 8
    ]

    # Vetor de termos independentes das restrições de desigualdade
    b = [6, 8]

    # Limites inferiores e superiores das variáveis (ambas não negativas)
    x0_bounds = (0, None)  # x1 ≥ 0
    x1_bounds = (0, None)  # x2 ≥ 0

    # Resolução do problema de programação linear usando o método 'highs'
    res = linprog(
        c,  # Vetor de coeficientes da função objetivo
        A_ub=A,  # Matriz de coeficientes das restrições de desigualdade
        b_ub=b,  # Vetor de termos independentes das restrições de desigualdade
        bounds=[x0_bounds, x1_bounds],  # Limites (mínimo e máximo) para cada variável de decisão
        method='highs',  # Método de otimização a ser usado (highs é um solver de alto desempenho)
    )

    # Exibe a solução ótima encontrada (convertendo o valor da função objetivo de volta para a maximização)
    print(f'A solução ótima deste problema é x* = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x*) = {-res.fun:.0f}.')

    # Chama funções para plotar gráficos 2D e 3D da solução
    plot_2d_problema_2(res)
    plot_3d_problema_2(res)

    # Retorna o objeto com os resultados da otimização (incluindo a solução ótima e o valor da função objetivo)
    return res


def problema_3():
    """
    Resolve o Problema 3 de otimização linear, maximizando a função objetivo:

        f(x1, x2, x3) = 15(x1 + 2x2) + 11(x2 - x3)
        f(x1, x2, x3) = 15x1 + 41x2 - 11x3

    sujeita às seguintes restrições:

        3x1 ≥ x1 + x2 + x3
        0 ≤ xj ≤ 1 para j = 1, 2, 3

    Restruturação das restrições:

        -2x1 - x2 - x3 ≤ -3
        0 ≤ x1 ≤ 1
        0 ≤ x2 ≤ 1
        0 ≤ x3 ≤ 1

    A solução ótima deste problema é x∗ = (1, 1, 0) com f(x∗) = 56.

    A função formula o problema no formato padrão de programação linear, convertendo o problema de maximização em um
    de minimização invertendo os coeficientes da função objetivo. Em seguida, utiliza o solver 'linprog' da
    biblioteca SciPy para encontrar a solução ótima.

    Por fim, plota gráficos 2D e 3D para visualizar a solução (funções não mostradas).

    Returns:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - 'x': array com os valores ótimos das variáveis de decisão (x1, x2, x3)
            - 'fun': valor ótimo da função objetivo (multiplicado por -1 para obter o valor original da maximização)
    """
    # Coeficientes da função objetivo (invertidos para transformar o problema de maximização em minimização)
    c = [-15, -41, 11]  # Original: 15x1 + 41x2 - 11x3

    # Matriz de coeficientes das restrições de desigualdade
    # Cada linha representa uma restrição, cada coluna uma variável.
    # A restrição original (3x1 ≥ x1 + x2 + x3) é reescrita como -2x1 - x2 - x3 ≤ -3
    # para se adequar ao formato A_ub * x ≤ b_ub
    A = [[-2, -1, -1]]

    # Vetor de termos independentes das restrições de desigualdade
    b = [-3]

    # Limites inferiores e superiores das variáveis
    x_bounds = [(0, 1), (0, 1), (0, 1)]

    # Resolução do problema de programação linear usando o método 'highs'
    res = linprog(
        c,  # Coeficientes da função objetivo
        A_ub=A,  # Matriz de coeficientes das restrições
        b_ub=b,  # Vetor de termos independentes das restrições
        bounds=x_bounds,  # Limites das variáveis
        method='highs',  # Método de otimização (highs - alto desempenho)
    )

    # Exibe a solução ótima encontrada (convertendo o valor da função objetivo de volta para a maximização)
    print(
        f'A solução ótima deste problema é x* = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x*) = {-res.fun:.0f}.')

    # Chama funções para plotar gráficos 2D e 3D da solução
    plot_2d_problema_3(res)
    plot_3d_problema_3(res)

    # Retorna o objeto com os resultados da otimização (incluindo a solução ótima e o valor da função objetivo)
    return res


def problema_4():
    """
    Resolve o problema de otimização linear 4, minimizando a função objetivo 10(x3 + x4)

        Min f(x1, x2, x3, x4) = 10(x3 + x4)
        Min f(x1, x2, x3, x4) = 10x3 + 10x4

    sujeita às seguintes restrições:

        ∑xj = 400 de 1 a 4
        xj − 2xj+1 ≥ 0, j = 1, 2, 3
        xj ≥ 0, j = 1, 2, 3, 4

    Restrições reescritas:

        x1 + x2 + x3 + x4 - 400 = 0

        x1 − 2x2 ≥ 0
        x2 − 2x3 ≥ 0
        x3 − 2x4 ≥ 0

        x1 ≥ 0
        x2 ≥ 0
        x3 ≥ 0
        x4 ≥ 0

    A solução ótima deste problema é x∗ = (400, 0, 0, 0) com f(x∗) = 0.

    A função formula o problema no formato padrão de programação linear, convertendo o problema de maximização
    em um de minimização invertendo os coeficientes da função objetivo. Em seguida, utiliza o solver 'linprog'
    da biblioteca SciPy para encontrar a solução ótima.

    Por fim, plota gráficos 2D e 3D para visualizar a solução (funções não mostradas).

    :return:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - x: array com os valores ótimos das variáveis x1, x2, x3 e x4.
            - fun: valor ótimo da função objetivo.
    """

    # Coeficientes da função objetivo (já na forma de minimização)
    c = [0, 0, 10, 10]

    # Matriz de coeficientes das restrições de igualdade e desigualdade
    A_eq = [[1, 1, 1, 1]]  # x1 + x2 + x3 + x4 = 400
    A_ub = [
        [-1, 2, 0, 0],  # x1 - 2x2 >= 0
        [0, -1, 2, 0],  # x2 - 2x3 >= 0
        [0, 0, -1, 2]  # x3 - 2x4 >= 0
    ]

    # Vetor de termos independentes das restrições de igualdade e desigualdade
    b_eq = [400]
    b_ub = [0, 0, 0]

    # Limites inferiores das variáveis (todas não negativas)
    bounds = [(0, None), (0, None), (0, None), (0, None)]

    # Resolução do problema de programação linear
    res = linprog(
        c, A_ub=A_ub,  # Matriz de coeficientes das restrições de desigualdade
        b_ub=b_ub,  # Vetor de termos independentes das restrições de desigualdade
        A_eq=A_eq,  # Matriz de coeficientes das restrições de igualdade
        b_eq=b_eq,  # Vetor de termos independentes das restrições de igualdade
        bounds=bounds,  # Limites das variáveis
        method='highs'  # Método de otimização (highs)
    )

    # Exibe a solução ótima encontrada
    print(
        f'A solução ótima deste problema é x* = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}, {res.x[3]:.0f}) com f(x*) = {res.fun:.0f}.')

    # Plota gráficos da solução
    plot_2d_problema_4(res)
    plot_3d_problema_4(res)

    # Retorna o objeto com os resultados da otimização (incluindo a solução ótima e o valor da função objetivo)
    return res


def problema_5():
    """
    Resolve o Problema 5 de otimização linear, maximizando a função objetivo -5x1 + 3(x1 + x3)

        Max f(x1, x2, x3) = -5x1 + 3(x1 + x3)
        Max f(x1, x2, x3) = -2x1 + 3x3

    sujeita às seguintes restrições:

        xj + 1 ≤ xj+1 -> j = 1, 2
        ∑xj = 12 de 1 a 3  -> j = 1, 2, 3
        xj ≥ 0 -> j = 1, 2, 3

    Restruturação das restrições:

        x1 - x2 + 1 ≤ 0
        x2 - x3 + 1 ≤ 0

        x1 + x2 + x3 - 12 = 0

        x1 ≥ 0
        x2 ≥ 0
        x3 ≥ 0

    A solução ótima deste problema é x∗ = (0, 1, 11) com f(x∗) = 36.

    OBSERVAÇÃO:

    O resultado da otimição é x* = (0, 1, 11) com f(x*) = 33, diferente do esperado (36).

    A função formula o problema no formato padrão de programação linear, convertendo o problema de maximização
    em um de minimização invertendo os coeficientes da função objetivo. Em seguida, utiliza o solver 'linprog'
    da biblioteca SciPy para encontrar a solução ótima.

    Por fim, plota gráficos 2D e 3D para visualizar a solução (funções não mostradas).

    Returns:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - 'x': array com os valores ótimos das variáveis de decisão (x1, x2, x3)
            - 'fun': valor ótimo da função objetivo (multiplicado por -1 para obter o valor original da maximização)
    """

    # Coeficientes da função objetivo
    c = [2, 0, -3]  # Note que queremos maximizar, então minimizamos o negativo

    # Matriz das restrições de desigualdade
    A = [
        [1, -1, 0],  # x1 - x2 ≤ -1
        [0, 1, -1],  # x2 - x3 ≤ -1
    ]

    # Vetor das restrições de desigualdade
    b = [-1, -1]

    # Matriz das restrições de igualdade
    A_eq = [
        [1, 1, 1],  # x1 + x2 + x3 = 12
    ]

    # Vetor das restrições de igualdade
    b_eq = [12]

    # Limites das variáveis
    x_bounds = (0, None)
    bounds = [x_bounds, x_bounds, x_bounds]

    # Resolver o problema
    res = linprog(
        c,  # Coeficientes da função objetivo
        A_ub=A,  # Matriz de restrições de desigualdade
        b_ub=b,  # Vetor de termos independentes das restrições de desigualdade
        A_eq=A_eq,  # Matriz de restrições de igualdade
        b_eq=b_eq,  # Vetor de termos independentes das restrições de igualdade
        bounds=bounds,  # Limites das variáveis
        method='highs'  # Método de otimização (highs)
    )

    # Imprimir os resultados
    if res.success:
        print("Solução ótima encontrada:")
        print(f"x* = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f})")

        plot_2d_problema_5(res)
        plot_3d_problema_5(res)
    else:
        print("Não foi possível encontrar uma solução ótima.")

    return res


def problema_6():
    print("Não existe o enunciado do Problema 6 =(")


def problema_7():
    """
    Resolve o Problema 7 de otimização linear, maximizando a função objetivo 9x1 + 5x2

        Max f(x) = 9x1 + 5x2

    sujeita a restrições trigonométricas:

        sin(k/13)x1 + cos(k/13)x2 ≤ 7, k = 1, 2, ..., 13
        x1, x2 ≥ 0

    Restrições reescritas:

        sin(1/13)x1 + cos(1/13)x2 ≤ 7
        sin(2/13)x1 + cos(2/13)x2 ≤ 7
        sin(3/13)x1 + cos(3/13)x2 ≤ 7
        sin(4/13)x1 + cos(4/13)x2 ≤ 7
        sin(5/13)x1 + cos(5/13)x2 ≤ 7
        sin(6/13)x1 + cos(6/13)x2 ≤ 7
        sin(7/13)x1 + cos(7/13)x2 ≤ 7
        sin(8/13)x1 + cos(8/13)x2 ≤ 7
        sin(9/13)x1 + cos(9/13)x2 ≤ 7
        sin(10/13)x1 + cos(10/13)x2 ≤ 7
        sin(11/13)x1 + cos(11/13)x2 ≤ 7
        sin(12/13)x1 + cos(12/13)x2 ≤ 7
        sin(13/13)x1 + cos(13/13)x2 ≤ 7

        x1 ≥ 0
        x2 ≥ 0

    A solução ótima deste problema é x* = (8, 0) com f(x*) = 74.87.

    A função formula o problema no formato padrão de programação linear, convertendo o problema de maximização
    em um de minimização invertendo os coeficientes da função objetivo. Em seguida, utiliza o solver 'linprog'
    da biblioteca SciPy para encontrar a solução ótima.

    As restrições são geradas dinamicamente usando um loop, variando o valor de 'k' de 1 a 13 para criar as
    restrições trigonométricas.

    Por fim, plota gráficos 2D e 3D para visualizar a solução (funções não mostradas).

    Returns:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - 'x': array com os valores ótimos das variáveis de decisão (x1, x2)
            - 'fun': valor ótimo da função objetivo (multiplicado por -1 para obter o valor original da maximização)
    """

    # Coeficientes da função objetivo (invertidos para transformar o problema de maximização em minimização)
    c = [-9, -5]  # Original: 9x1 + 5x2

    # Matriz de coeficientes das restrições de desigualdade
    # Cada linha representa uma restrição, cada coluna uma variável.
    A_ub = []
    b_ub = []

    for k in range(1, 14):
        # Coeficientes da restrição trigonométrica
        a = [math.sin(k / 13), math.cos(k / 13)]

        # Adiciona a restrição à matriz de coeficientes das restrições de desigualdade
        A_ub.append(a)

        # Adiciona o termo independente à lista de termos independentes
        b_ub.append(7)

    # Limites das variáveis (todas não negativas)
    bounds = [(0, None), (0, None)]

    # Resolve o problema de PL usando o solver de alto desempenho 'highs'
    res = linprog(
        c,  # Coeficientes da função objetivo
        A_ub=A_ub,  # Matriz de restrições de desigualdade
        b_ub=b_ub,  # Lados direitos das restrições de desigualdade
        bounds=bounds,  # Limites das variáveis
        method='highs',  # Método de otimização (highs)
    )

    # Exibe a solução ótima encontrada (convertendo o valor da função objetivo de volta para a maximização)
    print(
        f'A solução ótima deste problema é x* = ({res.x[0]:.3f}, {res.x[1]:.0f}) com f(x*) = {-res.fun:.2f}.'
    )

    # Chama funções para plotar gráficos 2D e 3D da solução
    plot_2d_problema_7(res)
    plot_3d_problema_7(res)

    # Retorna o objeto com os resultados da otimização (incluindo a solução ótima e o valor da função objetivo)
    return res


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
