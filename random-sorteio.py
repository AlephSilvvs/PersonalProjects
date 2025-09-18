"""Um professor quer sortear um dos seus quatro alunos para apagar o quadro. Faça um programa que ajude ele,
lendo o nome deles e escrevendo o nome do escolhido"""

import random

# Lista para armazenar os nomes
nomes = []

# Loop para ler os nomes
print("Digite os nomes que você quer sortear. Digite 'fim' quando terminar.")
while True:
    nome = input("Digite um nome: ")
    if nome.lower() == 'fim':
        break  # Sai do loop se o usuário digitar 'fim'
    elif nome:  # Garante que não adicionamos nomes vazios
        nomes.append(nome)

# Verifica se a lista não está vazia antes de sortear
if nomes:
    # Sorteia um nome da lista
    nome_sorteado = random.choice(nomes)

    # Exibe o nome sorteado
    print(f"\nO nome sorteado foi: {nome_sorteado}")
else:
    print("\nNenhum nome foi digitado. O sorteio não pode ser realizado.")