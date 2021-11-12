# Exercício Python 10: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira
# e mostre quantos dólares ela pode comprar.
reais = float(input('Quantos reais você tem na carteira? R$ '))
print('Com R$ {:.2f}, você pode comprar US$ {:.2f}'.format(reais, (reais/3.27)))
