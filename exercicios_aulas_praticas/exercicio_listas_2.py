
teste = []

teste.append('Fran')
teste.append(28)

galera = []
# galera.append(teste) # Cria uma ligação entre as duas listas, se mudar uma estrutura, automaticamente muda a outra.
galera.append(teste[:]) # Cria uma cópia
teste[0] = 'André'
teste[1] = 30
galera.append(teste[:])

print(teste)
print(galera)

#######################

pessoas = [['Carlota Jones', 39], ['Helô Moules', 28], ['Fiorella Delano', 30], ['Zambrota Wadiya', 29], ['Ygona Thunder', 22]]

print(pessoas[0]) # Carlota Jones, 39
print(pessoas[0][0]) # Carlota Jones
print(pessoas[4][1]) # 22
print(pessoas[3][0]) # Zambrota Wadiya

for pessoa in pessoas:
    print(f'{pessoa[0]} tem {pessoa[1]} anos de idade.')

#######################

funcionarios = []
dado = []

for i in range (0, 3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    funcionarios.append(dado[:])
    dado.clear()

for pessoa in funcionarios:
    if pessoa[1] >= 18:
        print(f'{pessoa[0]} é maior de idade. Tem {pessoa[1]} anos.')

print(funcionarios)

#######################