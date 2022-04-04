# A Confederação Nacional de Natação precisa de um programa que leia o ano
# de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
# - Até 9 anos: MIRIM
# - Até 14 anos: INFANTIL
# - Até 19 anos: JUNIOR
# - Até 25 anos: SÊNIOR
# - Acima: MASTER
ano = int(input('Ano de Nascimento: '))
from datetime import date
idade = date.today().year - ano
print(f'O atleta tem {idade} anos')
if idade <= 9:
    classificacao = 'Mirim'
elif idade <= 14:
    classificacao = 'Infantil'
elif idade <= 19:
    classificacao = 'Junior'
elif idade <= 25:
    classificacao = 'Sênior'
elif idade > 25:
    classificacao = 'Master'
print(f'Classificação: {classificacao}')
