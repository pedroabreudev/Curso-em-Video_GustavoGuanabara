# Exercício Python 11: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la,
# sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.
largura = float(input('Informe a Lagura da parede em metros: '))
altura = float(input('Informe a Altura da parede em metros: '))
print('Sua parede tem a dimensão de {}x{} e sua área é de {:.3f}m².'.format(largura, altura, (largura*altura)))
print('Para pintar essa parede, você precisará de {:.2f}l de tinta.'.format((largura*altura)/2))
