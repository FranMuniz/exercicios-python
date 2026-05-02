'''
Dada uma string:
    "aabbcdeff"
Retorne o primeiro caractere que não se repete.
Ex: 'c'
'''

from collections import Counter

texto = 'aabbcdeff'
contagem = Counter(texto)

for char in texto:
    if contagem[char] == 1:
        print(char)
        break