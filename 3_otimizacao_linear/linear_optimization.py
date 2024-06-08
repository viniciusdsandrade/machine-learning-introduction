import numpy as np
import plotly.graph_objects as go
from scipy.optimize import linprog


def problema_1():
    """
    Min f(x1, x2) = 5x1 + x2

    sujeita às seguintes restrições:

    * 2x1 + x2 <= 6
    * x1 + x2  <= 4
    * x1 + 5x2 >= 10
    * x1, x2   >= 0
    """
    c = [5, 1]
    A = [[-2, -1], [-1, -1], [-1, -5]]
    b = [-6, -4, -10]
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    res = linprog(
        c,
        A_ub=A,
        b_ub=b,
        bounds=[x0_bounds, x1_bounds],
        method='highs',
    )

    print(f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x∗) = {res.fun:.0f}.')

    # Plotagem dos gráficos 2D e 3D
    plot_2d(res, [-1, 6], [-1, 8], ['6 - 2 * x1', '4 - x1', '(10 - x1) / 5'],
            'Problema 1 - Região Factível e Solução Ótima (2D)')
    plot_3d(res, [-1, 6], [-1, 8], '5 * X1 + X2',
            {'2x1 + x2 <= 6': '6 - 2 * X1 - X2', 'x1 + x2 <= 4': '4 - X1 - X2',
             'x1 + 5x2 >= 10': '(10 - X1 - 5 * X2) / -1'},
            'Problema 1 - Região Factível e Solução Ótima (3D)')
    return res


def problema_2():
    """
    Max f(x1, x2) = 2x1 + 3x2

    sujeita às seguintes restrições:

    * x1 + 2x2 <= 6
    * 2x1 - x2 <= 8
    * x1, x2   >= 0
    """
    c = [-2, -3]  # Coeficientes invertidos para maximização
    A = [[1, 2], [2, -1]]
    b = [6, 8]
    x0_bounds = (0, None)
    x1_bounds = (0, None)

    res = linprog(
        c,
        A_ub=A,
        b_ub=b,
        bounds=[x0_bounds, x1_bounds],
        method='highs'
    )

    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}) com f(x∗) = {-res.fun:.0f}.')

    # Plotagem dos gráficos 2D e 3D
    plot_2d(res, [-1, 5], [-1, 8], ['6 - x1 / 2', '2*x1 - 8'],
            'Problema 2 - Região Factível e Solução Ótima (2D)')
    plot_3d(res, [-1, 5], [-1, 8], '-2 * X1 + 3 * X2',  # Função objetivo invertida para visualização
            {'x1 + 2x2 <= 6': '6 - X1 - 2 * X2', '2x1 - x2 <= 8': '2 * X1 - X2 - 8'},
            'Problema 2 - Região Factível e Solução Ótima (3D)', 'Ponto de Máximo')
    return res


# Função para plotar um gráfico 2D interativo
def plot_2d(res, x1_range, x2_range, restricoes, titulo, solucao_otima_nome="Solução ótima"):
    """
    Plota a região factível e a solução ótima em 2D.
    """
    fig = go.Figure()

    # Adiciona as linhas das restrições com formatação
    for restricao in restricoes:
        x1 = np.linspace(x1_range[0], x1_range[1], 2)
        x2 = eval(restricao)  # Avalia a expressão da restrição para x2
        fig.add_trace(go.Scatter(x=x1, y=x2, mode='lines', name=restricao, line=dict(width=2)))

    # Plota a solução ótima com formatação
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]],
                             mode='markers',
                             marker=dict(size=12, color='red', symbol='star'),
                             name=solucao_otima_nome))

    # Define a área visível do gráfico
    fig.update_xaxes(range=x1_range)
    fig.update_yaxes(range=x2_range)

    # Adiciona um título ao gráfico
    fig.update_layout(
        xaxis_title='x1',
        yaxis_title='x2',
        title=titulo
    )
    fig.show()


