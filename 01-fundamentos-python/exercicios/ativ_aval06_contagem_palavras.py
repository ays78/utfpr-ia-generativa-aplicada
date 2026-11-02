#Faça um programa para ler uma String e apresente todos as palavras desta String. Leve em consideração que entre as palavras existem um, e somente um, caractere espaço. Veja, também, que o ponto final não faz parte da última palavra. Observe o resultado final na coluna “Resultados”.

# Leitura da frase
frase = input()

# Remove o ponto final, se existir
if frase.endswith("."):
    frase = frase[:-1]

# Separa as palavras
palavras = frase.split(" ")

# Conta as palavras
quantidade = len(palavras)

# Exibe o resultado
print(f"Existem {quantidade} palavras, são elas:")
print()

for i in range(quantidade):
    print(f"{i + 1}a. palavra = {palavras[i]}")
