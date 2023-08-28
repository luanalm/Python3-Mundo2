# Faça um programa que calcule a soma entre todos os números impares que são multiplos de três e que se encontram no intervalo de 1 até 500.
s = 0
for n in range(1,501,3):
    if n % 2 == 0:
        n = n - n
    else:
        s += n
print(s)
