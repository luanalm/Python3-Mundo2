# Desenvolva um programa que leia seis números inteiros e mostre a soma apenas daqueles que forem pares. Se o valor digitado for impar, desconsidere-o.
s = 0
for x in range(0, 6):
    n = int(input('Digite um número: '))
    if n % 2 == 0:
        s += n
    else:
        n = n - n
print(s)
