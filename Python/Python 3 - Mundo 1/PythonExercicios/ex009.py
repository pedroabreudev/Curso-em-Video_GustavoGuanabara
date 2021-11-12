# Exercício Python 9: Faça um programa que leia um número Inteiro qualquer e mostre na tela a sua tabuada.
numero = int(input('Digite um número para ver sua tabuada: '))
indice = 0
print('-' * 12)
while indice <= 10:
    print('{} x {:2} = {}'.format(numero, indice, (numero * indice)))
    indice = indice + 1
print('-' * 12)