# Função para plotar um gráfico 3D interativo
def plot_3d(res, x1_range, x2_range, funcao_objetivo, restricoes_3d, titulo, solucao_otima_nome="Solução ótima"):
    """
    Plota a região factível, a solução ótima e a função objetivo em 3D interativo.
    """
    # Cria os pontos para plotar os planos das restrições
    n = 100  # Número de pontos na grade
    x1 = np.linspace(x1_range[0], x1_range[1], n)
    x2 = np.linspace(x2_range[0], x2_range[1], n)
    X1, X2 = np.meshgrid(x1, x2)

    # Calcula Z para a função objetivo
    Z_obj = eval(funcao_objetivo)

    # Cria o gráfico 3D interativo
    fig = go.Figure()

    # Adiciona a superfície da função objetivo
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z_obj, name='Função Objetivo', opacity=0.5, colorscale='viridis'))

    # Adiciona as superfícies das restrições
    for nome, restricao_z in restricoes_3d.items():
        Z = eval(restricao_z)  # Avalia a expressão da restrição para Z
        fig.add_trace(go.Surface(x=X1, y=X2, z=Z, name=nome, opacity=0.5, showscale=False))

    # Plota a solução ótima
    fig.add_trace(go.Scatter3d(x=[res.x[0]], y=[res.x[1]], z=[res.fun],
                               mode='markers', marker=dict(size=10, color='red'),
                               name=solucao_otima_nome))

    # Adiciona uma linha tracejada vertical da solução ótima até o plano xy
    fig.add_trace(go.Scatter3d(x=[res.x[0], res.x[0]], y=[res.x[1], res.x[1]], z=[0, res.fun],
                               mode='lines', line=dict(color='red', dash='dash'), showlegend=False))

    # Configura o layout do gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title='x1',
            yaxis_title='x2',
            zaxis_title='f(x1, x2)',
            camera=dict(eye=dict(x=2, y=2, z=1))  # Ajusta a visualização inicial
        ),
        title=titulo
    )
    fig.show()


def problema_3():
    """
    Max f(x1, x2, x3) = 15(x1 + 2x2) + 11(x2 -x3)

    sujeita as seguintes restrições:

    * 3x1 >=x1 +x2 + x3
    * 0 <= xj <= 1, j = 1, 2, 3

    A solução ótima deste problema é x∗ = (1, 1, 0) com f(x∗) = 56.
    :return:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - x: array com os valores ótimos das variáveis x1, x2 e x3.
            - fun: valor ótimo da função objetivo.
    """
    c = [-15, -41, 11]  # Coeficientes da função objetivo (a serem minimizados)
    A = [[-2, -1, -1]]  # Coeficientes das restrições de desigualdade
    b = [-3]  # Termos independentes das restrições de desigualdade
    x_bounds = [(0, 1), (0, 1), (0, 1)]  # Limites das variáveis (entre 0 e 1)

    res = linprog(
        c,
        A_ub=A,
        b_ub=b,
        bounds=x_bounds,
        method='highs',
        options={'disp': False}
    )

    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x∗) = {-res.fun:.0f}.')

    return res


def problema_4():
    """
    Min f(x1, x2, x3, x4) = 10(x3 + x4)

    sujeita às seguintes restrições:

    * ∑xj = 400 de 1 a 4
    * xj − 2xj+1 ≥ 0, j = 1, 2, 3
    * xj ≥ 0, j = 1, 2, 3, 4

    A solução ótima deste problema é x∗ = (400, 0, 0, 0) com f(x∗) = 0.

    :return:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - x: array com os valores ótimos das variáveis x1, x2, x3 e x4.
            - fun: valor ótimo da função objetivo.
    """
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
    res = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method='highs',
        options={'disp': False}
    )
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}, {res.x[3]:.0f}) com '
        f'f(x∗) = {res.fun:.0f}.')


