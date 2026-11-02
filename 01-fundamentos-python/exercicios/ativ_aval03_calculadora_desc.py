"""
Atividade Pratica 03 - Calculadora de Desconto Condicional
Disciplina: Fundamentos de Python
Especialização em IA Generativa Aplicada - UTFPR

Objetivo:
Calcular o desconto aplicado ao valor de um produto,
considerando as seguintes regras:

- Valores inferiores a R$ 5.000,00: desconto de 10%.
- Valores iguais ou superiores a R$ 5.000,00: desconto de 15%.

Conceitos:
- Variáveis e constantes
- Estruturas condicionais
- Funções e parâmetros
- Operadores aritméticos
- Tratamento de exceções
- Formatação de saída
"""

LIMITE_DESCONTO = 5000.00
DESCONTO_PADRAO = 10
DESCONTO_ESPECIAL = 15


def calcular_percentual_desconto(valor_produto: float) -> int:
    """Determina o percentual de desconto conforme o valor."""
    if valor_produto < LIMITE_DESCONTO:
        return DESCONTO_PADRAO

    return DESCONTO_ESPECIAL


def calcular_valor_final(
    valor_produto: float,
    percentual: int
) -> tuple[float, float]:
    """Calcula o desconto aplicado e o valor final."""
    valor_desconto = valor_produto * percentual / 100
    valor_final = valor_produto - valor_desconto

    return valor_desconto, valor_final


def exibir_resultado(
    valor_produto: float,
    percentual: int,
    valor_desconto: float,
    valor_final: float
) -> None:
    """Apresenta o resumo dos valores calculados."""
    print("\n=== RESUMO DA COMPRA ===")

    descricao_produto = "Valor do Produto"
    descricao_desconto = f"Valor do Desconto ({percentual}%)"
    descricao_final = "Valor Final"

    print(f"{descricao_produto:<23} = R$ {valor_produto:.2f}")
    print(f"{descricao_desconto:<23} = R$ {valor_desconto:.2f}")
    print(f"{descricao_final:<23} = R$ {valor_final:.2f}")


def main() -> None:
    """Executa o programa principal."""
    print("=== CALCULADORA DE DESCONTOS ===")

    try:
        valor_produto = float(
            input("Informe o valor do produto (R$): ")
        )

        if valor_produto < 0:
            print("Erro: o valor do produto não pode ser negativo.")
            return

        percentual = calcular_percentual_desconto(valor_produto)

        valor_desconto, valor_final = calcular_valor_final(
            valor_produto,
            percentual
        )

        exibir_resultado(
            valor_produto,
            percentual,
            valor_desconto,
            valor_final
        )

    except ValueError:
        print("Erro: informe um valor numérico válido.")


if __name__ == "__main__":
    main()
