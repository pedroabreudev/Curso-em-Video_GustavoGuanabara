# Exercício Python 16: Crie um programa que leia um número Real qualquer pelo teclado e mostre
# na tela a sua porção Inteira.
import math

num = float(input('Digite um valor: '))
inteiro = math.trunc(num)
print('O valor digitado foi {} e a sua porção inteira é {}'.format(num, inteiro))

