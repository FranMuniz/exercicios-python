'''Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade
de tinta necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m².
'''

largura = float(input('Informe a largura da sua parede em metros: '))
altura = float(input('Informe a altura da sua parede em metros: '))
area = largura * altura
tinta = area / 2

print(f'Sua parede tem a dimensão de {largura}x{altura} e sua área é de {area:.2f}m²')
print(f'Para pintar a parede, você precisará de {tinta:.2f}l de tinta :)')