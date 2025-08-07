#Media escolar
nome=str(input('\033[35m Qual o teu nome e sobre nome? ')).strip().title().split()
print(f'\n    Ola {nome[0]}!! Seja Bem Vindo ao Calculador de Média Escolar, \niremos calcular sua média de acordo com a nota das três unidades.\n')

n1=float(input('Digite a média da primeira unidade: '))

#pergunta sobre a segunda unidade
resposta_n1 = (input('Tem a média da segunda unidade?(Sim/Não) ')).strip().title()
if resposta_n1 =='Sim':
    n2=float(input('Digite a média da segunda unidade: '))
else:
    print('Não posso calcular sua média no agora, preciso de duas notas no minimo!!!')

resposta_n2 = str(input('Tem a nota da terceira unidade? ')).strip().title()
if resposta_n2 =='Sim':
    n3=float(input('Digite a nota da terceira unidade: '))
    soma2 = (n1+n2+n3)/3
    print (f'A sua média final somando as tres unidade é {soma2:.2f}')

else:
    media1=(n1+n2)/2
    print(f'Sua média da primeira e segunda unidade é {media1:.2f}')

print('FIM')
input()