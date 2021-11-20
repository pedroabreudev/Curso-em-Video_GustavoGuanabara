# Exercício Python 059: Crie um programa que leia dois valores e mostre um menu na tela:
# [ 1 ] somar
# [ 2 ] multiplicar
# [ 3 ] maior
# [ 4 ] novos números
# [ 5 ] sair do programa
# Seu programa deverá realizar a operação solicitada em cada caso.
from time import sleep
n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    opção = int(input('>>>>> Qual é a sua opção? '))
    if opção == 1:
        print('A soma entre {} + {} é = {}'.format(n1, n2, n1 + n2))
    elif opção == 2:
        print('A multiplicação entre {} x {} é = {}'.format(n1, n2, n1 * n2))
    elif opção == 3:
        if n1 > n2:
            print('O maior entre {} e {} é o {}'.format(n1, n2, n1))
        elif n1 == n2:
            print('O número {} e o número {} são IGUAIS!'.format(n1, n2))
        else:
            print('O maior entre {} e {} é o {}'.format(n1, n2, n2))
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente')
    print('=-=' * 10)
    sleep(0.5)
print('Saindo do programa! Volte sempre!')


