# Traveling Salesman Problem
#            Campinas Limeira  Sumaré Valinhos Hortolândia
# Campinas       0        45       23       31       13
# Limeira       45         0       17       43       27
# Sumaré        23        17        0       19       23
# Valinhos      31        43        19       0        39
# Hortolândia   13        27        23       39       0

# Tipos de solução
# Solução eurística = Jeito intuitivo de resolver um problema
# Solução factivel = engloba todos os requisitos do problema
# Solução aleatória = solução que não segue um padrão
# Solução ótima = melhor solução possível
# Solução subótima = solução que não é a melhor, mas é a melhor possível

# Tipos de algoritmo
# Algoritmo de força bruta = testa todas as possibilidades
# Algoritmo do Vizinho mais proximo = A cada novo passo escolhe o vizinho mais próximo
# Algoritmo Deterministico = Sempre retorna o mesmo resultado
# Algoritmo Estocástico = Pode retornar resultados diferentes
# Algoritmo Guloso = Escolhe a melhor opção a cada passo
# Algoritmo da Heuristaca da Insercao mais barata = A cada passo escolhe a melhor opção de inserção
# Algoritmo Aleatório = Escolhe uma opção aleatória a cada passo
# Algoritmo de busca local = A cada passo escolhe a melhor opção local
# Algoritmo de busca global = A cada passo escolhe a melhor opção global
# ALgoritmo meta-heurístico = Algoritmo que tenta encontrar a melhor solução possível


# Representação do grafo
graph = {
    "Campinas": {"Limeira": 45, "Sumaré": 23, "Valinhos": 31, "Hortolândia": 13},
    "Limeira": {"Campinas": 45, "Sumaré": 17, "Valinhos": 43, "Hortolândia": 27},
    "Sumaré": {"Campinas": 23, "Limeira": 17, "Valinhos": 19, "Hortolândia": 23},
    "Valinhos": {"Campinas": 31, "Limeira": 43, "Sumaré": 19, "Hortolândia": 39},
    "Hortolândia": {"Campinas": 13, "Limeira": 27, "Sumaré": 23, "Valinhos": 39}
}


def calculate_path_cost(path, graph):
    cost = 0
    for i in range(1, len(path)):
        cost += graph[path[i - 1]][path[i]]
    return cost


def generate_permutations(elements):
    if len(elements) <= 1:
        yield elements
    else:
        for perm in generate_permutations(elements[1:]):
            for i in range(len(elements)):
                yield perm[:i] + elements[0:1] + perm[i:]


def find_shortest_path(graph):
    cities = list(graph.keys())
    shortest_path = None
    shortest_path_cost = float('inf')
    for path in generate_permutations(cities):
        path_cost = calculate_path_cost(path, graph)
        if path_cost < shortest_path_cost:
            shortest_path = path
            shortest_path_cost = path_cost
    return shortest_path, shortest_path_cost


shortest_path, shortest_path_cost = find_shortest_path(graph)
print(f"O caminho mais curto é: {shortest_path} com custo total: {shortest_path_cost}")
