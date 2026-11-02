
"""
Exercício 08 - Menor e Maior Elemento de uma Lista
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Ler 7 números inteiros, armazená-los em uma lista
e identificar o menor e o maior elemento, incluindo
suas respectivas posições.

Conceitos:
- Listas
- Estruturas de repetição (for)
- Funções
- Operações min() e max()
- Método index()
- Tratamento de exceções
- Type hints e docstrings
"""

QUANTIDADE_ELEMENTOS = 7


def ler_numeros(quantidade: int) -> list[int]:
    """
    Lê uma quantidade definida de números inteiros.

    Args:
        quantidade: Número de elementos a serem informados.

    Returns:
        Lista contendo os números digitados.
    """
    numeros = []

    for _ in range(quantidade):
        numero = int(input())
        numeros.append(numero)

    return numeros


def encontrar_extremos(
    numeros: list[int]
) -> tuple[int, int, int, int]:
    """
    Identifica o menor e o maior elemento da lista.

    Returns:
        Tupla contendo:
        - Posição do menor elemento
        - Valor do menor elemento
        - Posição do maior elemento
        - Valor do maior elemento

    Raises:
        ValueError: Se a lista estiver vazia.
    """
    if not numeros:
        raise ValueError("A lista não pode estar vazia.")

    menor = min(numeros)
    maior = max(numeros)

    pos_menor = numeros.index(menor)
    pos_maior = numeros.index(maior)

    return pos_menor, menor, pos_maior, maior


def exibir_resultados(numeros: list[int]) -> None:
    """Exibe os elementos e os valores extremos."""
    for indice, numero in enumerate(numeros):
        print(f"x[{indice}] = {numero}")

    pos_menor, menor, pos_maior, maior = encontrar_extremos(
        numeros
    )

    print()
    print(f"Menor elemento, x[{pos_menor}] = {menor}")
    print(f"Maior elemento, x[{pos_maior}] = {maior}")


def main() -> None:
    """Executa o programa principal."""
    try:
        numeros = ler_numeros(QUANTIDADE_ELEMENTOS)
        exibir_resultados(numeros)

    except ValueError as erro:
        print(f"Erro: {erro}")


if __name__ == "__main__":
    main()
