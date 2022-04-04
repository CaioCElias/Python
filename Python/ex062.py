# Melhore o EXERCÍCIO 061, perguntando para o usuário se ele quer mostrar mais alguns termos.
# O programa encerra quando ele disser que quer mostrar 0 termos.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
total = 0
mais = 10
while mais != 0:
    total += mais
    while cont < total:
        print(f'{primeiro} → ', end='')
        primeiro += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quer mostrar mais quantos termos? '))
print(f'O programa foi finalizado com {total} termos')
