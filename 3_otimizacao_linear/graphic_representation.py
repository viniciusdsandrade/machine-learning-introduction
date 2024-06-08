import plotly.graph_objects as go
import numpy as np


def plot_2d_problema_1(res):
    """
    Plota a região factível e a solução ótima do Problema 1 em 2D.

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando a biblioteca Plotly.
    O gráfico exibe a região factível do Problema 1, definida pelas restrições do problema,
    e destaca a solução ótima encontrada pela função 'linprog'.

    Args:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Determina as restrições do Problema 1 e as converte em equações para plotagem.
        - Cria um gráfico Plotly e adiciona as retas que representam as restrições do problema.
        - Plota a solução ótima como um ponto destacado em vermelho na forma de uma estrela.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo zoom, pan e outras interações.

    Retorna:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res’) foi obtido para o Problema 1.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo, que oferece recursos
          avançados de visualização.
    """

    # Define os limites dos eixos
    x1_range = [-1, 6]
    x2_range = [-1, 8]
    restricoes = ['6 - 2 * x1', '4 - x1', '(10 - x1) / 5']  # Restrições do problema 1
    titulo = 'Problema 1 - Região Factível e Solução Ótima (2D)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # Adiciona as linhas das restrições com formatação
    for restricao in restricoes:
        x1 = np.linspace(x1_range[0], x1_range[1], 500)
        x2 = eval(restricao)
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


def plot_3d_problema_1(res):
    """
    Plota a região factível, a solução ótima e a função objetivo do Problema 1 em 3D.

    Esta função cria um gráfico interativo em três dimensões (3D) utilizando a biblioteca Plotly.
    O gráfico exibe a região factível do Problema 1, definida pelas restrições, e a superfície da
    função objetivo. A solução ótima é destacada como um ponto e conectada ao plano xy por uma
    linha tracejada.

    :arg
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1, x2 e z (valor da função objetivo) para abranger a região de interesse.
        - Determina as restrições do Problema 1 e as converte em equações para plotagem em 3D.
        - Cria um gráfico Plotly 3D e adiciona as superfícies que representam as restrições.
        - Plota a superfície da função objetivo, colorida de acordo com seus valores.
        - Plota a solução ótima como um ponto destacado em vermelho e uma linha vertical tracejada
          que a conecta ao plano xy.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo rotações, zoom e outras interações.

    :return
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 1.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo 3D, que oferece recursos
          avançados de visualização.
    """

    # Define os limites dos eixos
    x1_range = [-1, 6]
    x2_range = [-1, 8]
    funcao_objetivo = '5 * X1 + X2'  # Função objetivo do problema 1
    restricoes_3d = {'2x1 + x2 <= 6': '6 - 2 * X1 - X2', 'x1 + x2 <= 4': '4 - X1 - X2',
                     'x1 + 5x2 >= 10': '(10 - X1 - 5 * X2) / -1'}  # Restrições 3D
    titulo = 'Problema 1 - Região Factível e Solução Ótima (3D)'
    solucao_otima_nome = 'Solução ótima'

    # Cria os pontos para plotar os planos das restrições
    n = 100
    x1 = np.linspace(x1_range[0], x1_range[1], n)
    x2 = np.linspace(x2_range[0], x2_range[1], n)
    X1, X2 = np.meshgrid(x1, x2)

    # Calcula Z para a função objetivo
    Z_obj = eval(funcao_objetivo)

    fig = go.Figure()

    # Adiciona a superfície da função objetivo
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z_obj, name='Função Objetivo', colorscale='viridis'))

    # Adiciona as superfícies das restrições
    for nome, restricao_z in restricoes_3d.items():
        Z = eval(restricao_z)
        fig.add_trace(go.Surface(x=X1, y=X2, z=Z, name=nome, showscale=False))

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
        ),
        title=titulo
    )
    fig.show()


