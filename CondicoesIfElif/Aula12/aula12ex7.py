# Exercício 42
# Refaça o EXERCÍCIO 35 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo será formado:
# - Equilátero: todos os lados iguais
# - Isósceles: dois lados iguais
# - Escaleno: todos os lados diferentes

a = int(input('Primeiro lado: '))
b = int(input('Segundo lado: '))
c = int(input('Terceiro lado: '))

if (b + c > a) and (a + c > b) and (a + b > c):
    if (a == b) and (b == c):
        print('O triângulo é equilátero.')
    elif (a == b and a != c) or (b == c and b != a) or (c == a and c != b):
        print('O triângulo é isósceles.')
    else:
        print('O triângulo é escaleno.')
else:
    print('Os lados não formam um triângulo.')
