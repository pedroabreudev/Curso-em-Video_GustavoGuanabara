# Exercício Python 45: Crie um programa que faça o computador jogar Jokenpô com você.
from random import randint
from time import sleep

print('{:=^40}'.format(' Jokenpô '))
print('''Suas opções:
 [ 0 ] PEDRA
 [ 1 ] PAPEL
 [ 2 ] TESOURA ''')
jogador = int(input('Qual é a sua jogada? '))
itens = ('PEDRA', 'PAPEL', 'TESOURA')
computador = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO!!!')
print('-=' * 16)
print('O Jogador escolheu {} !'.format(itens[jogador]))
print('O Computador escolheu {} !'.format(itens[computador]))
print('-=' * 16)
if computador == jogador:
    print('EMPATE!')
elif computador == 0 and jogador == 1:
    print('JOGADOR VENCEU!')
elif computador == 0 and jogador == 2:
    print('COMPUTADOR VENCEU!')
elif computador == 1 and jogador == 0:
    print('COMPUTADOR VENCEU!')
elif computador == 1 and jogador == 2:
    print('JOGADOR VENCEU!')
elif computador == 2 and jogador == 0:
    print('JOGADOR VENCEU!')
elif computador == 2 and jogador == 1:
    print('COMPUTADOR VENCEU!')