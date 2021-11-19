# Exercício Python 56:
# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
# No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho
# e quantas mulheres têm menos de 20 anos.
somaidades = 0
maiorhomem = 0
nomevelho = ''
menormulher20 = 0
for contador in range(1, 5):
    print('-' * 5 + ' {}ª PESSOA'.format(contador) + '-' * 5)
    nome = str(input('Nome: ')).strip().upper()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    somaidades += idade
    if contador == 1 and sexo == 'M':
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'M' and idade > maiorhomem:
        maiorhomem = idade
        nomevelho = nome
    if sexo in 'F' and idade < 20:
        menormulher20 += 1
mediaidade = somaidades / 4
print('A média de idade do grupo é de {:.2f} anos'.format(mediaidade))
print('O nome do homem tem {} anos e se chama {}'.format(maiorhomem, nomevelho))
print('Ao todo são {} mulheres com menos de 20 anos'.format(menormulher20))
