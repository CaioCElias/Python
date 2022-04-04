# Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade,
# se ele ainda vai se alistar ao serviço militar, se é a hora de se alistar, ou se já passou
# do tempo do alistamento. Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
ano = int(input('Ano de nascimento: '))
from datetime import date
atual = date.today().year
idade = atual - ano
print(f'Quem nasceu em {ano} tem {idade} ano(s) em {atual}')
if idade == 18:
    print('Vá se alistar!')
elif idade < 18:
    tempo = 18 - idade
    print(f'Falta(m) {tempo} ano(s) para o alistamento')
    print(f'Seu alistamento será em {atual + tempo}')
elif idade > 18:
    tempo = idade - 18
    print(f'Você deveria ter se alistado há {tempo} ano(s)')
    print(f'Seu alistamento foi em {atual - tempo}')
