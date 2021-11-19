# Exercício Python 54: Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.
from datetime import date
maiores = 0
menores = 0
for controle in range(1, 8):
    ano = int(input('Em que ano a {}ª pessoa nasceu? '.format(controle)))
    if date.today().year - ano < 21:
        menores += 1
    else:
        maiores += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(maiores))
print('E também tivemos {} pessoas menores de idade'.format(menores))
