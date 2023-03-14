# Exercício 38
# Escreva um programa que leia dois números inteiros e compare-os, mostrando na tela uma mensagem:
# - O primeiro valor é maior
# - O segundo valor é maior
# - Não existe valor maior, os dois são iguais

x = int(input('Escreva um valor: '))
y = int(input('Escreva outro valor: '))

if x > y:
    print('O número {} é maior que o número {}.'.format(x, y))
elif y > x:
    print('O número {} é maior que o número {}.'.format(y, x))
else:
    print('O número {} é igual ao número {}.'.format(x, y))

