from random import randint
from time import sleep

itens = ('pedra', 'papel', 'tesoura')
jose = randint(0, 2)
andre = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print("PÔÔÔ!!!")
sleep(1)
print('-=' * 12)
print('o José escolheu {}'.format(itens[jose]))
print('-=' * 12)
print('O André escolheu {}'.format(itens[andre]))
print('-=' * 12)

if jose == 0:  # JOGOU PEDRA
    if andre == 0:
        print('EMPATE')
    elif andre == 1:
        print('André venceu')
    elif andre == 2:
        print('José Venceu')

elif jose == 1:
    if andre == 0:
        print('José Venceu')
    elif andre == 1:
        print('EMPATE')
    elif andre == 2:
        print('André Venceu')
elif jose == 2:  # JOGOU TESOURA
    if andre == 0:
        print('André Venceu')
    elif andre == 1:
        print('José Venceu')
    elif andre == 2:
        print('EMPATE')
