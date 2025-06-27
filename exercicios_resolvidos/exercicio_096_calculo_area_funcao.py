'''
Faça um programa que tenha uma função chamada area(), que receba 
as dimensões de um terreno retangular (largura e comprimento) e
mostre a área do terreno.
'''

# Função
def area(largura, comprimento):
    terreno = largura * comprimento
    print(f'A área de um terreno {largura:.1f}x{comprimento:.1f} é de {terreno}m²')



# Programa principal
print('Controle de Terrenos')
print('-' * 20)
larg = float(input('Largura (m): '))
comp = float(input('Comprimento (m): '))
area(largura=larg, comprimento=comp)