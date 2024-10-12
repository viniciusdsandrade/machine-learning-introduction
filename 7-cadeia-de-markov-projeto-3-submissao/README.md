## Projeto 3 de TI327 - Tópicos em Inteligência Artificial

## 🧑‍🎓 Integrantes

* Rafael Moreira Cavalcante de Souza
* Vinícius Dos Santos Andrade

**Descrição:**

Este projeto implementa o algoritmo PageRank, um algoritmo essencial utilizado por mecanismos de busca, como o Google,
para classificar a importância das páginas da web. O PageRank baseia-se no princípio de que uma página é mais relevante
se for referenciada por outras páginas de alta relevância.

**Contexto:**

Quando realizamos uma pesquisa no Google, os resultados são exibidos em ordem de relevância. O PageRank desempenha um
papel central na definição dessa relevância, garantindo que as páginas mais importantes e de maior qualidade sejam
priorizadas nos resultados.

**O Problema da "Inflação Artificial":**

Uma abordagem simples para classificar a importância de uma página seria contar o número de links que ela recebe. No
entanto, essa abordagem é suscetível a manipulações. Por exemplo, alguém poderia criar várias páginas fictícias que
referenciam uma página específica, inflando artificialmente sua classificação.

**A Solução: PageRank:**

O PageRank resolve esse problema ao considerar não apenas o número de links, mas também a relevância das páginas que
fazem essas referências. Um link proveniente de uma página importante tem mais peso do que um link de uma página com
menor relevância.

**Modelo do Navegador Aleatório:**

Uma forma de entender o PageRank é por meio do modelo do navegador aleatório. Imagine um navegador que percorre a web
clicando aleatoriamente em links. O PageRank de uma página pode ser interpretado como a probabilidade de que esse
navegador aleatório esteja em uma página específica em determinado momento.

**Fator de Amortecimento:**

Para lidar com situações em que o navegador pode ficar preso em um ciclo de páginas, é introduzido um fator de
amortecimento (damping factor). Com certa probabilidade, o navegador escolhe aleatoriamente uma página da web, em vez de
seguir um link da página atual.

**Implementação:**

O projeto implementa o PageRank de duas maneiras:

1. **Amostragem da Cadeia de Markov:** Simula o comportamento do navegador aleatório, navegando pelas páginas e
   registrando a frequência com que cada página é visitada.
2. **Algoritmo Iterativo:** Calcula o PageRank usando uma fórmula matemática recursiva que atualiza iterativamente os
   valores do PageRank até que eles convirjam.

**Código:**

O código em Python está estruturado da seguinte forma:

- **`crawl(directory)`:** Analisa um diretório de páginas HTML e identifica os links entre elas.
- **`transition_model(corpus, page, damping_factor)`:** Retorna a probabilidade de transição para outras páginas a
  partir de uma página específica.
- **`sample_pagerank(corpus, damping_factor, n)`:** Calcula o PageRank por amostragem da Cadeia de Markov.
- **`iterate_pagerank(corpus, damping_factor)`:** Calcula o PageRank usando o algoritmo iterativo.
- **`show_menu(...)`:** Exibe um menu interativo para o usuário.
- **`get_paths_group_choice()`:** Permite ao usuário selecionar o grupo de paths.
- **`get_corpus_choice(...)`:** Permite ao usuário selecionar o corpus para análise.
- **`process_pagerank(...)`:** Executa o cálculo do PageRank e exibe os resultados.
- **`main()`:** Função principal que orquestra a execução do programa.

**Resultados:**

O programa exibe os valores do PageRank calculados por amostragem e iteração (quando implementado) para cada página no
corpus selecionado. Os valores são apresentados em porcentagens e representam a importância relativa de cada página na
web.

**Observações:**

- O código inclui tratamento de erros para lidar com situações como funções não implementadas e diretórios inválidos.
- A formatação da saída foi aprimorada para melhor legibilidade.
- O código está bem documentado para facilitar a compreensão.

## 📋 Licença

Este projeto utiliza a licença [MIT](https://opensource.org/license/mit).
