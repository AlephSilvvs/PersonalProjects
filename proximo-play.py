# Pergunta o total de execicios feitos no dia e aquantidade de acertos
total = int(input('Quantos exercicios você fez? '))
acertos = int(input('Quantos você acertou? '))

# Calculos
if total > 0:
    porc = acertos / total * 100
    erros = total - acertos
    print(f'No total de {total} exercicios feito, você acertou {acertos} e errou {erros}\n'
          f'Sua porcentagem é de {porc:.0f}%')

else:
    print ('O total de exercicios deve ser maior que zero.')


