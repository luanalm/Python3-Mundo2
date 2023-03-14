# Exercício 37
# Escreva um programa que leia um número inteiro qualquer e preça para o usuário escolhar qual será a base de conversão:
# 1 - Binário
# 2 - Octal
# 3 - Hexadecimal

b = int(input('''Escolha para qual você deseja converter um número.
1 - Binário
2 - Octal
3 - Hexadecimal
Digite o número da base de conversão escolhida (1, 2 ou 3): '''))

if b == 1:
    n = int(input('Agora digite o número que deseja converter para Binário: '))
    print('O número {} convertido para Binário é {}.'.format(n, bin(n)))
elif b == 2:
    n = int(input('Agora digite o número que deseja converter para Octal: '))
    print('O número {} convertido para Octal é {}.'.format(n, oct(n)))
elif b == 3:
    n = int(input('Agora digite o número que deseja converter para Hexadecimal: '))
    print('O número {} convertido para Hexadecimal é {}.'.format(n, hex(n)))
else:
    print('O número escolhido é inválido. Tente novamente.')
