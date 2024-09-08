# Função genérica para calcular a probabilidade simples
def probabilidade_simples(casos_favoraveis, total_casos_possiveis):
    return casos_favoraveis / total_casos_possiveis


# Função genérica para calcular a probabilidade de eventos independentes
def probabilidade_eventos_independentes(prob_evento1, prob_evento2):
    return prob_evento1 * prob_evento2


# Função genérica para calcular a probabilidade condicional
def probabilidade_condicional(casos_favoraveis, total_casos_possiveis):
    return casos_favoraveis / total_casos_possiveis


# Função genérica para calcular a probabilidade de eventos mutuamente exclusivos
def probabilidade_mutuamente_exclusivos(prob_evento1, prob_evento2):
    return prob_evento1 + prob_evento2


# Função genérica para calcular a probabilidade de eventos não mutuamente exclusivos
def probabilidade_nao_mutuamente_exclusivos(prob_evento1, prob_evento2, prob_interseccao):
    return prob_evento1 + prob_evento2 - prob_interseccao


def main():
    # Exemplo 1: Probabilidade Simples
    casos_favoraveis = 4  # Número de Áses
    total_casos_possiveis = 52  # Total de cartas
    probabilidade = probabilidade_simples(casos_favoraveis, total_casos_possiveis)
    print(f"Exemplo 1: Probabilidade de tirar um Ás: {probabilidade:.2f}")

    # Exemplo 2: Probabilidade de Eventos Independentes
    prob_primeiro_rei = 4 / 52
    prob_segundo_rei = 3 / 51
    probabilidade = probabilidade_eventos_independentes(prob_primeiro_rei, prob_segundo_rei)
    print(f"Exemplo 2: Probabilidade de tirar dois Reis: {probabilidade:.4f}")

    # Exemplo 3: Probabilidade Condicional
    bolas_totais = 8
    bolas_azuis = 3
    bolas_vermelhas = 5
    probabilidade = probabilidade_condicional(bolas_azuis, bolas_totais - 1)
    print(f"Exemplo 3: Probabilidade condicional de tirar uma bola azul depois de uma vermelha: {probabilidade:.3f}")

    # Exemplo 4: Probabilidade de Eventos Mutuamente Exclusivos
    prob_rei = 4 / 52
    prob_dama = 4 / 52
    probabilidade = probabilidade_mutuamente_exclusivos(prob_rei, prob_dama)
    print(f"Exemplo 4: Probabilidade de tirar um Rei ou uma Dama: {probabilidade:.2f}")

    # Exemplo 5: Probabilidade de Eventos Não Mutuamente Exclusivos
    prob_as = 4 / 52
    prob_espadas = 13 / 52
    prob_as_espadas = 1 / 52
    probabilidade = probabilidade_nao_mutuamente_exclusivos(prob_as, prob_espadas, prob_as_espadas)
    print(f"Exemplo 5: Probabilidade de tirar um Ás ou uma carta de Espadas: {probabilidade:.2f}")


if __name__ == "__main__":
    main()