def plot_2d_problema_2(res):
    """
    Plota a região factível e a solução ótima do Problema 2 em 2D.

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando a biblioteca Plotly.
    O gráfico exibe a região factível do Problema 2, definida pelas restrições do problema,
    e destaca a solução ótima encontrada pela função 'linprog'.

    :param res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.
    :type res: Scipy.optimize.OptimizeResult

    :returns: None (exibe o gráfico diretamente)

    :raises: ImportError: Se a biblioteca Plotly não estiver instalada.

    :notes:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 2.
        - As restrições do problema são representadas por linhas retas no gráfico.
        - A região factível é a área do gráfico que satisfaz todas as restrições simultaneamente.
        - A solução ótima é o ponto na região factível que maximiza (ou minimiza, dependendo do problema)
          a função objetivo.
    """

    # Define os limites dos eixos
    x1_range = [-1, 6]
    x2_range = [-1, 4]
    restricoes = ['(6 - x1) / 2', '2 * x1 - 8']  # Restrições do problema 2
    titulo = 'Problema 2 - Região Factível e Solução Ótima (2D)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # Adiciona as linhas das restrições com formatação
    for restricao in restricoes:
        x1 = np.linspace(x1_range[0], x1_range[1], 100)
        x2 = eval(restricao)
        fig.add_trace(go.Scatter(x=x1, y=x2, mode='lines', name=restricao, line=dict(width=2)))

    # Plota a solução ótima com formatação (corrigido para x∗ = (4, 0))
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[0],  # Corrigido para y = 0
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


def plot_3d_problema_2(res):
    """
    Plota a região factível, a solução ótima e a função objetivo do Problema 2 em 3D.

    Esta função cria um gráfico interativo em três dimensões (3D) utilizando a biblioteca Plotly.
    O gráfico exibe a região factível do Problema 2, definida pelas restrições, e a superfície da
    função objetivo. A solução ótima é destacada como um ponto e conectada ao plano xy por uma
    linha tracejada.

    :param res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.
    :type res: Scipy.optimize.OptimizeResult

    :returns: None (exibe o gráfico diretamente)

    :raises: ImportError: Se a biblioteca Plotly não estiver instalada.

    :notes:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 2.
        - As restrições do problema são representadas por planos no gráfico 3D.
        - A função objetivo é representada por uma superfície colorida.
        - A solução ótima é o ponto na região factível onde a função objetivo atinge seu valor máximo.
    """

    # Define os limites dos eixos
    x1_range = [-1, 6]
    x2_range = [-1, 4]
    funcao_objetivo = '2 * X1 - 3 * X2'  # Função objetivo do problema 2 corrigida
    restricoes_3d = {'x1 + 2x2 <= 6': '6 - X1 - 2 * X2', '2x1 - x2 <= 8': '8 - 2 * X1 + X2'}  # Restrições 3D
    titulo = 'Problema 2 - Região Factível e Solução Ótima (3D)'
    solucao_otima_nome = 'Solução ótima'

    # Cria os pontos para plotar os planos das restrições
    n = 100
    x1 = np.linspace(x1_range[0], x1_range[1], n)
    x2 = np.linspace(x2_range[0], x2_range[1], n)
    X1, X2 = np.meshgrid(x1, x2)

    # Calcula Z para a função objetivo (corrigido)
    Z_obj = eval(funcao_objetivo)

    fig = go.Figure()

    # Adiciona a superfície da função objetivo
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z_obj, name='Função Objetivo', colorscale='viridis'))

    # Adiciona as superfícies das restrições
    for nome, restricao_z in restricoes_3d.items():
        Z = eval(restricao_z)
        fig.add_trace(go.Surface(x=X1, y=X2, z=Z, name=nome, showscale=False))

    # Plota a solução ótima (corrigido para x∗ = (4, 0))
    fig.add_trace(go.Scatter3d(x=[res.x[0]], y=[0], z=[res.fun],  # Corrigido para y = 0
                               mode='markers', marker=dict(size=10, color='red'),
                               name=solucao_otima_nome))

    # Adiciona uma linha tracejada vertical da solução ótima até o plano xy
    fig.add_trace(go.Scatter3d(x=[res.x[0], res.x[0]], y=[0, 0], z=[0, res.fun],  # Corrigido para y = 0
                               mode='lines', line=dict(color='red', dash='dash'), showlegend=False))

    # Configura o layout do gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title='x1',
            yaxis_title='x2',
            zaxis_title='f(x1, x2)',
        ),
        title=titulo
    )
    fig.show()


