import numpy as np
from scipy import stats
import pandas as pd

dados = [23, 23, 24, 24, 24, 25, 25, 26, 26, 28, 28, 28, 29, 29, 29,
         31, 31, 31, 33, 33, 33, 33, 33, 33, 34, 34, 34, 34, 35, 37,
         37, 38, 38, 39, 39, 39, 39, 39, 39, 40, 40, 42, 43, 45, 47]


def calcular_media(dados):
    """Soma todos os valores e divide pela quantidade de valores."""
    return np.mean(dados)


def calcular_mediana(dados):
    """Calcula a mediana dos dados."""
    return np.median(dados)


def calcular_moda(dados):
    """Calcula a moda dos dados."""
    moda = stats.mode(dados)
    if isinstance(moda.mode, np.ndarray):  # Verifica se moda.mode é um array NumPy
        return moda.mode[0], moda.count[0]
    else:
        return moda.mode, moda.count


def calcular_q1(dados):
    """Calcula o primeiro quartil (Q1) dos dados."""
    return np.percentile(dados, 25)


def calcular_q3(dados):
    """Calcula o terceiro quartil (Q3) dos dados."""
    return np.percentile(dados, 75)


def calcular_amplitude_total(dados):
    """Calcula a amplitude total dos dados."""
    return max(dados) - min(dados)


def calcular_desvio_padrao(dados):
    """Calcula o desvio padrão dos dados."""
    return np.std(dados)


def calcular_coeficiente_variacao(dados):
    """Calcula o coeficiente de variação dos dados."""
    media = calcular_media(dados)
    desvio_padrao = calcular_desvio_padrao(dados)
    return (desvio_padrao / media) * 100


def construir_distribuicao_frequencia(dados, num_classes):
    """Constrói a distribuição de frequência."""
    amplitude_total = calcular_amplitude_total(dados)
    amplitude_classe = amplitude_total / num_classes

    # Define os limites das classes
    limites_inferiores = [min(dados) + i * amplitude_classe for i in range(num_classes)]
    limites_superiores = [limite + amplitude_classe for limite in limites_inferiores]

    # Inicializa as frequências
    frequencias = [0] * num_classes

    # Conta as frequências para cada classe
    for valor in dados:
        for i in range(num_classes):
            if limites_inferiores[i] <= valor < limites_superiores[i]:
                frequencias[i] += 1
                break

    # Cria um DataFrame para a tabela de distribuição de frequência
    tabela_frequencia = pd.DataFrame({
        'Classe': [f'{limites_inferiores[i]:.2f} - {limites_superiores[i]:.2f}' for i in range(num_classes)],
        'Frequência': frequencias
    })

    return tabela_frequencia


def calcular_media_ponderada(tabela_frequencia):
    """Calcula a média ponderada a partir da tabela de frequência."""
    pontos_medios = [(float(classe.split(' - ')[0]) + float(classe.split(' - ')[1])) / 2
                     for classe in tabela_frequencia['Classe']]
    return sum(tabela_frequencia['Frequência'] * pontos_medios) / sum(tabela_frequencia['Frequência'])


def calcular_mediana_interpolacao(tabela_frequencia):
    """Calcula a mediana por interpolação linear a partir da tabela de frequência."""
    n = sum(tabela_frequencia['Frequência'])
    classe_mediana = 0
    limite_inferior_mediana = 0
    frequencia_acumulada_anterior = 0
    frequencia_classe_mediana = 0

    # Encontra a classe da mediana
    for i, frequencia in enumerate(tabela_frequencia['Frequência']):
        frequencia_acumulada = frequencia_acumulada_anterior + frequencia
        if frequencia_acumulada >= n / 2:
            classe_mediana = i
            limite_inferior_mediana = float(tabela_frequencia['Classe'][i].split(' - ')[0])
            frequencia_acumulada_anterior = frequencia_acumulada - frequencia
            frequencia_classe_mediana = frequencia
            break

    amplitude_classe = float(tabela_frequencia['Classe'][classe_mediana].split(' - ')[1]) - limite_inferior_mediana
    mediana = limite_inferior_mediana + (
            (n / 2 - frequencia_acumulada_anterior) / frequencia_classe_mediana) * amplitude_classe

    return mediana


def calcular_moda_czuber(tabela_frequencia):
    """Calcula a moda pela fórmula de Czuber a partir da tabela de frequência."""
    classe_modal = tabela_frequencia['Frequência'].idxmax()
    limite_inferior_modal = float(tabela_frequencia['Classe'][classe_modal].split(' - ')[0])
    frequencia_anterior = tabela_frequencia['Frequência'][classe_modal - 1] if classe_modal > 0 else 0
    frequencia_classe_modal = tabela_frequencia['Frequência'][classe_modal]
    frequencia_posterior = tabela_frequencia['Frequência'][classe_modal + 1] if classe_modal < len(
        tabela_frequencia) - 1 else 0
    amplitude_classe = float(tabela_frequencia['Classe'][classe_modal].split(' - ')[1]) - limite_inferior_modal

    moda = limite_inferior_modal + ((frequencia_classe_modal - frequencia_anterior) /
                                    (
                                            2 * frequencia_classe_modal - frequencia_anterior - frequencia_posterior)) * amplitude_classe

    return moda


def calcular_desvio_padrao_agrupado(tabela_frequencia, media_ponderada):
    """Calcula o desvio padrão para dados agrupados a partir da tabela de frequência."""
    pontos_medios = [(float(classe.split(' - ')[0]) + float(classe.split(' - ')[1])) / 2
                     for classe in tabela_frequencia['Classe']]
    n = sum(tabela_frequencia['Frequência'])
    soma_quadrados_desvios = sum(tabela_frequencia['Frequência'] * (pontos_medios - media_ponderada) ** 2)

    return np.sqrt(soma_quadrados_desvios / (n - 1))


if __name__ == "__main__":
    print(f"a) Média Aritmética: {calcular_media(dados):.2f}")
    print(f"b) Mediana: {calcular_mediana(dados):.2f}")
    moda, frequencia_moda = calcular_moda(dados)
    print(f"c) Moda: {moda} (aparece {frequencia_moda} vezes)")
    print(f"d) 1º Quartil: {calcular_q1(dados):.2f}")
    print(f"e) 3º Quartil: {calcular_q3(dados):.2f}")
    print(f"f) Amplitude Total: {calcular_amplitude_total(dados):.2f}")
    print(f"g) Desvio Padrão: {calcular_desvio_padrao(dados):.2f}")
    print(f"h) Coeficiente de Variação: {calcular_coeficiente_variacao(dados):.2f}%")

    num_classes = 3
    tabela_frequencia = construir_distribuicao_frequencia(dados, num_classes)

    print("\nTabela de Distribuição de Frequência:")
    print(tabela_frequencia)
