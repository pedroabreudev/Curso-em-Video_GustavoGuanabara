# Exercício Python 28:
# Escreva um programa que faça o computador “pensar” em um número inteiro
# entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
from random import randint
from time import sleep

print('-=-' * 20)
print('Estou pensando em um número entre 1 e 5....\nJá pensei ')
numero = randint(0, 5)
escolhido = int(input('Informe o número que você acha que eu escolhi: '))
print('PROCESSANDO...')
sleep(3)
print('O númerio escolhido foi {} e {}'.format(numero, 'você acertou, parabéns!'
if numero == escolhido else 'você errou!'))
print('-=-' * 20)