def plot_2d_problema_3(res):
    """
    Plota a região factível, a solução ótima e a restrição principal do Problema 3 em 2D (com x3 = 0).

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando a biblioteca Plotly.
    O gráfico exibe a região factível do Problema 3, considerando x3 fixo em 0, definida pela
    restrição principal do problema, e destaca a solução ótima encontrada pela função 'linprog'.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Determina a restrição principal do Problema 3 (simplificada para x3 = 0) e a converte em
          uma equação para plotagem.
        - Cria um gráfico Plotly e adiciona uma reta que representa a restrição principal.
        - Plota a solução ótima como um ponto destacado em vermelho.
        - Preenche a região factível com uma cor clara para facilitar a visualização.
        - Plota curvas de nível da função objetivo para mostrar a direção de crescimento da função.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo zoom, pan e outras interações.

    :return:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 3.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo, que oferece recursos
          avançados de visualização.
        - A restrição principal do problema é representada por uma linha reta no gráfico.
        - A região factível é a área triangular do gráfico que satisfaz a restrição e os limites
          das variáveis (0 ≤ x1, x2 ≤ 1).
        - A solução ótima é o ponto na região factível que maximiza a função objetivo.
        - As curvas de nível da função objetivo ajudam a visualizar como a função cresce em diferentes
          direções dentro da região factível.
    """

    # Define os limites dos eixos e outros parâmetros com base no problema 3
    x1_range = [0, 1.2]
    x2_range = [0, 2.2]
    restricoes = ['3*x1 - x1 - x2']  # Restrição principal do problema 3 (simplificada para x3 = 0)
    titulo = 'Problema 3 - Região Factível e Solução Ótima (2D)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # Cria uma grade 2D para x1 e x2
    x1 = np.linspace(x1_range[0], x1_range[1], 100)
    x2 = np.linspace(x2_range[0], x2_range[1], 100)
    X1, X2 = np.meshgrid(x1, x2)

    # Calcula Z_objetivo para a grade 2D (considerando x3 = 0)
    Z_objetivo = 15 * (X1 + 2 * X2) + 11 * X2

    # Adiciona as curvas de nível da função objetivo
    fig.add_trace(go.Contour(x=x1, y=x2, z=Z_objetivo,
                             contours=dict(start=Z_objetivo.min(), end=Z_objetivo.max(), size=5),
                             colorscale='viridis', name='Função Objetivo'))

    # Adiciona a região viável como um shape
    fig.add_trace(go.Scatter(x=[0, 1, 1, 0, 0], y=[0, 2, 1, 0, 0], fill="toself",
                             fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável'))

    # Adiciona as linhas das restrições (apenas a que define a reta)
    for restricao in restricoes:
        if "x1" in restricao:
            x2_reta = 2 * x1  # Calcula x2 com base na restrição 3x1 >= x1 + x2 (simplificada)
            fig.add_trace(go.Scatter(x=x1, y=x2_reta, mode='lines', name=restricao))
        else:
            pass  # As demais restrições são os limites do quadrado

    # Plota a solução ótima
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                             marker=dict(size=10, color='red'), name=solucao_otima_nome))

    # Configura o layout do gráfico
    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title=titulo,
        xaxis=dict(range=[x1_range[0] - 0.2, x1_range[1] + 0.2]),  # Ajusta o zoom do eixo x
        yaxis=dict(range=[x2_range[0] - 0.2, x2_range[1] + 0.2])  # Ajusta o zoom do eixo y
    )

    fig.show()


def plot_2d_problema_4(res):
    """
    Plota uma representação 2D simplificada do Problema 4.

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando a biblioteca Plotly.
    O gráfico exibe uma visualização simplificada do Problema 4, fixando as variáveis x3 e x4 em 0.
    A região viável aproximada e a solução ótima projetada no plano x1-x2 são mostradas.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Determina as restrições relevantes para a visualização 2D com x3 = x4 = 0.
        - Cria um gráfico Plotly e adiciona as retas que representam as restrições simplificadas.
        - Plota a solução ótima projetada (com x3 = x4 = 0) como um ponto destacado em vermelho.
        - Preenche uma região aproximada da região viável com uma cor clara para facilitar a visualização.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo zoom, pan e outras interações.

    :return:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 4.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo, que oferece recursos
          avançados de visualização.
        - A região viável exibida é uma aproximação, pois não considera todas as restrições do problema original.
        - A solução ótima projetada é o ponto no plano x1-x2 que corresponde à solução ótima do problema
          original, com as variáveis x3 e x4 fixadas em 0.
    """
    fig = go.Figure()

    # Cria uma grade 2D para x1 e x2
    x1 = np.linspace(0, 400, 400)
    x2 = np.linspace(0, 200, 200)  # x2 <= x1 / 2
    X1, X2 = np.meshgrid(x1, x2)

    # Restrições
    fig.add_trace(go.Scatter(x=x1, y=x1 / 2, mode='lines', name='x1 - 2x2 >= 0'))
    fig.add_trace(go.Scatter(x=x1, y=400 - x1, mode='lines', name='x1 + x2 <= 400 (com x3=x4=0)'))

    # Região Viável (aproximada, pois outras restrições não estão sendo visualizadas)
    fig.add_trace(go.Scatter(x=[0, 200, 400, 0], y=[0, 100, 0, 0],
                             fill="toself", fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável (aproximada)'))

    # Solução Ótima Projetada
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                             marker=dict(size=10, color='red'), name='Solução Ótima Projetada'))

    # Configura o layout do gráfico
    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title="Problema 4 - Visualização 2D (x3=0, x4=0)"
    )
    fig.show()


