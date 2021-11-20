# Exercício Python 060:
# Faça um programa que leia um número qualquer e mostre o seu fatorial.
# Exemplo:5! = 5 x 4 x 3 x 2 x 1 = 120
num = int(input('Digite um número para calcular seu Fatorial: '))
fatorial = 1
controler = num
print('Calculando o Fatorial de {}! = '.format(num), end='')
while controler > 0:
    print('{}'.format(controler), end='')
    print(' x ' if controler > 1 else ' = ', end='')
    fatorial *= controler
    controler -= 1
print('{}'.format(fatorial))
