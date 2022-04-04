# Crie um programa que faça o computador jogar Jokenpô com você.

# Aqui o jogador escolhe sua jogada
print('Suas opções:')
print('''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura''')
jogador = int(input('Qual é sua jogada? '))

# Timer para deixar o programa mais interativo
import time
print('JO')
time.sleep(1)
print('KEN')
time.sleep(1)
print('PÔ')
time.sleep(1)

# Aqui é a escolha do computador
from random import randint
computador = randint(1, 3)

if computador == 1:
    print('O computador escolheu PEDRA!')
elif computador == 2:
    print('O computador escolheu PAPEL!')
elif computador == 3:
    print('O computador escolheu TESOURA!')


# Aqui são as opções que vão acontecer segundo a escolha do jogador em relação ao computador
if jogador == 1:
    print('Você escolheu PEDRA!')
    if computador == 1:
        print('EMPATE!')
    elif computador == 2:
        print('VOCÊ PERDEU!')
    elif computador == 3:
        print('VOCÊ GANHOU!')
elif jogador == 2:
    print('Você escolheu PAPEL!')
    if computador == 1:
        print('VOCÊ GANHOU!')
    elif computador == 2:
        print('EMPATE!')
    elif computador == 3:
        print('VOCÊ PERDEU!')
elif jogador == 3:
    print('Você escolheu TESOURA!')
    if computador == 1:
        print('VOCÊ PERDEU!')
    elif computador == 2:
        print('VOCÊ GANHOU!')
    elif computador == 3:
        print('EMPATE!')
else:
    print('Digite um numero válido!')
