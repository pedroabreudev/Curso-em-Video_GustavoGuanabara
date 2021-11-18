# Exercício Python 040: Crie um programa que leia duas notas de um aluno e calcule sua média,
# mostrando uma mensagem no final, de acordo com a média atingida:
# – Média abaixo de 5.0: REPROVADO
# – Média entre 5.0 e 6.9: RECUPERAÇÃO
# – Média 7.0 ou superior: APROVADO

n1 = float(input('Primeira nota: '))
n2 = float(input('Segunda nota: '))
print('Tirando {:.2f} e {:.2f} a média do aluno é {:.2f}'.format(n1, n2, (n1 + n2) / 2))
if (n1 + n2) / 2 >= 7.0:
    print('O aluno está APROVADO')
elif (n1 + n2) / 2 < 5.0:
    print('O aluno está REPROVADO')
else:
    print('O aluno está de RECUPERAÇÃO')
