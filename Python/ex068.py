# Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o
# jogador PERDER, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

# Decoracao
print('=-' * 15)
print('VAMOS JOGAR PAR OU IMPAR')
print('=-' * 15)

# Importando
from random import randint
count = 0

while True:
    jogador = int(input('Diga um valor: '))
    escolha = ' '
    while escolha not in 'PI':
        escolha = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    computador = randint(0, 10)
    soma = jogador + computador
    print('-'*30)
    print(f'Você jogou {jogador} e o computador {computador}. Total de {soma}. ', end='')
    print('Deu par' if soma % 2 == 0 else 'Deu impar')
    print('-'*30)
    if escolha == 'P':
        if soma % 2 == 0:
            print('VOCÊ VENCEU!')
            print('-' * 30)
            count += 1
        if soma % 2 != 0:
            print('VOCÊ PERDEU!')
            break
    if escolha == 'I':
        if soma % 2 != 0:
            print('VOCÊ VENCEU!')
            print('-' * 30)
            count += 1
        if soma % 2 == 0:
            print('VOCÊ PERDEU!')
            break
    print('Vamos jogar novamente...')
# Fim de jogo
print('=-'*15)
print(f'GAME OVER! Você venceu {count} vezes')

