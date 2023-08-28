# Exercício 39
# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
# - Se ele ainda vai se alistar ao serviço militar.
# - Se é a hora de se alistar.
# - Se já passou do tempo do alistamento.
# Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
data = date.today().year

a = int(input('Ano de nascimento: '))
idade = data - a

if idade < 18:
    x = 18 - idade
    print('Ainda faltam {} anos para que você precise se alistar.'.format(x))
elif idade == 18:
    print('Você precisa se alistar imediatamente!')
else:
    x = idade - 18
    print('Você deveria ter se alistado há {} anos atrás.'.format(x))
