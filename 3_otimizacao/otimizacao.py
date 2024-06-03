from scipy.optimize import minimize
import numpy as np


# Otimização Matemática

# Otimizar significa encontrar a melhor maneira de fazer algo, dada uma medida do que é ser "melhor"

# Exemplos:
# - Quando fazemos compras, queremos minimizar o dinheiro gasto, ou maximizar a quantidade do foi comprado
# - Quando organizamos as horas de estudo, queremos aprender o máximo possível de preferência no menor tempo possível

# Matemáticamente, otimizar significa minizar ou maximizar uma função sujeita a restrições e suas variáveis
# min { f(x) : x pertence à Omega}
# f(x)  → função objetivo (ou função alvo)
# x     → vetor de variáveis de decisão
# Omega → conjunto de soluções factíveis/viáveis (restrições)

# f : R^n → R

# Exemplo prático
# min { f(x) = x1 + 2x2 + x3 : x1 - 0,3x2 <=0, x1+x2 <=2 }
# min f(x) = x1 + 2x2 + x3
# sujeita a x1 - 0,3x2 <=0
#           x1+x2 <=2

#  Algoritmo 'ADAM'
# Tipos de problema de otimização podem ser classificados como
# 1. Restrito ou Irrestríto
# 2. Linear ou Não Linear
# 3. Convexo ou Não Convexo

# Algoritmo Simplex:

# (1) Questão
# min  f(x1,x2) = 2x1 + x2
# Sujeito à x1 + x2 <= 1
#           x1 >=0
#           x2 >=0


# (2) Questão
# min  f(x1,x2) = x1
# Sujeito à x1^2 <= x2
#          x1^2 + x2^2 <= 2


def solve_minimization(funcao_objetivo, restricoes, limites=None, ponto_inicial=None):
    """
    Resolve um problema de otimização (minimização) utilizando a biblioteca scipy.optimize.

    Args:
        funcao_objetivo: Função que recebe um array NumPy com as variáveis de decisão
                         e retorna o valor da função objetivo.
        restricoes: Lista de dicionários, onde cada dicionário representa uma restrição.
                    Cada dicionário deve ter as chaves:
                        - 'type': tipo de restrição ('ineq' para desigualdade, 'eq' para igualdade).
                        - 'fun': função que recebe um array NumPy com as variáveis de decisão
                                 e retorna o valor da restrição.
        limites: Lista de tuplas, onde cada tupla representa os limites inferior e superior
                 de cada variável de decisão.
                 Ex: [(0, None), (None, 10)] significa que a primeira variável é ≥ 0
                 e a segunda é ≤ 10.
        ponto_inicial: Array NumPy com os valores iniciais para as variáveis de decisão.

    Returns:
        Objeto OptimizeResult da biblioteca scipy.optimize.
    """

    # Define um ponto inicial aleatório se não for fornecido
    if ponto_inicial is None:
        ponto_inicial = np.random.rand(len(limites))

    # Resolve o problema de otimização
    resultado = minimize(funcao_objetivo, ponto_inicial, bounds=limites, constraints=restricoes)

    return resultado


# --- Exemplo de uso com os problemas fornecidos ---

# Problema 1
def objetivo1(x):
    return 2 * x[0] + x[1]


def restricao1(x):
    return 1 - x[0] - x[1]


restricoes1 = [{'type': 'ineq', 'fun': restricao1}]
limites1 = [(0, None), (0, None)]


# Problema 2
def objetivo2(x):
    return x[0]


def restricao2a(x):
    return x[1] - x[0] ** 2


def restricao2b(x):
    return 2 - x[0] ** 2 - x[1] ** 2


restricoes2 = [{'type': 'ineq', 'fun': restricao2a},
               {'type': 'ineq', 'fun': restricao2b}]
limites2 = [(-1, 1), (0, 1)]

# Resolvendo os problemas
resultado1 = solve_minimization(objetivo1, restricoes1, limites1)
resultado2 = solve_minimization(objetivo2, restricoes2, limites2)

# Imprimindo os resultados
print("Questão 1:")
print(resultado1)
print("-" * 50)
print("Questão 2:")
print(resultado2)
