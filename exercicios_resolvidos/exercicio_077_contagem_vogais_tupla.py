'''
Crie um programa que tenha uma tupla com várias palavras (sem acentos) e, 
em seguida, mostre, para cada palavra, quais são as suas vogais.
'''

palavras = ('aprender', 'programar', 'linguagem', 'python', 'curso', 'gratis', 'estudar', 'praticar', 'trabalhar', 'mercado')
print('-' * 40)
print(f'{"VOGAIS":^40}')
print('-' * 40)
for palavra in palavras:
    vogais = [letra for letra in palavra if letra.lower() in 'aeiou']
    print(f'Na palavra "{palavra}" temos as vogais: {", ".join(vogais)}')
print('-' * 40) 