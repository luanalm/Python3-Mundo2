# Desenvolva um programa que leia o primeiro termo e a razão de uma Progressão Aritimética. No final, mostre os dez primeiros termos dessa progressão.

a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
an = 0

for n in range(1, 11):
    an = a1 + (n-1)*r
    print(an, end=' ')
