
"""
Exercício 07 - Preenchimento de Lista: Posições Pares e Ímpares
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Ler um número inteiro que representa o tamanho de uma lista.

Regras:
- Posições pares recebem o valor 0.
- Posições ímpares recebem o valor 1.
- A lista deve ser exibida entre chaves, com valores
  separados por vírgula e espaço.

Conceitos:
- Listas
- Estruturas de repetição
- Estruturas condicionais
- Operador módulo (%)
- Funções e type hints
- Formatação de saída
"""


def gerar_lista(tamanho: int) -> list[int]:
    """
    Gera uma lista com valores alternados entre 0 e 1.

    Args:
        tamanho: Quantidade de elementos da lista.

    Returns:
        Lista de inteiros contendo 0 nas posições pares
        e 1 nas posições ímpares.
    """
    lista = []

    for indice in range(tamanho):
        if indice % 2 == 0:
            lista.append(0)
        else:
            lista.append(1)

    return lista


def formatar_lista(lista: list[int]) -> str:
    """
    Formata uma lista de inteiros conforme o enunciado.

    Args:
        lista: Lista de números inteiros.

    Returns:
        Representação textual com valores entre chaves.
    """
    elementos = ", ".join(str(valor) for valor in lista)
    return "{" + elementos + "}"


def main() -> None:
    """Executa o programa principal."""
    try:
        tamanho = int(input())

        if tamanho < 0:
            print("Erro: o tamanho não pode ser negativo.")
            return

        lista = gerar_lista(tamanho)
        print(formatar_lista(lista))

    except ValueError:
        print("Erro: informe um número inteiro válido.")


if __name__ == "__main__":
    main()
