# Exercício Python 20: O mesmo professor do desafio 19 quer sortear a ordem de apresentação
# de trabalhos dos alunos.  Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
from random import shuffle

p = input('Primeiro aluno: ')
s = input('Segundo aluno: ')
t = input('Terceiro aluno: ')
q = input('Quarto aluno: ')
list = [p, s, t, q]
shuffle(list)
print('A ordem de apresentação será {}'.format(list))