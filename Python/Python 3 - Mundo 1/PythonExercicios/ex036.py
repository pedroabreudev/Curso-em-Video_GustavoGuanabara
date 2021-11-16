# Exercício Python 36: Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
# Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
# A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.

casa = float(input('Informe o valor da casa a ser financiada? R$ '))
salario = float(input('Informe o seu sálario? R$ '))
anos = int(input('Informe em quantos pretende pagar o financiamento? '))
prestacao = casa / (anos * 12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(casa, anos, prestacao))
if prestacao <= (salario * 30 / 100):
    status = 'APROVADO'
else:
    status = 'NEGADO'
print('Emprestimo pode ser {}'.format(status))
