# Melhore o jogo do EXERCÍCIO 028 onde o computador vai "pensar" em um número entre 0 e 10.
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos
# palpites foram necessários para vencer.

# Apresentação do jogo
print('Sou seu computador...\nAcabei de pensar em um número inteiro entre 0 e 10.')
print('Será que você consegue adivinhar qual foi?')

# Importanto um número aleatório
from random import randint
computador = randint(0, 10)

# Jogo
cont = 0
jogador = -1
while jogador != computador:
    cont += 1
    jogador = int(input('Qual seu palpite? '))
    if jogador > computador:
        print('Número muito alto, tente um menor')
    elif jogador < computador:
        print('Número muito baixo, tente um maior')
print(f'Parabéns, você adivinhou o número na {cont}ª tentativa')
