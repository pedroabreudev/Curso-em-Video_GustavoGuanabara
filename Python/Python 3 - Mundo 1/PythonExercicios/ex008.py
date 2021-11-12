# Exercício Python 8: Escreva um programa que leia um valor em metros e o exiba convertido em centímetros e milímetros.
valor = float(input('Informe um valor em metros: '))
print('O valor informado é {} metros,'
      ' convertido em centímetros é {}, e convertido em milímetros é {}'.format(valor, (valor*100), (valor*1000)))
