'''
Faça um progra que tenha uma função chamada escreva(), que receba
um texto qualquer como parâmetro e mostre uma mensagem com tamanho
adaptável.
Ex: escreva('Hello World!')
Saída:
~~~~~~~~~~~~
Hello World!
~~~~~~~~~~~~
'''

# Função
def escreva(msg):
    tam = len(msg) + 4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)


# Programa principal
texto = str(input('Informe o texto: '))

escreva(msg=texto)
