#Exercício Python 15: Escreva um programa que pergunte a quantidade de Km percorridos
# por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
# Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
km = float(input('Informe os Km percorridos: '))
dias = int(input('Informe os Dias alugados: '))
custoKM = km * 0.15
custoDia = dias * 60
soma = custoDia + custoKM
print('O valor a ser pago é R${:.2f}'.format(soma))
