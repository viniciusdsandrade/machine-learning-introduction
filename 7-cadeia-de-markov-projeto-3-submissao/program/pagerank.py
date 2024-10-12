from collections import defaultdict
from bs4 import BeautifulSoup
import random
import os

DAMPING = 0.85  # constante de damping
SAMPLES = 10000  # número de amostras


class Colors:
    RED = '\033[1;31m'
    CYAN = '\033[1;36m'
    GREEN = '\033[0;32m'
    BOLD = '\033[1m'
    YELLOW = '\033[33m'
    RESET = '\033[0m'


def crawl(directory):
    """
    Analisa um diretório de páginas HTML e identifica os links entre elas.

    Percorre um diretório contendo páginas HTML, extrai os links presentes
    em cada página e retorna um dicionário que mapeia cada página aos links
    que ela contém, considerando apenas links para outras páginas dentro
    do mesmo corpus.

    Parâmetros:
        directory (str): O caminho para o diretório contendo as páginas
                         HTML a serem analisadas.

    Retorno:
        dict: um dicionário onde:
              - Cada chave é o nome de um arquivo HTML no diretório
                (ex: "pagina1.html").
              - Cada valor é um conjunto (set) contendo os nomes dos
                arquivos HTML para os quais a página (chave) possui links.
                Links externos ao corpus são ignorados.
    """
    pages = dict()  # 1. Inicializa um dicionário vazio chamado 'pages' para armazenar a estrutura de links.

    for filename in os.listdir(directory):
        if not filename.endswith(".html"):  # 2. Verifica se o arquivo é um arquivo HTML (termina com ".html").
            continue  # 3. Se não for um arquivo HTML, pula para o próximo arquivo.
        # 4. Abre o arquivo HTML em modo de leitura.
        with open(os.path.join(directory, filename)) as f:
            soup = BeautifulSoup(f, "html.parser")  # 5. Analisa o conteúdo HTML usando BeautifulSoup.
            links = [link.get("href") for link in soup.find_all(
                "a")]  # 6. Encontra todas as tags <a> no HTML e extrai o atributo 'href' (o link) de cada tag <a> e armazena em uma lista.
            pages[filename] = set(links) - {
                filename}  # 7. Adiciona o nome do arquivo como chave no dicionário 'pages'e o conjunto de links (excluindo links para a própria página) como valor.

    for filename in pages:
        # 8. Filtra os links de cada página, mantendo apenas aqueles que se referem a outras páginas no corpus (presentes no dicionário 'pages').
        pages[filename] = set(link for link in pages[filename] if link in pages)

    return pages


def transition_model(corpus, page, damping_factor):
    """
    Retorna uma distribuição de probabilidade sobre qual página visitar em seguida,
    dada uma página atual.

    Com probabilidade `damping_factor`, escolhe um link aleatório ligado por `page`.
    Com probabilidade `1 - damping_factor`, escolhe um link aleatório escolhido
    de todas as páginas no corpus.
    """
    # 1. Inicializa a distribuição de probabilidade para todas as páginas no corpus com 0.
    probability_distribution = defaultdict(lambda: 0)

    # 2. Calcula a probabilidade de pular para qualquer página aleatoriamente (1 - damping_factor) / N.
    random_jump_probability = (1 - damping_factor) / len(corpus)
    # 3. Atribui essa probabilidade a cada página no corpus.
    for p in corpus:
        probability_distribution[p] = random_jump_probability

    # 4. Calcula a probabilidade de seguir um link da página atual (damping_factor / número de links na página).
    # 5. Verifica se a página tem links de saída.
    if corpus[page]:
        link_probability = damping_factor / len(corpus[page])
        # 6. Para cada link na página atual, adiciona a probabilidade do link à distribuição de probabilidade.
        for link in corpus[page]:
            probability_distribution[link] += link_probability
    # 7. Se a página não tiver links, distribui a probabilidade de damping igualmente entre todas as páginas.
    else:
        for p in corpus:
            probability_distribution[p] += damping_factor / len(corpus)

    return probability_distribution


def sample_pagerank(corpus, damping_factor, n):
    """
    Retorna os valores do PageRank para cada página,
    amostrando `n` páginas conforme o modelo de transição,
    começando com uma página aleatória.

    Retorna um dicionário onde as chaves são nomes de páginas e os valores
    são seus valores de PageRank estimados (um valor entre 0 e 1).
    Todos os valores de PageRank devem somar 1.
    """
    # 1. Inicializa o dicionário de PageRank com valores 0 para todas as páginas.
    pagerank = {page: 0 for page in corpus}

    # 2. Escolhe uma página aleatória para começar.
    current_page = random.choice(list(corpus.keys()))
    # 3. Incrementa a contagem da página inicial.
    pagerank[current_page] += 1

    # 4. Itera n vezes, amostrando páginas conforme o modelo de transição.
    for _ in range(n - 1):
        # 5. Obtém a distribuição de probabilidade para a página atual.
        transition_probabilities = transition_model(corpus, current_page, damping_factor)
        # 6. Escolhe a próxima página com base nas probabilidades de transição.
        next_page = random.choices(list(transition_probabilities.keys()),
                                   weights=list(transition_probabilities.values()))[0]
        # 7. Incrementa a contagem da página visitada.
        pagerank[next_page] += 1
        # 8. Atualiza a página atual.
        current_page = next_page

    # 9. Normaliza os valores de PageRank para que somem 1.
    total_visits = sum(pagerank.values())
    for page in pagerank:
        pagerank[page] /= total_visits

    return pagerank


