"""
Atividade Pratica 01 - Média Aritmética
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Ler dois números inteiros e calcular sua média aritmética,
apresentando o resultado com uma casa decimal.
"""


def calcular_media(numero1: int, numero2: int) -> float:
    """Calcula a média aritmética de dois números inteiros."""
    return (numero1 + numero2) / 2


def main() -> None:
    """Executa o programa principal."""
    print("=== CALCULADORA DE MÉDIA ARITMÉTICA ===")

    try:
        numero1 = int(input("Digite o primeiro número: "))
        numero2 = int(input("Digite o segundo número: "))

        media = calcular_media(numero1, numero2)

        print("\n--- RESULTADO ---")
        print(f"Primeiro número: {numero1}")
        print(f"Segundo número:  {numero2}")
        print(f"Média aritmética: {media:.1f}")

    except ValueError:
        print("Erro: informe apenas números inteiros.")


if __name__ == "__main__":
    main()
