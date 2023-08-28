# Exercício 41
# A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 20 anos: SÊNIOR
# - Acima: MASTER

from datetime import date
data = date.today().year

ano = int(input('Ano de nacimento: '))
idade = data - ano

if idade <= 9:
    print('O atleta tem {} anos, logo faz parte da categoria Mirím'.format(idade))
elif (idade > 9) and (idade <= 14):
    print('O atleta tem {} anos, logo faz parte da categoria Infantil'.format(idade))
elif (idade > 14) and (idade <= 19):
    print('O atleta tem {} anos, logo faz parte da categoria Júnior'.format(idade))
elif idade == 20:
    print('O atleta tem {} anos, logo faz parte da categoria Sênior'.format(idade))
else:
    print('O atleta tem {} anos, logo faz parte da categoria Master'.format(idade))
