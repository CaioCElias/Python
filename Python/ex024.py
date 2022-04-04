# Crie um programa que leia o nome de uma cidade e diga se ela começa ou não com o nome "SANTO".
cidade = input('Em que cidade você nasceu? ').strip().upper().split()
print('Você mora em uma cidade que começa com Santo?')
if cidade[0] == 'SANTO':
    print('SIM')
else:
    print('NÃO')
