"""
Atividade Pratica 05 - Repetição de caracteres de uma string
Disciplina: Fundamentos de Python
Curso: Especialização em IA Generativa Aplicada - UTFPR
Professor: Omero Francisco Bertol

Exercício: 
 Faça um programa para ler uma String e apresente todos os caracteres desta String 3 (três) vezes na tela do computador.
 Observe o resultado final na coluna “Resultados”.


Descrição:
    Desenvolver um programa que leia uma string informada
    pelo usuário, separe seus caracteres por espaços e
    apresente o resultado três vezes na tela.

Conceitos utilizados:
    - Entrada de dados com input()
    - Manipulação de strings
    - Método join()
    - Estrutura de repetição for
    - Função range()
    - Saída de dados com print()
"""

def main():
    # Realiza a leitura da string informada pelo usuário.
    texto = input()

    # Separa os caracteres da string utilizando espaços.
    caracteres_separados = " ".join(texto)

    # Exibe os caracteres separados três vezes.
    for _ in range(3):
        print(caracteres_separados)


if __name__ == "__main__":
    main()