def plot_3d_problema_4(res):
    """
    Plota uma representação 3D simplificada do Problema 4.

    Esta função cria um gráfico interativo em três dimensões (3D) utilizando a biblioteca Plotly.
    O gráfico exibe uma visualização simplificada do Problema 4, fixando a variável x4 em 0.
    A solução ótima projetada no espaço x1-x2-x3 é mostrada.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.

    Funcionalidades:
        - Cria um gráfico Plotly 3D.
        - Plota a solução ótima projetada (com x4 = 0) como um ponto destacado em vermelho.
        - Configura os rótulos dos eixos (x1, x2, x3) e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo rotações, zoom e outras interações.

    :return:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 4.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo 3D, que oferece recursos
          avançados de visualização.
        - A visualização é simplificada, pois não inclui as restrições do problema original, que são
          complexas de representar em 3D.
        - A solução ótima projetada é o ponto no espaço x1-x2-x3 que corresponde à solução ótima do problema
          original, com a variável x4 fixada em 0.
    """
    fig = go.Figure()

    # Solução Ótima
    fig.add_trace(go.Scatter3d(x=[res.x[0]], y=[res.x[1]], z=[res.x[2]], mode='markers',
                               marker=dict(size=10, color='red'), name='Solução Ótima'))

    # Configura o layout do gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="x3",
        ),
        title="Problema 4 - Visualização 3D (x4=0)"
    )
    fig.show()


def plot_2d_problema_5(res):
    """
    Plota uma representação 2D simplificada do Problema 5.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.
    """
    fig = go.Figure()

    # Gerando pontos para as retas
    x1 = np.linspace(0, 12, 100)

    # Restrição: x1 + 1 ≤ x2
    x2_rest1 = x1 + 1

    # Restrição: x1 + x2 ≤ 12 (considerando x3 = 0)
    x2_rest2 = 12 - x1

    # Plotando as restrições
    fig.add_trace(go.Scatter(x=x1, y=x2_rest1, mode='lines', name='x1 + 1 ≤ x2'))
    fig.add_trace(go.Scatter(x=x1, y=x2_rest2, mode='lines', name='x1 + x2 ≤ 12 (x3=0)'))

    # Região Viável (aproximada)
    fig.add_trace(go.Scatter(x=[0, 11, 12, 0], y=[1, 0, 12, 1], fill="toself",
                             fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável (aproximada)'))

    # Solução Ótima Projetada (com x3 = 0)
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                             marker=dict(size=10, color='red'), name='Solução Ótima Projetada'))

    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title="Problema 5 - Visualização 2D (x3=0)"
    )
    fig.show()


def plot_3d_problema_5(res):
    """
    Plota a região factível, a solução ótima e as restrições do Problema 5 em 3D.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog', contendo a solução ótima do problema.
    """
    fig = go.Figure()

    # Gerando pontos para os planos
    x1 = np.linspace(0, 12, 100)
    x2 = np.linspace(0, 12, 100)
    X1, X2 = np.meshgrid(x1, x2)

    # Restrição 1: x1 + 1 ≤ x2 → x2 >= x1 + 1
    Z1 = X1 + 1

    # Restrição 2: x2 + 1 ≤ x3 → x3 >= x2 + 1
    Z2 = X2 + 1

    # Restrição 3: x1 + x2 + x3 = 12 -> x3 = 12 - x1 - x2
    Z3 = 12 - X1 - X2

    # Plotando os planos das restrições
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z1, opacity=0.5, showscale=False, name='x2 >= x1 + 1'))
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z2, opacity=0.5, showscale=False, name='x3 >= x2 + 1'))
    fig.add_trace(go.Surface(x=X1, y=X2, z=Z3, opacity=0.5, showscale=False, name='x3 = 12 - x1 - x2'))

    # Solução Ótima
    fig.add_trace(go.Scatter3d(x=[res.x[0]], y=[res.x[1]], z=[res.x[2]], mode='markers',
                               marker=dict(size=10, color='red'), name='Solução Ótima'))

    fig.update_layout(
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="x3",
        ),
        title="Problema 5 - Visualização 3D"
    )
    fig.show()
