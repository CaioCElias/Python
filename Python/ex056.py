# Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. No final do programa, mostre:
# - A média de idade do grupo.
# - Qual é o nome do homem mais velho.
# - Quantas mulheres têm menos de 20 anos.

media = 0
velho = 0
nomevelho = 0
cont = 0

for p in range(1, 5):
    print(f'----- {p}ª PESSOA -----')
    nome = str(input('Nome: ')).title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).upper()
    media += idade
    if 'M' in sexo:
        if velho < idade:
            velho = idade
            nomevelho = nome
    elif 'F' in sexo:
        if idade < 20:
            cont += 1

if velho == 0 and nomevelho == 0:
    print('\nNão há homens na lista')
else:
    print(f'\nO homem mais velho tem {velho} anos e se chama {nomevelho}')

print(f'A média de idade do grupo é de {media/4} anos')
print(f'Ao todo são {cont} mulher(es) com menos de 20 anos')
