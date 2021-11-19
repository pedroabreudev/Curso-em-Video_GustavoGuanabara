# Laços de Repetição (Parte 2)
N = 1
par = impar = 0
while N != 0:
    N = int(input('Digite um valor: '))
    if N % 2 == 0:
        par += 1
    else:
        impar += 1
print('Você digitou {} números pares e {} números ímpares'.format(par, impar))
