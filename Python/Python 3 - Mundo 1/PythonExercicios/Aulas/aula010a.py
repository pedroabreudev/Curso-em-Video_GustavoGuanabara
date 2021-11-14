# tempo = int(input('Quantos anos tem seu carro? '))
# if tempo <=3:
#     print('Carro novo')
# else:
#     print('Carro velho')
# print('--FIM--')

# nome = str(input('Qual é seu nome? '))
# if nome == 'Pedro':
#     print('Que nome lindo você tem!')
# else:
#     print('Seu nome é tão normal!')
# print('Bom dia, {}!'.format(nome))

n1 = float(input('Informe a sua primeira nota:'))
n2 = float(input('Informe a sua segunda nota:'))
print('Sua média é {:.1f}, e você foi {}!'.format((n1 + n2) / 2, 'APROVADO' if (n1 + n2) / 2 >= 6 else 'REPROVADO'))
