# Exercício Python 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três
# e que se encontram no intervalo de 1 até 500.

soma = 0
numeros = 0
for contador in range(1, 501, 2):
    if contador % 3 == 0:
        soma += contador
        numeros += 1
print('A soma de todos os {} valores solicitados é {}'.format(numeros, soma))
