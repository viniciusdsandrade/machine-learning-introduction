import matplotlib.pyplot as plt
import pandas as pd
import io  # Importe o módulo io


# Função para criar o gráfico de barras com porcentagem relativa
def grafico_porcentagem_consumo(classes, consumo_por_classe):
    """Cria um gráfico de barras com a porcentagem relativa do consumo de energia por classe."""

    # Calcula o consumo total
    consumo_total = sum([sum(valores) for valores in consumo_por_classe.values()])

    # Criação do gráfico de barras com porcentagem relativa
    fig, ax = plt.subplots()

    # Criação das barras para cada classe com porcentagem
    for classe in classes:
        consumo_classe = sum(consumo_por_classe[classe])
        porcentagem = (consumo_classe / consumo_total) * 100
        ax.bar(classe, porcentagem, label=f'{classe} ({porcentagem:.3f}%)')

    # Configuração do gráfico
    ax.set_xlabel('Classe')
    ax.set_ylabel('Porcentagem do Consumo Total')
    ax.set_title('Consumo Mensal de Energia por Classe (% Relativa)')
    ax.legend()

    plt.show()


# Função para criar a distribuição de frequências e o histograma
def grafico_distribuicao_frequencias(dados, bins):
    """Cria uma distribuição de frequências e um histograma para o consumo de energia."""

    # Cria um DataFrame com os dados
    df = pd.read_csv(io.StringIO(dados), names=['Nº', 'Classe', 'Consumo'])

    # Cria a distribuição de frequências com os bins especificados
    frequencias = pd.cut(df['Consumo'], bins=bins, right=False).value_counts().sort_index()

    # Calcula as porcentagens
    porcentagens = (frequencias / frequencias.sum()) * 100

    # Imprime a tabela de distribuição de frequências
    print("Distribuição de Frequências:")
    for intervalo, frequencia in frequencias.items():
        print(f"{intervalo.left:.1f} – {intervalo.right:.1f}: {frequencia} ({porcentagens[intervalo]:.1f}%)")
    print(f"Total: {frequencias.sum()} (100%)")

    # Cria o histograma
    plt.hist(df['Consumo'], bins=bins, edgecolor='black')
    plt.xlabel('Consumo (kWh)')
    plt.ylabel('Frequência')
    plt.title('Histograma do Consumo de Energia')
    plt.show()


# Dados para o gráfico de porcentagem
classes = ['Residencial', 'Comercial', 'Industrial', 'Rural', 'PoderPublico']
consumo_por_classe = {
    'Residencial': [],
    'Comercial': [],
    'Industrial': [],
    'Rural': [],
    'PoderPublico': []
}

# Leitura dos dados da tabela (para o gráfico de porcentagem)
with open('consumo_energia.txt', 'r') as arquivo:
    for linha in arquivo:
        numero_classe, tipo_classe, consumo = linha.strip().split(',')
        consumo_por_classe[tipo_classe].append(float(consumo))

# Dados para a distribuição de frequências
dados = """
1,Residencial,236.0
2,Residencial,95.0
3,Residencial,304.0
4,Comercial,195.6
5,Industrial,420.0
6,Industrial,198.5
7,Residencial,232.0
8,Rural,145.8
9,Residencial,152.2
10,Industrial,587.5
11,PoderPublico,149.5
12,Comercial,200.4
13,Comercial,326.5
14,Industrial,240.7
15,Residencial,213.0
16,Residencial,110.0
17,PoderPublico,236.4
18,Comercial,358.0
19,Residencial,189.3
20,Industrial,285.0
21,Industrial,341.3
22,Residencial,273.6
23,Industrial,531.0
24,Industrial,476.4
25,Residencial,269.3
26,Industrial,350.0
27,Industrial,429.5
28,Industrial,195.0
29,Comercial,215.0
30,Industrial,362.8
"""
bins = [95, 185, 275, 365, 455, 545, 635]

# Chama as funções para gerar os gráficos
grafico_porcentagem_consumo(classes, consumo_por_classe)
grafico_distribuicao_frequencias(dados, bins)
