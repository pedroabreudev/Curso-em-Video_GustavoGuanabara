# Exercício Python 44: Elabore um programa que calcule o valor a ser pago por um produto,
# considerando o seu preço normal e condição de pagamento:
# à vista dinheiro/cheque: 10% de desconto
# à vista no cartão: 5% de desconto
# em até 2x no cartão: preço formal
# 3x ou mais no cartão: 20% de juros
print('{:=^40}'.format(' LOJAS GUANABARA '))
valor = float(input('Preço das compras: R$ '))
print('''FORMAS DE PAGAMENTO
 [ 1 ] à vista dinheiro ou cheque
 [ 2 ] à vista cartão
 [ 3 ] 2x no cartão
 [ 4 ] 3x ou mais no cartão''')
opção = int(input('Qual é a opção? '))
if opção == 1:
    total = valor - (valor * 10 / 100)
elif opção == 2:
    total = valor - (valor * 5 / 100)
elif opção == 3:
    total = valor
    parcela = total / 2
    print('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opção == 4:
    total = valor + (valor * 20 / 100)
    totalparcelas = int(input('Quantas parcelas? '))
    parcela = total / totalparcelas
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparcelas, parcela))
else:
    total = valor
    print('OPÇÃO INVÁLIDA de pagamento. Tente novamente! ')
print('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(valor, total))
