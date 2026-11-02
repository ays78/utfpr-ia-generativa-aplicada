
"""
Exercício 09 - Preenchimento Sequencial de Lista
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Ler um número inteiro e preencher uma lista de 10 posições.

Cada elemento da lista deve receber o valor inicial
somado ao índice da posição correspondente.

Conceitos:
- Listas
- Estruturas de repetição (for)
- Operadores aritméticos
- Funções
- Type hints e docstrings
- Tratamento de exceções
"""

TAMANHO_LISTA = 10


def gerar_lista(valor_inicial: int) -> list[int]:
    """
    Gera uma lista com valores sequenciais.

    Args:
        valor_inicial: Número inteiro informado pelo usuário.

    Returns:
        Lista de 10 números inteiros, começando pelo
        valor inicial e incrementando de 1 em 1.
    """
    numeros = [0] * TAMANHO_LISTA

    for indice in range(TAMANHO_LISTA):
        numeros[indice] = valor_inicial + indice

    return numeros


def exibir_resultados(
    valor_inicial: int,
    numeros: list[int]
) -> None:
    """Exibe os índices, os cálculos e os resultados."""
    for indice, numero in enumerate(numeros):
        print(
            f"x[{indice}] = "
            f"{valor_inicial} + {indice} = {numero}"
        )


def main() -> None:
    """Executa o programa principal."""
    try:
        valor_inicial = int(input())

        numeros = gerar_lista(valor_inicial)

        exibir_resultados(valor_inicial, numeros)

    except ValueError:
        print("Erro: informe um número inteiro válido.")


if __name__ == "__main__":
    main()
