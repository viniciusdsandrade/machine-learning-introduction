import multiprocessing
import psutil


def contar_nucleos_fisicos():
    """
    Conta o número de núcleos físicos da CPU.

    Retorna:
        int: Número de núcleos físicos.
        None: Se não for possível determinar.
    """
    try:
        physical_cores = psutil.cpu_count(logical=False)
        if physical_cores is None:
            print("Não foi possível determinar o número de núcleos físicos.")
            return None
        print(f"Número de núcleos físicos: {physical_cores}")
        return physical_cores
    except AttributeError:
        print("psutil não está instalado. Não foi possível determinar núcleos físicos.")
        return None
    except Exception as e:
        print(f"Ocorreu um erro ao contar núcleos físicos: {e}")
        return None


def contar_nucleos_logicos():
    """
    Conta o número de núcleos lógicos da CPU.

    Retorna:
        int: Número de núcleos lógicos.
    """
    try:
        logical_cores = psutil.cpu_count(logical=True)
        if logical_cores is None:
            # Fallback para métodos alternativos se psutil falhar
            logical_cores = multiprocessing.cpu_count()
            print(f"psutil não conseguiu determinar núcleos lógicos. Usando multiprocessing: {logical_cores}")
        else:
            print(f"Número de núcleos lógicos: {logical_cores}")
        return logical_cores
    except AttributeError:
        # Fallback se psutil não estiver disponível
        logical_cores = multiprocessing.cpu_count()
        print(f"psutil não está instalado. Número de núcleos lógicos: {logical_cores}")
        return logical_cores
    except Exception as e:
        print(f"Ocorreu um erro ao contar núcleos lógicos: {e}")
        # Fallback para multiprocessing em caso de erro
        try:
            logical_cores = multiprocessing.cpu_count()
            print(f"Usando multiprocessing para determinar núcleos lógicos: {logical_cores}")
            return logical_cores
        except Exception as ex:
            print(f"Falha ao usar multiprocessing: {ex}")
            return None


if __name__ == "__main__":
    # Chamar ambas as funções para contar núcleos físicos e lógicos
    nucleos_fisicos = contar_nucleos_fisicos()
    nucleos_logicos = contar_nucleos_logicos()
