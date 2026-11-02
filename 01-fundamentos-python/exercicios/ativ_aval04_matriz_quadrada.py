
"""
Atividade Pratica 04 - Matriz Quadrada com Bordas
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Ler um número inteiro que representa o tamanho de uma
matriz quadrada NxN.

A matriz deverá ser preenchida seguindo as regras:
- Bordas externas: asteriscos (*)
- Região interna: arrobas (@)

Conceitos:
- Estruturas de repetição (for)
- Laços aninhados
- Estruturas condicionais
- Listas
- Funções
- Validação de entrada
"""

SIMBOLO_BORDA = "*"
SIMBOLO_INTERNO = "@"


def gerar_matriz(tamanho: int) -> list[list[str]]:
    """
    Gera uma matriz quadrada com bordas diferenciadas.

    Args:
        tamanho: Quantidade de linhas e colunas.

    Returns:
        Matriz bidimensional contendo '*' nas bordas
        e '@' na região interna.
    """
    matriz = []

    for linha in range(tamanho):
        elementos = []

        for coluna in range(tamanho):
            if (
                linha == 0
                or linha == tamanho - 1
                or coluna == 0
                or coluna == tamanho - 1
            ):
                elementos.append(SIMBOLO_BORDA)
            else:
                elementos.append(SIMBOLO_INTERNO)

        matriz.append(elementos)

    return matriz


def exibir_matriz(matriz: list[list[str]]) -> None:
    """Exibe os elementos da matriz formatados."""
    for linha in matriz:
        print(" ".join(linha))


def main() -> None:
    """Executa o programa principal."""
    print("=== GERADOR DE MATRIZ QUADRADA ===")

    try:
        tamanho = int(input("Informe o tamanho da matriz: "))

        if tamanho <= 0:
            print("Erro: informe um número inteiro positivo.")
            return

        matriz = gerar_matriz(tamanho)

        print(f"\n--- MATRIZ {tamanho}x{tamanho} ---")
        exibir_matriz(matriz)

    except ValueError:
        print("Erro: informe apenas números inteiros.")


if __name__ == "__main__":
    main()
