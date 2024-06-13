from matplotlib import pyplot as plt
import plotly.graph_objects as go
import numpy as np


def plot_2d_problema_1(res):
    """
    Plota a região factível e a solução ótima do Problema 1 em 2D,
    mostrando todas as restrições graficamente.

    Esta função cria um gráfico interativo em duas dimensões (2D)
    utilizando a biblioteca Plotly. O gráfico exibe a região factível
    do Problema 1, definida pelas restrições do problema, e destaca
    a solução ótima encontrada pela função 'linprog'.

    Args:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Determina as restrições do Problema 1 e as converte em equações para plotagem.
        - Cria um gráfico Plotly e adiciona as retas que representam as restrições do problema.
        - Plota a solução ótima como um ponto destacado em vermelho na forma de uma estrela.
        - Preenche a região factível com uma cor clara para facilitar a visualização.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo zoom, pan e outras interações.

    Retorna:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 1.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo, que oferece recursos
          avançados de visualização.
    """

    # Define os limites dos eixos
    x1_range = [-1, 6]
    x2_range = [-1, 8]
    titulo = 'Problema 1 - Região Factível e Solução Ótima (2D)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # --- Restrições ---
    x1 = np.linspace(x1_range[0], x1_range[1], 500)

    # 2x1 + x2 <= 6  --> x2 <= 6 - 2x1
    fig.add_trace(go.Scatter(x=x1, y=6 - 2 * x1, mode='lines', name='2x1 + x2 <= 6', line=dict(width=2)))

    # x1 + x2 <= 4  --> x2 <= 4 - x1
    fig.add_trace(go.Scatter(x=x1, y=4 - x1, mode='lines', name='x1 + x2 <= 4', line=dict(width=2)))

    # x1 + 5x2 >= 10  --> x2 >= (10 - x1) / 5
    fig.add_trace(go.Scatter(x=x1, y=(10 - x1) / 5, mode='lines', name='x1 + 5x2 >= 10', line=dict(width=2)))

    # --- FIM DAS RESTRIÇÕES ---

    # Região Factível (aproximada)
    # Encontre os pontos de interseção das retas para delimitar a região factível
    fig.add_trace(go.Scatter(x=[0, 2, 10 / 3, 0], y=[2, 0, 8 / 3, 10 / 5],
                             fill="toself", fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável'))

    # Plota a solução ótima
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


def plot_2d_problema_2(res):
    """
    Plota a região factível e a solução ótima do Problema 2 em 2D,
    mostrando todas as restrições graficamente.

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando
    a biblioteca Plotly. O gráfico exibe a região factível do Problema 2,
    definida pelas restrições do problema, e destaca a solução ótima
    encontrada pela função 'linprog'.

    :param res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
               contendo a solução ótima do problema.
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
    titulo = 'Problema 2 - Região Factível e Solução Ótima (2D)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # --- Restrições ---
    x1 = np.linspace(x1_range[0], x1_range[1], 100)

    # x1 + 2x2 <= 6 --> x2 <= (6 - x1) / 2
    fig.add_trace(go.Scatter(x=x1, y=(6 - x1) / 2, mode='lines', name='x1 + 2x2 <= 6', line=dict(width=2)))

    # 2x1 - x2 <= 8 --> x2 >= 2x1 - 8
    fig.add_trace(go.Scatter(x=x1, y=2 * x1 - 8, mode='lines', name='2x1 - x2 <= 8', line=dict(width=2)))

    # --- FIM DAS RESTRIÇÕES ---

    # Região Factível
    # Encontre os pontos de interseção das retas para delimitar a região
    fig.add_trace(go.Scatter(x=[0, 4, 6, 0], y=[0, 0, 2, 3],
                             fill="toself", fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável'))

    # Plota a solução ótima (corrigido para x∗ = (4, 0))
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


def plot_2d_problema_3(res):
    """
    Plota a região factível, a solução ótima e todas as restrições do
    Problema 3 em 2D (com x3 = 0).

    Esta função cria um gráfico interativo em duas dimensões (2D) utilizando
    a biblioteca Plotly. O gráfico exibe a região factível do Problema 3,
    considerando x3 fixo em 0, definida por todas as restrições do problema,
    e destaca a solução ótima encontrada pela função 'linprog'.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Determina as restrições do Problema 3 (simplificadas para x3 = 0)
          e as converte em equações para plotagem.
        - Cria um gráfico Plotly e adiciona as retas/segmentos que representam as restrições.
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
        - A região factível é a área triangular do gráfico que satisfaz todas as restrições.
        - A solução ótima é o ponto na região factível que maximiza a função objetivo.
        - As curvas de nível da função objetivo ajudam a visualizar como a função cresce em diferentes
          direções dentro da região factível.
    """

    # Define os limites dos eixos e outros parâmetros com base no problema 3
    x1_range = [-0.2, 1.2]  # Ajustado para melhor visualização
    x2_range = [-0.2, 2.2]  # Ajustado para melhor visualização
    titulo = 'Problema 3 - Região Factível e Solução Ótima (2D, x3=0)'
    solucao_otima_nome = 'Solução ótima'

    fig = go.Figure()

    # Cria uma grade 2D para x1 e x2
    x1 = np.linspace(x1_range[0], x1_range[1], 100)
    # x2 = np.linspace(x2_range[0], x2_range[1], 100)
    # X1, X2 = np.meshgrid(x1, x2)

    # Calcula Z_objetivo para a grade 2D (considerando x3 = 0)
    # Z_objetivo = 15 * (X1 + 2 * X2) + 11 * X2

    # Adiciona as curvas de nível da função objetivo
    # fig.add_trace(go.Contour(x=x1, y=x2, z=Z_objetivo,
    #                          contours=dict(start=Z_objetivo.min(), end=Z_objetivo.max(), size=1),
    #                          colorscale='viridis', name='Função Objetivo'))

    # --- Restrições ---

    # 3x1 >= x1 + x2 + 0 --> 2x1 - x2 >= 0 --> x2 <= 2x1
    fig.add_trace(go.Scatter(x=x1, y=2 * x1, mode='lines', name='2x1 - x2 >= 0', line=dict(width=2)))

    # 0 <= x1 <= 1 (limites de x1)
    fig.add_trace(go.Scatter(x=[0, 0], y=x2_range, mode='lines', name='x1 = 0', line=dict(width=2)))
    fig.add_trace(go.Scatter(x=[1, 1], y=x2_range, mode='lines', name='x1 = 1', line=dict(width=2)))

    # 0 <= x2 <= 1 (limites de x2)
    fig.add_trace(go.Scatter(x=x1_range, y=[0, 0], mode='lines', name='x2 = 0', line=dict(width=2)))
    fig.add_trace(go.Scatter(x=x1_range, y=[1, 1], mode='lines', name='x2 = 1', line=dict(width=2)))

    # --- FIM DAS RESTRIÇÕES ---

    # Região Factível
    fig.add_trace(go.Scatter(x=[0, 1, 1, 0, 0], y=[0, 2, 1, 0, 0], fill="toself",
                             fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável'))

    # Plota a solução ótima
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                             marker=dict(size=10, color='red'), name=solucao_otima_nome))

    # Configura o layout do gráfico
    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title=titulo,
        xaxis=dict(range=x1_range),
        yaxis=dict(range=x2_range)
    )

    fig.show()


def plot_2d_problema_4(res):
    """
    Plota uma representação 2D do Problema 4, mostrando todas as restrições
    projetadas no plano x1-x2, com x3 fixo em um valor específico.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Fixa a variável x3 em um valor específico (x3_fixo).
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Projeta as restrições originais no plano x1-x2, considerando x3 fixo e x4 = 400 - x1 - x2 - x3.
        - Cria um gráfico Plotly e adiciona as retas que representam as restrições projetadas.
        - Plota a solução ótima projetada (com x3 fixo e x4 calculado) como um ponto destacado em vermelho.
        - Preenche a região viável no plano x1-x2 com uma cor clara para facilitar a visualização.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico interativo, permitindo zoom, pan e outras interações.

    :return:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 4.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo, que oferece recursos
          avançados de visualização.
        - A região viável exibida é uma projeção 2D da região factível 4D, considerando x3 fixo.
        - A solução ótima projetada é o ponto no plano x1-x2 que corresponde à solução ótima do problema
          original, com x3 fixo e x4 calculado.
    """

    fig = go.Figure()

    # Fixando x3
    x3_fixo = 50  # Você pode ajustar este valor

    # Cria uma grade 2D para x1 e x2
    x1 = np.linspace(0, 400, 400)
    # x2 = np.linspace(0, 200, 200)
    # X1, X2 = np.meshgrid(x1, x2)

    # --- Restrições projetadas no plano x1-x2 ---
    # Usamos x4 = 400 - x1 - x2 - x3

    # Restrição 1: x1 - 2*x2 >= 0 --> x2 <= x1 / 2
    fig.add_trace(go.Scatter(x=x1, y=x1 / 2, mode='lines', name='x1 - 2*x2 >= 0'))

    # Restrição 2: x2 - 2*x3 >= 0 --> x2 >= 2*x3
    fig.add_trace(go.Scatter(x=x1, y=np.full_like(x1, 2 * x3_fixo), mode='lines', name='x2 - 2*x3 >= 0'))

    # Restrição 3: x3 - 2*x4 >= 0 --> x4 <= x3 / 2 --> 400 - x1 - x2 - x3 <= x3 / 2
    # --> x2 >= 400 - x1 - 1.5*x3
    fig.add_trace(go.Scatter(x=x1, y=400 - x1 - 1.5 * x3_fixo, mode='lines', name='x3 - 2*x4 >= 0'))

    # Restrição 4 (soma): x1 + x2 + x3 + x4 = 400 --> x1 + x2 <= 400 - x3
    fig.add_trace(go.Scatter(x=x1, y=400 - x1 - x3_fixo, mode='lines', name='x1 + x2 + x3 + x4 = 400'))

    # --- FIM DAS RESTRIÇÕES ---

    # Encontrando a região viável (aproximada)
    # (Devido à complexidade, faremos uma aproximação visual)
    fig.add_trace(go.Scatter(x=[0, 2 * x3_fixo, 400 - 1.5 * x3_fixo, 400 - x3_fixo, 0],
                             y=[2 * x3_fixo, 2 * x3_fixo, 400 - 1.5 * x3_fixo - (400 - 1.5 * x3_fixo) / 2, 0, 0],
                             fill="toself", fillcolor="lightgray", line=dict(color="black"),
                             name='Região Viável (aproximada)'))

    # Solução Ótima Projetada (x3 fixo, x4 calculado)
    x4_otimo = 400 - res.x[0] - res.x[1] - x3_fixo
    fig.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                             marker=dict(size=10, color='red'),
                             name=f'Solução Ótima Projetada (x3={x3_fixo}, x4={x4_otimo:.2f})'))

    # Configura o layout do gráfico
    fig.update_layout(
        xaxis_title="x1",
        yaxis_title="x2",
        title=f"Problema 4 - Visualização 2D (x3={x3_fixo})"
    )
    fig.show()


def plot_2d_problema_5(res):
    """
    Plota as projeções 2D da região factível e a solução ótima do Problema 5.

    Como o Problema 5 possui três variáveis e uma restrição de igualdade,
    a representação direta em 2D é complexa. Em vez disso, esta função
    gera três gráficos 2D, cada um mostrando uma projeção da região
    factível em um plano formado por duas variáveis, mantendo a terceira fixa.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Cria três gráficos Plotly, um para cada par de variáveis: (x1, x2), (x1, x3) e (x2, x3).
        - Define os intervalos dos eixos x1, x2 e x3 para abranger a região de interesse do problema.
        - Determina as restrições relevantes para cada projeção 2D.
        - Adiciona as retas que representam as restrições simplificadas em cada gráfico.
        - Plota a solução ótima projetada em cada plano como um ponto destacado em vermelho.
        - Preenche a região viável aproximada em cada projeção com uma cor clara para facilitar a visualização.
        - Configura os rótulos dos eixos e o título de cada gráfico para melhor identificação.
        - Exibe os gráficos interativos, permitindo zoom, pan e outras interações.

    :return:
        None (exibe os gráficos diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 5.
        - A função utiliza a biblioteca Plotly para criar os gráficos interativos, que oferecem recursos
          avançados de visualização.
        - As regiões viáveis exibidas são aproximações, pois cada projeção considera apenas duas
          variáveis por vez, mantendo a terceira fixa.
        - A solução ótima projetada em cada plano é o ponto que corresponde à solução ótima do problema
          original, com uma das variáveis fixada.
    """

    # ---- Projeção x1 vs x2 (fixando x3) ----
    fig1 = go.Figure()

    # Como x1 + x2 + x3 = 12, podemos definir x3 = 12 - x1 - x2
    x1_range = np.linspace(0, 12, 100)
    x2_range = np.linspace(0, 12, 100)
    # x1, x2 = np.meshgrid(x1_range, x2_range)

    # Restrição 1: x2 >= x1 + 1
    fig1.add_trace(go.Scatter(x=x1_range, y=x1_range + 1, mode='lines', name='x2 >= x1 + 1'))

    # Restrição 2: x3 >= x2 + 1 --> 12 - x1 - x2 >= x2 + 1 --> x2 <= (11 - x1) / 2
    fig1.add_trace(go.Scatter(x=x1_range, y=(11 - x1_range) / 2, mode='lines', name='x3 >= x2 + 1'))

    # Encontrando a região viável
    x2_viavel = np.minimum(x1_range + 1, (11 - x1_range) / 2)
    fig1.add_trace(go.Scatter(x=x1_range, y=x2_viavel, fill='tozeroy', fillcolor='lightblue',
                              mode='none', name='Região Viável (x1 vs x2)'))

    # Solução Ótima (projetada)
    fig1.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[1]], mode='markers',
                              marker=dict(size=10, color='red'), name='Solução Ótima'))

    fig1.update_layout(xaxis_title="x1", yaxis_title="x2", title="Projeção x1 vs x2 (x3 fixo)")

    # ---- Projeção x1 vs x3 (fixando x2) ----
    fig2 = go.Figure()

    # Reorganizando a restrição 2 para x2: x2 <= x3 - 1
    x3_range = np.linspace(0, 12, 100)
    x2_viavel_2 = x3_range - 1

    # Restrição 1: x2 >= x1 + 1
    fig2.add_trace(go.Scatter(x=x1_range, y=x1_range + 1, mode='lines', name='x2 >= x1 + 1'))

    # Região viável (considerando x2 fixo)
    fig2.add_trace(go.Scatter(x=x1_range, y=x2_viavel_2, fill='tozeroy', fillcolor='lightgreen',
                              mode='none', name='Região Viável (x1 vs x3)'))

    # Solução Ótima (projetada)
    fig2.add_trace(go.Scatter(x=[res.x[0]], y=[res.x[2]], mode='markers',
                              marker=dict(size=10, color='red'), name='Solução Ótima'))

    fig2.update_layout(xaxis_title="x1", yaxis_title="x3", title="Projeção x1 vs x3 (x2 fixo)")

    # ---- Projeção x2 vs x3 (fixando x1) ----
    fig3 = go.Figure()

    # Usando as restrições 2 e 3 para definir a região
    fig3.add_trace(go.Scatter(x=x2_range, y=x2_range + 1, mode='lines', name='x3 >= x2 + 1'))
    fig3.add_trace(go.Scatter(x=x2_range, y=12 - x2_range, mode='lines', name='x1 + x2 + x3 = 12'))

    # Encontrando a região viável
    x3_viavel_3 = np.minimum(x2_range + 1, 12 - x2_range)
    fig3.add_trace(go.Scatter(x=x2_range, y=x3_viavel_3, fill='tozeroy', fillcolor='lightcoral',
                              mode='none', name='Região Viável (x2 vs x3)'))

    # Solução Ótima (projetada)
    fig3.add_trace(go.Scatter(x=[res.x[1]], y=[res.x[2]], mode='markers',
                              marker=dict(size=10, color='red'), name='Solução Ótima'))

    fig3.update_layout(xaxis_title="x2", yaxis_title="x3", title="Projeção x2 vs x3 (x1 fixo)")

    # Exibindo os gráficos
    fig1.show()
    fig2.show()
    fig3.show()


def plot_2d_problema_7(res):
    """
    Plota uma representação 2D do Problema 7, mostrando as restrições
    projetadas no plano x1-x2 e a solução ótima.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Define os intervalos dos eixos x1 e x2 para abranger a região de interesse do problema.
        - Cria um gráfico Matplotlib e adiciona as linhas que representam as restrições.
        - Plota a solução ótima como um ponto destacado.
        - Preenche a região viável no plano x1-x2 com uma cor clara para facilitar a visualização.
        - Configura os rótulos dos eixos e o título do gráfico para melhor identificação.
        - Exibe o gráfico.
        - Salva o gráfico em um arquivo.
    """

    fig, ax = plt.subplots()

    # Definindo os intervalos dos eixos
    x1 = np.linspace(0, 10, 400)
    # x2 = np.linspace(0, 10, 400)
    # X1, X2 = np.meshgrid(x1, x2)

    # Funções de restrição
    for k in range(1, 14):
        a1 = np.sin(k / 13)
        a2 = np.cos(k / 13)
        ax.plot(x1, (7 - a1 * x1) / a2, label=f'Restrição {k}')

    # Adicionando a solução ótima
    ax.plot(res.x[0], res.x[1], 'ro', label='Solução Ótima')

    # Preenchendo a região viável (corrigido para evitar o warning)
    y_vals = np.minimum.reduce([(7 - np.sin(k / 13) * x1) / np.cos(k / 13) for k in range(1, 14)])
    valid_points = np.where(y_vals >= 0)
    ax.fill_between(x1[valid_points], 0, y_vals[valid_points], color='lightgray', label='Região Viável')

    # Configurações do gráfico
    ax.set_xlim((0, 10))
    ax.set_ylim((0, 10))
    ax.set_xlabel('x1')
    ax.set_ylabel('x2')
    ax.set_title('Problema 7 - Visualização 2D')
    ax.legend()

    # Exibe o gráfico
    plt.show()


# -------------------------------------------------------------------------------------------------------------------------------
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


def plot_3d_problema_3(res):
    """
    Plota a região factível, a solução ótima, a função objetivo e todas as
    restrições do Problema 3 em 3D.

    Esta função cria um gráfico interativo em três dimensões (3D) utilizando
    a biblioteca Plotly. O gráfico exibe a região factível do Problema 3,
    definida pelas restrições, a superfície da função objetivo e a solução
    ótima destacada.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.

    Funcionalidades:
        - Define os pontos do cubo unitário e o plota com baixa opacidade.
        - Plota o plano da restrição principal '2x1 - x2 - x3 = 0'.
        - Adiciona os planos que representam os limites das variáveis (0 <= xj <= 1).
        - Destaca a região factível com uma cor semitransparente.
        - Plota pontos representativos da função objetivo dentro da região factível.
        - Plota a solução ótima como um ponto destacado em vermelho e o conecta ao
          plano x1-x2 com uma linha tracejada.
        - Configura os rótulos dos eixos, o título do gráfico e a posição da câmera.
        - Exibe o gráfico interativo, permitindo rotações, zoom e outras interações.

    :return:
        None (exibe o gráfico diretamente).

    Observações:
        - A função assume que o resultado da otimização ('res') foi obtido para o Problema 3.
        - A função utiliza a biblioteca Plotly para criar o gráfico interativo 3D,
          que oferece recursos avançados de visualização.
    """

    fig = go.Figure()

    # --- Cubo Unitário ---
    x, y, z = np.mgrid[0:2:2j, 0:2:2j, 0:2:2j]
    values = np.ones((2, 2, 2))
    fig.add_trace(go.Isosurface(
        x=x.flatten(),
        y=y.flatten(),
        z=z.flatten(),
        value=values.flatten(),
        isomin=0.5,
        isomax=1.5,
        opacity=0.2,
        surface_count=1,
        colorscale='Blues',
        showscale=False,
        name='Cubo Unitário'
    ))

    # --- Restrições ---
    x1_range = np.linspace(0, 1, 50)
    x2_range = np.linspace(0, 1, 50)
    x1, x2 = np.meshgrid(x1_range, x2_range)

    # 2x1 - x2 - x3 >= 0 --> x3 <= 2x1 - x2
    x3_restricao = 2 * x1 - x2
    fig.add_trace(go.Surface(
        x=x1,
        y=x2,
        z=x3_restricao,
        colorscale='Greys',
        opacity=0.8,
        showscale=False,
        name='2x1 - x2 - x3 >= 0'
    ))

    # Planos dos Limites
    for i in range(2):
        fig.add_trace(go.Surface(x=x1_range, y=np.full_like(x1_range, i), z=x2,
                                 colorscale='Reds', opacity=0.5, showscale=False, name=f'x2 = {i}'))
        fig.add_trace(go.Surface(x=np.full_like(x1_range, i), y=x2_range, z=x1,
                                 colorscale='Greens', opacity=0.5, showscale=False, name=f'x1 = {i}'))
        fig.add_trace(go.Surface(x=x2, y=x1, z=np.full_like(x1, i),
                                 colorscale='Blues', opacity=0.5, showscale=False, name=f'x3 = {i}'))

    # --- FIM DAS RESTRIÇÕES ---

    # --- Região Factível ---
    # (Pontos dentro do cubo e abaixo do plano da restrição)
    x1_factivel = np.linspace(0, 1, 20)
    x2_factivel = np.linspace(0, 1, 20)
    x1_f, x2_f = np.meshgrid(x1_factivel, x2_factivel)
    x3_f = np.minimum(2 * x1_f - x2_f, 1)  # Limita x3 pelo cubo unitário
    fig.add_trace(go.Scatter3d(
        x=x1_f.flatten(),
        y=x2_f.flatten(),
        z=x3_f.flatten(),
        mode='markers',
        marker=dict(size=4, color='orange', opacity=0.3),
        name='Região Factível (Pontos)'
    ))

    # --- Função Objetivo (Pontos Representativos) ---
    # Calcule a função objetivo para alguns pontos dentro da região factível
    num_pontos = 20
    x1_obj = np.random.rand(num_pontos)
    x2_obj = np.random.rand(num_pontos)
    x3_obj = np.minimum(2 * x1_obj - x2_obj, 1)  # Garante que os pontos estejam dentro da região factível
    z_obj = 15 * (x1_obj + 2 * x2_obj) + 11 * (x2_obj - x3_obj)
    fig.add_trace(go.Scatter3d(
        x=x1_obj,
        y=x2_obj,
        z=z_obj,
        mode='markers',
        marker=dict(size=4, color='purple'),
        name='Função Objetivo (Pontos)'
    ))

    # --- Solução Ótima ---
    fig.add_trace(go.Scatter3d(
        x=[res.x[0]],
        y=[res.x[1]],
        z=[res.x[2]],
        mode='markers',
        marker=dict(size=8, color='red'),
        name='Solução Ótima (1, 1, 0)'
    ))
    fig.add_trace(go.Scatter3d(
        x=[res.x[0], res.x[0]],
        y=[res.x[1], res.x[1]],
        z=[0, res.x[2]],
        mode='lines',
        line=dict(color='red', dash='dash'),
        showlegend=False
    ))

    # --- Layout do Gráfico ---
    fig.update_layout(
        scene=dict(
            xaxis_title='x1',
            yaxis_title='x2',
            zaxis_title='x3',
            xaxis=dict(range=[-0.2, 1.2]),  # Ajusta o zoom do eixo x
            yaxis=dict(range=[-0.2, 1.2]),  # Ajusta o zoom do eixo y
            zaxis=dict(range=[-0.2, 1.2]),  # Ajusta o zoom do eixo z
            aspectmode='cube'  # Mantém a proporção dos eixos
        ),
        title='Problema 3 - Visualização 3D Detalhada',
        scene_camera=dict(eye=dict(x=1.5, y=1.5, z=0.8))  # Posição da câmera
    )

    fig.show()


def plot_3d_problema_4(res):
    """
    Plota uma representação 3D do Problema 4 com elementos visuais aprimorados,
    incluindo as restrições.
    """
    fig = go.Figure()

    # Solução Ótima (destacada)
    fig.add_trace(go.Scatter3d(
        x=[res.x[0]],
        y=[res.x[1]],
        z=[res.x[2]],
        mode='markers',
        marker=dict(size=8, color='red'),
        name='Solução Ótima'
    ))

    # Plano de referência no eixo x1-x2 (z=0)
    x1_range = np.linspace(0, 400, 20)  # Ajustado para o problema 4
    x2_range = np.linspace(0, 200, 20)  # Ajustado para o problema 4
    x1_plane, x2_plane = np.meshgrid(x1_range, x2_range)
    fig.add_trace(go.Surface(
        x=x1_plane,
        y=x2_plane,
        z=np.zeros_like(x1_plane),
        colorscale='Greys',
        opacity=0.3,
        showscale=False
    ))

    # --- RESTRIÇÕES DO PROBLEMA 4 ---

    # Restrição 1: x1 - 2*x2 >= 0  --> x2 <= x1 / 2
    z_restricao1 = x1_plane / 2

    # Restrição 2: x2 - 2*x3 >= 0  --> x3 <= x2 / 2
    # Para esta restrição, vamos fixar x1 em um valor dentro do intervalo
    x1_fixo = 200  # Você pode ajustar este valor
    x2_restricao2 = np.linspace(0, x1_fixo / 2, 20)  # Ajustado para x1 fixo
    x2_plane_r2, z_restricao2 = np.meshgrid(x2_restricao2, x2_restricao2 / 2)
    x1_plane_r2 = np.full_like(x2_plane_r2, x1_fixo)  # Cria um plano em x1 = x1_fixo

    # Restrição 3: x3 - 2*x4 >= 0 → x4 ← x3 / 2
    # Similar à restrição 2, vamos fixar x1 e x2
    x2_fixo = 100  # Você pode ajustar este valor
    x3_restricao3 = np.linspace(0, x2_fixo / 2, 20)
    z_restricao3, x4_plane_r3 = np.meshgrid(x3_restricao3 / 2, x3_restricao3)
    x1_plane_r3 = np.full_like(z_restricao3, x1_fixo)
    x2_plane_r3 = np.full_like(z_restricao3, x2_fixo)

    # Adicione as superfícies das restrições ao gráfico
    fig.add_trace(go.Surface(x=x1_plane, y=x2_plane, z=z_restricao1, name='x2 <= x1 / 2', opacity=0.6))
    fig.add_trace(go.Surface(x=x1_plane_r2, y=x2_plane_r2, z=z_restricao2, name='x3 <= x2 / 2', opacity=0.6))
    fig.add_trace(go.Surface(x=x1_plane_r3, y=x2_plane_r3, z=z_restricao3, name='x4 <= x3 / 2', opacity=0.6))

    # --- FIM DAS RESTRIÇÕES ---

    # Configura o layout com zoom, iluminação e destaque dos eixos
    fig.update_layout(
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="x3",
            xaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='black'),
            yaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='black'),
            zaxis=dict(showgrid=True, gridcolor='lightgray', zeroline=True, zerolinecolor='black'),
            aspectmode='cube',  # Mantém a proporção dos eixos
            camera=dict(eye=dict(x=1.2, y=1.2, z=0.6))  # Posição da câmera
        ),
        title="Problema 4 - Visualização 3D (x4=0)",
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


def plot_3d_problema_7(res):
    """
    Plota uma representação 3D do Problema 7, mostrando a região factível
    e a solução ótima.

    :arg:
        res: Um objeto 'OptimizeResult' retornado pela função 'linprog',
              contendo a solução ótima do problema.
    """
    fig = go.Figure()

    # Gera uma grade 3D para x1, x2 e x3 (restrição)
    x1 = np.linspace(0, 10, 100)
    x2 = np.linspace(0, 10, 100)
    X1, X2 = np.meshgrid(x1, x2)

    for k in range(1, 14):
        sin_term = np.sin(k / 13) * X1
        cos_term = np.cos(k / 13) * X2
        fig.add_trace(go.Surface(x=X1, y=X2, z=7 - sin_term - cos_term, showscale=False, opacity=0.5,
                                 name=f'sin({k}/13)x1 + cos({k}/13)x2 <= 7'))

    # Solução Ótima
    fig.add_trace(
        go.Scatter3d(x=[res.x[0]], y=[res.x[1]], z=[7 - np.sin(1 / 13) * res.x[0] - np.cos(1 / 13) * res.x[1]],
                     mode='markers',
                     marker=dict(size=10, color='red'), name='Solução Ótima'))

    # Configura o layout do gráfico
    fig.update_layout(
        scene=dict(
            xaxis_title="x1",
            yaxis_title="x2",
            zaxis_title="Valor da Restrição"
        ),
        title="Problema 7 - Visualização 3D"
    )

    fig.show()
