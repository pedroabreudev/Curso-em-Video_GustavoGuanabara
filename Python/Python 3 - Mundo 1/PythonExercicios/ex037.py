# Exercício Python 37:
# Escreva um programa em Python que leia um número inteiro qualquer e peça para o usuário escolher qual será a base de conversão:
# 1 para binário, 2 para octal e 3 para hexadecimal.
numero = int(input('Informe um número inteiro: '))
print('Escolha uma das bases para conversão:\n[ 1 ] Binário\n[ 2 ] Octal\n[ 3 ] Hexadecimal')
escolha = int(input('Escolha a base de conversão: '))
if escolha == 1:
    print('{} covertido para BINÁRIO é igual a {}'.format(numero, bin(numero)[2:]))
elif escolha == 2:
    print('{} covertido para OCTAL é igual a {}'.format(numero, oct(numero)[2:]))
elif escolha == 3:
    print('{} covertido para HEXADECIMAL é igual a {}'.format(numero, hex(numero)[2:]))
else:
    print('Escolha inválida. Tente novamente!')