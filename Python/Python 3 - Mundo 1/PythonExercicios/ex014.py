# Exercício Python 14: Escreva um programa que converta uma temperatura digitando em graus Celsius
# e converta para graus Fahrenheit.
temperatura = float(input('Informe a temperatura em C: '))
print('A temperatura de {:.2f}C corresponde a {:.2f}F!'.format(temperatura, (temperatura * (9 / 5)) + 32))
