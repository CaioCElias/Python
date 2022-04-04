# Refaça o EXERCÍCIO 051, lendo o primeiro termo e a razão de uma PA, mostrando
# os 10 primeiros termos da progressão usando a estrutura while.
primeiro = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
cont = 0
while cont < 10:
    print(primeiro, end=' → ')
    primeiro += razao
    cont += 1
print('FIM')
