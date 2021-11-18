# Exercício Python 39: Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com a sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora exata de se alistar ou se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
from datetime import date

ano = int(input('Ano de nascimento: '))
print('Quem nasceu em {} tem {} anos em {}'.format(ano, (date.today().year - ano), date.today().year))
if date.today().year - ano == 18:
    print('Você deve se alistar IMEDIATAMENTE!')
elif date.today().year - ano < 18:
    print('Ainda falta(m) {} ano(s) para o alistamento!'.format(18 - (date.today().year - ano)))
    print('Seu alistamento será em {}'.format(18 - (date.today().year - ano) + date.today().year))
else:
    print('Você já deveria ter se alistado há {} ano(s)'.format((date.today().year - ano) - 18))
    print('Seu alistamento foi em {}'.format(date.today().year - ((date.today().year - ano) - 18)))
