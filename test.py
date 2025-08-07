# Pede o nome e sobrenome, formatando-o corretamente
nome = str(input('\033[35m Qual o teu nome e sobrenome? ')).strip().title().split()
print(
    f'\n    Olá {nome[0]}!! Seja Bem Vindo ao Calculador de Média Escolar, \niremos calcular sua média de acordo com as notas que você fornecer.\n')

# Pede a nota da primeira unidade
try:
    n1 = float(input('Digite a nota da primeira unidade: '))
except ValueError:
    print('Entrada inválida. Por favor, digite um número.')
    exit()

# Pergunta sobre a segunda unidade
resposta_n2 = str(input('Tem a nota da segunda unidade? (Sim/Não) ')).strip().title()

if resposta_n2 == 'Sim':
    try:
        n2 = float(input('Digite a nota da segunda unidade: '))
    except ValueError:
        print('Entrada inválida. Por favor, digite um número.')
        exit()

    # Pergunta sobre a terceira unidade
    resposta_n3 = str(input('Tem a nota da terceira unidade? (Sim/Não) ')).strip().title()

    if resposta_n3 == 'Sim':
        try:
            n3 = float(input('Digite a nota da terceira unidade: '))
        except ValueError:
            print('Entrada inválida. Por favor, digite um número.')
            exit()

        # Calcula e exibe a média das três notas
        media_final = (n1 + n2 + n3) / 3
        print(f'\nSua média final, somando as três unidades, é {media_final:.2f}')

    else:
        # Calcula e exibe a média das duas notas
        media_parcial = (n1 + n2) / 2
        print(f'\nSua média parcial (primeira e segunda unidade) é {media_parcial:.2f}')

else:
    # Caso o usuário não tenha a segunda nota
    print('Não é possível calcular a média. É preciso ter no mínimo duas notas.')

print('\nFIM')

# O input() no final só é necessário se você estiver rodando em um terminal que fecha imediatamente.
# Para scripts Python, geralmente não é necessário.
# input()