# Exercício 45
# Crie um programa que faça o computador jogar Jokenpô com você.
import random

result = random.randint(1,3)
jog = int(input('''Vamos jogar Jokenpô! Escolha sua jogada.
[ 1 ] Pedra.
[ 2 ] Papel.
[ 3 ] Tesoura.
Digite o número da jogada escolhida: '''))

if jog == 1:
    if result == 1:
        print('''Pedra x Pedra
              Ocorreu um empate.''')
    elif result == 2:
        print('''Papel x Pedra
              Que pena, você perdeu.''')
    elif result == 3:
        print('''Tesoura x Pedra
              Parabéns, você ganhou!''')
elif jog == 2:
    if result == 1:
        print('''Pedra x Papel
              Parabéns, você ganhou!''')
    elif result == 2:
        print('''Papel x Papel
              Ocorreu um empate.''')
    elif result == 3:
        print('''Tesoura x Papel
              Que pena, você perdeu''')
elif jog == 3:
    if result == 1:
        print('''Tesoura x Pedra
              Que pena, você perdeu.''')
    elif result == 2:
        print('''Tesoura x Papel
              Parabéns, você ganhou!''')
    elif result == 3:
        print('''Tesoura x Tesoura
              Ocorreu um empate.''')
else:
    print('O número escolhido é inválido. Tente novamente.')

