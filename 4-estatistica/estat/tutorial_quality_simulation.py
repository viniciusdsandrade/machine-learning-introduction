# tutorial_quality_simulation.py
from dataclasses import dataclass
from typing import List
import concurrent.futures
import random
import os


@dataclass
class TutorialCategory:
    nome: str
    numero_tutoriais: int
    probabilidade_bom: float

    def simular_tutoriais_bons(self, random_generator: random.Random) -> int:
        """
        Simula a quantidade de tutoriais bons para esta categoria.

        :param random_generator: Instância de random.Random para gerar números aleatórios.
        :return: Número de tutoriais bons simulados.
        """
        tutoriais_bons = 0
        for _ in range(self.numero_tutoriais):
            if random_generator.random() < self.probabilidade_bom:
                tutoriais_bons += 1
        return tutoriais_bons

    def expectativa(self) -> float:
        """
        Calcula a expectativa teórica de tutoriais bons.

        :return: Expectativa de tutoriais bons.
        """
        return self.numero_tutoriais * self.probabilidade_bom


class SimulationResult:
    def __init__(self, categories: List[TutorialCategory], total_bons: List[int], numero_simulacoes: int) -> None:
        self.categories = categories
        self.total_bons = total_bons
        self.numero_simulacoes = numero_simulacoes

    def display_results(self) -> None:
        print(f"Resultados após {self.numero_simulacoes} simulações:")
        for categoria, total in zip(self.categories, self.total_bons):
            media_bons = total / self.numero_simulacoes
            proporcao = (media_bons / categoria.numero_tutoriais) * 100
            print(f"Média de tutoriais {categoria.nome} bons: {media_bons:.2f} (Proporção: {proporcao:.2f}%)")

        print("\nAnálise Comparativa:")
        for categoria in self.categories:
            print(f"Total esperado de tutoriais bons no {categoria.nome}: {categoria.expectativa():.2f}")
        print("Conclusão: Mesmo com menor probabilidade individual, a quantidade maior resulta em mais tutoriais bons.")


def simulate_once(seed: int, categorias_data: List[dict]) -> List[int]:
    """
    Executa uma única simulação de tutoriais bons para cada categoria.

    :param seed: Semente para o gerador de números aleatórios.
    :param categorias_data: Lista de dicionários contendo dados das categorias.
    :return: Lista com o número de tutoriais bons para cada categoria.
    """
    rnd = random.Random(seed)
    bons_por_categoria = []
    for categoria_dict in categorias_data:
        categoria = TutorialCategory(**categoria_dict)
        bons = categoria.simular_tutoriais_bons(rnd)
        bons_por_categoria.append(bons)
    return bons_por_categoria


class TutorialQualitySimulation:
    def __init__(self, categories: List[TutorialCategory], numero_simulacoes: int) -> None:
        self.categories = categories
        self.numero_simulacoes = numero_simulacoes

    def run_simulation(self) -> SimulationResult:
        """
        Executa as simulações de forma paralela para melhorar a performance.

        :return: Resultado das simulações.
        """
        total_bons = [0 for _ in self.categories]

        # Definir o número de workers com base nos CPUs disponíveis
        max_workers = min(32, (os.cpu_count() or 1) + 4)

        # Preparar os dados das categorias para serem passados para os processos
        categorias_data = [categoria.__dict__ for categoria in self.categories]

        # Gerar sementes únicas para cada simulação
        random_seeds = [random.randint(0, 1_000_000_000) for _ in range(self.numero_simulacoes)]

        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            # Mapear as simulações com as sementes e os dados das categorias
            # Cada simulação recebe uma semente e os dados das categorias
            # Utilizamos list comprehension para passar múltiplos argumentos
            futures = [executor.submit(simulate_once, seed, categorias_data) for seed in random_seeds]

            for future in concurrent.futures.as_completed(futures):
                try:
                    simulation_result = future.result()
                    for idx, bons in enumerate(simulation_result):
                        total_bons[idx] += bons
                except Exception as e:
                    print(f"Ocorreu um erro na simulação: {e}")

        return SimulationResult(self.categories, total_bons, self.numero_simulacoes)

    @staticmethod
    def display_results(result: SimulationResult) -> None:
        """
        Exibe os resultados das simulações.

        :param result: Objeto SimulationResult contendo os resultados.
        """
        result.display_results()


def main() -> None:
    # Configurações (podem ser modificadas conforme necessário)
    tutoriais_brasil = 100
    fator_expansao = 20
    tutoriais_ingles = tutoriais_brasil * fator_expansao

    prob_bom_brasil = 0.7
    prob_bom_ingles = 0.4

    numero_simulacoes = 10_000

    brasil = TutorialCategory("Brasil", tutoriais_brasil, prob_bom_brasil)
    ingles = TutorialCategory("Inglês", tutoriais_ingles, prob_bom_ingles)

    simulation = TutorialQualitySimulation([brasil, ingles], numero_simulacoes)
    result = simulation.run_simulation()
    simulation.display_results(result)


if __name__ == "__main__":
    main()
