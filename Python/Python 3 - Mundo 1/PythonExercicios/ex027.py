# Exercício Python 27:
# Faça um programa que leia o nome completo de uma pessoa,
# mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Informe seu nome completo: ')).strip()
separa = nome.split()
print('Muito prazer em te conhecer!')
print('O seu primeiro nome é {}, e o seu último nome é {}'.format(separa[0], separa[len(separa)-1]))
