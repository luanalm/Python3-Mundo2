# Faça um programa que mostre uma contagem regrassiva para o estouro de fogos de artifício, indo de 10 até 0, com uma pausa de 1 segundo entre eles.

import time

for x in range(10,-1,-1):
    print(x)
    time.sleep(1)

print('🎆 FELIZ ANO NOVO!!!!! 🎆')
