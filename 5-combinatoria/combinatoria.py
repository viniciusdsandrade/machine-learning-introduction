# Importação da função de fatorial do módulo math
from math import factorial


# Função para calcular a permutação simples
def permutacao_simples(n):
    return factorial(n)


# Função para calcular a permutação com repetição
def permutacao_com_repeticao(n, repeticoes):
    denominador = 1
    for r in repeticoes:
        denominador *= factorial(r)
    return factorial(n) // denominador


# Função para calcular a combinação simples
def combinacao_simples(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


# Função para calcular o arranjo simples
def arranjo_simples(n, k):
    return factorial(n) // factorial(n - k)


def main():
    # Problema 1: Permutação Simples
    print("Problema 1: Permutação Simples")
    # Quantas maneiras diferentes é possível organizar 5 livros em uma prateleira?
    n = 5
    resultado = permutacao_simples(n)
    print(f"Organizar {n} livros: {resultado} maneiras\n")

    # Problema 2: Permutação com Repetição
    print("Problema 2: Permutação com Repetição")
    # Quantas maneiras diferentes é possível organizar a palavra "BALL"?
    n = 4  # Número de letras na palavra
    repeticoes = [2]  # Há 2 letras 'L'
    resultado = permutacao_com_repeticao(n, repeticoes)
    print(f"Organizar a palavra 'BALL': {resultado} maneiras\n")

    # Problema 3: Combinação Simples
    print("Problema 3: Combinação Simples")
    # De um grupo de 5 pessoas, de quantas maneiras diferentes podemos formar uma dupla?
    n = 5
    k = 2
    resultado = combinacao_simples(n, k)
    print(f"Formar uma dupla de {n} pessoas: {resultado} maneiras\n")

    # Problema 4: Arranjo Simples
    print("Problema 4: Arranjo Simples")
    # De um grupo de 5 pessoas, de quantas maneiras diferentes podemos escolher um presidente e um vice-presidente?
    n = 5
    k = 2
    resultado = arranjo_simples(n, k)
    print(f"Escolher um presidente e um vice-presidente de {n} pessoas: {resultado} maneiras\n")


# Executa a função principal
if __name__ == "__main__":
    main()
