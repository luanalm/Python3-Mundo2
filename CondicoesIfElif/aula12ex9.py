# Exercício 44
# Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e condição de pagamento:
# - À vista dinheiro/cheque: 10% de desconto
# - À vista no cartão: 5% de desconto
# - Até 2x no cartão: preço normal
# - 3x ou mais no cartão: 20% de juros

vnor = float(input('Insira o preço do produto: '))
pag = int(input('''Escolha uma forma de pagamento.
[ 1 ] À vista com dinheiro ou cheque.
[ 2 ] À vista no cartão.
[ 3 ] Até 2x no cartão.
[ 4 ] 3x ou mais no cartão.
Digite o número referente a sua escolha: '''))

if pag == 1:
    val = vnor - (vnor * 0.1)
    print('Você recebeu um desconto de 10%. Sendo assim, o valor a ser pago de R${:.2f}.'.format(val))
elif pag == 2:
    val = vnor - (vnor * 0.05)
    print('Você recebeu um desconto de 5%. Sendo assim, o valor a ser pago é R${:.2f}.'.format(val))
elif pag == 3:
    print('O valor a ser pago é R${:.2f}.'.format(vnor))
elif pag == 4:
    val = vnor + (vnor * 0.2)
    print('Será cobrada uma taxa de juros de 20%. Sendo assim, o valor total a ser pago é R${:.2f}.'.format(val))
else:
    print('O número escolhido não é válido. Tente novamente.')
