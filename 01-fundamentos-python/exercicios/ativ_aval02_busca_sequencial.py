"""
Atividade Pratica 02 - Busca Sequencial em Lista
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Implementar uma busca sequencial em uma lista de números
inteiros, identificando a posição do elemento procurado.

Conceitos:
- Listas
- Estruturas de repetição
- Estruturas condicionais
- Funções
- Tratamento de exceções
"""


def busca_sequencial(numeros: list[int], item: int) -> int:
    """
    Busca um número em uma lista utilizando busca sequencial.

    Args:
        numeros: Lista de números inteiros.
        item: Número que será procurado.

    Returns:
        Índice da primeira ocorrência do item.
        Retorna -1 quando o item não é encontrado.
    """
    for indice, numero in enumerate(numeros):
        if numero == item:
            return indice

    return -1


def exibir_lista(numeros: list[int]) -> None:
    """Exibe os índices e valores da lista."""
    elementos = ", ".join(
        f"{indice}:{valor}"
        for indice, valor in enumerate(numeros)
    )

    print(f"\nLista de números: {{{elementos}}}")


def main() -> None:
    """Executa o programa principal."""
    numeros = [10, 2, 7, 8, 5, 3, 22, 17, 18]

    print("=== BUSCA SEQUENCIAL EM LISTA ===")

    try:
        item = int(input("Digite o número que deseja buscar: "))

        exibir_lista(numeros)

        posicao = busca_sequencial(numeros, item)

        print("\n--- RESULTADO DA BUSCA ---")

        if posicao != -1:
            print(f"Número pesquisado: {item}")
            print("Status: Encontrado")
            print(f"Posição na lista: {posicao}")
        else:
            print(f"Número pesquisado: {item}")
            print("Status: Não encontrado")

    except ValueError:
        print("Erro: informe apenas números inteiros.")


if __name__ == "__main__":
    main()