def iterate_pagerank(corpus, damping_factor):
    """
    Calcula os valores de PageRank para cada página de forma iterativa
    até que os valores de PageRank converjam.
    
    Retorna um dicionário com os nomes das páginas e seus respectivos PageRanks.
    """
    # 1. Extrai o total de páginas no corpus
    numPages = len(corpus)

    # 2. Inicializa um dict para cada página com valor igual a 1/N (distribuição uniforme)
    pagerank = {page: 1 / numPages for page in corpus}

    # 3. Define o critério de convergência (erro aceitável)
    # O valor é baixo para ter certeza de que os valores de PageRank não estão mais mudando de forma significativa entre as iterações
    convergence_limit = 0.001

    # 4. Itera até que os valores de PageRank converjam.
    while True:
        # 4.1. Armazena os novos valores de PageRank após cada iteração
        new_pagerank = {}

        # 4.2. Variável para verificar se houve convergência
        converged = True

        # 4.3. Itera sobre todas as páginas no corpus
        for page in corpus:
            # 4.3.1 parte da fórmula do PageRank que representa a probabilidade de "pular" para uma página aleatória
            new_rank = (1 - damping_factor) / numPages

            # 4.3.2. Para cada other_page no corpus, verificamos se ela contribui para o PageRank da page
            for other_page in corpus:
                # Verifica se a página atual está nos links da outra página ou se a outra página não tem links
                if page in corpus[other_page] or len(corpus[other_page]) == 0:
                    # Se a outra página não tiver links, a contribuição é distribuída entre todas as páginas
                    num_links = len(corpus[other_page]) or numPages
                    # Soma a contribuição dessa outra página para o novo rank, completando a fórmula do PageRank
                    new_rank += damping_factor * (pagerank[other_page] / num_links)

            # 4.3.3. Armazena o novo valor de PageRank para a página.
            new_pagerank[page] = new_rank

            # 4.3.4. Verifica se a diferença absoluta entre o novo e o antigo PageRank excede o limite de convergência
            if abs(new_pagerank[page] - pagerank[page]) > convergence_limit:
                # Se a diferença for maior, ainda não convergiu
                converged = False

                # 4.4. Atualiza o PageRank com os novos valores
        pagerank = new_pagerank

        # 4.5. Se todos os valores convergiram, termina o loop
        if converged:
            break

            # 5. Normaliza o PageRank para garantir que a soma dos valores seja igual a 1
    total = sum(pagerank.values())
    pagerank = {page: rank / total for page, rank in pagerank.items()}

    # 6. Retorna o dicionário final de PageRank
    return pagerank


def show_menu(options,
              prompt="Escolha uma opção:",
              exit_option="S",
              exit_text="Sair"):
    """
    Exibe um menu com as opções fornecidas e retorna a escolha do usuário.
    """
    while True:
        print(f"\n{Colors.CYAN}{prompt}{Colors.RESET}")
        for key, description in options.items():
            print(f"{Colors.GREEN}{key}. {description}{Colors.RESET}")
        print(f"{Colors.YELLOW}{exit_option}. {exit_text}{Colors.RESET}")

        choice = input(f"{Colors.BOLD}Digite a opção desejada: {Colors.RESET}").upper()
        if choice in options or choice == exit_option:
            return choice
        print(f"{Colors.RED}Opção inválida. Tente novamente.\n{Colors.RESET}")


def get_paths_group_choice():
    """
    Função para escolher o grupo de paths.
    """
    path_descriptions = {
        "1": "Paths do notebook do Vini",
        "2": "Paths do desktop do Vini",
        "3": "Paths do desktop do Rafa",
        "4": "Paths da máquina do Prof. Dr. e Cientista Guilherme Macedo"
    }
    return show_menu(path_descriptions,
                     prompt="Escolha o grupo de paths:")


def get_corpus_choice(selected_paths):
    """
    Função para escolher o corpus com base no grupo de paths selecionado.
    """
    corpus_descriptions = {key: path for key, path in selected_paths.items()}

    while True:
        choice = show_menu(corpus_descriptions,
                           prompt="Escolha o corpus para analisar:",
                           exit_option="V",
                           exit_text="Voltar")
        if choice == "V":
            return None  # Retorna None para indicar que o usuário escolheu voltar

        corpus_dir = selected_paths[choice]

        # Verifica se o diretório do corpus existe
        if os.path.exists(corpus_dir):
            return corpus_dir
        else:
            print(f"{Colors.RED}O diretório '{corpus_dir}' não foi encontrado. Tente novamente.{Colors.RESET}\n")


