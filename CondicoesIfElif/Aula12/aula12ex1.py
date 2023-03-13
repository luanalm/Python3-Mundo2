# Exercício 36
# Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa. O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o empréstimo será negado.

print('Vamos ver se seu empréstimo será aprovado!')
val1 = float(input('Valor da casa: R$'))
sal = float(input('Valor do seu salário mensal: R$'))
ano = int(input('Anos que levará para pagar: '))

mes = ano * 12
val = val1 / mes
limite = 0.3 * sal

if val <= limite :
    print('O empréstimo para a compra da casa no valor total de R${:.2f} será aprovado! Você deverá pagar {:.2f} prestações no valor de R${:.2f}.'.format(val1, mes, val))
else:
    print('O emrpéstimo para a compra da casa no valor total de R${:.2f} não será aprovada! Pois o valor das prestações seria de R${:.2f}, que é um valor maior do que 30 por cento de seu salário. O valor limite para as prestações mensais, com seu salário atual seria de R${:.2f}.'.format(val1, val, limite))
