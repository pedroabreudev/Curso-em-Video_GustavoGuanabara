# Exercício Python 55: Faça um programa que leia o peso de cinco pessoas.
# No final, mostre qual foi o maior e o menor peso lidos.
menorPeso = 0
maiorPeso = 0
for contador in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(contador)))
    if contador == 1:
        menorPeso = peso
        maiorPeso = peso
    else:
        if peso > maiorPeso:
            maiorPeso = peso
        if peso < menorPeso:
            menorPeso = peso
print('O maior peso lido foi de {:.2f}KG'.format(maiorPeso))
print('O menor peso lido foi de {:.2f}KG'.format(menorPeso))
