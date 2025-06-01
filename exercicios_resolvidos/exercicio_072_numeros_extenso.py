'''
Crie um programa que tenha uma tupla totalmente preenchida com uma
contagem por extenso, de zero até vinte.
Seu programa deverá ler um número pelo teclado (entre 0 e 20) e
mostrá-lo por extenso.
'''

numeros_extenso = (
    'zero', 'um', 'dois', 'três', 'quatro', 'cinco',
    'seis', 'sete', 'oito', 'nove', 'dez',
    'onze', 'doze', 'treze', 'catorze', 'quinze',
    'dezeseis', 'dezesete', 'dezoito', 'dezenove', 'vinte'
)


while True:
    num = int(input('Informe um número entre 0 e 20: '))

    if 0 <= num <= 20:
        print(f'Você digitou o número {numeros_extenso[num]}.')
        opcao = str(input('Deseja continuar [S/N]?: ')).strip().upper()

        if opcao == 'N':
            break 
    else:
        print('Tente novamente! Valor fora do range (0 a 20).')

