import bisect

import numpy as np
import pandas as pd


def tipo_variavel():
    """a) Qual é o tipo de variável “quantidade de água parada”?"""
    print("a) Tipo de variável: Quantitativa Discreta")


def media_nao_agrupada(dados):
    """b) Calcule a quantidade média, em litros, de água parada para os dados não agrupados;"""
    media = np.mean(dados)
    print(f"b) Média: {media:.2f} litros")


def mediana_nao_agrupada(dados):
    """c) Calcule a quantidade mediana, em litros, de água parada para os dados não agrupados;"""
    mediana = np.median(dados)
    print(f"c) Mediana: {mediana} litros")


def moda_nao_agrupada(dados):
    """d) Calcule a moda da quantidade, em litros, de água parada para os dados não agrupados;"""
    moda = pd.Series(dados).mode()[0]
    print(f"d) Moda: {moda} litros")


def quartis_nao_agrupados(dados):
    """e) Calcule o 1º e o 3º quartil (Q1 e Q3) da quantidade, em litros, de água parada para os dados não agrupados;"""
    q1 = np.percentile(dados, 25)
    q3 = np.percentile(dados, 75)
    print(f"e) Q1: {q1} litros, Q3: {q3} litros")


def desvio_padrao_nao_agrupado(dados):
    """f) Calcule o desvio padrão da quantidade, em litros, de água parada para os dados não agrupados;"""
    desvio_padrao = np.std(dados)
    print(f"f) Desvio padrão: {desvio_padrao:.4f} litros")


def variancia_nao_agrupada(dados):
    """g) Calcule a variância da quantidade, em litros, de água parada para os dados não agrupados;"""
    variancia = np.var(dados)
    print(f"g) Variância: {variancia:.4f} litros")


def coeficiente_variacao_nao_agrupado(dados):
    """h) Calcule o coeficiente de variação da quantidade, em litros, de água parada para os dados não agrupados;"""
    media = np.mean(dados)
    desvio_padrao = np.std(dados)
    cv = (desvio_padrao / media) * 100
    print(f"h) Coeficiente de variação: {cv:.4f}%")


def amplitude_total(dados):
    """i) Calcule a amplitude total da quantidade, em litros, de água parada;"""
    amplitude = max(dados) - min(dados)
    print(f"i) Amplitude total: {amplitude} litros")


def distribuicao_frequencia(dados):
    """Função que gera a distribuição de frequência"""
    frequencias = pd.Series(dados).value_counts().sort_index()
    return frequencias


def media_agrupada(frequencias):
    """k) Calcule a quantidade média, em litros, de água parada para a distribuição de frequência (dados agrupados);"""
    # Considerando os valores como pontos médios das classes
    centros_classe = frequencias.index.values
    media_agrupada = (centros_classe * frequencias.values).sum() / frequencias.sum()
    print(f"\nk) Média (agrupada): {media_agrupada:.2f} litros")


def mediana_agrupada(frequencias):
    """l) Calcule a quantidade mediana, em litros, de água parada para a distribuição de frequência (dados agrupados);"""
    n = frequencias.sum()
    frequencia_acumulada = frequencias.cumsum()

    # Encontra a classe mediana
    classe_mediana = frequencia_acumulada[frequencia_acumulada >= n / 2].index[0]

    # Encontra a posição da classe mediana
    posicao_classe_mediana = bisect.bisect_left(frequencias.index.values, classe_mediana)

    # Classe mediana
    limite_inferior = frequencias.index[posicao_classe_mediana]

    # Calculando os parâmetros da mediana agrupada
    if posicao_classe_mediana > 0:
        frequencia_acumulada_anterior = frequencia_acumulada.iloc[posicao_classe_mediana - 1]
    else:
        frequencia_acumulada_anterior = 0

    frequencia_classe_mediana = frequencias.iloc[posicao_classe_mediana]

    # Assumimos que a amplitude da classe é constante. Se souber a amplitude exata, pode ajustá-la aqui.
    amplitude_classe = frequencias.index[1] - frequencias.index[0]  # Caso seja constante

    mediana_agrupada = limite_inferior + (
            (n / 2 - frequencia_acumulada_anterior) / frequencia_classe_mediana) * amplitude_classe
    print(f"l) Mediana (agrupada): {mediana_agrupada:.3f} litros")


