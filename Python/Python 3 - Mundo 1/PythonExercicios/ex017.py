# Exercício Python 17: Faça um programa que leia o comprimento
# do cateto oposto e do cateto adjacente de um triângulo retângulo.
# Calcule e mostre o comprimento da hipotenusa.

import math
oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hipotenusa = (oposto**2) + (adjacente**2)
print('O comprimento da hiponetesa é {:.2f}'.format(math.sqrt(hipotenusa)))

oposto = float(input('Comprimento do cateto oposto: '))
adjacente = float(input('Comprimento do cateto adjacente: '))
hi = math.hypot(oposto, adjacente)
print('O comprimento da hiponetesa é {:.2f}'.format(hi))