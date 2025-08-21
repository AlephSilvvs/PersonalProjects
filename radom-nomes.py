#Lista de nomes
nomes = []

while True:
    nome = input ('Digite um nome (ou "sair" para finalizar): ')
    if nome.lower() == 'sair':
        break
    nomes.append(nome)
print ('\nNomes inseridos: ')
for n in nomes:
    print(n)