def moda_agrupada(frequencias):
    """Calcule a moda da quantidade, em litros, de água parada para a distribuição de frequência (dados agrupados)."""

    # Índice da classe modal (com maior frequência)
    indice_modal = frequencias.argmax()

    # Frequência da classe modal
    f_m = frequencias.iloc[indice_modal]

    # Frequência da classe anterior (se existir)
    if indice_modal > 0:
        f_m_minus_1 = frequencias.iloc[indice_modal - 1]
    else:
        f_m_minus_1 = 0

    # Frequência da classe posterior (se existir)
    if indice_modal < len(frequencias) - 1:
        f_m_plus_1 = frequencias.iloc[indice_modal + 1]
    else:
        f_m_plus_1 = 0

    # Limite inferior da classe modal
    L = frequencias.index[indice_modal]

    # Amplitude da classe (supondo que seja constante)
    h = frequencias.index[1] - frequencias.index[0]

    # Cálculo da moda
    moda_agrupada = L + ((f_m - f_m_minus_1) / ((f_m - f_m_minus_1) + (f_m - f_m_plus_1))) * h

    print(f"m) Moda (agrupada): {moda_agrupada:.2f} litros")


def variancia_agrupada(frequencias):
    """n) Calcule a variância da quantidade, em litros, de água parada para a distribuição de frequência (dados agrupados);"""

    # Convertendo o index em uma array de numpy ou pandas Series
    pontos_medios = frequencias.index.to_numpy()

    # Calculando a média agrupada (ponderada pelas frequências)
    media_agrupada = (pontos_medios * frequencias.values).sum() / frequencias.sum()

    # Calculando a variância agrupada
    variancia_agrupada = (((pontos_medios - media_agrupada) ** 2) * frequencias.values).sum() / (frequencias.sum() - 1)

    print(f"n) Variância (agrupada): {variancia_agrupada:.2f} litros")


def desvio_padrao_agrupado(frequencias):
    """o) Calcule o desvio padrão da quantidade, em litros, de água parada para a distribuição de frequência (dados agrupados);"""

    # Convertendo o index em uma array de numpy
    pontos_medios = frequencias.index.to_numpy()

    # Calculando a média agrupada (ponderada pelas frequências)
    media_agrupada = (pontos_medios * frequencias.values).sum() / frequencias.sum()

    # Calculando a variância agrupada
    variancia_agrupada = (((pontos_medios - media_agrupada) ** 2) * frequencias.values).sum() / (frequencias.sum() - 1)

    # Calculando o desvio padrão (a raiz quadrada da variância)
    desvio_padrao_agrupado = variancia_agrupada ** 0.5

    print(f"o) Desvio padrão (agrupado): {desvio_padrao_agrupado:.2f} litros")


def coeficiente_variacao_agrupado(frequencias):
    """Calcule o coeficiente de variação da quantidade, em litros, de água parada para a distribuição de frequência (dados agrupados)."""

    # Convertendo o índice (intervalos de classe) em array numpy
    pontos_medios = frequencias.index.to_numpy()

    # Calculando a média agrupada (ponderada pelas frequências)
    media_agrupada = np.sum(pontos_medios * frequencias.values) / frequencias.sum()

    # Calculando a variância agrupada (ponderada)
    variancia_agrupada = np.sum(frequencias.values * (pontos_medios - media_agrupada) ** 2) / frequencias.sum()

    # Calculando o desvio padrão agrupado
    desvio_padrao_agrupado = np.sqrt(variancia_agrupada)

    # Calculando o coeficiente de variação (CV = desvio padrão / média) e multiplicando por 100 para obter em %
    coeficiente_variacao = (desvio_padrao_agrupado / media_agrupada) * 100

    print(f"p) Coeficiente de variação (agrupado): {coeficiente_variacao:.2f}%")


def verifica_simetria(dados):
    """q) Verifique se a curva é simétrica ou assimétrica."""
    media = np.mean(dados)
    mediana = np.median(dados)
    moda = max(set(dados), key=dados.count)  # Calculando a moda para dados não agrupados

    if media > mediana > moda:
        print("\nq) A curva tem assimetria à direita (média > mediana > moda).")
    else:
        print("\nq) A curva não é simétrica.")


def main():
    # Dados
    dados = "3,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,7,7,7,7,8,8,8,8,8,8,8,9,9,9,9,9,9,10,11,11,11,11,11,11,12,12,12,13,13,13,13,14,14,15,16,17,17,18,19,19,20,23"
    dados = list(map(int, dados.split(',')))

    # Chamando as funções
    tipo_variavel()
    media_nao_agrupada(dados)
    mediana_nao_agrupada(dados)
    moda_nao_agrupada(dados)
    quartis_nao_agrupados(dados)
    desvio_padrao_nao_agrupado(dados)
    variancia_nao_agrupada(dados)
    coeficiente_variacao_nao_agrupado(dados)
    amplitude_total(dados)
    frequencias = distribuicao_frequencia(dados)
    media_agrupada(frequencias)
    mediana_agrupada(frequencias)
    moda_agrupada(frequencias)
    variancia_agrupada(frequencias)
    desvio_padrao_agrupado(frequencias)
    coeficiente_variacao_agrupado(frequencias)
    verifica_simetria(dados)


if __name__ == "__main__":
    main()
