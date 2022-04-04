# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5
# e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
# O programa deverá escrever na tela se o usuário venceu ou perdeu.
print('=X'*30)
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
print('=X'*30)
print(' ')

# Gerar um número aleatório
from random import randint
num = randint(0, 5)
resposta = int(input(f'Em que número eu pensei? '))

if resposta == num:
    print('Parabéns, Resposta Correta!')

elif resposta < 0:
    print('Número inváldo')

elif resposta > 5:
    print('Número inváldo')

elif resposta != num:
    print(f'Resposta Incorreta! O número era {num}')