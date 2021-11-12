# Exercício Python 7: Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.
nota1 = float(input('Informe a primeira nota: '))
nota2 = float(input('Informe a segunda nota: '))
print('A primeira nota é {}, a segunda nota é {}, a média é {:.2f}'.format(nota1, nota2, (nota1+nota2)/2))
