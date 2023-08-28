# Mostre a tabuáda do número que o usuário escolher, utilizando o laço for

tab = int(input('Escolha o número da tabuáda desejada: '))

for x in range(0,11):
    y = tab * x
    print('{} x {} = {}'.format(tab, x, y))
