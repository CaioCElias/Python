# Crie um programa que leia dois valores e mostre um menu como o abaixo na tela:
# [ 1 ] Somar
# [ 2 ] Multiplicar
# [ 3 ] Maior
# [ 4 ] Novos Números
# [ 5 ] Sair do Programa
from time import sleep
num1 = int(input('Primeiro valor: '))
num2 = int(input('Segundo valor: '))
escolha = 0
while escolha != 5:
    sleep(2)
    print('=X=X=X=X=X=X=X=X=X=X')
    print('''[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa''')
    escolha = int(input('>>>> Qual é a sua escolha? '))
    if escolha == 1:
        print(f'\033[1;31m{num1} + {num2} = {num1+num2}\033[m')
    elif escolha == 2:
        print(f'\033[1;31m{num1} x {num2} = {num1*num2}\033[m')
    elif escolha == 3:
        if num1 > num2:
            print(f'\033[1;31mEntre {num1} e {num2}, o maior é {num1}\033[m')
        elif num1 < num2:
            print(f'\033[1;31mEntre {num1} e {num2}, o maior é {num2}\033[m')
        elif num1 == num2:
            print(f'\033[1;31mO número {num1} e {num2} têm o mesmo valor\033[m')
    elif escolha == 4:
        num1 = int(input('Primeiro valor: '))
        num2 = int(input('Segundo valor: '))
    elif escolha == 5:
        print('\033[1;31mFinalizando...\033[m')
        sleep(2)
        print('\033[1;31mPrograma finalizado.\033[m')
