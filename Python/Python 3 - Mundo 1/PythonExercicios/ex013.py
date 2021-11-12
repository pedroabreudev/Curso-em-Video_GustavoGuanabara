# Exercício Python 13: Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.
salario = float(input('Informe o seu sálario em: R$'))
print('O seu sálario é R$ {:.2f}, seu novo sálario com aumento de 15% é R$ {:.2f}'.format(salario, (salario * 1.15)))