def process_pagerank(corpus_dir, damping, samples):
    """
    Função para processar o PageRank com formatação aprimorada.
    """
    if corpus_dir is None:
        return  # Volta para o menu anterior se o usuário escolheu "Voltar" em get_corpus_choice

    try:
        corpus = crawl(corpus_dir)
    except NotImplementedError:
        print(f"{Colors.RED}Função 'crawl' não implementada ainda.{Colors.RESET}")
        return

    # PageRank via amostragem
    try:
        print(f"\n{Colors.CYAN}PageRank Results from Sampling (n = {samples}){Colors.RESET}")
        ranks_sampling = sample_pagerank(corpus, damping, samples)

        # Determina o tamanho máximo do nome da página para ajustar a formatação
        max_page_length = max(len(page) for page in ranks_sampling)

        for page in sorted(ranks_sampling):
            percentage = ranks_sampling[page] * 100
            formatted_percentage = f"{percentage:.4f}".rstrip('0').rstrip('.')

            # Formata a linha com a página justificada à esquerda e o valor à direita
            print(f"{Colors.YELLOW}  {page.ljust(max_page_length)}: {formatted_percentage}%{Colors.RESET}")
    except NotImplementedError:
        print(f"{Colors.RED}Função 'sample_pagerank' não implementada ainda.{Colors.RESET}")

    # PageRank via iteração
    try:
        print(f"\n{Colors.CYAN}PageRank Results from Iteration{Colors.RESET}")
        ranks_iteration = iterate_pagerank(corpus, damping)

        # Determina o tamanho máximo do nome da página para ajustar a formatação
        max_page_length = max(len(page) for page in ranks_iteration)

        for page in sorted(ranks_iteration):
            percentage = ranks_iteration[page] * 100
            formatted_percentage = f"{percentage:.4f}".rstrip('0').rstrip('.')

            # Formata a linha com a página justificada à esquerda e o valor à direita
            print(f"{Colors.YELLOW}  {page.ljust(max_page_length)}: {formatted_percentage}%{Colors.RESET}")
    except NotImplementedError:
        print(f"{Colors.RED}Função 'iterate_pagerank' não implementada ainda.{Colors.RESET}")


def main():
    BASE_PATH_NOTEBOOK_VINI = "C:\\Users\\vinic\\OneDrive\\Área de Trabalho\\ti327v-projeto3-equipe8\\program"
    BASE_PATH_DESKTOP_VINI = "C:\\Users\\Pichau\\Desktop\\ti327v-projeto3-equipe8\\program"
    BASE_PATH_DESKTOP_RAFA = "C:\\Users\\Rafael\\Documents\\Projects\\ti327v-projeto3-equipe8\\program"

    # TODO: Professor, fique à vontade para colocar o seu path base aqui para facilitar a execução dos testes
    BASE_PATH_GUI = "coloque o seu path base aqui (linha: 302)"

    path_notebook_vini = {
        "0": os.path.join(BASE_PATH_NOTEBOOK_VINI, "corpus0"),
        "1": os.path.join(BASE_PATH_NOTEBOOK_VINI, "corpus1"),
        "2": os.path.join(BASE_PATH_NOTEBOOK_VINI, "corpus2"),
    }

    path_desktop_vini = {
        "0": os.path.join(BASE_PATH_DESKTOP_VINI, "corpus0"),
        "1": os.path.join(BASE_PATH_DESKTOP_VINI, "corpus1"),
        "2": os.path.join(BASE_PATH_DESKTOP_VINI, "corpus2"),
    }

    path_desktop_rafa = {
        "0": os.path.join(BASE_PATH_DESKTOP_RAFA, "corpus0"),
        "1": os.path.join(BASE_PATH_DESKTOP_RAFA, "corpus1"),
        "2": os.path.join(BASE_PATH_DESKTOP_RAFA, "corpus2"),
    }

    path_desktop_guilherme_macedo = {
        "0": os.path.join(BASE_PATH_GUI, "corpus0"),
        "1": os.path.join(BASE_PATH_GUI, "corpus1"),
        "2": os.path.join(BASE_PATH_GUI, "corpus2"),
    }

    paths_options = {
        "1": path_notebook_vini,
        "2": path_desktop_vini,
        "3": path_desktop_rafa,
        "4": path_desktop_guilherme_macedo,
    }

    # Menu principal
    while True:
        choice_group = get_paths_group_choice()
        if choice_group == "S":
            break

        selected_paths = paths_options[choice_group]

        # Menu de seleção dos 'corpus'
        while True:
            corpus_dir = get_corpus_choice(selected_paths)
            if corpus_dir is None:  # Se o usuário escolheu "Voltar"
                break

            # Processar PageRank (agora corpus_dir pode ser None)
            process_pagerank(corpus_dir, DAMPING, SAMPLES)


if __name__ == "__main__":
    main()
