# Crie um programa que leia o nome de uma pessoa e diga se ela tem "SILVA" no nome.
nome = input('Qual seu nome completo? ').strip().title()
resposta = 'Silva' in nome
import time
print('Seu nome tem Silva?')
print('Analisando...')
time.sleep(3)
if resposta == True:
    print('Sim')
else:
    print('Não')
