'''
Crie um programa que simule o funcionamento de um caixa eletrônico. No início, pergunte ao
usuário qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas
cédulas de cada valor serão entregues.
OBS: Considere que o caixa possui cédulas de R$ 50, R$ 20, R$ 10 e R$ 1.
'''

print('=' * 30)
print(f'{"BANCO CEV":^30}')
print('=' * 30)

valor = int(input('Que valor que você quer sacar? R$'))

total = valor

cedulaAtual = 50
qntdCedula = 0

while True:
    if total >= cedulaAtual:
        total -= cedulaAtual
        qntdCedula += 1
    else:
        if qntdCedula > 0:
            print(f'{qntdCedula} cédulas de R${cedulaAtual}')
        if cedulaAtual == 50:
            cedulaAtual = 20
        elif cedulaAtual == 20:
            cedulaAtual = 10
        elif cedulaAtual == 10:
            cedulaAtual = 1
        qntdCedula = 0
        if total == 0:
            break

print('=' * 30)
print('Volte sempre.')
