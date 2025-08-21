#Programa que ler varios numeros e faz a soma

numeros = []
soma = 0  # Inicializa a variável 'soma' com 0

while True:
    entrada = input('Digite um numero para fazer a soma (ou "sair" para finalizar): ')
    if entrada.lower() == 'sair': # 2. Transforma a entrada em minúsculas
        break
    try:
        numero = int(entrada) # 3. Converte a entrada para inteiro dentro do try
        numeros.append(numero)
    except ValueError:
        print('Entrada inválida. Por favor, digite um número ou "sair".')

for numero in numeros:
    soma += numero

print(f'A soma dos números é: {soma}')