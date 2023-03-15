# Exercício 40
# Crie um programa que leia duas notas de um aluno e calcule sua média, mostrando uma mensagem no final, de acordo com a média atingida:
# - Média abaixo de 5,0: REPROVADO
# - Média entre 5,0 e 6,9: RECUPERAÇÃO
# Média 7,0 ou superior: APROVADO

x = float(input('Primeira nota: '))
y = float(input('Segunda nota: '))

med = (x + y)/2

if med < 5.0:
    print('Reprovado.')
elif (med >= 5.0) and (med < 7):
    print('Recuperação.')
elif med >= 7:
    print('Aprovado.')