def problema_5():
    """
     Max f(x1, x2, x3) = -5x1 + 3(x1 + x3) - 2x2

    sujeita às seguintes restrições:

    * xj + 1 <= xj+1 -> j = 1, 2
    * ∑xj = 12 de 1 a 3  -> j = 1, 2, 3
    * xj >= 0 -> j = 1, 2, 3

    A solução ótima deste problema é x∗ = (0, 1, 11) com f(x∗) = 36.

    :return:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - x: array com os valores ótimos das variáveis x1, x2 e x3.
            - fun: valor ótimo da função objetivo.
    """
    from scipy.optimize import linprog
    c = [2, 0, -3]  # Invertido para maximização
    A_ub = [[1, -1, 0], [0, 1, -1]]  # Coeficientes das restrições de desigualdade
    b_ub = [-1, -1]  # Termos independentes das restrições de desigualdade
    A_eq = [[1, 1, 1]]  # Coeficientes das restrições de igualdade
    b_eq = [12]  # Termos independentes das restrições de igualdade
    bounds = [(0, None), (0, None), (0, None)]  # Limites das variáveis (>= 0)
    res = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        A_eq=A_eq,
        b_eq=b_eq,
        bounds=bounds,
        method='highs',
        options={'disp': False}
    )
    print(
        f'A solução ótima deste problema é x∗ = ({res.x[0]:.0f}, {res.x[1]:.0f}, {res.x[2]:.0f}) com f(x∗) = {res.fun:.0f}.'
    )


def problema_6():
    print("Não existe o enunciado do Problema 6 =(")


def problema_7():
    """
    Maximizar f(x) = 9x1 + 5x2

    sujeito a:
    * sin(k/13)x1 + cos(k/13)x2 <= 7, k = 1, 2, ..., 13
    * x1, x2 >= 0

    A solução ótima deste problema é x∗ = (0, 1, 11) com f(x∗) = 36.

    :return:
        OptimizeResult: Objeto contendo os resultados da otimização, incluindo:
            - x: array com os valores ótimos das variáveis x1 e x2.
            - fun: valor ótimo da função objetivo.
    """

    # Coeficientes da função objetivo (a serem minimizados)
    c = [-9, -5]

    # Coeficientes das restrições de desigualdade
    A_ub = np.array([[np.sin(k / 13), np.cos(k / 13)] for k in range(1, 14)])

    # Termos independentes das restrições de desigualdade
    b_ub = np.array([7] * 13)

    # Limites inferiores das variáveis (x1, x2 >= 0)
    bounds = [(0, None), (0, None)]

    # Resolve o problema de programação linear
    res = linprog(
        c,
        A_ub=A_ub,
        b_ub=b_ub,
        bounds=bounds,
        method="highs",
        options={'disp': False}
    )

    if res.success:
        print(f'A solução ótima deste problema é x∗ = ({res.x[0]:.2f}, {res.x[1]:.2f}) com f(x∗) = {-res.fun:.2f}.')
    else:
        print("Otimização falhou. Status:", res.status)
        print("Mensagem:", res.message)

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

# https://docs.scipy.org/doc/scipy/reference/optimize.linprog-highs.html 13](1,2) Huangfu, Q., Galabova, I.,
# Feldmeier, M., and Hall, J. A. J. “HiGHS - high performance software for linear optimization.” https://highs.dev/ [
# 14] Huangfu, Q. and Hall, J. A. J. “Parallelizing the dual revised simplex method.” Mathematical Programming
# Computation, 10 (1), 119-142, 2018. DOI: 10.1007/s12532-017-0130-5 [15] Harris, Paula MJ. “Pivot selection methods
# of the Devex LP code.” Mathematical programming 5.1 (1973): 1-28. [16] Goldfarb, Donald, and John Ker Reid. “A
# practicable steepest-edge simplex algorithm.” Mathematical Programming 12.1 (1977): 361-371.
