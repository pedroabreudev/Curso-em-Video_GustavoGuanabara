# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
numero = int(input('Informe um número inteiro: '))
print('O seu número é {}, o seu dobro é {}, o seu triplo é {},'
      ' e a sua raiz quadrada é {:.2f}'.format(numero, numero*2, numero*3, numero**(1/2)))
